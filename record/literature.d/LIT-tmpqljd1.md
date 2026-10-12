---
status: Deferred
status_note: 'filed 2026-10-12 from the owner''s papers-feed, not read. Registered for [QUESTION-tmp84iod](../questions.d/QUESTION-tmp84iod.md), where it reviews the models of why training reaches neural collapse and what that state does to generalization and transfer. No NOTE is filed, and it stays Deferred until it is read, not on merit.'
title: 'Neural Collapse: A Review on Modelling Principles and Generalization'
version: 1
history:
- version: 1
  date: '2026-10-12'
  note: >-
    Filed, not read. Found in the owner's papers-feed snapshot of 2026-10-11 by embedding
    similarity to QUESTION-tmp84iod and judged from the abstract. Citation checked against arXiv
    on 2026-10-12: Vignesh Kothapalli, arXiv:2206.04041 (published in Transactions on Machine
    Learning Research, 2023), 2022-06-08, which is the `published:` date. Not held in the
    Anthology of the SOTA: a grep of its record/ (clone at commit d8b5ba5) for the identifier
    and title found nothing.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-12'
published: '2022-06-08'
arxiv: '2206.04041'
first_author: 'Kothapalli'
keywords:
- 'neural collapse'
- 'terminal phase of training'
- 'simplex equiangular tight frame'
- 'generalization'
- 'transfer learning'
implementations: []
summary: >-
  Kothapalli (2022). The paper reviews neural collapse: once training error reaches zero,
  last-layer features of a class shrink toward their class mean, the class means form a simplex
  equiangular tight frame, and the classifier acts as a nearest-class-centre rule. It surveys the
  principles used to model how training reaches this state. It then reviews what the state implies
  for generalization and transfer learning, and lists open directions. Not read.
---

# LIT-tmpqljd1: Neural Collapse: A Review on Modelling Principles and Generalization

Vignesh Kothapalli (2022), *Transactions on Machine Learning Research (2023); arXiv:2206.04041*.

Filed for [QUESTION-tmp84iod](../questions.d/QUESTION-tmp84iod.md): it reviews both halves of the question at once: the models of why
training reaches the collapsed, simplex-shaped last layer, and what that structure does to
generalization and transfer. The record already holds the original observation as [LIT-618](LIT-618.md), so this
review adds the modelling and the consequences rather than the phenomenon.

*Seeded from the abstract, not a reading. A reading should check the claim above first.*
