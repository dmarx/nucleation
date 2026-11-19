---
status: Active
title: 'Test-Time Training with Self-Supervision for Generalization under Distribution Shifts'
version: 2
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Filed, not read. Identifier checked on the arXiv API on 2026-11-19, no
    email address sent: v1 submitted 2019-09-29. Not held: no hit for the
    identifier, the title or Sun in record/literature.d.
- version: 2
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader, quotations rechecked by the
    filer; in NOTE-tmpt5pbx, account THEORY-tmp3hfjg. URL:
    https://arxiv.org/pdf/1909.13231 (HTTP 200, 2026-11-19; resolved to
    arXiv v3, 1 Jul 2020, 20 pages).
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-19'
published: '2019-09-29'
arxiv: '1909.13231'
first_author: 'Sun'
keywords: []
implementations: []
summary: >-
  Sun, Wang, Liu, Miller, Efros and Hardt (2020), ICML 2020, arXiv
  1909.13231. The paper that named test-time training: before predicting,
  a jointly trained network fine-tunes its shared features on a self-
  supervised task (rotation prediction) built from the single unlabeled
  test image, then discards the update or, in the online version, keeps it
  for the next image. It improves classification under corruption, video
  and CIFAR-10.1 shifts without hurting the original test set, and the
  gain tracks the alignment of the two tasks' gradients (proved for convex
  losses). Here because the owner raised test-time training at U26: its
  discarded and kept updates are the two sides of CLAIM-118, and its
  appendix prices the work moved to test time (QUESTION-095). Read in its
  NOTE. Read in NOTE-tmpt5pbx; its account is THEORY-tmp3hfjg.
---
<!-- inactive-ok-file: THEORY-tmp3hfjg — Proposed; cited in this filing of 2026-11-19 -->

# LIT-tmpklgue: Test-Time Training with Self-Supervision for Generalization under Distribution Shifts

Sun, Wang, Liu, Miller et al. (2019). arXiv 1909.13231.

## Standing in the record

Registered on 2026-11-19 from A58 of the exchange "Topological protection explained". The owner raised test-time training at U26; the record holds later TTT work ([LIT-801](LIT-801.md), [LIT-796](LIT-796.md)) but not this. Not read.
