---
number: 1057
status: Active
formerly:
- THEORY-tmp3wlcq
title: 'Gradient descent with backpropagation, weight decay and Newton''s method are one discrete-time semantics of an operad of potential-carrying lenses, in which the state moves by subtracting the sharpened sum of three pulled-back covectors (from the output, from the input wiring and from the potential); the semantics is an operad functor, so a composite''s update is assembled from its parts'' updates, and backpropagation is that functoriality'
version: 1
tags:
- compositionality
- learning-theory
- mathematics
date: '2026-10-27'
source:
- LIT-1649
summary: >-
  Spivak (2026), [LIT-1649](../literature.d/LIT-1649.md), read in [NOTE-1225](../notes.d/NOTE-1225.md) from arXiv v2. Lens
  internalization (Corollary 3.3.4) and an integrator give operad functors
  ArrSm → PC (Theorem 4.3.6, Corollary 6.4.1). Under the configuration
  integrator the state update is q ↦ q − ♯_q(ξ_Q), with ξ_Q the
  Q*-component of the sum in (58); a parameterized map wired to a loss
  gives gradient descent (76), a weight-only potential gives weight decay
  (Proposition 7.2.3), and an inverse-Hessian response gives Newton's
  method (67). Active as mathematics. Per datum, deterministic,
  explicit-Euler; Adam and momentum are conjectures.
---

# THEORY-1057: Gradient descent with backpropagation, weight decay and Newton's method are one discrete-time semantics of an operad of potential-carrying lenses, in which the state moves by subtracting the sharpened sum of three pulled-back covectors (from the output, from the input wiring and from the potential); the semantics is an operad functor, so a composite's update is assembled from its parts' updates, and backpropagation is that functoriality

## Source

Spivak (2026), [LIT-1649](../literature.d/LIT-1649.md), §§3.3, 4.3, 6.4–6.5 and 7.1–7.2 (pp. 26–28,
33–35, 61–67, 71–76 of arXiv 2606.28984v2); read in [NOTE-1225](../notes.d/NOTE-1225.md).

## What was actually shown

**The functor.** Corollary 3.3.4 (p. 28): "Let (C, I, ⊗, [−, −]) be a
symmetric monoidal closed category. There is a normal lax symmetric monoidal
functor Θ : Lens_C → C, (c⁻, c⁺) ↦ [c⁻, I] ⊗ c⁺." With the cotangent functor
cot : Mfd → Poly (strong symmetric monoidal, Proposition 6.1.2) and an
integrator (Definition 4.3.4), Theorem 4.3.6 gives an operad functor, and
Corollary 6.4.1 (p. 62): "Every cot-integrator 𝔦 induces an operad functor
Φ_𝔦 : ArrSm → PC with Φ_𝔦(1,1) ≅ y; hence it carries closed systems to
y-coalgebras."

**The update.** For an arrangement (Q, f⁺, f⁻, U), the covector at the
parameter is the Q*-component of

(T f⁺)ᵀξ_N + (T f⁻)ᵀω_M(m⁻) + dU, (58), p. 64,

and the configuration integrator sets q ↦ q − ♯_q(ξ_Q), (59), p. 65. "In
other words, the state is updated by summing three covectors pulled back
along the maps in (53) … projecting to the Q*-component, sharpening to a
vector via ♯_q, and subtracting it from the original state" (p. 65).

**The instances.**

- A parameterized map F : Q × ℝᵐ → ℝⁿ with zero potential, composed with a
  stateless loss arrangement, on a Euclidean parameter space with
  ♯_q = η_LR♯_Euc, gives q ↦ q − η_LR(T_q F(◽, x))ᵀξ, "ordinary gradient
  descent at rate η_LR" (76), p. 75. The covector ξ_M returned to the
  input is the backpropagated signal: "Backpropagation is thus the chain
  rule, packaged as the functoriality of Φconf" (p. 75).
- A weight-only potential (γ/2)‖q‖² changes the update to
  q ↦ (1 − η_LR γ)q − η_LR(T_q F(◽, x))ᵀξ (Proposition 7.2.3, p. 76).
- A closed system with response the inverse Hessian, ♯^U_q = (T_q(dU))⁻¹,
  gives q ↦ q − (T_q(dU))⁻¹(dU|_q), one Newton step (67), p. 72, provided
  the Hessian is invertible everywhere.

**Why each box can compute its own update.** The integrator must be a
monoidal natural transformation; "The monoidality of 𝔦 corresponds to the
compositionality of the semantics, that each box can compute its own
update" (p. 63). Naturality, by contrast, can be weakened by shrinking the
parameter category (Remark 6.4.2).

## What this does not say

- **That the training converges or generalizes.** The construction is of
  the update rule, not of its behaviour.
- **That other optimizers are covered.** Adam is a conjecture over a
  smaller parameter category (p. 62); momentum training under Φphase is
  "we expect" (p. 87). Stochastic updates are a proposed extension (p. 88).
- **That this supersedes [THEORY-519](THEORY-519.md).** Fong, Spivak and Tuyéras's
  functor sends the backward message as a requested input and needs an
  invertible error derivative; here the backward message is a covector and
  the loss is an arrangement in the same operad. They are different
  formalizations of the same algorithm, and neither paper derives one from
  the other.
- **Anything for practice.** It is an account of what gradient descent is,
  compositionally, and recommends nothing.
- **Beyond vector-space parameters.** Parameter spaces are responsive vector
  spaces; manifold parameters with connections are conjectured (Remark
  6.3.3).
