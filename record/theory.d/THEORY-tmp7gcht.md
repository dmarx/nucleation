---
status: Active
title: "Near a non-degenerate minimum, constant-rate SGD's stationary distribution is a Gaussian set by learning rate, batch size and preconditioner, which can be tuned to match the posterior at a given sample size; training time enters only as the wait for stationarity"
version: 1
tags:
- learning-theory
- probabilistic-modeling
date: '2026-10-31'
source:
- LIT-tmpwzrx7
- LIT-tmpxo5z5
summary: >-
  Mandt, Hoffman and Blei (2017, [LIT-tmpwzrx7](../literature.d/LIT-tmpwzrx7.md); first in 2016, [LIT-tmpxo5z5](../literature.d/LIT-tmpxo5z5.md)),
  read in [NOTE-tmpiaa2o](../notes.d/NOTE-tmpiaa2o.md) and [NOTE-tmph1our](../notes.d/NOTE-tmph1our.md). Under Gaussian, constant
  gradient noise BBᵀ, the continuous-time limit and a quadratic loss with
  positive-definite Hessian A, the stationary covariance solves
  AΣ + ΣA = (ε/S)BBᵀ; the preconditioner (2S/εN)(BBᵀ)⁻¹ makes it the
  posterior's A⁻¹/N exactly. Checked numerically. Active as a result about
  that model. It does not cover singular posteriors, several basins or the
  search phase, and it relates the optimiser's noise scale to sample size,
  not training time to sample size.
---
<!-- inactive-ok-file: QUESTION-tmpiir0l THEORY-209 THEORY-tmp8ggnh — Open or Proposed; the question this bears on, Kunin's deep-network reading, and the sibling filed from the same reading -->

# THEORY-tmp7gcht: Near a non-degenerate minimum, constant-rate SGD's stationary distribution is a Gaussian set by learning rate, batch size and preconditioner, which can be tuned to match the posterior at a given sample size; training time enters only as the wait for stationarity

## Source

Mandt, Hoffman and Blei (2017), [LIT-tmpwzrx7](../literature.d/LIT-tmpwzrx7.md), §§3–4 and Appendices B and
D of arXiv 1704.04289v2 (JMLR 18, pp. 6–14, 27–29); read in [NOTE-tmpiaa2o](../notes.d/NOTE-tmpiaa2o.md).
The same Theorems 1–2 first appear in Mandt, Hoffman and Blei (2016),
[LIT-tmpxo5z5](../literature.d/LIT-tmpxo5z5.md), read in [NOTE-tmph1our](../notes.d/NOTE-tmph1our.md).

## What was actually shown

**The model.** SGD with rate ε, batch S and preconditioner H on a loss
L = (1/N)Σℓ_n is approximated, under four assumptions, by the OU process
dθ = −HAθ dt + √(ε/S) HB dW:

1. gradient noise Gaussian with covariance C(θ)/S;
2. C(θ) ≈ BBᵀ constant near the optimum;
3. the continuous-time limit;
4. L = ½θᵀAθ with A positive definite, so the posterior is
   f ∝ exp(−(N/2)θᵀAθ).

**The stationary law.** N(0, Σ) with HAΣ + ΣAH = (ε/S)HBBᵀH (Eq. 13,
App. B), so Σ scales with ε/S.

**Matching a posterior.** Minimising KL(q‖f) over the settings gives
ε* = 2SD/(N tr BBᵀ) for a scalar rate (Theorem 1), H* = (2S/εN)(BBᵀ)⁻¹
for a full preconditioner (Theorem 2), and with H* the stationary law is
the posterior, Σ = A⁻¹/N (Corollary 4). With momentum, damping μ rescales
the noise to ε/(μS) and leaves the shape alone (Eq. 25).

**Checks ([NOTE-tmpiaa2o](../notes.d/NOTE-tmpiaa2o.md)).** For random 4 × 4 A and BBᵀ: direct numerical
minimisation of the KL over ε agrees with Theorem 1 to 10⁻⁶ relative;
Corollary 4 holds to 10⁻¹⁷; with H = h(BBᵀ)⁻¹ the stationary covariance is
exactly A⁻¹/N_eff with N_eff = 2S/(εh), so the preconditioner's scale is
an effective sample size; Eq. 25 against the exact stationary covariance
of the discrete momentum recursion is within 0.07% to 4%, falling with ε;
the discrete SGD covariance is within 5% of Eq. 13 at ε = 5 × 10⁻³.

**What could have failed.** The KL might have had no closed-form optimum
because Σ depends on ε, S and H implicitly. The trace identity
tr(AΣ) = (ε/2S)tr(BBᵀ) removes the dependence, and the optimum is exact.

**The reading it supports.** In this regime the optimiser's noise scale
does what sample size does in the posterior: ε/S (with the preconditioner)
sets a covariance, and choosing it picks the sample size whose Gaussian
posterior the stationary law matches. With a scalar rate the shape matches
only when BBᵀ ∝ A; under Assumption 5 (BBᵀ = A) the stationary covariance
is ε/(2S)·I, isotropic, while the posterior's is A⁻¹/N.

## What this does not say

- **Anything about singular models.** Assumption 4 requires a
  positive-definite Hessian. The posterior here is Gaussian and has no
  phases; a singular learning theory posterior, whose dominant region
  changes with n ([THEORY-087](THEORY-087.md)), is outside the result.
- **Anything about several basins.** The model is linearised at one
  optimum. Which basin SGD occupies, and how long it stays, the paper
  leaves to Kramers' escape-time argument, in one sentence (p. 7).
- **Anything about the transient.** The authors call the search phase the
  one in which "assumptions 1–4 are often violated and it is hard to say
  anything general" (p. 8). Training time enters only as the time to reach
  stationarity. So the result does not map training time to sample size;
  it maps noise scale to sample size. The one examples-to-sample-size
  correspondence in the paper is iterate averaging, [THEORY-tmp8ggnh](THEORY-tmp8ggnh.md).
- **That deep networks meet the assumptions.** The experiments are linear,
  logistic and softmax regression. Whether converged deep networks are in
  such a state is [THEORY-209](THEORY-209.md)'s question.
- **That constant-rate SGD without preconditioning matches the posterior.**
  It matches its scale, not its shape, unless the noise covariance is
  proportional to the Hessian (Table 1: KL 18.7 against 0.7 for full
  preconditioning on wine).

## Connections

[THEORY-779](THEORY-779.md) is the same calculation with momentum, noise ∝ Hessian and
weight decay, from Kunin et al.; its λ → 0 isotropy is this account's
Assumption 5 case with μ = 1 − β. McCandlish et al.'s temperature ε/B
([NOTE-293](../notes.d/NOTE-293.md), App. C) uses this stationary model.
