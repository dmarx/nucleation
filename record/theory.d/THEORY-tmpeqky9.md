---
status: Proposed
promote_when: >-
  A second source, such as a textbook on stochastic programming or risk
  measures or a later paper, states the same minimization formula for CVaR
  under the same continuity assumption, and states that minimizing it
  jointly yields the CVaR-minimizing decision with the VaR as a minimizer
  in α, and reduces to a linear program for linear losses on finitely many
  scenarios.
title: 'Rockafellar and Uryasev show that the conditional value-at-risk of a loss at level β equals the minimum over α of α + (1−β)⁻¹E[loss − α]⁺, so minimizing it over decisions is a joint minimization that also yields the value-at-risk, convex when the loss is convex in the decision and a linear program on sampled scenarios when the loss is linear'
version: 1
tags:
- operations-research
- mathematics
date: '2026-11-04'
source:
- LIT-tmpdvjiy
summary: >-
  Rockafellar and Uryasev (2000), LIT-tmpdvjiy, read in full in
  NOTE-tmpzgqov from the authors' 1999 manuscript (Theorems 1 and 2 with
  their proofs, §3). Proposed until a second source states the same. It
  holds for loss distributions without atoms, at a fixed β, in one period;
  it says nothing about how large a sample the rare scenarios need, which
  the paper's own examples show can be large.
---

# THEORY-tmpeqky9: Rockafellar and Uryasev show that the conditional value-at-risk of a loss at level β equals the minimum over α of α + (1−β)⁻¹E[loss − α]⁺, so minimizing it over decisions is a joint minimization that also yields the value-at-risk, convex when the loss is convex in the decision and a linear program on sampled scenarios when the loss is linear

## Source

Rockafellar and Uryasev (2000), LIT-tmpdvjiy; read in NOTE-tmpzgqov from the
authors' manuscript of 1999-09-05 (page numbers the manuscript's).

## What was actually shown

- **Theorem 1 (p. 5)**: for fixed x, F_β(x, α) "is convex and continuously
  differentiable" in α; its minimum is the β-CVaR and the left endpoint of
  its set of minimizers the β-VaR. Proved in the Appendix.
- **Theorem 2 (p. 6)**: "Minimizing the β-CVaR of the loss associated with
  x over all x ∈ X is equivalent to minimizing Fβ (x, α) over all (x, α) ∈
  X × IR", the minimizing α being the VaR of the optimal x, and the problem
  is convex "when f (x, y) is convex with respect to x".
- **§3 (p. 9)**: with the expectation replaced by a sample average, F_β is
  piecewise linear, and for losses linear in x the problem is a linear
  program with one auxiliary variable per scenario, whatever the
  distribution.
- Could have come out otherwise: the claim is a theorem, checked in the
  proofs; the numerical examples (a normal portfolio, a non-normal hedge)
  illustrate it and could have shown sampled solutions failing to approach
  the exact ones. They approach them, slowly under pseudo-random sampling.

## What this does not say

- That it holds for distributions with atoms: the paper assumes none and
  leaves that case to later work.
- That a modest sample suffices. At β = 0.99 with 1000 pseudo-random
  samples the CVaR was off by about 5% (Table 5); rare scenarios have to be
  in the sample.
- That minimizing CVaR minimizes VaR. It lowers VaR only in the sense that
  CVaR bounds it.
- Anything about decisions over time, or about losses whose distribution is
  itself unknown, such as those of capacity kept for rare emergencies.
