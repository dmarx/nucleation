---
status: Active
title: 'Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling'
version: 2
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Filed, not read. Identifier checked on the arXiv API on 2026-11-19, no
    email address sent: v1 submitted 2023-04-03. Not held: no hit for the
    identifier, the title or Biderman in record/literature.d.
- version: 2
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader, quotations rechecked by the
    filer; in NOTE-tmpzf8fo, account THEORY-tmp7himr. URL:
    https://arxiv.org/pdf/2304.01373 (HTTP 200, 2026-11-19; resolved to
    arXiv v2, 31 May 2023, 34 pages).
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-19'
published: '2023-04-03'
arxiv: '2304.01373'
first_author: 'Biderman'
keywords: []
implementations: []
summary: >-
  Biderman, Schoelkopf, Anthony, Bradley, O'Brien and others (2023), ICML
  2023, arXiv 2304.01373. Pythia is eight decoder-only language models,
  70M to 12B parameters, each trained once on the Pile and once on a
  deduplicated Pile (about 1.5 epochs) in one fixed data order, with 154
  public checkpoints per model (step 0, ten log-spaced early steps, every
  1,000 steps to 143,000) and tools to reconstruct the batches seen up to
  each; one run per size, cosine learning-rate decay to a tenth of peak.
  Its case studies find training order has little effect on memorization
  and a term-frequency effect on few-shot accuracy that appears only late
  and only at 2.8B and above. Here because it is the testbed of CASE-
  tmphsr99, whose named models (70M- and 160M-deduped) and checkpoints
  exist as described, and because many THEORY entries use its models
  without an entry for the suite. Read in its NOTE. Read in [NOTE-tmpzf8fo](../notes.d/NOTE-tmpzf8fo.md);
  its account is [THEORY-tmp7himr](../theory.d/THEORY-tmp7himr.md).
---
<!-- inactive-ok-file: THEORY-tmp7himr — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CASE-tmphsr99 — Proposed; cited in this filing of 2026-11-19 -->

# LIT-tmpyyhs0: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling

Biderman, Schoelkopf, Anthony, Bradley et al. (2023). arXiv 2304.01373.

## Standing in the record

Registered on 2026-11-19 from A52 of the exchange "Topological protection explained". It is the testbed of the owner-requested study, [CASE-tmphsr99](../cases.d/CASE-tmphsr99.md); many THEORY entries use its models without an entry for the suite. Not read.
