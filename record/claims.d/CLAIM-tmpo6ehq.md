---
status: Proposed
title: 'Ott and Antonsen''s family of oscillator distributions, with phase Fourier coefficients αⁿ, stays invariant only when the coupling carries the first harmonic of the phase alone: a second harmonic couples each coefficient to the one two places below, which for the first coefficient is the conjugate α* and for the others is a power of α, so the family is left everywhere except at full locking, |α| = 1'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation or the check: a phase velocity with a nonzero
  second harmonic, ω + Im(He^{−iθ}) + Im(H₂e^{−2iθ}) with H₂ ≠ 0, under
  which the family Fₙ = αⁿ with |α| < 1 is invariant, that is, the Fourier
  hierarchy's right-hand side at Fₙ = αⁿ equals nαⁿ⁻¹ α̇ for one α̇ and
  every n.
tags:
- complex-systems
- mathematics
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
grounds:
- THEORY-tmpmvcnr
bears_on:
- QUESTION-252
summary: >-
  Fills a gap in Ott and Antonsen 2008 (NOTE-tmpd7trg): the paper uses
  first-harmonic coupling throughout and does not say that the invariance
  needs it, and the verdict on whether its reduction is typical enough to
  be CLAIM-478's defeater (a) turns on that. Derived and checked
  numerically (scratch/studies/lead-094/oa_invariance.py, with a pytest).
  The result is known in the literature on higher-harmonic coupling, which
  the record does not hold; it is filed here as the record's own check.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpmvcnr CLAIM-478 — Proposed; the reading this fills a gap in and the claim the gap matters for -->

# CLAIM-tmpo6ehq: Ott and Antonsen's family of oscillator distributions, with phase Fourier coefficients αⁿ, stays invariant only when the coupling carries the first harmonic of the phase alone: a second harmonic couples each coefficient to the one two places below, which for the first coefficient is the conjugate α* and for the others is a power of α, so the family is left everywhere except at full locking, |α| = 1

## The derivation

Write the continuum distribution as f = (g/2π)[1 + Σₙ≥₁ (Fₙe^{inθ} + c.c.)],
with F₀ = 1 and F₋ₘ = Fₘ*. For a phase velocity
v = ω + (1/2i)(He^{−iθ} − H*e^{iθ}) + (1/2i)(H₂e^{−2iθ} − H₂*e^{2iθ}), the
continuity equation ∂f/∂t + ∂(vf)/∂θ = 0 gives, for n ≥ 1,

dFₙ/dt = −inωFₙ − (n/2)(HFₙ₊₁ − H*Fₙ₋₁) − (n/2)(H₂Fₙ₊₂ − H₂*Fₙ₋₂).

Put Fₙ = αⁿ and divide by nαⁿ⁻¹. For n ≥ 2 the right-hand side becomes
−iωα − (1/2)(Hα² − H*) − (1/2)(H₂α³ − H₂*α⁻¹), the same for every n. For
n = 1 the last term has F₋₁ = α* in place of α⁻¹. So the family is
invariant, with one α̇ serving every n, only if H₂*(α* − α⁻¹) = 0: either
H₂ = 0, which is Ott and Antonsen's case (their eq. 6), or |α| = 1, the fully
locked state. A harmonic m > 1 should fail the same way, at the coefficients n < m whose
partner index n − m runs below zero; only the second harmonic was checked.

## The check

`scratch/studies/lead-094/oa_invariance.py` evaluates the hierarchy at
Fₙ = αⁿ for n up to 8, reads α̇ off n = 1, and reports the largest mismatch
|dFₙ/dt − nαⁿ⁻¹α̇| over n = 2..8. Over five random draws with |α| = 0.6, the
mismatch was 1–4 × 10⁻¹⁶ with H₂ = 0, and 0.10–0.14 with |H₂| between 0.15 and 0.23;
at |α| = 1 with H₂ ≠ 0 it was 2 × 10⁻¹⁵. A pytest
(`test_oa_invariance.py`) holds the three cases.

## What it does not say

- Not that a reduction fails for higher harmonics: other low-dimensional
  descriptions may exist; only this family stops being invariant.
- Not how far off the family a weakly second-harmonic population drifts,
  or how fast; that would need a simulation.
- Not that first-harmonic coupling is rare. Phase reduction of weakly
  coupled limit-cycle oscillators yields a general periodic coupling
  function, of which the first harmonic is the leading term; how often it
  is the whole of it is left open.
