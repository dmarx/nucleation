---
number: 674
status: Proposed
formerly:
- THEORY-tmpxx3fy
promote_when: >-
  An audit of the extracted edges themselves against human labels, by
  experts or by the papers' authors, on a sample drawn by decade, field
  and method, at the baseline EO ≥ 4. Promoted if edge-level precision and
  recall for the causal label are high and roughly stable across decades,
  so that the rise cannot be laid to modern papers naming their designs
  more explicitly. Refuted if the causal label's precision on 1980s and
  1990s papers is low or its recall rises sharply with time. More runs of
  the same pipeline, agreement between its passes, or agreement with a
  trend measured by a similar design-keyword method cannot settle it.
title: "In NBER and CEPR working papers from 1980 to 2023, the share of claims backed by a design-based identification strategy (difference-in-differences, instrumental variables, RCT, regression discontinuity or synthetic control) rose about fourfold, from 7.7% of a paper's extracted edges in 1990 to 31.7% in 2020, as measured by an LLM extraction whose edges were never checked against human labels"
version: 1
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
---
<!-- inactive-ok-file: THEORY-451 — Proposed; Cartwright's account, named as a neighbour, nothing here rests on it -->
<!-- inactive-ok-file: LIT-079 — Proposed by its close reading; the only source, and the account is Proposed for the reason that reading gives -->

# THEORY-674: In NBER and CEPR working papers from 1980 to 2023, the share of claims backed by a design-based identification strategy (difference-in-differences, instrumental variables, RCT, regression discontinuity or synthetic control) rose about fourfold, from 7.7% of a paper's extracted edges in 1990 to 31.7% in 2020, as measured by an LLM extraction whose edges were never checked against human labels

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
