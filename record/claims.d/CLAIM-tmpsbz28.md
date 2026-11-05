---
status: Proposed
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
- THEORY-tmpmcxbv
- THEORY-tmpo2ib0
complements:
- CLAIM-tmp9jvpb
- CLAIM-tmp4rtpa
uses:
- TERM-tmpr3hl8
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
<!-- inactive-ok-file: CLAIM-tmp4rtpa CLAIM-tmp9jvpb NOTE-tmpec4ov NOTE-tmpwmx5d TERM-tmpr3hl8 THEORY-tmpmcxbv THEORY-tmpo2ib0 — Proposed or Skimmed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# CLAIM-tmpsbz28: Two constraint systems can have the same compatibility complex, the same move rule and the same costs and differ in whether a configuration meeting one demand reaches one meeting another, so compatibility equivalence does not imply equivalence of reachability; and of two constraint languages both NP-complete to satisfy, navigation can be polynomial for one and PSPACE-complete for the other

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
Papadimitriou; [NOTE-tmpec4ov](../notes.d/NOTE-tmpec4ov.md); [THEORY-tmpmcxbv](../theory.d/THEORY-tmpmcxbv.md)). For S = {R1/3}, positive
1-in-3 SAT, "This set is tight (actually, it is componentwise bijunctive),
but not Schaefer": satisfiability is NP-complete and deciding whether two
solutions are joined by single flips through solutions is polynomial. For
S = {RNAE}, positive NAE-3SAT, satisfiability is NP-complete and both
connectivity problems are PSPACE-complete. For languages that are not
tight the solution graph can have components of exponential diameter
(Theorem 2.10), A's "exponentially many operations"; Schwerdtfeger
([NOTE-tmpwmx5d](../notes.d/NOTE-tmpwmx5d.md); [THEORY-tmpo2ib0](../theory.d/THEORY-tmpo2ib0.md)) corrects the boundary to safely tight and
gives diameter 2^Ω(√n) beyond it. Equal in the complexity of finding a
solution, opposite in the complexity of navigating between solutions.

**On A's first way.** With a fixed local move rule, as in the instance and
in Gopalan et al., the same set of admissible configurations gives the same
moves. Two systems with "exactly the same satisfying configurations" and
different reconfiguration therefore differ in their move rule, their
P_z in [TERM-tmpr3hl8](../terms.d/TERM-tmpr3hl8.md)'s terms, which is A's point that processes are a layer
of their own; with move rules free to differ, the separation is easy, and
the content lies in which move rules are natural for a substrate.

## What it does not say

- **That the complex is idle.** It is the right invariant for which demands
  can be jointly met ([CLAIM-347](CLAIM-347.md)), and [CLAIM-tmp4rtpa](CLAIM-tmp4rtpa.md) shows how its
  budgeted form sits beside the reachability filtration. It does not carry
  reachability.
- **That the two layers are unrelated.** Reachability needs feasibility
  ([CLAIM-tmp9jvpb](CLAIM-tmp9jvpb.md)): no configuration outside the admissible set is
  reached.
- **Anything about organizations.** The instance is abstract; whether an
  organization's moves are local in some such sense is A's analogy.
