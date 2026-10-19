---
number: 391
status: Active
formerly:
- THEORY-tmp644mk
title: 'Recovery of a k-sparse vector by ℓ₁ minimization from n random measurements in dimension N switches, as N grows with δ = n/N and ρ = k/n fixed, from near-certain success to near-certain failure across a curve ρ(δ) that, for Gaussian matrices, the authors'' earlier face-counting theorems fix; in 2,948,000 optimizations at N = 200, 400 and 1600, eight non-Gaussian ensembles approached that curve in a way consistent with gaps shrinking as N^(−1/2), an exponent fitted on the same data, while at finite N the location depended on the ensemble'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-391 (batch 025, ADR-047 v3). NOTE-933 read the study in full, and
    every number the title rests on is in its text and tables. The title now
    attributes the Gaussian transition to the earlier theorems the paper
    restates, which the record does not hold. It also says the N^(−1/2)
    exponent was fitted on the same data. The promote_when, a proof or larger
    simulations, moves unchanged to QUESTION-168.
tags:
- mathematics
- mathematical-statistics
date: '2026-10-16'
source:
- LIT-1160
answers:
- QUESTION-120
summary: >-
  Donoho and Tanner (2009), [LIT-1160](../literature.d/LIT-1160.md), read in [NOTE-933](../notes.d/NOTE-933.md) from arXiv
  0906.2530v1. The Gaussian transition is a theorem of the authors' earlier
  papers, restated here. The universality is an observation from 2,948,000
  optimizations at N = 200, 400 and 1600: strict finite-N universality is
  rejected, and agreement as N → ∞ is not rejected. Sparse and Hadamard
  matrices sit about one transition width low at small N. The title states
  only what was measured. Whether the agreement is a limit theorem is
  QUESTION-168.
---

# THEORY-391: Recovery of a k-sparse vector by ℓ₁ minimization from n random measurements in dimension N switches, as N grows with δ = n/N and ρ = k/n fixed, from near-certain success to near-certain failure across a curve ρ(δ) that, for Gaussian matrices, the authors' earlier face-counting theorems fix; in 2,948,000 optimizations at N = 200, 400 and 1600, eight non-Gaussian ensembles approached that curve in a way consistent with gaps shrinking as N^(−1/2), an exponent fitted on the same data, while at finite N the location depended on the ensemble

## Source

Donoho and Tanner (2009), [LIT-1160](../literature.d/LIT-1160.md), *Phil. Trans. R. Soc. A* 367,
read in [NOTE-933](../notes.d/NOTE-933.md) from the 48-page arXiv text; the 21-page journal
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
  ([THEORY-390](THEORY-390.md)) give the same order, k ≍ n/log(N/n), not the curve.
- **That the superposition toy model's phase changes are this
  transition.** [NOTE-278](../notes.d/NOTE-278.md) asks the question; nothing here answers it.

## Connections

- [QUESTION-120](../questions.d/QUESTION-120.md): the superposition thread. The transition gives the sharp location
  that a sufficiency bound like [THEORY-390](THEORY-390.md) only brackets in order.
  It is not of the question's proposed shape.
