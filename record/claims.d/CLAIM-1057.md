---
number: 1057
status: Active
formerly:
- CLAIM-tmp9zqvq
title: 'In the toy model of superposition, Chen et al.''s missing transition 5 → 6 is not reached by plain SGD at any of the sample sizes, batch sizes, learning rates, initialisations and training lengths tried, on both sides of n ≈ 600; from the 5-gon it is closed outright, and from the live 5⁺-gon it was not reached, so for this model "inaccessible" describes SGD better than "not reached in 4,500 epochs at one setting"'
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Proposed to Active at the status review's ruling (the owner delegated
    these rulings): the title claims no more than the sweep measured, with
    its hedges kept; its grounds CASE-402 and THEORY-1275 are Active.
role: thesis
warrant: empirical
defeated_if: >-
  Plain SGD in this model (squared error, no weight decay or injected
  noise) reaching the 6-gon, all six features on, from a start that is not
  already near it, at some ordinary setting: a rate at which training does
  not diverge, any batch size, n on either side of 600, within ten times
  the paper's 4,500 epochs. A run that reaches it only through a
  positive-bias column would defeat the second half and leave CLAIM-1098
  standing.
tags:
- learning-theory
- loss-landscapes
date: '2026-11-22'
line:
- learned-structure
bears_on:
- QUESTION-363
grounds:
- CASE-402
- THEORY-1275
complements:
- CLAIM-1098
summary: >-
  The SGD half of [LEAD-175](../leads.d/LEAD-175.md), run in [CASE-402](../cases.d/CASE-402.md). It answers the part of
  [QUESTION-363](../questions.d/QUESTION-363.md) that asked whether "inaccessible" and "not reached in 4,500
  epochs at one setting" could be told apart for Chen et al.'s 5 → 6
  ([THEORY-1275](../theory.d/THEORY-1275.md)). The sweep has 1,008 runs not started at the 6-gon: n
  from 300 to 2,000, batch 1 to 100, rates 0.001 to 0.2, four
  initialisations, up to 45,000 epochs. None reached the 6-gon. Higher
  noise removed features instead of adding them. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---

# CLAIM-1057: In the toy model of superposition, Chen et al.'s missing transition 5 → 6 is not reached by plain SGD at any of the sample sizes, batch sizes, learning rates, initialisations and training lengths tried, on both sides of n ≈ 600; from the 5-gon it is closed outright, and from the live 5⁺-gon it was not reached, so for this model "inaccessible" describes SGD better than "not reached in 4,500 epochs at one setting"

## The claim

[THEORY-1275](../theory.d/THEORY-1275.md) left the missing 5 → 6 between two readings: the 6-gon is
inaccessible to SGD, or it was not reached in 4,500 epochs at the paper's
one setting (batch 20, rate 0.005). The sweep in [CASE-402](../cases.d/CASE-402.md) varied
every quantity that reading named:

- n = 300 and 500, below 600, and 700, 1,000 and 2,000, above it;
- batch 1, 5, 20 and 100;
- rates 0.001 to 0.2;
- the paper's perturbed 4-gon, the 5-gon, the 5⁺-gon and prior draws;
- 4,500 and 45,000 epochs.

None of 1,008 runs reached the 6-gon, while 288 of 288 started there
stayed. Noise pushes the other way. At batch 1 the 5⁺-gon starts lost
their live column, ending at the 5-gon or, at rate 0.2, at a 4-gon.

The two routes to the 6-gon differ:

- **Through the 5-gon** the move is closed, by [CLAIM-1098](CLAIM-1098.md): the
  dropped feature gets no gradient from any sample.
- **Through the 5⁺-gon**, whose sixth column is alive with a positive
  bias, the move is open in principle. In 56 runs at batch 20 and 100,
  for up to 45,000 epochs, it was not taken.

So, for this model and this trainer, the gap between the posterior,
dominated by the 6-gon at the training sample size, and SGD's endpoint
comes from accessibility, not from time or temperature within the ranges
tried. One of [QUESTION-363](../questions.d/QUESTION-363.md)'s three candidates, "the accessibility of
regions and the barriers between them", is the one that acts here. On
the 5-gon route there is no barrier to cross at all: the noise is zero in
the coordinates the crossing needs.

## What it does not say

- **That the 5⁺ route is closed.** It may open at a setting not tried, or
  with far longer training.
- **Anything for other trainers or models.** Adam, weight decay, Langevin
  noise and larger models are untested here.
- **That the posterior's order and SGD's order fail to correspond in
  general.** This is one model with one structural reason, a dead ReLU
  feature.
