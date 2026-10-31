---
status: Deferred
status_note: >-
  filed 2026-10-31 from A16 of the exchange "Analyze nucleation concepts" (2026-10-30 to 31); not read.
title: 'Overcoming Scaling Limits in On-Policy Self-Distillation for LLM Reasoning'
version: 1
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A16 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against arXiv (v1
    2026-09-29). A16 said it treats the forward-KL projection
    explicitly; that could not be confirmed from the abstract. The
    summary follows the abstract and the exchange's description; a
    reading should check it first.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-31'
published: '2026-09-29'
arxiv: '2609.37915'
first_author: 'Hossain'
keywords:
- 'self-distillation'
- 'on-policy distillation'
- 'imitation gap'
- 'LLM reasoning'
implementations: []
summary: >-
  Hossain, Kousar & Tourni (2026). On-policy self-distillation for LLM
  reasoning, where the teacher can use information unavailable to the
  student, leaving an imitation gap that limits how far the method
  scales; proposes ways around it.
---

# LIT-tmpbnm77: Overcoming Scaling Limits in On-Policy Self-Distillation for LLM Reasoning

Hossain, M. I., Kousar, H., & Tourni, I. C. (2026). Overcoming scaling limits in on-policy self-distillation for LLM reasoning. arXiv:2609.37915.

Filed, not read.

## Why this is here

A16 used it for the "privileged teacher" case of self-distillation: what the teacher knows and the student cannot see is averaged away, which is the limit [QUESTION-tmp4b001](../questions.d/QUESTION-tmp4b001.md) starts from.
