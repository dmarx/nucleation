---
status: Active
title: 'In overparameterized linear regression, iterated self-training with fresh covariates, noiseless pseudo-labels and minimum-norm students applies a fresh random orthogonal projection to the estimate each round, so noise from the first fit decays geometrically while signal along a direction of variance s decays at the slower rate s/(s + τ); risk is U-shaped under anisotropy and monotone under isotropy, tends to the risk of predicting zero, and every student fits its teacher exactly on its own sample'
version: 1
tags:
- learning-theory
- mathematical-statistics
date: '2026-10-31'
source:
- LIT-tmpcewsq
summary: >-
  Wu, Yang and Sun (2026), LIT-tmpcewsq, Theorem 3.2, Corollaries 3.3–3.4
  and B.1, and the projection identity of §3.2; read in NOTE-tmpbslp3 and
  checked by Monte Carlo in the spiked model. Active for the spiked
  closed form; the general concentration result (Theorem 4.2) is the
  paper's, proof not checked. It does not cover reused data, noise
  injected every round, or nonlinear students.
---

# THEORY-tmpp515i: In overparameterized linear regression, iterated self-training with fresh covariates, noiseless pseudo-labels and minimum-norm students applies a fresh random orthogonal projection to the estimate each round, so noise from the first fit decays geometrically while signal along a direction of variance s decays at the slower rate s/(s + τ); risk is U-shaped under anisotropy and monotone under isotropy, tends to the risk of predicting zero, and every student fits its teacher exactly on its own sample

## Source

Wu, Yang and Sun (2026), LIT-tmpcewsq, §§3–4 and Appendix B, pp. 3–7 and
11–12 of arXiv 2602.14029v1; read in NOTE-tmpbslp3.

## What was actually shown

With p > n_t, the minimum-norm fit to Y_t = X_t β̂_{t−1} is
β̂_t = (X_t⊤X_t)⁺X_t⊤X_t β̂_{t−1} = P_t β̂_{t−1}, with P_t the orthogonal
projection onto the row space of the fresh design X_t (§3.2). Under a
single spike Σ = (s − 1)u₁u₁⊤ + I with β = r u₁ and τ = p/n − 1, the
limiting risk is B*_t + V*_t, with B*_t = r²s(1 − (s/(s + τ))^{t+1})² and
V*_t = V*_{t−1}/(1 + τ) + τr²s^{2t+1}/(s + τ)^{2(t+1)} (Theorem 3.2). As
t → ∞, B*_t → r²s, the risk of β̂ = 0, and V*_t → 0. With s = 1 the risk is
monotone in t (Corollary B.1). With several spikes each direction is
filtered at its own rate s_j/(s_j + τ) (Theorem 3.6).

Checked by Monte Carlo (n = 400, p = 800, s = 5, r = σ = 1, six trials):
the simulated risk was 1.25, 1.10, 1.32, 1.62, 1.98, 2.33, 2.72, 3.05 over
t = 0–7, against 1.28, 1.13, 1.29, 1.59, 1.94, 2.31, 2.66, 2.99 from the
formula. Each student's residual on its own pseudo-labels was 10⁻¹⁴.

What could have failed: the strong direction could have been lost as fast
as the noise, giving monotone growth; or the projections could have
preserved the teacher, giving no change.

## What this does not say

- **That projection as such loses information on repetition.** A single
  P_t is idempotent: with the design reused, the estimate stops changing
  after one round, and with p ≤ n_t it never changes (§3.2). The loss
  comes from drawing a new subspace each round.
- **That self-training is safe if stopped early in general.** The optimal
  round depends on the spectrum and the noise; the iterated GCV that finds
  it is proved for this model only.
- **Anything about noise entering every round.** That is model collapse,
  where error grows (THEORY-289); here noise enters once.
- **That deep networks follow it.** One CIFAR-10 experiment of four rounds
  is suggestive only.
- **That a student which agrees with its teacher on its data agrees
  with it elsewhere.** It does not: exact agreement on n_t points fixes
  only an n_t-dimensional part of a p-dimensional estimate.
