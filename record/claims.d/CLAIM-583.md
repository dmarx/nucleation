---
number: 583
status: Proposed
formerly:
- CLAIM-tmpsbz28
title: 'Two constraint systems can have the same compatibility complex, the same move rule and the same costs and differ in whether a configuration meeting one demand reaches one meeting another, so compatibility equivalence does not imply equivalence of reachability; and of two constraint languages both NP-complete to satisfy, navigation can be polynomial for one and PSPACE-complete for the other'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a single flip within {000, 111} that joins
  the two configurations, or a difference between the two systems'
  compatibility complexes; or an error in the cited classifications, so that
  deciding whether two solutions of a positive 1-in-3 SAT formula are joined
  by single flips is not polynomial, or that of a positive NAE-3SAT formula
  not PSPACE-complete. Not defeated by the smallness of the construction,
  which is a counterexample to an implication, nor by systems in which the
  complex and reachability happen to agree.
tags:
- mathematics
- complex-systems
date: '2026-11-05'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-347
grounds:
- THEORY-1407
- THEORY-1413
complements:
- CLAIM-567
- CLAIM-560
uses:
- TERM-114
summary: >-
  A's proposal, from the pasted synthesis on resource-bounded realizability
  (three responses, pasted by the owner on 2026-11-05, continuing the
  exchange on constraint architectures), Response 3 §1: "compatibility
  equivalence doesn't imply computational equivalence." Shown here twice.
  The filer's construction: configurations {000, 111} and {000, 001}, each
  pair split between two demands, moves by single flips within the set; the
  complexes agree and only the second is connected. Gopalan et al. give the
  version across languages: positive 1-in-3 SAT and positive NAE-3SAT are
  both NP-complete to satisfy, and deciding whether two solutions are joined
  is polynomial for the first and PSPACE-complete for the second, with
  components of exponential diameter possible when the language is not
  tight. The construction is the filer's, from A's separation of the
  configuration layer from the process layer; adopting it is the owner's
  call.
---
<!-- inactive-ok-file: NOTE-tmpwxm2p — Skimmed; cited from the DNA origami readings of 2026-11-05 -->
<!-- inactive-ok-file: CLAIM-560 CLAIM-567 NOTE-1584 NOTE-1613 TERM-114 THEORY-1407 THEORY-1413 — Proposed or Skimmed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# CLAIM-583: Two constraint systems can have the same compatibility complex, the same move rule and the same costs and differ in whether a configuration meeting one demand reaches one meeting another, so compatibility equivalence does not imply equivalence of reachability; and of two constraint languages both NP-complete to satisfy, navigation can be polynomial for one and PSPACE-complete for the other

## The claim

A (Response 3 §1): "Two systems can have different underlying
configurations while exhibiting exactly the same pattern of compatible and
incompatible demands." "We could call this compatibility equivalence. Yet
compatibility equivalence doesn't imply computational equivalence." A
names two ways it can fail: "two systems might admit exactly the same
satisfying configurations, while one permits efficient reconfiguration
between them and the other requires exponentially many operations", and
"An even sharper possibility: one may have a path between configurations
while the other has no admissible path whatsoever. The configuration layer
alone cannot detect that distinction."

