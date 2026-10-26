---
status: Active
status_note: >-
  read 2026-10-26 (NOTE-tmpabelf) in full, from the arXiv print of the
  Transformer Circuits article; worth reading as the first mechanistic
  account of a transition in training, for the in-context learning score,
  and for the way it grades its own evidence by model class. Read it
  knowing that the case is causal only for small attention-only models
  (THEORY-tmp8cat0), that the large-model thesis is correlational and by
  analogy (THEORY-tmpkd3fq), that every model was trained once on the same
  data order, and that its dates for the window disagree between sections.
title: 'In-context Learning and Induction Heads'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T24 the reply says "Earlier work found that
    induction heads emerge around a sharp improvement in in-context learning
    in the studied transformer models. The evidence is stronger causally in
    small attention-only models than in larger models with MLPs", with no
    citation; that is this paper's abstract. Checked on 2026-10-26 against
    the arXiv record: Catherine Olsson, Nelson Elhage, Neel Nanda, Nicholas
    Joseph and 22 further authors (Anthropic), arXiv 2209.11895, v1
    submitted 24 September 2022, which is `published:`. The summary follows
    the arXiv abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmpabelf) from the arXiv PDF of 2209.11895, a
    61-page print of the Transformer Circuits article. Status Deferred →
    Active. Two accounts filed: THEORY-tmp8cat0 (Active) and
    THEORY-tmpkd3fq (Proposed). `published:` corrected from the arXiv v1
    date to 2022-03-08, the article's own "PUBLISHED Mar 8, 2022", its
    first appearance (ADR-002), as LIT-323 does for the same venue; the
    arXiv record is a later deposit. The article's URL is added. The
    summary is checked against the reading and kept, with "in large
    transformer models" made explicit.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-26'
published: '2022-03-08'
arxiv: '2209.11895'
url: 'https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html'
first_author: 'Olsson'
keywords:
- 'induction heads'
- 'in-context learning'
- 'phase change'
- 'transformer circuits'
- 'mechanistic interpretability'
implementations: []
summary: >-
  Olsson et al. (2022), arXiv:2209.11895. Induction heads, attention heads
  that complete [A][B] … [A] → [B], develop at precisely the point of a
  sudden sharp increase in in-context learning, visible as a bump in the
  training loss. Six lines of evidence argue that they may be the mechanism
  of most in-context learning in large transformers: strong and causal for small
  attention-only models, correlational for larger models with MLPs
  (abstract).
---
<!-- inactive-ok-file: THEORY-tmpkd3fq — Proposed; the wider thesis filed from this reading, cited as open -->

# LIT-tmpe7b5o: In-context Learning and Induction Heads

Olsson, C., Elhage, N., Nanda, N., Joseph, N., et al. (2022). In-context
learning and induction heads. *Transformer Circuits Thread*, 8 March
2022. arXiv:2209.11895.

Read in full on 2026-10-26 (NOTE-tmpabelf). The summary is checked
against the reading.

## Why this is here

Cited at T24 for the setting where the reply would first test the record's
perspective framework on training dynamics: which partial capacities exist
before the induction circuit forms. The record held it only as a pointer in
[NOTE-283](../notes.d/NOTE-283.md) and in the reading of [LIT-153](LIT-153.md) ([NOTE-106](../notes.d/NOTE-106.md)). It is the empirical
anchor of [QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md), and bears on [QUESTION-039](../questions.d/QUESTION-039.md) (what sets the order and
moment at which a network acquires a structure).
