---
status: Active
status_note: 'read in full 2026-09-30 ([NOTE-tmpq5vw7](../notes.d/NOTE-tmpq5vw7.md)); worth reading as a clean, intervention-backed decomposition of a loss plateau into circuit formation followed by knowledge storage, in a setting where knowledge is countable; its curriculum and fine-tuning results are single-seed and synthetic, and it measures no information quantity, so it bears on phases of training but not on the IB account.'
title: 'How do language models learn facts? Dynamics, curricula and hallucinations'
version: 2
history:
- version: 2
  date: '2026-09-30'
  note: >-
    Read in full (Full text of arXiv 2503.21676 v2 (24 Jul 2025; the arXiv
    comment says "Accepted at the 2nd Conference on Language Modeling
    (2025)"), 41 pp. Read everything: §§1–5, Limitations, references, and
    Appendices A–G, including all hyperparameter tables (G.1–G.5) and all
    figure captions. Text was extracted with PyMuPDF. The figures are images
    and were read from their captions, axis labels and the text, so numbers
    that are only visible in the plots are not quoted. v1 (27 Mar 2025) was
    not read. `published:` is the v1 date. The paper is already held in the
    Anthology of the SOTA as ANTH-LIT-450 (Active, with a NOTE reading it).
    Dual holding (nucleation ADR-013): nucleation holds it for the
    phases-of-training question behind THEORY-tmpd8w6r and beside LIT-345,
    as a mechanistically measured three-phase trajectory in a language
    model; the anthology holds it for data-schedule and fine-tuning
    practice.); the first NOTE on it, since it was seeded from the abstract
    alone. Status set from the reading: Active.
tags:
- learning-theory
- representation-learning
date: '2026-09-30'
published: '2025-03-27'
arxiv: '2503.21676'
first_author: 'Zucchet'
keywords:
- 'training phases'
implementations: []
summary: >-
  Zucchet et al. (2025), arXiv:2503.21676. 'An 8-layer, 44M-parameter
  decoder-only transformer trained with AdamW on synthetic biographies
  (64k individuals by default) learns factual recall in three phases. It
  first fits the marginal attribute-value distribution, then sits on a
  plateau exactly at the no-knowledge baseline, then acquires
  individual-specific associations. Plateau end grows with population as
  0.43·N^0.81 (R² = 0.998, N = 4k–256k, 5 seeds). Attention patching from
  post-plateau checkpoints removes the plateau, and attention from the
  recall position to name tokens rises through it, so the plateau is when
  the attention extraction circuit forms. Nothing in the three phases is a
  compression of input information: the last phase adds
  individual-specific information.'
---

# LIT-tmpb4i34: How do language models learn facts? Dynamics, curricula and hallucinations

Zucchet et al. (2025), *Conference on Language Modeling (COLM 2025), per the arXiv v2 comment "Accepted at the 2nd Conference on Language Modeling (2025)"; arXiv preprint 2503.21676* — arXiv:2503.21676

## Standing in the record

Filed on 2026-09-30 at the owner's request, as evidence on phases of training: whether they corroborate the
information-bottleneck account of a fitting then a compression phase ([LIT-324](LIT-324.md)), and what phase structure they show.
`published:` is the first appearance ([ADR-002](../decisions.d/ADR-002.md)).

Also held in the Anthology of the SOTA as [ANTH-LIT-450](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-450.md) ([ADR-013](../decisions.d/ADR-013.md)): the anthology reads it for ML practice, this record for what it shows about phases of training and the information-bottleneck account.

It was filed `Deferred`, unread. [NOTE-tmpq5vw7](../notes.d/NOTE-tmpq5vw7.md) is the close reading of 2026-09-30, and it placed the work: **Active** — worth reading as a clean, intervention-backed decomposition of a loss plateau into circuit formation followed by knowledge storage, in a setting where knowledge is countable; its curriculum and fine-tuning results are single-seed and synthetic, and it measures no information quantity, so it bears on phases of training but not on the IB account.
