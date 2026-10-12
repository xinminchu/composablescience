"""Build the Idealet graph from component JSON-LD files (baseline v0.1).

生长 (growth): new papers' components join the graph; citation edges are
mined between papers with rule-based intent classification.
修正 (correction): see revise.py (versions + supersedes edges).
重组 (recombination): see recombine.py (module -> paper generation).

Usage:
    python3 idealet/graph.py --inputs examples/a.jsonld examples/b.jsonld \\
        -o idealet/graph.json

Output graph.json: {"nodes": [...], "edges": [...]} with @type terms from
the scomp vocabulary. Citation mining is heuristic and records its
method + confidence; hand-annotated ComponentCitation edges in the
inputs are preserved as-is (gold).
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from idealet.intent import classify_intent, split_sentences  # noqa: E402
from idealet.entities import extract_mentions, align  # noqa: E402

STOP = {"the", "a", "an", "of", "in", "on", "for", "with", "and", "or",
        "to", "is", "are", "we", "our", "this", "that", "as", "by",
        "from", "it", "its", "at", "which", "their", "they", "based",
        "using", "via", "deep", "large", "base", "model", "models",
        "paper", "work", "neural", "novel", "pre-training", "fine-tuning",
        "state", "art"}

# intent -> preferred target component type in the cited paper
INTENT_TARGET = {
    "usesMethodIn": "MethodStrategy",
    "extends": "MethodStrategy",
    "confirms": "ProcessResults",
    "critiques": "ProcessResults",
    "background": "MotivationProblem",
    "reuses": "MethodStrategy",
}


def load_inputs(paths):
    articles, components, hand_cites = {}, {}, []
    for p in paths:
        with open(p, encoding="utf-8") as f:
            g = json.load(f).get("@graph", [])
        for n in g:
            t = n.get("@type", "")
            if t == "ScholarlyArticle":
                articles[n["@id"]] = n
            elif t == "ScholarlyComponent":
                components[n["@id"]] = n
            elif t == "ComponentCitation":
                hand_cites.append(n)
    return articles, components, hand_cites


def _slug_of(article_id):
    m = re.search(r"/(arxiv-[^/]+)$", article_id)
    return m.group(1) if m else article_id.rsplit("/", 1)[-1]


def paper_aliases(article):
    """Keywords that identify a paper in other papers' prose."""
    slug = _slug_of(article["@id"])
    aliases = set()
    m = re.search(r"(\d{4}\.\d{4,5})", slug)
    if m:
        aliases.add(m.group(1))
    name = article.get("schema:name") or article.get("name") or ""
    for w in re.findall(r"[A-Za-z][A-Za-z0-9\-]{3,}", name):
        if w.lower() not in STOP:
            aliases.add(w.lower())
    # author surnames are the strongest cross-paper signal when present
    for c in article.get("contributors", []) or []:
        nm = c.get("name") if isinstance(c, dict) else None
        if nm:
            aliases.add(nm.split()[-1].lower())
    return {a for a in aliases if len(a) >= 4}


def _has_cite_evidence(sent):
    # skip table-like text: mostly numbers / brackets, little prose
    alpha = len(re.sub(r"[^A-Za-z]", "", sent))
    if alpha < len(sent) * 0.45:
        return False
    return bool(re.search(r"et al\.?|\b(19|20)\d{2}\b|\[\d+\]|proposed by|"
                          r"introduced by|proposed in|shown in", sent, re.I))


def mine_citations(components, articles):
    """Mine (source_comp -> cited_paper) citation sentences."""
    comp_paper = {}
    for cid, c in components.items():
        for aid, a in articles.items():
            if cid.startswith(aid + "/"):
                comp_paper[cid] = aid
                break
    aliases = {aid: paper_aliases(a) for aid, a in articles.items()}
    mined = []
    for cid, c in components.items():
        src_paper = comp_paper.get(cid)
        text = c.get("schema:text") or c.get("text") or ""
        for sent in split_sentences(text):
            slow = sent.lower()
            for aid, als in aliases.items():
                if aid == src_paper:
                    continue  # no self-citation mining
                hit = next((a for a in als if a in slow), None)
                if hit and _has_cite_evidence(sent):
                    intent, conf, cue = classify_intent(sent)
                    mined.append({
                        "source": cid,
                        "cited_paper": aid,
                        "context": sent[:500],
                        "intent": intent,
                        "confidence": round(conf * 0.9, 2),
                        "cue": cue,
                        "alias_hit": hit,
                    })
                    break
    return mined


