---
number: 323
status: Proposed
formerly:
- THEORY-tmpwdx4q
promote_when: >-
  A held proof of the white-noise variance inequality and its equality
  case: that trace(P), with AP + PA† + I = 0, is at least
  Σ 1/(−2 Re λ_i), with equality only when A is normal. Ioannou (1995), to
  whom LIT-931 eq. 22 cites it, or a standard reference, would meet it. So
  would a record-own proof checked step by step, for instance via the Schur
  form A = U(Λ + N)U† with N strictly upper triangular. The finite-time and
  resolvent statements this clause used to share are THEORY-727,
  Active. More examples of large variance in particular systems cannot
  settle it.
title: 'Under spatially uncorrelated white noise, a stable non-normal linear system holds more variance than the sum of its pole contributions, and equality holds only when the operator is normal, so its spectrum understates the standing variance'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Split at the owner's direction, carrying out the promotion audit's
    decision (record/promotion-audit/decisions/THEORY-323.yaml, batch 007,
    ADR-047). The finite-time growth and resolvent statements, each checked
    by its textbook proof, are now THEORY-727, Active, which this
    THEORY extends. What stays is the white-noise variance clause, which
    LIT-931 eq. 22 cites to Ioannou (1995) and does not prove. The title is
    restated to that clause, and the promote_when is narrowed to it. The
    body below is unchanged; the note of 2026-10-19 says which parts moved.
tags:
- mathematics
- complex-systems
- natural-sciences
date: '2026-10-14'
source:
- LIT-931
- LIT-932
extends:
- THEORY-727
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

# THEORY-323: Under spatially uncorrelated white noise, a stable non-normal linear system holds more variance than the sum of its pole contributions, and equality holds only when the operator is normal, so its spectrum understates the standing variance

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

## Note of 2026-10-19: what moved, and what stays

The finite-time and resolvent statements in "What was actually shown" are
now [THEORY-727](THEORY-727.md), Active, with their textbook proofs written out. They
cover normal operators, growth as a singular value, the eigenvalue floor,
the numerical abscissa, the harmonic-forcing bound and pseudospectra. What
this THEORY still holds is the white-noise clause: trace(P) ≥
Σ 1/(−2 Re λ_i), with equality only for normal A. [LIT-931](../literature.d/LIT-931.md) cites it and the
record has not read the proof, so it stays Proposed.
