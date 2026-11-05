---
number: 567
status: Proposed
formerly:
- CLAIM-tmp9jvpb
title: 'That a target configuration is feasible, that it is reachable from the start under the admissible transformations, and that the process reliably reaches it are three properties, each implied by the next and none implying it'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the implications or the witnesses: a reading of reliable
  emergence under which it does not imply that some admissible run reaches
  the target, or a showing that the two-component sublevel set is not
  feasible-but-unreachable, or the symmetric fork not reachable-but-
  unreliable, under the definitions stated. Not defeated by systems in
  which the three coincide, nor by a richer class of admissible
  transformations that reconnects what a poorer one separates; the claim
  is that the three can come apart, relative to a declared class.
tags:
- mathematics
- complex-systems
- natural-sciences
date: '2026-11-05'
line:
- realizability
- readiness
- formal-apparatus
grounds:
- THEORY-1423
- THEORY-1418
- THEORY-1427
- THEORY-1409
complements:
- CLAIM-357
- CLAIM-347
- CLAIM-571
bears_on:
- QUESTION-380
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Parts 3 and 5: A's
  "Feasible target ⇏ reachable target" and "Global solution exists" against "Global solution reliably emerges", joined. Feasible means the target meets the constraints;
  reachable, that an admissible path leads to it; reliably reached, that
  the process ends there with probability at least 1 − ε. The
  implications are immediate and two constructions show neither converse.
  Berry et al., Stern, Pinson and Murugan, Chen and Santangelo, and Hull
  and Tachi give physical instances. It inserts reachability between the
  structural infeasibility and realized violation that [CLAIM-357](CLAIM-357.md)
  separates. The construction is the filer's, from A's two separations;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1423 THEORY-1418 THEORY-1427 THEORY-1409 CLAIM-571 CLAIM-562 CLAIM-354 — Proposed; the readings' accounts and A's proposals of 2026-11-04, cited as filed, nothing here rests on their being settled -->
<!-- inactive-ok-file: CASE-206 CASE-207 CASE-209 CLAIM-568 — Proposed or new; entries of 2026-11-05 from the pasted synthesis on constraint architectures, cited as open -->
<!-- inactive-ok-file: NOTE-1572 NOTE-1555 NOTE-1584 NOTE-1613 — Proposed or new; the resource-bounded realizability readings of 2026-11-05, cited as open -->

# CLAIM-567: That a target configuration is feasible, that it is reachable from the start under the admissible transformations, and that the process reliably reaches it are three properties, each implied by the next and none implying it

## The claim

A separates them twice. Part 3: "Feasible target ⇏ reachable target",
with existence, continuous reachability, singular passage and branch
selection to be kept apart. Part 5: existence ≠ reliable emergence, as
the design problem min_a C(a) s.t. P_a(s*|s0) ≥ 1−ε, and the proposed
experiment separating "Global solution exists" from "Global solution
reliably emerges". Joined, with a start s0, a target s* and a declared
class of admissible transformations:

1. **Feasible**: s* meets the constraints.
2. **Reachable**: some admissible path leads from s0 to s*.
3. **Reliably reached**: the process as it runs, under its actuation or
   policy a, ends at s* with probability P_a(s* | s0) ≥ 1 − ε, for a
   declared ε < 1.

**Each implies the one before.** A positive probability of ending at s*
means some admissible run ends there, and a run is an admissible path, so
3 implies 2. A path ending at s* lies in the configuration space, so 2
implies 1.

**Neither converse holds.**

- **Feasible, not reachable.** In [CLAIM-571](CLAIM-571.md)'s example at a budget of
  1.0, both 0 and 1 meet the constraint r(q) ≤ 1.0, and they lie in
  different components of the feasible set, so no admissible path joins
  them.
- **Reachable, not reliably reached.** Let a flat state branch into two
  paths, one ending at s* and one at a distractor, and let the actuation
  be unbiased between them. Then s* is reachable and P(s* | s0) = 1/2,
  below 1 − ε for any ε < 1/2.

Both separations are relative to the declared class. A: "impossibility is
relative to the declared model of admissible transformations".

## Physical instances

- **Feasible, not reachable: Berry, Lee-Trimble and Santangelo**
  ([NOTE-1605](../notes.d/NOTE-1605.md); [THEORY-1423](../theory.d/THEORY-1423.md)). For a near-flat vertex with positive
  curvature "the two nappes have split into two disconnected components";
  each is feasible, and folding without self-intersection does not join
  them. Allowing faces to pass through each other reportedly does. Jules
  et al.'s defect states ([NOTE-1617](../notes.d/NOTE-1617.md)) are a second instance: unreachable
  under uniaxial loading, reached only by twisting by hand.
