---
number: 280
status: Active
formerly:
- THEORY-tmprft5t
title: "The bisimulation metric between two finite Markov chains with observed states and a known cost bounded by 1 can be estimated without a transition model from independent samples of each chain's discounted state-pair occupancy, to accuracy ε with probability 1 − δ from a number of samples polynomial in the state-space sizes, 1/(1−γ), log(1/δ) and 1/ε²"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted at the owner's direction, carrying out the
    promotion audit's decision for THEORY-280 (batch 042, ADR-047 v2).
    Theorem 1 of Calo et al. was re-checked against the arXiv text: the
    kernel-free characterisation, the bound of the error by the duality
    gap through the rounding lemma, and each player's regret, in the dated
    note below. The rate holds; the constants carry slips that do not
    affect it. The title now names the sampling model, the observed finite
    states, the known bounded cost, the probability 1 − δ and the
    dependence on 1/(1−γ) and log(1/δ). The former promote_when's request
    for a matching ε⁻² lower bound moves to QUESTION-tmpimdnt.
tags:
- mathematical-statistics
- probabilistic-modeling
date: '2026-10-14'
source:
- LIT-948
- LIT-962
summary: >-
  Calo, Jonsson, Neu, Schwartz & Segovia-Aguas (2025), [LIT-948](../literature.d/LIT-948.md), read in
  [NOTE-763](../notes.d/NOTE-763.md). Bicausal occupancy couplings are characterised by
  constraints that use only each chain's sampled occupancy measure over
  consecutive state pairs. A stochastic primal-dual method on them gets an
  ε-accurate estimate with probability 1−δ from
  O((|X||Y|(|X|+|Y|) + (|X|+|Y|)log(1/δ))/((1−γ)²ε²)) independent
  samples per chain. The states must be observed and enumerable, the cost
  known, and the samples drawn with restarts. A single running stream and
  latent states are outside it.
---
<!-- inactive-ok-file: QUESTION-008 — Deferred or Proposed; the set-aside question this bears on, and the identification this account inherits, cited as open -->

# THEORY-280: The bisimulation metric between two finite Markov chains with observed states and a known cost bounded by 1 can be estimated without a transition model from independent samples of each chain's discounted state-pair occupancy, to accuracy ε with probability 1 − δ from a number of samples polynomial in the state-space sizes, 1/(1−γ), log(1/δ) and 1/ε²

## Source

Calo, Jonsson, Neu, Schwartz and Segovia-Aguas (2025), [LIT-948](../literature.d/LIT-948.md), read in
[NOTE-763](../notes.d/NOTE-763.md): §3 (Proposition 1, the Lagrangian, SOMCOT), §4
(Theorem 1, Lemma 1), Appendices A, B.4 and C. It builds on [LIT-962](../literature.d/LIT-962.md)
([THEORY-247](THEORY-247.md)) for the identification of the bicausal transport
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
- **Not for systems with actions,** as in [THEORY-247](THEORY-247.md).
- **Not a proved optimal rate.** The ε⁻² dependence is said to be optimal
  by appeal to lower bounds for static transport, not proved here.

## Connections

- **[THEORY-247](THEORY-247.md)** is the identification this estimator inherits.
- **[QUESTION-008](../questions.d/QUESTION-008.md)** (Deferred). [LIT-948](../literature.d/LIT-948.md) was filed as making approximate
  bisimulation "measurable for systems whose update structure is not
  known". It does that only where states are observed. [QUESTION-008](../questions.d/QUESTION-008.md)'s
  fidelity notion ([TERM-033](../terms.d/TERM-033.md)) compares observed responses with "no shared
  latent state required", which is the case the estimator does not
  cover. No `answers:` relation is filed.

## Note of 2026-10-19: Theorem 1, re-checked

The promotion audit (batch 042) followed Calo et al.'s proof against the
arXiv v1 text (App. A and C), at the level of the rate the title claims.

1. *Proposition 1.* With ν_µ(x, y) the state marginal of µ, the kernel
   coherence of [THEORY-247](THEORY-247.md) reads Σ_{y′} µ(x,y,x′,y′) = P_X(x′|x)ν_µ(x,y).
   Setting λ_X(y|x) = ν_µ(x,y)/ν_X(x) and using ν_X(x,x′) = ν_X(x)P_X(x′|x)
   turns it into (7); conversely, summing (7) over x′ gives
   ν_µ(x,y) = ν_X(x)λ_X(y|x), and substituting back gives coherence. The flow
   constraint, marginalised over y, makes the X-marginal of ν_µ solve the
   chain's own occupancy equation, whose solution is unique, so λ_X(·|x) is
   a distribution wherever ν_X(x) > 0.
2. *Error and duality gap (Lemma 1).* The Lagrangian is linear in the
   primal variables, so averaging the iterates averages the Lagrangian. Its
   maximum over the dual balls, of radius 6/(1−γ) for α and 2/(1−γ) for V,
   is ⟨µ̄, c⟩ plus (6∂C_X + 6∂C_Y + 2∂F)/(1−γ), the ℓ1 residuals of the three
   constraints. Rounding µ̄ to a valid occupancy coupling costs at most
   (3∂C_X + 3∂C_Y + ∂F)/(1−γ) in ℓ1 (Lemma 2: a contraction by γ through the
   flow constraint, and Altschuler et al.'s rounding bound per state pair).
   Since the rounded coupling is feasible and ‖c‖∞ ≤ 1, the error is at
   most the duality gap.
3. *Regrets.* Each player's regret is that of mirror descent or projected
   gradient ascent with bounded gradients on a bounded set: the α-players'
   of order √(|X|²|Y|K)/(1−γ) and √(|X||Y|²K)/(1−γ), the V-player's
   √(|X||Y|K)/(1−γ), the µ-player's √(K log(|X||Y|))/(1−γ), and the
   λ-players' √(|X| log|Y| K)/(1−γ) and √(|Y| log|X| K)/(1−γ). The dual
   comparator depends on the data; a ghost iterate (Nemirovski et al.;
   Rakhlin and Sridharan) turns the noise into a martingale with bounded
   increments, adding √(K log(1/δ))/(1−γ) terms. Dividing by K gives the
   stated rate.

The constants carry slips that leave the rate alone: with equal step
sizes the Bregman term is counted once where it appears twice, one
martingale constant is off by 2, and the final union bound covers four
probabilistic claims, not two, so the guarantee is 1 − 4δ for the stated
δ. [NOTE-763](../notes.d/NOTE-763.md) gives the dual radii as (1−γ)/6 and (1−γ)/2; they are 6/(1−γ)
and 2/(1−γ), as Lemma 1 needs.
