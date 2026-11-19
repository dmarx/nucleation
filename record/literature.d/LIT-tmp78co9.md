---
status: Active
title: 'End-to-End Test-Time Training for Long Context'
version: 2
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Filed, not read. Identifier checked on the arXiv API on 2026-11-19, no
    email address sent: v1 submitted 2025-12-29. Not held: no hit for the
    identifier, the title or Tandon in record/literature.d.
- version: 2
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader, quotations rechecked by the
    filer; in NOTE-tmp2v2zr, account THEORY-tmpv904w. URL:
    https://arxiv.org/pdf/2512.23675 (HTTP 200, 2026-11-19; resolved to
    arXiv v2, 31 Dec 2025, 29 pages).
tags:
- representation-learning
- anthology-candidate
date: '2026-11-19'
published: '2025-12-29'
arxiv: '2512.23675'
first_author: 'Tandon'
keywords: []
implementations: []
summary: >-
  Tandon, Dalal, Li, Koceja, Rød, ... and Sun (2025), arXiv 2512.23675. A
  sliding-window Transformer keeps learning at test time by next-token
  prediction on its context, compressing it into the MLP weights of its
  last quarter of blocks, from an initialization meta-learned for the loss
  after those updates. At 3B parameters it keeps full attention's scaling
  of loss with context length to 128K at constant per-token latency (2.7×
  faster at 128K), but loses to full attention on needle-in-a-haystack
  recall, and training is 3.4× slower at 8K. Here because A58 cited it for
  the owner's U26 case: its per-sequence weights and meta-learned
  initialization separate signal from interpreter (CLAIM-118), it prices
  work moved from inference into training (QUESTION-095), and its finding
  that test-time updates on an ordinarily trained model add little bears
  on the TTT arm of CASE-tmphsr99. Read in its NOTE. Read in NOTE-
  tmp2v2zr; its account is THEORY-tmpv904w.
---
<!-- inactive-ok-file: CASE-tmphsr99 THEORY-tmpv904w — Proposed; cited in this filing of 2026-11-19 -->

# LIT-tmp78co9: End-to-End Test-Time Training for Long Context

Tandon, Dalal, Li, Koceja et al. (2025). arXiv 2512.23675.

## Standing in the record

Registered on 2026-11-19 from A58 of the exchange "Topological protection explained". A58 cited it for the owner's U26 case. Not read.
