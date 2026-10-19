---
number: 738
status: Active
formerly:
- THEORY-tmpbyp9v
title: 'In the unconstrained-features max-margin problem with k classes under step imbalance and feature dimension at least k − 1, the unique optimal logits are the simplex-encoded labels, every margin equals one, and the classifier and embedding Gram matrices are the two square-root factors of that matrix''s singular value decomposition; the geometry is the simplex equiangular tight frame exactly when the classes are balanced or there are two of them'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-286 and filed Active at the owner's direction,
    carrying out the promotion audit's decision for THEORY-286 (batch 024,
    ADR-047). THEORY-286 joined this proved geometry to a conjecture that
    gradient descent reaches it and to single-seed measurements of trained
    networks. This THEORY holds LIT-994's Theorem 1 and Corollary 1.3. NOTE-764
    followed that proof only as sketched, so it was re-derived for the
    split, by a dual certificate written out below (ADR-047 v2). THEORY-286
    keeps the rest and extends this one.
tags:
- representation-learning
- learning-theory
- mathematics
date: '2026-10-19'
source:
- LIT-994
summary: >-
  Thrampoulidis, Kini, Vakilian and Behnia (2022), [LIT-994](../literature.d/LIT-994.md), Theorem 1 and
  Corollary 1.3, read in [NOTE-764](../notes.d/NOTE-764.md) and re-derived here. By [THEORY-726](THEORY-726.md) the
  problem is nuclear-norm minimisation of the logits under margin
  constraints. The polar factor of the simplex-encoded label matrix
  certifies it optimal, because under step imbalance its off-diagonal
  entries are negative. It does not say that gradient descent or trained
  networks reach this geometry, which is [THEORY-286](THEORY-286.md)'s.
extended_by:
- THEORY-286
---
<!-- inactive-ok-file: THEORY-286 — Proposed; the account this core was split from and that extends it, cited as open -->

# THEORY-738: In the unconstrained-features max-margin problem with k classes under step imbalance and feature dimension at least k − 1, the unique optimal logits are the simplex-encoded labels, every margin equals one, and the classifier and embedding Gram matrices are the two square-root factors of that matrix's singular value decomposition; the geometry is the simplex equiangular tight frame exactly when the classes are balanced or there are two of them

## Source

Thrampoulidis, Kini, Vakilian and Behnia (2022, NeurIPS), [LIT-994](../literature.d/LIT-994.md),
Theorem 1 and Corollary 1.3, read in [NOTE-764](../notes.d/NOTE-764.md). The re-derivation below
uses a dual certificate, not the paper's own route.

## What was actually shown

**Setup.** The problem is min ½‖W‖²_F + ½‖H‖²_F subject to
(w_{y_i} − w_c)ᵀh_i ≥ 1 for every sample i and class c ≠ y_i, with
W ∈ ℝ^{d×k}, H ∈ ℝ^{d×n} and d ≥ k − 1. Under step imbalance a classes
(set A) have Rm samples each and b classes (set B) have m, a + b = k. The
simplex-encoded label matrix is Ẑ = PY, with P = I − J/k and Y the
one-hot label matrix, so every column of class c is e_c − 1/k.

1. **Reduction.** For logits X = WᵀH, the least ½(‖W‖² + ‖H‖²) over
   factorisations is ‖X‖_* when d ≥ rank X ([THEORY-726](THEORY-726.md)), and every
   minimiser is balanced ([CLAIM-148](../claims.d/CLAIM-148.md)). So the problem is min ‖X‖_* subject
   to X[y_i, i] − X[c, i] ≥ 1. Ẑ is feasible, with every margin exactly 1.
2. **Certificate.** Let G = (ẐẐᵀ)^{+1/2} Ẑ, the polar factor of Ẑ. Then
   ‖G‖_op = 1 and ⟨G, Ẑ⟩ = ‖Ẑ‖_*. With D = diag(n_c), ẐẐᵀ = PDP, and
   M = (PDP)^{+1/2} annihilates the all-ones vector, so the column of G for
   class c is M e_c. If M's off-diagonal entries are negative, each column
   g of G (which sums to zero) is Σ_{c'≠c} μ_{c'}(e_c − e_{c'}) with
   μ_{c'} = −g[c'] > 0. Then for any feasible X,
   ⟨G, X⟩ = Σ μ × (margins of X) ≥ Σ μ = ⟨G, Ẑ⟩, and so
   ‖X‖_* ≥ ⟨G, X⟩ ≥ ⟨G, Ẑ⟩ = ‖Ẑ‖_*.
3. **Signs.** PDP has eigenvalue Rm on zero-sum vectors supported on A,
   m on zero-sum vectors supported on B, and λ_u = m(Rb + a)/k on
   u = 1_A/a − 1_B/b, with ‖u‖² = k/(ab). So
   M = Π_A/√(Rm) + Π_B/√m + uuᵀ/(‖u‖²√λ_u), where Π_A and Π_B project onto
   zero-sum vectors supported on A and B. Its off-diagonal entries are:
   within A, −1/(a√(Rm)) + b/(ak√λ_u), negative because b²R < kRb + ka;
   within B, −1/(b√m) + a/(bk√λ_u), negative because a² < kRb + ka; and
   across, −1/(k√λ_u). All are negative, so Ẑ is optimal.
4. **Uniqueness and the Gram matrices.** Every μ is positive, so at any
   optimum every margin equals 1, and X = Ẑ + 1rᵀ for some r. Since
   Ẑᵀ1 = 0, Xᵀ X = ẐᵀẐ + k rrᵀ, whose trace square root exceeds ‖Ẑ‖_*
   unless r = 0. So X = Ẑ. The balanced factorisation then gives ŴᵀŴ and
   ĤᵀĤ as the two square-root factors of Ẑ's singular value
   decomposition.
5. **When it is the ETF.** Ẑ's nonzero singular values are √(Rm), √m and
   √λ_u, with the multiplicities above. They are all equal, which is the
   simplex equiangular tight frame, exactly when R = 1, or when k = 2 and
   Ẑ has rank one.

What could have failed: one sign in step 3. A positive off-diagonal entry
of M would leave G outside the cone of constraint normals, and Ẑ could
then be beaten.

## What this does not say

- **Not that gradient descent reaches it.** Gradient descent on
  unregularized cross-entropy converges in direction to a KKT point of the
  non-convex problem, not provably to this minimiser. That is the
  authors' conjecture C1, and [THEORY-286](THEORY-286.md)'s.
- **Not that trained networks are at it.** The deep-network measurements,
  one seed per cell under weight decay, are [THEORY-286](THEORY-286.md)'s.
- **Not the regularized geometry.** The ridge results (Propositions 1–2)
  are [THEORY-286](THEORY-286.md)'s.
- **Not for class sizes other than a step.** The certificate works
  whenever M's off-diagonal entries are negative; only the step case is
  checked here.
