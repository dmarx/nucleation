---
number: 116
status: Proposed
formerly:
- THEORY-tmptd1hh
promote_when: >-
  A test of the stated direction, barrier ⇒ different mechanism, in deep
  networks trained on natural data. Take pairs that keep a linear barrier
  after the best available alignment, including the residual barriers
  of same-data seeds in narrow networks, and test each pair for shared
  invariances by intervening on the attributes the data are generated
  from, as in Lubana et al.'s Definitions 2–4. It is supported if every
  such pair fails to share some invariance. It is refuted by a pair with
  the same invariances under every intervention tested whose barrier
  survives alignment. That holds only when the alignment method is fixed
  in advance, since "not all symmetries were removed" must not be
  available as an escape after the fact. A proof beyond one hidden layer
  of the step the record lacks would also count: that two models relying
  on the same attributes share activation patterns up to symmetry. More
  synthetic-cue experiments in which barrier and cue reliance move
  together cannot settle it. They are the evidence already held, and they
  test the two directions jointly.
title: 'A linear barrier between two minima that survives the removal of symmetries marks a difference in the input attributes the two models rely on: they compute by different mechanisms'
version: 1
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-10-03'
source:
- LIT-669
- LIT-674
summary: >-
  Lubana et al. (2022), [LIT-669](../literature.d/LIT-669.md): models that rely on a synthetic cue
  and models that ignore it are separated by a linear barrier even after
  permutation matching. Fine-tuned models that keep a linear path to their
  parent keep its cue, and those that lose the path lose the cue. Their
  Conjecture 1 states this claim's direction. What their Appendix F.3
  proves, for a one-hidden-layer ReLU network with interpolating minima,
  is the converse: linear connectivity forces identical activation
  patterns, so models relying on attributes of different complexity
  cannot be linearly connected under any permutation. Zhou et al. (2023),
  [LIT-674](../literature.d/LIT-674.md), support that converse in deep image classifiers, where
  linearly connected pairs have features that blend layer by layer. The
  stated direction rests on experiments with synthetic cues and on a
  one-layer sufficiency argument.
extended_by:
- THEORY-111
---
<!-- inactive-ok-file: THEORY-111 THEORY-112 — Proposed; accounts this one is read beside, named in Connections, nothing here rests on them -->

# THEORY-116: A linear barrier between two minima that survives the removal of symmetries marks a difference in the input attributes the two models rely on: they compute by different mechanisms

## Source

- Lubana, Bigelow, Dick, Krueger & Tanaka (2022), [LIT-669](../literature.d/LIT-669.md), read in
  [NOTE-538](../notes.d/NOTE-538.md): Definitions 2–5, Conjecture 1, Figs. 4–5, Table 2, and
  Appendix F.3 (Lemmas 2–4, Theorem 1, Corollary 1, Remark 1, Fig. 13).
- Zhou, Yang, Yang, Yan & Hu (2023), [LIT-674](../literature.d/LIT-674.md), read in [NOTE-512](../notes.d/NOTE-512.md):
  Figs. 2–4 and Theorem 1, for the converse direction.

## The claim, and what "mechanism" means here

Two minima of one loss are separated by a barrier on the straight line
between them. The barrier remains after the architecture's symmetries
have been factored out, which in practice means neuron permutations. The
claim is that such a barrier is not an accident of parametrisation: the
two models rely on different attributes of the input. "Mechanism" is
Lubana et al.'s operational notion ([LIT-669](../literature.d/LIT-669.md), Definitions 2–4).
Model the data as generated from independent latent attributes. A model
is invariant to an intervention on one attribute if randomising that
attribute does not raise its loss. Two models are mechanistically similar
when they are invariant to the same interventions.

The claim has a converse that is better supported than the claim itself:
a linear low-loss path, up to symmetry, marks a shared mechanism. The
document keeps both, because the evidence comes in both directions and
must not be read as one.

## What was actually shown

**Fine-tuning, where the two directions co-occur.** Lubana et al. trained
VGG-13 and ResNet-18 on CIFAR-10 with a synthetic box cue correlated with
the label, then fine-tuned on cue-free data ([LIT-669](../literature.d/LIT-669.md), Fig. 5). With
small or medium learning rates, the fine-tuned model stayed linearly
connected to its parent and still relied on the cue on counterfactual
data. With a large learning rate, or with a cue perfectly correlated with
the label, there was a barrier, and the fine-tuned model was invariant to
the cue. In this controlled setting every barrier observed came with a
change of mechanism, and every kept path came with a kept mechanism. That
is the evidence for the stated direction in deep networks. It is a
co-occurrence across one fine-tuning protocol and three synthetic
datasets, not a test of the implication.

