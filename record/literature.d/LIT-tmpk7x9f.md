---
status: Deferred
status_note: >-
  filed 2026-10-15, not yet read. Registered at the owner's request (curation entry
  of 2026-10-15). A reading is under way.
title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling
  Model Parameters
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Identifier checked on arXiv on 2026-10-15: v1 submitted 2024-08-06.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15,
    commit d1573d2) for the arXiv id and the title found nothing. The anthology
    holds Kaplan et al. (ANTH-LIT-028), Hoffmann et al. (ANTH-LIT-068) and "Noise
    Hypernetworks: Amortizing Test-Time Compute in Diffusion Models" (ANTH-LIT-491).
tags:
- learning-theory
- anthology-candidate
date: '2026-10-15'
published: '2024-08-06'
arxiv: '2408.03314'
first_author: Snell
keywords:
- test-time compute
- scaling
- verifiers
- revision
implementations: []
summary: >-
  Snell, Lee, Xu and Kumar (2024), arXiv 2408.03314. Studies how to allocate test-time
  compute (search against verifiers, iterative revision) adaptively by prompt difficulty,
  and when extra test-time compute matches the gain from a larger pretrained model
  under matched FLOPs. As standardly cited; not yet read.
---

# LIT-tmpk7x9f: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

Snell, C., Lee, J., Xu, K. and Kumar, A. (2024). Scaling LLM test-time compute optimally can be more effective than scaling model parameters. [ARXIV-2408.03314](https://arxiv.org/abs/2408.03314)

Not read. A reading should replace this note.

## Why this is here

The owner, 2026-10-15: "there might also be something useful in the scaling law literature, regarding valuation of pre-training investment (amortized compute) vs inference time search/compute." Read for [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md): compute spent once in training is amortized over every later query, against compute spent at inference per query. Machine learning, filed here for that question with the anthology flag ([ADR-005](../decisions.d/ADR-005.md), [ADR-013](../decisions.d/ADR-013.md)); the anthology may hold its own reading.

The per-query side of the trade: when to spend at inference rather than up front.
