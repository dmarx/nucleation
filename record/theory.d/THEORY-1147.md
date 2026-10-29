---
number: 1147
status: Active
formerly:
- THEORY-tmpr2ueq
title: 'For entropy-regularized optimal transport with a fixed cost, the gradient of any differentiable function of the optimal plan with respect to the cost is obtained exactly from one linear system of size n + m whose matrix [[diag µ, T], [Tᵀ, diag ν]] is positive semidefinite and singular only along the gauge direction (1, −1), which does not affect the gradient; so the first-order effect of supervising any candidate pair on a utility of the whole alignment can be computed without forming the (nm)² Jacobian'
version: 1
tags:
- mathematics
- network-science
date: '2026-10-29'
source:
- LIT-1807
summary: >-
  Yu et al. (2026), [LIT-1807](../literature.d/LIT-1807.md), Lemmas 4.2 and 4.3 with Appendix A (pp.
  4–5, 14–17), read in [NOTE-1327](../notes.d/NOTE-1327.md). Proved by implicit differentiation of
  the optimality conditions; checked by finite differences. Active. It is
  a derivative: a local, first-order estimate of a finite change, exact
  only for plain entropic OT whose cost does not depend on the plan.
---

# THEORY-1147: For entropy-regularized optimal transport with a fixed cost, the gradient of any differentiable function of the optimal plan with respect to the cost is obtained exactly from one linear system of size n + m whose matrix [[diag µ, T], [Tᵀ, diag ν]] is positive semidefinite and singular only along the gauge direction (1, −1), which does not affect the gradient; so the first-order effect of supervising any candidate pair on a utility of the whole alignment can be computed without forming the (nm)² Jacobian

## Source

Yu, Qiu, Zeng, Thai, Liu and Tong (2026), [LIT-1807](../literature.d/LIT-1807.md), §4.1 and Appendix
A of arXiv 2605.24395v2; read in [NOTE-1327](../notes.d/NOTE-1327.md).

## What was actually shown

**Derivation (A.1, pp. 14–16).** The optimal entropic plan is
T_ij = exp((α_i + β_j − C̃_ij)/ε) (eq. 13). Differentiating gives
dT = (1/ε) T ⊙ (dα1ᵀ + 1dβᵀ − dC̃) (eq. 15), and keeping the marginals
fixed gives A(dα, dβ) = ((T ⊙ dC̃)1, (T ⊙ dC̃)ᵀ1) (eq. 24). An adjoint
vector y solving Ay = ((T ⊙ ∇_T f)1, (T ⊙ ∇_T f)ᵀ1) eliminates dα, dβ, so
∇_C̃ f = (1/ε) T ⊙ (y_α1ᵀ + 1y_βᵀ − ∇_T f) (eq. 32).

**Solvability (A.2–A.3, pp. 16–17).** zᵀAz = Σ T_ij(s_i + t_j)² ≥ 0; (1, −1)
is in the null space; the right side is orthogonal to it, so conjugate
gradients converge (Kaasschieter 1988, Hayami 2018). Any two solutions
differ along null directions, which cancel in y_α1ᵀ + 1y_βᵀ on the support
of T, so the gradient is unique. For a fully supported (dense entropic)
plan the null space is exactly span(1, −1); for a plan with disconnected
support it is larger, and the gradient is still unique on the support.

**Use.** Supervising pair (i, j) moves C̃_ij by −βC_ij, so its first-order
effect on f is −βC_ij(∇_C̃ f)_ij (eq. 7, p. 5).

**Checked.** On a 6 × 5 problem with ε = 0.1, solved by log-domain
Sinkhorn to convergence, the formula matched central finite differences to
9 × 10⁻¹¹ (f = ‖T‖²) and 6 × 10⁻¹⁰ (f = Σ T log T), and A had rank
n + m − 1 (numpy/scipy; my script).

**What could have failed.** The singular system could have had a right
side outside the range of A, or solutions giving different gradients.
Neither happens.

## What this does not say

- **What a label actually does.** A label is a finite change, a cost set
  to (1 − β)C_ij, β = 1 by default; the derivative predicts it only
  locally.
- **Anything for unregularized OT**, whose plan is piecewise constant in
  the cost; the 1/ε factor shows the derivative grows as ε → 0.
- **Anything exact for aligners whose cost depends on the plan**, such as
  fused Gromov–Wasserstein, or whose plan is not the fixed-cost entropic
  solution. The paper applies the score to such aligners without saying
  how ([NOTE-1327](../notes.d/NOTE-1327.md)).
- **That the utility measures accuracy.** The formula differentiates
  whatever f is supplied.
- **That this is new mathematics.** Implicit differentiation of entropic
  OT is known; the contribution is its use to score queries.
