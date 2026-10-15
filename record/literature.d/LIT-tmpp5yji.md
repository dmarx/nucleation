---
status: Deferred
status_note: >-
  filed 2026-10-15, not yet read. Registered at the owner's request (curation entry
  of 2026-10-15). A reading is under way.
title: Scaling Scaling Laws with Board Games
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Identifier checked on arXiv on 2026-10-15: v1 submitted 2021-04-07.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15,
    commit d1573d2) for the arXiv id and the title found nothing. The anthology
    holds Kaplan et al. (ANTH-LIT-028), Hoffmann et al. (ANTH-LIT-068) and "Noise
    Hypernetworks: Amortizing Test-Time Compute in Diffusion Models" (ANTH-LIT-491).
tags:
- learning-theory
- anthology-candidate
date: '2026-10-15'
published: '2021-04-07'
arxiv: '2104.03113'
first_author: Jones
keywords:
- scaling laws
- AlphaZero
- Hex
- train-time compute
- test-time compute
implementations: []
summary: >-
  Jones (2021), arXiv 2104.03113. Fits scaling laws for AlphaZero-style agents on
  Hex across board sizes and finds a trade-off between train-time and test-time
  compute: more training buys the same performance as more search at play time,
  at a measured exchange rate. As standardly cited; not yet read.
---

# LIT-tmpp5yji: Scaling Scaling Laws with Board Games

Jones, A. L. (2021). Scaling scaling laws with board games. [ARXIV-2104.03113](https://arxiv.org/abs/2104.03113)

Not read. A reading should replace this note.

## Why this is here

The owner, 2026-10-15: "there might also be something useful in the scaling law literature, regarding valuation of pre-training investment (amortized compute) vs inference time search/compute." Read for [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md): compute spent once in training is amortized over every later query, against compute spent at inference per query. Machine learning, filed here for that question with the anthology flag ([ADR-005](../decisions.d/ADR-005.md), [ADR-013](../decisions.d/ADR-013.md)); the anthology may hold its own reading.

The cleanest measured exchange rate between amortized (training) and per-query (search) compute.
