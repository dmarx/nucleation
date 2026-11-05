---
number: 571
status: Proposed
formerly:
- CLAIM-tmpbi4ca
title: 'For a fixed architecture, the resource threshold for reaching a target configuration need not equal the resource requirement of the target: it is the least, over admissible transition paths, of the peak requirement along the path, and it is infinite when no admissible path joins the two'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a path from 0 to 1 within [0, 1] whose
  largest value of r(q) = 0.7 + 2.4q(1 − q) is below 1.3, a bottleneck
  budget below the larger endpoint requirement, or a mistake in the
  sublevel set at 1.0. Not defeated by resources that are cumulative or
  rate-limited rather than capacities, by several resources at once, or
  by a change of architecture that lowers the threshold; the claim is
  about one capacity under one fixed architecture.
tags:
- mathematics
- operations-research
- complex-systems
date: '2026-11-05'
line:
- readiness
- realizability
- formal-apparatus
grounds:
- THEORY-1423
- THEORY-1420
complements:
- CLAIM-567
uses:
- TERM-106
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4. A's wording,
  with A's own definition of the threshold, B*(A, B) = inf over paths of
  max r along the path, written into it. Demonstrated by A's example
  r(q) = 0.7 + 2.4q(1 − q), checked: both endpoints cost 0.7, the
  threshold is 1.3, and at 1.0 the feasible set has two components.
  Mirth et al. show the threshold is the zero-dimensional merge level of
  the sublevel sets; Berry, Lee-Trimble and Santangelo give a case where
  it is infinite. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: NOTE-tmpwxm2p CASE-206 — Proposed, Skimmed; cited from the DNA origami readings of 2026-11-05 -->
<!-- inactive-ok-file: THEORY-1423 THEORY-1420 CLAIM-567 CLAIM-585 TERM-106 CASE-198 CASE-200 CLAIM-354 — Proposed; the readings' accounts and A's proposals of 2026-11-04, cited as filed, nothing here rests on their being settled -->
<!-- inactive-ok-file: CASE-204 CASE-206 CASE-207 CASE-208 CASE-211 CLAIM-569 TERM-105 — Proposed or new; entries of 2026-11-05 from the pasted synthesis on constraint architectures, cited as open -->
<!-- inactive-ok-file: NOTE-1585 CLAIM-563 NOTE-1581 CLAIM-591 CLAIM-560 CLAIM-586 — Proposed or new; the resource-bounded realizability readings of 2026-11-05, cited as open -->

# CLAIM-571: For a fixed architecture, the resource threshold for reaching a target configuration need not equal the resource requirement of the target: it is the least, over admissible transition paths, of the peak requirement along the path, and it is infinite when no admissible path joins the two

## The claim

A: "For a fixed architecture, the resource threshold for reaching a
target configuration need not equal the resource requirement of the
target. It depends on admissible transition paths, and may be infinite
when the configurations are disconnected under the allowed
transformations."

