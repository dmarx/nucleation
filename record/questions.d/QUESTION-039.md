---
number: 39
status: Open
formerly:
- QUESTION-tmp0dy29
title: 'What sets the order and the moment, in training time or in examples, at which a network acquires a structure, and is acquisition one kind of event or several?'
version: 2
history:
- version: 2
  date: '2026-10-26'
  note: >-
    A dated note added: the induction-heads paper, read on 2026-10-26
    for the exchange "Experimental Infrastructure Review", answers part
    of the question (THEORY-973), and the refined-LLC study reports
    several kinds of developmental event per component. The question is
    unchanged.
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
- THEORY-229
- THEORY-253
- THEORY-279
- THEORY-283
- THEORY-293
- THEORY-481
- THEORY-521
- THEORY-973
summary: >-
  Filed in the fourth synthesis pass to give readings no question asked
  for a place in the argument. It bears on [CLAIM-164](../claims.d/CLAIM-164.md). [THEORY-086](../theory.d/THEORY-086.md),
  [THEORY-187](../theory.d/THEORY-187.md), [THEORY-200](../theory.d/THEORY-200.md), [THEORY-204](../theory.d/THEORY-204.md) and [THEORY-039](../theory.d/THEORY-039.md) answer it in part; the
  body gives each one's limit.
refined_by:
- QUESTION-081
- QUESTION-158
- QUESTION-166
- QUESTION-176
- QUESTION-175
- QUESTION-193
- QUESTION-275
---
<!-- inactive-ok-file: THEORY-279 — Proposed; partial answers filed in the last two days, cited with their limits -->

# QUESTION-039: What sets the order and the moment, in training time or in examples, at which a network acquires a structure, and is acquisition one kind of event or several?

## The question

Networks acquire structure in an order and at thresholds. These include eigenspaces fitted at different rates, plateaus that end abruptly, invariances that appear at a training-set size, and correlations resolved out to a horizon. The question is what fixes when each structure arrives, whether that is data statistics, initial scale, depth, architecture or the optimizer, and whether the transitions reported under the name of "phases" are one phenomenon.

## Why the record needs it

The learned-structure line asks which structure training reaches and why. When it is reached is half of that. The record holds several mechanisms that each predict a threshold, and none of them is compared with the others. [CLAIM-164](../claims.d/CLAIM-164.md) is touched: in the kernel regime the unit that gets acquired is a whole eigenspace, and the guarantee is stated only for whole eigenspaces.

## What the record holds

- [THEORY-086](../theory.d/THEORY-086.md): in the kernel regime gradient descent fits "eigenspace by eigenspace", at rates set by the eigenvalues. Limit: linearised dynamics; Nanda et al.'s kernel moved.
- [THEORY-187](../theory.d/THEORY-187.md): from a small start ε, depth lengthens the plateau from about ln(s/ε) towards a power of 1/ε, and costs a bounded number of iterations from an order-one start. Limit: deep linear networks, decoupled starts.
- [THEORY-200](../theory.d/THEORY-200.md): invariance to synonyms and to displacements arrives "at the training-set size at which they learn the task". Limit: the model builds both invariances on shared statistics.
- [THEORY-204](../theory.d/THEORY-204.md): P tokens resolve correlations out to a horizon n*(P) ~ P^(1/(2β)), and the loss is the entropy at that horizon. Limit: it rests on assumptions; P reaches about 10^8.
- [THEORY-039](../theory.d/THEORY-039.md): the later phases "differ in kind", and none is a measured compression of I(X;T). This is the caution against reading every transition as one event.
- [THEORY-229](../theory.d/THEORY-229.md): for a symmetrized Barlow Twins loss on a linear or fixed-kernel model, gradient flow from small initialization learns the top eigenvectors of the pairs' cross-correlation one at a time, in order of eigenvalue, each at a time set by its eigenvalue and the log of the initial scale. The self-supervised instance of the [THEORY-187](../theory.d/THEORY-187.md) mechanism. Limit: proved from aligned initialization only; stepwise growth in ResNets is an experiment.
- [THEORY-279](../theory.d/THEORY-279.md): image classifiers and language models act on low-order statistics first, first-order before second-order, and later lose that sensitivity. Acquiring later structure can remove earlier behaviour. Limit: empirical, and the ordering is shown for first- before second-order only.
- [THEORY-253](../theory.d/THEORY-253.md): in a toy model of independent skills, the order is frequency order whatever the optimizer, but whether onset is sequential is set by the optimizer: gradient descent learns orthogonal skills together, sign descent one after another (the Domino effect). Limit: toy-model simulation and one fitted ODE.
- [THEORY-283](../theory.d/THEORY-283.md): for a two-layer network on a hierarchical multi-index target, direction k becomes recoverable at a sample count ∝ a_k^(−2), one at a time, through sharp spectral transitions. Limit: a theorem in sample size, not in training time; the network is a spectral first layer with a ridge readout.
- [THEORY-293](../theory.d/THEORY-293.md): for a capacity-bounded learner on a mixture of random facts and a second domain, the facts are learned not at all below a capacity threshold set by the mixing ratio, and Pythia models show the same threshold. Limit: static, saying whether facts are learned and not when; it assumes an ideal learner.

