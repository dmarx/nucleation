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
<!-- inactive-ok-file: CLAIM-566 — Proposed; cited from the note on A's synthesis on DNA origami -->
<!-- inactive-ok-file: NOTE-1644 — Skimmed; cited from the DNA origami readings of 2026-11-05 -->
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

## Note of 2026-11-05: the DNA origami readings

Read on the owner's request to connect the record's realizability inquiry to DNA origami; the works were chosen by the assistant.

**Rothemund, "Folding DNA to create nanoscale shapes and patterns".** Rothemund (2006), [LIT-2120](../literature.d/LIT-2120.md), read in [NOTE-1631](../notes.d/NOTE-1631.md), supports the distinction with a caveat.
Every design is compatible by construction, so every target is feasible, yet the AFM-judged
fraction of well-formed structures runs from about 1% (an equiangular triangle of rectangles) to
90% (a bridged rectangle). The yields mix folding with deposition and tip damage, so they bound
reliable reachability loosely and do not separate an unreached target from a damaged one. No status
changes.

**Sobczak, "Investigations of the DNA origami folding process".** Sobczak's dissertation (2018), [LIT-2138](../literature.d/LIT-2138.md), read in part in [NOTE-1644](../notes.d/NOTE-1644.md) and standing in for
Sobczak et al. (2012), supports the claim empirically. The folded brick is vastly favoured, yet at
56 °C a sample showed "absolutely no folded origamis even after 48 hours", while 6 °C lower most
fold within 2 h; reliable reaching holds only within a window of a few degrees. It leaves open
whether the window's edges are sharp thresholds or timescale artefacts.

**Wagenbauer, Wachauf and Dietz, "Quantifying quality in DNA self-assembly".** Wagenbauer, Wachauf and Dietz (2014), [LIT-2128](../literature.d/LIT-2128.md), read in [NOTE-1637](../notes.d/NOTE-1637.md), support the claim from
the observing side: samples that "might be judged as high-quality assembly products" under TEM and
gel mobility still lack one to six staple equivalents per object, and isothermal folding reaches
the shape but not the completeness of a 16 h ramp. What counts as reaching the target depends on
the probe; the paper leaves open how the shortfall is spread across particles.

**Marras, Zhou, Su and Castro, "Programmable motion of DNA origami mechanisms".** Marras et al. (2015), [LIT-2118](../literature.d/LIT-2118.md), read in [NOTE-1635](../notes.d/NOTE-1635.md), give the three properties separately for one configuration, the compacted bundle of a DNA origami Bennett linkage:
- Feasible: locking staples added at folding hold 93% of linkages there.
- Reachable: 9.9% of free linkages visit it by thermal motion.
- Reliably reached: only with added closing strands, which give 93.1%.

This supports the claim with a concrete triple. It leaves open whether the grid fractions are the solution fractions: the authors call them upper bounds, since surface deposition may push near-extreme mechanisms into the extremes. Misfolded particles were excluded.

**Majikes et al., "Revealing thermodynamics of DNA origami folding via affine transformations".** Majikes et al. (2020), [LIT-2117](../literature.d/LIT-2117.md), read in [NOTE-1632](../notes.d/NOTE-1632.md), measure only the equilibrium stability of one staple fold, and they frame yield as a matter of "limiting thermodynamic equilibria". That weakly qualifies the claim's separation: the paper treats holding as what limits yield, and says nothing about reachability or reliability, since it records no anneal and no kinetics. It leaves open whether a stable fold is also reliably reached.

**Dunn et al., "Guiding the folding pathway of DNA origami", and Schneider, Möritz and Dietz, "The sequence of events during folding of a DNA origami".** Dunn and colleagues ([NOTE-1643](../notes.d/NOTE-1643.md)) support the distinction: the well-folded shapes are feasible
and reached, yet in their model the reference staple set ends misfolded in 52% of runs against 1%
with broken seams, so reliability of reaching is a design property apart from feasibility
(experimental fitted yields 36-62%). Schneider, Möritz and Dietz ([NOTE-1641](../notes.d/NOTE-1641.md)) qualify it: with
the earliest-binding domains removed the target is still reached, "via another, slower pathway",
so reachability survives while speed does not; they report no yields, so reliability is not
measured there.

No status changes.

## Note of 2026-11-05: A's synthesis on DNA origami

From the synthesis on DNA origami by another assistant (A), pasted by the owner on 2026-11-05 and filed with its four further works in this pull request.

A closes on the claim's distinction: "The intended organization is specified in the design. The realized organization is produced by dynamics. Its persistence is a further property." That is this claim together with [CLAIM-566](CLAIM-566.md). Two of A's further works add numbers. In Majikes et al. 2021 ([NOTE-1633](../notes.d/NOTE-1633.md)), a single fold is feasible, yet at high staple excess fewer than half the molecules fold. In Douglas et al. 2009 ([NOTE-1629](../notes.d/NOTE-1629.md)), multilayer designs fold at 7 to 44 % after week-long anneals.

No status changes.

## Note of 2026-11-05: the further DNA origami readings

The works cited in A's two syntheses on DNA origami, pasted by the owner on 2026-11-05, read in this pull request.

**Lee Tin Wah et al., "Observing and controlling the folding pathway of DNA origami".** Lee Tin Wah et al. (2016), [LIT-2137](../literature.d/LIT-2137.md), qualify the claim. The same
target rectangle is reached under both staple allocations, so it is
feasible and reachable either way; but reliability is quantified only
under the standard allocation (85% defect-free). Under the altered one the
paper reports only "normal rectangles ... on a rugged surface" and a
reduced bulk signal, with no yield, so reliably-reachable is left
unquantified there.