**The construction (A's).** Fix an architecture. Let Q be its
configurations, r(q) the resource it takes to hold q (an instantaneous
capacity), and Γ(A, B) the continuous paths from A to B that the declared
transformations allow. The bottleneck budget is

  B*(A, B) = inf over γ ∈ Γ(A, B) of max_t r(γ(t)),

with the infimum over no paths read as +∞.

- **Never below the endpoints.** Every path contains A and B, so
  B*(A, B) ≥ max(r(A), r(B)).
- **Can be above them.** A's example: Q = [0, 1], A = 0, B = 1,
  r(q) = 0.7 + 2.4q(1 − q). Then r(0) = r(1) = 0.7. Every path from 0 to
  1 in [0, 1] passes through q = 1/2, where r = 1.3, and the straight path
  reaches no more, so B* = 1.3. At a budget of 1.0 the feasible set
  {q : r(q) ≤ 1.0} is q(1 − q) ≤ 1/8, that is [0, 0.1464…] ∪ [0.8536…, 1],
  the roots being (1 ± √½)/2: two components, each endpoint feasible and
  neither reachable from the other. The components merge at 1.3. Checked
  by the filer.
- **Can be infinite.** If the declared transformations admit no path,
  B* = +∞ whatever the endpoints cost.

The gap B* − max(r(A), r(B)) is the reconfiguration slack of the
transition ([TERM-106](../terms.d/TERM-106.md)): 0.6 in the example.

**What the readings add.**

- **The threshold is a merge level** (Mirth et al., [NOTE-1616](../notes.d/NOTE-1616.md);
  [THEORY-1420](../theory.d/THEORY-1420.md)). In sublevel-set persistent homology "two configurations
  are in the same connected component if there is a path between the
  configurations that does not exceed the chosen energy barrier". So B*
  is the level at which A and B first share a component of {r ≤ b}, the
  death of a zero-dimensional bar, the node joining them in a
  disconnectivity graph. That summary keeps only the lowest barrier:
  "Though disconnectivity graphs encode the energy barrier of the minimal
  energy pathway between two local minima, they do not represent multiple
  transition pathways." Other routes and their barriers are in the
  one-dimensional bars, which B* does not use.
- **A case where it is infinite** (Berry, Lee-Trimble and Santangelo,
  [NOTE-1605](../notes.d/NOTE-1605.md); [THEORY-1423](../theory.d/THEORY-1423.md)). For a near-flat rigid origami vertex with
  positive curvature, "the two nappes have split into two disconnected
  components". Every state on either nappe is feasible; under folding
  without self-intersection none on one can reach the other at any cost.
  It is relative to the declared transformations: "Anecdotally, it does
  appear that when faces are allowed to pass through each other,
  isometric trajectories can pass from one nappe to the other for any K."
  A: "impossibility is relative to the declared model of admissible
  transformations".

**The architecture is part of the statement.** Change it and Q, r and Γ
change with it. [CASE-198](../cases.d/CASE-198.md) lowers the threshold in A's example from 1.3
to 1.0 by admitting a switch to a staging architecture as a move, and
[CASE-200](../cases.d/CASE-200.md) shows a per-period budget of 1.0 reaching 1.3 by carry-over.

It is the resource-quantitative form of the separation between a feasible
target and a reachable one ([CLAIM-567](CLAIM-567.md)).

## What it does not say

- **That the peak is the only cost.** B* is for a capacity that must be
  held at each moment. A's table of resource types also has fixed stock,
  rate limit, cumulative expenditure, replenishable reserve and deadline.
  For cumulative expenditure a path costs its integral, not its peak, and
  time can substitute for peak capacity: A's example is two units for one
  minute against one unit for two.
- **Anything for several resources at once.** Then there is no scalar
  threshold ([CLAIM-585](CLAIM-585.md)).
- **That organizations have such an r.** The construction is formal; an
  organizational configuration space with a holding requirement is A's
  model, not something the record has measured.
- **That sublevel-set inclusion is viability.** Mirth et al.'s sublevel
  sets are caps on a scalar, not viability kernels ([THEORY-134](../theory.d/THEORY-134.md)); and
  inclusion of what is reachable under a cap is only a scalar case of the
  inclusion [CLAIM-354](CLAIM-354.md) compares agents by.

## Note of 2026-11-05: A's resource models and further distinctions

Later entries from the same paste instance and extend the claim. [CASE-206](../cases.d/CASE-206.md) is a real mechanism's version: a degree-4 origami vertex whose branch switch must pass the flat state, so its footprint threshold (about 1.87) exceeds both endpoints (0.75 and 0.875). [CASE-204](../cases.d/CASE-204.md) and [CASE-207](../cases.d/CASE-207.md) give the infinite case, and [CASE-208](../cases.d/CASE-208.md) the qualifier "for a fixed architecture" at work in a built system. The time-for-peak example and the resource-type table this claim mentions in passing are now [CASE-211](../cases.d/CASE-211.md) and [TERM-105](../terms.d/TERM-105.md), and construction cost as a third requirement is [CLAIM-569](CLAIM-569.md). No status changes.

## Note of 2026-11-05: the resource-bounded realizability readings

Readings filed beside the pasted synthesis on resource-bounded realizability place B* and price it. The readers of Lawvere ([NOTE-1585](../notes.d/NOTE-1585.md)) and of Marsden and Zwart ([NOTE-1602](../notes.d/NOTE-1602.md)) check that ([0, ∞], inf, max) is a quantale, so B* is the hom of the free category it enriches on the configuration graph, the closure over paths. Using max as the tensor is the readers' step; it is not among Marsden and Zwart's examples. In that category the affordable processes compose at every budget ([CLAIM-563](CLAIM-563.md)).

Ito et al. ([NOTE-1595](../notes.d/NOTE-1595.md)) make B* the minmax objective of their §4 and show that computing it can be hard: minmax power supply reconfiguration is strongly NP-hard (Lemma 3), maxmin clique reconfiguration has no constant-factor approximation unless P = NP (Theorem 4), and minmax set cover reconfiguration has a linear-time 2-approximation (Theorem 6). The reading of Raussen ([NOTE-1581](../notes.d/NOTE-1581.md)) and [CLAIM-591](CLAIM-591.md) add that under one-way moves B*(A, B) and B*(B, A) can differ, which the claim's undirected paths do not show. [CLAIM-560](CLAIM-560.md) pairs the threshold with [CLAIM-586](CLAIM-586.md)'s compatibility filtration; neither determines the other. No status changes.

## Note of 2026-11-05: the DNA origami readings

Read on the owner's request to connect the record's realizability inquiry to DNA origami; the works were chosen by the assistant.

**Sobczak, "Investigations of the DNA origami folding process".** Sobczak's dissertation (2018), [LIT-tmpwddcn](../literature.d/LIT-tmpwddcn.md), read in part in [NOTE-tmpwxm2p](../notes.d/NOTE-tmpwxm2p.md), supports the claim for
one step: isothermal folding near 50 °C still needs a brief denaturation first, since "this step
remains necessary to break up pre-existing secondary structures", so the path's peak exceeds what
folding and holding need. For a short-domain design the path down from 65 °C decides whether a
40 °C hold folds at all. Temperature acts as a window, not a monotone budget, so the peak reading
fits the denaturation step only.

**Marras, Zhou, Su and Castro, "Programmable motion of DNA origami mechanisms".** Marras et al. (2015), [LIT-tmp11aw1](../literature.d/LIT-tmp11aw1.md), qualify the claim in the reverse direction. The compacted state of their DNA origami Bennett linkage is cheap to reach: thermal motion visits it at no input cost. It is dear to hold, needing bound bridging strands or locking staples against what the authors take to be electrostatic repulsion. So the reaching threshold and the holding requirement differ here because holding costs more, not reaching. The paper measures no threshold over the path. Compare [CASE-206](../cases.d/CASE-206.md), where passage costs more than either end state.

**Dunn et al. and Dannenberg et al., two DNA origami readings.** Dunn and colleagues ([NOTE-tmpvgzvb](../notes.d/NOTE-tmpvgzvb.md)) support it qualitatively: from the part-folded 1:1
intermediate, the 5:0 fold is "inaccessible unless at least one seam connection is broken", a
barrier beyond what holding the target takes, though none is measured. Dannenberg and colleagues
([NOTE-tmpyo994](../notes.d/NOTE-tmpyo994.md)) support it in a kinetic sense: in their domain-level model, 10 against 0.1 °C per
minute lowers the annealing temperature by 5.3 °C and raises melting by about 1.3 °C, and fewer
staples lower annealing but not melting. Their model has a unique equilibrium at each temperature,
so this is rate-dependent hysteresis from barriers, not a peak-cost path in the claim's sense;
whether origami shows the latter is left open.

No status changes.

## Note of 2026-11-05: the further DNA origami readings

The works cited in A's two syntheses on DNA origami, pasted by the owner on 2026-11-05, read in this pull request.

**Majikes et al., "Failure Mechanisms in DNA Self-Assembly".** Majikes et al. (2021), [LIT-tmplg4lb](../literature.d/LIT-tmplg4lb.md), support the claim as a hypothesis in
the whole-origami story: leaving the blocked state needs a whole staple
displaced, possible only once neighbouring folds raise the local j-factor,
whereas holding the fold needs no such thing, so the transition threshold
differs from the holding requirement. At the single fold no path cost is
measured.

**Ni, Zhou, Zhu, Bershadsky, Ai, Wang, Sha, Seeman and Chaikin, "Cooperativity, entropy, and effective concentration in DNA origami self-replication".** Ni et al. (2026), [LIT-tmpairr7](../literature.d/LIT-tmpairr7.md), support the claim. Separating daughter from parent requires a peak of about 50 °C, unlike the 18 °C hold at which the complex forms. A feasible cycle exists only while that peak stays below the temperature at which the tiles unravel. The authors "could barely separate tetramers". The reading leaves open how the peak requirement grows past four tiles, which the model predicts and experiment has not reached.

No status changes.

## Note of 2026-11-05: the readings on correction, repair, replication and nucleation barriers

Read at the owner's invitation to add readings to the DNA origami filing; the works were chosen by the assistant.

**Cumberworth, Frenkel and Reinhardt, "Design-dependent nucleation barriers".** Supports. In simulation, reaching the folded three-row design at Tm means crossing about 10 kBT (about 20 kBT at domain resolution) above both end states, more than holding it needs. A few degrees below Tm the barrier is gone, so the reach threshold equals the hold threshold there.
- Scheckenbach et al. ([LIT-tmpzoh9c](../literature.d/LIT-tmpzoh9c.md)) support it in kind: restoring a kinked 12HB needed heating to 50 °C.
- Winfree and Bekbolatov ([LIT-tmp1pdwj](../literature.d/LIT-tmp1pdwj.md)) weakly qualify it: escaping a mismatch costs time, not a peak.

Left open: the profile is a one-dimensional projection, and no kinetics are simulated.

**Zhou, Sha, Ni, Seeman and Chaikin, "Mutations in artificial self-replicating tiles".**

- Separating daughter from template needs 48 °C, while the configuration is formed and held at 22 °C (Zhou et al. 2021, Methods).
- The threshold for the transition exceeds what the target needs to persist.

No status changes.
