---
number: 930
status: Proposed
formerly:
- CLAIM-tmp0h57p
title: 'In a small two-layer ReLU network trained from small initial weights on a tree whose levels carry independently set strengths, the levels are acquired in the same direction as in a deep linear network, by input strength times target strength, but with the spread of acquisition times compressed to about four-tenths of its exponent, so that many strength profiles a deep linear network separates are acquired together; in NTK parametrization the target strengths stop mattering between width 256 and 1024'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-052: the small
    nonlinear arm of the phase diagram QUESTION-217 proposes.
role: thesis
warrant: empirical
defeated_if: >-
  A rerun of the design in scratch/studies/lead-052/, with more seeds or
  other step sizes at which every level is acquired, in which the
  small-initialization two-layer ReLU network acquires some cell's levels
  coarse-first where the two-layer linear network acquires them
  fine-first, or the reverse; or in which its fitted exponent of
  acquisition time on target strength is not clearly smaller in magnitude
  than the linear network's (above about −0.6 against about −0.9); or in
  which the NTK-parametrized network at width 1024 or more orders levels
  by target strength. Not defeated by larger trees, noisy items or bigger
  networks behaving otherwise, which bound its scope.
tags:
- learning-theory
- representation-learning
date: '2026-11-22'
line:
- learned-structure
bears_on:
- QUESTION-217
- QUESTION-039
grounds:
- CASE-351
summary: >-
  The nonlinear arm of [CASE-351](../cases.d/CASE-351.md). Eight items on a depth-3 tree,
  inputs and targets with a strength per level, a width-64 two-layer ReLU
  network from initial scale 0.01, three seeds per cell, 130 cells. In no
  cell, at any of five threshold settings, did it acquire the levels in
  the opposite direction from the two-layer linear network. But its
  acquisition times scaled about as (c·g)^(−0.4) against the linear
  network's (c·g)^(−1): once the strongest level is acquired the others
  follow soon after (at target strengths 1, 1, 4, times 2.4, 2.5, 2.1
  against the linear network's 5.5, 5.5, 1.5), so 18 of 81 and 34 of 49
  cells were simultaneous. Unlike the kernel learners it weighs input and
  target strengths alike. In NTK parametrization the dependence on target
  strength held at width 64, faded at 256 and was gone at 1024 and 4096;
  in standard parametrization at width 64 it held at every initial scale
  from 0.003 to 3. The compression is not explained. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-351 CLAIM-929 — new; the study and the demonstrated claim of LEAD-052, filed 2026-11-22 -->

# CLAIM-930: In a small two-layer ReLU network trained from small initial weights on a tree whose levels carry independently set strengths, the levels are acquired in the same direction as in a deep linear network, by input strength times target strength, but with the spread of acquisition times compressed to about four-tenths of its exponent, so that many strength profiles a deep linear network separates are acquired together; in NTK parametrization the target strengths stop mattering between width 256 and 1024

## The claim

[CLAIM-929](CLAIM-929.md) derives the order for two limiting learners: a kernel
reads the input strength of each level only, and a decoupled deep linear
network the product of input and target strength. This claim places a
small nonlinear network between them, from [CASE-351](../cases.d/CASE-351.md).

- **Direction.** From small initial scale, the two-layer ReLU network
  never ordered the levels against the deep linear network's order, in
  either grid, at δ = 0.5, 0.1 or 0.02 or with ties at 1.1, 1.25 or 1.5.
  Like the deep linear network, and unlike the kernel, it weighed input
  and target strength alike (fitted exponents −0.43 and −0.42).
- **Spread.** Its exponent on strength was about −0.4 (−0.36 in the first
  grid, −0.42 in the second), against −0.92 to −0.95 for the two-layer
  linear network. Where the linear network separated levels by a factor of
  2 to 4, the ReLU network often acquired them within 25% of each other:
  simultaneous in 18 of 81 and 34 of 49 cells at the main setting. How
  large the simultaneous region is depends on the tie threshold (2 cells
  at 1.1, 47 at 1.5, in the first grid), as it must when times are
  compressed rather than reordered.
- **Transition.** The order by target strength is a finite-width effect in
  NTK parametrization: present at width 64 (exponent −0.45), weak at 256
  (−0.10), absent at 1024 and 4096 (−0.01), where the network follows the
  kernel. In standard parametrization at width 64 it was present at every
  initial scale tried.

## What it bears on

For [QUESTION-217](../questions.d/QUESTION-217.md), acquisition order in this family is a joint property of
the strengths and the learner: the same tree gives every phase, and the
nonlinear network's phase map is the linear one's with its boundaries
widened into a band of simultaneous acquisition. For [QUESTION-039](../questions.d/QUESTION-039.md), the
small network's acquisition times are set mostly by the strongest level,
which pulls the weaker ones along, a coupling between levels that neither
limiting learner has.

## What it does not say

One tree of eight items, deterministic, full batch, gradient descent, one
width (64) for the small-scale arm, three seeds per cell. It does not say
why the times compress, nor that larger trees, sampled items, hidden-layer
decoders, other optimizers or deeper networks behave the same.
