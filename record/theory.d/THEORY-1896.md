---
number: 1896
status: Proposed
formerly:
- THEORY-tmppt44k
promote_when: >-
  Theorems 2.1–2.3 and Lemma 3.2 checked step by step under their stated
  assumptions, by a reader or an independent paper, with no error found:
  forward-KL fine-tuning on new data alone has β⋆ = 0 as its unique
  population minimizer, reverse-KL RL toward the mode-keeping target
  converges to it with old-mean drift bounded by overlap terms decaying
  exponentially in separation, and the tilt of a frozen reference keeps its
  components and only reweights them.
title: 'Balasubramanian and Kasiviswanathan prove, in a two-mode equal-covariance Gaussian mixture with the old component already correct, that forward-KL fine-tuning on new data alone drives the old mode''s weight to zero, while KL-regularized reinforcement learning toward a target that keeps the old mode converges to that target and moves the old mean only through overlap terms that decay exponentially with mode separation, and that an exponential tilt of a frozen reference can reweight its modes but not create or recover one'
version: 1
tags:
- learning-theory
- probabilistic-modeling
- anthology-candidate
date: '2026-11-15'
source:
- LIT-2630
bears_on:
- QUESTION-392
summary: >-
  Balasubramanian & Kasiviswanathan (2026), [LIT-2630](../literature.d/LIT-2630.md), read in
  [NOTE-1986](../notes.d/NOTE-1986.md). The formal counterpart, under a fixed KL anchor, of the
  reading of RL post-training as sharpening ([THEORY-1880](THEORY-1880.md)): the optimum
  is a tilt of the reference, which keeps its components. Proved in an
  idealization; the tilt result assumes disjoint support and step rewards.
  No CLAIM is listed as corroborated; its bearing on [CLAIM-576](../claims.d/CLAIM-576.md) is proposed
  as a dated note. The wording is the reader's; adopting it is the owner's
  call.
---
<!-- inactive-ok-file: THEORY-1880 THEORY-1908 — Proposed; new entries filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-576 — Proposed; the claim this account bears on -->

# THEORY-1896: Balasubramanian and Kasiviswanathan prove, in a two-mode equal-covariance Gaussian mixture with the old component already correct, that forward-KL fine-tuning on new data alone drives the old mode's weight to zero, while KL-regularized reinforcement learning toward a target that keeps the old mode converges to that target and moves the old mean only through overlap terms that decay exponentially with mode separation, and that an exponential tilt of a frozen reference can reweight its modes but not create or recover one

## The result

Balasubramanian & Kasiviswanathan (2026), [LIT-2630](../literature.d/LIT-2630.md); read in
[NOTE-1986](../notes.d/NOTE-1986.md).

Population-level theorems in the two-mode model. Forward KL on new data
alone "is strictly increasing in β ... so β⋆ = 0 is the unique population
minimizer" (Thm. 2.1). Reverse KL toward the mode-keeping target converges
to it, with drift "gated by misassignment probabilities that decay
exponentially with mode separation" (Thms. 2.2–2.3). For max E[r] −
τ·KL(π‖πref), "The unique optimizer is the exponential tilt" (App. A); in
the disjoint-support case with step rewards, the tilted target keeps the
reference's components and reweights them by Eq. 3.18, so a mode with zero
reference mass stays at zero (Lemma 3.2). These are proofs; what could
fail is a step of a derivation, which this reading did not check.

## What it does not show

- Anything about language models directly: whether "modes" are behaviours
  is left to future work (§4), and no experiment on a language model was
  read.
- That RL in practice cannot create modes. The tilt result needs a fixed
  reference; Yue et al. mostly train without KL, and ProRL
  ([THEORY-1908](THEORY-1908.md)) resets the reference.
- The result beyond two modes (App. D, not read) or beyond equal
  covariances.
