---
status: Active
status_note: >-
  read 2026-10-26 (NOTE-tmpx60d8) in full, from the Transformer Circuits
  article; worth reading for the exact decomposition of an attention-only
  transformer into end-to-end paths and of each head into separable QK and
  OV circuits (THEORY-tmphm85g, re-derived and checked by the record), for
  the three kinds of head composition, and as the paper in which induction
  heads are found, by K-composition with a previous-token head, in a
  two-layer attention-only model (THEORY-tmpb4xka). Read it knowing that
  the models are toys without MLPs, that the framework ignores layer norm
  and biases, that the composition diagram was corrected after publication,
  and that the interactive figures carry much of the evidence.
title: 'A Mathematical Framework for Transformer Circuits'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read, at the owner's request of 2026-10-26: asked "how's
    the record on neural circuit theory?", the answer found the record held
    almost none of the core circuits literature, and the owner said "go
    ahead and register and read those". Checked on 2026-10-26 against the
    article's own page: Nelson Elhage, Neel Nanda, Catherine Olsson, Tom
    Henighan, Nicholas Joseph, Ben Mann and 19 further authors, with Chris
    Olah for correspondence (Anthropic), Transformer Circuits Thread,
    "Published Dec 22, 2021", which is `published:` (ADR-002). It has no
    arXiv record and no DOI, so the article's URL is the source. The
    summary follows the article's Summary of Results.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmpx60d8) from the article,
    https://transformer-circuits.pub/2021/framework/index.html, fetched
    2026-10-26, its text extracted from the HTML; the interactive figures
    and diagrams were read from their captions and the surrounding text
    only. Status Deferred → Active. Two accounts filed, both Active:
    THEORY-tmphm85g (the path expansion, checked numerically by the
    record) and THEORY-tmpb4xka (the two-layer model). The summary is
    checked against the reading and kept, with the post-publication
    correction added.
tags:
- representation-learning
- compositionality
- anthology-candidate
date: '2026-10-26'
published: '2021-12-22'
url: 'https://transformer-circuits.pub/2021/framework/index.html'
first_author: 'Elhage'
keywords:
- 'transformer circuits'
- 'residual stream'
- 'QK circuit'
- 'OV circuit'
- 'path expansion'
- 'attention head composition'
- 'induction heads'
- 'mechanistic interpretability'
implementations: []
summary: >-
  Elhage et al. (2021), Transformer Circuits Thread. Rewrites a transformer
  without changing it: heads act independently and add into a linear
  residual stream, each head is a low-rank QK matrix that sets where to
  attend and a low-rank OV matrix that sets what is moved, and with
  attention patterns frozen an attention-only model is a sum of end-to-end
  path terms. Zero-layer models are bigram tables, one-layer attention-only
  models bigram and skip-trigram tables read off the weights, and two-layer
  models use K-composition with a previous-token head to form induction
  heads, [a][b] … [a] → [b]. A correction of the composition diagram adds
  more composition than first reported. Models with MLPs are left open.
---
<!-- inactive-ok-file: THEORY-802 THEORY-tmp1dufu — Proposed; the basis-relative account and the head-development account this bears on, cited as open -->

# LIT-tmp9dono: A Mathematical Framework for Transformer Circuits

Elhage, N., Nanda, N., Olsson, C., Henighan, T., Joseph, N., Mann, B., et
al. (2021). A mathematical framework for transformer circuits.
*Transformer Circuits Thread*, 22 December 2021.
https://transformer-circuits.pub/2021/framework/index.html

Read in full on 2026-10-26 (NOTE-tmpx60d8). Two accounts were drawn from
it: THEORY-tmphm85g and THEORY-tmpb4xka.

## Why this is here

Registered and read at the owner's request of 2026-10-26, after an answer to
"how's the record on neural circuit theory?" found that the record held
almost none of the core circuits literature. The record's transformer
circuits line rested on this paper without holding it. The induction-head
paper (LIT-tmpe7b5o) takes its induction head and its K-composition
mechanism from here, and THEORY-tmp8cat0 and the readings of Wang et al.'s
refined learning coefficients (THEORY-tmp9uzkw, THEORY-tmp1dufu) and of
Musat et al. (THEORY-tmpdxhxm, THEORY-tmpvqsx2) use its two-layer
attention-only setting and its vocabulary of QK and OV circuits. Its
observation that the residual stream has no privileged basis is the setting
of THEORY-802 and THEORY-018.
