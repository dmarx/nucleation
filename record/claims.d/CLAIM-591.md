---
number: 591
status: Proposed
formerly:
- CLAIM-tmpy685m
title: 'Connectivity of the configurations affordable at a budget does not settle reachability among them: under directed moves a state can share a connected component with a target and have no admissible path to it, and the least budget for going from one configuration to another can differ from that for coming back, so a persistence summary of sublevel sets bounds the reachability filtration without fixing it'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the constructions: a directed path from v to u in the two-state
  system, or a least budget from v to u below 3 in the three-state one; or a
  directed path between two configurations that leaves the component of the
  sublevel set containing them. Not defeated by systems whose moves are all
  reversible at the same cost, where connectivity and reachability coincide;
  the claim says connectivity does not settle reachability in general.
tags:
- mathematics
- complex-systems
- control-theory
date: '2026-11-05'
line:
- realizability
- formal-apparatus
grounds:
- THEORY-1434
- THEORY-1376
- THEORY-1415
complements:
- CLAIM-560
- CLAIM-571
- CLAIM-568
uses:
- TERM-114
summary: >-
  A's proposal, from the pasted synthesis on resource-bounded realizability
  (three responses, pasted by the owner on 2026-11-05, continuing the
  exchange on constraint architectures), Response 3 §5: "Topology records
  what is connected, not necessarily what can be computationally or
  dynamically traversed", and "Ordinary topological connectivity is
  symmetric; computational reachability need not be." Demonstrated by the
  filer on two small systems, one with a one-way move and one where going
  costs 1 and coming back 3. The readings give real instances: deadlocks in
  a connected state space of concurrent programs (Raussen), defect states of
  a Kresling stack left only irreversibly, and Lawvere's non-symmetric
  metrics. Every directed path stays in one component, so persistence gives
  a necessary condition only. It qualifies [CLAIM-571](CLAIM-571.md) and
  [CLAIM-568](CLAIM-568.md), which do not say whether their paths are directed. The
  wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: NOTE-tmpwxm2p — Skimmed; cited from the DNA origami readings of 2026-11-05 -->
<!-- inactive-ok-file: CLAIM-560 CLAIM-568 CLAIM-571 CLAIM-585 NOTE-1585 THEORY-1376 THEORY-1415 — Proposed or Skimmed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# CLAIM-591: Connectivity of the configurations affordable at a budget does not settle reachability among them: under directed moves a state can share a connected component with a target and have no admissible path to it, and the least budget for going from one configuration to another can differ from that for coming back, so a persistence summary of sublevel sets bounds the reachability filtration without fixing it

## The claim

A (Response 3 §5): "Topology records what is connected, not necessarily
what can be computationally or dynamically traversed. Two states might lie
in the same connected component of a geometric configuration space while
the available actuators cannot move the system from one to the other. And
a system may permit motion from A to B but not from B to A. Ordinary
topological connectivity is symmetric; computational reachability need
not be." A proposes "three levels together": persistent homology,
"Directed paths and reachability", and "Resource-graded process
composition".

