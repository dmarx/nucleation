---
number: 398
status: Active
formerly:
- CLAIM-tmp5fx5d
title: 'In a stable linear Gaussian VAR(1) on ℝⁿ, a scalar linear coarse variable Y = LX is, in its own law, an ARMA process of orders at most (n, n − 1); so its Mori–Zwanzig memory, though non-zero at every lag in general, is carried exactly by finitely many coordinates that are functions of Y''s own past and innovations'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a stable VAR(1) with Gaussian noise and a
  scalar Y = LX for which det(I − AB)Y_t has non-zero autocovariance at
  some lag of n or more, B the backshift.
tags:
- complex-systems
- probabilistic-modeling
- mathematics
date: '2026-10-20'
line:
- distributed-agency
- formal-apparatus
answers:
- QUESTION-248
grounds:
- LIT-1304
- THEORY-733
rests_on:
- CLAIM-389
summary: >-
  Derived in the reading of Chorin and Lu (2015), [NOTE-1028](../notes.d/NOTE-1028.md), and
  re-checked here. Their NARMAX closures are fitted, with no error bound;
  in the linear Gaussian class the same idea is exact. A coarse variable
  with memory admits a finite Markovian augmentation built only from its
  own history, which is the augmentation [THEORY-257](../theory.d/THEORY-257.md)'s criterion conditions
  on. Scalar Y, VAR(1), Gaussian noise.
---
<!-- inactive-ok-file: THEORY-257 — Proposed; the account whose conditioning set this matches, nothing here rests on it -->

# CLAIM-398: In a stable linear Gaussian VAR(1) on ℝⁿ, a scalar linear coarse variable Y = LX is, in its own law, an ARMA process of orders at most (n, n − 1); so its Mori–Zwanzig memory, though non-zero at every lag in general, is carried exactly by finitely many coordinates that are functions of Y's own past and innovations

## The claim

Take X_t = AX_{t−1} + ε_t, A stable, ε_t Gaussian white noise, and a
scalar Y_t = LX_t. With B the backshift, (I − AB)X_t = ε_t. Multiplying by
the adjugate gives det(I − AB)X_t = adj(I − AB)ε_t. det(I − AB) is a
polynomial φ(B) of degree at most n, and each entry of adj(I − AB) is a
polynomial of degree at most n − 1. So φ(B)Y_t = L adj(I − AB)ε_t is a
finite moving combination of ε at lags 0 to n − 1. Its autocovariance
vanishes beyond lag n − 1. A stationary Gaussian process with that
property is an MA(q) with q ≤ n − 1 in its own innovations (spectral
factorization), so Y is ARMA with orders at most (n, n − 1). Its state in
innovations form consists of past Y and past innovations, which are
functions of Y's own past when the moving-average part is invertible.

Against [CLAIM-389](CLAIM-389.md)'s memory kernels M_j = K₁₂K₂₂^(j−1)K₂₁: these are
non-zero at every lag in general, but by Cayley–Hamilton they satisfy a
linear recurrence of order dim W⊥. The infinite memory is therefore
finitely generated, and the ARMA form realizes it within Y's own history.

**Checks.** On a random n = 3 model, φ(B)Y had autocovariances 1.643,
0.837 and 0.516 at lags 0–2 and below 10⁻¹⁶ at lags 3–6. For
[QUESTION-222](../questions.d/QUESTION-222.md)'s own example (ẋ = −x + y, ẏ = 0.2x − 0.3y, with noise,
sampled at h = 0.1), the continuous kernel 0.2e^(−0.3t) never vanishes,
yet det(I − A_hB)x has autocovariance 0.1767 and −0.0879 at lags 0 and 1
and zero beyond: the sampled x is exactly ARMA(2, 1). Re-run by the
coordinator.

## What it does not say

- **Not the minimal order.** That the ARMA order equals 1 plus the Hankel
  rank of the memory is not proved here. It is proved, for every scalar
  stationary process with rational autocovariance, in [CLAIM-397](CLAIM-397.md). The
  ARMA state is a finite realization of the Wiener filter of
  [THEORY-819](../theory.d/THEORY-819.md).
- **Not a bound for truncation.** Dropping the moving-average part leaves
  an AR(p) model whose extra error fell geometrically, at a rate set by
  the moving-average zero, in one example. That rate is neither an
  eigenvalue of A nor of K₂₂. It is numerical, not part of the claim.
- **Nothing beyond the linear Gaussian VAR(1).** Chorin and Lu's
  nonlinear closures ([THEORY-818](../theory.d/THEORY-818.md)) are fitted and carry no such
  guarantee.
- **Not for vector Y without change.** The same adjugate argument gives
  a VARMA, but its orders and identifiability are not checked here.
