---
number: 861
status: Active
formerly:
- THEORY-tmpwl9bj
title: 'When a deployed model changes the distribution it is scored on, retraining on the distribution the last model induced contracts at rate εβ/γ, for a β-jointly smooth, γ-strongly convex loss and a distribution map that is ε-Lipschitz in Wasserstein-1 distance, and so converges to a unique performatively stable point when ε < γ/β; each condition is needed, since dropping strong convexity, joint smoothness or the bound on ε each admits a case where retraining never converges'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-1044. The result is Perdomo et al.'s
    Theorem 3.5 and Proposition 3.6. The proof of Theorem 3.5 and the
    counterexamples (a) and (c) were re-derived below, which meets the
    condition for Active under ADR-047 v2.
tags:
- learning-theory
- causality
date: '2026-10-21'
source:
- LIT-1336
summary: >-
  Perdomo, Zrnic, Mendler-Dünner and Hardt (2020), [LIT-1336](../literature.d/LIT-1336.md), read in
  [NOTE-1044](../notes.d/NOTE-1044.md). Retraining under performativity is a fixed-point
  iteration, and these are the conditions for it to settle. Its fixed
  point is self-consistent, not optimal ([THEORY-839](THEORY-839.md)), and outside
  the conditions there may be several or none.
---
<!-- inactive-ok-file: CLAIM-402 — Proposed; filed from the same exchange, the claim this account bears on, cited as open -->

# THEORY-861: When a deployed model changes the distribution it is scored on, retraining on the distribution the last model induced contracts at rate εβ/γ, for a β-jointly smooth, γ-strongly convex loss and a distribution map that is ε-Lipschitz in Wasserstein-1 distance, and so converges to a unique performatively stable point when ε < γ/β; each condition is needed, since dropping strong convexity, joint smoothness or the bound on ε each admits a case where retraining never converges

## Source

Perdomo, Zrnic, Mendler-Dünner and Hardt (2020), ICML 2020,
[LIT-1336](../literature.d/LIT-1336.md), read in full in [NOTE-1044](../notes.d/NOTE-1044.md) from arXiv v4: Theorem 3.5
(proof in Appendix D.1) and Proposition 3.6 (§3.2 and Appendix D.2). The
re-derivation below follows the paper's proof.

## What was actually shown

Let G(θ) = argmin_φ E_{Z∼D(θ)} ℓ(Z; φ), so retraining is θ_{t+1} = G(θ_t)
and a stable point is a fixed point of G. Fix θ, θ′, and let
f(φ) = E_{D(θ)} ℓ(Z; φ), f′(φ) = E_{D(θ′)} ℓ(Z; φ), and Δ = G(θ) − G(θ′).

1. **Strong convexity.** G(θ) minimizes the γ-strongly convex f, so
   f(G(θ)) − f(G(θ′)) ≥ Δᵀ∇f(G(θ′)) + (γ/2)‖Δ‖² and
   f(G(θ′)) − f(G(θ)) ≥ (γ/2)‖Δ‖². Adding: −γ‖Δ‖² ≥ Δᵀ∇f(G(θ′)).
2. **The shift.** z ↦ Δᵀ∇_θℓ(z; G(θ′)) is β‖Δ‖-Lipschitz by (A1) and
   Cauchy–Schwarz. By Kantorovich–Rubinstein and ε-sensitivity, its means
   under D(θ) and D(θ′) differ by at most β‖Δ‖ · ε‖θ − θ′‖. So
   Δᵀ∇f(G(θ′)) ≥ Δᵀ∇f′(G(θ′)) − εβ‖Δ‖‖θ − θ′‖.
3. **Optimality.** G(θ′) minimizes f′ over the convex Θ, so
   Δᵀ∇f′(G(θ′)) ≥ 0.

Together, −γ‖Δ‖² ≥ −εβ‖Δ‖‖θ − θ′‖, so ‖G(θ) − G(θ′)‖ ≤ (εβ/γ)‖θ − θ′‖.
For ε < γ/β, G is a contraction on the closed set Θ, and Banach's theorem
gives a unique fixed point θ_PS with ‖θ_t − θ_PS‖ ≤ (εβ/γ)^t ‖θ₀ − θ_PS‖.

**Each condition is needed** (Proposition 3.6).

- (a) Convex, not strongly: ℓ = βyθ on [−1, 1] with Y a point mass at εθ.
  DPR(θ, φ) = εβθφ is minimized at φ = −sign(θ), so any start other than
  0 gives …, 1, −1, 1, … The unique stable point 0 is never reached.
- (c) ε = γ/β or more: ℓ = (y − θ)², so β = γ, with Y a point mass at
  1 + εθ. G(θ) = 1 + εθ contracts by exactly ε. For ε > 1 the iterates
  θ_t = (ε^t − 1)/(ε − 1) + θ₀ε^t diverge from θ_PS = 1/(1 − ε), and at
  ε = 1 no stable point exists. The bound in Theorem 3.5 is attained.
- (b) Strongly convex, not jointly smooth: a regularized hinge
  C·max(−1, yθ) + (γ/2)(θ − 1)² with large C oscillates (Appendix D.2;
  read, not re-derived).

What could have failed: the shift in distribution enters through the
gradient's dependence on z. Without joint smoothness the same W₁ shift
could move the gradient arbitrarily, and (b) shows that happening.

## What this does not say

- **Not that the stable point is good.** It is optimal only for the
  distribution it induces. Its distance from the performative optimum is
  [THEORY-839](THEORY-839.md), and the two can differ by a factor of two or more
  (Example 2.2).
- **Not that the stable point says what other policies would produce.**
  Retraining samples D(θ_t) only at the visited θ_t.
- **Not uniqueness outside the conditions.** A threshold rule or any
  discrete classifier is not strongly convex. Several stable points, or
  none (Example 3.4), are then possible.
- **Not the finite-sample or gradient versions.** Theorems 3.8 and 3.10
  extend it under tighter bounds on ε and were read, not checked.
- **Not a history-dependent world.** D(·) depends only on the current
  model.

## Connections

- **[CLAIM-402](../claims.d/CLAIM-402.md).** A26 §2's two-fixed-point toy is outside these
  conditions, which is why it can have two. A fixed point "consistent with
  the behavioral evidence generated under that classification" is a
  performatively stable point.
- **[CLAIM-409](../claims.d/CLAIM-409.md) and [CLAIM-407](../claims.d/CLAIM-407.md)** concern what a description keeps
  under dynamics and under intervention. This is the learning-side case:
  a model fitted on the data its own use produces converges to
  self-consistency, and the conditions above are when it does.
