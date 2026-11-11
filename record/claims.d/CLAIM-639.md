---
number: 639
status: Proposed
formerly:
- CLAIM-tmpopi1b
title: 'Knowing each configuration''s requirement to within ε fixes every transition threshold to within ε but not which of a system''s own reachable classes an observer''s partitions can agree with: where two merges of the merge tree lie within 2ε of each other, an error within ε can reorder them, replacing a level that agrees under some order of probe costs with one that agrees under none'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the witness: a recomputation of the five-state path with the
  stated requirements and probes in which the true middle level of the
  merge tree is not the common refinement of a set of the probes, the
  estimated middle level is one, or the estimate differs from the true
  requirement by more than 0.1 somewhere; or a proof that an estimate
  within ε of the requirement everywhere leaves the levels of the merge
  tree unchanged. Not defeated by systems whose distinct merges all lie
  more than 2ε apart, where the order is kept; the claim says the
  agreement can change, not that it always does. Also defeated as a
  contribution if CLAIM-580 or CLAIM-592 already states that agreement of
  the two partitions is, or is not, stable under error in the requirement.
tags:
- mathematics
- individuation
- operations-research
date: '2026-11-11'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-580
- CLAIM-592
- CLAIM-581
summary: >-
  [CLAIM-580](CLAIM-580.md) shows that a planner who knows each configuration's
  requirement to within ε knows every transition threshold to within ε.
  [CLAIM-592](CLAIM-592.md) shows that whether a system's own reachable classes are ever
  what an observer can tell apart depends on which levels its merge tree
  ([CLAIM-581](CLAIM-581.md)) has and on the order of probe costs. The two do not combine
  into a stability for the agreement. The thresholds move by at most ε,
  but two merges whose heights are within 2ε can swap order, and the merge
  tree's levels change with them. A five-state witness, checked with
  python3 -I: with errors of 0.1, the true merge tree has a middle level
  that the probes refine to, so the partitions agree on it under one cost
  order, while the estimated tree's middle level is refined to by no set
  of probes, so under the estimate no order brings any nontrivial level
  into view. So [CLAIM-592](CLAIM-592.md)'s design lever, choosing what is cheap to observe
  so as to bring a chosen level of the system's structure into view, needs
  the requirement known to within half the gap between the merges that
  bound that level. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: ADR-075 ADR-084 — Proposed; the test this claim is filed under -->

# CLAIM-639: Knowing each configuration's requirement to within ε fixes every transition threshold to within ε but not which of a system's own reachable classes an observer's partitions can agree with: where two merges of the merge tree lie within 2ε of each other, an error within ε can reorder them, replacing a level that agrees under some order of probe costs with one that agrees under none

## The claim

