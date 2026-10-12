---
status: Deferred
status_note: 'filed 2026-10-12 from the owner''s papers-feed, not read. Registered for [QUESTION-030](../questions.d/QUESTION-030.md), where an intervention reproduces a feature''s effect through a dormant pathway, so interventional success does not identify the constituting relation. No NOTE is filed, and it stays Deferred until it is read, not on merit.'
title: 'Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching'
version: 1
history:
- version: 1
  date: '2026-10-12'
  note: >-
    Filed, not read. Found in the owner's papers-feed snapshot of 2026-10-11 by embedding similarity to QUESTION-030
    and judged from the abstract. Citation checked against arXiv on 2026-10-12: Aleksandar Makelov, Georg Lange, Neel
    Nanda, arXiv:2311.17030 (NeurIPS 2023 Workshop on Attributing Model Behavior at Scale, per the arXiv comment),
    submitted 2023-11-28, which is the `published:` date. Not held in the Anthology of the SOTA: a grep of its record/
    (clone at commit d8b5ba5) for the identifier and title found nothing.
tags:
- causality
- representation-learning
- anthology-candidate
date: '2026-10-12'
published: '2023-11-28'
arxiv: '2311.17030'
first_author: 'Makelov'
keywords:
- 'activation patching'
- 'subspace interventions'
- 'mechanistic interpretability'
- 'interpretability illusion'
- 'fact editing'
implementations: []
summary: >-
  Makelov et al. (2023). The paper shows that a subspace intervention can make a model behave as if a feature's value
  changed while the effect actually runs through a dormant parallel pathway that is causally disconnected from the
  outputs. It demonstrates this in a distilled example, on indirect object identification and on factual recall, and
  links it to rank-1 fact editing. It also shows what a successful case looks like where prior circuit analysis is
  available. Not read.
---

# LIT-tmpgygfq: Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching

Aleksandar Makelov, Georg Lange and Neel Nanda (2023), *arXiv:2311.17030* (NeurIPS 2023 Workshop on Attributing Model Behavior at Scale).

Filed for [QUESTION-030](../questions.d/QUESTION-030.md): a concrete case where an intervention reproduces a feature's effect through a pathway that does not carry it. Interventional success then does not identify the relation that constitutes the behaviour.

*Seeded from the abstract, not a reading. A reading should check the claim above first.*
