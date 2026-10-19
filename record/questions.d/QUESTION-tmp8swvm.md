---
status: Open
title: "Does the law of balance hold in a deep network trained on real data during its limiting dynamics: for parameter groups related by a rescaling symmetry, does the difference of squared norms move toward the value where the groups' gradient-noise traces are equal, at a rate that scales with learning rate over batch size?"
version: 1
tags:
- learning-theory
- loss-landscapes
date: '2026-10-19'
line: 'learned-structure'
refines:
- QUESTION-069
summary: >-
  The promotion condition formerly on [THEORY-211](../theory.d/THEORY-211.md), moved here unchanged when
  [THEORY-211](../theory.d/THEORY-211.md) was narrowed and promoted on 2026-10-19 to the SDE model in
  which the law of balance is proved. Whether the law holds for a deep
  network trained on real data is not shown; the tests are small synthetic
  networks.
---

# QUESTION-tmp8swvm: Does the law of balance hold in a deep network trained on real data during its limiting dynamics: for parameter groups related by a rescaling symmetry, does the difference of squared norms move toward the value where the groups' gradient-noise traces are equal, at a rate that scales with learning rate over batch size?

## Why it is a question

[THEORY-211](../theory.d/THEORY-211.md), narrowed on 2026-10-19, holds Ziyin, Li and Ueda's law of
balance ([LIT-1012](../literature.d/LIT-1012.md), Theorem 1) in the model it is proved in: the
stochastic-differential-equation model of SGD with a parameter-dependent
gradient-noise covariance. There, along a rescaling symmetry, the
difference of squared norms receives no noise and drifts, at a rate
proportional to learning rate over batch size, to the point where the two
groups' gradient-noise traces are equal. Until that date [THEORY-211](../theory.d/THEORY-211.md)'s
promote_when asked for the law measured in a deep network on real data. At
the owner's direction, from the promotion audit's batch 027 ([ADR-047](../decisions.d/ADR-047.md)), the
THEORY was narrowed and promoted on the model, and the condition moved
here unchanged.

It is open because the SDE model is an approximation of SGD at small
learning rates, and the evidence for its prediction is a small synthetic
ReLU network and toy models ([NOTE-714](../notes.d/NOTE-714.md)). It refines [QUESTION-069](QUESTION-069.md)'s question
of whether a trained solution's properties belong to the solutions or to
the regime they were trained in, and bears on [QUESTION-080](QUESTION-080.md), since motion
along a symmetry changes no function.

## What would answer it

The condition formerly on [THEORY-211](../theory.d/THEORY-211.md), unchanged. What would answer it
affirmatively: for parameter groups related by a rescaling symmetry
(adjacent layers through a ReLU, or the query and key matrices of
attention), the difference of squared norms moving toward the value at
which the groups' gradient-noise traces are equal, at a rate that scales
with learning rate over batch size, with weight decay adding to it, from
more than one initialization. What would answer it negatively: in such a
network at stationarity, the difference staying at its initial value, as
under gradient flow, or diffusing without a preferred value, as under
isotropic noise. A failure of the SDE approximation at the learning rates
used would limit the law, not refute it. More solvable toy models cannot
settle it.
