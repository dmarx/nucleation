---
status: Deferred
status_note: >-
  filed 2026-10-15, not yet read. Registered at the owner's request (curation entry
  of 2026-10-15). A reading is under way.
title: 'Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling
  Laws'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Identifier checked on arXiv on 2026-10-15: v1 submitted 2023-12-31.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15,
    commit d1573d2) for the arXiv id and the title found nothing. The anthology
    holds Kaplan et al. (ANTH-LIT-028), Hoffmann et al. (ANTH-LIT-068) and "Noise
    Hypernetworks: Amortizing Test-Time Compute in Diffusion Models" (ANTH-LIT-491).
tags:
- learning-theory
- anthology-candidate
date: '2026-10-15'
published: '2023-12-31'
arxiv: '2401.00448'
first_author: Sardana
keywords:
- scaling laws
- inference cost
- compute-optimal
- Chinchilla
implementations: []
summary: >-
  Sardana, Portes, Doubov and Frankle (2023), arXiv 2401.00448. Adds expected inference
  demand to the compute-optimal choice of model size and training data, so that
  with enough expected queries a smaller model trained longer is cheaper overall.
  As standardly cited; not yet read.
---

# LIT-tmppelbm: Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws

Sardana, N., Portes, J., Doubov, S. and Frankle, J. (2023). Beyond Chinchilla-optimal: Accounting for inference in language model scaling laws. [ARXIV-2401.00448](https://arxiv.org/abs/2401.00448)

Not read. A reading should replace this note.

## Why this is here

The owner, 2026-10-15: "there might also be something useful in the scaling law literature, regarding valuation of pre-training investment (amortized compute) vs inference time search/compute." Read for [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md): compute spent once in training is amortized over every later query, against compute spent at inference per query. Machine learning, filed here for that question with the anthology flag ([ADR-005](../decisions.d/ADR-005.md), [ADR-013](../decisions.d/ADR-013.md)); the anthology may hold its own reading.

Expected reuse made an explicit term in the choice of how much to precompute.
