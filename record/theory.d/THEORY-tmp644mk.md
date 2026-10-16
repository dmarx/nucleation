---
status: Proposed
promote_when: >-
  A proof that, for some non-Gaussian ensemble in the paper's class, such as
  random signs, the ℓ₁ recovery transition converges to the Gaussian
  ρ(δ; C) as N → ∞; or simulations at problem sizes an order of magnitude
  beyond N = 1600 in which the gap to the Gaussian curve keeps shrinking as
  N^(−1/2) for an ensemble not used to choose that exponent. More
  simulations at the same sizes do not settle it.
title: 'Recovery of a k-sparse vector by ℓ₁ minimization from n random measurements in dimension N switches, as N grows with δ = n/N and ρ = k/n fixed, from near-certain success to near-certain failure across a curve ρ(δ) that face counts of randomly projected polytopes fix for Gaussian matrices; eight non-Gaussian ensembles were observed to approach the same curve, with gaps shrinking as N^(−1/2), while at finite N the location depends on the ensemble'
version: 1
tags:
- mathematics
- mathematical-statistics
date: '2026-10-16'
source:
- LIT-tmpwlsvo
answers:
- QUESTION-tmpa0dq9
summary: >-
  Donoho and Tanner (2009), [LIT-tmpwlsvo](../literature.d/LIT-tmpwlsvo.md), read in [NOTE-tmpw0lqu](../notes.d/NOTE-tmpw0lqu.md) from arXiv
  0906.2530v1. The Gaussian transition is a theorem of the authors' earlier
  papers, restated here. The universality is an observation from 2,948,000
  optimizations at N = 200, 400 and 1600: strict finite-N universality is
  rejected, and agreement as N → ∞ is not rejected. Sparse and Hadamard
  matrices sit about one transition width low at small N. Proposed because
  the asymptotic claim rests on three problem sizes and an exponent chosen
  on the same data.
---

# THEORY-tmp644mk: Recovery of a k-sparse vector by ℓ₁ minimization from n random measurements in dimension N switches, as N grows with δ = n/N and ρ = k/n fixed, from near-certain success to near-certain failure across a curve ρ(δ) that face counts of randomly projected polytopes fix for Gaussian matrices; eight non-Gaussian ensembles were observed to approach the same curve, with gaps shrinking as N^(−1/2), while at finite N the location depends on the ensemble

## Source

Donoho and Tanner (2009), [LIT-tmpwlsvo](../literature.d/LIT-tmpwlsvo.md), *Phil. Trans. R. Soc. A* 367,
read in [NOTE-tmpw0lqu](../notes.d/NOTE-tmpw0lqu.md) from the 48-page arXiv text; the 21-page journal
version could not be fetched.

## What was actually shown

**The Gaussian case (Theorem 2.1, proved elsewhere).** For A n × N with
iid N(0, 1) entries, n = δN, k = ρn and N → ∞, the expected fraction of
k-faces of the cross-polytope (or simplex) that survive projection by A
tends to 1 for ρ < ρ(δ; Q) and to 0 above it. By Lemmas 2.1–2.2 that
fraction is the success rate of ℓ₁ recovery (or nonnegative recovery by
linear programming). No formula is given; the figures print values such as
ρ(δ; C) = 0.189 at δ = 0.1 and 0.3848 at δ = 0.5. The finite-N transition
width is about 0.65/√N.

**The study.** 2,948,000 optimizations over 16,984 settings, eight
non-Gaussian ensembles with two coefficient types, at N = 200, 400 and
1600.

**The findings.** Z-scores against the Gaussian lie mostly in [−2, 2].
Strict universality at finite N is rejected: the mean Z-score trends with
δ. Weak universality, a difference of O(N^(−1/2)), is not rejected:
adding non-decaying terms gives F = 0.7467, p = 0.7475, and γ = 1/2 fits
best among the exponents tried, chosen on the same data. Random signs,
analysed after the model was fixed, fit it out of sample. Ternary(1/10),
Expander and Hadamard sit about one transition width low at small N,
because their columns are not in general position; the effect is gone by
N = 1600 for the first two.

**What could have come out otherwise.** A non-Gaussian ensemble whose gap
to the Gaussian curve stopped shrinking with N would refute the asymptotic
claim. At the sizes tried, none did.

## What this does not say

- **That universality is proved.** The authors say the result "goes far
  beyond current theory". The universality class is not delineated.
- **That the location is ensemble-free at any finite N.** It is not.
- **Anything about other decoders.** The curves are for ℓ₁ and linear
  programming recovery only.
- **That the transition is a union-bound threshold.** It is an exact
  limiting location from counting faces. Union-bound arguments
  ([THEORY-tmp4mezl](THEORY-tmp4mezl.md)) give the same order, k ≍ n/log(N/n), not the curve.
- **That the superposition toy model's phase changes are this
  transition.** [NOTE-278](../notes.d/NOTE-278.md) asks the question; nothing here answers it.

## Connections

- [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md): the superposition thread. The transition gives the sharp location
  that a sufficiency bound like [THEORY-tmp4mezl](THEORY-tmp4mezl.md) only brackets in order.
  It is not of the question's proposed shape.
