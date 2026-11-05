---
status: Proposed
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
- distributed-agency
- formal-apparatus
grounds:
- THEORY-tmps6lqg
- THEORY-tmpq2qdv
- THEORY-tmpucnpz
- THEORY-tmpmqxmo
complements:
- CLAIM-357
- CLAIM-347
- CLAIM-tmpbi4ca
bears_on:
- QUESTION-tmp9lrtl
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
<!-- inactive-ok-file: THEORY-tmps6lqg THEORY-tmpq2qdv THEORY-tmpucnpz THEORY-tmpmqxmo CLAIM-tmpbi4ca CLAIM-tmp675a9 CLAIM-354 — Proposed; the readings' accounts and A's proposals of 2026-11-04, cited as filed, nothing here rests on their being settled -->
<!-- inactive-ok-file: CASE-tmpe48yq CASE-tmpez9ok CASE-tmpnqvjs CLAIM-tmpal9mc — Proposed or new; entries of 2026-11-05 from the pasted synthesis on constraint architectures, cited as open -->

# CLAIM-tmp9jvpb: That a target configuration is feasible, that it is reachable from the start under the admissible transformations, and that the process reliably reaches it are three properties, each implied by the next and none implying it

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

- **Feasible, not reachable.** In [CLAIM-tmpbi4ca](CLAIM-tmpbi4ca.md)'s example at a budget of
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
  ([NOTE-tmpt066u](../notes.d/NOTE-tmpt066u.md); [THEORY-tmps6lqg](../theory.d/THEORY-tmps6lqg.md)). For a near-flat vertex with positive
  curvature "the two nappes have split into two disconnected components";
  each is feasible, and folding without self-intersection does not join
  them. Allowing faces to pass through each other reportedly does. Jules
  et al.'s defect states ([NOTE-tmpwz8jy](../notes.d/NOTE-tmpwz8jy.md)) are a second instance: unreachable
  under uniaxial loading, reached only by twisting by hand.
- **Reachable, not reliably reached: Stern, Pinson and Murugan**
  ([NOTE-tmp9dvve](../notes.d/NOTE-tmp9dvve.md); [THEORY-tmpq2qdv](../theory.d/THEORY-tmpq2qdv.md)). A pattern designed with one folding motion
  has "an exponential number of ‘distractor’ folding branches accessible
  from a bifurcation at the flat state", and the designed branch, which
  can even be made the ground state, is reached by randomly placed
  fixed-torque actuators with a 50% chance only when "actuators are
  needed on 18 out of a total of 60 creases". Simulation, one pattern,
  zero temperature.
- **The same, at a singular point: Chen and Santangelo** ([NOTE-tmpwpp63](../notes.d/NOTE-tmpwpp63.md);
  [THEORY-tmpucnpz](../theory.d/THEORY-tmpucnpz.md)). Generically 2^Vi branches meet at the flat state, all
  satisfying every constraint, and "a generic structure is likely to
  become trapped in a “misfolded” state".
- **The same, under a declared class of actuation: Hull and Tachi**
  ([NOTE-tmpryygx](../notes.d/NOTE-tmpryygx.md); [THEORY-tmpmqxmo](../theory.d/THEORY-tmpmqxmo.md)). "the Miura-ori and Chicken Wire patterns are not
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
- **[CLAIM-tmpbi4ca](CLAIM-tmpbi4ca.md)** gives the first separation a resource threshold.
- **[CLAIM-354](CLAIM-354.md)** separates instantaneous freedom from viable reachability;
  this adds that reachability is not reliable emergence.

## What it does not say

- **That organizations exhibit the separations.** The witnesses are a
  construction and mechanical systems. A's organizational reading is an
  analogy.
- **That reliable emergence needs more intervention.** Where intervention
  is placed can matter more than how much ([CLAIM-tmp675a9](CLAIM-tmp675a9.md)).
- **That the separations are absolute.** Each is relative to a declared
  class of transformations and a declared process.

## Note of 2026-11-05: A's resource models and further distinctions

At a footprint budget of 1.5, [CASE-tmpe48yq](../cases.d/CASE-tmpe48yq.md)'s two folded states are both feasible and neither can reach the other. [CASE-tmpez9ok](../cases.d/CASE-tmpez9ok.md) makes the declared class of moves itself depend on an energy budget. [CASE-tmpnqvjs](../cases.d/CASE-tmpnqvjs.md) separates simultaneous, sequential and separate capability for one squad. [CLAIM-tmpal9mc](CLAIM-tmpal9mc.md) sorts the ways reachability fails into four obstructions with different remedies. No status changes.
