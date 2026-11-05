# English paper — Round 2 revision brief (paste to Claude Code / vscc)

## Context

The Chinese draft has gone through three rounds and is now finalized as the working draft
(6,000 characters, Sections 1–4). This English draft is a strong Round 1, but it is now
**two theoretical rounds behind** the Chinese version. This brief brings it to parity.
Do not rewrite from scratch — revise in place.

## A. Mechanical must-fix (highest priority)

1. **Real compile.** The delivered PDF shows unresolved `[?]` citations and `Section ??` /
   `Table ??` references. Compile with pdfLaTeX + BibTeX (install TeX Live/MiKTeX, or use
   Overleaf). Fix all `\label`/`\ref` pairs. Deliver a PDF with **zero `[?]` and zero `??`**.
2. **Add reference [14]** to the bibliography (it was added to the prompt after your draft):
```latex
\bibitem{natsensors2026} Shaping the AI systems that speak for science. (2026). Editorial. \textit{Nature Sensors}, 1, 559--560. https://doi.org/10.1038/s44460-026-00109-0.
```

## B. Parity upgrades (from the finalized Chinese draft)

3. **§1 — add the Nature Sensors evidence [14].** A 2025 survey found 61% of researchers use
   AI tools to discover and summarize papers rather than reading them on journal platforms;
   Perplexity AI surpassed 30 million daily searches in 2025 and partnered with Wiley to
   deliver peer-reviewed content directly. Add the honest qualification: a self-reported
   usage share is not a first-reading share; platform-wide search volume is not academic
   retrieval volume. The two observations together show non-journal platforms shaping
   first visibility.
4. **§1.2 — tighten the operational definition.** Add: the "first reader" is not "every paper
   opened by a machine first" but "**AI systems massively mediating humans' first contact
   with scholarly content (discovery, summarization, ranking, pre-evaluation)**".
   "First contact" = the first *effective informational* contact on which a decision to
   read/cite/evaluate further is based — not a download event. Whether the machine changes
   the choice must be measured separately.
5. **§1 — add a falsifiability paragraph.** What evidence would strengthen or shrink the
   claim (audited publisher AI-access logs, consented researcher workflow logs, behavioral
   measures separating first AI summary from first full-text reading)? If representative
   samples show low AI mediation or no effect on selection, the strong version of the
   claim must be narrowed or abandoned.
6. **§2 — historical scoping (one paragraph).** The critique targets **the post-WWII regime
   of the whole journal paper as the dominant credit credential**, especially formal
   resource allocation keyed to venues — not the claim that credit historically had only
   one channel. Preprint, monograph, conference, patent, software and data traditions show
   plurality is old. Frame plural settlement as a **return/reorganization** of that
   plurality under auditable infrastructure — not an invention. (This strengthens, not
   weakens, Section 3.)
7. **§3.1 — replace Table 1 with the 5×3 matrix.** For each dimension distinguish:
   - **Observability**: what existing data sources can record it?
   - **Construct validity**: does the indicator measure what it claims? Where is the bias?
   - **Institutional applicability**: which institutions can use it, in which decisions?

   | Dimension | Observability (candidate sources) | Construct validity (main biases) | Institutional applicability (who decides what) |
   |---|---|---|---|
   | Origination | structured novelty statements; timestamped archives; retrospective "first" attributions | retrospective attribution is winner's narrative; timestamps prove priority, not importance | hiring/tenure; prizes |
   | Evidence quality | data/code availability badges; named reviews of method–conclusion fit | availability ≠ correctness; badges can become formalistic | journal/conference acceptance; grant review |
   | Verification | replication badges; open review records; locatable counterexamples | a replicable error is still an error; negative replications are hard to publish → observation is skewed | grant renewal/completion; field consensus |
   | Maintenance | version histories; erratum response records; long-term availability checks | update frequency ≠ maintenance quality; value hard to compare across fields | infrastructure and long-term project funders; repository operators |
   | Downstream use | citations, code dependencies, dataset citations (excluding self/reciprocal/automated) | mixed citation motives; disciplinary citation cultures differ | institutional impact assessment; policy evaluation |

   Caption: "candidate design, not empirical results." Follow with one paragraph: **observability
   is the admission ticket, construct validity is honesty, institutional applicability is use.**
   Different decisions need different (dimension, validity-requirement) combinations — that is
   the *positive measurement-theoretic reason* for no single total score. This upgrades "we do
   not presume a sum" from a defensive disclaimer to an argument.
8. **§3.3 — add the record → adopt → allocate chain.** (1) Open, interoperable infrastructure
   records identifiers, attribution, dependencies, evidence, timestamps. (2) Plural
   accountable agents (field peers, independent replicators, data/software auditors, affected
   contributors) verify and allow dissent. (3) Institutions allocate: universities disclose
   per-dimension contributions in hiring/promotion files; funders record what evidence grants
   rest on; journals show verification/maintenance status. Those who record must not
   monopolize verification and allocation — separation of powers.
9. **§3.4 — incentive compatibility (condensed, ~150 words).** Observable: verifiable version
   submissions, sourced replications, external dependencies, erratum response times, declared
   interests. Not auto-credited: unverified downloads, bot traffic, reciprocal citation rings,
   mass-produced surface reviews. Suspected gaming → record the checkable anomaly first,
   judged by independent persons in disciplinary context; statistical anomaly alone never
   equals misconduct. Affected contributors get to see the basis, rebut, request human review.

## C. Resolving the `\verify{}` tags

- **ARC** — VERIFIED. Replace tag with:
  `\bibitem{arc2023} Australian Research Council. (2023). Policy on the use of generative AI tools in the ARC's grants programs. Released 7 July 2023.`
  (Confirm the canonical URL at arc.gov.au before final submission.)
- **PRC alliance** — VERIFIED, **date corrected: 28 October 2026** (not 2025). Joint initiative
  of COAR and ASAPbio, 40+ stakeholders. Change "Oct. 2025" → "Oct. 2026". Suggested:
  `\bibitem{prc2026} Publish, Review, Curate (PRC) Alliance. (2026). Launch announcement, 28 October 2026. Joint initiative of COAR and ASAPbio.`
  (Confirm URL at publish-review-curate.org.)
- **eLife** — the substance is correct (eLife replaced accept/reject with public review +
  curation). Confirm the exact announcement reference before citing.
- **COPE / publisher authorship policies** — COPE's position (AI tools cannot be authors;
  authorship requires accountability) is real; confirm exact wording at publicationethics.org.
- **OpenAI classifier withdrawal (July 2023)** — real, widely reported; confirm the primary
  source before citing.
- **Wiley 4,946-researcher / 63% figures** — NOT yet verified. Either replace with the
  verified 61% figure from [14] or keep the `\verify{}` tag.
- **Psychiatry / oncology journal-policy surveys; ICLR 2025 review-feedback experiment;
  Nature 2026 41.3M-paper study** — keep the `\verify{}` tags or delete the sentences.
  The argument must not depend on them either way.

## D. Constraints

- Keep body within **3,000–4,500 words** (currently ~3,540; the additions above are ~400 words — fits).
- Keep: the four epistemic-status labels, the A1/A2/A3 assumption framing, P1–P3 as
  hypotheses, "upgrade of peer review, not its abolition", the three self-limitations.
- Boundaries unchanged: no people, groups, or internal names; never the abbreviation "PoC";
  proof of contribution only via contribution accounting and provenance.
- New sources beyond the list above: mark `[TO VERIFY]`, never carry the argument.
- Output: complete compilable LaTeX + a clean PDF with no `[?]` and no `??`.
