---
status: Proposed
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
<!-- inactive-ok-file: CLAIM-tmpy688z CLAIM-tmpym2vz CLAIM-tmpu6t8z CLAIM-tmp41gfr THEORY-1272 LIT-tmppf38y — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Deferred works registered from that exchange and not read; Proposed entries the record already held, cited for context -->

# TERM-tmplplcf: ambient, intrinsic, effective and spectral dimension (of a learned representation)

## Definition

For representations z = h(x) ∈ ℝ^D of inputs x drawn from a data
distribution:

- **Ambient dimension D**: the number of embedding coordinates, the width of
  the layer.
- **Intrinsic dimension m**: the number of degrees of freedom along the
  manifold the representations lie near, as a local estimator measures it.
  A29 §1: trained networks' representations "can have intrinsic dimensions
  far below their layer widths, and … intrinsic dimensionality changes
  systematically across layers" (Ansuini and colleagues, LIT-tmppf38y,
  Deferred: registered, not read).
- **Effective dimension D_PR**: the participation ratio of the centred
  covariance Σ, D_PR = (tr Σ)²/tr(Σ²), equal to D when all eigenvalues are
  equal and near k when k equal directions carry the variance. It sets how
  sharply norms concentrate (CLAIM-tmpy688z).
- **Spectral dimension d_s**: the exponent in the small-eigenvalue density
  ρ(λ) ∝ λ^(d_s/2 − 1) of the Laplacian of the graph through which the
  representations interact; for a regular m-dimensional geometry d_s = m.
  It sets whether long-wavelength fluctuations destroy order (CLAIM-tmpu6t8z).

## Why the record needs the word

The four come apart, and claims about high-dimensional representations
change truth value with the one meant. A29: "A dataset could lie on a
curved, 20-dimensional manifold embedded in 4,096-dimensional space. Its
interaction graph might have still another effective spectral dimension."
Concentration of measure is governed by D_PR, not D (CLAIM-tmpy688z); the
fluctuation criterion by d_s (CLAIM-tmpu6t8z); a sphere in ℝ^D is a thin shell of
intrinsic dimension D − 1, so a thin annulus is not a low-dimensional
manifold (CLAIM-tmp41gfr). The participation ratio does not estimate m: at width
768 smooth codes of manifolds of intrinsic dimension 20 to 100 all have
D_PR near 20 to 29 (CLAIM-tmpym2vz).

Three spectra go with them, and A29 §7 warns they "are not
interchangeable": the covariance spectrum (where variance lies, fixing
D_PR), the graph Laplacian spectrum (the geometry of interaction or
diffusion, fixing d_s) and the dynamical stability spectrum (which
perturbations grow, decay or persist).

## Senses kept apart

- The spectral dimension of SGD's weight drift held in THEORY-1272 is a
  property of parameter dynamics, not of a representation's interaction
  graph. It shares the name and not the object.
- THEORY-301's participation ratio is of a kernel difference between two
  representations, the same formula applied to another matrix.