- **Reachable, not reliably reached: Stern, Pinson and Murugan**
  ([NOTE-1571](../notes.d/NOTE-1571.md); [THEORY-1418](../theory.d/THEORY-1418.md)). A pattern designed with one folding motion
  has "an exponential number of ‘distractor’ folding branches accessible
  from a bifurcation at the flat state", and the designed branch, which
  can even be made the ground state, is reached by randomly placed
  fixed-torque actuators with a 50% chance only when "actuators are
  needed on 18 out of a total of 60 creases". Simulation, one pattern,
  zero temperature.
- **The same, at a singular point: Chen and Santangelo** ([NOTE-1614](../notes.d/NOTE-1614.md);
  [THEORY-1427](../theory.d/THEORY-1427.md)). Generically 2^Vi branches meet at the flat state, all
  satisfying every constraint, and "a generic structure is likely to
  become trapped in a “misfolded” state".
- **The same, under a declared class of actuation: Hull and Tachi**
  ([NOTE-1603](../notes.d/NOTE-1603.md); [THEORY-1409](../theory.d/THEORY-1409.md)). "the Miura-ori and Chicken Wire patterns are not
  self-foldable under our definition": the folding exists, and no
  crease-local driving force selects it uniquely.

## Relations

- **[CLAIM-357](CLAIM-357.md)** separates structural infeasibility (no admissible update
  meets the demands) from realized violation (one does, and the actual
  update does not) for a single update. This claim puts reachability
  between them, for processes that move through intermediate states: a
  target can be feasible and unrealized because no path leads to it,
  which is neither of [CLAIM-357](CLAIM-357.md)'s cases. The reading of Hull and Tachi
  calls it a third case.
- **[CLAIM-347](CLAIM-347.md)**'s compatibility complex registers property 1 for sets of
  demands. It does not register 2 or 3: Chen and Santangelo's branches
  are jointly feasible realizations among which the process must select,
  and Berry et al.'s nappes are jointly feasible and disconnected.
- **[TERM-060](../terms.d/TERM-060.md)**. A feasible target that is not reached is not frustrated in
  the term's structural sense. The term's governance-induced case is
  nearer, but there the target is attainable by an admissible update and
  the governance does not select it, while here no path may exist.
- **[CLAIM-571](CLAIM-571.md)** gives the first separation a resource threshold.
- **[CLAIM-354](CLAIM-354.md)** separates instantaneous freedom from viable reachability;
  this adds that reachability is not reliable emergence.

## What it does not say

- **That organizations exhibit the separations.** The witnesses are a
  construction and mechanical systems. A's organizational reading is an
  analogy.
- **That reliable emergence needs more intervention.** Where intervention
  is placed can matter more than how much ([CLAIM-562](CLAIM-562.md)).
- **That the separations are absolute.** Each is relative to a declared
  class of transformations and a declared process.

## Note of 2026-11-05: A's resource models and further distinctions

At a footprint budget of 1.5, [CASE-206](../cases.d/CASE-206.md)'s two folded states are both feasible and neither can reach the other. [CASE-207](../cases.d/CASE-207.md) makes the declared class of moves itself depend on an energy budget. [CASE-209](../cases.d/CASE-209.md) separates simultaneous, sequential and separate capability for one squad. [CLAIM-568](CLAIM-568.md) sorts the ways reachability fails into four obstructions with different remedies. No status changes.

## Note of 2026-11-05: the resource-bounded realizability readings

Two groups of readings filed beside the pasted synthesis on resource-bounded realizability bear on the claim. The finite-domain CSP dichotomy of Bulatov ([NOTE-1572](../notes.d/NOTE-1572.md)) and Zhuk ([NOTE-1555](../notes.d/NOTE-1555.md)) concerns only the first property: it classifies the complexity of deciding whether a solution exists, over fixed finite languages, and says nothing about reaching one solution from another; Zhuk's "linked" is a false friend. Polymorphisms are the precedent for an algebra predicting the complexity of feasibility; whether one predicts reachability is open relative to those papers, and for Boolean languages is the question Gopalan et al. take up ([NOTE-1584](../notes.d/NOTE-1584.md)).

The complexity readings give the second separation hardness results. In Eppstein's flaps and flips ([NOTE-1611](../notes.d/NOTE-1611.md), Theorem 4) both endpoints are valid flat states, and deciding whether one reaches the other is PSPACE-complete even at bounded treewidth. Ito et al. ([NOTE-1595](../notes.d/NOTE-1595.md), Theorems 1 and 2) show the reconfiguration versions of many NP-complete problems PSPACE-complete, while matroid bases and matchings reconfigure in polynomial time. For Boolean languages that are not tight, Gopalan et al. find st-connectivity PSPACE-complete with components of exponential diameter possible; Schwerdtfeger ([NOTE-1613](../notes.d/NOTE-1613.md)) corrects the boundary slightly toward the hard side. None of them bears on the third property. No status changes.
