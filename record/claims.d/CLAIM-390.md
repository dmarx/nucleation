---
number: 390
status: Active
formerly:
- CLAIM-tmpymy0a
title: 'For a block of coordinates in a stable linear Gaussian VAR(1), dynamical dependence is at most ½ log det(I + Σ_YY⁻¹ A_YR C A_YRᵀ), with A_YR the coupling into the block and C the covariance of the rest given the block''s present state, so it is of second order in the coupling into the block, whatever the coupling out of it'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a stable linear Gaussian VAR(1) and a block
  of its coordinates whose transfer entropy from the whole system exceeds
  the stated bound.
tags:
- complex-systems
- information-theory
- mathematics
date: '2026-10-20'
line:
- distributed-agency
- formal-apparatus
grounds:
- THEORY-733
summary: >-
  First found in the reading of Chorin, Hald and Kupferman (2000),
  [NOTE-989](../notes.d/NOTE-989.md), as a by-product; derived and checked here. It answers
  the forward half of [QUESTION-221](../questions.d/QUESTION-221.md) for a block's full state: weak
  coupling into a block makes its dynamical dependence small, to second
  order. It is about the block's full state, not its aggregate. For the
  aggregate, the block's own internal dynamics add a defect of their own
  ([CLAIM-386](CLAIM-386.md)).
bears_on:
- QUESTION-221
---
<!-- inactive-ok-file: THEORY-257 — Proposed; the account whose dependence this bounds, open -->
# CLAIM-390: For a block of coordinates in a stable linear Gaussian VAR(1), dynamical dependence is at most ½ log det(I + Σ_YY⁻¹ A_YR C A_YRᵀ), with A_YR the coupling into the block and C the covariance of the rest given the block's present state, so it is of second order in the coupling into the block, whatever the coupling out of it

## The claim

Let X = (Y, R) with X_t = AX_{t−1} + ε_t stable, ε_t ~ N(0, Σ), Σ ≻ 0,
and write Y_t = A_YY Y_{t−1} + A_YR R_{t−1} + ε_{Y,t}. Dynamical dependence
is T(X → Y) = ½ log det Var(Y_t | Y⁻) / det Var(Y_t | X⁻) ([THEORY-257](../theory.d/THEORY-257.md),
[THEORY-733](../theory.d/THEORY-733.md)), and Var(Y_t | X⁻) = Σ_YY.

The predictor A_YY Y_{t−1} + A_YR E[R_{t−1} | Y⁻] uses only Y's past. Its
error is A_YR(R_{t−1} − E[R_{t−1} | Y⁻]) + ε_{Y,t}, and the two terms are
independent. So

Var(Y_t | Y⁻) ⪯ Σ_YY + A_YR Cov(R_{t−1} | Y⁻) A_YRᵀ
⪯ Σ_YY + A_YR C A_YRᵀ,

where C = Cov(R_{t−1} | Y_{t−1}) under the stationary law. The second step
holds because conditioning on less cannot shrink a Gaussian conditional
covariance. Since log det is monotone on positive definite matrices,

T(X → Y) ≤ ½ log det(I + Σ_YY⁻¹ A_YR C A_YRᵀ) ≤ ½ tr(Σ_YY⁻¹ A_YR C A_YRᵀ).

C ⪯ Π_RR, so for A_YR = εB with the rest fixed, T = O(ε²). The coupling out
of the block, A_RY, enters only through C and the stationary covariance.

**The check.** Random five-variable systems with a two-coordinate block,
twenty at each ε ∈ {0.2, 0.1, 0.05, 0.025}, with random noise
covariances, and the dependence computed from exact stationary
covariances. The bound held in all 80 cases. The ratio T/ε² stayed between
8.5 and 10.5 across the four values of ε, which is second order.

## What it does not say

- **Not about the block's aggregate.** The bound is for the block's full
  state. A sum over the block can be dependent even with no coupling into
  the block, if the block's internal dynamics do not close on the sum.
  That part is [CLAIM-386](CLAIM-386.md).
- **Not a reason to ask for weak coupling both ways.** Only the coupling
  into the block enters the bound. Near-decomposability's weak coupling in
  both directions is sufficient for a small bound, not necessary.
- **Not beyond linear Gaussian VAR(1).** For VAR(p) the same argument
  applies lag by lag and was not written out.
