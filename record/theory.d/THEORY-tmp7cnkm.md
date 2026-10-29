---
status: Active
title: 'Anchors entered as node features in fused Gromov–Wasserstein break a structural tie only when they move under it: with α strictly between 0 and 1, the zero-cost matchings of a structure with itself are exactly its automorphisms that fix every anchor, so a 6-cycle has 12 with no anchor, 2 with one anchor, 1 with two adjacent anchors and still 2 with two antipodal ones, and whether a set of anchors identifies the correspondence can be decided from the structure before any fit'
version: 1
tags:
- mathematics
- network-science
date: '2026-10-29'
source:
- LIT-tmpjs7kp
summary: >-
  Derived from Vayer et al. (2019), LIT-tmpjs7kp, Theorem 3.2's zero case,
  read in NOTE-tmp6e5aw; the paper does not state it. Checked by
  enumerating all 720 matchings of a 6-cycle with four anchor patterns.
  Active: an elementary consequence of a proved theorem, checked. It is
  about exact ties; with noisy data, symmetries become near-ties, and the
  theorem says nothing about how near.
---
<!-- inactive-ok-file: CASE-055 CASE-tmph0fxi — stipulated; the designs whose anchors this bears on -->

# THEORY-tmp7cnkm: Anchors entered as node features in fused Gromov–Wasserstein break a structural tie only when they move under it: with α strictly between 0 and 1, the zero-cost matchings of a structure with itself are exactly its automorphisms that fix every anchor, so a 6-cycle has 12 with no anchor, 2 with one anchor, 1 with two adjacent anchors and still 2 with two antipodal ones, and whether a set of anchors identifies the correspondence can be decided from the structure before any fit

## Source

Vayer, Chapel, Flamary, Tavenard and Courty (2019), LIT-tmpjs7kp, Theorem
3.2, p. 4, with Theorem 6.4, pp. 12–13 of arXiv 1805.09114v3; read in
NOTE-tmp6e5aw. The consequence and the count are this record's.

## What was actually shown

**From the paper.** For α ∈ ]0, 1[ and distance-matrix structures, FGW = 0
iff some bijection σ preserves the weights, the features (a_i = b_σ(i))
and the structure (C₁(i, k) = C₂(σ(i), σ(k))).

**The step.** Give each anchor node a feature that no other node has, and
every other node one common feature. Compare a structure with itself. A
zero-cost bijection must preserve the structure, so it is an
automorphism, and it must send each anchor to the node with its feature,
so it fixes every anchor. Conversely, every such automorphism costs zero.
The zero-cost matchings are therefore the stabilizer of the anchors in the
automorphism group. Every optimal plan between two structures comes with
an orbit under that subgroup.

**Checked.** For the 6-cycle with shortest-path distances, I enumerated
all 720 permutations and counted those of zero cost. With no anchor:
12 at α = 0.5 and α = 1 (the dihedral group), 720 at α = 0. With one
anchor: 2 at α = 0.5, 12 at α = 1, 120 at α = 0. With two adjacent anchors:
1, 12 and 24. With two antipodal anchors: 2, 12 and 24. The reflection
through the axis joining two antipodal anchors fixes both, so they leave a
tie that two adjacent anchors do not.

**What could have failed.** Anchors might have broken ties through the
structure term's coupling of all pairs, even where no symmetry moved them.
They do not. Their effect is exactly to remove the automorphisms that move
them.

## What this does not say

- **Anything about noisy anchors or noisy structure.** Exact symmetries are
  rare in measured data. Near-symmetries give near-ties, and FGW's theorem
  gives no margin.
- **That the solver finds the identified matching.** Conditional gradient
  reaches stationary points (p. 5).
- **That anchors must be features.** They can also enter as fixed
  couplings or constraints. The stabilizer argument applies to any
  mechanism that forces each anchor to its counterpart.
- **That one anchor in general position always suffices.** It suffices on a
  cycle up to the reflection through it. Graphs with larger automorphism
  groups can need more.
