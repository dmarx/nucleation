---
number: 792
status: Proposed
formerly:
- THEORY-tmpowz2q
promote_when: >-
  A derivation, or a controlled measurement across depths, showing that deep
  linear networks started off the decoupled set behave the same way:
  learning time, counted in iterations at the stable step size, bounded in
  depth when the initial end-to-end gain on every mode is of order one, and
  growing as a power of 1/ε when it is ε. That means random orthogonal or
  random small weights, not aligned with the task's singular vectors. More
  runs from decoupled starts cannot settle it, since there the result is
  already exact.
title: In a deep linear network trained by gradient descent from generic initial weights, not only from decoupled ones, depth slows learning through the initial end-to-end strength of each mode, so that random orthogonal weights, whose product is an isometry, learn in a number of iterations that stays bounded as depth grows, as Saxe, McClelland and Ganguli argue from simulation
version: 1
tags:
- learning-theory
date: '2026-10-20'
source:
- LIT-864
extends:
- THEORY-187
answers:
- QUESTION-166
summary: >-
  Saxe, McClelland and Ganguli (2014), [LIT-864](../literature.d/LIT-864.md), read in [NOTE-667](../notes.d/NOTE-667.md). The exact
  depth law is proved only from decoupled, balanced starts, and that part is
  the Active [THEORY-187](THEORY-187.md). Beyond it, the paper argues from MNIST runs and
  random-matrix simulations that random orthogonal layers are such a start
  in effect, because their product is an isometry, while scaled Gaussian
  layers are not. This THEORY holds that wider claim, which is argued and
  simulated and not derived.
---

# THEORY-792: In a deep linear network trained by gradient descent from generic initial weights, not only from decoupled ones, depth slows learning through the initial end-to-end strength of each mode, so that random orthogonal weights, whose product is an isometry, learn in a number of iterations that stays bounded as depth grows, as Saxe, McClelland and Ganguli argue from simulation

## Source

[LIT-864](../literature.d/LIT-864.md). Filed by the promotion audit's narrowing-loss sweep
(batch 066, [ADR-047](../decisions.d/ADR-047.md) v4) on 2026-10-20, to carry the wider claim that the
narrowing of [THEORY-187](THEORY-187.md) dropped. [THEORY-187](THEORY-187.md) is Active and is this
THEORY's evidence; this one stays Proposed.

## What was actually shown

The paper solves the dynamics exactly when the initial weights are
decoupled: aligned with the singular vectors of the input–output
correlation and balanced across layers. [THEORY-187](THEORY-187.md) states that result,
re-derived in the promotion audit. The paper then argues, from MNIST
runs and from simulations of random matrix products, that random
orthogonal layers behave like a decoupled start of order-one strength,
because the product of orthogonal matrices is an isometry on every mode,
and that scaled Gaussian layers preserve norms but not isometry and so
learn slowly at depth ([NOTE-667](../notes.d/NOTE-667.md), §3 and the closing sections). That step
is the argument this THEORY records. No derivation covers a start off the
decoupled set.

## What would settle it

The promote_when is inherited from [THEORY-187](THEORY-187.md)'s before it was
narrowed, and [QUESTION-166](../questions.d/QUESTION-166.md) asks the same question.

## What this does not say

It does not say that the ε law of [THEORY-187](THEORY-187.md) (a plateau growing from
ln(1/ε) towards 1/ε) holds from small random weights; the paper argues
that small Gaussian starts are slow but does not derive their rate. It
says nothing about nonlinear networks, beyond the paper's separate and
also simulated claim about tanh networks near gain 1. It is not advice
on how to initialise.