**Dissimilar endpoints have a barrier.** A model trained with the cue and
one trained without it are joined by a quadratic Bezier path that is low
loss on the data it was fitted to. The straight line between them has a
barrier, with or without activation-matching permutation (Fig. 4). This is
the converse direction: different mechanisms, therefore a barrier.

**The proof, and its direction.** Appendix F.3 works in a one-hidden-layer
ReLU network f(x; W) = (1/N)1ᵀϕ(Wᵀx), with binary labels and minima that
interpolate the data. Inputs carry attributes of different spline
complexity K plus noise dimensions. Lemma 2 shows that if two
interpolating minima are linearly mode connected on the data, every
hidden unit is on or off in both for every input: their activation
patterns are identical. Lemma 4 shows that models relying on attributes
of different complexity cannot have matching activation patterns under any
permutation of units. Theorem 1 combines them: such models are not
linearly connected under any permutation. Lemma 3, simplicity bias, is
restated from earlier work, not proved.

So what is proved is "different mechanism, of different complexity ⇒
barrier after every permutation", or equivalently "linearly connected up to
permutation ⇒ same activation patterns". That is the converse of
Conjecture 1 as the paper states it ("cannot be linear mode connected ...
must be mechanistically dissimilar"). The stated direction is equivalent
to "same mechanism ⇒ linearly connected up to permutation". For it the
appendix offers a sufficiency argument (Corollary 1, Remark 1). Two
models with identical activation patterns, up to permutation, are linear
in each other along the path, so they are linearly connected. The figure
offers the matching example: two models relying on the K = 4 attribute
connect after permutation, and a K = 0 model connects to a model trained
on both attributes, which simplicity bias makes rely on K = 0 too (Fig.
13). The missing step is that two models relying on the same attribute
have the same activation patterns up to permutation, and it is not
proved. The appendix's closing argument concerns a different gap, the
case of dissimilar mechanisms of equal complexity, and so it also bears
on the converse.

**The converse in deep networks.** Zhou et al. measured pairs that are
linearly connected, whether spawned from a shared early checkpoint or
aligned by permutation ([LIT-674](../literature.d/LIT-674.md), Figs. 2–3). In nearly every layer
of an MLP, VGG-16, ResNet-20 and ResNet-50, the features of the
interpolated network point in the direction of the interpolated features.
Independently trained pairs, which are not linearly connected, are far
from it (Fig. 4). Their Theorem 1 derives this layerwise linearity from
two conditions. The first, weak additivity of ReLU on the two networks'
pre-activations, amounts to the shared activation signs of Lubana et al.'s
Lemma 2, reached independently. Linearly connected deep networks therefore
compute the same features up to a linear blend, which is the converse
direction at the level of features. They did not intervene on data
attributes, so this is feature identity, not mechanism in Lubana et al.'s
sense.

## What this does not say

- **It does not say a barrier is always disagreement.** The stated
  direction is proved nowhere, and the deep-network evidence for it is one
  synthetic-cue fine-tuning protocol.
- **It does not say different mechanisms always produce a barrier.**
  Lubana et al. mark an exception themselves: dissimilar mechanisms of
  similar complexity can share activation patterns and be linearly
  connected (Table 2's asterisk, App. F.3). They argue the case is rare in
  practice, but do not show it.
- **It does not say curved connectivity means anything about mechanism.**
  Proposition 2 makes dissimilar minima mode connected along some path,
  given enough width. Fig. 4's curve holds only on the data it was fitted
  to and fails on counterfactuals.
- **"After symmetries are removed" is only as good as the alignment.**
  Every experiment uses permutations found by activation or weight
  matching, which is a heuristic. A barrier left by imperfect matching
  says nothing about mechanism. Unless the alignment is fixed in advance,
  the claim can always be rescued by saying not all symmetry was removed.
- **The cues are synthetic and the endpoints of Fig. 4 are trained on
  different data.** Two seeds on one dataset, the setting of the
  permutation conjecture, are not tested for mechanism at all.

## Connections

- **The barriers left after alignment.** The anthology's [ANTH-THEORY-010](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-010.md)
  says most of the barrier between independently trained networks is
  permutation, not disagreement. [THEORY-112](THEORY-112.md), filed alongside this
  one, says the barrier left after the full symmetry group is factored
  out falls with width and rises with depth. This account has to say what
  that residual barrier is. Either narrow or deep same-data seeds rely on
  different attributes, which nothing here has tested, or their residual
  barrier is a counterexample to the stated direction. That is the test
  `promote_when` asks for.
- **[THEORY-111](THEORY-111.md)** carries the converse direction further: from
  activation patterns in one hidden layer to every layer's features, and
  to what weight averaging does inside a basin.
- **Practice across the boundary.** The anthology's [ANTH-SOTA-217](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-217.md) (align
  permutations before averaging) assumes that what remains after alignment
  is benign. On this account it is benign only when the two models share
  a mechanism.
