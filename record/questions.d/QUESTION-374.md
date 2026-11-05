---
number: 374
status: Open
formerly:
- QUESTION-tmp3icc7
title: 'What is the structure of a system''s individuation indexed jointly by an observing budget and an acting budget, which invariants of that bifiltration are computable, and where do observing and acting draw on the same resource so that the two cannot be raised together?'
version: 1
tags:
- individuation
- mathematics
- complex-systems
date: '2026-11-05'
line:
- realizability
summary: >-
  The assistant's own question, filed on 2026-11-05 at the owner's
  invitation to contribute, following [CLAIM-557](../claims.d/CLAIM-557.md): budgeted individuation
  runs in opposite directions from outside and from inside, so it is a
  two-parameter family. Three things are open: what structure that family
  has (it is a bifiltration, and multiparameter persistence warns that
  such objects need not have complete discrete invariants); which of its
  invariants can be computed for the toy systems filed here ([CASE-206](../cases.d/CASE-206.md),
  [CASE-212](../cases.d/CASE-212.md), [CLAIM-583](../claims.d/CLAIM-583.md)'s pair); and when observing and acting
  share one budget, so that a system or an inquirer must choose between
  telling more apart and being able to become more. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp7y162 CASE-tmpa6s9d CLAIM-592 CLAIM-572 — Proposed, new or Skimmed; cited from the assistant's reading across the DNA origami readings -->
<!-- inactive-ok-file: CASE-206 CASE-212 CLAIM-557 CLAIM-583 NOTE-1568 NOTE-1609 — Proposed or Skimmed; entries filed in this pull request, cited as open -->
<!-- inactive-ok-file: CLAIM-570 CASE-199 — Proposed; the frontier claim and its worked case, cited as open -->
<!-- inactive-ok-file: CLAIM-572 — Proposed; the shared-budget claim, cited as open -->

# QUESTION-374: What is the structure of a system's individuation indexed jointly by an observing budget and an acting budget, which invariants of that bifiltration are computable, and where do observing and acting draw on the same resource so that the two cannot be raised together?

## Why it is a question

[CLAIM-557](../claims.d/CLAIM-557.md) shows that the outside partition (what probes affordable at
o can tell apart) refines with o and the inside partition (what can be
turned into one another within a) coarsens with a. Their pair is a family
over two budgets. Three things follow that the record does not settle:

- **Structure.** Families over two parameters are where Vipond and Botnan
  and Lesnick ([NOTE-1609](../notes.d/NOTE-1609.md), [NOTE-1568](../notes.d/NOTE-1568.md)) show complete discrete
  invariants fail. Whether the special form here, one family refining and
  one coarsening over the same configurations, escapes that is open.
- **Computation.** For the record's small cases the two partitions can be
  listed. Which summary of the pair (for example, the set of budget pairs at
  which the partitions agree) is both informative and cheap is open.
- **Shared resources.** An organization often observes and acts with the
  same staff, time or attention. Where o + a is bounded, raising one lowers
  the other, and a system must choose between telling more apart and being
  able to become more. Whether that trade has a structure across cases, and
  whether [CLAIM-475](../claims.d/CLAIM-475.md)'s point that formulating questions costs resources is a
  special case of it, is open.

## What would answer it

A computation of both partitions over a grid of budget pairs for
[CASE-206](../cases.d/CASE-206.md) and [CLAIM-583](../claims.d/CLAIM-583.md)'s pair, with a summary invariant and a
proof of what it determines; and an organizational case in which observing
and acting draw on one budget, with the trade measured.

## Note of 2026-11-05: the two frontiers, a partial answer

A, reading this pull request, proposed comparing the outside and inside
partitions by inclusion. [CLAIM-570](../claims.d/CLAIM-570.md) makes that exact: the budget pairs
at which everything indistinguishable is mutually reachable form an up-set,
those at which everything mutually reachable is indistinguishable a
down-set, the partitions agree on their intersection, and both boundaries
have closed forms (the largest peak distance within an observational class;
the least budget separating two mutually reachable states). [CASE-199](../cases.d/CASE-199.md)
computes them. This answers the computation part of the question for
finite systems under peak costs. The structure of the whole two-budget
family, and organizations whose observing and acting draw on one budget remain
open. No status changes.

## Note of 2026-11-05: the degree-4 vertex computed

[CASE-206](../cases.d/CASE-206.md) now carries both frontiers for nine states of the vertex.
With probes for flatness, mode, side and depth at costs 1 to 4, the outside
and inside partitions agree non-trivially in one window
(3 ≤ o < 4, 1.125 ≤ a < 1.866), on the flat state and the four
half-branches; with side and depth costs swapped, only the trivial
agreements remain. That suggests the question's third part has teeth: which
distinctions a system's observers can afford early decides whether its
own reachable classes ever show up as individuals. No status changes.

## Note of 2026-11-05: one budget for observing and acting

The question's last part is answered in one setting by [CLAIM-572](../claims.d/CLAIM-572.md). With
o + a ≤ B and nested probes, the cheapest split is always at a probe cost,
the ready splits at a fixed budget can form separate intervals, and buying
probes while each lowers the total can stop short of the cheapest. On the
degree-4 vertex, with probe costs 1 to 4, the cheapest is pure acting
(1.866), and at B = 4 the ready splits are o in [0, 2.134] and o = 4. The
trade bites where a probe separates nothing a common response cannot cover
until a later probe completes the separation. No status changes.

## Note of 2026-11-05: the DNA origami readings, read across

The assistant's reading across the eight DNA origami readings filed on the owner's request to connect the record's inquiry to DNA origami. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.

Three things bear on the two-budget structure.

- **A resource can set the costs it pays.** Heat pays for crossing barriers and also sets the free energies, so reachability within a time budget is a window in temperature, not an up-set, and a schedule can reach what no constant level reaches (CLAIM-tmp7y162, CASE-tmpa6s9d). The acting budget of the question's frontier is the special case of a resource that leaves the costs fixed.
- **Probes are not ordered by cost.** Gel mobility and TEM cannot tell a 42-helix bundle with every staple from one missing up to 7 %, a cheap defect label can, and cryo-EM, far costlier, "might be able to resolve site-specific defects, but it will be blind to stochastically distributed defects" (Wagenbauer, Wachauf and Dietz, NOTE-tmpmw05j). Each probe still refines, but which distinctions a budget buys first is set by which probes are cheap, as CLAIM-592 says.
- **Observing can act.** In Rothemund's AFM (NOTE-tmp8kyp2), the settings that resolve a single missing staple also damage the sample: "repeated scanning created holes difficult to distinguish from holes due to missing strands". There the observing budget is spent partly out of the system's own integrity, so the two budgets are not separable, which is the converse of the dual-control case that CLAIM-572 excludes. Whether the frontier survives an observer whose probes change the states they sort is open.

No status changes.
