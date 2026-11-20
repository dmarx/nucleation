---
number: 2091
status: Proposed
formerly:
- THEORY-tmpoqh3f
title: 'Ito and colleagues find that pretraining a small network on rule primitives and two-rule combinations of a compositional rule task builds abstract rule representations that give high zero-shot accuracy on the full task, that a network without pretraining needs several times more samples, pretraining counted, to match it, and that reversing the pretraining order leaves generalization at chance'
version: 1
source:
- LIT-2877
tags:
- compositionality
- neuroscience
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent replication over several stated seeds finds that
  rule-primitive then two-rule pretraining gives zero-shot accuracy well
  above chance on held-out three-rule contexts, that a network without
  pretraining needs several times more total samples, pretraining
  included, to reach the same held-out accuracy, and that reversing the
  two stages leaves zero-shot accuracy near chance.
corroborates:
- CLAIM-756
summary: >-
  From the reading of [LIT-2877](../literature.d/LIT-2877.md) in [NOTE-2170](../notes.d/NOTE-2170.md). Learned primitives
  make compositions cheaper, pretraining counted; mechanism correlational.
  Proposed until its promote_when is met.
---

# THEORY-2091: Ito and colleagues find that pretraining a small network on rule primitives and two-rule combinations of a compositional rule task builds abstract rule representations that give high zero-shot accuracy on the full task, that a network without pretraining needs several times more samples, pretraining counted, to match it, and that reversing the pretraining order leaves generalization at chance

## The account

A 2×128 ReLU network: no pretraining, 23 per cent zero-shot on 64 contexts; primitives then two-rule pretraining, 92 per cent. Matching it from scratch takes up to 4.23 times the samples, pretraining included. The parallelism score tracks zero-shot accuracy during pretraining (r = 0.88). Reversed pretraining gives chance.

## Evidence

Seed count unstated (degrees of freedom suggest about 40 networks per condition); one task family; small MLPs.
