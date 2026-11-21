---
status: Proposed
title: 'Wei, Zhang, Cousseau, Ozeki and Amari show that in two-layer networks trained by averaged online gradient descent, the flow near an overlap singularity has to leading order a universal first integral whose constant decides whether an orbit reaches the line of overlapping units or passes on to the elimination singularity, as most orbits do; that the line is stable, saddle or split by the signature of a residual matrix, a Milnor-like attractor on which a noise-driven random walk is the on-singularity plateau; and that orbits passing near it cross a flat region where the loss changes only at fourth order, a shorter near-singularity plateau'
promote_when: >-
  The record integrates the averaged equations 3.6–3.7 numerically for a
  definite H and confirms that ½uᵀu − (2w∗²/3) log((z² + 3)²/|z|) is
  constant along orbits and that C₀ = −(8w∗²/3) log 2 separates orbits
  that meet u = 0 from those that do not; and checks Theorem 1's
  stability statement against the paper's Eq. 2.53.
version: 1
tags:
- learning-theory
- loss-landscapes
date: '2026-11-21'
source:
- LIT-3000
summary: >-
  Wei, Zhang, Cousseau, Ozeki and Amari (2008), LIT-3000, read in
  NOTE-tmpl89m0. Orbits, not time courses: a conserved quantity of the
  averaged flow fixes where learning goes near coinciding units, and the
  long plateau on the singularity is a noise-driven walk along a line of
  equivalent models, not a slow decay along a degenerate direction.
---
<!-- inactive-ok-file: LIT-tmp5rr3p — Deferred, registered 2026-11-21 from this reading, unread -->

# THEORY-tmpg4aat: Wei, Zhang, Cousseau, Ozeki and Amari show that in two-layer networks trained by averaged online gradient descent, the flow near an overlap singularity has to leading order a universal first integral whose constant decides whether an orbit reaches the line of overlapping units or passes on to the elimination singularity, as most orbits do; that the line is stable, saddle or split by the signature of a residual matrix, a Milnor-like attractor on which a noise-driven random walk is the on-singularity plateau; and that orbits passing near it cross a flat region where the loss changes only at fourth order, a shorter near-singularity plateau

## Source

Wei, Zhang, Cousseau, Ozeki and Amari, "Dynamics of Learning Near
Singularities in Layered Networks", Neural Computation 20, 813–843
(2008), LIT-3000, read from the published version in NOTE-tmpl89m0.

## What was actually shown

- **Where.** Overlap singularities R(i, j) and elimination singularities
  R(i) are, with their intersections, "the only singular regions" of RBF
  networks and gaussian mixtures (§2.3).
- **Stability** (Theorem 1) by the signature of (1 − z²)H.
- **Orbits** (Theorem 2, Eq. 3.10): h(u) = ½uᵀu = (2w∗²/3)
  log((z² + 3)²/|z|) + C, in Fukumizu and Amari's coordinates
  (LIT-tmp5rr3p); C against C₀ decides whether an orbit meets R₁* or
  passes R₂* (Eq. 3.15); "in most cases, the model parameter reaches R∗2".
- **Two plateaus.** On the singularity: attraction to the stable part of
  R₁*, then "a long period of random walk on R∗1", a "Milnor-like
  attractor", driven by "the fluctuations due to the noise and the random
  sampling of input" (§4.1). Near it: Ė of order u⁴ where z ≈ ±1 (§4.2),
  with Ė < 0 throughout, so it is shorter (p. 839).

## What this does not say

- **Any time course.** No plateau length, escape rate, power law or
  relaxation exponent is derived; of the walk only that "it might take a
  long time for the system to escape". So it is no evidence that slow
  learning near singularities is algebraic relaxation.
- **Anything about deep or wide networks**: two hidden units in the
  analysis and the experiments.
- **Elimination singularities away from overlaps**, which "still remains
  unknown" (§5).
- **Learning coefficients or resolution.**
