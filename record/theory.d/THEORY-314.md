---
number: 314
status: Active
formerly:
- THEORY-tmpiw6t1
title: "Every minimizer of an arbitrary cost on the training outputs plus a strictly increasing function of the RKHS norm lies in the span of the kernel functions at the training points, by the reproducing property and orthogonal decomposition alone"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Promoted, carrying out the promotion audit's decision for THEORY-314
    (batch 025, ADR-047 v2). The promote_when asked for a proof over the
    full completed RKHS with the conditions for a minimizer to exist. Both
    are re-derived in the decision file and summarised in the note of
    2026-10-19 below. promote_when is removed.
tags:
- mathematics
- learning-theory
date: '2026-10-14'
source:
- LIT-261
summary: >-
  Schölkopf, Herbrich & Smola (2001), [LIT-261](../literature.d/LIT-261.md), Theorem 1 with its
  proof (eqs. 18–24), read in [NOTE-836](../notes.d/NOTE-836.md) and checked. No convexity
  of the cost and no Riesz theorem is used; the RKHS is built from the
  kernel, so the reproducing property holds by construction. The theorem
  is stated over countable kernel expansions of finite norm, assumes a
  minimizer exists, and does not cover costs that see f other than
  through its values at the training points.
---

# THEORY-314: Every minimizer of an arbitrary cost on the training outputs plus a strictly increasing function of the RKHS norm lies in the span of the kernel functions at the training points, by the reproducing property and orthogonal decomposition alone

## Source

Schölkopf, Herbrich & Smola (2001), [LIT-261](../literature.d/LIT-261.md), §1.2 (eqs. 7–12), Theorem 1
and its proof (eqs. 13–24), and the remarks on p. 420, as read in
[NOTE-836](../notes.d/NOTE-836.md).

## What was actually shown

**The theorem.** X is any nonempty set and k a real positive-definite
kernel on it. g is strictly increasing on [0, ∞), and c maps the m
training triples (x_i, y_i, f(x_i)) to ℝ ∪ {∞}, with no further
condition: it may couple the points, be non-convex, or encode hard
constraints. Then any f in F, the class of countable expansions
Σ β_i k(·, z_i) of finite norm, that minimizes c + g(‖f‖) has the form
f = Σ_{i=1}^m α_i k(·, x_i).

**The proof.** Split f into its projection onto span{k(·, x_i)} and an
orthogonal remainder v. The reproducing property makes every f(x_j)
independent of v, so the cost does not see v. Pythagoras makes ‖f‖²
the sum of the two squared norms, so a strictly increasing g is strictly
larger unless v = 0. The reading checked each step: it needs v ∈ F (true,
since v is f minus a finite expansion) and strict monotonicity, nothing
else.

**Where the reproducing property comes from.** The RKHS is constructed
from k: finite combinations of k(·, x) with ⟨f, g⟩ := Σ α_i β_j k(x_i, x′_j),
then completion. ⟨k(·, x), f⟩ = f(x) holds by that construction (eq. 11).
No representation theorem is invoked.

What could have failed: a cost whose dependence on f is only through the
m values leaves no room for the orthogonal part to help, so the only way
the claim could fail is through the regularizer, and strict monotonicity
closes that.

## What this does not say

- **Not that a minimizer exists in general.** The theorem characterizes
  minimizers. The paper states no conditions for one to exist. Sufficient
  ones are in the note of 2026-10-19 below.
- **Not stated over the full RKHS in the paper.** The paper's class F is
  countable kernel expansions of finite norm (eq. 13). The note of
  2026-10-19 proves the result over the completed H_k directly.
- **Not that the finite problem is easy.** Without convexity of c and g
  the m-dimensional problem (eq. 30) can have local minima (p. 420).
- **Not for costs that see more than point values.** Costs on
  derivatives or integrals of f fall outside it; an analogue there would
  need representers of other functionals, which is where the Riesz
  theorem would enter.
- **Not the semiparametric case as proved.** Theorem 2 is stated without
  proof.
- **Not advice about which regularizer to use.** The examples recast
  existing algorithms; any recommendation belongs to the anthology.

## Note of 2026-10-19: over the completed RKHS, with existence

Re-derived for the promotion audit (batch 025, ADR-047 v2). The full
steps are in the audit's decision file for THEORY-314.

- **The theorem over H_k.** S = span{k(·, x_i)} is finite-dimensional,
  hence closed. So every f in H_k splits as f_S + v with v ⊥ S. The
  reproducing property gives f(x_j) = ⟨f, k(·, x_j)⟩ = f_S(x_j), so the
  cost cannot see v. Pythagoras gives ‖f‖ ≥ ‖f_S‖, with equality iff
  v = 0. A strictly increasing g then makes any f with v ≠ 0 strictly
  worse than f_S.
- **Existence.** A minimizer exists if c is lower semicontinuous and
  bounded below in the outputs, g is lower semicontinuous with g(t) → ∞,
  and the objective is finite somewhere. The infimum over H_k equals the
  infimum over S. On S the sublevel sets are closed and bounded in
  finite dimensions, hence compact, and an lsc function attains its
  minimum on them.
- **Without lower semicontinuity it can fail.** With m = 1,
  k(x_1, x_1) = 1, g(t) = t, and c = 0 when f(x_1) > 1, 2 otherwise, the
  infimum 1 is approached and never attained.

## Connections

- [THEORY-009](THEORY-009.md) cites this proof as the parallel case to spectral
  self-supervised learning: there too the needed structure (symmetry) is
  had directly, and Riesz is not used. This document makes that citation
  rest on a checked reading.
- Kernel PCA appears as a special case (Example 5, eq. 31), with a
  unit-variance constraint encoded as c = ∞. It gives one functional at a
  time, not an eigenspace, so it does not by itself reach the spectral
  results of [QUESTION-052](../questions.d/QUESTION-052.md).
