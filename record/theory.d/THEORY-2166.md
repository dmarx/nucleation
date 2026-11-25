---
number: 2166
status: Proposed
formerly:
- THEORY-tmpt1tw7
title: 'Geodesics to manifold edges reduce sloppy models'
statement: >-
  Transtrum and Qiu reduce a sloppy model by following a geodesic along the
  Fisher metric's least sensitive direction until its smallest eigenvalue
  goes to zero at a boundary of the bounded model manifold, evaluating the
  limit found there to remove one parameter combination, refitting and
  repeating, so that the reduced model sits at a hypercorner; the method
  needs the manifold to have a hierarchy of edges and corners as well as of
  widths
promote_when: >-
  An application of the method by authors outside the Sethna group and
  its authors' collaborators, to a model they did not design, that
  reaches a reduced model at a boundary limit by these four steps; and
  either that application or the letter's Supplemental Material shows a
  model with a hierarchy of widths and no corners on which the method
  fails to reach a simpler model. The 48-to-12 EGFR result, restated in
  the 2015 review, is the same group's and does not meet this.
version: 1
tags:
- model-comparison
- information-geometry
date: '2026-11-21'
source:
- LIT-2979
corroborates:
- CLAIM-820
summary: >-
  Transtrum and Qiu (2014), [LIT-2979](../literature.d/LIT-2979.md), read in [NOTE-2253](../notes.d/NOTE-2253.md). The
  manifold boundary approximation turns the hyper-ribbon into a
  reduction algorithm: boundaries are where a parameter combination
  reaches a limit (0, ∞, or two terms merging), the reduced model is a
  hypercorner, and the method requires nested edges and corners, which an
  ellipsoid with a hierarchy of widths lacks.
---
<!-- inactive-ok-file: CLAIM-833 — Proposed; filed 2026-11-21 from the exchange "Rich Get Richer Power Laws" -->

# THEORY-2166: Geodesics to manifold edges reduce sloppy models

## Source

Transtrum and Qiu, "Model Reduction by Manifold Boundaries", Phys. Rev.
Lett. 113, 098701 (2014), [LIT-2979](../literature.d/LIT-2979.md), read from the NIH author manuscript
(PMC4425275) in [NOTE-2253](../notes.d/NOTE-2253.md). The Supplemental Material is unread.

## What was actually shown

- **The algorithm** (para. 9): smallest-eigenvalue direction; a geodesic
  "until a boundary is identified"; "identify it with a limiting
  approximation in the mathematical form of the model. Evaluating this
  limit removes one parameter combination"; refit; repeat.
- **The signature of a boundary** (para. 11): "the smallest eigenvalue
  separates from the others and approaches zero."
- **Three worked models.** A sum of exponentials, whose boundaries are
  rates to 0 or ∞ and "two terms merge together" (para. 12); the
  48-parameter EGFR model, reduced "from 48 to 12 parameters", after which
  no eigenvalue is below 1 (para. 16, Fig. 3); a generalized Ising chain,
  whose boundaries are "Jμ → ±∞", one hypercorner being a block-spin step
  (paras 17–18).
- **A condition.** "the model manifold be bounded with a hierarchy of
  boundaries"; an ellipsoid has "a hierarchy of widths but without a
  hierarchy of edges; i.e., there are no corners" (para. 21).

## What this does not say

- **Sufficient conditions** for the hierarchy of boundaries: "we cannot
  give sufficient conditions for this hierarchical structure" (para. 22).
- **That boundaries are singular strata** in the sense of singular learning
  theory. Most of its boundaries lie at infinite parameter values, reached
  as finite points only in the closure of the manifold in prediction
  space; the paper neither uses the word "stratum" nor cites that theory.
- **Anything about learning.** No training, no networks, no move away from
  a singular configuration ([CLAIM-833](../claims.d/CLAIM-833.md)'s other half).
- **That the method is automatic.** A human names the limit.
