# ComposableScience — from articles to components

ComposableScience decomposes scholarly articles into **typed, addressable, citable
components** (motivation, review, method, results, conclusions, artifacts),
links components with **semantic citation edges**, and resolves entity
mentions across papers — so contribution can be measured at a finer
granularity than the article.

> **Note:** this repository was formerly named **ScholComp**. The ScholComp
> paper and v0.1 demo below remain intact; the new name reflects the broader
> direction — *composable science*.

This repository is the **public demo companion** to the paper
*"From Articles to Components: Building a Component-Level Citation Graph
for Scholarly Communication"* (in preparation).

## What works today (v0.1 demo)

- **Schema** (`schema/`): JSON-LD context + six component types (A–F),
  compatible with schema.org / CiTO / CRediT by design.
- **Segmenter** (`segmenter/`): deterministic, stdlib-only baseline that
  splits an article into sections, classifies each into A–F, and emits
  JSON-LD with stable URIs and provenance. No API keys, no network
  (except an optional `--url` fetch).
- **Viewer** (`viewer/`): dependency-free page that renders the components
  and the component graph from the emitted JSON-LD.
- **Example** (`examples/`): *"Attention Is All You Need"*
  (arXiv:1706.03762) decomposed into 9 components + 2 hand-annotated
  illustrative citation edges.

## Quickstart

```bash
# 1. Segment a paper straight from arXiv's HTML rendering
python3 segmenter/segment.py \
  --url https://ar5iv.org/html/1706.03762 \
  --slug arxiv-1706-03762 \
  -o examples/arxiv-1706-03762.jsonld

# 2. View it
python3 -m http.server 8000
# open http://localhost:8000/viewer/index.html
```

Expected output for the example paper: 9 components
(`a1` Abstract → A, `a2` Introduction → A, `b1` Background → B,
`c1` Model Architecture → C, `c2` Why Self-Attention → C,
`c3` Training → C, `d1` Results → D, `e1` Conclusion → E,
`f1` Attention Visualizations → F).

## Roadmap

- [x] Component schema (JSON-LD, draft v0.1)
- [x] Rule-based segmentation baseline + viewer
- [ ] Citation-intent mining (7-class, CiTO-aligned) ← next
- [ ] Cross-paper entity resolution (mention → registry, NIL handling)
- [ ] LLM-assisted segmentation with human-in-the-loop review
- [ ] Component editor + article renderer (round-trip)

## Design principles

1. **Addressability** — every component gets a stable URI.
2. **Compatibility** — reuse schema.org, CiTO, CRediT; mint new terms only
   for genuine gaps.
3. **Provenance-first** — every extracted fact records *how* it was produced
   and how confident the extractor is.
4. **Round-trip** — components reassemble into a conventional article; no
   author behavior change required.
5. **Honest baselines** — deterministic first, ML where judgment is needed.

## License

MIT — see [LICENSE](LICENSE). Schema: CC0.
