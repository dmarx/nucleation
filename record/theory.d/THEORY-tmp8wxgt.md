---
status: Proposed
title: 'Han and colleagues show that, in Llama-2 and OLMo-2 language models of 0.5B-4B parameters pre-trained at 20 or 140 tokens per parameter, AdamW weight decay above the default 0.1 during pre-training yields models that score better on the fine-tuning task after fine-tuning, even where it leaves a worse pre-training loss, so that pre-training loss does not rank pre-trained models by their performance after further training.'
version: 1
source:
- LIT-tmpkfcwr
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
bears_on:
- QUESTION-tmpwqepn
corroborates:
- CLAIM-675
promote_when: >-
  An independent group, pre-training models of its own across weight decay
  values with all else fixed, finds the fine-tuned score on held-out tasks
  rising with pre-training weight decay above 0.1, and finds at least one
  pair in which the higher-weight-decay model has the worse pre-training
  loss and the better fine-tuned score, beyond seed variation of pre-
  training.
summary: >-
  From the reading of [LIT-tmpkfcwr](../literature.d/LIT-tmpkfcwr.md) in [NOTE-tmps6j9j](../notes.d/NOTE-tmps6j9j.md). Han, Bordt, Zhang and
  Kakade (2026), arXiv 2602.11137, ICML 2026. They pre-train Llama-2 and
  OLMo-2 models (0.5B-4B, at 20 and 140 tokens per parameter) across AdamW
  weight decay values, then fine-tune on twelve tasks. Weight decay above
  the default 0.1 gives better fine-tuned performance even where it
  worsens pre-training loss (OLMo-2-1B at 140 tokens per parameter), so
  pre-training loss does not rank models by what they become. Plasticity
  is measured only as the fine-tuned score on the target task, and
  forgetting is not measured. It is here as a preventive training regime
  for overconsolidation ([CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)) and an arm of [CASE-tmphsr99](../cases.d/CASE-tmphsr99.md), and
  it is the clearest case for [CLAIM-675](../claims.d/CLAIM-675.md)'s point that present capability
  does not rank later capability. Read in its NOTE.
---
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-tmp8ljvp — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-tmp8wxgt: Han and colleagues show that, in Llama-2 and OLMo-2 language models of 0.5B-4B parameters pre-trained at 20 or 140 tokens per parameter, AdamW weight decay above the default 0.1 during pre-training yields models that score better on the fine-tuning task after fine-tuning, even where it leaves a worse pre-training loss, so that pre-training loss does not rank pre-trained models by their performance after further training.

## The account

Weight decay, usually tuned for the base model's validation loss, also shapes how much the model gains from later fine-tuning. Higher pre-training weight decay gives "greater performance gains downstream after finetuning" across model families, sizes, both training regimes and twelve tasks. The advantage holds over fine-tuning hyperparameters, so "pretraining performance is not perfectly predictive of downstream performance". Higher weight decay goes with more linearly separable representations, lower-rank query–key products and less overfitting of pre-training data. The authors say these mechanisms are correlational.

## What it does not show

- Not that weight decay prevents a decline of plasticity with training length. Length is not varied within a run.
- Not that pre-trained capability is kept. Forgetting during fine-tuning is not measured.
- Not that weight decay applied late, or at fine-tuning time alone, restores plasticity.
- Not beyond 4B parameters or 140 tokens per parameter. The authors expect low loss may win in heavily overtrained runs.