**An instance (the filer's).** Two systems on three bits, every
configuration costing 0, a move being a single bit flip that stays within
the admissible set (Gopalan et al.'s solution graph):

| system | admissible configurations | D₁ | D₂ | moves |
|---|---|---|---|---|
| A | {000, 111} | {000} | {111} | none |
| B | {000, 001} | {000} | {001} | 000 ↔ 001 |

Both have the compatibility complex {∅, {1}, {2}} of [CLAIM-347](CLAIM-347.md): each demand
is met, the two never jointly. In A the configuration meeting D₁ cannot
reach the one meeting D₂; in B it can, in one move. Checked by the filer
by enumeration. Same complex, same move rule, same costs, different
reachability: A's "sharper possibility".

**The version across languages** (Gopalan, Kolaitis, Maneva and
Papadimitriou; [NOTE-1584](../notes.d/NOTE-1584.md); [THEORY-1407](../theory.d/THEORY-1407.md)). For S = {R1/3}, positive
1-in-3 SAT, "This set is tight (actually, it is componentwise bijunctive),
but not Schaefer": satisfiability is NP-complete and deciding whether two
solutions are joined by single flips through solutions is polynomial. For
S = {RNAE}, positive NAE-3SAT, satisfiability is NP-complete and both
connectivity problems are PSPACE-complete. For languages that are not
tight the solution graph can have components of exponential diameter
(Theorem 2.10), A's "exponentially many operations"; Schwerdtfeger
([NOTE-1613](../notes.d/NOTE-1613.md); [THEORY-1413](../theory.d/THEORY-1413.md)) corrects the boundary to safely tight and
gives diameter 2^Ω(√n) beyond it. Equal in the complexity of finding a
solution, opposite in the complexity of navigating between solutions.

**On A's first way.** With a fixed local move rule, as in the instance and
in Gopalan et al., the same set of admissible configurations gives the same
moves. Two systems with "exactly the same satisfying configurations" and
different reconfiguration therefore differ in their move rule, their
P_z in [TERM-114](../terms.d/TERM-114.md)'s terms, which is A's point that processes are a layer
of their own; with move rules free to differ, the separation is easy, and
the content lies in which move rules are natural for a substrate.

## What it does not say

- **That the complex is idle.** It is the right invariant for which demands
  can be jointly met ([CLAIM-347](CLAIM-347.md)), and [CLAIM-560](CLAIM-560.md) shows how its
  budgeted form sits beside the reachability filtration. It does not carry
  reachability.
- **That the two layers are unrelated.** Reachability needs feasibility
  ([CLAIM-567](CLAIM-567.md)): no configuration outside the admissible set is
  reached.
- **Anything about organizations.** The instance is abstract; whether an
  organization's moves are local in some such sense is A's analogy.

## Note of 2026-11-05: the DNA origami readings

Read on the owner's request to connect the record's realizability inquiry to DNA origami; the works were chosen by the assistant.

**Rothemund, "Folding DNA to create nanoscale shapes and patterns".** Rothemund (2006), [LIT-tmp5gf89](../literature.d/LIT-tmp5gf89.md), read in [NOTE-tmp8kyp2](../notes.d/NOTE-tmp8kyp2.md), qualifies and leaves open. "All merge
patterns create the same shape", so one target admits many staple sets, but no yields are compared
between merge patterns. The comparisons he reports (bridged against unbridged seams, linear against
circular scaffold) add or remove constraints or change the scaffold, so none holds the compatibility
complex fixed.

**Sobczak, "Investigations of the DNA origami folding process".** Sobczak's dissertation (2018), [LIT-tmpwddcn](../literature.d/LIT-tmpwddcn.md), read in part in [NOTE-tmpwxm2p](../notes.d/NOTE-tmpwxm2p.md), supports the claim in
kind but not in the strict sense: three routings of one brick shape with the same composition show
"more than two orders of magnitude of variation between the mean folding times" and fold at
different temperatures, but routing changes the complex. Permuting the scaffold sequence along one
routing changed nothing (§5.2.2), which is the closest the reading comes to the claim's case, and
it goes the other way.

**Wagenbauer, Wachauf and Dietz, "Quantifying quality in DNA self-assembly".** Wagenbauer, Wachauf and Dietz (2014), [LIT-tmpduceb](../literature.d/LIT-tmpduceb.md), read in [NOTE-tmpmw05j](../notes.d/NOTE-tmpmw05j.md), qualify only: two
42-helix-bundle variants of one shape, one "that differed in its topology of chain connectivity",
fold best at 52 °C and 48 °C. Different connectivity means a different complex, so this is a
same-target, different-architecture case rather than the claim's.

**Dunn, Dannenberg, Ouldridge, Kwiatkowska, Turberfield and Bath, "Guiding the folding pathway of DNA origami".** Dunn and colleagues ([LIT-tmpqku12](../literature.d/LIT-tmpqku12.md), [NOTE-tmpvgzvb](../notes.d/NOTE-tmpvgzvb.md)) anneal one dimer origami template, whose
well-folded shapes they argue are of roughly equal free energy, to different distributions of
those shapes by changing only the staples that stabilize intermediates: halving the long-range
seam staples shifts products strongly toward the 5:0 fold and, in their model, cuts misfolds from
52% to 1%. This qualifies the claim rather than instancing it: the targets and their energies are
held, but the staple change alters the move costs, so it is the same targets reached differently,
not the same complex, moves and costs. Whether a case meeting the claim's full condition exists in
origami is left open.

No status changes.

## Note of 2026-11-05: the further DNA origami readings

The works cited in A's two syntheses on DNA origami, pasted by the owner on 2026-11-05, read in this pull request.

**Majikes et al., "Failure Mechanisms in DNA Self-Assembly".** Majikes et al. (2021), [LIT-tmplg4lb](../literature.d/LIT-tmplg4lb.md), qualify the claim. Changing the
staple motif while keeping which scaffold sites are joined (same
complementarity) left yield unchanged; changing fold distance (geometry,
not complementarity) changed it. This supports the spirit, same
compatibility yet different outcome with geometry and concentration, while
the motif test is a null for the pure staple-set variant. No status
changes.

**Majikes, Hasni, Haridas, Robertson, Pintar, Zwolak and Liddle, "Complex cooperativity in DNA origami revealed via design-dependent defectivity".** Majikes et al. (2026), [LIT-tmpbkl3k](../literature.d/LIT-tmpbkl3k.md), qualify the reading of origami as a case of this claim. Their 34 designs share the target shape, but not the compatibility complex: routing, seams and staple motifs change which domains pair. What they show is the weaker "same target, different constraint system, different reliability". Sequence rotation, which keeps the routing and is the nearest to the same complex, changed nothing. The claim's strong condition remains without an experimental instance here.

No status changes.

## Note of 2026-11-05: Shirt-Ediss et al., "Optimising DNA origami assembly by reducing off-target interactions", read

Cited in A's third synthesis on DNA origami, pasted by the owner on 2026-11-05.

**Shirt-Ediss, Torelli et al., "Optimising DNA origami assembly".** Shirt-Ediss, Torelli et al. (2026), LIT-tmp91912, read in NOTE-tmp6ediz, support the claim at the domain
level and qualify it at the base level. The variants share design, routing and intended pairing, nearer to
one compatibility complex than the designs of Majikes et al. (2026), yet differ sharply in yield; but the
authors attribute the difference to extra off-target compatibilities, so the full base-level complex
differs. The reading shows that domain-level equivalence does not fix reachability; it is not a
counterexample within one fully specified complex.

No status changes.
