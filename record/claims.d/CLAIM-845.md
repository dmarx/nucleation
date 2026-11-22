---
number: 845
status: Proposed
formerly:
- CLAIM-tmpvrbdt
title: 'Read as a gap in support, a bulk separated from a sparse tail is not what a continuous transition shows from below, where the size distribution falls without a break into an exponential cutoff; a bulk beside a separate population of large sizes belongs to the far side of the transition, as a giant cluster or a major outbreak in a finite system, or to a first-order transition'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A standard model of a continuous transition (branching, percolation, an
  epidemic, an Ising-type model) whose size distribution, on the near side
  of the transition, has a range of sizes between the bulk and the largest
  sizes that is markedly emptier than the sizes on both sides of it, not
  caused by a finite-system bump at the size limit; or an argument that
  "separated" in the owner's sentence cannot mean a gap in support.
tags:
- complex-systems
- probabilistic-modeling
date: '2026-11-21'
line:
- formal-apparatus
grounds:
- CASE-303
- CASE-305
summary: >-
  Reading (a) of the owner's conjecture [CLAIM-840](CLAIM-840.md) (U5 of the exchange
  "Rich Get Richer Power Laws"), filed as the alternative to reading (b),
  [CLAIM-829](CLAIM-829.md). It takes "separated" as a gap in support and checks it.
  Below the transition there is none: the Poisson cascade's size law falls
  strictly at every size, and the cluster-size histograms of 2D site
  percolation at p = 0.50, 0.55 and 0.58 fall over every logarithmic bin,
  with no empty bin. Above it there is one: at p = 0.65 the largest
  cluster holds 62% of the sites and the next 202, and a Reed–Frost
  epidemic of 1,000 at R0 = 1.5 ends either below 100 or near 580 cases,
  with 4 runs in 20,000 in between. This agrees with A's own correction at
  A7 §4. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-840 CLAIM-829 CASE-303 CASE-305 CLAIM-769 — Proposed or new; the owner's conjecture, the other reading, the cases and argument filed with it, and held entries cited as contrasts -->

# CLAIM-845: Read as a gap in support, a bulk separated from a sparse tail is not what a continuous transition shows from below, where the size distribution falls without a break into an exponential cutoff; a bulk beside a separate population of large sizes belongs to the far side of the transition, as a giant cluster or a major outbreak in a finite system, or to a first-order transition

**This is reading (a) of [CLAIM-840](CLAIM-840.md), one of two alternatives.** The
other, reading (b), is [CLAIM-829](CLAIM-829.md). The owner chooses.

## The claim

Take the owner's "a bulk mass separated by a low mass long tail" to mean a
gap: a range of sizes between the bulk and the tail that is much emptier
than the sizes on either side.

**Below a continuous transition there is no such gap.** The size law is a
power times an exponential cutoff, s^(−τ)·e^(−s/s_c), which falls at every
size. On the cases:

- Poisson branching ([CASE-303](../cases.d/CASE-303.md)): the exact law (Borel) is strictly
  decreasing at every s up to 200,000, for R = 0.5, 0.9, 0.99, 0.999 and
  at R = 1.
- 2D site percolation on a 2,000 × 2,000 lattice ([CASE-305](../cases.d/CASE-305.md)): at
  p = 0.50, 0.55 and 0.58 (p_c ≈ 0.5927) the number of clusters per site
  falls across every logarithmic bin, with no empty bin between occupied
  ones; the largest cluster is only 1.2 to 1.4 times the second.

**On the far side, or at a first-order transition, there is one.** At
p = 0.62 and 0.65 the largest cluster holds 55% and 62% of the sites,
while the second largest has 1,385 and 202. Every bin between is empty. In
a Reed–Frost epidemic among 1,000 people ([CASE-305](../cases.d/CASE-305.md)), final sizes at
R0 = 0.8 and 1.0 fall away from one case with no second peak. At
R0 = 1.5 they split into minor outbreaks, nearly all below 100, and a major
peak around 500 to 700 (the final-size equation gives 583). Only 4 of 20,000
runs fall in [200, 400). At R0 = 2 the split runs from below 20 to above
700. Coexisting phases at a first-order transition give the other kind of
two-population distribution. The record holds one such case, Sun and
colleagues' shrub-grass automaton ([THEORY-1825](../theory.d/THEORY-1825.md)).

So, read this way, the owner's pattern belongs to the other side of the
transition, which is what A said at A7 §4: "In a conventional continuous
critical transition, there isn't usually a genuine gap between the bulk
and the tail … A truly separated second population is often a feature of
the **supercritical regime** … Alternatively, an actual bimodal
distribution can occur around certain discontinuous, first-order
transitions." A's table there ("Small-event bulk with rapidly decaying
tail: Subcritical … Two pronounced peaks: Phase coexistence, mixture
processes, or a discontinuous transition") is the diagnostic this claim
rests on, now checked on two models.

## Checked, and how

All figures were computed with `python3 -I` in this session: the Borel
law in closed form, percolation by `scipy.ndimage.label` on random
lattices (seed 20261121), and the epidemic as a chain-binomial simulation.
[CASE-303](../cases.d/CASE-303.md) and [CASE-305](../cases.d/CASE-305.md) give the code.

## What it does not say

- Not that the owner's conjecture is false. On reading (b) it holds
  ([CLAIM-829](CLAIM-829.md)).
- Not that no finite near-critical system ever shows a bump. A finite
  system at or near criticality can pile probability up at its size limit,
  which shows as a bump at the cutoff. That bump is a finite-size effect
  and not a separate population below the transition. It was not checked
  here.
- Not that a bulk plus a heavy tail implies any transition. A mixture of
  exponential rates gives one with none ([CLAIM-769](CLAIM-769.md)).
