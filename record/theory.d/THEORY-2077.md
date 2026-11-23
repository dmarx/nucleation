---
number: 2077
status: Proposed
formerly:
- THEORY-tmppm9la
title: 'Anguita and colleagues show in two-layer diagonal linear networks trained to convergence that the initialization''s absolute scale, its relative scale between layers and the readout''s scale at fine-tuning place fine-tuning in one of four regimes that trade reuse of pretrained features against a bias to learn sparse new ones; that the relative scale changes fine-tuning''s inductive bias even when the pretrained function is the same; and that which regime generalizes best depends on how the fine-tuning task''s features overlap the pretrained ones'
version: 1
source:
- LIT-2861
extends:
- THEORY-tmpw69kb
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  A rigorous derivation or independent replication confirms that diagonal
  linear networks with the same pretrained function and different relative
  layer scale reach different fine-tuning generalization, with the best
  regime changing with task overlap as stated; or a controlled experiment
  in a nonlinear network, with feature overlap set by design, shows the
  same overlap-dependent ranking.
corroborates:
- CLAIM-754
- CLAIM-675
summary: >-
  From the reading of [LIT-2861](../literature.d/LIT-2861.md) in [NOTE-2159](../notes.d/NOTE-2159.md). Cited by ChatGPT for
  the owner's point at U37; it gives an analytical case of equal present
  capability with different later learning. Proposed until its
  promote_when is met.
---

# THEORY-2077: Anguita and colleagues show in two-layer diagonal linear networks trained to convergence that the initialization's absolute scale, its relative scale between layers and the readout's scale at fine-tuning place fine-tuning in one of four regimes that trade reuse of pretrained features against a bias to learn sparse new ones; that the relative scale changes fine-tuning's inductive bias even when the pretrained function is the same; and that which regime generalizes best depends on how the fine-tuning task's features overlap the pretrained ones

## The account

Pretrain a two-layer diagonal linear network to zero error, re-balance
it, reset the readout to a chosen scale and fine-tune. Fine-tuning's
implicit bias is a per-dimension penalty set by the pretrained function
and by three scales: the initialization's absolute scale, the relative
scale between the layers, and the readout's. They place fine-tuning in
one of four regimes, rich or lazy and dependent on pretraining or not,
and full reliance on pretraining cannot be combined with full sparsity
bias. The relative scale leaves the pretrained function unchanged and
still changes what fine-tuning learns. Which regime generalizes best
depends on the fine-tuning task: reuse when its features coincide with
the pretrained ones, new learning when they do not, the rich dependent
regime when they are a subset.

## Evidence

A theorem for the implicit bias and a non-rigorous replica calculation
for the error, in a solvable model; qualitative experiments in ResNets
and a one-layer Transformer. Pretraining length is never varied.

## Note of 2026-11-23: Lippl and Lindsey, read
<!-- inactive-ok-file: THEORY-tmpw69kb — Proposed or new; filed by the lead run of 2026-11-23 -->

The theory this one extends is now read ([THEORY-tmpw69kb](THEORY-tmpw69kb.md);
[NOTE-tmpw2i45](../notes.d/NOTE-tmpw2i45.md)): infinitesimal initialization with balanced layers, the
readout scale γ the only free scale, and three of the four regimes here
(rich, lazy, and nested feature selection, which this account's rich,
pretraining-dependent regime resembles, both being best when the main
task uses a subset of the pretrained features). Where this account sets the relative scale at
initialization, Lippl and Lindsey reach a nested regime by rescaling the
weights after pretraining. `extends` is written. The reading does not
meet this account's promote_when: it is the earlier, narrower theory,
not an independent derivation.
