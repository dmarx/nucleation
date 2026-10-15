---
status: Active
status_note: >-
  read in full 2026-10-15 from the authors' arXiv preprint v3 (arxiv.org/pdf/2401.00448v3,
  14 Apr 2025), which is the ICML 2024 paper (PMLR 235, also fetched from proceedings.mlr.press/v235/sardana24a.html
  and diffed: same equations, tables and numbers, small wording edits); v1 (2023-12-31)
  is an earlier two-author NeurIPS 2023 workshop version without the experiments.
  Worth reading as the worked case of choosing how much to precompute by expected
  use: fixing quality, it adds lifetime inference FLOPs (2N per token) to training
  FLOPs (6N per token), finds the optimum numerically (no closed form), and shows
  the optimal model shrinking and training longer as demand grows (30B-Chinchilla
  quality with 10^13 inference tokens: 13.6B on 2.84× the data, 28% fewer FLOPs;
  in dollars, with inference at 1% utilisation, savings of 17% to 58%), with 47
  training runs up to 10,000 tokens per parameter showing quality still improving
  but more slowly than the fitted law predicts. For [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md) it supplies
  expected reuse and a non-zero per-use cost as explicit terms, and nothing for
  staleness, uncertainty about demand (assumed known before training) or erosion;
  for [CLAIM-tmpygqjz](../claims.d/CLAIM-tmpygqjz.md) it instantiates the break-even n > F/(c_r − c_a − u) with u
  = 0, and shows the choice as a continuous dial tied by a production function rather
  than a file-or-not decision.
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
    Read the same day (NOTE-tmpshw57). The reading found that v1 (2023-12-31) is
    an earlier two-author workshop paper without training runs; the work as cited,
    read in v3 and checked against the ICML 2024 version, first appeared as v2.
    `published:` keeps the arXiv v1 date, per the record's rule.
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
  Sardana, Portes, Doubov and Frankle (2024, ICML; arXiv 2401.00448). Fixing a target
  pre-training loss and adding inference FLOPs (2N per token over a known lifetime
  demand D_inf) to training FLOPs (6N per token), the compute-minimising model is
  smaller and trained on more data than Chinchilla-optimal, increasingly so as D_inf
  approaches and exceeds the training-set size; the optimum has no closed form and
  is found numerically. The savings are modest in FLOPs (for a 30B-Chinchilla-quality
  model with 10^13 inference tokens, 28% by training 13.6B on 2.84× the data) and
  larger in dollars once inference's low hardware utilisation is priced in (17%
  to 58% in the paper's examples). 47 training runs (150M–6B parameters, 10–10,000
  tokens per parameter) find loss still falling at extreme ratios, but more slowly
  than Chinchilla-fitted laws predict, so the formula overstates the gain from long
  training. Demand is assumed known before training and fixed given quality; there
  is no term for uncertainty, discounting, obsolescence or a model being replaced.
---

# LIT-tmppelbm: Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws

Sardana, N., Portes, J., Doubov, S. and Frankle, J. (2023). Beyond Chinchilla-optimal: Accounting for inference in language model scaling laws. [ARXIV-2401.00448](https://arxiv.org/abs/2401.00448)

## Key takeaways

Read in full ([NOTE-tmpshw57](../notes.d/NOTE-tmpshw57.md)). Fixing a target pre-training loss and adding inference FLOPs (2N per token over a known lifetime demand D_inf) to training FLOPs (6N per token), the compute-minimising model is smaller and trained on more data than Chinchilla-optimal, increasingly so as D_inf approaches and exceeds the training-set size; the optimum has no closed form and is found numerically. The savings are modest in FLOPs (for a 30B-Chinchilla-quality model with 10^13 inference tokens, 28% by training 13.6B on 2.84× the data) and larger in dollars once inference's low hardware utilisation is priced in (17% to 58% in the paper's examples). 47 training runs (150M–6B parameters, 10–10,000 tokens per parameter) find loss still falling at extreme ratios, but more slowly than Chinchilla-fitted laws predict, so the formula overstates the gain from long training. Demand is assumed known before training and fixed given quality; there is no term for uncertainty, discounting, obsolescence or a model being replaced.

## Why this is here

The owner, 2026-10-15: "there might also be something useful in the scaling law literature, regarding valuation of pre-training investment (amortized compute) vs inference time search/compute." Read for [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md): compute spent once in training is amortized over every later query, against compute spent at inference per query. Machine learning, filed here for that question with the anthology flag ([ADR-005](../decisions.d/ADR-005.md), [ADR-013](../decisions.d/ADR-013.md)); the anthology may hold its own reading.

Expected reuse made an explicit term in the choice of how much to precompute.

The reading ([NOTE-tmpshw57](../notes.d/NOTE-tmpshw57.md)) confirms it: lifetime inference demand is an explicit term, so with enough demand a smaller model trained longer is cheaper. Demand is assumed known in advance and independent of model size; there is no staleness, uncertainty or erosion term, and the precomputed thing is a cheaper computation, not a stored answer.
