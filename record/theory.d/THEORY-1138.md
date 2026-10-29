---
number: 1138
status: Active
formerly:
- THEORY-tmpdtrq6
title: 'Optimal transport whose cost is the Lovász extension of a submodular set function on source–target assignments stays a convex problem, a zero-sum game in which an adversary picks the cost matrix from the function''s base polytope, and reduces to ordinary optimal transport exactly when the set function is modular; the convexity needs submodularity, so the paper''s own threshold cost, which is not concave at its threshold, falls outside it, and the induced discrepancy is symmetric only when the set function is'
version: 1
tags:
- mathematics
date: '2026-10-29'
source:
- LIT-1815
summary: >-
  Alvarez-Melis, Jaakkola and Jegelka (2018), [LIT-1815](../literature.d/LIT-1815.md), §3, read in
  [NOTE-1324](../notes.d/NOTE-1324.md) from arXiv v1. The convexity and game form are standard
  submodular analysis; the failure of eq. (12) and the asymmetry were
  checked numerically. Active. It does not say structured couplings
  predict better; the experiments are single runs on 100 samples.
---

# THEORY-1138: Optimal transport whose cost is the Lovász extension of a submodular set function on source–target assignments stays a convex problem, a zero-sum game in which an adversary picks the cost matrix from the function's base polytope, and reduces to ordinary optimal transport exactly when the set function is modular; the convexity needs submodularity, so the paper's own threshold cost, which is not concave at its threshold, falls outside it, and the induced discrepancy is symmetric only when the set function is

## Source

Alvarez-Melis, Jaakkola and Jegelka (2018), [LIT-1815](../literature.d/LIT-1815.md), §§2.2–3.2, pp.
4–7, and Appendix A, p. 18 of arXiv 1712.06199v1; read in [NOTE-1324](../notes.d/NOTE-1324.md).

## What was actually shown

**The framework.** A set function F on assignments (u, v) is submodular
when marginal costs diminish (eq. 7, p. 4). Its Lovász extension f is
convex iff F is submodular, and then f(w) = max_{x ∈ B_F} wᵀx (eqs. 8–9,
Lovász 1983). So min_{γ ∈ M} f(γ) = min_γ max_{κ ∈ B_F} ⟨γ, κ⟩ is a convex
problem and a convex–concave saddle-point problem over two polytopes, with
a Nash equilibrium (pp. 6–7). If F is modular, B_F is the single point C
and the problem is ordinary OT (p. 7).

**Lemma 3.1 (p. 6; proof p. 18).** With C a metric, F non-decreasing,
F(∅) = 0 and F({(i, j)}) > 0 iff C_ij > 0, d_F ≥ 0, and d_F = 0 iff µ = ν.

**Checked, against the paper.** Eq. (12) with the square root, g(x) =
min{x, α} + √[x − α]₊, has slope 1 below α and unbounded slope just above
it. It is not concave (with α = 1, g(1) = 1 lies below the chord value
1.108 from g(0.9) and g(1.1)). On one block of five edges, 84 of 405
diminishing-returns inequalities failed for F = g(Σ C), and none for
g = √. The paper's statement that "the symmetry of d F (µ, ν) is trivial"
(p. 18) fails when F is defined from the source side's groups only, as in
its domain-adaptation experiment. In a 3 × 3 example solved exactly as a
linear program over all vertices of B_F, d_F was 0.574 one way and 0.759
with the roles exchanged.

**What could have failed.** A set-wise cost on couplings could have made
the problem non-convex, as the discrete matching version is hard to
approximate (p. 6). Submodularity prevents that. Leaving submodularity,
as eq. (12) does, gives the guarantee up.

## What this does not say

- **That the framework finds structure.** The groups are inputs.
- **That every useful higher-order cost is admissible.** Only submodular
  ones keep this form: economies of grouping, not penalties for
  co-occurrence.
- **That d_F is a metric.** No triangle inequality is claimed, and symmetry
  needs a symmetric F.
- **That the reported accuracies came from a submodular cost.** The paper
  states the threshold form it used. With that form the guarantees do not
  apply.
