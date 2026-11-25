---
number: 2295
status: Active
formerly:
- THEORY-tmpmvcnr
title: 'Ott–Antonsen manifold reduces Kuramoto to ODEs'
statement: >-
  Ott and Antonsen show that for infinitely many globally coupled phase
  oscillators with first-harmonic coupling, the distributions whose phase
  Fourier coefficients are powers of one function of frequency form an
  invariant manifold, on which the order parameter obeys a finite set of
  ordinary differential equations exactly when the frequency distribution is
  rational, one complex equation per pole in the lower half-plane, while the
  distribution on the manifold stays infinite-dimensional, with a continuous
  spectrum of neutral modes
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings), under ADR-057 and ADR-065: a reported title read in full
    (NOTE-2385); invariance re-derived (CLAIM-1145's hierarchy at
    H_2 = 0) and eq. 10 checked by a 200,000-oscillator simulation started
    on the manifold, with a Gaussian control that fails
    (scratch/studies/lead-094/oa_eq10_check.py: maximum deviation 0.004,
    0.003, 0.001 at K = 1, 3, 4 against 0.05, 0.15, 0.20 for the control),
    run by the reviewer and re-run by the coordinator. Old condition: "An
    independent derivation, or a simulation of a large population started
    on the manifold, confirms what the title says: that the family of
    distributions with Fourier coefficients αⁿ is invariant under first-
    harmonic global coupling, and that with a Lorentzian frequency
    distribution the order parameter then follows eq. 10 of the paper.
    Whether the manifold attracts is not required; it is held separately
    (THEORY-2276)."
tags:
- complex-systems
- mathematics
date: '2026-11-22'
source:
- LIT-2248
corroborates:
- CLAIM-388
- CLAIM-1145
bears_on:
- QUESTION-218
- QUESTION-281
- QUESTION-252
summary: >-
  Ott and Antonsen (2008), [LIT-2248](../literature.d/LIT-2248.md), read in full in [NOTE-2385](../notes.d/NOTE-2385.md). The
  reduction is exact on a restricted class of states and needs no small
  parameter. It is a nonlinear case of [CLAIM-388](../claims.d/CLAIM-388.md)'s closure of a collective
  variable without a block, and the candidate defeater of [CLAIM-478](../claims.d/CLAIM-478.md) that
  [LEAD-094](../leads.d/LEAD-094.md) names; the verdict is filed as alternatives ([CLAIM-1058](../claims.d/CLAIM-1058.md),
  [CLAIM-1088](../claims.d/CLAIM-1088.md)). Proposed until the invariance and eq. 10 are confirmed
  independently.
---
<!-- inactive-ok-file: THEORY-2276 CLAIM-1058 CLAIM-1088 — Proposed or new; the sequel's reading and the verdict filed from this one -->
<!-- inactive-ok-file: CLAIM-478 — Proposed; the claim this reading was read against -->

# THEORY-2295: Ott–Antonsen manifold reduces Kuramoto to ODEs

## Source

Ott and Antonsen (2008), "Low Dimensional Behavior of Large Systems of
Globally Coupled Oscillators", *Chaos* 18: 037113, [LIT-2248](../literature.d/LIT-2248.md), read from the
arXiv preprint in [NOTE-2385](../notes.d/NOTE-2385.md).

## The account

Write the continuum distribution's phase Fourier coefficients as
fₙ(ω, t). The family fₙ = α(ω, t)ⁿ, with |α| < 1 and α analytic and
decaying in the lower half ω-plane, solves the continuity equation of the
Kuramoto problem exactly when α obeys one equation per frequency (eq. 6);
the family is invariant. For a Lorentzian g the frequency integral closes
on its pole, and the order parameter's modulus obeys
dρ/dt + (1 − K/2)ρ + (K/2)ρ³ = 0, solved in closed form; a rational g with
m poles in the lower half-plane gives m complex equations. The same holds
for a periodic drive, for communities of oscillators, and, as a delay
equation, for uniform delay. On the manifold the distribution keeps
infinitely many degrees of freedom whose linearization has "a continuous
spectrum of neutral modes" (p. 9): the order parameter's law is closed
without those degrees of freedom relaxing. The paper leaves open whether
the manifold attracts (note 24); the sequel answers it for the order
parameter ([THEORY-2276](THEORY-2276.md)).

## Conditions

Infinite N, all-to-all coupling, coupling through the first harmonic of
the phase difference only. [CLAIM-1145](../claims.d/CLAIM-1145.md) shows that a second harmonic
breaks the invariance except at full locking.

## Bearing

- It corroborates [CLAIM-388](../claims.d/CLAIM-388.md): a function of the whole state is exactly
  closed under uniform coupling, where no subset of units is a block, now
  in a nonlinear model.
- It bears on [QUESTION-218](../questions.d/QUESTION-218.md) (the closed variable is a function of the whole
  state, and in the community model one per community at any coupling
  between them), on [QUESTION-281](../questions.d/QUESTION-281.md) (the locking onset as an instability with
  an exact low-dimensional law) and on [QUESTION-252](../questions.d/QUESTION-252.md) (closure and fidelity
  hold on the manifold while the omitted variables neither relax nor are
  slaved).
- Its bearing on [CLAIM-478](../claims.d/CLAIM-478.md)'s defeater (a) is contested; see
  [CLAIM-1058](../claims.d/CLAIM-1058.md) and [CLAIM-1088](../claims.d/CLAIM-1088.md).
