---
number: 323
status: Proposed
formerly:
- THEORY-tmpwdx4q
promote_when: >-
  A reading of a standard reference that proves the general statements
  rather than collecting them, such as Trefethen & Embree's Spectra and
  Pseudospectra or Schmid & Henningson's Stability and Transition in Shear
  Flows, confirming that for any norm the growth over time t is
  ‖e^{At}‖, that the numerical abscissa bounds it as t → 0, and that the
  white-noise variance equals the equivalent normal variance only when A
  is normal. What cannot settle it: more examples of transient growth in
  particular systems, which illustrate the claim and do not prove it.
title: 'For a non-normal linear operator the eigenvalues govern only the long-run limit: a system whose every mode decays can amplify perturbations over finite times, and hold more forced variance, by factors its spectrum does not predict'
version: 1
tags:
- mathematics
- complex-systems
- natural-sciences
date: '2026-10-14'
source:
- LIT-931
- LIT-932
summary: >-
  Farrell & Ioannou (1996), [LIT-931](../literature.d/LIT-931.md), read in [NOTE-831](../notes.d/NOTE-831.md), with Trefethen
  et al. (1993), [LIT-932](../literature.d/LIT-932.md), read in [NOTE-839](../notes.d/NOTE-839.md). Linear algebra, worked in
  examples: growth over time t is the top singular value of the
  propagator, which the eigenvalues bound from below, not above. It holds
  in a chosen norm, and a norm can always be found that makes the
  operator normal. It says nothing about whether the growth survives
  nonlinearity.
---
<!-- inactive-ok-file: CLAIM-186 — Proposed; the claim this account bears on, open -->
<!-- inactive-ok-file: THEORY-304 THEORY-325 — Proposed; companion accounts filed from the same readings -->

# THEORY-323: For a non-normal linear operator the eigenvalues govern only the long-run limit: a system whose every mode decays can amplify perturbations over finite times, and hold more forced variance, by factors its spectrum does not predict

## Source

Farrell & Ioannou, "Generalized Stability Theory. Part I: Autonomous
Operators" (1996), [LIT-931](../literature.d/LIT-931.md), read in full in [NOTE-831](../notes.d/NOTE-831.md): §2 (eqs.
1–10), §3 (eqs. 11–31), §4 (examples). Trefethen, Trefethen, Reddy &
Driscoll, "Hydrodynamic Stability Without Eigenvalues" (1993), [LIT-932](../literature.d/LIT-932.md),
read in full in [NOTE-839](../notes.d/NOTE-839.md): eqs. 5–13.

## What was actually shown

For du/dt = Au, with A fixed in time and growth measured in a chosen
inner-product norm:

- **Normal operators are governed by their eigenvalues.** If AA† = A†A,
  ‖e^{At}‖ = e^{λ^R_max t}, with λ^R_max the largest real part of an
  eigenvalue ([LIT-931](../literature.d/LIT-931.md), §2).
- **Non-normal operators are not, except as t → ∞.**
  - Growth over time t is ‖e^{At}‖, the largest singular value of the
    propagator, and the optimal perturbation is the matching right
    singular vector ([LIT-931](../literature.d/LIT-931.md), eqs. 4–5).
  - The eigenvalues give a floor, not a ceiling: σ²_max ≥
    e^{(λ_i+λ_i*)t} for every eigenvalue (eq. 6).
  - At t → 0 the growth rate is the numerical abscissa, the top
    eigenvalue of (A + A†)/2, which can be positive when every mode
    decays (eq. 10).
  - At t → ∞ the leading mode wins, but it is best excited by its
    adjoint vector, not by itself (eqs. 8–9).
- **The forced response is larger too.**
  - The response to harmonic forcing is bounded by κ(E)/dist(iω, Λ(A)),
    not 1/dist ([LIT-931](../literature.d/LIT-931.md), eq. 19).
  - Large resonance can occur far from any eigenvalue: "pseudoresonance"
    ([LIT-932](../literature.d/LIT-932.md), eqs. 5–7).
  - Under spatially uncorrelated white noise, the spectral density
    trace(R†R) is at least the sum of the pole contributions, "with
    equality only when A is normal" ([LIT-931](../literature.d/LIT-931.md), eq. 22, cited to Ioannou
    1995). A non-normal system holds more variance than the normal
    system with the same spectrum.
- **The spectrum is fragile.** An operator perturbation of norm ε can
  move eigenvalues anywhere in the ε-pseudospectrum, which for a
  non-normal operator may reach far past the ε-neighbourhood of the
  spectrum ([LIT-932](../literature.d/LIT-932.md), eq. 13).
- **Sizes in examples.**
  - A 2 × 2 operator with eigenvalues −1 and −2 and eigenvectors at
    angle π/100 grows about eightfold before decaying.
  - A damped Eady model, stable in every mode, grows a hundredfold in
    energy over four days.
  - A damped channel with only decaying modes grows its two-day optimal
    112-fold ([LIT-931](../literature.d/LIT-931.md), Figs. 4, 8, 12).

What could have come out otherwise: the examples. The general statements
are theorems of linear algebra, quoted with their standard proofs or
cited.

## What this does not say

- **It does not say the growth persists.** In a stable autonomous system
  every perturbation still decays in the end, at the rate of the
  spectral abscissa. The claim is about the finite-time and forced
  behaviour, not the asymptote.
- **It does not say non-normality is a property of the system alone.** It
  is relative to the norm. "It is always possible to find a (usually
  unphysical) norm that renders the operator normal" ([LIT-931](../literature.d/LIT-931.md), §2). The
  claim has content only once a norm is fixed on independent grounds,
  such as energy.
- **It does not say what happens nonlinearly.** That transient growth
  hands disturbances to nonlinear dynamics and so causes transition to
  turbulence is a separate claim. In [LIT-932](../literature.d/LIT-932.md) it is a conjecture
  ([THEORY-304](THEORY-304.md)).
- **It does not say time-varying operators settle.** For operators that
  change in time, non-normality can produce asymptotic instability, not
  only transient growth ([THEORY-325](THEORY-325.md)).
- **It does not say directed coupling is the source of non-normality.**
  The sources in these papers are background shear. A one-way coupling
  such as the upper-triangular 2 × 2 example is non-normal, but neither
  paper states a general rule about directed structures.

## Connections

No relations are declared.

- **[CLAIM-186](../claims.d/CLAIM-186.md).** Its note "settling does not rule out bursts" cites
  these papers for exactly this claim, and states it at the right
  strength. What this account adds is the forced case: under continual
  small disturbance a non-normal system shows more standing variance than
  its spectrum predicts, not only occasional bursts. And it adds the
  caveat that the reading across needs a norm.
- **[THEORY-304](THEORY-304.md).** The shear-flow case, with scalings in Reynolds
  number.
- **[THEORY-325](THEORY-325.md).** The time-dependent case, where transient growth
  can become asymptotic instability.
