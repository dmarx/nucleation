---
status: Active
title: 'A model optimal for the distribution its own deployment induces, a performatively stable point, need not minimize the risk it actually incurs, and the gap is bounded: for a loss that is L_z-Lipschitz in the data and γ-strongly convex in the parameters, and a distribution map that is ε-Lipschitz in Wasserstein-1 distance, every stable point lies within 2L_zε/γ of every performative optimum; in a biased-coin example the stable point is µ/(1 − ε) and the optimum µ/(1 − 2ε), equal only when the prediction has no effect'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-tmpmuo87. The bound is Perdomo et al.'s
    Theorem 4.3, the example their Example 2.2, the non-convexity their
    Proposition 4.2. All three were re-derived below and the example
    checked numerically, which meets the condition for Active under
    ADR-047 v2.
tags:
- learning-theory
- causality
date: '2026-10-21'
source:
- LIT-tmpwbhro
summary: >-
  Perdomo, Zrnic, Mendler-Dünner and Hardt (2020), [LIT-tmpwbhro](../literature.d/LIT-tmpwbhro.md), read in
  [NOTE-tmpmuo87](../notes.d/NOTE-tmpmuo87.md). Self-consistency under one's own influence and the best
  outcome under that influence are different targets. The bound says they
  are close when the influence is weak relative to the loss's curvature.
  It does not say how to find the optimum, which needs the distribution map
  away from the deployed model.
---
<!-- inactive-ok-file: CLAIM-tmpeftzb — Proposed; filed from the same exchange, the claim this account bears on, cited as open -->

# THEORY-tmp9lnfi: A model optimal for the distribution its own deployment induces, a performatively stable point, need not minimize the risk it actually incurs, and the gap is bounded: for a loss that is L_z-Lipschitz in the data and γ-strongly convex in the parameters, and a distribution map that is ε-Lipschitz in Wasserstein-1 distance, every stable point lies within 2L_zε/γ of every performative optimum; in a biased-coin example the stable point is µ/(1 − ε) and the optimum µ/(1 − 2ε), equal only when the prediction has no effect

## Source

Perdomo, Zrnic, Mendler-Dünner and Hardt (2020), ICML 2020,
[LIT-tmpwbhro](../literature.d/LIT-tmpwbhro.md), read in full in [NOTE-tmpmuo87](../notes.d/NOTE-tmpmuo87.md) from arXiv v4: Example 2.2,
Proposition 4.2 (Appendix D.6) and Theorem 4.3 (Appendix D.7). The
re-derivations below are the record's, following the paper.

## What was actually shown

Write DPR(θ, θ′) = E_{Z∼D(θ)} ℓ(Z; θ′). θ_PO minimizes DPR(θ, θ); θ_PS
minimizes DPR(θ_PS, ·).

**They differ.** Example 2.2: X uniform on {±1}, Y | X ~
Bernoulli(½ + µX + εθX), predictor θx + ½, squared loss. Since
E[Y − ½ | X] = (µ + εθ)X, X² = 1 and (Y − ½)² = ¼,

DPR(θ, θ′) = ¼ − 2θ′(µ + εθ) + θ′².

Optimizing θ′ for fixed θ gives θ′ = µ + εθ, whose fixed point is
θ_PS = µ/(1 − ε). Setting θ′ = θ gives PR(θ) = ¼ − 2µθ + (1 − 2ε)θ², so
θ_PO = µ/(1 − 2ε) for ε < ½. They coincide iff ε = 0. At µ = 0.2,
ε = 0.3, retraining converged to 0.2857 = θ_PS, while θ_PO = 0.5, with
performative risks 0.168 and 0.150. For ε ∈ [½, 1), PR is concave in θ,
although ε < γ/β = 1, so retraining converges and direct minimization of
PR is non-convex (Proposition 4.2).

**The gap is bounded.** Let d = ‖θ_PO − θ_PS‖.

- Strong convexity and the first-order condition at θ_PS (Lemma C.1)
  give DPR(θ_PS, θ_PO) − DPR(θ_PS, θ_PS) ≥ (γ/2)d².
- ℓ(·; θ_PO) is L_z-Lipschitz in z, so by Kantorovich–Rubinstein and
  ε-sensitivity, DPR(θ_PS, θ_PO) − DPR(θ_PO, θ_PO) ≤ L_zεd.
- Optimality of θ_PO gives DPR(θ_PO, θ_PO) ≤ DPR(θ_PS, θ_PS).

So (γ/2)d² ≤ DPR(θ_PS, θ_PO) − DPR(θ_PS, θ_PS) ≤ DPR(θ_PS, θ_PO) −
DPR(θ_PO, θ_PO) ≤ L_zεd, and d ≤ 2L_zε/γ. It holds for every stable point
and every optimum, so neither need be unique.

What could have failed: stability is a condition at one point, optimality
a condition over all deployments, and nothing forces them near each other
in general. Strong convexity in θ and Lipschitz dependence on z are what
tie them.

## What this does not say

- **Not that stable points exist.** Existence needs Theorem 3.5's
  conditions ([THEORY-tmpwl9bj](THEORY-tmpwl9bj.md)) or Proposition 4.1's compactness and
  convexity.
- **Not how to find the optimum.** θ_PO depends on how D(θ) varies away
  from the deployed model, which retraining never observes.
- **Not a bound in risk.** Corollary 5.1 converts it to risk when ℓ is
  also L_θ-Lipschitz in θ, giving 2L_zε(L_θ + L_zε)/γ.
- **Not that a stable model is wrong.** It is calibrated for the world it
  makes. A26: "A performatively stable model isn't necessarily false,
  unjust, or captured."

## Connections

- **[CLAIM-tmpeftzb](../claims.d/CLAIM-tmpeftzb.md).** A category confirmed by the outcomes its own use
  produces is the stable point. This shows the stable point can be a worse
  choice than an alternative that would have produced different evidence.
  That is the claim's reason to model the effect of use, made exact in
  one family of models.
- **[CLAIM-tmppi0xf](../claims.d/CLAIM-tmppi0xf.md).** Closure under ordinary dynamics does not preserve
  intervention responses. In the same spirit, optimality under the
  deployed distribution does not give optimality under the map D(·).
