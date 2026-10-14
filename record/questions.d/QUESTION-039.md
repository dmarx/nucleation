---
number: 39
status: Open
formerly:
- QUESTION-tmp0dy29
title: 'What sets the order and the moment, in training time or in examples, at which a network acquires a structure, and is acquisition one kind of event or several?'
version: 1
tags:
- learning-theory
- representation-learning
- compositionality
date: '2026-10-12'
line: 'learned-structure'
answered_by:
- THEORY-086
- THEORY-187
- THEORY-200
- THEORY-204
- THEORY-039
- THEORY-212
- THEORY-tmpbaoyn
summary: >-
  Filed in the fourth synthesis pass to give readings no question asked
  for a place in the argument. It bears on [CLAIM-164](../claims.d/CLAIM-164.md). [THEORY-086](../theory.d/THEORY-086.md),
  [THEORY-187](../theory.d/THEORY-187.md), [THEORY-200](../theory.d/THEORY-200.md), [THEORY-204](../theory.d/THEORY-204.md) and [THEORY-039](../theory.d/THEORY-039.md) answer it in part; the
  body gives each one's limit.
refined_by:
- QUESTION-081
---
<!-- inactive-ok-file: THEORY-tmpbaoyn — Proposed; a partial answer filed today, cited with its limit -->

# QUESTION-039: What sets the order and the moment, in training time or in examples, at which a network acquires a structure, and is acquisition one kind of event or several?

## The question

Networks acquire structure in an order and at thresholds. These include eigenspaces fitted at different rates, plateaus that end abruptly, invariances that appear at a training-set size, and correlations resolved out to a horizon. The question is what fixes when each structure arrives, whether that is data statistics, initial scale, depth or architecture, and whether the transitions reported under the name of "phases" are one phenomenon.

## Why the record needs it

The learned-structure line asks which structure training reaches and why. When it is reached is half of that. The record holds several mechanisms that each predict a threshold, and none of them is compared with the others. [CLAIM-164](../claims.d/CLAIM-164.md) is touched: in the kernel regime the unit that gets acquired is a whole eigenspace, and the guarantee is stated only for whole eigenspaces.

## What the record holds

- [THEORY-086](../theory.d/THEORY-086.md): in the kernel regime gradient descent fits "eigenspace by eigenspace", at rates set by the eigenvalues. Limit: linearised dynamics; Nanda et al.'s kernel moved.
- [THEORY-187](../theory.d/THEORY-187.md): from a small start ε, depth lengthens the plateau from about ln(s/ε) towards a power of 1/ε, and costs a bounded number of iterations from an order-one start. Limit: deep linear networks, decoupled starts.
- [THEORY-200](../theory.d/THEORY-200.md): invariance to synonyms and to displacements arrives "at the training-set size at which they learn the task". Limit: the model builds both invariances on shared statistics.
- [THEORY-204](../theory.d/THEORY-204.md): P tokens resolve correlations out to a horizon n*(P) ~ P^(1/(2β)), and the loss is the entropy at that horizon. Limit: it rests on assumptions; P reaches about 10^8.
- [THEORY-039](../theory.d/THEORY-039.md): the later phases "differ in kind", and none is a measured compression of I(X;T). This is the caution against reading every transition as one event.
- [THEORY-tmpbaoyn](../theory.d/THEORY-tmpbaoyn.md): for a symmetrized Barlow Twins loss on a linear or fixed-kernel model, gradient flow from small initialization learns the top eigenvectors of the pairs' cross-correlation one at a time, in order of eigenvalue, each at a time set by its eigenvalue and the log of the initial scale. The self-supervised instance of the [THEORY-187](../theory.d/THEORY-187.md) mechanism. Limit: proved from aligned initialization only; stepwise growth in ResNets is an experiment.

## What would answer it

One setting in which two of these mechanisms make different predictions about timing, measured with each work's own quantity. For example, a hierarchical task trained from small and from order-one initial scale.
