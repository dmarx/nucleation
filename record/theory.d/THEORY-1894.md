---
number: 1894
status: Active
formerly:
- THEORY-tmpmapw3
title: 'Brown and colleagues find that drawing more independent samples from a language model raises coverage, the fraction of problems at least one sample solves, smoothly and often log-linearly over four orders of magnitude, so that with automatic verification DeepSeek-Coder-V2-Instruct goes from 15.9% of SWE-bench Lite issues with one sample to 56% with 250, while without a verifier majority voting and reward-model selection plateau far below coverage'
version: 2
history:
- version: 2
  date: '2026-11-20'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings), under ADR-065. The title reports what Brown and colleagues
    find, keeping their hedges ("often log-linearly"; coverage, not
    success, without a verifier); NOTE-1972 read the sections the title
    draws on in full (abstract, §1, §2, §3.1, §4, §5), and nothing in the
    record contradicts the report. The old promote_when asked for a
    measurement by others: "An independent measurement on another model
    and task with an automatic verifier showing coverage rising with the
    number of independent samples over at least two orders of magnitude,
    and on a task without one showing majority-vote or reward-model
    accuracy plateauing while coverage keeps rising." It moves word for
    word to THEORY-2130, Proposed, which extends this entry and
    asserts the authors' wider thesis. CLAIM-697 now lists this entry
    under corroborated_by, not grounds (ADR-058).
tags:
- learning-theory
- anthology-candidate
date: '2026-11-15'
source:
- LIT-2622
bears_on:
- QUESTION-279
- QUESTION-392
corroborates:
- CLAIM-567
- CLAIM-576
- CLAIM-654
- CLAIM-697
summary: >-
  Brown et al. (2024), [LIT-2622](../literature.d/LIT-2622.md), read in [NOTE-1972](../notes.d/NOTE-1972.md). Repeated
  sampling is a budget: it raises what the process reaches at some attempt
  without changing the model, and the gap between coverage and selection
  separates reaching a correct output from identifying it. Corroborates
  [CLAIM-567](../claims.d/CLAIM-567.md)'s split between reachable and reliably reached with a measured
  case, and [CLAIM-576](../claims.d/CLAIM-576.md)'s split between a budget that makes affordable and a
  capability that makes discoverable; neither claim rests on it. The
  wording is the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1880 — Proposed; new entry filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-576 — Proposed; the claim this account corroborates -->

# THEORY-1894: Brown and colleagues find that drawing more independent samples from a language model raises coverage, the fraction of problems at least one sample solves, smoothly and often log-linearly over four orders of magnitude, so that with automatic verification DeepSeek-Coder-V2-Instruct goes from 15.9% of SWE-bench Lite issues with one sample to 56% with 250, while without a verifier majority voting and reward-model selection plateau far below coverage

## The result

Brown et al. (2024), [LIT-2622](../literature.d/LIT-2622.md); read in [NOTE-1972](../notes.d/NOTE-1972.md).

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
  success at small k is Yue et al.'s result ([THEORY-1880](THEORY-1880.md)), measured
  with this metric.
