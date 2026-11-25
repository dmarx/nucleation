---
number: 349
status: Proposed
formerly:
- CASE-tmpi9sds
title: 'Finite Markovian augmentation in linear VAR'
statement: >-
  Finite Markovian augmentation of a linear coarse variable, computed
  exactly in linear Gaussian VAR(1) models with vector coarse variables: the
  finite-lag error bound held on 400 random models, the Kalman augmentation
  was Markov with unchanged transfer entropy on 16, and the filter's rate
  exceeded the eliminated dynamics' spectral radius in 67 of 2,000, never
  with one eliminated variable
version: 1
standing: documented
kind: executed-study
tags:
- mathematics
- complex-systems
- probabilistic-modeling
date: '2026-11-22'
bears_on:
- QUESTION-222
illustrates:
- CLAIM-925
line:
- distributed-agency
- formal-apparatus
summary: >-
  Run on 2026-11-22 for [LEAD-084](../leads.d/LEAD-084.md) (scratch/studies/lead-084/, on the branch
  claude/lead-084-markov-augmentation). Every number comes from exact
  stationary covariances, with numpy and scipy, and 308 pytest checks
  pass. It checks [CLAIM-925](../claims.d/CLAIM-925.md)'s identities and bound, compares the
  minimal augmentation with the Mori–Zwanzig and Krylov sizes of
  [NOTE-989](../notes.d/NOTE-989.md), and tests whether the eliminated dynamics bound the rate. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-925 — new; the claim this study checks -->

# CASE-349: Finite Markovian augmentation in linear VAR

## The case

**The class.** X_{t+1} = AX_t + w_t, A stable, w ~ N(0, Σ), Σ ≻ 0;
Y = LX with m from 1 to n − 1 and n from 2 to 7; no observation noise.
Random A is Gaussian, rescaled to a spectral radius in [0.29, 0.97]. Σ is
either diagonal or a random full matrix. In the rate test, 30% of the
models are made non-normal by an upper-triangular similarity. The steady
filter is solved by scipy's algebraic Riccati solver on the reduced
filter of the eliminated variables, and agrees with plain iteration to
5 × 10⁻¹³.

**Results** (scratch/studies/lead-084/results.md):

1. **The finite-lag error and its bound** (400 models, p = 1, 2, 4, 8,
   12). The error of the p-lag regression, computed from block
   autocovariances alone, equals the Riccati recursion from the stationary
   prior to 7 × 10⁻¹⁵ relative. The excess over the whole-past error and
   the bound minus the excess are both positive semidefinite to round-off
   (−1.4 × 10⁻¹⁴). The ratio of excess to bound, in trace, has median
   0.75 and minimum 0.04.
2. **The exact augmentation** (four constructed models and twelve
   random ones). Y with k_min memory coordinates from the Kalman predictor
   is Markov: the defect max_k |C(k) − Ω^k C(0)|, in whitened coordinates,
   is at most 10⁻⁶ (10⁻¹¹ or less in 14 of 16). Dropping any one
   coordinate raises it to between 10⁻³ and 0.4. k_min is at most n − m
   throughout, equals it in the random models, and is 0 for
   [CLAIM-389](../claims.d/CLAIM-389.md)'s zero-memory pair and for a closed Y. It equals the Hankel
   rank of the Mori–Zwanzig memory kernels in all 16. [NOTE-989](../notes.d/NOTE-989.md)'s
   dynamically independent augmentation, the Krylov space of row(L),
   needs as many memory coordinates or more: n − m in every random model,
   and one where k_min is 0 for the zero-memory pair. The transfer entropy from X to the augmented
   state equals that to Y in every model, 0.120 nats for the zero-memory
   pair.
3. **The rate against the eliminated dynamics** (2,000 models). The
   filter's rate ρ(A_cl) exceeded ρ(A₂₂) in Mori's frame in 1,022 models,
   so the projected block's spectrum does not bound it. It exceeded ρ(Ã),
   the projection-invariant eliminated dynamics, in 67, 62 of them among
   the models not made non-normal, by a factor of up to 1.18. Ã was
   unstable in 552 models whose filter was stable. With one eliminated
   variable (937 models) there was no violation. ρ(A_cl) never exceeded
   the contraction factor c. For scalar Y the nonzero eigenvalues of A_cl
   matched the moving-average zeros of [CLAIM-398](../claims.d/CLAIM-398.md)'s ARMA form to
   2 × 10⁻¹⁴, on 50 models.
4. **Nilpotent eliminated dynamics.** For
   A = [[0.1, 0.3, −1], [0.6, 0, −0.7], [0.1, 0, 0]], Y = x₁, Σ = I, the
   memory kernel is 0.08 and −0.021 at lags 1 and 2 and zero beyond, and
   ρ(Ã) = 0. The excess error at p = 1, 2, 3, 4, 6 is 7.9 × 10⁻³,
   1.5 × 10⁻³, 1.5 × 10⁻⁵, 1.5 × 10⁻⁷ and 1.4 × 10⁻¹¹, falling at
   ρ(A_cl)² = 0.0994².
5. **Weak inward coupling.** In a three-variable model with A₁₂ = ε, as ε
   falls from 0.4 to 0.025, ρ(A_cl) rises from 0.600 to 0.678, towards
   ρ(Ã) = 0.678, and the excess error at p = 3 over ε² settles near 0.08.
6. **[QUESTION-222](../questions.d/QUESTION-222.md)'s own example,** ẋ = −x + y, ẏ = 0.2x − 0.3y,
   with unit white noise, sampled exactly at h = 0.1. The filter's rate is
   0.9009 a step, about e^{−1.04t}, which is the moving-average zero. The
   eliminated variable's own rate is 0.971, about e^{−0.3t}, the memory
   kernel's. The whole-past error is 0.0975. The excess error of p lags is
   7.9 × 10⁻⁵ at p = 1, 1.2 × 10⁻⁵ at p = 10 and 2.3 × 10⁻⁸ at p = 40,
   each about a tenth of the bound. Truncating Y's own history converges
   faster than the memory kernel decays.

## What it can show

That the bound and the identities of [CLAIM-925](../claims.d/CLAIM-925.md) hold numerically
across the class, that the eliminated block's spectrum, in either form,
does not bound the rate in general, and that k_min matched the
Mori–Zwanzig Hankel rank on every model tried. It is documented: the
study's README reruns it in about ten seconds.

It cannot show that k_min always equals the Hankel rank, which would
need a proof. Ranks were read with a relative tolerance of 10⁻¹², and
generic random models can have Hankel singular values near it, so the
random models of item 2 were drawn with spectral radius 0.9. It says
nothing about observation noise, VAR(p), or nonlinear classes.
