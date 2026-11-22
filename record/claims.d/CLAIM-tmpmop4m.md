---
status: Proposed
title: 'In a small two-layer ReLU network trained full-batch on four independent skills of unequal frequency, changing only the optimizer from gradient descent to sign descent or Adam, at order-one initial scale, moves the weaker skills from rising fastest at the start to rising late and compresses the weakest skill''s learning time relative to the strongest''s about fourfold, without the clean frequency-ordered sequence of the Geometry model; from small initial scale gradient descent alone delays them most'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-045: the
    trained-network test QUESTION-193's second limb asks for, in one small
    setting.
role: thesis
warrant: empirical
defeated_if: >-
  A rerun of the same design (scratch/studies/lead-045/), with more seeds
  or at other step sizes within the range at which every optimizer learns
  all four skills, in which the weaker skills' level at half their own
  learning time, or their learning time relative to skill 1's, does not
  differ between gradient descent and sign descent at order-one scale; or
  in which gradient descent from scale 0.01 does not delay them more than
  from order-one scale. Not defeated by a larger or different network that
  behaves otherwise, which bounds the claim's scope without contradicting
  it.
tags:
- learning-theory
- representation-learning
date: '2026-11-22'
line:
- learned-structure
bears_on:
- QUESTION-193
- QUESTION-039
grounds:
- CASE-tmpd2k95
summary: >-
  The second limb of QUESTION-193, run once in a small setting
  (CASE-tmpd2k95): one-hot skill code plus x ~ N(0, I₈), skill i's target
  a_i·x, frequencies 0.70, 0.18, 0.08, 0.04, a width-64 two-layer ReLU
  network with zero initial output, three seeds per arm. At order-one
  scale, the weaker skills' level at half their own learning time, over
  0.9, was 0.71 under gradient descent (0.76 is an exponential curve) and
  0.47 under sign descent, 0.43 under Adam; skill 4's learning time
  relative to skill 1's fell from about 23 to about 5.5. That is the
  direction the Geometry model predicts (CLAIM-tmpyepkb), not its form:
  the derived ratio is 2.24, skills 2 to 4 were not delayed in frequency
  order, and the skills interfered through shared hidden units. From scale
  0.01, gradient descent gave the strongest delay of all (0.11), the
  small-initialization mechanism, and sign descent weakened it. One
  architecture, full batch, three seeds. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpd2k95 CLAIM-tmpyepkb THEORY-783 — new or Proposed; the study, the derivation beside it, and the wider reading it bears on -->

# CLAIM-tmpmop4m: In a small two-layer ReLU network trained full-batch on four independent skills of unequal frequency, changing only the optimizer from gradient descent to sign descent or Adam, at order-one initial scale, moves the weaker skills from rising fastest at the start to rising late and compresses the weakest skill's learning time relative to the strongest's about fourfold, without the clean frequency-ordered sequence of the Geometry model; from small initial scale gradient descent alone delays them most

## The claim

In the network of CASE-tmpd2k95, with only the optimizer changed:

| | delay, skills 2–4 (level at half own learning time / 0.9) | t_learned/t_1, skill 4 |
|---|---|---|
| gradient descent, order one | 0.71 (0.59–0.80) | 23.4 (8.3–38) |
| sign descent, order one | 0.47 (0.27–0.70) | 5.4 (4.4–6.7) |
| Adam, order one | 0.43 (0.23–0.64) | 5.5 (4.5–7.0) |
| gradient descent, scale 0.01 | 0.11 (0.01–0.26) | 15.8 (14.5–17.2) |
| sign descent, scale 0.01 | 0.25 (0.02–0.61) | 6.0 (4.9–7.7) |

A value of 0.76 is an exponential learning curve, fastest at the start;
lower is a curve held back that rises late. Under sign descent at order-one
scale skill 1 reached half its level by step 19 to 28, and skills 2 to 4
reached theirs close together, between steps 112 and 178.

## What it shows

- **The optimizer arm.** At order-one scale, where gradient descent shows
  no plateau, swapping in sign descent or Adam delays the weaker skills and
  bunches their learning after the strongest. In the sense of
  QUESTION-193's second limb, onsets that were simultaneous became
  later, and the spread of completion times was compressed the way the
  derivation (CLAIM-tmpyepkb) says it is.
- **The two mechanisms separated.** From small scale, gradient descent
  delays the weaker skills more than any other arm, and switching it to
  sign descent reduces the delay. So the delay from small initialization
  (THEORY-229, THEORY-187) and the delay from the optimizer
  (THEORY-253) responded to different interventions, as QUESTION-039's
  proposed test requires.

## What it does not show

- **Not the Domino form.** The compression stopped at about twice the
  derived Geometry ratios (3.0, 4.1, 5.4 against 1.67, 2.06, 2.24), skill 2
  was the most delayed rather than skill 4, and no skill waited for the one
  before it to finish.
- **Not independent skills in the dynamics.** Under every optimizer the
  weaker skills' levels fell to −0.2 or −0.3 while skill 1 was being
  learned. The skills are independent in the data and share the network's
  hidden units, which the Geometry model excludes.
- **Not general.** One architecture of width 64, full batch, three seeds,
  one step size per optimizer (with one check at a third of the step for
  sign descent, which gave 4.5 for skill 4). Not a stochastic batch, a
  larger network or a hierarchical task.
- **Not about real training.** It bears on the wider reading THEORY-783,
  that sign-like optimizers are one source of sequential onset in trained
  networks, as one small instance, without testing it on a network anyone
  trains for use.
