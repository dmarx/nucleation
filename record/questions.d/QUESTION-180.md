---
number: 180
status: Open
formerly:
- QUESTION-tmphiinp
title: 'Does the rate-distortion function of an optimisation trajectory given its sample, with the coupling coefficient M bounded or estimated and the 4Lε term kept, account for the generalisation of trained networks?'
version: 1
tags:
- learning-theory
- information-theory
date: '2026-10-19'
line: 'learned-structure'
summary: >-
  Filed when the promotion audit (batch 038) narrowed and promoted
  [THEORY-266](../theory.d/THEORY-266.md), Theorem 7 of [LIT-233](../literature.d/LIT-233.md), on its proof. The former promote_when
  asked for an evaluation that would settle whether the trajectory's
  compressibility given the sample accounts for generalisation. That is
  more than the theorem says. This question holds it.
---

# QUESTION-180: Does the rate-distortion function of an optimisation trajectory given its sample, with the coupling coefficient M bounded or estimated and the 4Lε term kept, account for the generalisation of trained networks?

## Why it is a question

[THEORY-266](../theory.d/THEORY-266.md) states Theorem 7 of [LIT-233](../literature.d/LIT-233.md). For a loss in [0, 1] that is
L-Lipschitz in a distortion, the average generalisation error along a
trajectory is bounded, with high probability, through the
rate-distortion function of the trajectory's law given the sample, a
coupling coefficient M and a distortion term 4Lε. In the proof, the
trajectory's information about its sample enters only through M. The
paper's CIFAR-10 experiment drops M and 4Lε. It shows only that the
estimated rate and the test gap fall together over learning rates, on
separate axes. For FCN4 the plotted rate term is about 3, which is vacuous
for 0–1 loss.

So whether compressibility given the data, which is what the experiment
compares, accounts for generalisation is open. The term that carries the
dependence on the data was left out.

## What would answer it

An evaluation of Theorem 7's bound for a trained network that bounds or
estimates M from data and keeps the 4Lε term, with the rate-distortion
function estimated by a method whose error is controlled. Co-movement of an
estimated rate with test error across learning rates or architectures,
with M dropped, cannot settle it.
