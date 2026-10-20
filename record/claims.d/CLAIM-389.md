---
number: 389
status: Active
formerly:
- CLAIM-tmpmonrv
title: 'In a stable linear Gaussian VAR(1), exact dynamical independence of a linear coarse-graining implies that its Mori–Zwanzig memory vanishes, but not conversely: memory needs coupling out of the coarse variable and back, and dependence needs only the way back, so a coarse variable can be Markov in its own law with zero memory and still be dynamically dependent'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation, or in the counterexample: a check showing
  that for A = [[0.5, 0.4], [0, 0.3]], Σ = I − AAᵀ and Y = X₁ either some
  memory kernel K₁₂K₂₂^(j−1)K₂₁ is non-zero or the transfer entropy from X
  to Y is zero.
tags:
- complex-systems
- information-theory
- mathematics
date: '2026-10-20'
line:
- distributed-agency
- formal-apparatus
answers:
- QUESTION-222
grounds:
- THEORY-733
- LIT-1245
summary: >-
  Derived in the reading of Chorin, Hald and Kupferman (2000),
  [NOTE-989](../notes.d/NOTE-989.md), and re-checked here. It settles, for the linear Gaussian
  VAR(1) class, the relation [QUESTION-222](../questions.d/QUESTION-222.md) left open between memory in
  the reduced dynamics and [THEORY-257](../theory.d/THEORY-257.md)'s dynamical independence: memory is
  the round trip Y → rest → Y, dependence the inward leg alone. Not about
  VAR(p ≥ 2), where the reading reports that an independent variable can
  carry memory, nor about nonlinear systems.
supports:
- CLAIM-tmp5fx5d
---
<!-- inactive-ok-file: THEORY-257 — Proposed; the account whose criterion this relates to memory, open -->
# CLAIM-389: In a stable linear Gaussian VAR(1), exact dynamical independence of a linear coarse-graining implies that its Mori–Zwanzig memory vanishes, but not conversely: memory needs coupling out of the coarse variable and back, and dependence needs only the way back, so a coarse variable can be Markov in its own law with zero memory and still be dynamically dependent

## The claim

Take X_t = AX_{t−1} + ε_t, stable, ε_t ~ N(0, Σ), Σ ≻ 0, with stationary
covariance Π, and a linear coarse-graining Y = LX with row space W. Work
with linear functionals of the state in L²(Π), where the transition
operator acts as Aᵀ and Mori's projection is the Π-orthogonal projection
onto W. Split Aᵀ into blocks: K₁₁ (W → W), K₂₁ (W → W⊥), K₁₂ (W⊥ → W) and
K₂₂ (W⊥ → W⊥). The discrete-time Mori–Zwanzig decomposition then has
memory kernels M_j = K₁₂K₂₂^(j−1)K₂₁, j ≥ 1 ([NOTE-989](../notes.d/NOTE-989.md)).

- **Independence ⇒ no memory.** By [THEORY-733](../theory.d/THEORY-733.md), Y is exactly
  dynamically independent iff W is invariant under Aᵀ, that is iff
  K₂₁ = 0. Then every M_j = 0.
- **No memory ⇏ independence.** A = [[0.5, 0.4], [0, 0.3]],
  Σ = I − AAᵀ (positive definite), Y = X₁. Then Π = I, so the blocks are
  read directly off Aᵀ: K₂₁ = 0.4 and K₁₂ = 0, and every M_j = 0. Y's
  autocovariance is 0.5ᵗ, so in its own law Y is an AR(1), Markov. Yet X₂
  enters Y_t with coefficient 0.4 and is uncorrelated with Y's whole past
  (Cov(X_{t−1}, X_{t−1−k}) = A^k has a zero (2, 1) entry). So
  T(X → Y) = ½ ln(Var(Y_t|Y⁻)/Σ₁₁) = ½ ln(0.75/0.59) = 0.120 nats. That
  was re-checked from the exact stationary covariances (0.1200).

In words: memory is information that leaves the coarse variable and comes
back to it. Dependence is information that arrives from outside, whether or
not it started inside. A coarse variable can receive news it never sent.

## What it does not say

- **Nothing for VAR(p ≥ 2) or for state-space models.** The reading
  reports that there an exactly independent variable can carry memory
  ([THEORY-733](../theory.d/THEORY-733.md)'s criterion constrains every lag, and the lags mix inside
  W). That was not re-checked here.
- **That zero memory is common.** It is not generic; the reading found it
  in none of 200 random models.
- **Anything about nonlinear projections.** For a deterministic flow with
  an invariant measure, the reading derives that zero memory, zero noise
  and exact closure coincide. That is a different statement, with no noise
  injected from outside, and it is recorded in the NOTE, not here.

## Note of 2026-10-20: why "not conversely"

For any scalar stationary process, Mori's memory for the projection onto
the current value is a functional of the process's own autocovariance, and
vanishes iff that autocovariance is geometric ([CLAIM-tmp511ss](CLAIM-tmp511ss.md), from the
reading of Lin and Lu, [NOTE-tmpqnsb1](../notes.d/NOTE-tmpqnsb1.md)). Memory is a property of Y's own law;
dependence is a property of its joint law with the rest of the system. So
no memory measure can detect dependence, which is the structural reason
the converse fails.
