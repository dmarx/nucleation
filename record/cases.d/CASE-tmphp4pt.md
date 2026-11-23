---
status: Proposed
title: 'The crossed intervention run on a small conventionally trained network'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out the lead that asks for
    this run. Code, tests and results are committed under
    scratch/studies/lead-105/.
standing: documented
kind: executed-study
tags:
- learning-theory
- agency
date: '2026-11-23'
line:
- learned-structure
- distributed-agency
draws_on:
- THEORY-253
bears_on:
- QUESTION-122
illustrates:
- CLAIM-tmp60fme
- CLAIM-tmp2k67n
summary: >-
  The two interventions of [CASE-113](CASE-113.md), crossed, on one small network
  trained conventionally on two tasks with a task-identity input: a
  width-32 two-layer ReLU network, trained by heavy-ball SGD or by Adam,
  twelve seeds each. The conflicting learning demand is a change of task
  B's target to one opposed to task A (cosine −0.87), trained jointly; the
  response is how much task A is lost while B is relearned. Holding the
  network fixed and changing the optimizer, at matched pace, moved the
  response in every trained network (by −39% to +147% of the baseline
  loss). Holding the optimizer fixed and disrupting a learned state also
  moved it: re-initializing the eight most task-selective hidden units and
  healing raised the loss of A by 61% under the training optimizer for
  heavy-ball-trained networks, and eight random units did not. Neither
  limb of [CLAIM-367](../claims.d/CLAIM-367.md)'s defeat condition held. The share of the response
  that varies with the optimizer, against the share that varies with the
  learned state, depended on which optimizer had trained the network.
  One small network, full batch, twelve seeds. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-367 CLAIM-tmp60fme CLAIM-tmp2k67n CLAIM-tmpmgb7l CLAIM-tmpyf8s0 — Proposed or new; the claim the run tests, and the claims filed by the lead run of 2026-11-23 -->

# CASE-tmphp4pt: The crossed intervention run on a small conventionally trained network

## What was done

[CASE-113](CASE-113.md) states two interventions and their reading: change the
optimizer with the network fixed, and disrupt a learned state with the
optimizer fixed. [CLAIM-367](../claims.d/CLAIM-367.md) is defeated if the first leaves the
network's responses to conflicting learning demands unchanged while the
second abolishes or alters them. This run does both on one conventionally
trained network, on 2026-11-23, with numpy on CPU. Code, eight tests and
all results are in scratch/studies/lead-105/ (README.md, PROGRESS.md,
results/).

**Network and training.** Input [x; e_t], x ~ N(0, I₈) and e_t the one-hot
code of task t; task A's target a·x, task B's b·x, a and b orthonormal; 512
examples per task, full batch. A two-layer ReLU network of width 32 with
standard initialization, trained 3000 steps by heavy-ball SGD (step 0.01,
momentum 0.9) or by Adam (step 3·10⁻³), to levels 0.997 and 1.000 on both
tasks. Seeds 0 to 11 for data and initialization.

**The conflicting demand (the probe).** Task B's target changes to
b₂·x, b₂ = (b − √3 a)/2, whose cosine with a is −0.87, so that relearning
B through features the tasks share undoes A. Both tasks train jointly for
600 steps. The response measures: A's **peak forgetting** (its largest fall
in level, level being 1 − MSE/E[y²]), A's level when B first reaches 0.9,
B's relearning time, the cosine of the two task gradients at the start
(which no optimizer touches) and the tasks' segregation over hidden units
at the end (0 when every unit serves both tasks equally, 1 when each
serves one).

**Pace matched.** Each probe optimizer's step size was calibrated, on four
networks with seeds outside the study's, so that the intact network
relearns B in 40 steps (median). The optimizers differ in path, not in
speed.

**Optimizer arm.** The same trained parameters probed under plain SGD,
heavy ball, Adam and sign descent (all with fresh state), and under the
training optimizer with its state carried from training.

**Learned-state arm.** The probe optimizer fixed, the network changed:
- *permuted*: hidden units permuted, a null control (same function, same
  dynamics);
- *rescaled*: each hidden unit's input weights multiplied by c_i and its
  output weight divided by c_i, c_i log-uniform in [1/2, 2], which leaves
  the function exactly unchanged;
- *ablate-selective*: the 8 hidden units most selective for one task
  re-initialized, then 1000 healing steps on the original tasks under the
  training optimizer;
- *ablate-random*: the same with 8 random units;
- *continued*: 1000 more steps of training without disruption, the control
  for healing.

Every state was probed under every optimizer, so the grid is crossed.

## Results

Peak forgetting of A, paired differences from the baseline (intact
network, probed by its own training optimizer), mean and 95% interval over
twelve seeds; * where the interval excludes zero.

