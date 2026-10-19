---
status: Active
title: 'Under a local quadratic model of the loss with the greedy optimal step, per-step progress at batch size B is ΔL_max/(1 + B_noise/B), and at fixed B the steps and examples needed satisfy (S/S_min − 1)(E/E_min − 1) = 1, with E_min/S_min the progress-weighted mean of B_noise'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-033 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-033.yaml, batch 018, ADR-047).
    NOTE-293 re-derived eqs. 2.5–2.7 and the hyperbola from App. D.1. The
    derivation is re-derived again below and in the decision file (ADR-047
    v2). The assumptions the authors call unfounded are in the title, so
    this entry claims what follows from them and nothing about whether
    training satisfies them. THEORY-033 keeps the measured prediction,
    Proposed.
tags:
- learning-theory
- mathematics
date: '2026-10-19'
source:
- LIT-348
summary: >-
  McCandlish, Kaplan, Amodei et al. (2018), [LIT-348](../literature.d/LIT-348.md), §2 and App. D.1, as
  read and re-derived in [NOTE-293](../notes.d/NOTE-293.md). A derivation under stated assumptions:
  a second-order model of the loss along the step, an unbiased minibatch
  gradient of covariance Σ/B, and the step size that maximises the
  expected decrease. It says nothing about whether real training meets
  those assumptions, or how well the noise scale predicts the measured
  critical batch, which is [THEORY-033](THEORY-033.md).
extended_by:
- THEORY-033
---
<!-- inactive-ok-file: THEORY-033 — Proposed; the measured account this derivation was split from, not leaned on -->

# THEORY-tmpgjhho: Under a local quadratic model of the loss with the greedy optimal step, per-step progress at batch size B is ΔL_max/(1 + B_noise/B), and at fixed B the steps and examples needed satisfy (S/S_min − 1)(E/E_min − 1) = 1, with E_min/S_min the progress-weighted mean of B_noise

## Source

McCandlish, Kaplan, Amodei & the OpenAI Dota Team (2018), [LIT-348](../literature.d/LIT-348.md),
eqs. 2.2–2.12 and App. D.1, as read in [NOTE-293](../notes.d/NOTE-293.md).

## What was actually shown

A derivation. Write G for the gradient, H for the Hessian and Σ for the
per-example gradient covariance.

1. Let V be the batch gradient, with E V = G and Cov V = Σ/B. To second
   order, L(θ − εV) = L(θ) − ε GᵀV + ½ ε² VᵀHV.
2. Take expectations. E[GᵀV] = |G|², and E[VᵀHV] = GᵀHG + tr(HΣ)/B. The
   expected decrease is ΔL(ε) = ε|G|² − ½ ε² (GᵀHG + tr(HΣ)/B).
3. The maximising step is ε* = |G|²/(GᵀHG + tr(HΣ)/B), and
   ΔL* = ΔL_max/(1 + B_noise/B), with ΔL_max = ½|G|⁴/GᵀHG and
   B_noise = tr(HΣ)/GᵀHG.
4. At fixed B and constant B_noise, a given decrease takes
   S = S_min(1 + B_noise/B) steps and E = SB = S_min(B + B_noise)
   examples, so E_min = S_min·B_noise. Then S/S_min − 1 = B_noise/B and
   E/E_min − 1 = B/B_noise, whose product is 1.
5. When B_noise varies over the run, apply step 4 to each short stretch
   and sum. With ⟨B_noise⟩ the mean of B_noise weighted by the decrease
   each stretch contributes, S/S_min − 1 = ⟨B_noise⟩/B and
   E/E_min − 1 = B/⟨B_noise⟩. The hyperbola is exact ([NOTE-293](../notes.d/NOTE-293.md)).
6. E|V − G|²/|G|² = tr(Σ)/(B|G|²) = B_simple/B. So B_simple is the batch at
   which the gradient's expected squared error equals its squared norm,
   and if H ∝ I then B_noise = B_simple.

What could have come out otherwise: nothing in the algebra. Its content
is that, under these assumptions, examples substitute for steps almost
one-for-one below B_noise and are mostly wasted above it.

## What this does not say

- **That the assumptions hold in training.** The authors call them "many
  unfounded assumptions" (§2.2). The fit across eight tasks is evidence
  for the form, and it belongs to [THEORY-033](THEORY-033.md).
- **That B_crit is predicted.** S_min and E_min are fitted per goal, so
  B_crit is a fitted parameter. How well B_simple tracks it is
  [THEORY-033](THEORY-033.md)'s measured claim.
- **That the knee is a channel-capacity effect.** Progress per step
  saturates at ΔL_max. A Shannon–Hartley log(1 + SNR) does not saturate.
- **Anything about generalisation.** The derivation concerns training
  loss only.
