---
number: 922
status: Proposed
formerly:
- CLAIM-tmpmvt0a
title: 'In a model with a home and a staging architecture and one capacity, the same intervention, admitting the staging architecture, creates reachability where the home configuration space is disconnected and only lowers the bottleneck budget where it is connected, while a budget or a reserve changes neither the bottleneck budget nor the least time, and a deadline shorter than every route through the staging architecture takes that remedy away'
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-tmpsfjxu) at its
    membership pass of 2026-11-23, under ADR-104's rule: the revised
    manuscript in scratch/manuscripts/governance-of-possibility/ states
    its proposition or uses it as a step, in §9.1, §9.5. No other change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction or the computation of the executed study
  CASE-345: in the family it declares (holding costs h + βq(1 − q)
  with β ≥ 0 under each architecture, a switch at q costing the dearer
  of the two plus s, switching allowed at every q), a setting where the
  bottleneck budget with the staging architecture admitted differs from
  min(B*(home), max(max(h0, h1) + s, h1 + β1/4)); a setting with the
  home space disconnected where admitting it does not make B reachable,
  or with it connected where it does more than lower B*; a budget or
  reserve that changes B* or T*; or, in the base model, a route through
  the staging architecture that reaches B by time 2. Not defeated by
  other cost shapes, several resources, cumulative costs, a staging
  architecture faster than the home one, or real organizations that
  behave otherwise; the claim is about the declared model.
tags:
- operations-research
- mathematics
date: '2026-11-22'
line:
- realizability
- readiness
bears_on:
- QUESTION-392
rests_on:
- CLAIM-571
grounds:
- CASE-345
complements:
- CLAIM-568
- CLAIM-586
uses:
- TERM-115
summary: >-
  From the executed study [CASE-345](../cases.d/CASE-345.md), [LEAD-075](../leads.d/LEAD-075.md)'s run of A's staging
  experiment. Admitting a staging architecture is one intervention; in
  the model it creates reachability when a crease constraint disconnects
  the home space, and when the home space is connected it lowers the
  bottleneck budget or does nothing, by the closed form
  B*(staging admitted) = min(B*(home), max(max(h0, h1) + s, h1 + β1/4)),
  derived and confirmed in 960 settings. A budget or a reserve never moves
  the bottleneck budget or the least time; it moves the capacity toward
  them. The staging route saves capacity and costs time (at least 2.58
  against 1 in the base model), so at a deadline of 2 the architectural
  remedy is gone and a case reachable only through it becomes one
  reachable only with the reserve, or not in time. For [QUESTION-392](../questions.d/QUESTION-392.md):
  whether an intervention creates a capability or cheapens one is fixed
  here by the home architecture and the contingency's deadline, not by
  the kind of intervention. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
works:
- governance-of-possibility
---
<!-- inactive-ok-file: CASE-345 — new; the executed study this claim is grounded in, filed in the same batch -->

# CLAIM-922: In a model with a home and a staging architecture and one capacity, the same intervention, admitting the staging architecture, creates reachability where the home configuration space is disconnected and only lowers the bottleneck budget where it is connected, while a budget or a reserve changes neither the bottleneck budget nor the least time, and a deadline shorter than every route through the staging architecture takes that remedy away

## The claim

The model is [CASE-345](../cases.d/CASE-345.md)'s, which is [CASE-198](../cases.d/CASE-198.md)'s made a graph. A state
is (q, z): q ∈ [0, 1] and z the home architecture or a staging one. One
capacity must be held at every moment ([CLAIM-571](CLAIM-571.md)'s scope). Holding q
costs r0(q) = h0 + β0 q(1 − q) under home and r1(q) = h1 + β1 q(1 − q)
under staging, with β0, β1 ≥ 0; switching z at q peaks at
max(r0(q), r1(q)) + s and is allowed at every q. A = (0, home) and
B = (1, home). A crease constraint, when present, forbids home moves
across a stretch around q = 1/2.

1. **Admitting the staging architecture creates reachability or lowers
   the threshold, according to the home space.** Every path from A to B
   passes q = 1/2. Under home it pays r0(1/2) = B*(home) there. Under
   staging it pays r1(1/2) = h1 + β1/4 and must have switched at least
   once, at a q where the switch costs at least max(h0, h1) + s; the
   route that switches at q = 0, crosses under staging and switches back
   at q = 1 attains both bounds. So

     B*(staging admitted) = min(B*(home), max(max(h0, h1) + s, h1 + β1/4)).

   With the crease, B*(home) is infinite and the right-hand side is
   finite: the intervention creates reachability. Without it, the
   intervention lowers B* when the staging term is the smaller and
   otherwise does nothing. The study confirms the formula in all 960
   settings of its sweep: 480 with the crease, all made reachable; 211
   without it lowered, 269 unchanged. In the base numbers
   ([CASE-198](../cases.d/CASE-198.md)), 1.3 falls to 1.0.

2. **A budget or a reserve moves neither threshold.** B* and the least
   time T*(b) are functions of the architecture alone; a budget or a
   temporary reserve changes only whether the capacity b, or b + ρ,
   meets them. So neither ever makes an unreachable B reachable, which
   is [CLAIM-568](CLAIM-568.md)'s "added actuation can … not join disconnected
   configurations" and [CLAIM-586](CLAIM-586.md)'s budget bound, for transitions.

3. **A deadline can take the architectural remedy away.** In the base
   model a route through the staging architecture takes at least 2.58
   (two switches of 0.5 and a slower crossing) where the home route takes
   1. At a deadline of 2 the least capacity that arrives in time is 1.3
   with or without the staging architecture: the cases the study classed
   "only through an architectural change" become "only with a temporary
   reserve" or "too expensive", and, with the crease, "reachable, but not
   by the deadline". Readiness in [TERM-115](../terms.d/TERM-115.md)'s sense follows: at deadlines
   of 2 or less, admitting the staging architecture leaves it unchanged
   at every budget; at 3 or more, it shifts the readiness curve 0.3
   lower in budget.

**What it bears on.** [QUESTION-392](../questions.d/QUESTION-392.md) asks when an intervention creates a
capability rather than makes one cheaper, faster or more reliable to
reach. In this model the answer is not a property of the intervention.
The one intervention does each according to whether the home space is
connected, and whether it helps at all depends on the contingency's
deadline. A budget or a reserve always works on the capacity side and
never creates reachability.

## What it does not say

- **That staging is generally slower.** That follows from the times the
  model sets. A staging architecture faster to cross would reverse the
  trade, and a deadline would then favour it.
- **That "creates" is absolute.** Reachability is created relative to the
  home architecture. Relative to the declared space of (q, z) pairs, the
  path was always there, and admitting it lowered B* from infinity.
  [QUESTION-392](../questions.d/QUESTION-392.md)'s warning that the verdict turns on the declared space
  holds here exactly.
- **Anything about real organizations, several resources, or costs that
  accumulate.**
