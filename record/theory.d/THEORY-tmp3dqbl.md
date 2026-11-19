---
status: Proposed
title: 'Springer and colleagues show that, past an inflection point in pre-training length, language models degrade more under a fixed-size later modification (fine-tuning or weight noise), so that longer pre-training can leave a worse model after fine-tuning even though the base model keeps improving, and they attribute this mainly to forgetting of pre-trained capability that grows with pre-training ("progressive sensitivity").'
version: 1
source:
- LIT-tmpq5g0q
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
bears_on:
- QUESTION-tmpwqepn
corroborates:
- CLAIM-675
promote_when: >-
  An independent group, on checkpoints or models not the authors', finds
  at a fixed fine-tuning learning rate that the rise in pre-training loss
  caused by fine-tuning grows monotonically with pre-training tokens, and
  that this rise eventually outweighs the base model's gain, so the fine-
  tuned model's pre-training loss is U-shaped in tokens; on at least one
  family where each budget is annealed separately.
summary: >-
  From the reading of [LIT-tmpq5g0q](../literature.d/LIT-tmpq5g0q.md) in [NOTE-tmpp1jb7](../notes.d/NOTE-tmpp1jb7.md). Springer, Goyal, Wen,
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
  ([CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)) and the Pythia study ([CASE-tmphsr99](../cases.d/CASE-tmphsr99.md)), which it
  qualifies: the case is mainly about forgetting under modification, not a
  higher budget to acquire. Read in its NOTE.
---
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-tmp8ljvp — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-tmp3dqbl: Springer and colleagues show that, past an inflection point in pre-training length, language models degrade more under a fixed-size later modification (fine-tuning or weight noise), so that longer pre-training can leave a worse model after fine-tuning even though the base model keeps improving, and they attribute this mainly to forgetting of pre-trained capability that grows with pre-training ("progressive sensitivity").

## The account

Extended pre-training improves the base model steadily. For a modification of fixed size, though, the harm to pre-trained capability grows with pre-training ("for modifications of equal magnitude, models that have undergone longer pre-training exhibit greater forgetting"). When that growth outruns the base model's improvement, the post-trained model gets worse with more pre-training. Tuning the fine-tuning learning rate moves the damage between the new task and the old one rather than removing it. In a two-layer linear model, "Catastrophic overtraining is inevitable without regularization", and regularization delays it "at the cost of downstream performance".

## What it does not show

- Not that longer pre-training raises the budget needed to acquire a new task. Acquisition budget is not measured, and the effect is mostly on the old capability.
- Not that any intervention restores plasticity late. Only fine-tuning-time choices are tried, and they trade.
- Not at 7B up to 3T tokens, where it is not observed.
- Not a general law: one run per real model family, small controlled models, a linear theory.
