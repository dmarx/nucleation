---
number: 391
status: Proposed
formerly:
- CASE-tmp3axlj
title: 'Thermodynamics of prediction reproduced'
statement: >-
  Still, Sivak, Bell and Crooks's thermodynamics of prediction reproduced on
  small driven Markov systems, then with feedback from system to drive, and
  in a percept–action loop where the predictive and interventional
  partitions differ
version: 1
standing: documented
kind: executed-study
tags:
- thermodynamics
- information-theory
- causality
- learning-theory
date: '2026-11-23'
line:
- learned-structure
- formal-apparatus
draws_on:
- THEORY-026
- THEORY-1125
bears_on:
- QUESTION-494
summary: >-
  [LEAD-005](../leads.d/LEAD-005.md)'s first milestone for [QUESTION-494](../questions.d/QUESTION-494.md): reproduce a known
  no-feedback result, then add feedback. The result is Still, Sivak, Bell
  and Crooks (2012), already read ([LIT-327](../literature.d/LIT-327.md), [NOTE-295](../notes.d/NOTE-295.md)) and held as
  [THEORY-026](../theory.d/THEORY-026.md). In numpy (scratch/studies/lead-005/, 15 tests), 300 random
  4-state systems driven by a 3-symbol Markov signal through Metropolis
  kernels satisfy the per-switch identity (Eq. 14), the summed identity
  (Eq. 17) and the heat identity (Eq. 19) to 3e-15, and the bounds (Eqs.
  16, 18, 21) in every instance; no step's nostalgia is negative; Monte
  Carlo trajectories agree with the exact averages. With the drive made to
  depend on the system's state (500 systems), the identities and the summed
  bound still hold, but a step's nostalgia is negative in 405, the summed
  nostalgia in 323, and the dissipation and the excess work in 6. In an
  8-percept loop where the predictive partition is a sticky nuisance and
  the interventional partition is the context the action must match, the
  memory that keeps only the context is the cheapest that does the task by
  every cost measured; the policy that uses it changes its nostalgia from
  ln 2 to 0 and leaves its heat per step unchanged. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1123 CLAIM-1189 CLAIM-1124 CLAIM-1116 — filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CLAIM-1071 — Proposed; cited for what the run bears on -->

# CASE-391: Thermodynamics of prediction reproduced

## What was done

[LEAD-005](../leads.d/LEAD-005.md) asks for a published no-feedback result on the cost of
predictive memory to be reproduced in a small finite-state model, then for
feedback to be added and memories compared that keep the predictive
partition, the interventional partition, or neither. The result chosen is
Still, Sivak, Bell and Crooks (2012), "The thermodynamics of prediction"
([LIT-327](../literature.d/LIT-327.md), read in full in [NOTE-295](../notes.d/NOTE-295.md), its account [THEORY-026](../theory.d/THEORY-026.md)). It is the result
[QUESTION-494](../questions.d/QUESTION-494.md) names, and the record already holds its reading, so no
second reading was filed. Its text was re-checked from arXiv v3 for the
indexing and for the definition of dissipation.

Code, tests and results are in scratch/studies/lead-005/ (`still2012.py`,
`feedback_toy.py`, `run_study.py`, `test_lead005.py`,
`results/summary.md`). The whole run takes about 30 seconds on one core;
15 tests pass. Units are k_BT and nats.

**The model.** The paper's protocol: a system with state s and energies
E(s, x) starts in equilibrium with the signal x_0. At each step the signal
switches x_t → x_{t+1} with s held (work E(s_t, x_{t+1}) − E(s_t, x_t)),
then s relaxes under a fixed kernel at x_{t+1} (heat). Everything is
computed exactly from the joint law of (s, x), and by Monte Carlo over
200,000 trajectories as a check on the bookkeeping.

**Two readings of dissipation.** The paper's Eqs. 9–10 define dissipation
per protocol, with the distribution of s conditioned on the whole drive
path, while Eq. 13 averages free energies with p(s | x) conditioned on the
current signal only. Both were computed. The excess work is the same under
both, as it must be; the per-protocol dissipation is never larger.

## Part 1: without feedback, the paper's setting

300 random systems: 4 states, a 3-symbol Markov drive with Dirichlet(0.5)
rows, energies uniform in [0, 3], one Metropolis sweep per relaxation (so
far from equilibrium), six steps.

| check | result |
|---|---|
| Eq. 14, per switch: β⟨W_diss⟩ = I[s_t;x_t] − I[s_t;x_{t+1}] | holds, max error 1.1e-15 |
| Eq. 17, the sum, and Eq. 19, heat = I_e + dissipation | hold, max error 2.7e-15 |
| first law | holds, max error 2.2e-15 |
| Eq. 16, relaxation lowers the nonequilibrium free energy | 300 of 300 |
| Eq. 18, summed nostalgia ≤ dissipation ≤ excess work | 300 of 300, smallest slack 0.0095 |
| Eq. 21, heat out ≥ I_e + summed nostalgia | 300 of 300 |
| per-step nostalgia ≥ 0 | 300 of 300 |
| Eq. 18 with the per-protocol dissipation | 300 of 300, smallest slack 0.0095 |
| Monte Carlo ⟨W⟩ and ⟨Q⟩ within 4 s.e. of exact | 20 of 20 checked |

