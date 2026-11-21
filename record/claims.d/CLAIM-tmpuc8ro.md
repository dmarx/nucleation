---
status: Proposed
title: 'A population of independent factored modes q = ab with zero target, started small and at random, relaxes on average as a power law with a logarithmic correction, though almost every mode relaxes exponentially: each mode''s rate is set by its conserved imbalance a² − b², and those rates reach down to zero with a density that does not vanish there'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation or the computation: the closed form
  |q(t)| = |D| / (2 sinh(asinh(|D|/2|q₀|) + 2|D|t)) failing to solve the
  flow of K = a²b², or the population mean of |q| from independent
  Gaussian starts not approaching the exponent −2 (and of K the exponent
  −3) as t grows. That a real network's factored modes are coupled or
  have nonzero targets does not defeat the claim, which is about the
  stated population; it limits what the claim can explain.
tags:
- learning-theory
- complex-systems
- mathematics
date: '2026-11-21'
line:
- learned-structure
rests_on:
- CLAIM-tmpcbfdj
grounds:
- CASE-152
summary: >-
  Fills a gap the ledger found in A39's claim that singular modes could
  stand in for critical slowing (CLAIM-tmpv5asv) in the exchange "Rich Get
  Richer Power Laws" (2026-11-21): A gives no step from one algebraic mode
  to a broad distribution of timescales. This is one step, derived and
  checked numerically. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmpcbfdj CLAIM-tmpv5asv CLAIM-tmp9bp04 — Proposed; filed with this claim -->

# CLAIM-tmpuc8ro: A population of independent factored modes q = ab with zero target, started small and at random, relaxes on average as a power law with a logarithmic correction, though almost every mode relaxes exponentially: each mode's rate is set by its conserved imbalance a² − b², and those rates reach down to zero with a density that does not vanish there

## The claim

Take K = a²b², a dormant feature whose target is zero (A37 §2; CASE-152's
model). Gradient flow ȧ = −2ab², ḃ = −2a²b conserves D = a² − b². The
product q = ab obeys q̇ = −2q√(D² + 4q²), which integrates to

  |q(t)| = |D| / (2 sinh(asinh(|D|/(2|q₀|)) + 2|D|t)).

At D = 0 this is q₀/(1 + 4q₀t), the balanced line's algebraic decay
(CLAIM-tmpcbfdj). For D ≠ 0 it is algebraic until t ≈ 1/|D|, then
exponential at rate 2|D|.

Now take many independent modes started at a, b ∼ N(0, σ²). The rate 2|D|
varies from mode to mode, and D = (a − b)(a + b) is a product of two
independent Gaussians, whose density diverges logarithmically at 0. The
population mean is therefore dominated at late times by the modes with
|D| ≲ 1/t, whose share falls like (log t)/t. So ⟨|q|⟩ ∼ (log σ²t)/t² and
⟨K⟩ ∼ (log σ²t)/t³: power laws with logarithmic corrections, although only
a measure-zero set of modes relaxes algebraically.

## The check

The assistant's, with `python3 -I` (`t5/check4.py`). The closed form
matches numerical integration of the flow from (0.3, 0.2) to seven digits
at t = 1, 10, 50. A population of 2 × 10⁶ modes with σ = 0.1 gives local
exponents of ⟨|q|⟩ of −1.42, −1.60, −1.70, −1.77, −1.82, −1.85, −1.87,
−1.88, −1.89 at t = 3 × 10², 10³, …, 3 × 10⁶. For ⟨K⟩ they are −2.34 to
−2.90. Both approach −2 and −3 as −2 + 1/ln(σ²t) and −3 + 1/ln(σ²t) predict:
at t = 10⁵, −1.855 against −1.853 observed, and −2.855 against −2.844.

## What it shows

It answers the ledger's gap at CLAIM-tmpv5asv: a step from single
singular modes to a power law in aggregate relaxation. The step needs no
criticality, no hierarchy of degeneracies and no tuning, only factored
parameters, a small random start and a zero target. The exponent is set by
how the density of the conserved quantity behaves at zero, not by any
learning coefficient: every mode here has λ = ½ and m = 2.

## What it does not say

- That the power laws seen in training come from this. Real modes are
  coupled, have nonzero targets, and train under noise and weight decay,
  which breaks the conservation of D (CLAIM-tmp9bp04's objective does).
- That the exponent is universal. A different start, for example a
  balanced one (D ≡ 0), gives ⟨|q|⟩ ∼ 1/(4t) instead.
- That rates distributed down to zero are new as a source of power laws:
  that is the general mechanism of superposed exponentials. What is
  specific is that factored parameters supply the distribution through a
  conserved quantity.
