---
status: Proposed
title: 'For a chain with symmetric rates ε to the power U on a connected graph of n states and E edges, the log commute time between two states lies within log max(E, n − 1) of log n plus log(1/ε) times their minimax barrier, an ultrametric; so the time geometry of the state space is hyperbolic in Gromov''s four-point sense with δ bounded independently of ε while its distances grow as log(1/ε), and as time scales separate it becomes the tree of classes reachable within a budget'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: in the identity κ = n·R_eff for a chain
  with symmetric rates and uniform stationary law; in the series bound
  R_eff ≤ (n − 1)ε^(−u) along a minimax path; in the cut bound
  R_eff ≥ ε^(−u)/E across the boundary of the states reachable from i by
  edges with U < u; in the minimax barrier being an ultrametric; or in
  the step from additive distance c to an ultrametric to four-point
  hyperbolicity δ ≤ 2c.
tags:
- mathematics
- complex-systems
- network-science
date: '2026-11-20'
line:
- formal-apparatus
- distributed-agency
rests_on:
- CLAIM-581
summary: >-
  The link the record lacked between dynamical hierarchy (levels marked by
  rate gaps, THEORY-1306, THEORY-1558, CLAIM-478) and geometric
  hyperbolicity (THEORY-193, THEORY-196): separated time scales make the
  log commute-time geometry of a state space tree-like, and the tree is
  the one CLAIM-581 builds from peak-capacity thresholds. Proved by
  electrical-network bounds and checked numerically. The owner asked
  (2026-11-20) whether the record could "formalize the relationship
  between hierarchy and hyperbolicity". Results of this kind belong to
  Freidlin–Wentzell metastability theory, which the record does not hold
  (LEAD-tmpdv2tt); the proof here stands on its own. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1558 CLAIM-478 THEORY-196 — Proposed; the readings and claims this links -->

# CLAIM-tmpxi826: For a chain with symmetric rates ε to the power U on a connected graph of n states and E edges, the log commute time between two states lies within log max(E, n − 1) of log n plus log(1/ε) times their minimax barrier, an ultrametric; so the time geometry of the state space is hyperbolic in Gromov's four-point sense with δ bounded independently of ε while its distances grow as log(1/ε), and as time scales separate it becomes the tree of classes reachable within a budget

## The claim

Let a continuous-time Markov chain on a connected graph with n states and E
edges have symmetric rates q_ij = ε^(U_ij), 0 < ε < 1, so that its stationary
law is uniform. Small ε means strongly separated time scales: an edge with a
higher barrier U is slower by a power of ε. Let

- κ(i, j) be the commute time, the expected time to go from i to j and
  back, and D(i, j) = log κ(i, j);
- u(i, j) be the minimax barrier: over paths from i to j, the least
  possible highest U along the path. This is CLAIM-581's peak-capacity
  threshold, and it is an ultrametric.

Then for every pair and every ε,

  | D(i, j) − log n − log(1/ε)·u(i, j) | ≤ log max(E, n − 1).

## Proof

1. **Commute time is resistance.** For this chain κ(i, j) = n·R_eff(i, j),
   where R_eff is the effective resistance between i and j in the network
   with conductance q_ij on each edge.
2. **Upper bound.** A path attaining u has at most n − 1 edges, each with
   U ≤ u and so resistance ε^(−U) ≤ ε^(−u). Resistance in series and
   Rayleigh monotonicity give R_eff ≤ (n − 1)ε^(−u).
3. **Lower bound.** Let S be the set of states reachable from i by edges
   with U < u. Then j ∉ S, or u would be smaller. Every edge leaving S has
   U ≥ u, so the total conductance across the cut is at most E·ε^u, and by
   the Nash-Williams bound R_eff ≥ ε^(−u)/E.
4. Take logarithms and add log n.

**Hyperbolicity.** Write s = log(1/ε) and c = log max(E, n − 1). D − log n
is within c of s·u, and s·u is an ultrametric, which satisfies the
four-point condition with δ = 0: of the three sums d(x,y) + d(z,w),
d(x,z) + d(y,w), d(x,w) + d(y,z), the two largest are equal. Moving each
distance by at most c moves each sum by at most 2c, so the two largest
differ by at most 4c and the metric is δ-hyperbolic with δ ≤ 2c (adding the
constant log n changes no difference of sums). δ does not depend on ε,
while the distances grow as s. So hyperbolicity relative to scale,
δ/diameter, goes to zero as time scales separate, and D/s converges to the
ultrametric u. The tree is CLAIM-581's tree of classes reachable within a
budget.

**When levels show.** Two levels of that tree whose barriers differ by Δu
are separated in D by about s·Δu. They can be told apart in the geometry
when s·Δu exceeds the slack 2c, and not otherwise.

## Checks

Run under `python3 -I` on 2026-11-20 (scripts in the curation entry of
2026-11-20, 232905).

- **Identity and bounds.** 4×4 torus (n = 16, E = 32), barriers uniform on
  [0, 1]: κ/(n·R_eff) − 1 at most 6 × 10⁻¹²; log R_eff − s·u stayed in
  [−0.77, 0.64] for ε from 0.5 to 10⁻⁹, inside the proven [−3.47, 2.71].
- **Relative hyperbolicity.** On the same chain, δ stayed near 0.27 while
  δ/s fell: 0.31, 0.095, 0.058, 0.030, 0.020 at ε = 0.5, 10⁻¹, 10⁻², 10⁻⁴,
  10⁻⁶; max |D/s − u| fell from 3.5 to 0.24.
- **A designed hierarchy.** A binary tree of depth 4, rates g^(level − 1)
  between leaves, multiplied within a level by symmetric factors up to e^h.
  With h = 0 the metric is ultrametric for every g, by symmetry. With
  h = 0.5 and 1, δ fell as the gap grew (h = 1: 0.073, 0.047, 0.011, 0.001
  at g = 0.5, 0.1, 0.01, 0.001), while the defect from equal heights per
  level did not fall. The single-linkage tree of the time geometry had the
  designed topology in every run once the gap beat the spread within levels
  (all runs at g ≤ 0.1 for h = 0.5 and 1; at h = 3, 1 of 5 runs at g = 0.1,
  4 of 5 at 0.01, 5 of 5 at 0.001), and a rearranged topology, with as many
  classes added as lost, when it did not (every run at g = 0.5). The
  remaining defect is unequal heights within a level, largest among
  siblings: the tree is the designed one with nodes of a level at
  different heights, not a finer tree.
- **Flat chains.** A 16-cycle and the 4×4 torus with equal rates: δ = 0.32
  against diameter 1.45, and 0.22 against 0.35.

## What it does not say

- Not that it holds beyond symmetric rates. For general reversible chains
  the conductances are π_i·q_ij and the barriers are heights relative to
  wells; the same argument should go through, and was not checked.
- Not the converse: that a tree-like time geometry with well-separated
  levels requires separated rates. Only the spacing argument above bears on
  it (QUESTION-tmpv6fxp).
- Not that the result is new to mathematics. Freidlin–Wentzell theory and
  the metastability literature hold the small-noise asymptotics of
  transition times; the record holds neither.
- Not that coupling produces the separation. The barriers are given here.
  CLAIM-481 holds that coupling does not by itself separate time scales.
