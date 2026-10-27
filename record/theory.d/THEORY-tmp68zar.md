---
status: Active
title: 'In a model that fits y = Σ v_i x_i² with ỹ = Σ_r (W_r·x)² + b, on independent inputs of zero mean, unit variance and common fourth moment k, the expected squared error at the optimal bias is (k − 1)Σ(n_i − v_i)² − 2Σn_i² + 2Σn_i²/C_i, in the squared embedding lengths n_i and capacities C_i = (w_i·w_i)²/Σ_j(w_i·w_j)², and its minimum with the capacities summing to the number of neurons D gives C_i = clip((k − 1)v_i/((k − 3)λ) − 2/(k − 3), 0, 1): for k ≤ 3 each feature is given a whole dimension or none, and for k > 3 a feature is shared between neurons exactly when 2λ/(k − 1) < v_i < λ'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-tmp8m63d, the reading of Scherlis et al.
    (2022) in full. Re-derived step by step below from the model's
    definition, and checked numerically on 2026-10-27: a Monte Carlo
    estimate of the loss (3,000,000 sparse uniform samples, six features,
    three neurons, k = 6) gave 295.7 against 295.9 from both closed
    forms, the capacities summed to at most D, and a numerical solution
    of the allocation for N = 6, D = 3, k = 10 matched the closed-form
    λ and C_1 of §3.5.2 at every importance tried inside the shared
    phase, with the thresholds 1.875 and 0.323 bounding it. A
    demonstrated result within its model, with its conditions in the
    title (ADR-043; ADR-047 on re-derivation). The authors' wider
    account is THEORY-tmp2tsxo, Proposed.
tags:
- representation-learning
date: '2026-10-27'
source:
- LIT-tmp9yvin
summary: >-
  Scherlis et al. (2022), LIT-tmp9yvin, read in NOTE-tmp8m63d: the
  quadratic toy model of superposition solved in closed form. Its loss
  separates by feature through capacity, so the marginal value of
  capacity is −∂L/∂C_i = 2n_i²/C_i², and sparsity, through k, decides
  whether returns to capacity diminish. It is the model the causal
  scrubbing appendix's §6 analyses. It holds for this model and says
  nothing directly about trained networks.
---
<!-- inactive-ok-file: THEORY-tmp2tsxo — Proposed; the authors' wider account, cited as open -->
# THEORY-tmp68zar: In a model that fits y = Σ v_i x_i² with ỹ = Σ_r (W_r·x)² + b, on independent inputs of zero mean, unit variance and common fourth moment k, the expected squared error at the optimal bias is (k − 1)Σ(n_i − v_i)² − 2Σn_i² + 2Σn_i²/C_i, in the squared embedding lengths n_i and capacities C_i = (w_i·w_i)²/Σ_j(w_i·w_j)², and its minimum with the capacities summing to the number of neurons D gives C_i = clip((k − 1)v_i/((k − 3)λ) − 2/(k − 3), 0, 1): for k ≤ 3 each feature is given a whole dimension or none, and for k > 3 a feature is shared between neurons exactly when 2λ/(k − 1) < v_i < λ

## Source

Scherlis, Sachan, Jermyn, Benton and Shlegeris (2022), *Polysemanticity
and Capacity in Neural Networks*, arXiv 2210.01892 v4, LIT-tmp9yvin, read
in full in NOTE-tmp8m63d: §3 and Appendices A and C, with the capacity
bound of Appendix F and the feasibility result of Appendix H.

## What was actually shown

**The derivation, re-done.** Write A = WᵀW, so ỹ = xᵀAx + b, and
M = A − diag(v), so ỹ − y = xᵀMx + b.

1. For independent x_i with mean 0, variance 1 and fourth moment k,
   E[xᵀMx] = tr M and Var[xᵀMx] = (k − 1)Σ_i M_ii² + 2Σ_{i≠j} M_ij². The
   optimal b is −tr M, leaving
   E[L] = (k − 1)Σ_i(n_i − v_i)² + 2Σ_{i≠j}(w_i·w_j)², with n_i = A_ii
   (the paper's eq. 12).
2. By the definition of capacity, Σ_j(w_i·w_j)² = n_i²/C_i, so
   Σ_{j≠i}(w_i·w_j)² = n_i²/C_i − n_i², which gives the title's form
   (eq. 13).
3. At fixed C, ∂L/∂n_i = 2(k − 1)(n_i − v_i) − 4n_i + 4n_i/C_i = 0, so
   n_i = (k − 1)v_i/((k − 3) + 2/C_i). Since n is optimal for every C,
   dL/dC_i = ∂L/∂C_i = −2n_i²/C_i² (eq. 14), never positive, so the
   capacities saturate their bound, Σ C_i = D.
4. An interior optimum has a common value of n_i/C_i; call it λ (the
   paper's λ in eq. 15, which is √(λ₄/2) for the multiplier λ₄ of its
   eq. 4). Substituting n_i = λC_i in step 3 gives
   C_i = (k − 1)v_i/((k − 3)λ) − 2/(k − 3), clipped to [0, 1] at the
   corners, with λ fixed by Σ C_i = D.
5. For k > 3, C_i ≤ 0 when v_i ≤ 2λ/(k − 1) and C_i ≥ 1 when v_i ≥ λ. For
   k < 3 the expression decreases in v_i and the loss is concave in each
   C_i (−2n_i²/C_i² rises in magnitude with C_i), so the optimum is at
   corners: the D most important features get a dimension each.
6. The allocation is realizable: any C with 0 ≤ C_i ≤ 1 and Σ C_i = D is
   the capacity vector of a semiorthogonal W (Theorem 1), for which
   n_i ∝ C_i, and columns can be rescaled to set the constant.

**The numerical check.** Described in the history note: the loss formula
against Monte Carlo, and the allocation against a numerical solution.

**What could have come out otherwise.** The interference term need not
have reduced to a function of each feature's own capacity, and then the
allocation would not separate. The fourth moment could have entered the
two terms alike, leaving sparsity no effect on sharing.

## What this does not say

- **Not about trained networks.** One hidden layer, a scalar target that
  is a sum of squares, a quadratic activation, independent features.
- **Not about ReLU or GeLU models,** which the paper treats only
  numerically, in figures.
- **Not that a shared feature is polysemantic in every basis by this
  result alone.** That is the geometry of §4: this model's solution is a
  single block, which is polysemantic in any basis.

## Connections

- **LIT-1583 (§6) and NOTE-1202.** The appendix's two-feature,
  one-neuron case: with a = b, v₁ = v₂ = 1, D = 1 and N = 2, step 4 gives
  C₁ = C₂ = 1/2 and λ = 2(k − 1)/(k + 1), and v = 1 < λ exactly when
  k > 3, so equal features of high kurtosis share the neuron, as the
  appendix states.
- **LIT-323.** Elhage et al.'s observation that sparser inputs give more
  superposition, derived here for this model through k.