Fix a finite system whose configurations carry a holding requirement r,
with reversible moves, so that the threshold d(x, y) between two
configurations is the least, over paths, of the largest r along the path
([CLAIM-571](CLAIM-571.md)'s threshold, with identities free, as in [CLAIM-581](CLAIM-581.md)). As the
acting budget a rises, the classes of configurations within a of one
another form the merge tree of [CLAIM-581](CLAIM-581.md). An observer buys probes, each a
partition of the configurations, in order of cost, and its partitions form
a chain of common refinements ([CLAIM-592](CLAIM-592.md)).

1. **The thresholds are stable** ([CLAIM-580](CLAIM-580.md)). If |r̂ − r| ≤ ε everywhere,
   every threshold moves by at most ε. So does each merge height, since a
   merge height is a threshold.
2. **The levels are not.** Two distinct merges at heights h₁ < h₂ with
   h₂ − h₁ < 2ε can be reordered by an error within ε that raises the
   first bottleneck and lowers the second. The partition between them is
   then a different partition.
3. **So the agreement is not.** By [CLAIM-592](CLAIM-592.md), a level of the merge tree
   agrees with the observer's partition under some cost order exactly when
   it is the common refinement of some set of the probes. Changing the
   levels changes which partitions are candidates, while the probes stay
   the same.

## The witness

Configurations x, m₁, y, m₂, z in a path, moves between neighbours both
ways. r(x) = r(y) = r(z) = 0, r(m₁) = 1.0, r(m₂) = 1.1. Probe p separates
x, m₁ and y from the rest; probe q separates z from the rest.

| | requirement at m₁, m₂ | middle level of the merge tree | agrees under some cost order |
|---|---|---|---|
| true | 1.0, 1.1 | {x, m₁, y} {m₂} {z}, on [1.0, 1.1) | yes: it is the refinement of p and q |
| estimate | 1.1, 1.0 | {x} {m₁} {y, m₂, z}, on [1.0, 1.1) | no: no set of probes refines to it |

The estimate is within 0.1 of r everywhere, and every threshold is within
0.1 of the true one, as [CLAIM-580](CLAIM-580.md) says. The two merges are 0.1 apart, less
than 2ε = 0.2. Under the true requirement the observer buying p then q
agrees with the system on its middle level; under the estimate no order of
the two probes gives agreement on any level other than the trivial ones.
Checked with python3 -I by enumeration of thresholds, merge levels and
refinements of probe subsets.

## What it adds

- **A limit to [CLAIM-580](CLAIM-580.md)'s guarantee.** [CLAIM-580](CLAIM-580.md) says the threshold does
  not amplify error. The structure built from many thresholds, the levels
  of the merge tree, is not a threshold, and an error that leaves every
  threshold nearly right can change it.
- **A condition on [CLAIM-592](CLAIM-592.md)'s design lever.** [CLAIM-592](CLAIM-592.md) says an
  instrument-maker who can change what is cheap to observe can bring a
  chosen level into view if some set of probes refines to it. Whether that
  level exists is itself known only to within the requirement's error: it
  is secure when the two merges that bound it are more than 2ε apart,
  since then every pair the level joins has an estimated threshold below
  every pair it separates.

## Admission

Filed as a derived result ([ADR-075](../decisions.d/ADR-075.md), step 5, as [ADR-084](../decisions.d/ADR-084.md) applies it to a
claim whose premises are claims).

- **The derivation.** From [CLAIM-580](CLAIM-580.md), merge heights move by at most ε.
  From [CLAIM-581](CLAIM-581.md), the merge tree's levels are the partitions at its merge
  heights, so their order fixes the levels. From [CLAIM-592](CLAIM-592.md), the candidate
  levels for agreement are the refinements of probe sets, fixed by the
  probes alone. An ε-error that reorders two merges therefore changes the
  levels while leaving the candidates fixed, and the witness shows one in
  which the true middle level is a candidate and the estimated one is not.
- **Why it is not trivial.** Neither premise says it, and the first reads
  as though it might carry over: a reader of [CLAIM-580](CLAIM-580.md) told that every
  threshold is known to within ε could take the merge tree, and with it
  [CLAIM-592](CLAIM-592.md)'s agreement, to be known too. The claim says which part
  carries over (the heights) and which does not (their order, and so the
  levels).
- **A realistic case.** On [CASE-206](../cases.d/CASE-206.md)'s vertex the agreeing window that
  [CLAIM-572](CLAIM-572.md)'s note of 2026-11-07 gives, 1.125 ≤ a < 1.866, is bounded by
  two merges 0.741 apart, so an error in the footprint below about 0.37
  leaves that level in the merge tree. That case is consistent with the claim and
  does not meet its `defeated_if`: the claim says the agreement can
  change, and there it does not at those error sizes.

## What it does not say

- That agreement is fragile everywhere. A level whose two bounding
  merges lie more than 2ε apart survives an error within ε, by the same
  bound.
- Anything about error in the probe costs, which [CLAIM-592](CLAIM-592.md) already
  covers: reordering the probes is what its cost order is.
- Anything about error in which moves are admissible, which [CLAIM-580](CLAIM-580.md)
  also sets aside.
- Anything about organizations; the witness is a construction.
