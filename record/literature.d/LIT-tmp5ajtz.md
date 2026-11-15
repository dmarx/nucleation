---
status: Active
status_note: >-
  read 2026-11-15 (NOTE-tmpjbvav) from the arXiv PDF, v3: the abstract,
  §1, §2 (tasks, coverage, the pass@k estimator), §3.1 (the scaling law),
  §4 (verification and flaky tests) and §5 in full; §2.2–2.3 (model sizes,
  FLOPs and cost) and the appendices other than B skimmed. Worth reading
  here as a measured separation of reachability under a sampling budget
  (coverage at large k) from reliability (one sample), and of reaching a
  correct output from identifying it (the verifier gap): the distinctions
  of CLAIM-567 and CLAIM-576.
title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on
    test-time compute and repeated sampling. Citation checked on the arXiv
    API: Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V.
    Le, Christopher Ré and Azalia Mirhoseini; v1 submitted 2024-07-31,
    which is `published:`; v3 (2024-12-30) is the copy read. No journal-ref
    on arXiv, so filed as a preprint; any later venue is unverified, since
    OpenAlex and Semantic Scholar both refused with HTTP 429 and were not
    retried. No email address was sent to any service. The record held no
    LIT for this work.
tags:
- learning-theory
- anthology-candidate
date: '2026-11-15'
published: '2024-07-31'
arxiv: '2407.21787'
first_author: 'Brown'
keywords:
- 'repeated sampling'
- 'inference compute'
- 'coverage'
- 'pass@k'
- 'verification'
- 'inference-time scaling laws'
implementations:
- https://github.com/ScalingIntelligence/large_language_monkeys
summary: >-
  Brown et al. (2024), arXiv:2407.21787. Coverage, the fraction of problems
  solved by at least one of k independent samples, rises with k over four
  orders of magnitude, often log-linearly; with unit tests as verifier,
  DeepSeek-Coder-V2-Instruct solves 15.9% of SWE-bench Lite with one sample
  and 56% with 250. Without a verifier, majority voting and reward models
  plateau far below coverage. Here for CLAIM-567 (reachable against
  reliably reached) and CLAIM-576 (a budget makes affordable, a verifier
  makes discoverable); the source the record's PASS@(k,T) entries
  (LIT-2441, THEORY-1703) build on without holding. Its account is
  THEORY-tmpmapw3.
---
<!-- inactive-ok-file: THEORY-tmpmapw3 — Proposed; new entries filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-576 THEORY-1703 THEORY-331 — Proposed; the claim this work bears on, the agentic extension of its metric, and the compute-trade reading it is compatible with -->

# LIT-tmp5ajtz: Large Language Monkeys: Scaling Inference Compute with Repeated Sampling

Brown, B., Juravsky, J., Ehrlich, R., Clark, R., Le, Q. V., Ré, C. &
Mirhoseini, A. (2024). Large Language Monkeys: Scaling Inference Compute
with Repeated Sampling. arXiv preprint arXiv:2407.21787.

## Key takeaways

*From the reading, NOTE-tmpjbvav.*

- **Coverage scales with samples** (abstract): "When we apply repeated
  sampling to SWE-bench Lite, the fraction of issues solved with
  DeepSeek-Coder-V2-Instruct increases from 15.9% with one sample to 56%
  with 250 samples, outperforming the single-sample state-of-the-art of
  43%." On CodeContests, Gemma-2B goes "from 0.02% with one sample to 7.1%
  with 10,000 samples" (§1).
- **The verifier gap** (§1): on MATH, coverage rises from 82.9% at 100
  samples to 98.44% at 10,000, while majority voting or reward models gain
  only "from 40.50% to 41.41%".
- **Coverage is per-problem** (§2, Eq. 1): the unbiased estimator
  1 − C(N − Cᵢ, k)/C(N, k), averaged over problems. It approaches
  1 − (1 − pᵢ)^k per problem; over a dataset it is the mean of that, not
  1 − (1 − p̄)^k.

## Standing in the record

A's SWE-bench figure is exact, for DeepSeek-Coder-V2-Instruct in the
Moatless Tools framework. The reader's verdict adds what A's qualifier, a particular
evaluation setup, should name: the 56% is coverage under the repository's
own unit tests as verifier, and 11.3% of problems had flaky tests, handled
by a majority of 11 runs. A's formula 1 − (1 − p)^N is not in the paper;
it holds per problem under i.i.d. sampling, not on the mean success rate.

Compatible with Snell et al. (LIT-1063, THEORY-331): repeated sampling
helps only where per-sample success is above zero. Its advice on spending
inference compute is ML practice and belongs to the anthology (ADR-048);
hence the flag.
