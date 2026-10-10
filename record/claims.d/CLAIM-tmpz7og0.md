---
status: Active
title: 'Approximate transports compose into a category only if the distortion obeys a triangle inequality and later kernels are nonexpansive, so the semigroup claim''s "category or semigroup" holds for exact kernels, and for approximate ones only under those conditions'
version: 1
role: granted
tags:
- mathematics
- probabilistic-modeling
date: '2026-10-10'
line: pragmatic-transport
objects_to:
- CLAIM-098
uses:
- TERM-008
summary: >-
  Found in the record's audit of the line on 2026-10-10 (formal lens); no
  turn of the exchange raises it. [TERM-008](../terms.d/TERM-008.md)'s founding sense is a
  transport that gets "within some eps", and [CLAIM-106](CLAIM-106.md) makes fidelity
  graded. Kernels always compose, but the composite of an ε₁-transport
  and an ε₂-transport is an (ε₁ + ε₂)-transport only if the distortion
  obeys a triangle inequality and the second kernel is nonexpansive. In
  total variation both hold. [QUESTION-017](../questions.d/QUESTION-017.md) holds the triangle inequality
  open and does not tie it to the category claim. Granted, because it is
  elementary. It does not say the category claim fails for exact
  transports or in total variation.
---
<!-- inactive-ok-file: CLAIM-098 — Proposed; open, and cited as the claim this objection is to -->
<!-- inactive-ok-file: CLAIM-106 CLAIM-059 — Proposed; the graded-fidelity and regimes claims, cited as open -->

# CLAIM-tmpz7og0: Approximate transports compose into a category only if the distortion obeys a triangle inequality and later kernels are nonexpansive, so the semigroup claim's "category or semigroup" holds for exact kernels, and for approximate ones only under those conditions

## The objection

[CLAIM-098](CLAIM-098.md) quotes the manuscript's §4: "The more inclusive notion is a
category or semigroup of stochastic transformations", and among the cases
it separates is "(iii) approximate preservation". [TERM-008](../terms.d/TERM-008.md)'s founding sense
is approximate. U20: "there should be some transport map that at least gets
to within some eps". [CLAIM-106](CLAIM-106.md) makes fidelity graded.

Exact kernels compose: a Markov kernel followed by a Markov kernel is one.
What a category of approximate transports needs is more. Its arrows carry
their distortion, and the distortion of a composite has to be bounded by
the parts. Let T₁ take A to B with d(K₁#e_A, e_B) ≤ ε₁, and T₂ take B to C
with d(K₂#e_B, e_C) ≤ ε₂. Then

d(K₂K₁#e_A, e_C) ≤ d(K₂#(K₁#e_A), K₂#e_B) + d(K₂#e_B, e_C) ≤ Lε₁ + ε₂,

where the first step is the triangle inequality and L is how much K₂ can
stretch distances in d. The composite is an (ε₁ + ε₂)-transport when d
obeys the triangle inequality and L ≤ 1. Without either, it need not be.

- **No triangle inequality.** Let d be the squared difference of Bernoulli
  parameters, d(p, q) = (p − q)², and let both kernels be the identity.
  With e_A, e_B and e_C the Bernoulli laws with parameters 0, 1/2 and 1,
  ε₁ = ε₂ = 1/4, and the composite's distortion is 1, which exceeds
  ε₁ + ε₂ = 1/2. Squared Hellinger distance does the same on these three
  laws: each step costs 1 − √(1/2), about 0.29, and the composite costs 1.
- **An expansive kernel.** In the Wasserstein-1 distance on the real line,
  the deterministic kernel x ↦ 2x doubles every distance. The composite is
  then only a (2ε₁ + ε₂)-transport.

In total variation both conditions hold. It is a metric, and every Markov
kernel is nonexpansive in it, which is [CLAIM-059](CLAIM-059.md)'s point: "For Markov
kernels acting on probability measures under total variation distance, the
contraction coefficient is at most one." So the gap is for the other
distortions, and [CLAIM-059](CLAIM-059.md) says amplification needs one: "Amplification
requires a different metric, an expanded state model, or an appropriate
state-dependent dynamics." [QUESTION-017](../questions.d/QUESTION-017.md) holds the triangle inequality open,
quoting C6 Appendix B that the distortion "does not obey a triangle
inequality unless the chosen constructions guarantee one". It does not tie
that to the category claim.

## What it does not say

- It does not say the category claim fails for exact transports, or for
  total variation with Markov kernels.
- It does not say approximate transports fail to compose. Their kernels
  always compose. What can fail is the bound on the composite's
  distortion, so [CLAIM-098](CLAIM-098.md)'s (iii) sits in the category only once the
  distortion measure is fixed and meets the two conditions.
