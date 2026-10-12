"""Entity mention extraction + cross-paper alignment (baseline v0.1).

Baseline approach (stdlib-only, deterministic):
  1. Candidates: quoted terms + Title-Case phrases (2-4 words) from
     component texts, minus stopwords / section-header noise.
  2. Alignment: normalized lowercase form is the entity key; surface
     forms become aliases. NIL = first-seen mention mints the entity.
  3. Kind heuristic: cue words -> Method / Dataset / Concept.

Emits ResearchEntity nodes + EntityMention edges using the schema.org /
scomp vocabulary already present in schema/context.jsonld.
Roadmap: LLM-assisted extraction with human review; NIL clustering.
"""

import re

_STOP = {
    "the", "a", "an", "of", "in", "on", "for", "with", "and", "or",
    "to", "we", "our", "this", "that", "these", "those", "as", "by",
    "from", "is", "are", "was", "were", "be", "been", "it", "its",
    "at", "which", "their", "they", "he", "she", "you", "i",
    "et", "al", "fig", "table", "section", "figure", "arxiv",
}

_METHOD_CUES = {"model", "network", "transformer", "attention", "layer",
                "encoder", "decoder", "architecture", "mechanism", "method",
                "approach", "algorithm", "module"}
_DATASET_CUES = {"dataset", "corpus", "benchmark", "squad", "glue",
                 "wmt", "corpus", "treebank"}


def _norm(s):
    return re.sub(r"\s+", " ", s.strip().lower())


def extract_mentions(text):
    """Return a list of (surface, kind_hint) candidate mentions."""
    text = text or ""
    cands = []
    # 1) quoted terms: "..." / '...'
    for m in re.finditer(r'"([^"]{3,60})"|\'([^\']{3,60})\'', text):
        surf = m.group(1) or m.group(2)
        if len(surf.split()) <= 6:
            cands.append(surf.strip())
    # 2) Title-Case phrases of 2-4 words
    for m in re.finditer(r"\b([A-Z][a-zA-Z0-9\-]+(?:\s+[A-Z][a-zA-Z0-9\-]+){1,3})\b", text):
        surf = m.group(1)
        words = surf.split()
        if any(w.lower() in _STOP for w in words):
            continue
        if len(surf) < 5:
            continue
        cands.append(surf)
    # dedupe, keep order
    seen, out = set(), []
    for c in cands:
        k = _norm(c)
        if k not in seen and len(k) >= 4:
            seen.add(k)
            out.append(c)
    return out


def kind_of(surface):
    low = surface.lower()
    if any(w in low for w in _DATASET_CUES):
        return "Dataset"
    if any(w in low for w in _METHOD_CUES):
        return "Method"
    return "Concept"


def align(all_mentions):
    """all_mentions: {component_id: [surface, ...]}.

    Returns (entities, mentions) where entities is a list of
    {"@id", "canonicalName", "aliases", "entityKind"} and mentions is a
    list of {"component": id, "entity": id, "surfaceForm": surface}.
    Entity ids are stable: entity/<slugified-canonical>.
    """
    key_to_ent = {}
    mentions = []
    order = 0
    for comp_id, surfs in all_mentions.items():
        for surf in surfs:
            key = _norm(surf)
            if key in _STOP or len(key) < 4:
                continue
            ent = key_to_ent.get(key)
            if ent is None:
                slug = re.sub(r"[^a-z0-9]+", "-", key).strip("-")[:48]
                ent = {
                    "@id": f"idealet:entity/{slug or 'e' + str(order)}",
                    "@type": "ResearchEntity",
                    "canonicalName": surf,
                    "aliases": [],
                    "entityKind": kind_of(surf),
                    "extractionMethod": "rule-based",
                }
                key_to_ent[key] = ent
                order += 1
            if surf not in ent["aliases"] and surf != ent["canonicalName"]:
                ent["aliases"].append(surf)
            mentions.append({
                "@type": "EntityMention",
                "component": comp_id,
                "entity": ent["@id"],
                "surfaceForm": surf,
            })
    # keep entities that are mentioned in >= 2 components (alignment signal)
    from collections import Counter
    cnt = Counter(m["entity"] for m in mentions)
    entities = [e for e in key_to_ent.values() if cnt[e["@id"]] >= 2]
    keep = {e["@id"] for e in entities}
    mentions = [m for m in mentions if m["entity"] in keep]
    return entities, mentions
