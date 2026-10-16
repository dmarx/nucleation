---
number: 634
status: Active
formerly:
- THEORY-tmpsuuh4
title: "In a ring of M chemotactic catalyst species, each making the next one's substrate, the non-reciprocal nearest-neighbour coupling makes the linear stability matrix circulant: the uniform state goes unstable for any M exactly when the species attract themselves, and the parity of M then decides the leading mode, a real alternating mode for even M that sorts species by parity into two static clusters, and a complex pair for odd M that can give persistent oscillation"
version: 1
tags:
- complex-systems
- natural-sciences
date: '2026-10-16'
source:
- LIT-036
summary: >-
  Ouazan-Reboul, Agudo-Canalejo & Golestanian (2023), [LIT-036](../literature.d/LIT-036.md), read in
  [NOTE-079](../notes.d/NOTE-079.md). The spectrum is exact for equal parameters (Eq. 5): instability
  iff μ(p) − μ(s) < 0, real leading eigenvalue for M = 2K, complex pair for
  M = 2K + 1. Brownian dynamics at M = 5 and 6 bear out the linear
  predictions; the odd-cycle oscillation is one trajectory at one parameter
  set. Direct metabolic partners repel; same-parity second neighbours
  co-aggregate. The origin-of-life reading is untested, and the authors
  concede in the review file that real catalysts' mobilities are unknown.
---
<!-- inactive-ok-file: THEORY-412 THEORY-492 THEORY-548 — Proposed; accounts that name this paper, or a parallel, cited for context, nothing here rests on their being settled -->

# THEORY-634: In a ring of M chemotactic catalyst species, each making the next one's substrate, the non-reciprocal nearest-neighbour coupling makes the linear stability matrix circulant: the uniform state goes unstable for any M exactly when the species attract themselves, and the parity of M then decides the leading mode, a real alternating mode for even M that sorts species by parity into two static clusters, and a complex pair for odd M that can give persistent oscillation

## Source

Ouazan-Reboul, Agudo-Canalejo & Golestanian (2023), [LIT-036](../literature.d/LIT-036.md), *Nature
Communications*, read in full in [NOTE-079](../notes.d/NOTE-079.md) with the peer-review file.

## What was actually shown

**The model.** M species of catalytic particles on a cycle, all with equal
activity α, mobility μ(s) toward their own substrate and μ(p) toward their
own product, and equal density ρ0. Species m consumes its substrate and
makes species m+1's. So m moves toward m−1, which makes its food, and m−1
moves toward or away from m, which eats its product: the coupling is
non-reciprocal.

**The spectrum (Eqs. 4–5).** With quasi-static chemicals and the q = 0 mode,
the stability matrix is circulant, and Re λ_ℓ = −(αρ0/D)(μ(p) −
μ(s))[1 − cos(2πℓ/M)], Im λ_ℓ = (αρ0/D)(μ(s) + μ(p)) sin(2πℓ/M).

- The uniform state is unstable iff μ(p) − μ(s) < 0, whatever M and the
  chasing strength (Eq. 6).
- **Even M = 2K.** The leading eigenvalue is real, with eigenvector
  (1, −1, 1, …). In simulation at M = 6, single-species clusters form and
  then gather into two "clusters of clusters", one per parity, and mean
  cluster size saturates at N/2 (Fig. 3a, Fig. 1e).
- **Odd M = 2K + 1.** The alternating mode does not exist, and the leading
  pair is complex (Eq. 9). "If two clusters attempt to come together, a
  third will systematically come to break them apart" (p. 4). At M = 5 with
  strong chasing, clusters are invaded by the next species and "explode" in
  a regular sequence, peak clusters holding 20–30% of particles
  (Supplementary Note 2).

**What could have come out otherwise.** The parity effect is exact at
linear order. The nonlinear outcomes could have washed it out; at M = 5 and
6, with ten parameter sets, they did not.

## What this does not say

- **That metabolic partners cluster together.** In the cross-repelling case
  direct partners m and m±1 repel. What co-aggregates is species of the
  same parity. The paper's closing line says otherwise, and [NOTE-079](../notes.d/NOTE-079.md)
  corrects it.
- **That odd cycles always oscillate.** The oscillation needs chasing to
  dominate growth, by an order-of-magnitude criterion (Eq. 11), and was
  shown for one trajectory at M = 5. Larger odd M, such as the citric acid
  cycle's 11, was not simulated.
- **That the result survives unequal parameters.** Every species is
  identical here. The authors cite their own follow-up preprints for
  robustness and show none of it.
- **That this is how metabolism began.** The paper defines no flux, output
  or fitness, so "odd cycles may have an advantage" is undefined. Asked by
  a referee, the authors wrote that "there isn't sufficient information
  about the µ's for specific catalysts … for us to make quantitative
  claims" (Peer Review File, p. 9).
- **That clustering is exponentially fast.** The text says exponential, the
  Fig. 1e caption super-exponential, and the growth law was determined
  "qualitatively".

## Connections

- **Turing's instability ([THEORY-543](THEORY-543.md)).** The same method, linearising
  about a uniform state and reading the growing mode off the eigenvalues,
  with a different mechanism. Here the catalysts, which are conserved,
  self-organise, not the reactants.
- **Delay in random Lotka–Volterra communities ([THEORY-548](THEORY-548.md))** is the
  other route in this group from the structure of an interaction matrix to
  oscillation: there a delay pushes a stable pair across the imaginary
  axis, here a cycle's parity removes the real mode.
- **Driven matter ([THEORY-412](THEORY-412.md))** and **geochemistry forcing metabolism
  ([THEORY-492](THEORY-492.md))** name this paper as a self-organised chemical state.
  It computes no dissipation, so it is neither evidence for nor against
  either.
- **Dissipative structures ([THEORY-692](THEORY-692.md)).** The cycle is a catalytic,
  non-equilibrium system whose uniform state goes unstable, treated by
  linear stability alone, with no entropy-production principle.
