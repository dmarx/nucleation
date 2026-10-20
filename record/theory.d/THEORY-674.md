---
number: 674
status: Active
formerly:
- THEORY-tmpxx3fy
title: 'In Garg and Fetzer''s GPT-4o-mini extraction from NBER and CEPR working papers, edges kept in at least 4 of 9 passes and never checked against human labels, the mean per-paper share of edges labelled as backed by difference-in-differences, instrumental variables, an RCT, regression discontinuity or synthetic control rose from 7.7% in 1990 to 31.7% in 2020, at every overlap threshold; the paper''s per-decade slope fell from +0.0187 to +0.0011 once method mix and graph volume were controlled'
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-674 (batch 074, ADR-047 v3 and v4): one study read in full in
    NOTE-083, its §3 numbers re-checked against the arXiv v2 text. The title
    now states what was measured, the output of the authors' extraction
    pipeline, with the controlled slope the paper reports beside the raw
    rise. The claim that the share of design-backed claims in economics
    rose about fourfold leaves the title; the paper asserts it, so under
    ADR-047 v4 it is filed as a new Proposed THEORY, THEORY-824, which
    extends this one and takes the promote_when (an edge-level audit
    against human labels) unchanged.
tags:
- social-science
- causality
- philosophy-of-science
date: '2026-10-16'
source:
- LIT-079
summary: >-
  Garg & Fetzer (2024; arXiv v2 2026), [LIT-079](../literature.d/LIT-079.md), read in full in [NOTE-083](../notes.d/NOTE-083.md).
  GPT-4o-mini, nine passes per paper over the first 30 pages of 44,852
  working papers, edges kept in at least 4 of 9 passes. The direction of the
  trend holds across overlap thresholds, its level does not (mean causal
  share 0.152 at EO = 1, 0.270 at EO = 9), and it nearly vanishes once
  method mix and graph volume are controlled. Validation covers paper-level
  method labels only, with RCT precision about 0.02. The association of
  causal structure with top-five publication rests on year-fixed-effect
  regressions over different subsamples and is not part of this claim.
  Promoted 2026-10-20 on the measurement alone (ADR-047 v3); the economics
  claim is held as THEORY-824.
extended_by:
- THEORY-824
---
<!-- inactive-ok-file: THEORY-451 — Proposed; Cartwright's account, named as a neighbour, nothing here rests on it -->
<!-- inactive-ok-file: LIT-079 — Proposed by its close reading for edges never validated against human labels; the only source, and the narrowed title states that limit -->
<!-- inactive-ok-file: THEORY-824 — Proposed; the economics claim this measurement is taken to show, filed when the narrowing dropped it -->

# THEORY-674: In Garg and Fetzer's GPT-4o-mini extraction from NBER and CEPR working papers, edges kept in at least 4 of 9 passes and never checked against human labels, the mean per-paper share of edges labelled as backed by difference-in-differences, instrumental variables, an RCT, regression discontinuity or synthetic control rose from 7.7% in 1990 to 31.7% in 2020, at every overlap threshold; the paper's per-decade slope fell from +0.0187 to +0.0011 once method mix and graph volume were controlled

## Source

Prashant Garg and Thiemo Fetzer, "Causal Claims in Economics" (OSF 2024;
arXiv v2, February 2026), [LIT-079](../literature.d/LIT-079.md), read in full in [NOTE-083](../notes.d/NOTE-083.md), with v1
compared for the reframing.

## What was actually shown

**The measure.** Each paper becomes a directed graph over JEL concepts.
An edge is a stated source → sink relation, and it is "causal" when the
paper supports it with DiD (including TWFE and event studies), IV, an RCT,
an RDD or synthetic control. Structural estimation and causal language
without such a design count as non-causal (§2.2). GPT-4o-mini reads the
first 30 pages three times, extracts edges three times from each summary,
and an edge is kept if it appears in at least 4 of the 9 lists. That leaves
42,404 papers, not 44,852 (Table A10).

**The trend (§3, Fig. 2a).** 23.8% of baseline edges are causal. The mean
per-paper causal share is 7.7% (1990), 8.6% (2000), 21.5% (2010), 31.7%
(2020) and 32.6% (2023). By field, pre- to post-2000: Health 9.7 → 41.9%,
Urban 9.0 → 37.4, Development 6.9 → 37.2, Macro 6.3 → 12.9. Paper-level
method shares move the same way: DiD 10.5% (1980) → 20.3% (2023), RCT 0.8%
(2000) → 8.0%. The field ordering agrees with Goldsmith-Pinkham (2024),
which the paper cites.

**What could have come out otherwise.** The share could have been flat, or
its direction could have depended on the overlap threshold. It rises at
every threshold (Fig. A1), though its level rises with the threshold too:
0.152 at EO = 1, 0.225 at EO = 4, 0.270 at EO = 9 (Table A10).

## What this does not say

- **That the edges are accurate.** No edge was checked against a human
  label. The external checks are of paper-level method and field labels
  (n = 285): DiD, RDD and IV reach F1 0.68–0.74, but RCT per-run F1 is
  0.03 and field precision 0.05–0.43 (Tables A6–A7). The snippet check is
  self-consistency and stops at EO = 3. The v1 validation figures (F1
  0.83–0.99) were rewritten in v2 to these.
- **That the rise is in economics rather than in the extractor.** Modern
  papers name their designs; older ones may not. A DiD rate of 10.5% and an
  RDD rate of 1.3% in 1980 look like label noise ([NOTE-083](../notes.d/NOTE-083.md)'s inference).
  With method-mix and graph-volume controls the trend falls from +0.0187 to
  +0.0011 per decade. The promised robustness table is absent, and the
  per-decade unit is hard to square with the headline levels.
- **That causal claims pay.** The +1.36 pp top-five probability per
  doubling of causal edges comes from bivariate regressions with year
  fixed effects only, no field controls, on the roughly 28% of papers with
  a causal edge, against non-causal measures estimated on about 83%. The
  paper itself calls β "a conditional association, not a causal effect".
- **That the claims are true.** The pipeline records what papers claim,
  not whether the identification works (fn. 1).

## Connections

- Cartwright's account of evidence for singular causal claims
  ([THEORY-451](THEORY-451.md), from [LIT-213](../literature.d/LIT-213.md)) already names this paper as documenting
  the narrowing to RCT-, DiD- and IV-backed claims she describes. Neither
  cites the other.
- [NOTE-083](../notes.d/NOTE-083.md) reads the paper mainly as a cautionary example of LLM-assisted
  extraction, the record's own method. Validating the unit of analysis one
  uses, here edges rather than paper labels, is the lesson; it is
  machine-learning practice and is not filed here.

## Narrowed and promoted (2026-10-20)

Batch 074 of the promotion audit narrowed the title to the measurement and
promoted it under [ADR-047](../decisions.d/ADR-047.md) v3. The numbers it keeps are in the paper's
running text (§3): 7.7% (1990), 8.6% (2000), 21.5% (2010), 31.7% (2020),
and the per-decade slopes +0.0187 unadjusted, +0.0174 with field controls
and +0.0011 with method-mix and graph-volume controls. The units of the
slopes are the paper's and do not obviously match the levels (see above).
The wider claim, that economics papers increasingly back their claims with
design-based identification, is the paper's own reading of the series. It
is held as [THEORY-824](THEORY-824.md), Proposed until the edges are audited against
human labels.
