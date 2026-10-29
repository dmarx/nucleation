---
number: 366
status: Active
formerly:
- CLAIM-tmpuia0a
title: 'Whether several objectives share a strict first-order descent direction, 0 ∉ conv{g_i}, is invariant under smooth invertible reparameterization, while the sign of a Euclidean gradient inner product is not, and a negative inner product does not exclude common descent; a budgeted version is invariant only with the metric pulled back'
version: 3
history:
- version: 2
  date: '2026-10-26'
  note: >-
    A dated note added: T24 of the exchange "Experimental Infrastructure
    Review" restricted g_kᵀg_j to Euclidean gradient descent and added a
    separate caveat for Adam; the two are one fact, since a constant
    preconditioner is gradient descent in another chart (checked). The
    claim is unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added, from the reading of Désidéri's MGDA
    note (NOTE-1401). The claim is unchanged.
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
- TERM-060
answers:
- QUESTION-286
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
  training trajectories ([QUESTION-127](../questions.d/QUESTION-127.md)). The practice corollary, not
  to diagnose task conflict by gradient cosine, is the anthology's.
---

# CLAIM-366: Whether several objectives share a strict first-order descent direction, 0 ∉ conv{g_i}, is invariant under smooth invertible reparameterization, while the sign of a Euclidean gradient inner product is not, and a negative inner product does not exclude common descent; a budgeted version is invariant only with the metric pulled back

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
Φ_r of [CLAIM-365](CLAIM-365.md) is chart-independent when the metric is carried
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
[QUESTION-127](../questions.d/QUESTION-127.md)'s. A35's summary of the gap: "same current function ≠
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
  mathematics because the frustration account ([TERM-060](../terms.d/TERM-060.md)) needs a
  diagnosis that is not an artefact of coordinates.

## Note of 2026-10-26: the preconditioner is a chart

The reply at T24 of the exchange "Experimental Infrastructure Review"
offered g_kᵀg_j as a measure of task interaction "under ordinary Euclidean
gradient descent", and added that for Adam the optimizer state would have
to be accounted for ([QUESTION-275](../questions.d/QUESTION-275.md)). The two caveats are one.

- The first-order change in task j's loss from a preconditioned step on
  task k is −η g_jᵀ P g_k. On random quadratics the actual change was
  −7.771 × 10⁻⁴ against a prediction of −7.772 × 10⁻⁴.
- A constant P = JJᵀ is exactly gradient descent in the chart θ = Jψ
  (checked to 2 × 10⁻¹⁶). So the cross-term's sign under a preconditioner
  is the Euclidean product's sign in another chart.
- This claim's own example, (1, 1) and (1, −½) under J = diag(½, 2), is the
  preconditioner diag(¼, 4), and gives −7/4.
- Random diagonal preconditioners flipped the sign of the Euclidean
  product in 444 of 2,000 trials.

The budgeted test's dual norm gᵀG⁻¹g already implies this, with
P = G⁻¹. Adam's P depends on the gradients and moves in time, so the
identity holds only step by step. The reply's measure also needs this
claim's other half: a negative product does not exclude common descent,
and the chart-invariant test is 0 ∉ conv{g_i}. The claim is unchanged.

## Note of 2026-10-29: a published source for the constructive half

Désidéri's note on the multiple-gradient descent algorithm, [LIT-1212](../literature.d/LIT-1212.md), is
now read ([NOTE-1401](../notes.d/NOTE-1401.md)). Its Lemma 2.1 and Theorem 2.2 are exactly the
constructive half of A33's criterion as proved above: if 0 ∉ conv{g_i},
the minimum-norm point of the hull gives a common strict descent
direction. The converse, that zero in the hull excludes common strict
descent, is not stated there; its Lemma 1.2 proves only that
Pareto-optimality implies stationarity. The one-line proof of the
converse above stands and needs no source.

Its Remark 3 bears on this claim's line between invariant and
non-invariant objects. Whether a common direction exists is unchanged by
positive rescaling of the gradients, while the direction of the
minimum-norm combination is not, and the author leaves the choice of
scaling open. The claim is unchanged.
