---
number: 2006
status: Proposed
formerly:
- THEORY-tmp3dqbl
title: 'Springer and colleagues show that, past an inflection point in pre-training length, language models degrade more under a fixed-size later modification (fine-tuning or weight noise), so that longer pre-training can leave a worse model after fine-tuning even though the base model keeps improving, and they attribute this mainly to forgetting of pre-trained capability that grows with pre-training ("progressive sensitivity").'
version: 1
source:
- LIT-2829
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
bears_on:
- QUESTION-495
corroborates:
- CLAIM-675
- CLAIM-758
promote_when: >-
  An independent group, on checkpoints or models not the authors', finds
  at a fixed fine-tuning learning rate that the rise in pre-training loss
  caused by fine-tuning grows monotonically with pre-training tokens, and
  that this rise eventually outweighs the base model's gain, so the fine-
  tuned model's pre-training loss is U-shaped in tokens; on at least one
  family where each budget is annealed separately.
summary: >-
  From the reading of [LIT-2829](../literature.d/LIT-2829.md) in [NOTE-2119](../notes.d/NOTE-2119.md). Springer, Goyal, Wen,
  Kumar, Yue, Malladi, Neubig and Raghunathan (2025), arXiv 2503.19206.
  They name "catastrophic overtraining": past an inflection point, longer
  pre-training leaves a worse model after instruction or multimodal fine-
  tuning even though the base model keeps improving (OLMo-1B at 3T against
  2.3T tokens; not seen at 7B up to 3T). In controlled small models and a
  deep-linear theory, they trace it to "progressive sensitivity": a fine-
  tune of fixed size destroys more pre-trained capability the longer the
  model was pre-trained. The cost shows up mostly as forgetting caused by
  the acquisition, and the new task itself gets worse only in some
  settings. It is here as the prime empirical case for overconsolidation
  ([CLAIM-758](../claims.d/CLAIM-758.md)) and the Pythia study ([CASE-294](../cases.d/CASE-294.md)), which it
  qualifies: the case is mainly about forgetting under modification, not a
  higher budget to acquire. Read in its NOTE.
---
<!-- inactive-ok-file: CASE-294 CLAIM-758 — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-2006: Springer and colleagues show that, past an inflection point in pre-training length, language models degrade more under a fixed-size later modification (fine-tuning or weight noise), so that longer pre-training can leave a worse model after fine-tuning even though the base model keeps improving, and they attribute this mainly to forgetting of pre-trained capability that grows with pre-training ("progressive sensitivity").

## The account

Extended pre-training improves the base model steadily. For a modification of fixed size, though, the harm to pre-trained capability grows with pre-training ("for modifications of equal magnitude, models that have undergone longer pre-training exhibit greater forgetting"). When that growth outruns the base model's improvement, the post-trained model gets worse with more pre-training. Tuning the fine-tuning learning rate moves the damage between the new task and the old one rather than removing it. In a two-layer linear model, "Catastrophic overtraining is inevitable without regularization", and regularization delays it "at the cost of downstream performance".

## What it does not show

- Not that longer pre-training raises the budget needed to acquire a new task. Acquisition budget is not measured, and the effect is mostly on the old capability.
- Not that any intervention restores plasticity late. Only fine-tuning-time choices are tried, and they trade.
- Not at 7B up to 3T tokens, where it is not observed.
- Not a general law: one run per real model family, small controlled models, a linear theory.

## Note of 2026-11-19: Anguita and colleagues, read
A contrast ([NOTE-tmpr453b](../notes.d/NOTE-tmpr453b.md)): Anguita and colleagues vary initialization, not pretraining length, and measure only fine-tuning error, so their account says nothing about catastrophic overtraining or forgetting.

## Note of 2026-11-19: Howard and Ruder, read
A parallel ([NOTE-tmp44esf](../notes.d/NOTE-tmp44esf.md)): Howard and Ruder also find that full fine-tuning at an aggressive rate loses the pretrained benefit and that a gentler schedule keeps it; they do not vary pretraining length.
