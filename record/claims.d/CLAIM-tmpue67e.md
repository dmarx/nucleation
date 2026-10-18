---
status: Active
title: 'On a norm-ball update set the local frustration residual Φ_r = min over ‖d‖ ≤ r of max_i(ε_i + g_iᵀd) equals the maximum over the simplex of Σλ_iε_i − r‖Σλ_ig_i‖_*, so infeasibility of the declared improvements has a certificate, and any admissible actual update exceeds Φ_r by a nonnegative governance regret'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: an instance of the convex local problem
  (finite-dimensional, norm-ball update set, linear first-order changes)
  where the primal and dual values differ, where a feasible d exists
  despite a multiplier vector λ ≥ 0 with Σλ_iε_i > r‖Σλ_ig_i‖_*, or where
  an admissible update has worst shortfall below Φ_r. Not defeated by
  nonconvex or discrete update sets, by the failure of the first-order
  model at finite steps, or by the residual's dependence on units, all of
  which the claim excludes or states.
tags:
- operations-research
- mathematics
- loss-landscapes
date: '2026-10-18'
line:
- distributed-agency
- formal-apparatus
rests_on:
- CLAIM-tmp55mls
uses:
- TERM-tmp9lmlt
summary: >-
  A34 §4 and A35 §3 of the exchange of 2026-10-17, checked. The residual
  is the smallest worst-case shortfall of the declared local improvements
  ε_i over updates of size at most r. Minimax for the bilinear problem on
  two compact convex sets gives the dual over the simplex, so Φ_r > 0
  exactly when some λ certifies that no update meets all demands (A34's
  form). Governance regret Γ is the gap between an actual admissible
  update's shortfall and Φ_r, and is never negative. For L₁ = (θ − 1)²,
  L₂ = (θ + 1)² at θ = 0, Φ_r = ε for every r. The sharp edge: per A37 it
  is a cardinal refinement of the ordinal fact ([CLAIM-tmp55mls](CLAIM-tmp55mls.md)), and its
  magnitude depends on units (A36 §2D).
---

# CLAIM-tmpue67e: On a norm-ball update set the local frustration residual Φ_r = min over ‖d‖ ≤ r of max_i(ε_i + g_iᵀd) equals the maximum over the simplex of Σλ_iε_i − r‖Σλ_ig_i‖_*, so infeasibility of the declared improvements has a certificate, and any admissible actual update exceeds Φ_r by a nonnegative governance regret

## The claim

A34 §4 posed the test: under a budget r, is there a d with ‖d‖_𝓜 ≤ r and
−⟨g_i, d⟩ ≥ ε_i for all i? A35 §3.1, at the owner's U35 ("agree that this
is our top priority, flesh this out"), defined the residual

  Φ(θ; 𝒰, ε) = min_{d∈𝒰} max_i (ε_i + g_iᵀd),

with g_i the gradient of demand i and ε_i > 0 the improvement it requires
over the next local step. Φ ≤ 0 when some admissible update meets every
requirement to first order; Φ > 0 when every admissible update fails one.
A35 §3.2 gave the dual for 𝒰_r = {d : ‖d‖ ≤ r}. Both are checked here.

## Proof

Let ‖·‖ be a norm on ℝᵖ and ‖h‖_* = max_{‖d‖≤1} hᵀd its dual. Write Δ for
the simplex in ℝⁿ.

1. **Primal as a saddle problem.** max_i a_i = max_{λ∈Δ} Σλ_ia_i, so
   Φ_r = min_{‖d‖≤r} max_{λ∈Δ} [Σλ_iε_i + (Σλ_ig_i)ᵀd]. The function is
   affine in d and linear in λ, and both sets are compact and convex.
