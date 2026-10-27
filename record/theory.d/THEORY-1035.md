---
number: 1035
status: Proposed
formerly:
- THEORY-tmp2tsxo
promote_when: >-
  Evidence from a trained network that is not a toy: for features
  identified independently of the account (for instance by a sparse
  dictionary), capacities measured at a layer, and the features with
  capacity strictly between 0 and 1 found to have approximately equal
  marginal loss reduction from more capacity, estimated by intervention;
  sparser or higher-kurtosis features found more often shared, across
  features or across training distributions; and block structure in the
  embedding differing between architectures trained on the same data in
  the direction the account predicts. Refuted if shared features in a
  trained network have marginal values that differ widely, or if
  sparsity does not predict sharing. Further solved toy models, or the
  phase diagrams of six-feature models, cannot settle it.
title: 'In trained neural networks, polysemantic neurons arise from the loss-optimal allocation of a layer''s limited capacity among features: a feature is shared between neurons when its marginal loss reduction from capacity equals that of the features it shares with, so that sparser, higher-kurtosis inputs, which make returns to capacity diminish, produce more polysemanticity, and the block structure of the embedding, which architecture shapes, sets how many features each neuron mixes, as Scherlis, Sachan, Jermyn, Benton and Shlegeris propose'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-1205, as the claim the demonstrated
    THEORY-1036 leaves out (ADR-047 v4). The authors offer it as a
    suspicion: the framework "is getting at some important aspects of
    what's going on in the training process for real neural networks,
    though probably the story in large models is probably substantially
    messier" (the announcing post).
tags:
- representation-learning
date: '2026-10-27'
source:
- LIT-1625
extends:
- THEORY-1036
summary: >-
  Scherlis et al. (2022), [LIT-1625](../literature.d/LIT-1625.md), read in [NOTE-1205](../notes.d/NOTE-1205.md). The
  paper's account of polysemanticity in general: capacity allocation at
  the loss optimum, driven by sparsity, with architecture deciding block
  size. The general first-order condition holds for any loss under two
  stated assumptions; its application to trained networks, and the role
  of architecture, rest on toy models only.
---
# THEORY-1035: In trained neural networks, polysemantic neurons arise from the loss-optimal allocation of a layer's limited capacity among features: a feature is shared between neurons when its marginal loss reduction from capacity equals that of the features it shares with, so that sparser, higher-kurtosis inputs, which make returns to capacity diminish, produce more polysemanticity, and the block structure of the embedding, which architecture shapes, sets how many features each neuron mixes, as Scherlis, Sachan, Jermyn, Benton and Shlegeris propose

## Source

Scherlis et al. (2022), *Polysemanticity and Capacity in Neural
Networks*, [LIT-1625](../literature.d/LIT-1625.md), read in full in [NOTE-1205](../notes.d/NOTE-1205.md): §§1, 2, 3.7, 4.6
and 5, and the Alignment Forum post that announced it.

## What is asserted

That polysemanticity can be understood "through the lens of feature
capacity": the model has a fixed amount of capacity to allocate, the
optimum equalizes marginal returns among partially represented features,
"polysemanticity will arise when there are diminishing marginal returns
to capacity", which sparse inputs produce, and "differences in
architecture can lead to different sizes of blocks, which could provide a
way to control the extent of polysemanticity in models".

## What the record holds toward it

- **The first-order condition (§2.2),** which needs only that capacity
  never hurts and that every allocation is realizable. It is general, but
  it describes an optimum, and trained networks need not reach it.
- **One model solved** ([THEORY-1036](THEORY-1036.md)), where the account holds
  exactly.
- **Six-feature numerical comparisons** with Elhage et al.'s autoencoder
  ([LIT-323](../literature.d/LIT-323.md)) under three activations, shown as phase diagrams: the
  qualitative shape agrees, the block structure differs.

## Why it stays Proposed

No trained network is examined, the comparisons are of toy models, and
the authors themselves expect the story in large models to be messier.
The architecture claim rests on one contrast between two toys.

## What would confirm or reject it

The promote_when above.
