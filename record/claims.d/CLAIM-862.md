---
number: 862
status: Proposed
formerly:
- CLAIM-tmpvq33w
title: 'Protected couplings give scale-free phases'
statement: >-
  In the KPZ interface, the ordered Toner–Tu flock and the two-dimensional
  XY phase, a symmetry or a conservation law protects a coupling or forbids
  a restoring term, so that scale-free behaviour holds over a whole phase
  with nothing tuned; a perturbation that breaks the protection, such as an
  explicit preferred direction, a finite interaction range or, for KPZ, more
  than two dimensions at weak coupling, restores a characteristic scale or
  puts a tuned point back
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A reading of one of the three cases showing that its untuned scaling
  does not depend on the protection named (that the KPZ exponents survive
  a term breaking the tilt symmetry, the flock's anomalous fluctuations
  survive a compass, or the XY phase's algebraic order survives a finite
  interaction range); or a fourth case, in the same class of
  field-theoretic systems, with a protected coupling and no restoring
  term that nonetheless needs tuning to be scale free.
tags:
- complex-systems
- natural-sciences
- thermodynamics
date: '2026-11-22'
line:
- formal-apparatus
bears_on:
- QUESTION-508
complements:
- CLAIM-841
grounds:
- THEORY-2202
- THEORY-2198
- THEORY-2199
- THEORY-2206
- THEORY-2197
summary: >-
  Fills a gap the readings of 2026-11-22 found: [QUESTION-508](../questions.d/QUESTION-508.md) asks what a
  system must have for its long-distance behaviour to sit at a fixed
  point with nothing left to tune, and [CLAIM-841](CLAIM-841.md) lists the routes without
  saying what three of them share. Read, KPZ (tilt invariance; the
  coupling's relevance by dimension), Toner and Tu (pseudo-Galilean
  invariance and mass conservation; a compass gives a mass) and BKT (U(1)
  symmetry in exactly two dimensions; a finite penetration depth frees
  the vortices) share one shape: a protection, and a perturbation that
  undoes it. It does not say that every untuned power law has this
  source, and the BKT case needs the dimension as well as the symmetry.
  The wording is the assistant's (Claude, in this session); adopting it
  is the owner's call.
---
<!-- inactive-ok-file: THEORY-2202 THEORY-2198 THEORY-2199 THEORY-2206 THEORY-2197 — Proposed; the readings of 2026-11-22 this claim rests on -->
<!-- inactive-ok-file: CLAIM-841 TERM-139 THEORY-1095 — Proposed; the claim this complements and the entries it uses -->

# CLAIM-862: Protected couplings give scale-free phases

## The gap it fills

[QUESTION-508](../questions.d/QUESTION-508.md) asks why some systems are scale free without tuning, and
[CLAIM-841](CLAIM-841.md) lists routes that are. The readings of 2026-11-22 of three of
those routes show a common shape that neither entry states, and A27 §6's
"A symmetry can protect scale-free fluctuations, and explicitly breaking
that symmetry can introduce a characteristic scale" names only for the
Goldstone case.

## The three cases

| Case | What protects | What it protects | What undoes it |
|---|---|---|---|
| KPZ interface ([THEORY-2202](../theory.d/THEORY-2202.md), [THEORY-2198](../theory.d/THEORY-2198.md)) | invariance under h → h + const and a small tilt | no restoring term ∝ h (the reading's inference, not the paper's words); λ not renormalized, χ + z = 2 | in d > 2 a small λ is irrelevant: a tuned threshold g* ≃ d − 2 separates the smooth phase from KPZ |
| Toner–Tu flock ([THEORY-2199](../theory.d/THEORY-2199.md)) | rotation invariance; pseudo-Galilean invariance at λ₁ = λρ; mass conservation | no mass for v⊥; λ₁, ∆, D∥ not renormalized in d = 2, so χ = 1 − z | a compass "will introduce a "mass"", leaving "no interesting fluctuations" (p. 63) |
| 2D XY phase ([THEORY-2206](../theory.d/THEORY-2206.md), [THEORY-2197](../theory.d/THEORY-2197.md)) | U(1) symmetry, with d = 2 | a vortex's energy and entropy both ∝ ln L, so the fugacity is irrelevant along a line of fixed points | a finite penetration depth cuts off the logarithm and frees vortices "at any T > 0" (p. 98) |

In each, the scale-free behaviour belongs to a whole phase, as the flock
paper puts it, to "the low temperature fixed point" and not to "the
fixed point that controls the order-disorder transition" (Toner and Tu,
p. 64); and in each the phase is entered without setting a parameter to a
special value. In the language of [TERM-139](../terms.d/TERM-139.md), the protection keeps every
relevant direction at the fixed point (or fixed line) at zero, or makes
the one candidate perturbation irrelevant.

## What it does not say

- **That every untuned power law has this source.** [CLAIM-841](CLAIM-841.md) lists
  others: sustained flux, cumulative advantage, coarsening, geometric
  recursion, broad relaxation spectra, and self-organized criticality,
  where nothing is protected and feedback or growth does the work.
- **That symmetry suffices for BKT.** The XY case needs the dimension as
  well: the logarithmic interaction is a two-dimensional fact, and in
  three dimensions the same U(1) symmetry gives true long-range order and
  a tuned transition. KPZ too needs d ≤ 2 for its untuned reach.
- **That the protection is exact in each case.** The flock's d = 2
  exactness rests on a flow the authors call "highly probable"
  ([THEORY-1095](../theory.d/THEORY-1095.md)'s question); the KPZ exponents are exact only in d = 1.
- **That every perturbation listed is in the readings.** The compass,
  the penetration depth and d > 2 are; a pinning term breaking KPZ's
  shift symmetry, which would give a restoring term ∝ h and a finite
  correlation length, is the assistant's inference, not read.

## How it bears on [QUESTION-508](../questions.d/QUESTION-508.md)

A partial criterion for one class: in field theories of this kind, look
for the symmetry or conservation law that keeps each relevant direction
at zero, and for the perturbation that would break it; the system is
scale free without tuning where the protection holds and the dimension
permits. It is a narrowing, not an answer: it says nothing of feedback,
flux or growth routes.