**Two constructions (the filer's).** Each state's requirement is r and a
path is affordable at b when every state on it has r ≤ b.

- **One-way.** States u and v, r = 1 each, one move u → v. At every
  b ≥ 1 they form one connected component and v never reaches u: the least
  budget from u to v is 1, from v to u infinite.
- **Asymmetric thresholds.** States u, v, w with r = 1, 1, 3 and moves
  u → v, v → w, w → u. The least budget from u to v is 1; from v back to u
  it is 3, through w. A persistence summary of the sublevel sets, which
  forgets direction, merges u and v at 1 both ways.

Checked by the filer by enumeration.

**Necessary, not sufficient.** Every directed path lies in one component of
the sublevel set joined by the moves read without direction. So if q
reaches q′ at b they share a component of Q(b), and the zero-dimensional
persistence of r bounds the reachability filtration of [CLAIM-560](CLAIM-560.md) from
above. When every move can be undone at the same cost the two coincide,
and [CLAIM-571](CLAIM-571.md)'s threshold is the merge level.

**Instances in the readings.**

- **Concurrency** (Raussen, [LIT-2073](../literature.d/LIT-2073.md), the stand-in for Fajstrup,
  Goubault and Raussen). In the state space of a program whose processes
  share resources of given capacities, a deadlock is a state in the
  connected space from which no nontrivial directed execution leaves, and a
  doomed region is joined to the target topologically and by no directed
  path. There the obstruction comes from the capacities themselves: the
  forbidden region is where concurrent demands exceed a resource's
  capacity, so A's second and third levels coincide in that model.
- **Origami** ([NOTE-1617](../notes.d/NOTE-1617.md); [THEORY-1415](../theory.d/THEORY-1415.md)). A series stack of bistable
  Kresling barrels has defect states that the loading protocol cannot reach
  and can leave only irreversibly.
- **Costs** (Lawvere; [NOTE-1585](../notes.d/NOTE-1585.md); [THEORY-1376](../theory.d/THEORY-1376.md)). A generalized metric
  need not be symmetric: "the natural asymmetry carries considerable
  information". Lawvere's example, as the reading reports it, is the work
  needed to get from a to b in mountainous country.

## What it does not say

- **That directed topology is required.** Lawvere's non-symmetric
  enrichment carries the asymmetry at the level of costs, before any
  homotopy; A turns to directed homotopy for it, and the readings show
  either can.
- **That the held thresholds are wrong.** [CLAIM-571](CLAIM-571.md) and [CLAIM-585](CLAIM-585.md)
  are stated over paths without direction, which is right for reversible
  moves. For one-way moves the threshold from A to B and from B to A are
  two numbers. [CLAIM-568](CLAIM-568.md)'s geometric disconnection, no path in
  the fixed configuration space, covers a deadlock in a connected space
  only if its paths are read as directed.
- **That direction means dissipation.** In the concurrency model it is the
  progress of each process's program, not physical irreversibility.

## Note of 2026-11-05: the DNA origami readings

Read on the owner's request to connect the record's realizability inquiry to DNA origami; the works were chosen by the assistant.

**Sobczak, "Investigations of the DNA origami folding process".** Sobczak's dissertation (2018), [LIT-tmpwddcn](../literature.d/LIT-tmpwddcn.md), read in part in [NOTE-tmpwxm2p](../notes.d/NOTE-tmpwxm2p.md), supports directed,
asymmetric costs empirically: leaving the folded state takes 5–10 °C more than entering it ("We
observe a significant hysteresis"), and unfolding runs "on the order of seconds" against minutes to
hours for folding. The 2012 abstract calls unfolding equilibrium where the thesis calls it less out
of equilibrium than folding; the full Science paper was not read.

**Marras, Zhou, Su and Castro, "Programmable motion of DNA origami mechanisms".** Marras et al. (2015), [LIT-tmp11aw1](../literature.d/LIT-tmp11aw1.md), support the claim qualitatively. Closing and reopening their DNA origami Bennett linkage are different one-way chemical moves:
- Inputs differ: bridging strands at twofold excess close it, displacing strands at twentyfold excess over those reopen it.
- Rates differ: half-times of 55 s closing and 49 s expanding.

The configuration returns while the reagent state does not. The paper reports one cycle only, and it leaves open whether repeated cycling or waste accumulation changes what is reachable.

**Dunn et al. and Dannenberg et al., two DNA origami readings.** Both support the claim at the edge. Dunn and colleagues ([NOTE-tmpvgzvb](../notes.d/NOTE-tmpvgzvb.md)): seams bound "effectively,
irreversibly" make a target unreachable from a part-folded state in the same configuration
space, and cooling and heating show hysteresis. Dannenberg and colleagues ([NOTE-tmpyo994](../notes.d/NOTE-tmpyo994.md)): a
three-domain staple's direct 101 → 111 move "is impossible, as the central staple domain and the
scaffold cannot twist round each other", a one-way topological restriction between states one
domain apart, and binding and unbinding rates depend on temperature in opposite ways. Neither
measures directed costs between configurations.

No status changes.

## Note of 2026-11-05: the readings on correction, repair, replication and nucleation barriers

Read at the owner's invitation to add readings to the DNA origami filing; the works were chosen by the assistant.

**Winfree and Bekbolatov, "Proofreading tile sets".** Qualifies. The kTAM obeys detailed balance, yet the paper's kinetic-trap models treat coverage of a mismatched tile by further growth as an irreversible step at a fitted rate. A microscopically reversible system is effectively one-way at the time scales that matter, and a covered mismatch is not reached back. Left open: the freezing rates are fitted with "no strong justification" (footnote 9).

No status changes.