2. **Exchange.** By the minimax theorem for such functions (von Neumann's,
   or Sion's), min and max commute:
   Φ_r = max_{λ∈Δ} min_{‖d‖≤r} [Σλ_iε_i + (Σλ_ig_i)ᵀd].
3. **Inner minimum.** min_{‖d‖≤r} hᵀd = −r‖h‖_*, by the definition of
   the dual norm. So

     Φ_r = max_{λ∈Δ} [ Σλ_iε_i − r‖Σλ_ig_i‖_* ].

4. **The certificate.** The minimum in the primal is attained (continuous
   function, compact set), so a d with ‖d‖ ≤ r and −g_iᵀd ≥ ε_i for all i
   exists iff Φ_r ≤ 0, iff Σλ_iε_i ≤ r‖Σλ_ig_i‖_* for every λ ∈ Δ, and,
   since both sides are positively homogeneous in λ, for every λ ≥ 0. That
   is A34's form. A λ ≥ 0 with Σλ_iε_i > r‖Σλ_ig_i‖_* certifies
   infeasibility by itself: any feasible d would give Σλ_iε_i ≤
   −(Σλ_ig_i)ᵀd ≤ r‖Σλ_ig_i‖_*.
5. **Governance regret.** For an update d^actual the organization
   actually makes, Γ = max_i(ε_i + g_iᵀd^actual) − Φ_r. If d^actual is
   admissible, it is one of the d the minimum ranges over, so Γ ≥ 0. Γ = 0
   exactly when the actual update is a minimizer.

The identity was also checked numerically when this was filed: on 2,000
random instances with the ∞-norm ball (dual norm ℓ₁), both sides solved
as linear programs agreed to within 10⁻¹⁴.

## The worked case

K07 ([CASE-tmpuc54q](../cases.d/CASE-tmpuc54q.md)), A35 §3.4: L₁ = (θ − 1)², L₂ = (θ + 1)², θ ∈ ℝ, at
θ = 0, with ε₁ = ε₂ = ε. Here g₁ = −2, g₂ = 2, and ‖·‖_* = |·|. The dual
value at λ = (½, ½) is ε − r·0 = ε, so Φ_r ≥ ε. Every d gives
max(ε − 2d, ε + 2d) ≥ ε, with equality at d = 0, so Φ_r = ε for every
r ≥ 0. No budget helps: this is structural frustration ([CLAIM-tmpl8vsy](CLAIM-tmpl8vsy.md)).
After K07's split into θ_A, θ_B, at (0, 0) with the Euclidean norm,
Φ_r = ε − √2·r, which is positive only while r < ε/√2.

## An application of a known theorem

A39 §2A: if 𝒰 ⊆ ℝᵖ is convex, each A_i = {d ∈ 𝒰 : −g_iᵀd ≥ ε_i} is convex,
so by Helly's theorem, when the demands cannot all be met, "some subset of
at most p+1 demands already witnesses the incompatibility". A39 said what
it is: "an application of an established theorem, not a new theorem". In
the terms of [CLAIM-tmp55mls](CLAIM-tmp55mls.md), the minimal non-faces of the complex have at
most p + 1 members, and fewer when 𝒰 has lower affine dimension. The bound
needs convexity, and A39: "nonlinear, discrete, or nonconvex learning
constraints need not obey this same bound."

## What it does not say

- **That the multipliers are endorsement weights.** A35: "Importantly,
  these dual multipliers are not endorsement weights." They certify
  difficulty; the weights governance actually assigns are another matter
  ([CLAIM-tmpl8vsy](CLAIM-tmpl8vsy.md), [QUESTION-tmpkzu6g](../questions.d/QUESTION-tmpkzu6g.md)).
- **That the magnitude means anything without units.** A36 §2D: "Even when
  all objectives are numerical, their units matter. Rescaling one loss
  function can change the scalar diagnosis unless we rescale and normalize
  the corresponding requirement consistently." The sign of Φ_r, feasible or
  not, survives a consistent rescaling of g_i and ε_i together; its size
  does not. Per A37 the residual is "a quantitative refinement of a more
  basic order-theoretic feasibility problem, not the definition of
  frustration itself", which is why it rests on [CLAIM-tmp55mls](CLAIM-tmp55mls.md).
- **Anything beyond the convex local model.** A34: it "applies to this
  local linearized, norm-constrained problem; additional nonconvex
  architectural or discrete update constraints require different
  analysis."
- **That a change of chart changes it.** With the metric pulled back it is
  invariant ([CLAIM-tmpuia0a](CLAIM-tmpuia0a.md)); with the Euclidean norm taken afresh in each
  chart it is a different problem.
