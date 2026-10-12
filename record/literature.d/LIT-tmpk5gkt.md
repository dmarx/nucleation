---
status: Deferred
status_note: 'filed 2026-10-12 from the owner''s papers-feed, not read. Registered for [QUESTION-tmp84iod](../questions.d/QUESTION-tmp84iod.md), where it explains why training reaches the collapsed geometry through dynamics on the central path. No NOTE is filed, and it stays Deferred until it is read, not on merit.'
title: 'Neural Collapse Under MSE Loss: Proximity to and Dynamics on the Central Path'
version: 1
history:
- version: 1
  date: '2026-10-12'
  note: >-
    Filed, not read. Found in the owner's papers-feed snapshot of 2026-10-11 by embedding
    similarity to QUESTION-tmp84iod and judged from the abstract. Citation checked against arXiv
    on 2026-10-12: X. Y. Han, Vardan Papyan, David L. Donoho, arXiv:2106.02073 (ICLR 2022),
    2021-06-03, which is the `published:` date. Not held in the Anthology of the SOTA: a grep of
    its record/ (clone at commit d8b5ba5) for the identifier and title found nothing.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-12'
published: '2021-06-03'
arxiv: '2106.02073'
first_author: 'Han'
keywords:
- 'neural collapse'
- 'mean squared error loss'
- 'central path'
- 'gradient flow'
- 'simplex equiangular tight frame'
implementations: []
summary: >-
  Han et al. (2021). The paper shows that neural collapse also occurs under mean squared error
  loss, on three networks and five standard datasets. It decomposes the MSE loss into a term where
  the last-layer classifier is exactly least-squares and a term for deviation from it, and finds
  the deviation negligible during training. This motivates the "central path", along which the
  classifier stays MSE-optimal for the current features. It studies renormalized gradient flow
  along this path to explain how collapse arises. Not read.
---

# LIT-tmpk5gkt: Neural Collapse Under MSE Loss: Proximity to and Dynamics on the Central Path

X. Y. Han, Vardan Papyan, David L. Donoho (2021), *ICLR 2022; arXiv:2106.02073*.

Filed for [QUESTION-tmp84iod](../questions.d/QUESTION-tmp84iod.md): it gives a mechanism for why training reaches the collapsed geometry,
through dynamics on the central path. The record holds the phenomenon as [LIT-618](LIT-618.md) but not this
mechanism.

*Seeded from the abstract, not a reading. A reading should check the claim above first.*