[LIT-954](../literature.d/LIT-954.md) files no theory and is not a single-event account: it puts thresholds and power laws in one vocabulary but treats them as two kinds of event, connectivity changes and waiting-time statistics.

## What would answer it

One setting in which two of these mechanisms make different predictions about timing, measured with each work's own quantity. For example, a hierarchical task trained from small and from order-one initial scale. Or the same skills trained by gradient descent and by sign descent: the steps of [THEORY-229](../theory.d/THEORY-229.md) are a property of gradient flow, while the Domino steps of [THEORY-253](../theory.d/THEORY-253.md) vanish under it, so swapping the optimizer separates the two mechanisms.

## Note of 2026-10-26: induction heads, and several kinds of event

<!-- inactive-ok-file: THEORY-967 THEORY-1004 — Proposed; readings of the same day, cited with their limits -->

Three works T24 of the exchange "Experimental Infrastructure Review" drew
on for [QUESTION-275](QUESTION-275.md), which refines this one, were read on
2026-10-26.

- **[THEORY-973](../theory.d/THEORY-973.md)** answers in part. In small attention-only
  transformers of two to six layers, the moment in-context learning
  arrives is the window in which induction heads form; ablating them
  removes nearly all of it; one-layer models show neither; and letting a
  single layer attend by the previous token, which removes the need for
  two heads to compose, brings the jump to one-layer models and moves it
  earlier in two-layer ones. So the moment is set, there, by when a
  composition becomes available. Limit: one family of models, one run per
  model and one data order, and a window that overlaps learning-rate
  warm-up. Whether induction drives the transition or accompanies a
  shared latent event, such as learning to compose layers, the authors
  leave open themselves.
- **One kind of event or several.** The refined-LLC study ([NOTE-1188](../notes.d/NOTE-1188.md))
  reports at least three per component: growth (a head's local learning
  coefficient rising), refinement (it falling),
  and repurposing, in which first-layer n-gram heads become the induction
  circuit's previous-token heads and n-grams pass between heads
  ([THEORY-967](../theory.d/THEORY-967.md), Proposed, from two checkpoints of one run). The
  per-head curves differentiate by functional type over training
  ([THEORY-975](../theory.d/THEORY-975.md)), which bears on when heads specialize, not on when a
  structure is acquired, and is not listed as an answer.
- **Features.** Cross-checkpoint crosscoders show the features that
  matter for agreement moving from token-specific to category detectors,
  and still shifting after accuracy has stopped improving
  ([THEORY-1004](../theory.d/THEORY-1004.md), Proposed). Acquisition read off a task score can end
  before the structure stops changing.

The question is unchanged.
