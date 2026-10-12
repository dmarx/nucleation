---
status: Deferred
status_note: 'filed 2026-10-12 from the owner''s papers-feed, not read. Registered for [QUESTION-tmp0dy29](../questions.d/QUESTION-tmp0dy29.md), where it offers one mechanism for the order in which a network acquires structure. No NOTE is filed, and it stays Deferred until it is read, not on merit.'
title: 'Neural Networks Learn Statistics of Increasing Complexity'
version: 1
history:
- version: 1
  date: '2026-10-12'
  note: >-
    Filed, not read. Found in the owner's papers-feed snapshot of 2026-10-11 by embedding similarity to
    QUESTION-tmp0dy29 and judged from the abstract. Citation checked against arXiv on 2026-10-12: Nora
    Belrose, Quintin Pope, Lucia Quirke et al., arXiv:2402.04362, 2024-02-06, which is the `published:`
    date. Not held in the Anthology of the SOTA: a grep of its record/ (clone at commit d8b5ba5) for the
    identifier and title found nothing.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-10-12'
published: '2024-02-06'
arxiv: '2402.04362'
first_author: 'Belrose'
keywords:
- 'distributional simplicity bias'
- 'training dynamics'
- 'low-order moments'
- 'n-gram statistics'
- 'maximum-entropy distributions'
implementations: []
summary: >-
  Belrose et al. (2024). The paper argues that networks learn the low-order moments of the data first
  and higher-order correlations later. It shows that early in training networks do well on maximum-
  entropy data that matches only the low-order statistics of the training set, and lose this ability
  later. It proves that token n-gram frequencies are equivalent to moments of embedding vectors, and
  reports the same bias in language models. Not read.
---

# LIT-tmp9mkww: Neural Networks Learn Statistics of Increasing Complexity

Nora Belrose, Quintin Pope, Lucia Quirke, Alex Mallen and Xiaoli Fern (2024), *arXiv:2402.04362*.

Filed for [QUESTION-tmp0dy29](../questions.d/QUESTION-tmp0dy29.md): a mechanism for the order of acquisition. Low-order moments are learned before higher-order ones, and n-gram frequencies are shown to be moments of the embeddings, so the claim reaches discrete tokens.

*Seeded from the abstract, not a reading. A reading should check the claim above first.*
