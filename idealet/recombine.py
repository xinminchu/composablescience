"""重组 (recombination): generate a paper from modules.

Picks components (resolved to their current versions) and emits a new
ScholarlyArticle whose hasComponent edges point at them -- the
"module -> paper" direction of the Idealet vision. The new article
records its provenance (which components, which versions, who composed).

Usage:
    python3 idealet/recombine.py --graph idealet/graph.json \\
        --pick <id1> <id2> ... --title "A survey of ..." \\
        --agent "sam" -o idealet/recombined-survey.json
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def current_of(g, cid):
    """Resolve a component id (or lineage) to its latest version."""
    nodes = [n for n in g["nodes"]
             if n.get("@type") == "ScholarlyComponent"]
    lin = next((n.get("lineage", n["@id"]) for n in nodes
                if n["@id"] == cid or n.get("lineage") == cid), cid)
    versions = [n for n in nodes if n.get("lineage", n["@id"]) == lin]
    if not versions:
        raise ValueError(f"component not found: {cid}")
    return max(versions, key=lambda n: n.get("version", 1))


def main():
    ap = argparse.ArgumentParser(description="Recombine modules into a paper.")
    ap.add_argument("--graph", required=True)
    ap.add_argument("--pick", nargs="+", required=True,
                    help="component ids (or lineages); resolved to current versions")
    ap.add_argument("--title", required=True)
    ap.add_argument("--agent", default="")
    ap.add_argument("-o", "--output", required=True)
    args = ap.parse_args()

    g = load(args.graph)
    chosen = [current_of(g, cid) for cid in args.pick]
    slug = "recombined-" + re.sub(r"[^a-z0-9]+", "-",
                                  args.title.lower()).strip("-")[:40]
    aid = f"idealet:{slug}"
    article = {
        "@id": aid,
        "@type": "ScholarlyArticle",
        "schema:name": args.title,
        "hasComponent": [{"@id": c["@id"]} for c in chosen],
        "composedOf": [{"component": c["@id"],
                        "version": c.get("version", 1),
                        "lineage": c.get("lineage", c["@id"])}
                       for c in chosen],
        "composedBy": args.agent,
        "provenance": ("recombined from Idealet components; each keeps its "
                       "own version history and citation edges"),
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump({"@graph": [article] + chosen}, f,
                  ensure_ascii=False, indent=1)
    vers = ", ".join(f"{c['@id'].split('/')[-1]}"
                     for c in chosen)
    print(f"composed {aid} from {len(chosen)} components [{vers}]\n-> {args.output}")


if __name__ == "__main__":
    main()