def pick_target(components, cited_paper, intent):
    """Heuristic: intent -> most relevant component of the cited paper."""
    want = INTENT_TARGET.get(intent, "MotivationProblem")
    cands = [cid for cid, c in components.items()
             if cid.startswith(cited_paper + "/")
             and c.get("componentType") == want]
    if cands:
        return sorted(cands, key=lambda x: components[x].get("order", 0))[0]
    same = [cid for cid in components if cid.startswith(cited_paper + "/")]
    if same:
        return sorted(same, key=lambda x: components[x].get("order", 0))[0]
    return cited_paper


def build(paths):
    articles, components, hand_cites = load_inputs(paths)

    nodes, edges = [], []
    for aid, a in articles.items():
        nodes.append({"@id": aid, "@type": "ScholarlyArticle",
                      "name": a.get("schema:name") or a.get("name"),
                      "slug": _slug_of(aid)})
    for cid, c in components.items():
        nodes.append({"@id": cid, "@type": "ScholarlyComponent",
                      "componentType": c.get("componentType"),
                      "name": c.get("schema:name") or c.get("name"),
                      "order": c.get("order", 0),
                      "version": 1,
                      "lineage": cid,
                      "text": (c.get("schema:text") or c.get("text") or "")[:2000]})
        edges.append({"@type": "hasComponent", "from": _paper_of(cid, articles),
                      "to": cid})
    # hand-annotated citations first (gold)
    seen_pairs = set()
    for h in hand_cites:
        s = _ref(h.get("sourceComponent"))
        t = _ref(h.get("targetComponent"))
        edges.append({"@type": "cites", "from": s, "to": t,
                      "intent": h.get("citationIntent", "background"),
                      "context": h.get("citationContext", "")[:500],
                      "method": "hand-annotated", "confidence": 1.0})
        seen_pairs.add((s, t))
    # mined citations
    for m in mine_citations(components, articles):
        tgt = pick_target(components, m["cited_paper"], m["intent"])
        if (m["source"], tgt) in seen_pairs:
            continue
        seen_pairs.add((m["source"], tgt))
        edges.append({"@type": "cites", "from": m["source"], "to": tgt,
                      "intent": m["intent"], "context": m["context"],
                      "method": "rule-based", "confidence": m["confidence"],
                      "note": ("heuristic target: intent->%s component; "
                               "alias '%s'") % (INTENT_TARGET.get(m["intent"]),
                                                m["alias_hit"])})
    # entities (alignment across components/papers)
    mentions_in = {cid: extract_mentions(
        (components[cid].get("schema:text") or "")) for cid in components}
    entities, mentions = align(mentions_in)
    nodes.extend(entities)
    for m in mentions:
        edges.append({"@type": "mentions", "from": m["component"],
                      "to": m["entity"], "surfaceForm": m["surfaceForm"]})
    return {"nodes": nodes, "edges": edges,
            "meta": {"method": "idealet/graph.py v0.1 (rule-based baseline)",
                     "n_inputs": len(paths)}}


def _ref(v):
    return v.get("@id") if isinstance(v, dict) else v


def _paper_of(cid, articles):
    for aid in articles:
        if cid.startswith(aid + "/"):
            return aid
    return None


def main():
    ap = argparse.ArgumentParser(description="Build the Idealet graph.")
    ap.add_argument("--inputs", nargs="+", required=True)
    ap.add_argument("-o", "--output", required=True)
    args = ap.parse_args()
    g = build(args.inputs)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(g, f, ensure_ascii=False, indent=1)
    n_cite = sum(1 for e in g["edges"] if e["@type"] == "cites")
    n_ent = sum(1 for n in g["nodes"] if n["@type"] == "ResearchEntity")
    print(f"nodes={len(g['nodes'])} edges={len(g['edges'])} "
          f"citations={n_cite} entities={n_ent} -> {args.output}")


if __name__ == "__main__":
    main()