| | trained by heavy ball | trained by Adam |
|---|---|---|
| baseline | 0.046 (sd 0.013) | 0.030 (sd 0.023) |
| optimizer → SGD | −0.018 [−0.021, −0.014]* | +0.013 [+0.006, +0.021]* |
| optimizer → heavy ball | (baseline) | +0.045 [+0.037, +0.052]* |
| optimizer → Adam | −0.006 [−0.021, +0.009] | (baseline) |
| optimizer → sign descent | −0.010 [−0.019, −0.001]* | 0.000 [−0.004, +0.004] |
| training optimizer, state carried | 0.000 | +0.038 [+0.024, +0.053]* |
| state → permuted | 0.000 | 0.000 |
| state → rescaled | +0.009 [−0.005, +0.023] | −0.002 [−0.005, +0.001] |
| state → ablate-selective | +0.028 [+0.015, +0.042]* | +0.016 [−0.002, +0.034] |
| state → ablate-random | +0.002 [−0.004, +0.008] | +0.001 [−0.009, +0.011] |
| state → continued | −0.003 [−0.004, −0.001]* | +0.001 [+0.001, +0.002]* |

Ablate-selective under the other probe optimizers, for Adam-trained
networks: +0.031* under SGD, +0.039* under heavy ball, +0.014* under sign
descent; ablate-random +0.015* and +0.024* under SGD and heavy ball. For
heavy-ball-trained networks ablate-selective was +0.023* under SGD and
+0.021 and +0.015 (intervals reaching zero) under Adam and sign descent.

Share of the variation of peak forgetting across the (state × optimizer)
cells, seed-averaged, five states by four fresh optimizers:
heavy-ball-trained, state 0.58, optimizer 0.39, interaction 0.03;
Adam-trained, state 0.15, optimizer 0.81, interaction 0.04. A's level when
B reached 0.9 gives the same picture (0.78 against 0.18; 0.06 against
0.92).

Other measures:
- Segregation at the end of the probe moved with the optimizer
  (heavy-ball-trained: +0.067* under Adam, +0.035* under sign descent;
  Adam-trained: −0.025* to −0.036* under the other three). It moved with
  the state only under ablate-random for Adam-trained networks (−0.060*).
- The task-gradient cosine at the start is a property of the network and
  the data, untouched by the optimizer by construction. Ablate-selective
  lowered it in heavy-ball-trained networks (−0.10 [−0.20, −0.002]).
- Rescaling left forgetting unchanged within the intervals but changed the
  relearning time (−16.5 steps [−27, −6] heavy-ball-trained, −2.6 [−4.7,
  −0.4] Adam-trained).
- Momentum carried from heavy-ball training is negligible at convergence,
  so carrying it changed nothing. Adam's carried second moments are tiny at
  convergence and inflate the first steps, which more than doubled the
  forgetting (+0.038) and cut B's relearning time from 41 to 10 steps.

## What it can show

- In this network, the first limb of [CLAIM-367](../claims.d/CLAIM-367.md)'s defeat condition
  fails: changing the optimizer with the network fixed changed the response
  to the conflicting demand in both trained populations, at matched pace,
  in the optimizer's state alone as well as in its rule
  ([CLAIM-tmp60fme](../claims.d/CLAIM-tmp60fme.md)).
- The second limb holds in part: disrupting the units that carry the
  learned task separation, and healing, altered the response under the
  training optimizer for one population, more than disrupting as many
  random units.
- How much of the response sits with each is not fixed: it depends on
  which optimizer trained the network, and a disruption's effect depends on
  the optimizer that meets it. Two readings of what that does to
  [CLAIM-367](../claims.d/CLAIM-367.md) are filed as alternatives
  ([CLAIM-tmpmgb7l](../claims.d/CLAIM-tmpmgb7l.md), [CLAIM-tmpyf8s0](../claims.d/CLAIM-tmpyf8s0.md)).
- A function-preserving change of the network's parameters is the same
  thing as a change of the optimizer's per-coordinate step sizes, so the
  two arms are not separated by anything the network computes
  ([CLAIM-tmp2k67n](../claims.d/CLAIM-tmp2k67n.md)).

## What it cannot show

- Anything about a larger network, another architecture, stochastic
  batches, or a conflict that persists for longer. Here the conflict
  resolves in tens of steps and the losses are a few percent of A's level.
- That the task separation is a *regulatory* representation in
  [CASE-113](CASE-113.md)'s sense, a variable that the network uses to govern its
  updates. It is learned structure that shapes how conflict propagates;
  System B or C of [CASE-113](CASE-113.md) was not built.
- Anything about frustration or affect. The forgetting measured is
  optimization strain in A31's sense, nothing more.
- Whether the ablation-and-heal result is about the units' selectivity or
  about re-initializing high-activity units; the random-ablation control
  rules out only disruption of equal size.
