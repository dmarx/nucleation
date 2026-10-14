---
number: 325
status: Proposed
formerly:
- THEORY-tmpyhatw
promote_when: >-
  A reading here of the stochastic-stability theorems the paper leans on
  (Has'minskii 1980; Arnold & Kliemann 1983; Colonius & Kliemann 1993)
  confirming that, for dimension at least 2 and noise matrices neither
  skew-symmetric nor commuting with the mean operator, multiplicative
  white noise of sufficient amplitude gives a positive top Lyapunov
  exponent, and a computation or theorem showing the threshold falls as
  the mean operator's non-normality rises. The first half of the claim
  (non-normality necessary; a non-normal operator stable at every
  instant can be destabilized) already rests on a bound and explicit
  examples. What cannot settle it: more simulations of particular
  systems, which add instances, not generality.
title: 'Time dependence can destabilize a non-normal linear system that is stable at every instant; non-normality is necessary for this, and random variation of the operator destabilizes generically, needing less variation the more non-normal and less damped the mean operator'
version: 1
tags:
- mathematics
- complex-systems
- natural-sciences
date: '2026-10-14'
source:
- LIT-929
summary: >-
  Farrell & Ioannou (1996), Part II, [LIT-929](../literature.d/LIT-929.md), read in [NOTE-842](../notes.d/NOTE-842.md).
  Necessity is a one-line bound and the destabilization is shown in
  explicit examples. Genericity under noise is cited to stochastic
  stability theory, and the role of non-normality and damping is shown
  numerically. In the deterministic examples, variation much faster than
  the transient growth destabilizes nothing.
---
<!-- inactive-ok-file: CLAIM-186 — Proposed; the claim this account bears on, open -->
<!-- inactive-ok-file: THEORY-323 — Proposed; the autonomous account this one extends -->

# THEORY-325: Time dependence can destabilize a non-normal linear system that is stable at every instant; non-normality is necessary for this, and random variation of the operator destabilizes generically, needing less variation the more non-normal and less damped the mean operator

## Source

Farrell & Ioannou, "Generalized Stability Theory. Part II: Nonautonomous
Operators" (1996), [LIT-929](../literature.d/LIT-929.md), read in full in [NOTE-842](../notes.d/NOTE-842.md): §2 (eqs.
1–7), §4 (eqs. 10–26), §5 (eqs. 27–37), Figs. 6–9.

## What was actually shown

For du/dt = A(t)u, stability is the sign of the first Lyapunov exponent
λ = lim sup ln‖Φ(t)‖/t (eq. 6).

- **Non-normality is necessary (eq. 12).** Since d‖u‖²/dt =
  u†(A + A†)u, λ lies between the long-run averages of the smallest and
  largest eigenvalues of (A(t) + A†(t))/2. For a normal operator the
  largest is the spectral abscissa, so an operator that is normal and
  stable at every instant has a negative exponent. A stable operator
  can be destabilized by time variation only if it is non-normal.
- **It happens (§4).**
  - An undamped oscillator whose frequency switches between 0.5 and 3
    every T units, neutral at every instant, has a positive exponent
    except near integer multiples of half a period (Fig. 6). The
    authors state that this persists with damping, when the operator is
    stable at each instant, without showing it.
  - A 2 × 2 operator with eigenvalues ±i, neutral at every instant and
    randomly rotated at each step, has a positive exponent for every
    angle between its eigenvectors except π/2, increasing with the
    non-normality (Fig. 7).
  - The mechanism: "transient growth instigated at the starting time is
    continued with further growth when the switch to the second operator
    takes place, forestalling the decay that would occur in the
    autonomous case."
- **Random variation destabilizes generically (§§4–5).** For A(t) =
  Ā + εΣξ_i(t)B_i with Stratonovich white noise, the paper cites
  Has'minskii and Colonius & Kliemann for a positive exponent at
  sufficient ε, in dimension ≥ 2, when the B_i are neither skew-symmetric
  nor commute with Ā. If they commute, one basis diagonalizes both and
  noise cannot destabilize.
- **Non-normality lowers the threshold; damping raises it (Figs. 8–9).**
  For a damped oscillator with noisy restoring force, the exponent falls
  with damping and rises with noise. In a three-layer baroclinic model
  the noise needed falls as the shear, which sets the non-normality,
  rises. At typical shear a positive exponent appears for wind
  fluctuations of about 10%, and reaches about 1/5 day⁻¹ at 30%.

What could have come out otherwise: the examples and the numerical
dependence on shear and damping. Necessity is a bound.

## What this does not say

- **It does not say any time variation destabilizes.** In both
  deterministic examples the exponent vanishes as the switching interval
  goes to zero (T → 0; δt → 0 in eq. 26). Variation much faster than
  the transient growth averages out. Only under white noise scaled as
  δt^{−1/2} does the fast limit stay unstable. Which case a real system
  resembles depends on how its variation is correlated in time.
- **It does not prove genericity itself.** That rests on cited theorems
  not read here, and on low-dimensional numerical examples.
- **It does not say damping is irrelevant.** Damping "of sufficient
  magnitude is able to asymptotically stabilize the Lyapunov exponents,
  even with high temporal variability" (§5).
- **It does not settle mean-square behaviour.** The stability meant is
  sample stability, an almost surely negative exponent. For stochastic
  systems the second-moment exponent can be unstable when the sample
  exponent is not (μ₂ ≥ 2λ only).
- **It does not settle where the atmosphere's error growth comes
  from.** That long-range forecast error comes from the flow's time
  dependence rather than intrinsic chaos is the paper's suggestion, from
  a three-layer model.

## Connections

No relations are declared.

- **[THEORY-323](THEORY-323.md).** The autonomous account, where non-normality gives
  transient growth only. This one says time variation can turn that
  transient growth into asymptotic instability.
- **[CLAIM-186](../claims.d/CLAIM-186.md).** Its note says an argument under development is the
  nonautonomous case and so has "no fixed modes to appeal to". This
  account goes further, and against the note's comfort: a structure that
  is stable at every snapshot need not settle if it keeps changing and
  is non-normal. Read across, it also names what would restore settling:
  a normal structure, enough damping, or, in the deterministic examples,
  change much faster than the transient growth. Which of these anchoring
  corresponds to is the reading's question, not the paper's.
