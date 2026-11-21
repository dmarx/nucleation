---
status: Proposed
title: 'For a Gaussian representation the relative spread of the squared norm is √(2/D_PR), with D_PR the covariance participation ratio, so concentration is set by effective rather than ambient dimension; under a rank power-law spectrum λ_j ∝ j^−α, D_PR grows as D for α below 1/2, as D/log D at 1/2, as D^(2(1−α)) between 1/2 and 1, as (log D)² at 1, and tends to a constant above 1'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the variance identity for a Gaussian squared norm, or in the
  asymptotics of the two power sums below. Not met by non-Gaussian or
  non-power-law representations, which the claim does not cover, nor by
  slow convergence at finite width, which CLAIM-tmpym2vz adds and the asymptotic
  statement does not deny.
tags:
- representation-learning
- mathematics
- mathematical-statistics
date: '2026-11-21'
line:
- learned-structure
- formal-apparatus
bears_on:
- QUESTION-tmpvu6cb
uses:
- TERM-tmplplcf
grounds:
- LIT-tmp7uzka
summary: >-
  A30 §5 of the exchange "Rich Get Richer Power Laws" (2026-11-21), with
  the power-law spectrum of A29 §7: the Gaussian annulus generalizes to
  anisotropic covariance with the participation ratio in place of D, and a
  rank power-law spectrum fixes how that ratio grows with width. A30:
  "Power-law covariance spectra can dramatically change how concentration
  of measure scales with representation dimension." The bridge between the
  exchange's power-law thread and its high-dimensional one. The wording is
  A's (the other assistant in the exchange "Rich Get Richer Power Laws",
  A29 and A30); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpym2vz TERM-tmplplcf LIT-tmp7uzka — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Deferred works registered from that exchange and not read -->

# CLAIM-tmpy688z: For a Gaussian representation the relative spread of the squared norm is √(2/D_PR), with D_PR the covariance participation ratio, so concentration is set by effective rather than ambient dimension; under a rank power-law spectrum λ_j ∝ j^−α, D_PR grows as D for α below 1/2, as D/log D at 1/2, as D^(2(1−α)) between 1/2 and 1, as (log D)² at 1, and tends to a constant above 1

## The claim

**Effective dimension sets concentration.** A30 §5: for z ∼ N(0, Σ),
E‖z‖² = tr Σ and Var ‖z‖² = 2 tr(Σ²), so

SD(‖z‖²)/E‖z‖² = √(2/D_PR), with D_PR = (tr Σ)²/tr(Σ²).

"For this Gaussian model, the strength of relative radial concentration is
controlled by the **effective covariance dimension**, rather than directly by
ambient dimension." Variance in 20 orthogonal directions of a 4,096-wide
layer gives D_PR ≈ 20 (TERM-tmplplcf).

**Power-law spectra set how it scales.** A29 §7 recalls covariance spectra
λ_j ∝ j^(−α), observed in neural population responses (Stringer and
colleagues, LIT-tmp7uzka, Deferred: registered, not read), with residual
variance beyond rank k ∝ k^(1−α) for α > 1. A30 §5 then gives, for
D_PR = (Σ_(j≤D) j^(−α))²/Σ_(j≤D) j^(−2α):

| α | D_PR as D grows |
|---|---|
| 0 ≤ α < 1/2 | ∝ D |
| α = 1/2 | ∝ D/log D |
| 1/2 < α < 1 | ∝ D^(2(1−α)) |
| α = 1 | ∝ (log D)² |
| α > 1 | tends to a constant, ζ(α)²/ζ(2α) |

So above α = 1 "the embedding can have arbitrarily large ambient dimension
while retaining only a finite effective number of variance-bearing
directions. Its radial concentration need not become arbitrarily sharp";
below it, a flat enough spectrum concentrates norms strongly.

## Checked

- The identity: for independent N(0, λ_k) coordinates in Σ's eigenbasis,
  Var ‖z‖² = Σ 2λ_k² = 2 tr(Σ²).
- The table: computed in this session (python3 -I) by direct summation to
  D = 10⁶. The α = 1 row matches (6/π²)(ln D + γ)², to five digits at
  D = 10⁶ (125.93 both); the α > 1 limits are ζ(α)²/ζ(2α) (7.73 at α = 1.4,
  reached by D ≈ 10⁵). The table is right as an asymptotic statement.
- At D = 768 the relative spread √(2/D_PR) of the squared norm is 0.051 for
  a flat spectrum, 0.25 at α = 1 (D_PR = 31.7) and 0.39 at α = 1.2: a
  power-law representation of that width sits in a far thicker shell than
  the isotropic annulus.

## Gaps

- **Finite width.** Near α = 1, where Stringer's bound and the observed
  spectra sit, the asymptotic regimes are reached only at widths far beyond
  any network's, so the table does not let a measurement at realistic
  widths tell the regimes apart. That is the assistant's CLAIM-tmpym2vz.
- **Gaussian and centred.** The identity is for a centred Gaussian. For
  other laws Var ‖z‖² adds fourth cumulants; a nonzero mean must be removed
  first (A30 §9 says "centered"). Real embeddings are neither isotropic nor
  pure power laws, which A30 itself names.
- **Three spectra.** The covariance spectrum here is not the graph
  Laplacian's or the stability spectrum's (A29 §7, kept apart in TERM-tmplplcf).