This reproduces the result as [THEORY-026](../theory.d/THEORY-026.md) states it, with both of its
conditions met (a Markov drive, kernels that keep each equilibrium
stationary). It extends that entry's one-off check of 2026-10-19 to 300
instances, with code. A test also confirms the 0.3835-nat example of
[CLAIM-1071](../claims.d/CLAIM-1071.md): a memory that copies a two-state Markov drive with
rows (0.9, 0.1) and (0.2, 0.8) pays H(X_t | X_{t+1}) at every switch.

## Part 2: with feedback

The drive's next value now depends on the system's state:
x_{t+1} ~ D(· | x_t, s_t), one Dirichlet(0.5) row per pair. Everything
else is unchanged. 500 systems.

- The identities (Eqs. 14, 17, 19, first law) still hold, to 2e-15. They
  are algebra and do not use the no-feedback assumption.
- Relaxation still lowers the nonequilibrium free energy (500 of 500), so
  Eq. 18's lower bound still holds (500 of 500).
- But in 405 systems some step's nostalgia is negative, in 323 the summed
  nostalgia is negative, and in 6 the dissipation and the excess work are
  negative (smallest excess work −0.29 k_BT): net work is extracted, paid
  for by the controller's use of the system's state, which this accounting
  does not price. See [CLAIM-1123](../claims.d/CLAIM-1123.md).

## Part 3: a percept–action loop where the partitions differ

The percept is x = (u, v, y). u is a fresh fair coin each step, the context
the action must match. v is sticky (kept with probability 1 − ε), so it
predicts the next percept but does not affect what any action does. y is
the outcome of the last action: y' = [a = u], flipped with probability δ.
The action is a function of the memory. Memory is a physical system whose
energy is 0 where s = φ(x) and a gap Δ elsewhere, re-equilibrated after each
switch (a kernel that keeps each equilibrium stationary). φ is the
partition the memory keeps.

**The partitions, computed.** Grouping percepts by p(x_{t+1} | x_t) gives
the predictive partition {v} under random actions or under the agent's own
successful loop, and {u, v} under a fixed action. Grouping them by their
response to every intervention gives {u} for the outcome y (the
causal-bottleneck reading of [THEORY-1125](../theory.d/THEORY-1125.md)) and {u, v} for the whole next
percept.

**The memories**, at ε = 0.1, δ = 0.05, Δ = 6, per step at stationarity:

| memory | success | I_mem | I_pred | nostalgia | heat per step | H[S_t \| S_{t+1}] |
|---|---|---|---|---|---|---|
| none | 0.500 | 0 | 0 | 0 | 0 | 0 |
| predictive {v} | 0.500 | 0.676 | 0.364 | 0.312 | 0.597 | 0.334 |
| interventional {u}, a = u | 0.948 | 0.676 | 0.000 | 0.676 | 2.985 | 0.693 |
| interventional {u}, a = 0 | 0.500 | 0.676 | 0.488 | 0.188 | 2.985 | 0.693 |
| u and v | 0.946 | 1.335 | 0.360 | 0.975 | 3.268 | 1.035 |
| full {u, v, y} | 0.941 | 1.514 | 0.355 | 1.158 | 3.508 | 1.293 |

Three settings more (ε, δ, Δ = 0.02, 0, 10; 0.3, 0.1, 4; 0.1, 0.05, 12)
give the same ordering. Of the memories that do the task, the one that
keeps only u is the cheapest by the Still nostalgia, by the heat per step
of this implementation, and by the entropy lost when the memory is
overwritten. The predictive memory does nothing for the task. The same
memory of u has nostalgia ln 2 when used to match and 0 when unused (in the
noiseless limit, a tested case), with the same heat per step: the policy
moves dissipation between the work step and the relaxation and does not
change the total. See [CLAIM-1189](../claims.d/CLAIM-1189.md), and, for the two readings of what
the cheapest memory keeps, [CLAIM-1124](../claims.d/CLAIM-1124.md) and its alternative
[CLAIM-1116](../claims.d/CLAIM-1116.md).

## What it can show

Being a documented run, it shows that the stated relations hold, or fail,
in the models built, exactly up to rounding. The identities and the
no-feedback bounds are theorems; the run checks the bookkeeping that the
later parts rely on. The feedback failures are exhibited instances, so
their existence is shown. The toy's ranking holds in four parameter
settings, computed exactly.

## What it cannot show

- **Anything about a learner.** Every kernel and every policy is fixed. The
  loop has no adaptation, so revising a memory, one of [QUESTION-494](../questions.d/QUESTION-494.md)'s
  four costs, is not measured.
- **A general answer to [QUESTION-494](../questions.d/QUESTION-494.md).** The toy is built so that the
  partitions differ cleanly, and its task is defined by intervention, so
  that the interventional memory serves it follows from the construction.
  What the run adds is that the thermodynamic costs agree with it, and that
  the predictive partition, which the no-feedback result favours, does
  nothing for the task.
- **The full cost of feedback.** The controller that reads the memory to
  choose the action, and so steers the drive, is not priced. Negative
  dissipation in Part 2 is the familiar sign of that omission, not a free
  lunch.
- **The heat of a better implementation.** The heat per step is that of a
  sudden switch with full re-equilibration and a gap of Δ; a slower
  protocol would dissipate less. The ordering held by all three measures,
  but only the nostalgia and the overwrite entropy are
  implementation-free.
- **The conditions [QUESTION-191](../questions.d/QUESTION-191.md) asks about.** Every no-feedback system
  here meets both of [THEORY-026](../theory.d/THEORY-026.md)'s conditions, so the run does not test
  whether the bound fails without them. The path enumerator in the code
  would take a non-Markov drive; that was not run.
