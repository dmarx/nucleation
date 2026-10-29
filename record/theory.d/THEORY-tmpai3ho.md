---
status: Active
title: 'Optimal transport between two point sets related by one unknown global linear map from a Schatten ℓp ball reduces, when every admissible map preserves angles or the target is whitened, to choosing the coupling Γ that maximises the dual Schatten-q norm of the transported cross-covariance XΓYᵀ: the nuclear norm when the maps are orthogonal, and the Frobenius norm when they lie on a Frobenius sphere, which is exactly the Gromov–Wasserstein problem with cosine similarity and squared loss; in every case one transformation acts on the whole space'
version: 1
tags:
- mathematics
- representation-learning
date: '2026-10-29'
source:
- LIT-tmpbs68a
summary: >-
  Alvarez-Melis, Jegelka and Jaakkola (2019), [LIT-tmpbs68a](../literature.d/LIT-tmpbs68a.md), Lemmas
  4.1–4.3 with proofs in Appendix D; read in [NOTE-tmpdwqe2](../notes.d/NOTE-tmpdwqe2.md). Each step was
  checked numerically. Active: proved, and checked. The conditions
  matter. The p = 2 link to GW holds for the original transport problem
  only when the target is whitened and all vectors have equal norm, which
  the paper states in two separate places. Nothing here makes the chosen
  class the right one for given data, and nothing in it is local.
---
<!-- inactive-ok-file: QUESTION-130 — Open; the question whose distinction this result sharpens -->

# THEORY-tmpai3ho: Optimal transport between two point sets related by one unknown global linear map from a Schatten ℓp ball reduces, when every admissible map preserves angles or the target is whitened, to choosing the coupling Γ that maximises the dual Schatten-q norm of the transported cross-covariance XΓYᵀ: the nuclear norm when the maps are orthogonal, and the Frobenius norm when they lie on a Frobenius sphere, which is exactly the Gromov–Wasserstein problem with cosine similarity and squared loss; in every case one transformation acts on the whole space

## Source

Alvarez-Melis, Jegelka and Jaakkola (2019), [LIT-tmpbs68a](../literature.d/LIT-tmpbs68a.md), §4 and
Appendix D, pp. 4–6 and 11–12 of arXiv 1806.09277v2; read in
[NOTE-tmpdwqe2](../notes.d/NOTE-tmpdwqe2.md).

## What was actually shown

**The problem.** For X ∈ ℝ^{d×n}, Y ∈ ℝ^{d×m}, weights p, q, couplings
Π(p, q) and maps P in F_p = {‖P‖_p ≤ k_p} (Schatten norm), minimise
⟨Γ, C(X, PY)⟩ with squared Euclidean cost (eq. 7). This equals
max over Γ, P of 2⟨XΓYᵀ, P⟩ − Σ p_i‖x_i‖² − Σ q_j‖Py_j‖² (eq. 9).

**Lemma 4.1.** If every P ∈ F preserves inner products, or ‖P‖_F is
constant on F and Y diag(q) Yᵀ = I, the last term does not depend on P,
and (9) becomes max over Γ, P of ⟨XΓYᵀ, P⟩ (eq. 10). Checked: for an
unwhitened Y, Σ q_j‖Py_j‖² ranged from 1.75 to 27.59 over random P with
‖P‖_F = √5. For the whitened Y it was 5 for every P.

**Lemma 4.2.** For M = UΣVᵀ, max over ‖P‖_p ≤ k of ⟨P, M⟩ is k‖σ(M)‖_q,
with q the dual exponent, attained at U diag(s) Vᵀ. That is von Neumann's
trace inequality with Hölder. For p = ∞ it gives the Procrustes solution
UVᵀ. Checked: the closed form attains k‖σ‖_q for p = ∞, 2 and 1, and no
random feasible P exceeded it.

**The two reductions.** For p = ∞ with k = 1, F_∞ = O(d) under either
condition, and (10) is max_Γ ‖XΓYᵀ‖_* (eq. 13). For p = 2 with
‖P‖_F = √d, (10) is max_Γ ‖XΓYᵀ‖_F (eq. 14).

**Lemma 4.3.** With unit-norm columns, C^x = XᵀX and C^y = YᵀY, and
Σ (C^x_ik − C^y_jl)² Γ_ij Γ_kl equals a term fixed by the marginals minus
2‖XΓYᵀ‖_F². So minimising GW with cosine similarity and squared loss is
maximising (14). Checked on random data: the identity holds to 10 decimal
places, and the GW objective equals the constant minus twice it.

**What it means.** Estimating a global transformation from a stated class
and comparing only quantities that such a transformation leaves alone
are, for this class, the same problem. Both (13) and (14) are unitarily
invariant norms, so both are unchanged by an orthogonal map of either
space.

**What could have failed.** The P-dependent term could have survived
without the conditions, and it does. The identity in Lemma 4.3 could have
needed more than unit norms. It does not.

## What this does not say

- **That GW is OT with a global map in general.** The p = 2 link to the
  original transport problem (7) needs both Lemma 4.1's whitening and
  Lemma 4.3's equal norms. Real embeddings meet neither without
  preprocessing.
- **That the invariance class is right for given data.** F is "pre-specified"
  (p. 4) and chosen by the analyst. Where the spaces differ by a
  non-linear warp, no p fits ([LIT-tmpentcd](../literature.d/LIT-tmpentcd.md)).
- **Anything local.** One P acts on every point. There is no frame per
  node, no relation that transforms, no cycle, and so no holonomy. This is
  the global freedom of the three that the exchange's A6 kept apart, not
  the per-entity freedom of [THEORY-tmpf3jtf](THEORY-tmpf3jtf.md).
- **That the solution is unique.** The problem is not jointly concave, and
  any symmetry of the data inside the class gives ties ([THEORY-tmpa43ta](THEORY-tmpa43ta.md)).
- **That annealing finds the global optimum.** The paper's robustness to
  initialisation is observed on its tasks, not proved.
