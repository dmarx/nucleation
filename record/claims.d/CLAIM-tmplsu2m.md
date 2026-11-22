---
status: Proposed
title: 'In a stable linear Gaussian VAR(1) with a linear coarse variable of any dimension m observed without noise, the Kalman filter of the eliminated variables is an exact Markovian augmentation with at most n − m memory coordinates, and keeping only the last p values of the coarse variable costs an excess error bounded by L A_clᵖ(Π − P∞)A_clᵖᵀLᵀ; the rate is the filter''s closed loop, which the eliminated dynamics bound when one variable is eliminated and not in general'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a stable VAR(1) with Σ ≻ 0 and a full-rank
  L for which the one-step error of predicting Y from its last p values
  falls below the whole-past error or exceeds the stated bound, or for
  which Y together with the filter's estimate of the eliminated variables
  is not Markov, or for which augmenting Y with that estimate changes the
  transfer entropy from X.
tags:
- complex-systems
- mathematics
- probabilistic-modeling
- information-theory
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
bears_on:
- QUESTION-222
complements:
- CLAIM-398
summary: >-
  Derived for [LEAD-084](../leads.d/LEAD-084.md) and checked with numpy (scratch/studies/lead-084/,
  308 pytest checks; the study is [CASE-tmpi9sds](../cases.d/CASE-tmpi9sds.md)). It extends [CLAIM-398](CLAIM-398.md)
  from a scalar to a vector coarse variable and adds what that claim left
  out: an error bound for keeping finitely many lags. The bound's rate is
  the closed loop of the Kalman filter, whose eigenvalues are the zeros of
  Y's minimum-phase spectral factor. It is bounded by the eliminated
  dynamics when n − m = 1, and a three-variable model with nilpotent
  eliminated dynamics shows it is not in general. The augmentation leaves
  the transfer entropy from X to Y unchanged. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-257 — Proposed; the account whose criterion the transfer-entropy result bears on, nothing here rests on it -->
<!-- inactive-ok-file: CASE-tmpi9sds — new; the numerical study filed with this claim -->

# CLAIM-tmplsu2m: In a stable linear Gaussian VAR(1) with a linear coarse variable of any dimension m observed without noise, the Kalman filter of the eliminated variables is an exact Markovian augmentation with at most n − m memory coordinates, and keeping only the last p values of the coarse variable costs an excess error bounded by L A_clᵖ(Π − P∞)A_clᵖᵀLᵀ; the rate is the filter's closed loop, which the eliminated dynamics bound when one variable is eliminated and not in general

## The claim

**Setting.** X_{t+1} = AX_t + w_t on ℝⁿ, A stable, w_t ~ N(0, Σ) i.i.d.,
Σ ≻ 0, and Y_t = LX_t with L of full row rank m < n. Π is the stationary
covariance. P_p = Cov(X_{t+1} | Y_t, …, Y_{t−p+1}), and P∞ is its limit,
the error of predicting from Y's whole past. Choose any complement R = NX,
so that X ↔ (Y, R), and write A and Σ in blocks.

**1. An exact augmentation, with at most n − m coordinates.** Let
r̂_t = E[R_t | Y_{≤t}], the Kalman filter of the eliminated variables.
Since Y_t is known exactly, E[X_t | Y_{≤t}] is a linear function of
(Y_t, r̂_t), and so is the predictive state x̂_{t+1|t} = AE[X_t | Y_{≤t}].
Then Z_t = (Y_t, r̂_t) is Markov:
Y_{t+1} = Lx̂_{t+1|t} + e_{t+1}, with e_{t+1} the innovation, independent
of the past, and r̂_{t+1} is a linear function of (Z_t, e_{t+1}). Its
one-step error is the whole-past error LP∞Lᵀ. The fewest linear memory
coordinates that do the same is
k_min = rank Cov(O x̂_{t+1|t} | Y_t) ≤ n − m, with O = [L; LA; …; LAⁿ⁻¹].
Fewer cannot determine the conditional law of Y's future, and the range
of that covariance, read off O x̂_{t+1|t}, suffices because the
unobservable subspace is A-invariant. In the linear Gaussian case,
then, the augmentation the question asks for is the Kalman filter.

