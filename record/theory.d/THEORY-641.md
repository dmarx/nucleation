---
number: 641
status: Active
formerly:
- THEORY-tmptk080
title: "Under a well-specified, identifiable parametric Markov model of the target given the joint past, with ergodic lagged states, transfer entropy is the limit of the normalised log-likelihood ratio for the null of no dependence on the source's past, so it is Granger-sense predictive improvement; for finite-state chains the plug-in estimator is exactly that statistic, and under the null and the usual regularity it is asymptotically χ² with the difference in parameter counts as degrees of freedom"
version: 1
tags:
- information-theory
- mathematical-statistics
date: '2026-10-16'
source:
- LIT-048
summary: >-
  Barnett & Bossomaier (2012), [LIT-048](../literature.d/LIT-048.md), read in full in [NOTE-053](../notes.d/NOTE-053.md). The
  consistency result is a one-line consequence of Props. 1–2, and Prop. 2
  is argued informally. The χ² null is imported from Wald (1943), whose
  regularity conditions are not checked. The non-central χ² for T > 0 is
  at best a local-alternative approximation. The finite-state identity
  and the Gaussian equivalence (half the Granger statistic) are exact.
---

<!-- inactive-ok-file: THEORY-275 — Proposed; named as where such a test would apply, nothing here rests on it -->

# THEORY-641: Under a well-specified, identifiable parametric Markov model of the target given the joint past, with ergodic lagged states, transfer entropy is the limit of the normalised log-likelihood ratio for the null of no dependence on the source's past, so it is Granger-sense predictive improvement; for finite-state chains the plug-in estimator is exactly that statistic, and under the null and the usual regularity it is asymptotically χ² with the difference in parameter counts as degrees of freedom

## Source

Barnett & Bossomaier (2012), "Transfer Entropy as a Log-likelihood
Ratio", arXiv 1205.6339v3 (Phys. Rev. Lett. 109, 138105), [LIT-048](../literature.d/LIT-048.md), read
in full in [NOTE-053](../notes.d/NOTE-053.md). The PRL version was not compared.

## What was actually shown

**The setting.** (X_t, Y_t) jointly stationary; X's law given the k-lag
joint history is f(x_t | x^k_t, y^k_t; θ), identifiable and
well-specified; the lagged vector U_t is ergodic. The joint process need
not be Markov.

**Prop. 1.** The average log-likelihood of the true model converges
almost surely to −H(X_t | X^k_t, Y^k_t), by the ergodic theorem.

**Theorem 1a.** Transfer entropy is a difference of two such conditional
entropies, so T̂ = −(1/(n−k)) log Λ, for the nested null "f does not
depend on y^k_t", converges almost surely to T_{Y→X}. It is consistent
but "will generally be biased".

**Theorem 1b.** If T = 0, 2(n−k)T̂ is asymptotically χ²(d), with d the
difference in parameter counts. This follows "from the standard
large-sample theory" (Wald 1943) and is not proved in the letter.

**Two exact cases.**

- *Finite state spaces (Eqs. 19–21).* The plug-in estimator is the
  likelihood-ratio estimator, because the transition probabilities are
  the parameters and their ML estimates are the empirical conditionals.
  So d = (a−1)a^k(b^k−1). The reading checked d = 2 at a = b = 2, k = 1.
- *Linear Gaussian VAR (p. 5).* T̂ is half the Granger-causality
  statistic, recovering Barnett, Barrett & Seth (2009).

**Illustration (Fig. 1).** A binary bivariate chain, with T_{Y→X} =
0.0823 nats at θ = 0.4 (checked), approaches the χ²(2) null at n = 20,
40, 100 over 10⁵ realisations.

What could have come out otherwise: the plug-in estimator need not have
coincided with any likelihood ratio. For finite states it does, exactly.

## What this does not say

- **That transfer entropy measures causal influence in the
  interventional sense.** It is a predictive, log-likelihood-ratio
  quantity, Granger's sense, not Pearl's ([NOTE-053](../notes.d/NOTE-053.md), on [LIT-025](../literature.d/LIT-025.md)).
- **That the χ² null holds at realistic sample sizes.** It is asymptotic,
  under regularity the letter does not check. A boundary null, such as a
  transition probability of zero, breaks it. The evidence is one toy
  chain at n ≤ 100.
- **That 2(n−k)T̂ is non-central χ² when T > 0.** λ grows with n, so that
  can only be a local-alternative approximation; for fixed T > 0 the
  statistic is asymptotically normal ([NOTE-053](../notes.d/NOTE-053.md), Corrections).
- **That surrogate tests are unnecessary.** Asserted in the conclusion,
  with no finite-sample comparison (C9).
- **Anything about conditional transfer entropy.** "It may be verified"
  (p. 5) is not a proof (C8).
- **What T̂ estimates under misspecification.** Then it estimates a
  KL-projection quantity, not the transfer entropy.

## Connections

- Wald (1943), the source of the χ² null, is the paper Stigler presents
  as the rigorous completion of Fisher's argument with restrictive
  conditions, and the finite-state d grows exponentially in k, which is
  Neyman–Scott territory ([THEORY-534](THEORY-534.md); the link is [NOTE-053](../notes.d/NOTE-053.md)'s).
- T_{Y→X} = I(X_t; Y^k_t | X^k_t) is one summand of the vulnerability
  invariant's numerator ([THEORY-568](THEORY-568.md)), so this gives a model-based
  sampling distribution for one term of a Shannon invariant.
- [THEORY-031](THEORY-031.md) (the likelihood-ratio detector) shares only the
  likelihood-ratio framing. [THEORY-275](THEORY-275.md) measures directional information
  between coupled units and is where a test of this kind would be applied.
