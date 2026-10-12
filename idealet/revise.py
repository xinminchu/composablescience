"""修正 (correction): component versioning for the Idealet graph.

A revised component becomes a NEW node; the old node is kept and linked
by a `supersedes` edge. Nothing is ever overwritten: the graph holds the
full history, and `snapshot` resolves the "current consensus" view.

Usage:
    python3 idealet/revise.py revise --graph idealet/graph.json \\
        --component <component-id> --text-file revised.txt \\
        --note "fixed the attention formula" --agent "sam"
    python3 idealet/revise.py snapshot --graph idealet/graph.json \\
        -o idealet/graph-current.json
"""

import argparse
import copy
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save(g, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(g, f, ensure_ascii=False, indent=1)


def revise(g, component_id, new_text, note="", agent=""):
    nodes = g["nodes"]
    base = next((n for n in nodes
                 if n.get("@type") == "ScholarlyComponent"
                 and n["@id"] == component_id), None)
    if base is None:
        # maybe an old version id was given: resolve to its lineage head
        base = next((n for n in nodes
                     if n.get("@type") == "ScholarlyComponent"
                     and n.get("lineage") == component_id), None)
        if base is None:
            raise ValueError(f"component not found: {component_id}")
        # find latest of that lineage
        lineage = base["lineage"]
        versions = [n for n in nodes
                    if n.get("@type") == "ScholarlyComponent"
                    and n.get("lineage") == lineage]
        base = max(versions, key=lambda n: n.get("version", 1))
        lineage = base["lineage"]
    else:
        lineage = base.get("lineage", base["@id"])
    versions = [n for n in nodes
                if n.get("@type") == "ScholarlyComponent"
                and n.get("lineage") == lineage]
    v = max(n.get("version", 1) for n in versions) + 1
    new_id = f"{lineage}@v{v}"
    node = copy.deepcopy(base)
    node["@id"] = new_id
    node["version"] = v
    node["lineage"] = lineage
    node["text"] = new_text
    node["revisionNote"] = note
    node["revisedBy"] = agent
    # rewire: edges that pointed at the old head now point at the new head,
    # except history edges (supersedes) which stay.
    old_head = max(versions, key=lambda n: n.get("version", 1))["@id"]
    for e in g["edges"]:
        if e.get("@type") == "supersedes":
            continue
        if e.get("to") == old_head:
            e["to"] = new_id
        if e.get("from") == old_head and e.get("@type") == "hasComponent":
            e["to"] = new_id
    g["edges"].append({"@type": "supersedes", "from": new_id, "to": old_head,
                       "note": note, "agent": agent})
    nodes.append(node)
    return new_id


def snapshot(g):
    """Return the current-consensus view: latest version per lineage."""
    latest = {}
    for n in g["nodes"]:
        if n.get("@type") != "ScholarlyComponent":
            continue
        lin = n.get("lineage", n["@id"])
        if lin not in latest or n.get("version", 1) > latest[lin].get("version", 1):
            latest[lin] = n
    keep_ids = {n["@id"] for n in g["nodes"]
                if n.get("@type") != "ScholarlyComponent"}
    keep_ids |= set(latest)
    nodes = [n for n in g["nodes"] if n["@id"] in keep_ids]
    edges = [e for e in g["edges"]
             if e.get("@type") == "supersedes"
             or (e.get("from") in keep_ids and e.get("to") in keep_ids)]
    return {"nodes": nodes, "edges": edges,
            "meta": {"view": "current-snapshot",
                     "n_lineages": len(latest)}}


def main():
    ap = argparse.ArgumentParser(description="Revise a component (versioning).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("revise")
    r.add_argument("--graph", required=True)
    r.add_argument("--component", required=True)
    r.add_argument("--text-file", required=True)
    r.add_argument("--note", default="")
    r.add_argument("--agent", default="")
    s = sub.add_parser("snapshot")
    s.add_argument("--graph", required=True)
    s.add_argument("-o", "--output", required=True)
    args = ap.parse_args()

    if args.cmd == "revise":
        g = load(args.graph)
        with open(args.text_file, encoding="utf-8") as f:
            text = f.read()
        new_id = revise(g, args.component, text, args.note, args.agent)
        save(g, args.graph)
        print(f"revised -> {new_id} (history kept, supersedes edge added)")
    else:
        g = load(args.graph)
        snap = snapshot(g)
        save(snap, args.output)
        print(f"snapshot: {snap['meta']['n_lineages']} lineages -> {args.output}")


if __name__ == "__main__":
    main()
