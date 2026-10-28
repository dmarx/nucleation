---
number: 1030
status: Proposed
formerly:
- THEORY-tmpt0fr3
promote_when: >-
  Causal evidence, in more than one model, that hidden units act as the
  memories the reading names: ablating or patching a unit (or a small set)
  removes the next-token effect its key's patterns predict, on inputs
  that match those patterns and not on others; or editing a unit's output
  row changes the predictions after its patterns in the way its value says.
  Refuted if, in models where the reading is tested causally, the effects
  are carried mostly by directions that are not single units (so that the
  memories are the analyst's basis, not the model's), or if a unit's
  ablation changes predictions unrelated to its key's patterns as much as
  related ones. More maximum-activation patterns or vocabulary projections
  cannot settle it: that is the evidence it already rests on.
title: 'In transformer language models, each hidden unit of a feed-forward layer acts as a key–value memory, its input weights detecting patterns in the prefix and its output weights promoting the tokens that follow them, and a layer''s output composes many such memories while the residual stream refines the prediction from layer to layer, as Geva, Schuster, Berant and Levy propose'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-1200, the reading of Geva et al. (2021)
    in full, as the general reading the paper draws from what it measured
    in one model (THEORY-1033). The paper states that it expects
    the reading to hold for other transformers and leaves that untested.
tags:
- representation-learning
date: '2026-10-27'
source:
- LIT-1576
extends:
- THEORY-1033
summary: >-
  Geva et al. (2021), [LIT-1576](../literature.d/LIT-1576.md), read in [NOTE-1200](../notes.d/NOTE-1200.md): "feed-forward
  layers in transformer-based language models operate as key-value
  memories, where each key correlates with textual patterns in the
  training examples, and each value induces a distribution over the output
  vocabulary", and "we thus expect our qualitative empirical observations
  to hold across diverse settings". Evidence in one model, correlational
  only. ROME's storage hypothesis ([THEORY-1011](THEORY-1011.md)) borrows the name and reads
  keys and values at another level.
---
<!-- inactive-ok-file: THEORY-1011 THEORY-802 — Proposed; the storage hypothesis that borrows this reading and the basis question it bears on, cited as open -->

# THEORY-1030: In transformer language models, each hidden unit of a feed-forward layer acts as a key–value memory, its input weights detecting patterns in the prefix and its output weights promoting the tokens that follow them, and a layer's output composes many such memories while the residual stream refines the prediction from layer to layer, as Geva, Schuster, Berant and Levy propose

## Source

Geva et al. (2021), [LIT-1576](../literature.d/LIT-1576.md), read in full in [NOTE-1200](../notes.d/NOTE-1200.md).

## What is asserted

A functional reading of the algebra. FF(x) = f(x·Kᵀ)·V is an
unnormalized key–value memory (demonstrated, and Sukhbaatar et al.'s).
The claim is that trained models use it as one: the units' keys are
pattern detectors and their values next-token distributions, so that the
feed-forward layers are a store of pattern-to-continuation associations,
composed within a layer and refined across layers.

## What the record holds toward it

- **For:** [THEORY-1033](THEORY-1033.md), in one WikiText-103 model: recognizable
  patterns for every sampled key, a shallow-to-semantic gradient, and
  value–key agreement far above chance in the upper layers.
- **Weak where it matters:** that agreement is about 3.5% of units at
  best, and there is no causal test.
- **Against the unit as the unit of memory:** the dictionary-learning
  readings ([LIT-1545](../literature.d/LIT-1545.md), [LIT-1533](../literature.d/LIT-1533.md)) find MLP neurons largely polysemantic and
  read cleaner features off a learned overcomplete basis. That bears on
  "each hidden unit", not on the memory form. The record's basis question
  ([THEORY-802](THEORY-802.md)) applies to the choice of units as memories.
- **Borrowed at another level:** ROME ([LIT-1536](../literature.d/LIT-1536.md), [THEORY-1011](THEORY-1011.md)) reads the
  whole output matrix as a linear associative memory keyed by activation
  vectors. That reading is not this one, and evidence for one is not
  evidence for the other.

## Why it stays Proposed

The evidence is from one small model and is correlational throughout. The
reading's "each key correlates with textual patterns" is shown; "operate
as key–value memories", in the sense that the model's predictions are
produced by those associations, is not.

## What would confirm or reject it

The promote_when above.
