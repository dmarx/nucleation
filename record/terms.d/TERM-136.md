---
number: 136
status: Proposed
formerly:
- TERM-tmplplcf
title: 'ambient, intrinsic, effective and spectral dimension (of a learned representation)'
version: 1
tags:
- representation-learning
- mathematics
- mathematical-statistics
date: '2026-11-21'
line:
- learned-structure
- formal-apparatus
draws_on:
- THEORY-1272
- THEORY-301
summary: >-
  Four dimensions of a learned representation that the exchange "Rich Get
  Richer Power Laws" (2026-11-21) keeps apart and the record had no word
  for: the ambient dimension D (layer width), the intrinsic dimension m of
  the manifold the representations lie near, the effective dimension of
  their covariance (its participation ratio D_PR), and the spectral
  dimension d_s of the graph through which they interact. Ambient,
  intrinsic and spectral are A29 §1's; the effective dimension is A30 §5's.
  The wording is A's (the other assistant in the exchange "Rich Get Richer
  Power Laws", A29 and A30); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpwtoad — Proposed, Deferred or new; the readings of 2026-11-22 and the entries they bear on -->
<!-- inactive-ok-file: CLAIM-847 CLAIM-848 CLAIM-842 CLAIM-797 THEORY-1272 LIT-2998 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Deferred works registered from that exchange and not read; Proposed entries the record already held, cited for context -->

# TERM-136: ambient, intrinsic, effective and spectral dimension (of a learned representation)

## Definition

For representations z = h(x) ∈ ℝ^D of inputs x drawn from a data
distribution:

- **Ambient dimension D**: the number of embedding coordinates, the width of
  the layer.
- **Intrinsic dimension m**: the number of degrees of freedom along the
  manifold the representations lie near, as a local estimator measures it.
  A29 §1: trained networks' representations "can have intrinsic dimensions
  far below their layer widths, and … intrinsic dimensionality changes
  systematically across layers" (Ansuini and colleagues, [LIT-2998](../literature.d/LIT-2998.md),
  Deferred: registered, not read).
- **Effective dimension D_PR**: the participation ratio of the centred
  covariance Σ, D_PR = (tr Σ)²/tr(Σ²), equal to D when all eigenvalues are
  equal and near k when k equal directions carry the variance. It sets how
  sharply norms concentrate ([CLAIM-847](../claims.d/CLAIM-847.md)).
- **Spectral dimension d_s**: the exponent in the small-eigenvalue density
  ρ(λ) ∝ λ^(d_s/2 − 1) of the Laplacian of the graph through which the
  representations interact; for a regular m-dimensional geometry d_s = m.
  It sets whether long-wavelength fluctuations destroy order ([CLAIM-842](../claims.d/CLAIM-842.md)).

## Why the record needs the word

The four come apart, and claims about high-dimensional representations
change truth value with the one meant. A29: "A dataset could lie on a
curved, 20-dimensional manifold embedded in 4,096-dimensional space. Its
interaction graph might have still another effective spectral dimension."
Concentration of measure is governed by D_PR, not D ([CLAIM-847](../claims.d/CLAIM-847.md)); the
fluctuation criterion by d_s ([CLAIM-842](../claims.d/CLAIM-842.md)); a sphere in ℝ^D is a thin shell of
intrinsic dimension D − 1, so a thin annulus is not a low-dimensional
manifold ([CLAIM-797](../claims.d/CLAIM-797.md)). The participation ratio does not estimate m: at width
768 smooth codes of manifolds of intrinsic dimension 20 to 100 all have
D_PR near 20 to 29 ([CLAIM-848](../claims.d/CLAIM-848.md)).

Three spectra go with them, and A29 §7 warns they "are not
interchangeable": the covariance spectrum (where variance lies, fixing
D_PR), the graph Laplacian spectrum (the geometry of interaction or
diffusion, fixing d_s) and the dynamical stability spectrum (which
perturbations grow, decay or persist).

## Senses kept apart

- The spectral dimension of SGD's weight drift held in [THEORY-1272](../theory.d/THEORY-1272.md) is a
  property of parameter dynamics, not of a representation's interaction
  graph. It shares the name and not the object.
- [THEORY-301](../theory.d/THEORY-301.md)'s participation ratio is of a kernel difference between two
  representations, the same formula applied to another matrix.

## Note of 2026-11-22: Stringer and colleagues, read

Stringer and colleagues ([LIT-2972](../literature.d/LIT-2972.md), [NOTE-tmp923nm](../notes.d/NOTE-tmp923nm.md), [THEORY-tmpwtoad](../theory.d/THEORY-tmpwtoad.md)): **a
parallel.** The Supplementary Discussion (§2.2) separates four dimensions
of a population code: ambient, planar (the dimension of the linear span,
close to this term's linear-span sense), manifold, and fractal (upper
Minkowski) dimension. The fractal sense has no counterpart here; it is
what a spectrum decaying more slowly than n^(−1−2/d′) for every d′ > d
gives a code of a d-dimensional stimulus set (Theorem 4). A candidate
addition if the record comes to use it. Background, so no relation.
