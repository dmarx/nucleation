---
status: Proposed
title: 'For a candidate structure whose removal makes the remaining model singular, the reification rule''s Gaussian Occam term misprices the cost of keeping it, by a term that grows with log n, so the rule is exact only where the model stays regular'
version: 1
role: counter
tags:
- model-comparison
- individuation
date: '2026-10-11'
line: distributed-agency
objects_to:
- CLAIM-154
grounds:
- THEORY-087
- THEORY-079
- THEORY-031
summary: >-
  A narrowing of [CLAIM-154](CLAIM-154.md), filed on 2026-10-11 from a synthesis review
  that found the record already held the readings that limit it.
  [CLAIM-154](CLAIM-154.md)'s rule prices a candidate with a Gaussian Occam factor, which
  is exact in the conjugate case it was re-checked in. The candidates it
  is meant for (blocks, sectors, couplings with hidden structure) are
  plausibly singular, where [THEORY-087](../theory.d/THEORY-087.md) puts the penalty at λ log n, not
  (d/2) log n, and [THEORY-079](../theory.d/THEORY-079.md) says the Laplace form errs by a term that
  grows with log n. Both THEORYs are Proposed, so this is too.
---
<!-- inactive-ok-file: CLAIM-174 CLAIM-175 THEORY-079 THEORY-087 — Proposed; open, and cited as open: under test, not settled -->

# CLAIM-tmpczjuu: For a candidate structure whose removal makes the remaining model singular, the reification rule's Gaussian Occam term misprices the cost of keeping it, by a term that grows with log n, so the rule is exact only where the model stays regular

## The claim

[CLAIM-154](CLAIM-154.md) says to keep a candidate direction, block or sector when
d'² exceeds the Occam term ln(s²/σ²), with a Gaussian prior and a Laplace
posterior. "In the conjugate Gaussian case the rule is the Bayes factor
exactly", and that case was re-run here. Its own caveat is about
magnitude far from the threshold: "Away from the threshold the Laplace
form can understate the evidence badly."

The limit this claim adds is about the kind of model, not the distance
from the threshold:

- **The penalty depends on regularity.** In a regular model the Occam
  factor comes from the curvature at the optimum and grows as (d/2) log n.
  In a singular model, where the Fisher information is degenerate at the
  optimum, it grows as λ log n, with λ the real log canonical threshold,
  and λ falls below d/2 when the prior is positive on the optimal set
  ([THEORY-087](../theory.d/THEORY-087.md), from MacKay and Watanabe).
- **Laplace-based pruning misprices singular reductions.** [THEORY-079](../theory.d/THEORY-079.md) says
  Bayesian model reduction under the Laplace approximation charges the
  reductions of a singular parent with a Gaussian Occam factor, so its
  evidence differences can be wrong by a term that grows with log n. The
  same arithmetic is in [CLAIM-154](CLAIM-154.md)'s rule.
- **The candidates are the singular kind.** Models "with hierarchical
  layers or hidden variables are singular" ([THEORY-079](../theory.d/THEORY-079.md), citing Watanabe).
  [CLAIM-154](CLAIM-154.md) is put to work on near-decomposable blocks, on couplings
  ([CLAIM-174](CLAIM-174.md)) and on the owner's dancing couple ([CLAIM-175](CLAIM-175.md)). Removing a
  block or a coupling from such a model typically leaves parameters that
  the data no longer pin down. That is the singular case. The step from
  "blocks and couplings" to "singular" is the filer's, and it should be
  checked on a concrete family.

The direction of the error follows from [THEORY-087](../theory.d/THEORY-087.md), as the filer reads it.
Where λ < d/2, the true penalty is smaller than the Gaussian term, so the
rule overcharges a candidate and prunes structure the exact Bayes factor
would keep. Because the gap grows with log n, more data does not wash it
out, and near the threshold it can flip the decision. That is the kind of
failure [CLAIM-154](CLAIM-154.md)'s own defeater counts.

[THEORY-031](../theory.d/THEORY-031.md) adds a smaller point. d' separates sensitivity from criterion
only for equal-variance normal signal and noise. The rule's "effect-to-noise
ratio" inherits that assumption.

## What it does not say

- It does not say [CLAIM-154](CLAIM-154.md) is wrong where it was checked. The conjugate
  case is exact, and nothing here touches it.
- It does not say the error always runs one way. λ < d/2 is the case
  [THEORY-087](../theory.d/THEORY-087.md) names. Other singular structures need their own λ.
- It does not rest on read theorems. The singular half of [THEORY-087](../theory.d/THEORY-087.md) is a
  theorem the record holds as cited, and [THEORY-079](../theory.d/THEORY-079.md) is the record's own
  synthesis. A test would settle both: compare the rule with an exact or
  WBIC-estimated Bayes factor on a two-block coupling model or
  reduced-rank regression, near the threshold, as n grows.
- [CLAIM-154](CLAIM-154.md) is dual-filed from the mathematics-of-meaning record
  ([MOM-CLM-160](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-160.md)). The same limit would apply there. Filing it there is
  that record's business.

## What would answer it

The rule and an exact or WBIC-estimated Bayes factor agree on keep or
prune near the threshold, across n, in a family where removing the
candidate makes the model singular.
