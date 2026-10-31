---
status: Deferred
status_note: >-
  filed 2026-10-31 from U15 (the owner's link), A15 and A16 of the exchange "Analyze nucleation concepts" (2026-10-30 to 31); not read.
title: 'Multi-Token Prediction Done Right'
version: 1
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from U15 (the owner's link), A15 and A16 of the
    exchange "Analyze nucleation concepts" (2026-10-30 to 31).
    Citation checked against arXiv (v1 2026-10-28, single author).
    Code at github.com/JaydenTeoh/Soft-MTP. The summary follows the
    abstract and the readers' check of the HTML text; the paper was
    not read for the record. The summary follows the abstract and
    the exchange's description; a reading should check it first.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-31'
published: '2026-10-28'
arxiv: '2610.38331'
first_author: 'Teoh'
keywords:
- 'multi-token prediction'
- 'self-distillation'
- 'next-token prediction'
- 'Soft-MTP'
implementations: []
summary: >-
  Teoh (2026). Decomposes the multi-token-prediction cross-entropy
  gradient exactly into a KL self-distillation term toward the model's
  own next-token predictions and a residual, reports that the residual
  carries most of the gradient reaching the shared trunk with low
  signal-to-noise, and proposes Soft-MTP. Experiments at 167M–1.2B
  parameters.
---

# LIT-tmpu9af8: Multi-Token Prediction Done Right

Teoh, J. (2026). Multi-token prediction done right. arXiv:2610.38331.

Filed, not read.

## Why this is here

The owner linked it at U15: "maybe framing this recursive production as self-distillation could be helpful". A15 and A16 built on its decomposition the reading of self-distillation as conditional projection: the student reproduces the teacher averaged over what the student cannot see. That is [QUESTION-tmp4b001](../questions.d/QUESTION-tmp4b001.md)'s starting point. A16's detail about the shared head's routing could not be checked from the abstract.