**Majikes, Patrone, Kearsley, Zwolak and Liddle, "Failure Mechanisms in DNA Self-Assembly".** Majikes et al. (2021), [LIT-2133](../literature.d/LIT-2133.md), read in [NOTE-1633](../notes.d/NOTE-1633.md), support the
claim directly and sharply. The folded state is feasible and reached, yet
at high staple excess reached by under half the molecules, not because
feasibility fails but because an equilibrium competitor, the blocked
state, is favoured: folded/blocked = j_fold/[staple]. Reliability is a
continuous quantity set by S0/j, distinct from feasibility and from bare
reachability.

**Douglas, Dietz, Liedl, Högberg, Graf and Shih, "Self-assembly of DNA into nanoscale three-dimensional shapes".** Douglas et al. (2009), [LIT-2130](../literature.d/LIT-2130.md), read in [NOTE-1629](../notes.d/NOTE-1629.md), support the
claim. Multilayer designs are feasible and reachable but reached reliably
only in 7–44% of scaffold, and the same feasible design is not reached at
all under a 1.2 h ramp, at 4 mM Mg2+ or at high Na+. Feasible, reachable
and reliably reached come visibly apart.

**Douglas, Bachelet and Church, "A Logic-Gated Nanorobot".** Douglas, Bachelet and Church (2012), [LIT-2136](../literature.d/LIT-2136.md), read in [NOTE-1634](../notes.d/NOTE-1634.md),
support the claim. The closed barrel is feasible; the open state is
reachable only given the right antigen keys; and the reliability of
reaching it is tuned by lock-duplex length (shorter locks open at lower
key concentration but spontaneously more often) and reported as population
fractions, not certainty.

**Aksel, Navarro, Fong and Douglas, "Design principles for accurate folding of DNA origami".** Aksel et al. (2024), [LIT-2125](../literature.d/LIT-2125.md), read in [NOTE-1642](../notes.d/NOTE-1642.md), support the separation weakly. Each of four published multilayer blocks is feasible and is reached at 2-6% gel-measured yield. Redesigning only the staple breakpoints, and for one block also the scaffold seam, reaches the nominally same layout at 48-61%. Reliability here is one hand-bounded gel window after one anneal, with no stated replicates. The reading leaves open whether the gain holds under a counted measure.

**Majikes, Hasni, Haridas, Robertson, Pintar, Zwolak and Liddle, "Complex cooperativity in DNA origami revealed via design-dependent defectivity".** Majikes et al. (2026), [LIT-2127](../literature.d/LIT-2127.md), read in [NOTE-1639](../notes.d/NOTE-1639.md), support the separation empirically. 34 designs encode one feasible 2D target. Under one fixed protocol, how reliably the target is reached varies with design: defectivity runs from about 10 to 35, and the largest uncertainty, staple-pool variation, is ±2.8. The reading leaves open whether the ordering holds under standard anneals, a check that rests on supplementary sections not read.

**Ni, Zhou, Zhu, Bershadsky, Ai, Wang, Sha, Seeman and Chaikin, "Cooperativity, entropy, and effective concentration in DNA origami self-replication".** Ni et al. (2026), [LIT-2124](../literature.d/LIT-2124.md), read in [NOTE-1630](../notes.d/NOTE-1630.md), support the separation for replication. In their model, separating very large tile patterns is feasible. In experiment, separation was reached only up to tetramers before the tiles unravelled, and the per-cycle replication rate fell from about 1.9 for dimers to 1.6 for tetramers. The reading leaves open where the practical limit lies beyond four tiles.

No status changes.

## Note of 2026-11-05: Shirt-Ediss et al., "Optimising DNA origami assembly by reducing off-target interactions", read

Cited in A's third synthesis on DNA origami, pasted by the owner on 2026-11-05.

**Shirt-Ediss, Torelli et al., "Optimising DNA origami assembly".** Shirt-Ediss, Torelli et al. (2026), [LIT-2123](../literature.d/LIT-2123.md), read in [NOTE-1627](../notes.d/NOTE-1627.md), support the claim and give the
cleanest instance on the record: for four DNA origami shapes, three scaffold sequences each with fully
complementary staples realise one design, so every variant is feasible by construction, yet under one
protocol the share of well-folded objects ranges from about 65–75% to 0–20% according to the off-target
binding the sequence allows. It leaves open the line between reachable and reliably reachable, since some
objects of the off-target-prone variants are well folded, and the cause of the failures is inferred, not
observed.

No status changes.

## Note of 2026-11-05: the readings on correction, repair, replication and nucleation barriers

Read at the owner's invitation to add readings to the DNA origami filing; the works were chosen by the assistant.

**Winfree and Bekbolatov, "Proofreading tile sets"; Scheckenbach et al., "Self-regeneration and self-healing".** Both separate reachable from reliably reached.
- In Winfree and Bekbolatov ([LIT-2119](../literature.d/LIT-2119.md)), the direct and proofreading tile sets reach the same target in the aTAM, but with 1 % against 0.01 % error at the same kTAM conditions.
- In Scheckenbach et al. ([LIT-2139](../literature.d/LIT-2139.md)), repair of a 12HB missing nine staples brings about half the defective structures back to intact (63 % → 32 % defective): reachable, not reliably reached.

Left open: neither gives the reliability as a function of resource.

**Zhou, Sha, Ni, Seeman and Chaikin, "Mutations in artificial self-replicating tiles".**

- The target dimer is feasible without a seed, yet in the cycle "no dimer was formed without the seed" (Zhou et al. 2021, Fig. 3C). Feasibility is not reachability.
- The one-sided design's ceiling of 2 per cycle is reached only in part (1.6 in the mixed run), so reaching is not reliable.
- Left open: how the unseeded rate (0.0007 dimers/monomer cycle) scales.

No status changes.