**2. Keeping p lags: the error and its bound.** Under stationarity the
best predictor from the last p values of Y is the Kalman filter started
p steps back from the prior N(0, Π), so P_p is the Riccati recursion
from P₀ = Π. Let K = AP∞Lᵀ(LP∞Lᵀ)⁻¹ and A_cl = A − KL. With exact
observations of Y, P∞ = A_cl P∞ A_clᵀ + Σ. The predictor with the fixed
gain K, started at the prior, has error e_{k+1} = A_cl e_k + w_k, so its
covariance after p steps is P∞ + A_clᵖ(Π − P∞)A_clᵖᵀ. The optimal p-lag
predictor does no worse, and no better than the whole past. So

0 ⪯ LP_pLᵀ − LP∞Lᵀ ⪯ L A_clᵖ (Π − P∞) A_clᵖᵀ Lᵀ.

This is an augmentation by k = m(p − 1) coordinates, the past values,
with its excess error falling as ρ(A_cl)^{2p} up to a polynomial factor.

**3. What sets the rate.** A_cl has m zero eigenvalues. Its others are
those of the reduced filter of R, Ã(I − K_f A₁₂), where
Ã = A₂₂ − Σ₂₁Σ₁₁⁻¹A₁₂ is the eliminated dynamics with Y's innovation
regressed out. Ã is the same for every complement R, while A₂₂ is not.
By the matrix inversion lemma, the eigenvalues of A_cl are the zeros of
the minimum-phase spectral factor I + L(zI − A)⁻¹K of Y. For scalar Y they
are the moving-average zeros of [CLAIM-398](CLAIM-398.md)'s ARMA form, which explains
that claim's observation that its truncation rate was set by the
moving-average zero. Then:

- **One eliminated variable (n − m = 1).** By Sherman–Morrison,
  a_cl = ã / (1 + P_R A₁₂ᵀΣ₁₁⁻¹A₁₂), so |a_cl| ≤ |ã|. The eliminated
  dynamics bound the rate, and coupling into Y makes it faster.
- **In general, a contraction.** With P_R the steady Cov(R_t | Y_{≤t}) ≻ 0
  and Q = Σ₂₂ − Σ₂₁Σ₁₁⁻¹Σ₁₂, the reduced closed loop is
  ÃP_fP_R⁻¹, and in the norm |P_R^{−1/2}v| it contracts by
  c = (1 − λ_min(P_R⁻¹Q))^{1/2}. So ρ(A_cl) ≤ c < 1.
- **Not bounded by the eliminated spectrum.** With
  A = [[0.1, 0.3, −1], [0.6, 0, −0.7], [0.1, 0, 0]], Y = x₁ and Σ = I,
  Ã = A₂₂ = [[0, −0.7], [0, 0]] is nilpotent, and the memory kernel
  A₁₂A₂₂^{j−1}A₂₁ is zero beyond lag 2. Yet ρ(A_cl) = 0.0994, and the
  excess error of p lags is positive for every p, falling by 0.0994² a
  step. A finite memory kernel does not make Y a finite autoregression,
  because the eliminated variables also feed Y noise that Y's own past
  can only reconstruct approximately.
- **Weak inward coupling.** As A₁₂ → 0, A_cl → Ã and the excess error is
  O(|A₁₂|²).

**4. The augmentation leaves dynamical dependence unchanged.** Z's past
and Y's past generate the same information, and Z_{t+1} adds to Z's past
only Y_{t+1}'s innovation. So
T(X → Z) = I(Z_{t+1}; X_{≤t} | Z_{≤t}) = T(X → Y)
= ½ log det(LP∞Lᵀ) / det(LΣLᵀ). The Kalman augmentation makes Y Markov
in its own law. It does not make it any more or less dynamically
independent in [THEORY-257](../theory.d/THEORY-257.md)'s sense, which already conditions on Y's
history.

## What it does not say

- **Not beyond the linear Gaussian VAR(1) with noiseless Y.** The
  Riccati and fixed-gain argument carries over to observation noise and
  to VAR(p) in companion form, but that is not checked here. Nonlinear
  classes are untouched.
- **Not a bound in terms of the eliminated spectrum in general.** The
  rate is that of the filter, which depends on the coupling and the noise
  as well. Only the case n − m = 1 and the weak-coupling limit tie it to
  Ã. The contraction factor c is computable but depends on P_R.
- **Not that k_min equals the Hankel rank of the Mori–Zwanzig memory.**
  [NOTE-989](../notes.d/NOTE-989.md) gives that rank as the size of an augmentation that makes
  Y's law Markov. The two agreed on all 16 models in the study, but no
  proof is offered here.
- **No ruling on levels.** Item 4 shows that the dynamical-independence
  verdict is the same for the augmented state and for Y with its history.
  Whether the record's level criteria should be applied to the augmented
  state or to the instantaneous one is still open.
