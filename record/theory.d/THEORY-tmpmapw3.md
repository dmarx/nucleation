---
status: Proposed
promote_when: >-
  An independent measurement on another model and task with an automatic
  verifier showing coverage rising with the number of independent samples
  over at least two orders of magnitude, and on a task without one showing
  majority-vote or reward-model accuracy plateauing while coverage keeps
  rising.
title: 'Brown and colleagues find that drawing more independent samples from a language model raises coverage, the fraction of problems at least one sample solves, smoothly and often log-linearly over four orders of magnitude, so that with automatic verification DeepSeek-Coder-V2-Instruct goes from 15.9% of SWE-bench Lite issues with one sample to 56% with 250, while without a verifier majority voting and reward-model selection plateau far below coverage'
version: 1
tags:
- learning-theory
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmp5ajtz
bears_on:
- QUESTION-279
- QUESTION-392
corroborates:
- CLAIM-567
- CLAIM-576
summary: >-
  Brown et al. (2024), LIT-tmp5ajtz, read in NOTE-tmpjbvav. Repeated
  sampling is a budget: it raises what the process reaches at some attempt
  without changing the model, and the gap between coverage and selection
  separates reaching a correct output from identifying it. Corroborates
  CLAIM-567's split between reachable and reliably reached with a measured
  case, and CLAIM-576's split between a budget that makes affordable and a
  capability that makes discoverable; neither claim rests on it. The
  wording is the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-tmp5ajtz NOTE-tmpjbvav — new entries filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-576 THEORY-1703 — Proposed; the claim this account corroborates and the agentic extension of its metric -->

# THEORY-tmpmapw3: Brown and colleagues find that drawing more independent samples from a language model raises coverage, the fraction of problems at least one sample solves, smoothly and often log-linearly over four orders of magnitude, so that with automatic verification DeepSeek-Coder-V2-Instruct goes from 15.9% of SWE-bench Lite issues with one sample to 56% with 250, while without a verifier majority voting and reward-model selection plateau far below coverage

## The result

Brown et al. (2024), LIT-tmp5ajtz; read in NOTE-tmpjbvav.

Across coding, formal-proof and math tasks and several model families,
coverage measured by the unbiased per-problem estimator rises with the
number of samples k, fit by log(c) ≈ a·k^b (§3.1). On SWE-bench Lite, with
the repository's unit tests as verifier, coverage is success: 15.9% at
one sample, 56% at 250 (abstract). On MATH, coverage reaches 98.44% at
10,000 samples while majority voting or reward models stay near 41% (§1).
It could have come out otherwise: coverage could have saturated early, and
selection could have tracked coverage.

## What it does not show

- That a problem unsolved at the largest k is unsolvable. Coverage is
  still rising where it stops.
- That repeated sampling helps where per-sample success is zero: the
  estimator is per problem, and coverage over a dataset is the mean of
  1 − (1 − pᵢ)^k, not 1 − (1 − p̄)^k.
- Deployable success without a verifier. The 56% depends on unit tests,
  11.3% of which were flaky (§4.2.1).
- Anything about training. That RL can trade coverage at large k for
  success at small k is Yue et al.'s result (THEORY-tmp9rnyv), measured
  with this metric.
