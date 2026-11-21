---
status: Proposed
title: "Transtrum, Machta and Sethna (2010) argue that a nonlinear least-squares model's manifold of predictions is typically bounded and ribbon-like, its cross-sectional widths each thinner than the last by a roughly constant factor, from the error of polynomial interpolation for analytic models of one variable; in one eight-parameter model they observe the geodesic widths along the eigendirections of JᵀJ tracking the square roots of its eigenvalues over about four decades; fits fail where algorithms reach the manifold's boundaries, and adding geodesic acceleration to Levenberg–Marquardt raised its success on one four-exponential test from 33% to 65%"
promote_when: >-
  An independent reproduction (not by the authors) of the paper's two
  computations: geodesic cross-sectional widths along the eigendirections
  of JᵀJ beside √λ for a sum of exponentials in log parameters, finding
  both hierarchies over about four decades and the widths tracking √λ; and
  Levenberg–Marquardt with and without geodesic acceleration on the
  four-exponential test started near a boundary, finding the
  accelerated success rate clearly higher. The generality the authors
  "suggest" is not part of the title and is not asked for here.
version: 1
tags:
- information-geometry
- model-comparison
- mathematical-statistics
date: '2026-11-21'
source:
- LIT-tmpd3swn
corroborates:
- CLAIM-tmpficzj
summary: >-
  Transtrum, Machta and Sethna (2010), [LIT-tmpd3swn](../literature.d/LIT-tmpd3swn.md), read in
  [NOTE-tmpamhd2](../notes.d/NOTE-tmpamhd2.md). The letter that named the hyper-ribbon. Its explanation
  of the width hierarchy (interpolation) and its link to the spectrum
  (an observation in one model) are separate, and neither is a theorem;
  the fuller treatment is [LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md) ([THEORY-tmpgsgka](THEORY-tmpgsgka.md)).
---
<!-- inactive-ok-file: THEORY-tmpgsgka — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# THEORY-tmpkoje5: Transtrum, Machta and Sethna (2010) argue that a nonlinear least-squares model's manifold of predictions is typically bounded and ribbon-like, its cross-sectional widths each thinner than the last by a roughly constant factor, from the error of polynomial interpolation for analytic models of one variable; in one eight-parameter model they observe the geodesic widths along the eigendirections of JᵀJ tracking the square roots of its eigenvalues over about four decades; fits fail where algorithms reach the manifold's boundaries, and adding geodesic acceleration to Levenberg–Marquardt raised its success on one four-exponential test from 33% to 65%

## Source

Transtrum, Machta and Sethna, Phys. Rev. Lett. 104, 060201 (2010),
[LIT-tmpd3swn](../literature.d/LIT-tmpd3swn.md), read from arXiv 0909.3884v2 in [NOTE-tmpamhd2](../notes.d/NOTE-tmpamhd2.md).

## What was actually shown

- **An argument.** For an analytic function of one variable sampled within
  its radius of convergence R, fixing n data points leaves a range at the
  next that shrinks by about (t − tₙ₊₁)/R < 1 per point: "Each cross section
  is thinner than the last by a roughly constant factor, yielding the
  observed hierarchy." A ratio-test heuristic for large n.
- **An observation.** For one eight-dimensional model, "Geodesic
  cross-sectional widths ... along the eigendirections of the metric from
  some central point" and the square roots of the metric's eigenvalues,
  "the widths and singular values each spanning around four orders of
  magnitude"; the eigenvalues themselves span eight. The two-exponential
  manifold has boundaries "when θµ = 0, ∞ and when θ1 = θ2".
- **A diagnosis.** "Since most boundaries occur at infinite parameter
  values", algorithms that walk to an edge get lost: "the geodesics hit
  the edges long before finding a good fit".
- **A test.** On a four-exponential problem started near a boundary,
  success 65% with geodesic acceleration against 33% for traditional
  Levenberg–Marquardt (Table I; trial count not stated).

What could have failed: the widths could have been comparable, or
uncorrelated with the spectrum, in the one model computed; acceleration
could have made no difference.

## What this does not say

- **That widths equal √λ in general.** One model, one central point;
  "suggests" is the authors' word. [LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md) finds the match conditional
  on units and starting point, and failing in magnitude for PC12.
- **That the interpolation bound is proved,** or that it covers models of
  several variables or with chaotic dependence on parameters, which the
  paper itself excludes, with models whose parameters "are individually
  measured by the data".
- **That the boundaries are singular strata.** The letter lists θ₁ = θ₂ as a
  boundary; it does not say the metric is singular there ([LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md)
  does).
- **That geodesic acceleration is generally better.** One test problem.
- **A noise model.** Distances are raw residuals; "Fisher Information" is
  JᵀJ under unit error.
