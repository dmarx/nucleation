---
number: 39
status: Open
formerly:
- QUESTION-039
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
summary: >-
  Filed in the fourth synthesis pass to give readings no question asked
  for a place in the argument. It bears on [CLAIM-164](../claims.d/CLAIM-164.md). [THEORY-086](../theory.d/THEORY-086.md),
  [THEORY-187](../theory.d/THEORY-187.md), [THEORY-200](../theory.d/THEORY-200.md), [THEORY-204](../theory.d/THEORY-204.md) and [THEORY-039](../theory.d/THEORY-039.md) answer it in part; the
  body gives each one's limit.
---
<!-- inactive-ok-file: THEORY-1353 — Proposed or Open; cited from the reading of Dong (2026) as open -->
<!-- inactive-ok-file: THEORY-279 — Proposed; partial answers filed in the last two days, cited with their limits -->
<!-- inactive-ok-file: THEORY-tmpr9w2r — Proposed, new or Deferred; filed on 2026-11-21 from the readings of that day -->

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

## Note of 2026-11-04: Dong, "The Kinetics of Training", read

Dong (2026; [THEORY-1353](../theory.d/THEORY-1353.md)) answers this question for conjunction
circuits in transformers to about 1B parameters. The moment is dated by a
precursor clock, prospective for induction heads only (six unseen models,
median error 5.0%). The order is cheap stages first and the joint
alignment last. Acquisition is one kind of rate-limiting event, a single
joint step: a chain of comparable steps would show an Erlang shape, and
the measured shape is exponential. The answer is single-author and
unreplicated, and its exponential evidence is strongest in a toy. No
status changes.

## Note of 2026-11-19: the data-scheduling readings, read
<!-- inactive-ok-file: THEORY-2065 THEORY-2071 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Two readings bear on order. Hu and colleagues ([THEORY-2071](../theory.d/THEORY-2071.md), bears_on): structure first, and the first phase's duration, set the later cost. Chen and colleagues ([THEORY-2065](../theory.d/THEORY-2065.md), bears_on): which skills help which is set by the data and departs from the task's dependency order, and ordering skills in sequence does no better than random. Whether acquisition is one kind of event or several stays open.

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: THEORY-2058 THEORY-2060 THEORY-2074 THEORY-2075 THEORY-2081 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

The follow-up readings bear on the order of data more than on the moment a
structure is acquired. Zhang and colleagues ([THEORY-2074](../theory.d/THEORY-2074.md), bears_on):
difficulty order moves when aggregate competence arrives, mostly not the
endpoint. Nishida and colleagues ([THEORY-2060](../theory.d/THEORY-2060.md)) and Wang and colleagues
([THEORY-2058](../theory.d/THEORY-2058.md)) describe which data align with training early and late,
attribution only. Stern and colleagues ([THEORY-2081](../theory.d/THEORY-2081.md)) find what a
separate first phase taught is overwritten at the switch and kept under
interleaving, so order bears on retention as well as acquisition. The
procedural paper ([THEORY-2075](../theory.d/THEORY-2075.md)) finds the first phase's length matters
non-monotonically. Background for the question's mechanisms.

## Note of 2026-11-19: the task-composition readings, read
<!-- inactive-ok-file: THEORY-2090 THEORY-2091 THEORY-2092 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Ito and colleagues ([THEORY-2091](../theory.d/THEORY-2091.md)): the order of pretraining stages
decides whether compositional generalization appears at all. He and
colleagues ([THEORY-2092](../theory.d/THEORY-2092.md)): grokking unfolds as saturation, then bridge
recovery, then integration of facts. Driscoll and colleagues
([THEORY-2090](../theory.d/THEORY-2090.md)): slow acquisition of motifs, then fast recombination.

## Note of 2026-11-21: Hoogland, Wang, Farrugia-Roberts, Carroll, Wei & Murfet, read

Bears on whether acquisition is one kind of event ([NOTE-tmp2pgi8](../notes.d/NOTE-tmp2pgi8.md),
[THEORY-tmpr9w2r](../theory.d/THEORY-tmpr9w2r.md)). The stages include acquisitions (bigrams, n-grams,
induction heads, in-context learning), groundwork laid before any visible
change (§6.2), and simplifications in which the estimated coefficient falls
(LM3, LR3, LR4; [QUESTION-tmphkb1w](QUESTION-tmphkb1w.md)). So "acquisition" in this paper is
several kinds of event, timed by one scalar. Written as `bears_on` from the
reading.


## Note of 2026-11-22: the optimizer swap, run ([LEAD-045](../leads.d/LEAD-045.md))

<!-- inactive-ok-file: CASE-tmpd2k95 CLAIM-tmpyepkb CLAIM-tmpmop4m — new; the study and claims of LEAD-045, filed 2026-11-22 -->

The test this question proposes, the same skills under gradient descent and
under sign descent, was run ([CASE-tmpd2k95](../cases.d/CASE-tmpd2k95.md)). In the Geometry model, sign
descent re-times gradient descent's own path by the gradient norm
([CLAIM-tmpyepkb](../claims.d/CLAIM-tmpyepkb.md)): the optimizer sets when each skill arrives, not the
order or the path. In one small ReLU network ([CLAIM-tmpmop4m](../claims.d/CLAIM-tmpmop4m.md)), the delay
from the optimizer appeared at order-one scale, and the delay from small
initialization appeared under gradient descent at scale 0.01 and weakened
under sign descent: two mechanisms that answer to different interventions.
The hierarchical task from small and order-one scale was not run. The
question is unchanged.
