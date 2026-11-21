---
status: Proposed
title: 'For a chain with symmetric rates ε to the power U on a connected graph of n states and E edges, the log commute time between two states lies within log max(E, n − 1) of log n plus log(1/ε) times their minimax barrier, an ultrametric; so after scaling by log(1/ε) the time geometry of the state space converges to that ultrametric, the tree of classes reachable within a budget, and a level of the tree shows in the geometry once the rate ratio across it exceeds max(E, n − 1) squared; that the geometry is hyperbolic with bounded δ is not the content, since the logarithm of any metric is nearly an ultrametric'
version: 3
history:
- version: 2
  date: '2026-11-20'
  note: >-
    Restated before merging, at the owner's turn of 2026-11-20: "maybe I'm
    being brash calling it 'scale separation' and a more appropriate -- or at
    least easier to demonstrate -- assertion would call it 'rate
    differences'". The bound holds at every ε, so the claim never needed a
    limit; the title now states the finite condition, a rate ratio across a
    level, in place of "as time scales separate". The proof is unchanged.
    Version 1's title: "For a chain with symmetric rates ε to the power U on a connected graph of n states and E edges, the log commute time between two states lies within log max(E, n − 1) of log n plus log(1/ε) times their minimax barrier, an ultrametric; so the time geometry of the state space is hyperbolic in Gromov's four-point sense with δ bounded independently of ε while its distances grow as log(1/ε), and as time scales separate it becomes the tree of classes reachable within a budget".
- version: 3
  date: '2026-11-21'
  note: >-
    Revised after the reading of Bovier and colleagues (NOTE-tmpjot4l).
    Its reader observed, and the assistant checked, that the logarithm of
    any metric is an ultrametric up to ln 2, so the bounded hyperbolicity
    version 2's title stated holds for every chain; the title now states
    the content, which ultrametric and how its levels are spaced. The
    sentence that the record holds neither Freidlin–Wentzell nor
    metastability theory was wrong and is corrected (LIT-2035, LIT-2037
    held). The reading joins grounds. Version 2's title: "For a chain with
    symmetric rates ε to the power U on a connected graph of n states and
    E edges, the log commute time between two states lies within log
    max(E, n − 1) of log n plus log(1/ε) times their minimax barrier, an
    ultrametric; so the time geometry of the state space is hyperbolic in
    Gromov's four-point sense with δ bounded independently of the rates,
    and a level of the tree of classes reachable within a budget shows in
    that geometry once the rate ratio across it exceeds max(E, n − 1)
    squared".
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
grounds:
- THEORY-tmph10k5
summary: >-
  The link the record lacked between dynamical hierarchy (levels marked by
  rate gaps, [THEORY-1306](../theory.d/THEORY-1306.md), [THEORY-1558](../theory.d/THEORY-1558.md), [CLAIM-478](CLAIM-478.md)) and geometric
  hyperbolicity ([THEORY-193](../theory.d/THEORY-193.md), [THEORY-196](../theory.d/THEORY-196.md)): rate differences across levels
  make the log commute-time geometry of a state space tree-like, and the tree is
  the one [CLAIM-581](CLAIM-581.md) builds from peak-capacity thresholds. Proved by
  electrical-network bounds and checked numerically. The owner asked
  (2026-11-20) whether the record could "formalize the relationship
  between hierarchy and hyperbolicity". Results of this kind belong to
  Freidlin–Wentzell metastability theory, which the record does not hold
  ([LEAD-tmpdv2tt](../leads.d/LEAD-tmpdv2tt.md)); the proof here stands on its own. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1366 THEORY-1370 THEORY-tmph10k5 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: THEORY-1558 CLAIM-478 THEORY-196 — Proposed; the readings and claims this links -->

# CLAIM-tmpxi826: For a chain with symmetric rates ε to the power U on a connected graph of n states and E edges, the log commute time between two states lies within log max(E, n − 1) of log n plus log(1/ε) times their minimax barrier, an ultrametric; so after scaling by log(1/ε) the time geometry of the state space converges to that ultrametric, the tree of classes reachable within a budget, and a level of the tree shows in the geometry once the rate ratio across it exceeds max(E, n − 1) squared; that the geometry is hyperbolic with bounded δ is not the content, since the logarithm of any metric is nearly an ultrametric

## The claim

Let a continuous-time Markov chain on a connected graph with n states and E
edges have symmetric rates q_ij = ε^(U_ij), 0 < ε < 1, so that its stationary
law is uniform. Small ε means strongly separated time scales: an edge with a
higher barrier U is slower by a power of ε. Let

- κ(i, j) be the commute time, the expected time to go from i to j and
  back, and D(i, j) = log κ(i, j);
- u(i, j) be the minimax barrier: over paths from i to j, the least
  possible highest U along the path. This is [CLAIM-581](CLAIM-581.md)'s peak-capacity
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
ultrametric u. The tree is [CLAIM-581](CLAIM-581.md)'s tree of classes reachable within a
budget.

**What bounded δ does not show.** The bounded δ is not evidence of
hierarchy. For any metric d, d(x, z) ≤ 2·max(d(x, y), d(y, z)), so log d
satisfies the ultrametric inequality up to ln 2, and effective resistance is
a metric: the log commute-time geometry of every chain, whatever its rates,
is nearly an ultrametric. The reader of Bovier and colleagues pointed this
out ([NOTE-tmpjot4l](../notes.d/NOTE-tmpjot4l.md)), and the assistant checked it: over 400 random 9-point
metrics the four-point δ of log d never exceeded 0.66 (curation entry of
2026-11-21). The flat chains below have small δ for that reason. What the
rates add is which ultrametric, the minimax barrier scaled by log(1/ε), and
spacing between its levels that grows past the slack. Those are the claim's
content.

**When levels show.** Two levels of that tree whose barriers differ by Δu
are separated in D by about s·Δu. They can be told apart in the geometry
when s·Δu exceeds the slack 2c, that is, when the rate ratio across the
level, ε^(−Δu), exceeds e^(2c) = max(E, n − 1)². That is a finite rate
difference, not a limit: the claim needs no asymptotic separation of
scales. The factor is sufficient and loose; in the designed hierarchy below,
levels showed at ratios near 10 on 16 states, where the factor is 1,024
([QUESTION-tmp4ma9f](../questions.d/QUESTION-tmp4ma9f.md)).

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
  it ([QUESTION-tmpv6fxp](../questions.d/QUESTION-tmpv6fxp.md)).
- Not that the result is new to mathematics. Freidlin–Wentzell theory and
  the metastability literature hold the small-noise asymptotics of
  transition times. The record holds both, which version 1 wrongly denied:
  Freidlin and Wentzell ([LIT-2035](../literature.d/LIT-2035.md), [THEORY-1366](../theory.d/THEORY-1366.md)), Berglund on Kramers' law
  ([LIT-2037](../literature.d/LIT-2037.md), [THEORY-1370](../theory.d/THEORY-1370.md)), and now Bovier and colleagues ([THEORY-tmph10k5](../theory.d/THEORY-tmph10k5.md)),
  whose minus log capacity is an ultrametric up to ln 3 between metastable
  points, a slack independent of n and E, for general reversible chains
  under genericity.
- Not that coupling produces the separation. The barriers are given here.
  [CLAIM-481](CLAIM-481.md) holds that coupling does not by itself separate time scales.
