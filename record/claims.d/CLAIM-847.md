---
number: 847
status: Proposed
formerly:
- CLAIM-tmpy688z
title: 'For a Gaussian representation the relative spread of the squared norm is √(2/D_PR), with D_PR the covariance participation ratio, so concentration is set by effective rather than ambient dimension; under a rank power-law spectrum λ_j ∝ j^−α, D_PR grows as D for α below 1/2, as D/log D at 1/2, as D^(2(1−α)) between 1/2 and 1, as (log D)² at 1, and tends to a constant above 1'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    After the reading of LIT-2972 (NOTE-tmp923nm, THEORY-tmpwtoad), which
    confirms the attribution. Added in place: Stringer's Corollary 3.1
    rules out α ≤ 1 asymptotically for a code with a continuous kernel
    that keeps finite variance, so the rows α ≤ 1 describe codes whose
    trace diverges with width. LIT-2972 replaced in the grounds by its
    reading. The table and status are unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the variance identity for a Gaussian squared norm, or in the
  asymptotics of the two power sums below. Not met by non-Gaussian or
  non-power-law representations, which the claim does not cover, nor by
  slow convergence at finite width, which CLAIM-848 adds and the asymptotic
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
- QUESTION-515
uses:
- TERM-136
grounds:
- THEORY-tmpwtoad
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
<!-- inactive-ok-file: CLAIM-848 TERM-136 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->
<!-- inactive-ok-file: THEORY-tmpwtoad ARG-tmpbad4y — Proposed or new; the reading of Stringer and colleagues and the argument on its bound, 2026-11-22 -->
<!-- inactive-ok-file: THEORY-tmpwn1xp — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# CLAIM-847: For a Gaussian representation the relative spread of the squared norm is √(2/D_PR), with D_PR the covariance participation ratio, so concentration is set by effective rather than ambient dimension; under a rank power-law spectrum λ_j ∝ j^−α, D_PR grows as D for α below 1/2, as D/log D at 1/2, as D^(2(1−α)) between 1/2 and 1, as (log D)² at 1, and tends to a constant above 1

## The claim

**Effective dimension sets concentration.** A30 §5: for z ∼ N(0, Σ),
E‖z‖² = tr Σ and Var ‖z‖² = 2 tr(Σ²), so

SD(‖z‖²)/E‖z‖² = √(2/D_PR), with D_PR = (tr Σ)²/tr(Σ²).

"For this Gaussian model, the strength of relative radial concentration is
controlled by the **effective covariance dimension**, rather than directly by
ambient dimension." Variance in 20 orthogonal directions of a 4,096-wide
layer gives D_PR ≈ 20 ([TERM-136](../terms.d/TERM-136.md)).

**Power-law spectra set how it scales.** A29 §7 recalls covariance spectra
λ_j ∝ j^(−α), observed in neural population responses (Stringer and
colleagues, [LIT-2972](../literature.d/LIT-2972.md), read 2026-11-22 as [THEORY-tmpwtoad](../theory.d/THEORY-tmpwtoad.md)), with residual
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

**Which rows a code can keep.** Stringer's Corollary 3.1 (Supplementary
Discussion §2.5): a code with finite population variance and a continuous
kernel has λ_n = o(n^(−1)). So the rows α ≤ 1 describe codes whose trace,
tr Σ = Σ_(j≤D) j^(−α), diverges as width grows (as log D at α = 1); held as
width grows, such a code is, for Stringer, discontinuous or of infinite
variance. At any fixed width every row is a possible spectrum; the
restriction is on how a family of codes scales.

*Changed 2026-11-22, version 2:* the paragraph above added; the citation
of Stringer updated to the reading.

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
  widths tell the regimes apart. That is the assistant's [CLAIM-848](CLAIM-848.md).
- **Gaussian and centred.** The identity is for a centred Gaussian. For
  other laws Var ‖z‖² adds fourth cumulants; a nonzero mean must be removed
  first (A30 §9 says "centered"). Real embeddings are neither isotropic nor
  pure power laws, which A30 itself names.
- **Three spectra.** The covariance spectrum here is not the graph
  Laplacian's or the stability spectrum's (A29 §7, kept apart in [TERM-136](../terms.d/TERM-136.md)).

## Note of 2026-11-22: Stringer and colleagues, read

Stringer and colleagues ([LIT-2972](../literature.d/LIT-2972.md)) were read ([NOTE-tmp923nm](../notes.d/NOTE-tmp923nm.md),
[THEORY-tmpwtoad](../theory.d/THEORY-tmpwtoad.md)). **Supports the attribution, as background.** The
spectrum is a power law with exponent "just above 1 (1.04±0.02 SE ...)",
fitted over ranks 11 to 500, and the residual variance k^(1−α) is the
tail-sum device of the supplement's Theorem 4. **Adds** the restriction
above: Corollary 3.1 rules out α ≤ 1 asymptotically for codes keeping
finite variance with a continuous kernel. [CLAIM-848](CLAIM-848.md)'s use of the bound is
corrected in place to its strict, tail-only form ([ARG-tmpbad4y](../arguments.d/ARG-tmpbad4y.md)).

## Note of 2026-11-22: Ansuini and colleagues, read

Ansuini, Laio, Macke and Zoccolan (LIT-2998, NOTE-tmptf55k, THEORY-tmpwn1xp): **background, with
a pointed control.** The paper does not treat norms. Its covariance-matched
Gaussian, with "the same second-order moments" as the representations, has
an intrinsic dimension "two orders of magnitude larger", growing with N:
second moments, which fix D_PR and with it this claim's norm spread, do not
fix nearest-neighbour geometry. Consistent with this claim's scope, a
Gaussian representation, and a warning against carrying it to real
representations' local geometry. No relation.
