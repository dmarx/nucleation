---
number: 369
status: Active
formerly:
- CLAIM-tmpc36bo
title: 'In symmetric resource-mediated competition with interaction matrix A = UᵀU and growth rates r = Uᵀb − c, Lotka–Volterra population dynamics are multiplicative gradient flow on the convex feature-selection objective ½‖b − Un‖² + cᵀn over the nonnegative orthant: the invasion fitness of an absent component is the negative partial derivative of that objective, and the uninvadable equilibria are its KKT points'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: that under the stated assumptions (A = UᵀU,
  r = Uᵀb − c, dynamics ṅ_i = n_i(r_i − (An)_i)) the per-capita growth of a
  component differs from −∂_i L, that L fails to decrease along the flow,
  or that an equilibrium with every absent component unable to invade can
  violate the KKT conditions of min L over n ≥ 0. Not defeated by
  competitive systems with asymmetric interactions, or growth rates not of
  the form Uᵀb − c, which the claim excludes.
tags:
- ecology
- mathematics
- learning-theory
date: '2026-10-18'
line:
- formal-apparatus
- distributed-agency
grounds:
- CASE-118
complements:
- CLAIM-279
summary: >-
  From a synthesis the owner relayed on 2026-10-18 (workbench entry of that
  date), checked here and given a proof. When competition between
  components is mediated by shared resources with feature or niche vectors
  u_i, so that A = UᵀU and r = Uᵀb − c, the Lotka–Volterra dynamics are
  ṅ_i = −n_i ∂_i L with L(n) = ½‖b − Un‖² + cᵀn: entropic mirror descent on
  the positive orthant. A rare component's invasion fitness is −∂_i L, the
  value of adding that feature, and uninvadable equilibria are the KKT
  points of the convex program. The sharp edge: the identity needs a
  shared scalar objective, and it fails for asymmetric interactions or
  processes with competing objectives, which is where an organization
  stops being an optimizer. Mehta et al. (2019) and Marsland, Cui and
  Mehta (2020) give the general duality for consumer–resource models.
---
<!-- inactive-ok-file: CLAIM-279 CLAIM-288 — Proposed or Deferred; open claims, readings and works cited as open, nothing here rests on their being settled -->

# CLAIM-369: In symmetric resource-mediated competition with interaction matrix A = UᵀU and growth rates r = Uᵀb − c, Lotka–Volterra population dynamics are multiplicative gradient flow on the convex feature-selection objective ½‖b − Un‖² + cᵀn over the nonnegative orthant: the invasion fitness of an absent component is the negative partial derivative of that objective, and the uninvadable equilibria are its KKT points

## The claim

Let components i = 1, …, k have abundances, or unnormalized participation
intensities, n_i ≥ 0 and niche or feature vectors u_i ∈ ℝᵐ, the columns of U. Let
b ∈ ℝᵐ be the environmental supply or target signal and c_i ≥ 0 a
maintenance cost. Assume

  A = UᵀU,  r = Uᵀb − c,  ṅ_i = n_i (r_i − (An)_i).

Define L(n) = ½‖b − Un‖² + cᵀn. Then:

1. **Gradient form.** ∇L = UᵀUn − Uᵀb + c = An − r, so
   ṅ_i = −n_i ∂_i L. In logarithmic coordinates, d/dt log n_i = −∂_i L,
   which is continuous-time mirror descent with the entropy potential
   Σ n_i log n_i on the positive orthant.
2. **Descent.** dL/dt = Σ ∂_i L · ṅ_i = −Σ n_i (∂_i L)² ≤ 0.
3. **Invasion fitness.** A component's per-capita growth is
   r_i − (An)_i = −∂_i L. At a resident equilibrium with n_i = 0, the
   rare component invades exactly when s_i = −∂_i L > 0: when increasing
   its weight from zero lowers the objective to first order.
4. **KKT.** At an equilibrium every active component has ∂_i L = 0. If no
   absent component can invade, every absent one has ∂_i L ≥ 0. These are
   the KKT conditions for min L over n ≥ 0. Since A is positive
   semidefinite, L is convex, so such points are global minima. With A
   singular there may be several, and which one the flow reaches depends
   on the start.

So in this model three quantities coincide:

| ecology | optimization | learning |
|---|---|---|
| invasion fitness s_i | negative directional derivative −∂_i L at n_i = 0 | value of adding feature i |

It was checked numerically. For a random U (6 × 4), b and c, the identity
ṅ = −n ⊙ ∇L holds to machine precision. Integrating the flow, L
decreased at every step, and at the endpoint active components had zero
gradient and the absent one a positive gradient.

