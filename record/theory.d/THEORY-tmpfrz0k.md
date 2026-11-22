---
status: Proposed
promote_when: >-
  The published Science text is confirmed to carry the results the title
  gives as the preprint states them (a lawful copy of the print version,
  or a later statement by the authors), and an independent simulation of
  the model and of Models A and B reproduces a stationary tail near
  k^(−3), an exponential without preferential attachment and a
  non-stationary distribution without growth. Not met, and not defeated,
  by tests of whether real networks are scale free, which bear on the
  proposal's reach and not on what the paper found.
title: 'Barabási and Albert, growing a network one vertex at a time with links attached in proportion to degree, find a stationary power-law degree distribution with exponent near 3 by simulation and exactly 3 by a mean-field argument, an exponential distribution without preferential attachment, a non-stationary one tending to a complete graph without growth, and scaling only for a linear kernel, and propose growth and preferential attachment as the generic origin of the power-law tails they report in real networks'
version: 1
tags:
- network-science
- complex-systems
date: '2026-11-22'
source:
- LIT-3004
bears_on:
- QUESTION-505
summary: >-
  Barabási & Albert (1999), LIT-3004, read in the arXiv preprint in
  NOTE-tmpwgw8e. The record's source for the base case of CLAIM-817 and
  the premise of CLAIM-830, and for A3's sentence that attachment alone
  does not guarantee a power law (ARG-tmp3q9cy). The sharp edge: the
  proposal that the mechanism is generic rests on four networks whose
  slopes were drawn by eye, the premise Broido and Clauset test
  (THEORY-tmphcnj3). Proposed until the print text and a replication
  confirm it.
---
<!-- inactive-ok-file: THEORY-tmpmsncg THEORY-tmpzmy66 — Proposed; the readings beside this one -->
<!-- inactive-ok-file: CLAIM-817 CLAIM-830 THEORY-tmphcnj3 ARG-tmp3q9cy — Proposed or new; the claims this reading grounds, the reading that qualifies its premise and the argument that says how -->

# THEORY-tmpfrz0k: Barabási and Albert, growing a network one vertex at a time with links attached in proportion to degree, find a stationary power-law degree distribution with exponent near 3 by simulation and exactly 3 by a mean-field argument, an exponential distribution without preferential attachment, a non-stationary one tending to a complete graph without growth, and scaling only for a linear kernel, and propose growth and preferential attachment as the generic origin of the power-law tails they report in real networks

## Source

Barabási & Albert (1999), "Emergence of Scaling in Random Networks",
Science 286, 509, LIT-3004, read in the arXiv preprint (cond-mat/9910332)
in NOTE-tmpwgw8e.

## What was actually shown

A model: at every step "a new vertex with m(≤ m0) edges" attaches with
Π(k_i) = k_i/Σ_jk_j. Simulation: "an exponent γmodel = 2.9±0.1", with
"P(k) ... independent of time". Mean field: ∂k_i/∂t = k_i/2t,
k_i = m(t/t_i)^(1/2), and with vertices added "at equal time intervals"
P(k) = 2m²/k³, "giving γ = 3, independent of m". Model A, without
preference, "leads to P(k) ∼ exp(−βk)". Model B, without growth, shows
power-law scaling "at early times" but "P(k) is not stationary", and all
vertices end connected. Hence "both ingredients ... are needed"; and
"simulations indicate that scaling is present only for α = 1" (p. 7).

What could have come out otherwise: Models A and B could have kept the
tail. They do not, which is what makes the two ingredients jointly needed
in this model.

## What this does not say

- Not that real networks are scale free with γ = 3. The four empirical
  exponents (2.1 to about 4) are slopes drawn on log–log plots with no fit
  or test, and the model gives 3.
- Not a derivation of the nonlinear-kernel regimes; that is one sentence
  on simulations, and the regimes are Krapivsky, Redner and Leyvraz's
  (THEORY-tmpmsncg).
- Not that Model B never shows a power law: it does, transiently.
- Not that 3 is exact for the stochastic model; the exact distribution
  (2m(m+1)/[k(k+1)(k+2)]) is later work (THEORY-tmpzmy66).
