---
status: Read
paper: LIT-tmp5ajtz
title: 'Brown et al. — Large Language Monkeys'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:2407.21787v3, https://arxiv.org/pdf/2407.21787,
    text by pdftotext. Read in full: the abstract, §1, §2 (tasks, coverage
    and the pass@k estimator, §2.1 results), §3.1 (the scaling law, Fig.
    5), §4 (verification, flaky tests) and §5 (discussion and limitations).
    Skimmed: §2.2–2.3 (model sizes, FLOPs and cost) and the appendices
    other than B. The filer rechecked every quote below against the
    downloaded text. The abstract says selection methods plateau "beyond
    several hundred samples", §1 and §4 "beyond approximately 100 samples";
    both are reported.
date: '2026-11-15'
summary: >-
  Repeated independent sampling as an axis of inference compute. Coverage
  rises with the number of samples, often log-linearly, and with an
  automatic verifier becomes success (SWE-bench Lite: 15.9% at one sample,
  56% at 250). Without one, majority vote and reward models plateau far
  below coverage. A measured gap between reachability under a budget and
  reliability, and between reaching a correct output and identifying it.
---
<!-- inactive-ok-file: LIT-tmp5ajtz THEORY-tmpmapw3 THEORY-tmp9rnyv — new entries filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-576 THEORY-1703 CLAIM-663 THEORY-331 — Proposed; entries this reading bears on or sits beside -->

# NOTE-tmpjbvav: Brown et al. — Large Language Monkeys

## Contribution

Treats the number of independent samples as a scaling axis for inference
compute. Coverage, the fraction of problems at least one sample solves,
rises smoothly with the number of samples across tasks and models, and is
fit by an exponentiated power law. Where answers can be verified
automatically, coverage is success, and a weaker model with many samples
can beat a stronger model with one.

## Key insight

Repeated sampling makes reachable what a single attempt seldom reaches;
whether that reach is usable depends on a verifier that can "find the
needle in the haystack" (§1).

## Assumptions

- Pass/fail tasks; samples i.i.d. given the prompt. §5: all attempts are
  "generated independently of one another using the exact same prompt and
  hyperparameters", with temperature "the sole mechanism for creating
  diversity".
- Coverage is an upper bound on success, reached only with a perfect
  verifier; for GSM8K and MATH it uses an oracle answer check.

## Key results

- **SWE-bench Lite** (abstract): "the fraction of issues solved with
  DeepSeek-Coder-V2-Instruct increases from 15.9% with one sample to 56%
  with 250 samples, outperforming the single-sample state-of-the-art of
  43%." §2.1: "One sample/attempt for this benchmark refers to one entire
  multi-turn trajectory" in the Moatless Tools framework, checked "using
  the repository's suite of unit tests".
- **Flaky tests** (§4.2.1): "11.3% of problems have flaky test suites";
  these are run 11 times and a majority taken (App. B).
- **CodeContests** (§1): Gemma-2B coverage goes "from 0.02% with one sample
  to 7.1% with 10,000 samples".
- **The verifier gap** (§1): on MATH with Llama-3-8B-Instruct, coverage goes
  from 82.9% at 100 samples to 98.44% at 10,000; majority voting or reward
  models improve only "from 40.50% to 41.41%". Selection methods plateau
  "beyond several hundred samples" (abstract), "beyond approximately 100
  samples" (§1).
- **The law** (§3.1, Eq. 2): log(c) ≈ a·k^b, over "four orders of
  magnitude"; some curves "do not follow this trend closely" (Fig. 5).
- **The estimator** (§2, Eq. 1): pass@k is the mean over problems of
  1 − C(N − Cᵢ, k)/C(N, k), Chen et al.'s unbiased estimator.

## Concepts

Coverage (pass@k); precision and verification; inference-time scaling law;
amplifying a weaker model; the verifier bottleneck.

## Bearing on the record

- **CLAIM-567 (feasible, reachable, reliably reached)**: a measured case.
  Coverage at large k is reachability by the sampling process; one-sample
  success is nearer reliability. At 56% against 15.9% the two are far
  apart. It adds a measured witness to the claim's demonstrated ones.
- **CLAIM-576 (budget, discovery, architecture)**: close to a direct
  instance of two of its three ways. Raising k is a budget that makes
  already-possible solutions affordable to reach; the verifier gap
  separates reaching a correct output from being able to pick it out,
  which is the claim's discoverability apart from affordability.
- **QUESTION-279**: coverage keeps rising where selection has stopped, so a
  finite run of failed attempts does not show that no solution is
  reachable.
- **LIT-2441 and THEORY-1703 (PASS@(k,T))**: this is the single-turn
  coverage metric that Zhai et al. extend with interaction depth, and that
  Yue et al. (THEORY-tmp9rnyv) use to compare base and RL models.
- **THEORY-331 (Snell et al.)**: compatible. Repeated sampling raises
  coverage only where per-sample success is above zero, as test-time
  compute wins there only on questions the small model sometimes solves.

## Limitations

- The cost and FLOPs analysis was skimmed.
- The SWE-bench figure is one model in one agent framework.
- Coverage is not deployable success where no verifier exists.
