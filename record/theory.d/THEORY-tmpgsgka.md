---
status: Proposed
title: "Transtrum, Machta and Sethna (2011) argue from the interpolation error of analytic functions that a multiparameter nonlinear least-squares model's manifold is a bounded hyper-ribbon whose geodesic widths fall by a roughly constant factor; in natural or log units and from a central point the widths match the Jacobian's singular values for a sum of exponentials and a small tanh network, though not in magnitude for the PC12 model; and the manifold's boundaries are where the metric JᵀJ is singular, usually at parameters running to 0 or ∞ but also on finite fold lines such as equal rates"
promote_when: >-
  On a model neither reducible to a linear one nor computed by the authors,
  an independent computation that finds the geodesic widths, from a
  central point in natural or log units, falling roughly geometrically
  and tracking the Jacobian's singular values within a stated factor; and,
  for a model with a finite fold such as two equal rates, a check that the
  metric JᵀJ loses rank on the fold and at the parameter limits that bound
  the manifold. A theorem making the interpolation argument rigorous under
  stated conditions would meet the first half.
version: 1
tags:
- information-geometry
- model-comparison
- mathematical-statistics
date: '2026-11-21'
source:
- LIT-tmpzkxka
corroborates:
- CLAIM-tmpficzj
- CLAIM-tmpcg4uu
bears_on:
- QUESTION-tmpzlagu
summary: >-
  Transtrum, Machta and Sethna (2011), LIT-tmpzkxka, read in
  NOTE-tmpzxtnv. The geometry the record's TERM-tmp5z2du and TERM-tmptiim0
  rest on. The widths are invariant where the Fisher spectrum is not, and
  match √λ only under conditions; the edges of the hyper-ribbon are where
  the metric is singular, which ties sloppiness to singularity at the
  boundary and leaves the interior regular.
---
<!-- inactive-ok-file: TERM-tmp5z2du TERM-tmptiim0 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# THEORY-tmpgsgka: Transtrum, Machta and Sethna (2011) argue from the interpolation error of analytic functions that a multiparameter nonlinear least-squares model's manifold is a bounded hyper-ribbon whose geodesic widths fall by a roughly constant factor; in natural or log units and from a central point the widths match the Jacobian's singular values for a sum of exponentials and a small tanh network, though not in magnitude for the PC12 model; and the manifold's boundaries are where the metric JᵀJ is singular, usually at parameters running to 0 or ∞ but also on finite fold lines such as equal rates

## Source

Transtrum, Machta and Sethna, Phys. Rev. E 83, 036701 (2011),
LIT-tmpzkxka, read from arXiv 1010.1449v1 in NOTE-tmpzxtnv.

## What was actually shown

- **Widths.** From the polynomial interpolation error (§III, Eq. 13): "Each
  cross section is thinner than the last by a roughly constant factor ∆ =
  δt/R"; "We describe the shape of a model manifold with such a hierarchy
  as a hyper-ribbon." A heuristic, with conditions: analytic, derivatives
  not growing too fast, points not too widely spaced, n large.
- **Widths and singular values.** Exact for polynomial fitting on a ball;
  within a factor √(2/M) for exponentials in a continuum limit; numerically,
  for an eight-parameter sum of exponentials in log parameters and a
  4-4-2 tanh network, the geodesic widths from a central point "nicely
  track the singular values" (Fig. 6). For PC12 they are "smaller by
  several orders of magnitude", with the same spacing. "This depends on
  the choice of parameters and the placement of the best fit." So width ≈
  singular value of J ≈ √λ, in natural or log units, from a central point.
- **Invariance.** "one can always reparametrize the manifold to make the
  metric at a point any symmetric, positive definite matrix": the
  spectrum is not intrinsic; the widths are.
- **Boundaries.** "Model boundaries correspond to points on the manifold
  where the metric is singular. Typical boundaries occur when parameters
  are near their extreme values (such as ±∞ or zero)"; the equal-rate
  "fold line" is the exception, where "No parameters were at extreme
  values, but the model behavior was nonetheless singular." When
  M < 2N, finite singular points are generic (Eq. 16); otherwise only
  near-singular ones. In log parameters every boundary lies at infinity.

What could have failed: the widths could have been unrelated to the
singular values in the network, and the fold could have been a regular
point of the metric.

## What this does not say

- **That widths ≈ √λ always.** The match needs natural units and a central
  start; PC12 fails it in magnitude. It is not 1/√λ.
- **That the interpolation argument is a theorem,** or that it covers
  several independent variables except "in some multidimensional sense".
- **That every boundary is a finite singular stratum.** Most lie at
  infinite parameter values; finite folds are generic only with fewer data
  than twice the parameters.
- **Anything about learning coefficients or Bayesian evidence.** The
  singular points are of the metric; their Watanabe invariants are not
  computed.
- **That a 4-4-2 network speaks for large ones.** One small network.
