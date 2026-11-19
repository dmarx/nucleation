---
status: Active
title: 'VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning'
version: 2
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Filed, not read. Identifier checked on the arXiv API on 2026-11-19, no
    email address sent: v1 submitted 2021-05-11. Not held: no hit for the
    identifier, the title or Bardes in record/literature.d.
- version: 2
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader, quotations rechecked by the
    filer; in NOTE-tmpprl89, account THEORY-tmp78qwh. URL read:
    https://arxiv.org/pdf/2105.04906 (HTTP 200, 0.87 MB PDF; header
    "arXiv:2105.04906v3 [cs.CV] 28 Jan 2022"; running head "Published as a
    conference paper at ICLR 2022").
tags:
- representation-learning
- anthology-candidate
date: '2026-11-19'
published: '2021-05-11'
arxiv: '2105.04906'
first_author: 'Bardes'
keywords: []
implementations: []
summary: >-
  Bardes, Ponce, LeCun (2021), ICLR 2022, arXiv 2105.04906. The loss has
  three terms on the embeddings: invariance (mean squared distance between
  two views), a hinge holding each variable's batch standard deviation
  above 1, and a penalty on off-diagonal covariances, the last two applied
  to each branch separately. In the ablation the invariance term alone
  collapses everything to one vector, covariance cannot stop it, and the
  variance term does (57.5%, and 68.6% with all three, at 100 epochs;
  73.2% at 1000). The hinge must be on the standard deviation: on the
  variance, its gradient vanishes and the embeddings collapse. That bears
  on LIT-228's Laplacian-eigenmaps reading, which assumes a squared
  variance term. Here because A27 used it as a non-collapse mechanism
  (CLAIM-481's note of 2026-11-19). Read in its NOTE. Read in NOTE-
  tmpprl89; its account is THEORY-tmp78qwh.
---
<!-- inactive-ok-file: THEORY-tmp78qwh — Proposed; cited in this filing of 2026-11-19 -->

# LIT-tmpf5qpo: VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning

Bardes, Ponce, LeCun (2021). arXiv 2105.04906.

## Standing in the record

Registered on 2026-11-19 from A27 of the exchange "Topological protection explained". A27 used it as a non-collapse mechanism; [LIT-228](LIT-228.md) reads it as Laplacian eigenmaps but there was no entry for the work itself. Not read.
