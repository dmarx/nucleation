---
status: Deferred
status_note: >-
  filed 2026-10-26, not read. Registered from the owner's exchange
  "Experimental Infrastructure Review", shared at
  https://chatgpt.com/share/6adfa6e4-a0b0-83e9-b3a0-0b53e6000277 and read
  from the saved copy the owner uploaded, which holds turns T18–T24 only. No
  NOTE is filed.
title: 'In-context Learning and Induction Heads'
version: 1
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
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-26'
published: '2022-09-24'
arxiv: '2209.11895'
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
  of most in-context learning in transformers: strong and causal for small
  attention-only models, correlational for larger models with MLPs
  (abstract).
---

# LIT-tmpe7b5o: In-context Learning and Induction Heads

Olsson, C., Elhage, N., Nanda, N., Joseph, N., et al. (2022). In-context
learning and induction heads. arXiv:2209.11895.

Not read. The summary is drawn from the abstract, and a reading should
check it first.

## Why this is here

Cited at T24 for the setting where the reply would first test the record's
perspective framework on training dynamics: which partial capacities exist
before the induction circuit forms. The record held it only as a pointer in
[NOTE-283](../notes.d/NOTE-283.md) and in the reading of [LIT-153](LIT-153.md) ([NOTE-106](../notes.d/NOTE-106.md)). It is the empirical
anchor of [QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md), and bears on [QUESTION-039](../questions.d/QUESTION-039.md) (what sets the order and
moment at which a network acquires a structure).
