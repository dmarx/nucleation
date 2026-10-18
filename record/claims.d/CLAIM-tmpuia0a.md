---
status: Active
title: 'Whether several objectives share a strict first-order descent direction, 0 ∉ conv{g_i}, is invariant under smooth invertible reparameterization, while the sign of a Euclidean gradient inner product is not, and a negative inner product does not exclude common descent; a budgeted version is invariant only with the metric pulled back'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof: a smooth invertible change of coordinates under
  which some objectives have a common strict first-order descent direction
  in one chart and none in the other, or an error in the counterexample,
  that the inner products of (1, 1) and (1, −½) and of their transforms
  under diag(½, 2) do not have opposite signs. Not defeated by
  non-invariance of finite-step trajectories or of optimizer-dependent
  quantities, which the claim does not cover.
tags:
- information-geometry
- loss-landscapes
- mathematics
date: '2026-10-18'
line:
- learned-structure
- formal-apparatus
complements:
- CLAIM-263
- CLAIM-305
grounds:
- THEORY-082
uses:
- TERM-tmp9lmlt
summary: >-
  A35 §2 of the exchange of 2026-10-17, at the owner's U35 "double click"
  on whether functionally equivalent parameterizations give equivalent
  frustration diagnoses. Gradients transform as g′ = Jᵀg and directions as
  v′ = J⁻¹v, so directional derivatives, and with them the common-descent
  test 0 ∉ conv{g_i}, do not depend on coordinates. A Euclidean inner
  product does: g₁ = (1, 1), g₂ = (1, −½) have product ½, and under
  θ = diag(½, 2)ψ their transforms have −7/4, while d = (−1, 0) lowers
  both throughout. The sharp edge: it covers coordinate changes of one
  parameter space at first order, not function-preserving symmetries or
  training trajectories ([QUESTION-tmpm1wok](../questions.d/QUESTION-tmpm1wok.md)). The practice corollary, not
  to diagnose task conflict by gradient cosine, is the anthology's.
---

# CLAIM-tmpuia0a: Whether several objectives share a strict first-order descent direction, 0 ∉ conv{g_i}, is invariant under smooth invertible reparameterization, while the sign of a Euclidean gradient inner product is not, and a negative inner product does not exclude common descent; a budgeted version is invariant only with the metric pulled back

## The claim

The owner, at U35, on A34's question "When do two functionally equivalent
parameterizations yield equivalent frustration diagnoses?": "interesting
question, double click on this." A35 §2 answered the first-order part.
Pairwise gradient conflict, g_iᵀg_j < 0, is used as a conflict test in
multi-task learning (for example by Yu et al. (2020)). A35: "gradients are
covectors. Their Euclidean inner product is not preserved under arbitrary
changes of parameter coordinates."

## Proof

**Transport.** Let θ = φ(ψ) be smooth with invertible Jacobian J at the
point. For L′_i(ψ) = L_i(φ(ψ)), the chain rule gives g′_i = Jᵀg_i. A
displacement v in θ corresponds to v′ = J⁻¹v in ψ. So

  g′_iᵀv′ = g_iᵀ J J⁻¹ v = g_iᵀv.

The first-order change of each objective along a given displacement does
not depend on the chart.

**Common descent is invariant.** There is a v with g_iᵀv < 0 for all i iff
there is a v′ = J⁻¹v with g′_iᵀv′ < 0 for all i, by the identity above.
Equivalently, 0 ∈ conv{g_i} iff 0 ∈ conv{Jᵀg_i}, since Σλ_iJᵀg_i =
Jᵀ(Σλ_ig_i) and Jᵀ is invertible.

That the convex-hull test is the common-descent test (A33's criterion) is a
theorem of the alternative of Gordan's kind, proved directly. If 0 =
Σλ_ig_i with λ in the simplex, then Σλ_i g_iᵀv = 0 for every v, so not
all g_iᵀv are negative. If 0 ∉ conv{g_i}, let h ≠ 0 be the point of
minimum norm in conv{g_i}; for every x in the hull hᵀx ≥ |h|², so v = −h
gives g_iᵀv ≤ −|h|² < 0 for all i.

**The sign of an inner product is not invariant.** A35's counterexample,
checked: g₁ = (1, 1), g₂ = (1, −½), g₁ᵀg₂ = 1 − ½ = ½. With
θ = diag(½, 2)ψ, J = Jᵀ = diag(½, 2), so g′₁ = (½, 2), g′₂ = (½, −1), and
g′₁ᵀg′₂ = ¼ − 2 = −7/4. The objectives are the same; the conflict label
flips.

**A negative inner product does not exclude common descent.** In the same
example d = (−1, 0) gives g₁ᵀd = g₂ᵀd = −1. In ψ it is d′ = J⁻¹d = (−2, 0),
and g′₁ᵀd′ = g′₂ᵀd′ = −1, with g′₁ᵀg′₂ < 0. For two nonzero gradients
the invariant fact is simpler: they have a common descent direction iff
they are not antiparallel, and antiparallelism is preserved by Jᵀ.

**A budgeted test needs the transported metric.** If update size is
measured by a metric G_θ, ‖v‖² = vᵀG_θv, the same problem in ψ uses the
pullback G_ψ = JᵀG_θJ, and then ‖v′‖_{G_ψ} = ‖v‖_{G_θ}. The dual norm of
the gradient is preserved as well: g′ᵀG_ψ⁻¹g′ = gᵀG_θ⁻¹g. So the residual
Φ_r of [CLAIM-tmpue67e](CLAIM-tmpue67e.md) is chart-independent when the metric is carried
along. A35: "If we use the Euclidean norm afresh in every representation,
we're not keeping the optimization geometry fixed; we're changing the
optimization problem." This is [THEORY-082](../theory.d/THEORY-082.md)'s point, that steepest descent
is defined only relative to a metric, applied to the feasibility test.

## A35's table

A35 §2 sorted diagnostics by expected invariance:

| Diagnostic | Invariance |
|---|---|
| Pairwise Euclidean gradient angles | Not invariant under general reparameterization |
| Common strict first-order descent, all tangent directions allowed | Invariant under smooth invertible coordinate changes |
| Budgeted feasibility, update geometry transported | Locally invariant under the same changes |
| Actual finite-step trajectories | Not necessarily invariant unless the update rule and its state transform too |
| Feasibility of specified changes to the represented function | Invariant under function-preserving parameterization, with the function class and allowed changes fixed |

This claim proves rows one to three. Rows four and five are
[QUESTION-tmpm1wok](../questions.d/QUESTION-tmpm1wok.md)'s. A35's summary of the gap: "same current function ≠
same learning dynamics".

## What it does not say

- **That the common-descent test is the right test.** It is the
  unbudgeted, first-order one. Budgets, module constraints and finite
  steps change feasibility (A33 §3A).
- **Anything about function-preserving symmetries.** A reparameterization
  here is a chart of one parameter space. Two networks related by a
  permutation of units or a blow-up ([CLAIM-263](CLAIM-263.md), [CLAIM-305](CLAIM-305.md), [THEORY-112](../theory.d/THEORY-112.md))
  are not covered: the map need not be a diffeomorphism of the whole space,
  and the Fisher metric can be degenerate there ([THEORY-082](../theory.d/THEORY-082.md)).
- **What practitioners should do.** That a cosine-based conflict
  diagnostic is chart-dependent is an instruction for machine-learning
  practice, and it belongs in the anthology. This record keeps the
  mathematics because the frustration account ([TERM-tmp9lmlt](../terms.d/TERM-tmp9lmlt.md)) needs a
  diagnosis that is not an artefact of coordinates.
