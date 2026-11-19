---
status: Active
title: 'Which Attention Heads Matter for In-Context Learning?'
version: 2
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Filed, not read. Identifier checked on the arXiv API on 2026-11-19, no
    email address sent: v1 submitted 2025-02-19. Not held: no hit for the
    identifier, the title or Yin in record/literature.d.
- version: 2
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader, quotations rechecked by the
    filer; in NOTE-tmpa9eoe, account THEORY-tmpqvj8f. URL read:
    https://arxiv.org/pdf/2502.14010 (HTTP 200, 1.4 MB PDF, arXiv v1 of 19
    Feb 2025). Kind of copy: arXiv preprint (step 5, first place to look).
    Date: 2026-11-19. Nothing stopped the fetch.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-19'
published: '2025-02-19'
arxiv: '2502.14010'
first_author: 'Yin'
keywords: []
implementations: []
summary: >-
  Yin and Steinhardt (2025; arXiv 2502.14010) compare induction heads and
  function-vector (FV) heads in twelve models (Pythia 70M–6.9B, GPT-2,
  Llama 2 7B). Ablating each type while sparing heads of the other shows
  that few-shot in-context accuracy depends mainly on FV heads,
  increasingly with scale. Induction heads matter for Olsson et al.'s
  token-loss difference, which the authors show measures something else.
  Across Pythia training, induction heads form near step 1,000 of 143,000.
  FV heads strengthen from about step 16,000 to the end, with few-shot
  accuracy, and many began as induction heads; that they are precursors is
  the authors' conjecture. Here because A56 used it for the in-context arm
  of CASE-tmphsr99. On Pythia it says in-context ability is still rising
  at late checkpoints, and it qualifies THEORY-990. Read in its NOTE. Read
  in NOTE-tmpa9eoe; its account is THEORY-tmpqvj8f.
---
<!-- inactive-ok-file: THEORY-990 THEORY-tmpqvj8f — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CASE-tmphsr99 — Proposed; cited in this filing of 2026-11-19 -->

# LIT-tmpbi4vz: Which Attention Heads Matter for In-Context Learning?

Yin, Steinhardt (2025). arXiv 2502.14010.

## Standing in the record

Registered on 2026-11-19 from A56 of the exchange "Topological protection explained". A56 used it for an in-context arm of [CASE-tmphsr99](../cases.d/CASE-tmphsr99.md). Not read.
