---
status: Proposed
title: 'Azizpour, Priesemann, Zierenberg and Levina show, analytically in the limits and by simulation between them, that in a random network of stochastic spiking neurons with a branching (absorbing-to-active) transition at λ = 1, a leaky readout with finite integration time T makes both the number of ε-discriminable input rates and a fluctuation-aware dynamic range peak at a subcritical λ* < 1, at different λ* for the two measures, with λ* approaching the critical point as T grows, because critically slowed population fluctuations not averaged out within T blur the readout'
promote_when: >-
  An independent study, a replication with the authors' released code or
  another model with an absorbing-to-active transition and a finite-time
  readout, finds discriminability of input rates maximal at a subcritical
  coupling that moves toward the critical point as the readout's
  integration time grows.
version: 1
tags:
- neuroscience
- complex-systems
- information-theory
date: '2026-11-22'
source:
- LIT-2980
bears_on:
- QUESTION-507
- QUESTION-091
summary: >-
  Azizpour and colleagues, [LIT-2980](../literature.d/LIT-2980.md), read in [NOTE-tmporpz2](../notes.d/NOTE-tmporpz2.md). "Criticality
  maximizes dynamic range" (Kinouchi and Copelli, [LIT-tmpcc25u](../literature.d/LIT-tmpcc25u.md)) becomes
  "only for infinite integration time": every finite readout window has a
  subcritical optimum, different for the two measures. One transition
  (branching), one task family (discriminating stationary input rates);
  the paper itself says the side of the optimum depends on the task and
  the transition. Grounds [CLAIM-809](../claims.d/CLAIM-809.md)'s window- and task-dependence
  ([ARG-tmp5sgtm](../arguments.d/ARG-tmp5sgtm.md)).
---
<!-- inactive-ok-file: LIT-tmpcc25u LIT-tmpfn6b8 ARG-tmp5sgtm CLAIM-809 CLAIM-814 — Proposed, Deferred or new; the reading, the works it names and the claims it bears on -->

# THEORY-tmpye6xs: Azizpour, Priesemann, Zierenberg and Levina show, analytically in the limits and by simulation between them, that in a random network of stochastic spiking neurons with a branching (absorbing-to-active) transition at λ = 1, a leaky readout with finite integration time T makes both the number of ε-discriminable input rates and a fluctuation-aware dynamic range peak at a subcritical λ* < 1, at different λ* for the two measures, with λ* approaching the critical point as T grows, because critically slowed population fluctuations not averaged out within T blur the readout

## Source

Azizpour, Priesemann, Zierenberg and Levina, "Finite integration time can
shift optimal sensitivity away from criticality", [LIT-2980](../literature.d/LIT-2980.md), read from the
arXiv v1 PDF of 2602.09491 in [NOTE-tmporpz2](../notes.d/NOTE-tmporpz2.md).

## What was actually shown

- N = 10⁴ binary stochastic neurons, w_ij = λ/K_i, Poisson input at rate
  h on a fraction μ = 0.2, a leaky-integrator readout of timescale T on a
  fraction ν = 0.2 plus Gaussian noise σ = 10⁻².
- Limits solved: T → ∞ (mean field) and T → 0 (Fokker–Planck after a
  Kramers–Moyal expansion); finite T by simulation with Beta fits
  interpolated by a small neural network.
- "n_d exhibits a maximum at a T-dependent subcritical λ < 1 ... every
  finite integration time will have an optimal 0 < λ < 1, while for
  infinite integration time, n_d is bound by the Gaussian noise of the
  readout" (p. 3); the dynamic range "develops a T-dependent maximum,
  which is, however, different from the maximum of n_d"; "With increasing
  timescale T, the maximum λ* moves closer to the critical point" (Fig. 2).
- Mechanism (p. 4): fluctuations near the transition "can smear out the
  signal if they are aligned with the readout".

What could have failed: at finite T the measures could have peaked at
λ = 1, or the optimum could have moved away from 1 as T grew; neither did.

## What this does not say

- Not that subcritical is best for every transition or task: "On which
  side of the transition this optimum lies will, however, depend on both
  the task and the type of phase transition" (p. 4), and at the transition
  to chaos the paper cites the supercritical side as beneficial
  (Toyoizumi and Abbott, [LIT-tmpfn6b8](../literature.d/LIT-tmpfn6b8.md)).
- Nothing on memory, nonlinear computation or temporal patterns: the
  task is discriminating stationary input rates.
- Not Fisher information: the measure is the ideal-observer overlap
  error between output distributions.
- No uncertainty on λ* is given; the biological mapping (τ ≈ 10–100 ms or
  50–500 ms) depends on the assumed timestep.

## Connections

Grounds [CLAIM-809](../claims.d/CLAIM-809.md)'s window- and task-dependence ([ARG-tmp5sgtm](../arguments.d/ARG-tmp5sgtm.md)). Contrast
with [CLAIM-814](../claims.d/CLAIM-814.md): there readout noise pushes the optimum toward the
transition; here unaveraged internal fluctuations push it away. Bears on
[QUESTION-507](../questions.d/QUESTION-507.md) (point 2, which measure) and [QUESTION-091](../questions.d/QUESTION-091.md) (distance from
criticality set by the readout).
