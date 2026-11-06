---
number: 106
status: Proposed
formerly:
- TERM-tmp2ysyt
title: 'reconfiguration slack: the temporary resources a system needs to move between two configurations it can each hold, beyond what holding either one requires, while keeping specified commitments'
version: 1
tags:
- operations-research
- complex-systems
- society-and-governance
date: '2026-11-05'
line:
- readiness
refines:
- TERM-107
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4. A's
  definition: "temporary resources required to move between otherwise
  feasible organizational regimes while preserving specified
  commitments". Made exact here as the gap between the bottleneck budget
  of a transition and the larger of its endpoints' holding requirements,
  infinite when no admissible path joins them. It folds in A's
  "resource-constrained reconfiguration", the name of the inquiry rather
  than a concept, and A's three reserves (operational, reconfiguration,
  competency), of which this is the second. A special case of
  organizational slack: measured against current output it is slack, and
  its use is the transition, which the output does not show. The wording
  is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-107 TERM-115 TERM-112 TERM-110 CLAIM-571 CLAIM-585 CLAIM-558 CASE-198 CASE-200 — Proposed; A's proposals of 2026-11-04 and the entries filed beside them, cited as filed -->
<!-- inactive-ok-file: CASE-206 TERM-105 — Proposed or new; entries of 2026-11-05 from the pasted synthesis on constraint architectures, cited as open -->

# TERM-106: reconfiguration slack: the temporary resources a system needs to move between two configurations it can each hold, beyond what holding either one requires, while keeping specified commitments

## Definition

A: "Reconfiguration slack: temporary resources required to move between
otherwise feasible organizational regimes while preserving specified
commitments."

Made exact, for one resource. Let r(q) be what it takes to hold
configuration q, and let the admissible paths from A to B be those
allowed by the declared transformations along which the specified
commitments hold throughout. The bottleneck budget B*(A, B) is the least,
over admissible paths, of the largest r met along the path, and +∞ if
there is none ([CLAIM-571](../claims.d/CLAIM-571.md)). The reconfiguration slack of the
transition is

  σ(A → B) = B*(A, B) − max(r(A), r(B)) ≥ 0.

It is zero when some admissible path never costs more than the costlier
endpoint, positive when every path climbs above both, and infinite when
the two are disconnected. In A's example, r(q) = 0.7 + 2.4q(1 − q) on
[0, 1], both endpoints cost 0.7 and B* = 1.3, so σ = 0.6. With several
resources the slack is not a number but the set of budgets that suffice,
less what holding requires ([CLAIM-585](../claims.d/CLAIM-585.md)).

The term's job is to name a resource whose use the current output does
not show. A's closing: "Slack isn't merely unused capacity held in
reserve against disturbances. It can be the resource that makes an
otherwise inaccessible organizational transformation possible." A
transition needing σ > 0 is feasible at both ends and unreachable on any
budget that covers only the ends.

**Relative to the declared transformations and to the architecture.** σ
is computed for one admissible class and one constraint architecture.
Admit a change of architecture as a move and it can fall:
[CASE-198](../cases.d/CASE-198.md) lowers it from 0.6 to 0.3.

## Three reserves

A names three: "Operational reserve", "Reconfiguration reserve",
"Competency reserve", which "can interact but need not be substitutable."
The synthesis gives only the names; the glosses are the filer's.

- **Operational reserve**: held while in a configuration, against
  disturbance and contingency. It is the useful slack of [TERM-107](TERM-107.md)
  that buffers shocks, and one input to readiness ([TERM-115](TERM-115.md)).
- **Reconfiguration reserve**: held for moving between configurations.
  This term.
- **Competency reserve**: the maintained ability to carry out a
  configuration's work at all, which decays without practice
  ([CLAIM-558](../claims.d/CLAIM-558.md)).

They need not be substitutable because they are different resources on
different timescales: A, "money cannot always be converted into the resource needed on the relevant timescale." A budget that covers an operational
reserve does not supply a skill, and a skill does not supply the peak
capacity a transition needs.

## Resource-constrained reconfiguration

A also proposed as a term "Resource-constrained reconfiguration: the
study of which changes in a system's organizational state or constraint
architecture remain reachable under specified resource, time, and
viability constraints." That names an inquiry, not a concept a claim is
stated in, so it is folded in here rather than filed. Its objects are the
bottleneck budget, the sets of sufficient budgets, and this slack.

## What it is not

- **Organizational slack in general** ([TERM-107](TERM-107.md)). This refines it: a
  reconfiguration reserve, measured against current output, is slack in
  that sense, and a useful one, but its use is a transition the output
  measure leaves out. An observer who reads it as waste and removes it
  forecloses the transition ([CASE-200](../cases.d/CASE-200.md)).
- **A unit of last resort** ([TERM-112](TERM-112.md)): an operational reserve held
  for congestion, not for a change of configuration.
- **Strain** ([TERM-060](TERM-060.md)): a cost of meeting demands that are jointly
  realizable. Reconfiguration slack is a cost on the path, not on the
  target, and lacking it makes a feasible target unreachable, not
  infeasible, so it is not frustration in [TERM-060](TERM-060.md)'s structural sense
  either.
- **The ratchet** ([TERM-110](TERM-110.md)): a rule by which a principal cuts what goes
  unspent. It is one way reconfiguration slack is lost, not the slack.

## What would settle it

A claim of the record's own stated in it that the owner adopts, or a
case outside constructions where the gap between a transition's peak and
its endpoints' requirements is measured. Adopting it is the owner's call.

## Note of 2026-11-05: A's resource models and further distinctions

[CASE-206](../cases.d/CASE-206.md) gives a geometric instance, a slack of about 0.99, and shows the slack depends on the declared resource: under crease energy instead of footprint it is 0. [TERM-105](TERM-105.md) sorts resources by type where this term's three reserves sort them by purpose, so one reserve can be of several types. No status changes.

## Note of 2026-11-06: what holds it back

Its uses do not yet share one sense: CLAIM-577 measures slack against the current configuration alone, B*(q, q′) − r(q), not against the costlier endpoint as defined here, and CLAIM-579's summary calls reconfiguration slack a field over configurations, which is where a reconfiguration reserve can be applied, not σ. The several-resource form, "the set of budgets that suffice, less what holding requires", is not yet defined, and no claim stated in the term has been adopted, its own settle condition.