**The two-component case** ([CASE-118](../cases.d/CASE-118.md)). With A = [[1, ρ], [ρ, 1]],
0 ≤ ρ < 1, and r₁ = r₂ = 1, the invasion growth of either component into
the other's equilibrium (n = 1) is 1 − ρ. That is also λ_min(A). The
condition number of the Gram matrix is κ(A) = (1 + ρ)/(1 − ρ). In this
model, niche overlap weakens the rare component's invasion advantage and
ill-conditions the feature system by the same parameter. The
correspondence is exact here and does not extend as an identity to
arbitrary competitive systems.

## Why the record holds it

[QUESTION-083](../questions.d/QUESTION-083.md) asks whether processes sharing one update rule can come to
hold differentiated, mutually regulated authority. [CLAIM-279](CLAIM-279.md) says roles
are regimes, not kinds, and its note of 2026-10-18 brings in Chesson's
coexistence mechanisms. This claim gives the formal bridge those entries
lacked. In the potential case, ecological coexistence of differentiated
components is the same mathematics as sparse feature selection, and the
recovery test of [QUESTION-083](../questions.d/QUESTION-083.md) is a marginal-value test. It also marks
exactly where the bridge ends (below).

## Two boundaries of application

**Abundance is not a normalized share of authority.** The theorem is about
nonnegative, unconstrained abundances. Influence in an organization is
often relational, budgeted or competitive, and normalized so that
Σ w_i = 1. That is a different dynamical model. If the shares are read
off the abundances, w_i = n_i / Σ_j n_j, then with f_i(n) = −∂_i L(n):

  ẇ_i = w_i ( f_i(n) − Σ_j w_j f_j(n) ).

This is a replicator equation, not the gradient flow on the orthant. If
instead fitness is evaluated directly at w on the simplex, the
equilibrium conditions carry a common Lagrange multiplier: ∂_i L(w) = λ
for every active component, not ∂_i L = 0. So the equivalence between
ecology and optimization does not automatically survive a change from
abundance dynamics to conserved authority shares. Normalized endorsement
is a separate model, and this claim does not cover it. That is not a
claim that normalized endorsement cannot optimize. Normalization changes
the feasible geometry and the equilibrium conditions, but it does not
necessarily remove a potential-function reading. Whether one survives
depends on how fitness and authority are defined on the simplex. For
example, replicator dynamics whose fitness is evaluated at the shares
themselves, f_i(w) = −∂_i L(w), are a gradient flow of −L on the simplex
under the Shahshahani metric. The equation above, with fitness evaluated
at the unnormalized n, is not of that form in general. (A point from the
owner's review of the filing, relayed 2026-10-18.)

**The algebra holds for any U; the ecological reading needs a sign
condition.** The gradient-flow correspondence holds for arbitrary real
feature vectors, because UᵀU is positive semidefinite. But signed feature
vectors can have negative inner products. Then some off-diagonal entries
of A are negative, and the corresponding Lotka–Volterra interaction is
facilitative, not competitive. Reading A as a matrix of competitive niche
overlaps also needs nonnegative off-diagonal interactions, as in models
whose resource-use vectors are nonnegative.

## What it does not say

- **That ecological selection optimizes learning objectives in general.**
  The identity needs symmetric interactions, A = UᵀU, and growth rates of
  the form Uᵀb − c. With asymmetric or nonreciprocal interactions
  ([THEORY-634](../theory.d/THEORY-634.md), Blumenthal, Rocks and Mehta 2024) there may be no scalar L
  at all.
- **That operators with competing objectives are optimizers.** An
  organization whose processes disagree about the desired outcome has, in
  general, no shared L whose gradient describes their interactions. That
  is where the equivalence breaks, and where it becomes interesting for
  agency. A local influence field might be split as F(n) = −∇V(n) + J(n),
  with J the non-potential part, but the split depends on a chosen metric
  and convention and is not unique without one. Whether organizations with
  the same local incentives and more non-reciprocity converge, oscillate,
  switch among configurations or become chaotic is open ([THEORY-548](../theory.d/THEORY-548.md) on
  delay-induced Lotka–Volterra instability, [THEORY-634](../theory.d/THEORY-634.md) on non-reciprocal
  catalytic rings).
- **That the kernel fixes coexistence.** The same Gram matrix supports
  coexistence or exclusion depending on r ([CASE-118](../cases.d/CASE-118.md)).
- **That a population of coexisting specialists governs itself.**
  Coexistence is not endogenous regulation ([CLAIM-288](CLAIM-288.md)).
