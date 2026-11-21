---
status: Proposed
title: 'Gutenkunst and colleagues find that in seventeen systems-biology models, with 9 to 234 parameters, the Hessian of a least-squares deviation of all time courses in log parameters has eigenvalues spanning many decades, all but one more than six, roughly evenly in log with no cutoff, along eigenvectors skewed from the bare parameter axes; and that in one of them a collective fit constrains a prediction that direct measurement would match only with all 24 relevant parameters measured to about 25%'
promote_when: >-
  An independent computation, by authors outside the Sethna group, of the
  spectra of several of the seventeen models (from their published SBML
  and the cost of Eq. 1) finds the same spans, the same absence of a gap
  and few eigenvectors aligned with a bare axis; and a recomputation of
  the PC12 comparison of Fig. 4 confirms the ±25% figure. The filer's
  recomputation of the eigenvalues from the paper's own Dataset S1
  Hessians checks the arithmetic, not the finding, and does not meet this.
version: 1
tags:
- model-comparison
- information-geometry
- natural-sciences
date: '2026-11-21'
source:
- LIT-2999
summary: >-
  Gutenkunst, Waterfall, Casey, Brown, Myers and Sethna (2007), [LIT-2999](../literature.d/LIT-2999.md),
  read in [NOTE-tmp1feoo](../notes.d/NOTE-tmp1feoo.md). The empirical base of sloppiness: a two-part
  criterion (even spread over many decades, and skew from the bare axes),
  shown across a collection, and the argument that collective fits beat
  direct measurement for predictions, shown in one model. Across the
  collection the resolved span stays at 5–10 decades while the density of
  eigenvalues per decade grows with the number of parameters (the
  reader's computation from Dataset S1, recomputed by the filer).
---
<!-- inactive-ok-file: LIT-tmpmgyty — Deferred, registered 2026-11-21 from this reading, unread -->
<!-- inactive-ok-file: TERM-140 — Proposed; filed 2026-11-21, the term this reading corrects -->

# THEORY-tmpks8pd: Gutenkunst and colleagues find that in seventeen systems-biology models, with 9 to 234 parameters, the Hessian of a least-squares deviation of all time courses in log parameters has eigenvalues spanning many decades, all but one more than six, roughly evenly in log with no cutoff, along eigenvectors skewed from the bare parameter axes; and that in one of them a collective fit constrains a prediction that direct measurement would match only with all 24 relevant parameters measured to about 25%

## Source

Gutenkunst, Waterfall, Casey, Brown, Myers and Sethna, "Universally
Sloppy Parameter Sensitivities in Systems Biology Models", PLoS Comput.
Biol. 3(10): e189 (2007), [LIT-2999](../literature.d/LIT-2999.md), read from the Europe PMC full text in
[NOTE-tmp1feoo](../notes.d/NOTE-tmp1feoo.md).

## What was actually shown

- **Spread.** "In every case, the eigenvalues span many decades. All but
  one span more than 10⁶ ... approximately evenly spaced in their
  logarithm; there is no well-defined cutoff between 'important' and
  'unimportant' parameter combinations" (Results, Fig. 1B).
- **Skew.** "These characteristic parameter sensitivities that evenly span
  many decades and are skewed from bare parameter axes define a 'sloppy'
  model"; by I/P, "very few axes have I/P ≈ 1".
- **Loose parameters.** An idealized fit with 100 points per parameter at
  10% error "leaves many parameters with greater than 100% uncertainty"
  for most models (Fig. 3).
- **Tight predictions, in one model.** In the 48-parameter PC12 model
  (Brown et al. 2004, [LIT-tmpmgyty](../literature.d/LIT-tmpmgyty.md)), the ERK prediction is tight after a
  fit that constrains no parameter better than a factor of 50, while
  matching it by measurement needs "all 24 involved parameters" to ±25%
  (Fig. 4).
- **Causes, argued.** The parametrization is "fundamental to the system,
  not an artifact"; decoupling experiments "will naturally not yield
  sloppy parameter sensitivities"; the PC12 model with every scale set to
  1 "remains sloppy".

**From the paper's Dataset S1**, computed by the reader and recomputed by
the filer, not stated by the paper: the exception to "more than 10⁶" is
the Kholodenko kinase cascade (5.2 decades); the resolved span stays at
5–10 decades from 9 to 234 parameters while eigenvalues per decade rise
from about 1 to 15–22; the large models' spans are lower bounds under a
numerical floor near 10⁻⁷.

## What this does not say

- **A threshold.** "Many decades" and "evenly" have no number; "evenly"
  is judged by eye from a figure clipped at 5×10⁻⁷.
- **That tight predictions from loose parameters hold across the
  collection.** Fig. 3 shows loose parameters in most models; tight
  predictions are shown in one.
- **How the spectrum scales with the number of parameters.** The paper
  says nothing on it. The record's earlier reading of "evenly spaced" as
  a fixed factor per rank, and with it a span growing in proportion to
  the number of parameters, is not borne out by the Dataset S1 spectra
  ([TERM-140](../terms.d/TERM-140.md), version 3).
- **Anything chart-free.** The spectra are in log parameters, which the
  paper defends as fundamental; the model manifold and its widths come
  later in the programme.
- **Real data.** The spectra are of a design in which every species is
  observed continuously, simulated from the published parameters.
