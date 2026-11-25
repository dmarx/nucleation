---
number: 319
status: Proposed
formerly:
- CASE-tmpd2k95
title: 'Sign descent derived and run against gradient descent on the same unequal-frequency skills'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-045. Code, tests
    and results are committed under scratch/studies/lead-045/.
standing: documented
kind: executed-study
tags:
- learning-theory
- representation-learning
date: '2026-11-22'
line:
- learned-structure
reported_in:
- THEORY-253
draws_on:
- THEORY-229
- THEORY-187
bears_on:
- QUESTION-193
- QUESTION-039
illustrates:
- CLAIM-883
summary: >-
  The study [LEAD-045](../leads.d/LEAD-045.md) asks for, in two parts. First, the Geometry model of
  [THEORY-253](../theory.d/THEORY-253.md) (loss Σ p_i (1 − θ·t_i)², orthonormal random t_i, d = 1000)
  under gradient descent, sign descent and Adam, set against an ODE derived
  for sign descent in the mean-field limit: the derived onset ratios match
  the simulation to within 2% at every frequency tried, two to five
  skills, better than the paper's fitted Resource form. Second, one
  two-layer ReLU network trained on four independent skills of frequency
  ∝ i^(−2), under all three optimizers, from order-one and from small
  initial scale, three seeds each. At order-one scale, changing only the
  optimizer from gradient descent to sign descent or Adam made the weaker
  skills rise late instead of fastest at the start (level at half their
  learning time 0.71 against 0.47 and 0.43) and cut skill 4's learning
  time relative to skill 1's from about 23 to about 5.5; the clean Domino
  form did not appear, and the skills interfered. From small scale,
  gradient descent alone delayed them most. One small network, full batch,
  three seeds; the hierarchical-task design the lead also names was not
  run. The wording is the assistant's (Claude, in this session); adopting
  it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-883 CLAIM-882 THEORY-783 — Proposed or new; the claims this study grounds, and the wider reading it bears on -->

# CASE-319: Sign descent derived and run against gradient descent on the same unequal-frequency skills

## What was done

[LEAD-045](../leads.d/LEAD-045.md) asks to train one network on independent skills of unequal
frequency under gradient descent and under sign descent (or Adam), and to
derive, for sign descent, the delayed onset of each weaker skill and the
ratio of onset times. Both were done on 2026-11-22, with numpy on CPU; the
code, its twelve tests, the full derivation and every number are in
scratch/studies/lead-045/ (README.md; results/). A skill counts as learned
at level 0.9.

**The derivation** ([CLAIM-883](../claims.d/CLAIM-883.md)). In the Geometry model, with the
task vectors generic with respect to the coordinates and d large, a sign
step moves skill j by η Σ_k t_jk sign(Σ_i p_i u_i t_ik), and the Gaussian
identity E[X sign Z] = √(2/π) Cov(X, Z)/σ_Z gives
du_j/dt = −c p_j u_j / ‖p∘u‖₂ with c = η√(2d/π). That is gradient flow with
its clock divided by the gradient norm. Its consequences, each checked
against the simulation:

| p₁ (two skills) | 0.5 | 0.7 | 0.8 | 0.9 | 0.95 | 0.99 |
|---|---|---|---|---|---|---|
| t₂/t₁, sign descent simulated | 1.02 | 1.29 | 1.49 | 1.76 | 1.91 | 2.05 |
| t₂/t₁, derived | 1.00 | 1.26 | 1.47 | 1.75 | 1.91 | 2.06 |
| t₂/t₁, paper's Resource form, N₀ = 0 | 1.00 | 1.24 | 1.42 | 1.69 | 1.87 | 2.06 |
| t₂/t₁, Adam at default β | 1.01 | 1.30 | 1.60 | 2.38 | 3.44 | 6.80 |
| t₂/t₁, gradient descent | 1.00 | 2.38 | 4.13 | 9.38 | 19.9 | 104 |
| skill 2's level when skill 1 is learned, sign / GD | 0.88 / 0.90 | 0.61 / 0.62 | 0.43 / 0.43 | 0.23 / 0.22 | 0.12 / 0.11 | 0.03 / 0.02 |

With five skills at p_i ∝ i^(−α), α = 1, 2, 3, the derived t_n/t_1 lie
within 0.08 of the simulated ones (README). On the paper's rotated
quadratic, sign descent with the Hadamard rotation holds x₂ to x₄ exactly
still until x₁ = 0.111 at step 444, as derived, and the half-times 251, 730,
1172 and 1731 reproduce the record's earlier run (note of 2026-10-19 on
[THEORY-253](../theory.d/THEORY-253.md)); with R = I all four fall together. Adam with β₁ = β₂ = 0
matches sign descent to four figures.

**The network** ([CLAIM-882](../claims.d/CLAIM-882.md)). Input: the one-hot code of skill i
and x ~ N(0, I₈); skill i's target a_i·x with the a_i orthonormal;
p = 0.70, 0.18, 0.08, 0.04; 4096 examples, full batch; a two-layer ReLU
network of width 64 whose output is zero at the start (antisymmetric
initialization). Gradient descent at rate 0.2; sign descent and Adam at
10⁻³; order-one scale (W ~ N(0, 1/fan-in), v ~ N(0, 1/width)) and that
scale times 0.01; seeds 0, 1, 2. "Delay" is a skill's level at half its own
learning time, over 0.9: 0.76 for an exponential curve, less for one held
back.

| optimizer, initial scale | delay, skills 2–4, mean (range) | t_learned/t_1, skills 2, 3, 4 |
|---|---|---|
| gradient descent, order one | 0.71 (0.59–0.80) | 6.1, 11.8, 23.4 |
| sign descent, order one | 0.47 (0.27–0.70) | 3.0, 4.1, 5.4 |
| Adam, order one | 0.43 (0.23–0.64) | 3.0, 4.2, 5.5 |
| gradient descent, 0.01 | 0.11 (0.01–0.26) | 5.2, 9.9, 15.8 |
| sign descent, 0.01 | 0.25 (0.02–0.61) | 2.4, 3.3, 6.0 |
| Adam, 0.01 | 0.28 (−0.02–0.46) | 3.3, 4.5, 6.3 |

The Geometry model's derived ratios for the same frequencies are 1.67,
2.06 and 2.24 under sign descent and 4, 9 and 16 under gradient descent. A
sign-descent run at a third of the step gave 3.1, 3.7 and 4.5. Under every
optimizer the weaker skills' levels fell to −0.2 or −0.3 while skill 1 was
being learned.

## What it can show

It is documented: the runs happened and are rerunnable in about five
minutes. In the Geometry model it shows that the derived ODE describes sign
descent quantitatively, so the Domino effect of [THEORY-253](../theory.d/THEORY-253.md) has a
derivation, and what kind of thing it is: a change of clock along gradient
descent's own path. In the network it shows, for one architecture and
three seeds, that swapping only the optimizer at order-one scale moves the
weaker skills' onsets later and compresses their spread, and that from
small scale gradient descent alone delays them, the mechanism of
[THEORY-229](../theory.d/THEORY-229.md) and [THEORY-187](../theory.d/THEORY-187.md). It bears on the wider reading [THEORY-783](../theory.d/THEORY-783.md)
as one small instance.

It cannot show that larger or stochastically trained networks behave so,
and the network's skills are independent in the data but not in the
dynamics: they share hidden units and interfere, which the Geometry model
excludes. The hierarchical task from small and order-one scale, which the
lead also names, was not run.
