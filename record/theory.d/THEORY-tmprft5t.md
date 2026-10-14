---
status: Proposed
promote_when: >-
  An independent check of Theorem 1 of LIT-948, or a matching result by
  other authors: a proof that the kernel-free LP characterises bicausal
  occupancy couplings, and that a sample-based estimator reaches ε
  accuracy with a number of independent occupancy samples polynomial in
  |X|, |Y|, 1/(1−γ) and 1/ε². A lower bound matching the ε⁻² rate in this
  setting would also strengthen it. It is refuted by an error in
  Proposition 1, or by a family of finite chains on which the estimator,
  run as the theorem specifies, misses by more than the bound with
  probability above δ. What cannot settle it: experiments run with tuned
  decaying step sizes and minibatches, or on correlated single-trajectory
  data, which lie outside the theorem.
title: 'The bisimulation metric between two finite Markov chains can be estimated from sampled transitions without a transition model, to accuracy ε with a number of samples polynomial in the state-space sizes and 1/ε²'
version: 1
tags:
- mathematical-statistics
- probabilistic-modeling
date: '2026-10-14'
source:
- LIT-948
- LIT-962
summary: >-
  Calo, Jonsson, Neu, Schwartz & Segovia-Aguas (2025), [LIT-948](../literature.d/LIT-948.md), read in
  [NOTE-tmp6orlr](../notes.d/NOTE-tmp6orlr.md). Bicausal occupancy couplings are characterised by
  constraints that use only each chain's sampled occupancy measure over
  consecutive state pairs. A stochastic primal-dual method on them gets an
  ε-accurate estimate with probability 1−δ from
  O((|X||Y|(|X|+|Y|) + (|X|+|Y|)log(1/δ))/((1−γ)²ε²)) independent
  samples per chain. The states must be observed and enumerable, the cost
  known, and the samples drawn with restarts. A single running stream and
  latent states are outside it.
---
<!-- inactive-ok-file: QUESTION-008 THEORY-tmp7x3wf — Deferred or Proposed; the set-aside question this bears on, and the identification this account inherits, cited as open -->

# THEORY-tmprft5t: The bisimulation metric between two finite Markov chains can be estimated from sampled transitions without a transition model, to accuracy ε with a number of samples polynomial in the state-space sizes and 1/ε²

## Source

Calo, Jonsson, Neu, Schwartz and Segovia-Aguas (2025), [LIT-948](../literature.d/LIT-948.md), read in
[NOTE-tmp6orlr](../notes.d/NOTE-tmp6orlr.md): §3 (Proposition 1, the Lagrangian, SOMCOT), §4
(Theorem 1, Lemma 1), Appendices A, B.4 and C. It builds on [LIT-962](../literature.d/LIT-962.md)
([THEORY-tmp7x3wf](THEORY-tmp7x3wf.md)) for the identification of the bicausal transport
distance with the bisimulation metric.

## What was actually shown

**A kernel-free characterisation (Proposition 1).** Let ν_X(x, x') be
the discounted occupancy of consecutive state pairs of M_X, and ν_Y that
of M_Y. Then µ is the occupancy coupling of a bicausal coupling if and
only if, for some nonnegative λ_X(y|x) and λ_Y(x|y), three conditions
hold:

- the flow constraint holds;
- Σ_{y'} µ(x,y,x',y') = ν_X(x,x') λ_X(y|x);
- Σ_{x'} µ(x,y,x',y') = ν_Y(y,y') λ_Y(x|y).

The proof shows these are equivalent to [LIT-962](../literature.d/LIT-962.md)'s kernel-based coherence
constraints, using P_X(x'|x) = ν_X(x,x')/ν_X(x).

**An estimator with a guarantee (Theorem 1).** The distance is a saddle
point of a Lagrangian whose ν-dependent gradients have unbiased
one-sample estimators. Entropic stochastic mirror descent runs on the
primal variables and projected stochastic gradient ascent on the duals.
Assume ‖c‖∞ ≤ 1, with the stated step sizes. Then the averaged iterate
satisfies, with probability at least 1 − δ,
|⟨µ̄_K − µ*, c⟩| = O((√(|X||Y|(|X|+|Y|)) + √((|X|+|Y|) log(1/δ))) / (√K (1−γ))).
Each iteration uses one transition from each chain and Θ(|X|²|Y|²)
computation, and the constants are numerical only.

**What could have failed.** If the coupling constraints could not be
written in terms of sampleable quantities, no unbiased gradient would
exist. The rate also had to come out polynomial: the proof bounds the
error by a duality gap and the gap by the players' regrets, and a
rounding argument (Lemma 2) is needed to turn an infeasible average into
a bound.

## What this does not say

- **Not from a single stream.** The theorem assumes independent draws
  from the discounted occupancy measures. Drawing them exactly means
  running each chain from its fixed initial state to a geometric time
  and keeping the last pair, so restarts are needed. Data from one
  running trajectory are outside the theorem. The authors "expect" the
  method to cope with them, and their experiments do not use such data.
- **Not without observing the states.** The state spaces must be finite,
  known in advance and observed in each sample, since the primal variable
  is a table over (X×Y)². The kernel may be unknown; the states may not
  be latent.
- **Not without a given cost.** The ground cost must be known on every
  pair of states. Which differences count is decided before estimation,
  not learned.
- **Not an exact test of bisimilarity.** An ε-estimate cannot certify
  distance zero, so it gives approximate bisimulation, not a decision on
  the relation.
- **Not for systems with actions,** as in [THEORY-tmp7x3wf](THEORY-tmp7x3wf.md).
- **Not a proved optimal rate.** The ε⁻² dependence is said to be optimal
  by appeal to lower bounds for static transport, not proved here.

## Connections

- **[THEORY-tmp7x3wf](THEORY-tmp7x3wf.md)** is the identification this estimator inherits.
- **[QUESTION-008](../questions.d/QUESTION-008.md)** (Deferred). [LIT-948](../literature.d/LIT-948.md) was filed as making approximate
  bisimulation "measurable for systems whose update structure is not
  known". It does that only where states are observed. [QUESTION-008](../questions.d/QUESTION-008.md)'s
  fidelity notion ([TERM-033](../terms.d/TERM-033.md)) compares observed responses with "no shared
  latent state required", which is the case the estimator does not
  cover. No `answers:` relation is filed.
