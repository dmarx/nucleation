---
status: Active
title: 'On First-Order Meta-Learning Algorithms'
version: 2
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Filed, not read. Identifier checked on the arXiv API on 2026-11-19, no
    email address sent: v1 submitted 2018-03-08. Not held: no hit for the
    identifier, the title or Nichol in record/literature.d.
- version: 2
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader, quotations rechecked by the
    filer; in NOTE-tmparjas, account THEORY-tmpbzf9h. URL read:
    https://arxiv.org/pdf/1803.02999 (served arXiv:1803.02999v3, 22 Oct
    2018; HTTP 200, application/pdf).
tags:
- learning-theory
- anthology-candidate
date: '2026-11-19'
published: '2018-03-08'
arxiv: '1803.02999'
first_author: 'Nichol'
keywords: []
implementations: []
summary: >-
  Nichol, Achiam and Schulman (2018), OpenAI, arXiv 1803.02999. Reptile
  meta-learns an initialization by repeatedly training on a sampled task
  and moving the initialization toward the result; it matches MAML on few-
  shot Omniglot and Mini-ImageNet with first-order gradients only, and a
  Taylor expansion shows its update, like MAML's, is joint training plus a
  term rewarding generalization between mini-batches of one task, a term
  that grows with step size and inner steps and is absent at one step. The
  authors suggest plain SGD does part of this already and that joint
  training plus fine-tuning stays a strong baseline; their RL results were
  negative. Here because A54 proposed it as the meta-trained arm of CASE-
  tmphsr99: the reading supports it as a cheap arm, with joint training on
  the same tasks as its control and the inner budget k fixed. Read in its
  NOTE. Read in NOTE-tmparjas; its account is THEORY-tmpbzf9h.
---
<!-- inactive-ok-file: THEORY-tmpbzf9h — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CASE-tmphsr99 — Proposed; cited in this filing of 2026-11-19 -->

# LIT-tmp2gj7u: On First-Order Meta-Learning Algorithms

Nichol, Achiam, Schulman (2018). arXiv 1803.02999.

## Standing in the record

Registered on 2026-11-19 from A54 of the exchange "Topological protection explained". A54 proposed it as a meta-trained arm of [CASE-tmphsr99](../cases.d/CASE-tmphsr99.md). Not read.
