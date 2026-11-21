---
status: Proposed
title: "If a representation's collective deformations have a local Gaussian elastic energy on an interaction graph of spectral dimension d_s, their long-wavelength fluctuations diverge for d_s at or below 2, so whether conventional order survives is set by the spectral dimension of the interaction geometry, not by layer width"
version: 1
role: supposed
warrant: demonstrated
tags:
- representation-learning
- complex-systems
- mathematics
date: '2026-11-21'
line:
- learned-structure
bears_on:
- QUESTION-tmpvu6cb
uses:
- TERM-tmplplcf
grounds:
- THEORY-2047
- THEORY-2051
- LIT-tmph28ji
summary: >-
  A29 §6 of the exchange "Rich Get Richer Power Laws" (2026-11-21):
  equipartition over the Laplace modes of an interaction graph whose
  eigenvalue density goes as λ^(d_s/2 − 1) makes the mean-square
  deformation diverge at small λ for d_s ≤ 2, the lower critical dimension
  of the Mermin–Wagner theorem read on a learned manifold. Supposed: every
  premise (a local elastic energy, equilibrium fluctuations, a chosen
  graph) is assumed, not derived from training. The wording is A's (the
  other assistant in the exchange "Rich Get Richer Power Laws", A29);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-tmplplcf CLAIM-tmp526xr THEORY-2047 THEORY-2051 THEORY-1272 LIT-tmph28ji — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Deferred works registered from that exchange and not read; Proposed entries the record already held, cited for context -->

# CLAIM-tmpu6t8z: If a representation's collective deformations have a local Gaussian elastic energy on an interaction graph of spectral dimension d_s, their long-wavelength fluctuations diverge for d_s at or below 2, so whether conventional order survives is set by the spectral dimension of the interaction geometry, not by layer width

## The claim

A29 §6 supposes a collective deformation field u on the learned manifold M
with energy F[u] = (κ/2)∫_M ‖∇_M u‖² dV. Expanding u in the eigenfunctions
of the Laplace–Beltrami operator, −Δ_M φ_n = λ_n φ_n, gives
F = (κ/2)Σ λ_n |a_n|², and for "equilibrium-like Gaussian fluctuations"
⟨|a_n|²⟩ ∝ T_eff/(κ λ_n), the spin-wave spectrum. If the small-eigenvalue
density goes as ρ(λ) ∝ λ^(d_s/2 − 1), which defines the spectral dimension
d_s of the interaction geometry (TERM-tmplplcf), then

⟨u²⟩ ∼ ∫_0^Λ ρ(λ)/λ dλ ∼ ∫_0^Λ λ^(d_s/2 − 2) dλ,

which diverges at the lower limit for d_s ≤ 2, logarithmically at d_s = 2.
"That's the same lower-critical-dimensional phenomenon we encountered in the
XY model": the Mermin–Wagner theorem (LIT-tmph28ji, Deferred: registered,
not read), read on the learned interaction graph.

The conclusion A29 draws: "A high ambient dimension does not tell us whether
the representation has these fluctuation properties." A 4,096-wide layer
whose interactions live on a graph of low spectral dimension can still have
strong long-wavelength fluctuations; "the governing collective dimension may
be neither the neural layer width nor even the manifold's ordinary intrinsic
dimension, but the effective spectral dimension of the network-mediated
interactions" (A29 §12).

The integral is checked: for ρ(λ) = λ^(d_s/2 − 1) on (0, 1] the integral of
ρ/λ is finite, 1/(d_s/2 − 1), exactly when d_s > 2.

## Why it is only supposed

The filing found these premises assumed, not derived (they are A29's own
caveats, made sharper):

- **The elastic energy.** No continuous symmetry that a trained
  representation breaks is identified, and the field u is never defined, so
  there is no Goldstone mode for the spectrum to describe. A29 itself: "the
  existence of such an elastic description must be derived or justified
  from the training dynamics".
- **Equilibrium.** T_eff presumes a fluctuation–dissipation relation, which
  A29 §4 doubts for training.
- **Which graph.** d_s is a property of a graph's Laplacian, and A29 does
  not say which: a k-nearest-neighbour graph of the embeddings, the kernel
  K_ij of CLAIM-tmp526xr, or the data's adjacency. The criterion d_s ≤ 2 depends on
  the choice. The record's held spectral dimension of SGD's drift
  (THEORY-1272) is a fourth, different object.
- **Zero modes.** A29: "not every near-zero eigenmode represents a physical
  Goldstone mode. Some can be artifacts of parameter redundancy, arbitrary
  rotations of embedding coordinates, or weakly constrained features."

## What the record holds

THEORY-2047 (Laplacian eigenmaps) holds the graph Laplacian's low modes as an
embedding; THEORY-2051 holds a symmetry-broken phase with Goldstone-type
behaviour in equivariant deep networks at initialisation. Neither holds the
fluctuation criterion.
