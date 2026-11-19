---
status: Active
title: 'What Can Transformers Learn In-Context? A Case Study of Simple Function Classes'
version: 2
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Filed, not read. Identifier checked on the arXiv API on 2026-11-19, no
    email address sent: v1 submitted 2022-08-01. Not held: no hit for the
    identifier, the title or Garg in record/literature.d.
- version: 2
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader, quotations rechecked by the
    filer; in NOTE-tmpbf4ra, account THEORY-tmpxdk37. URL read:
    https://arxiv.org/pdf/2208.01066 (HTTP 200, 3.0 MB PDF, arXiv v3 of 11
    Aug 2023). Kind of copy: arXiv preprint (step 5, first place to look).
    Date: 2026-11-19. Nothing stopped the fetch.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-19'
published: '2022-08-01'
arxiv: '2208.01066'
first_author: 'Garg'
keywords: []
implementations: []
summary: >-
  Garg, Tsipras, Liang and Valiant (2022; arXiv 2208.01066, v3 Aug 2023)
  define in-context learning of a function class as a property of a fixed
  model and train small transformers from scratch to achieve it. On unseen
  20-dimensional linear functions the trained model matches least squares,
  and it stays close under noisy labels, subspace inputs and mismatched
  orthants. Trained on sparse linear functions, depth-4 trees or two-layer
  networks, it nears Lasso, beats greedy tree learning and XGBoost, and
  matches a gradient-trained network. It is fragile under input scaling
  and skewed covariance, and the authors leave open what this means for
  language models. Here because A56 cited it for in-context learning as a
  learned algorithm. It is the behavioural counterpart to the exact
  identities of [THEORY-169](../theory.d/THEORY-169.md) and a case of [CLAIM-118](../claims.d/CLAIM-118.md)'s split between a
  learned interpreter and a discarded per-sequence fit. Read in its NOTE.
  Read in [NOTE-tmpbf4ra](../notes.d/NOTE-tmpbf4ra.md); its account is [THEORY-tmpxdk37](../theory.d/THEORY-tmpxdk37.md).
---
<!-- inactive-ok-file: THEORY-tmpxdk37 — Proposed; cited in this filing of 2026-11-19 -->

# LIT-tmpx4h3s: What Can Transformers Learn In-Context? A Case Study of Simple Function Classes

Garg, Tsipras, Liang, Valiant (2022). arXiv 2208.01066.

## Standing in the record

Registered on 2026-11-19 from A56 of the exchange "Topological protection explained". A56 cited it for in-context learning as a learned algorithm, held in substance by [CLAIM-118](../claims.d/CLAIM-118.md) and [THEORY-169](../theory.d/THEORY-169.md). Not read.
