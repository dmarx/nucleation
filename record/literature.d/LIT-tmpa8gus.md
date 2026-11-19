---
status: Active
title: 'Agentic-TTT: Training test-time policy for test-time training'
version: 2
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Filed, not read. Identifier checked on the arXiv API on 2026-11-19, no
    email address sent: v1 submitted 2026-10-08. Not held: no hit for the
    identifier, the title or Lu in record/literature.d.
- version: 2
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader, quotations rechecked by the
    filer; in NOTE-tmp0i0a5, account THEORY-tmpddlli. URL:
    https://arxiv.org/pdf/2610.12002 (HTTP 200, 2026-11-19; arXiv v1, 8 Oct
    2026, 26 pages).
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-19'
published: '2026-10-08'
arxiv: '2610.12002'
first_author: 'Lu'
keywords: []
implementations: []
summary: >-
  Lu and Kankanhalli (2026), arXiv 2610.12002. Five test-time-training
  methods become tools that produce reusable LoRA skills over a frozen
  backbone, and a policy trained by distillation and GRPO decides per
  query whether to answer directly, reuse a skill or build one, on utility
  gain minus a compute penalty. On a benchmark deliberately enriched for
  queries where adaptation helps, it raises Qwen2.5-7B's verified utility
  from 0.256 to 0.510, cuts adaptation compute by about 30% under a
  moderate penalty without losing utility, and amortizes skill
  construction through reuse (61 of 100 reuses help, 1 harms). Here
  because A58 cited it for learning when to update: its rule, build when
  gain amortized over expected reuse covers the compute, is [QUESTION-095](../questions.d/QUESTION-095.md)'s
  trade and [CLAIM-303](../claims.d/CLAIM-303.md)'s criterion for parameter skills. Read in its NOTE.
  Read in [NOTE-tmp0i0a5](../notes.d/NOTE-tmp0i0a5.md); its account is [THEORY-tmpddlli](../theory.d/THEORY-tmpddlli.md).
---
<!-- inactive-ok-file: THEORY-tmpddlli — Proposed; cited in this filing of 2026-11-19 -->

# LIT-tmpa8gus: Agentic-TTT: Training test-time policy for test-time training

Lu, Kankanhalli (2026). arXiv 2610.12002.

## Standing in the record

Registered on 2026-11-19 from A58 of the exchange "Topological protection explained". A58 cited it for learning when to update, which bears on [QUESTION-095](../questions.d/QUESTION-095.md). Not read.
