---
status: Proposed
promote_when: >-
  Three results together. Branching statistics recomputed from the
  skeletons without the rule that merges two close bifurcations into a
  trifurcation, with the merging cutoff varied. The actual surface
  minimiser run on random terminal sets, not a sigmoid calibrated on one
  tetrahedron, giving a predicted distribution of the intermediate-link
  length to compare with the data. And a test of the sprouting breakpoint
  against a smooth no-breakpoint model, such as Zamir's cylinders, by
  likelihood or cross-validation, with the breakpoint's selection bias
  accounted for. Promoted if the trifurcation excess and a sharp sprouting
  threshold survive all three; refuted if either disappears. More
  datasets analysed by the present pipeline cannot settle it, since the
  pipeline's own choices partly produce the features.
title: "The local branching geometry of physical tree networks, neurons, blood vessels, trees, corals and plants, is set by minimising the surface area of tubes that must keep a minimum circumference, not by minimising length: this predicts trifurcations once links are thick relative to their separation (χ = w/r above about 0.83) and orthogonal sprouts once one branch is much thinner than the other two (ρ = w′/w below about 0.6), both departures from Steiner trees that the data show qualitatively"
version: 1
tags:
- network-science
- natural-sciences
- neuroscience
date: '2026-10-16'
source:
- LIT-069
summary: >-
  Meng, Piazza, Both, Barzel & Barabási (2026), [LIT-069](../literature.d/LIT-069.md), read in full with
  the SI in [NOTE-075](../notes.d/NOTE-075.md). Only two symmetric motifs are solved, each by a
  local, penalised optimiser started from the Steiner layout; the "exact"
  mapping to string worldsheets holds for a problem the paper does not
  solve. The random-terminal prediction is a sigmoid fitted to one
  tetrahedron, trifurcations are partly made by a merging rule, the one
  robustness check moves the key statistic 4.3-fold, and the sprouting
  breakpoints are chosen per dataset with no null. Real motifs are about
  25% longer than Steiner, which the model leaves unexplained.
---
<!-- inactive-ok-file: LIT-069 — Proposed by its close reading; the only source, and the account is Proposed for the reasons that reading gives -->

# THEORY-tmpwyqo3: The local branching geometry of physical tree networks, neurons, blood vessels, trees, corals and plants, is set by minimising the surface area of tubes that must keep a minimum circumference, not by minimising length: this predicts trifurcations once links are thick relative to their separation (χ = w/r above about 0.83) and orthogonal sprouts once one branch is much thinner than the other two (ρ = w′/w below about 0.6), both departures from Steiner trees that the data show qualitatively

## Source

Xiangyi Meng, Benjamin Piazza, Csaba Both, Baruch Barzel and Albert-László
Barabási (2026), "Surface optimization governs the local design of
physical networks", *Nature* 649, 315–322, [LIT-069](../literature.d/LIT-069.md), read in full with the
Supplementary Information in [NOTE-075](../notes.d/NOTE-075.md).

## What was actually shown

**The departure from Steiner (Fig. 1).** Length-minimal (Steiner) trees
have only degree-3 nodes, planar bifurcations and 120° angles. In six
classes of 3D networks, k = 4 nodes are 17.0% (human neurons), 6.5%
(fly), 8.3% (one arterial tree), 17.7% (tropical trees), 8.7% (corals)
and 4.6% (Arabidopsis); P(θ) has no peak at 2π/3; bifurcations are close
to, but not exactly, planar.

**The model (Eqs. 1–2).** Each link is a smooth sleeve; total surface area
is minimised subject to every non-contractible loop around a link having
length at least w. Length minimisation has no scale; this has two, χ = w/r
and ρ = w′/w.

**Trifurcations (Fig. 3g; SI Fig. 13).** For a regular tetrahedron of
terminals the intermediate link length λ = l/w drops sharply to 0 at
χ ≈ 0.83: two close junctions cost more area than one merged junction.
Empirical P(λ → 0) is positive in all six datasets.

**Sprouts (Fig. 4g; SI Fig. 19).** With two equal branches and a thinner
third, the thin branch leaves perpendicular to a straight thick path
(Ω₁→₂ = 0) for ρ below about 0.6, and the angle rises linearly above. A
plain-cylinder model (Zamir) instead approaches 90° only as ρ → 0.
Breakpoints fitted per dataset lie at 0.52–0.92, and sprouts are 11–53% of
equal-branch bifurcations. In human neurons 3,911 of 4,003 sprouts (97.7%)
end on a synapse (the caption says 92%).

**What could have come out otherwise.** The data could have looked like
Steiner trees: degree 3, 120°, planar. They do not, in all six classes.
The sharp thresholds could have been absent in the simulations; for the
two symmetric motifs they are present.

## What this does not say

- **That real networks are surface-optimal.** Agreement is qualitative.
  Real double-bifurcation motifs are 1.20–1.35 times the Steiner length,
  which the model, predicting straight cylinders away from junctions, does
  not explain. "A stereotypical principle that is not overwritten by
  functional or global need" (p. 320) is an assertion.
- **That the theory was solved exactly.** Strebel's exact minimal-area
  solution ignores immersibility in three dimensions and has conical
  singularities. The numbers come from a locally minimising, penalised
  quad-mesh optimisation, and SI §5 concedes "a globally distinct surface
  configuration may still achieve a lower total area".
- **That trifurcations are measured independently of the analysis.** Two
  bifurcations with intermediate link at most w/2π are merged into one
  trifurcation (SI Eq. 43), and the one skeletonisation check changes
  P(λ → 0) from 0.276 to 1.200. The "roughly 15%" k = 4 figure is pooled
  and 96% human-neuron nodes.
- **That the random-terminal curve came from the minimiser.** Running it on
  10⁶ quadruplets was "un-scalable"; λ was mapped through a sigmoid
  calibrated on the tetrahedron, and the empirical Steiner reference is the
  distribution of external legs, whose relation to internal ones has
  Spearman ρ of only 0.11–0.42.
- **That the sprouting transition is sharp in the data.** Breakpoints are
  chosen to maximise a slope jump, with no null; the tree dataset's jump is
  0.002.
- **That surface is the right cost.** For neurons, corals and trees the
  authors say volume must also count; the volume check is one motif.
- **Anything about looped networks.** Loops are excluded by construction.

## Connections

- **Graph curvature** ([THEORY-tmp6xq6t](THEORY-tmp6xq6t.md), from [LIT-004](../literature.d/LIT-004.md); [THEORY-tmpdk0fo](THEORY-tmpdk0fo.md), from
  [LIT-020](../literature.d/LIT-020.md)). Those curvatures live on an abstract graph's edges and are
  blind to the thickness ratios χ and ρ that drive this account. [NOTE-075](../notes.d/NOTE-075.md)
  draws the contrast.
- **What it leaves open.** [NOTE-075](../notes.d/NOTE-075.md) suggests the natural question this
  seeds: at what scale material-cost optimisation stops predicting
  morphology, local junction geometry against the 25% excess in global
  layout.
