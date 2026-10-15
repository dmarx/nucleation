---
status: Active
status_note: >-
  read in full 2026-10-15 from the arXiv preprint (arxiv.org/pdf/2408.03314, v1
  of 2024-08-06, the only arXiv version) and from the ICLR 2025 conference version,
  open access in the ICLR proceedings (proceedings.iclr.cc, retitled "... than Scaling
  Parameters for Reasoning"), which is a revision not posted to arXiv: it charges
  verifier calls to inference FLOPs, which halves the stated R values (0.16/0.79/22
  become 0.08/0.40/11) at unchanged budgets, and adds a verifier-quality check.
  Worth reading as the standard empirical case that the best use of inference compute
  depends on how hard a question is for the base model, and that choosing the method
  per difficulty bin matches best-of-N with up to about 4× less test-time compute
  on MATH with PaLM 2-S*, before counting the 2048-sample difficulty estimate. For
  [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md) it shows a FLOPs-matched amortization model: a ~14× larger model's
  extra pretraining is a fixed cost spread over all inference, so the per-query
  test-time budget it buys scales as M + 3(M − 1)/R, with R the ratio of inference
  to pretraining tokens; test-time compute wins at low R on easy and medium questions
  and loses at high R and on the hardest questions at every R. R is aggregate inference
  volume, not a count of recurring queries; the larger model's per-token cost is
  a retrieval-cost term; query predictability appears as difficulty but its cost
  is not counted; staleness and erosion are absent.
title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling
  Model Parameters
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: 'Filed, not read. Identifier checked on arXiv on 2026-10-15: v1 submitted
    2024-08-06. Not held in the Anthology of the SOTA: a grep of its record/ (clone
    of 2026-10-15, commit d1573d2) for the arXiv id and the title found nothing.
    The anthology holds Kaplan et al. (ANTH-LIT-028), Hoffmann et al. (ANTH-LIT-068)
    and "Noise Hypernetworks: Amortizing Test-Time Compute in Diffusion Models"
    (ANTH-LIT-491). Read the same day (NOTE-tmpeazah).'
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
  Snell, Lee, Xu and Kumar (2024, arXiv 2408.03314; ICLR 2025). On MATH with PaLM
  2-S*, which way of spending test-time compute works best (beam search against
  a process reward model versus best-of-N; sequential self-revision versus parallel
  sampling) depends on how hard the question is for the base model, and choosing
  the method per difficulty bin matches best-of-N with up to about 4× less test-time
  compute (the discussion says 2–4×). In a FLOPs-matched comparison with a ~14×
  larger model, the extra test-time compute a small model may spend is set by R,
  the ratio of total inference tokens to pretraining tokens: when R is small the
  larger model's pretraining cost buys many samples per query and test-time compute
  wins on easy and medium questions; when R is large the budget per query falls
  toward the parameter ratio and the larger model wins, always on the hardest questions.
  Difficulty estimation (2048 samples per question) and verifier and revision-model
  finetuning are not counted in the compute, R is an aggregate token ratio with
  no term for which queries recur, and the evidence is one model family on one benchmark
  of 500 test questions.
---

# LIT-tmpk7x9f: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

Snell, C., Lee, J., Xu, K. and Kumar, A. (2024). Scaling LLM test-time compute optimally can be more effective than scaling model parameters. [ARXIV-2408.03314](https://arxiv.org/abs/2408.03314)

## Key takeaways

Read in full ([NOTE-tmpeazah](../notes.d/NOTE-tmpeazah.md)). On MATH with PaLM 2-S*, which way of spending test-time compute works best (beam search against a process reward model versus best-of-N; sequential self-revision versus parallel sampling) depends on how hard the question is for the base model, and choosing the method per difficulty bin matches best-of-N with up to about 4× less test-time compute (the discussion says 2–4×). In a FLOPs-matched comparison with a ~14× larger model, the extra test-time compute a small model may spend is set by R, the ratio of total inference tokens to pretraining tokens: when R is small the larger model's pretraining cost buys many samples per query and test-time compute wins on easy and medium questions; when R is large the budget per query falls toward the parameter ratio and the larger model wins, always on the hardest questions. Difficulty estimation (2048 samples per question) and verifier and revision-model finetuning are not counted in the compute, R is an aggregate token ratio with no term for which queries recur, and the evidence is one model family on one benchmark of 500 test questions.

## Why this is here

The owner, 2026-10-15: "there might also be something useful in the scaling law literature, regarding valuation of pre-training investment (amortized compute) vs inference time search/compute." Read for [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md): compute spent once in training is amortized over every later query, against compute spent at inference per query. Machine learning, filed here for that question with the anthology flag ([ADR-005](../decisions.d/ADR-005.md), [ADR-013](../decisions.d/ADR-013.md)); the anthology may hold its own reading.

The per-query side of the trade: when to spend at inference rather than up front.

The reading ([NOTE-tmpeazah](../notes.d/NOTE-tmpeazah.md)) adds the amortization term: in the FLOPs-matched comparison the larger model's extra pretraining is spread over the ratio R of inference to pretraining tokens, and test-time compute wins only at low R on easier questions. R is an aggregate volume, not repeated queries, and the larger model also pays more per inference token, a retrieval cost the amortized-inference readings lacked.
