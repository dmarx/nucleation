---
number: 724
status: Active
formerly:
- THEORY-tmp8dvpa
title: 'For a linear system du/dt = A(t)u, non-normality is necessary for time dependence to destabilize an operator that is uniformly stable at every instant, and a non-normal operator neutral at every instant can be asymptotically unstable under switching'
version: 2
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-325 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-325.yaml, batch 006, ADR-047).
    THEORY-325 bundled a deterministic half, which rests on a one-line
    bound and explicit examples (NOTE-842's claims C2 and C3, both
    strong), with a stochastic half that rests on cited theorems and
    numerics. This THEORY holds the deterministic half. Necessity is stated
    with the uniform condition α(t) ≤ −c < 0, which the bound needs. The
    stable-at-every-instant case, which the paper asserts without showing,
    is CLAIM-376, the record's own construction. THEORY-325 keeps
    the stochastic half and extends this one.
- version: 2
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-281 and corroborates CLAIM-376, at the reading
    review of 2026-11-11 (by topic, mathematics; ADR-091). The
    question names it as evidence: "A transient can leave a regime
    whose every eigenvalue is stable. Non-normal growth does so
    (THEORY-724; Trefethen et al., LIT-932, read)." The claim proves
    the case this reading's source asserts: its summary, "The case
    THEORY-724's source asserts and does not show", and its body, "It
    inherits A(t)'s non-normality, as THEORY-724's bound requires."
    The claim grounds on LIT-929 and does not need the reading, so
    corroborates. No other change.
tags:
- mathematics
- complex-systems
date: '2026-10-19'
source:
- LIT-929
summary: >-
  Farrell & Ioannou (1996), Part II, [LIT-929](../literature.d/LIT-929.md), eq. 12 and §4, read in
  [NOTE-842](../notes.d/NOTE-842.md). Because d‖u‖²/dt = u†(A + A†)u, the first Lyapunov exponent
  lies between the long-run averages of the extreme eigenvalues of the
  Hermitian part. For a normal operator the largest is the spectral
  abscissa, so an operator that is normal and uniformly stable at every
  instant has a negative exponent. A switched undamped oscillator, neutral
  at every instant, has a positive exponent. The stochastic genericity
  results are [THEORY-325](THEORY-325.md)'s, still Proposed.
bears_on:
- QUESTION-281
corroborates:
- CLAIM-376
---
<!-- inactive-ok-file: THEORY-325 — Proposed; the stochastic account this half was split from and that extends it, cited as open -->

# THEORY-724: For a linear system du/dt = A(t)u, non-normality is necessary for time dependence to destabilize an operator that is uniformly stable at every instant, and a non-normal operator neutral at every instant can be asymptotically unstable under switching

## Source

Farrell & Ioannou, "Generalized Stability Theory. Part II: Nonautonomous
Operators" (1996), [LIT-929](../literature.d/LIT-929.md), read in full in [NOTE-842](../notes.d/NOTE-842.md): §2 (eqs. 1–7), eq. 12,
§4 (eqs. 13–26), Figs. 6–7.

## What was actually shown

For du/dt = A(t)u, stability is the sign of the first Lyapunov exponent
λ = lim sup ln‖Φ(t)‖/t (eq. 6), with Φ the propagator.

- **Non-normality is necessary (eq. 12).** Since
  d‖u‖²/dt = u†(A + A†)u, the exponent satisfies
  lim sup (1/t)∫λ_min dt ≤ λ ≤ lim sup (1/t)∫λ_max dt, where λ_min and
  λ_max are the extreme eigenvalues of (A(t) + A†(t))/2. For a normal
  operator λ_max is the spectral abscissa α(t) = max Re spec A(t). So if
  A(t) is normal and α(t) ≤ −c < 0 for every t, then λ ≤ −c. The condition
  must be uniform: with α(t) < 0 tending to 0, the bound gives only λ ≤ 0.
- **It happens.** The oscillator d/dt(x, v) = [[0, 1], [−ω²(t), 0]](x, v),
  with ω switching between 0.5 and 3 every T units, is neutral at every
  instant (eigenvalues ±iω) and non-normal. Its exponent is positive except
  near integer multiples of half a period (Fig. 6). A 2 × 2 operator with
  eigenvalues ±i, randomly rotated at each step, has a positive exponent
  for every angle between its eigenvectors except π/2 (Fig. 7).
- **The mechanism.** "Transient growth instigated at the starting time is
  continued with further growth when the switch to the second operator
  takes place, forestalling the decay that would occur in the autonomous
  case."

Necessity is a bound, so what could show it wrong is an error in that
line. The examples could have come out stable, and did not.

## What this does not say

- **That the paper shows the stable-at-every-instant case.** It shows
  neutral cases and states that damping preserves the effect without
  showing it. The record closes that case in [CLAIM-376](../claims.d/CLAIM-376.md).
- **That any time variation destabilizes.** The exponent vanishes as the
  switching interval goes to zero. Variation much faster than the transient
  growth averages out.
- **Anything about random variation in general.** Genericity under
  multiplicative noise, and how the threshold depends on non-normality and
  damping, are [THEORY-325](THEORY-325.md)'s, still Proposed.
