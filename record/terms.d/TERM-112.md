---
number: 112
status: Proposed
formerly:
- TERM-tmpexd3x
title: 'unit of last resort: a response unit kept out of routine assignment and dispatched only when every regular unit is busy, so its record of use measures congestion, not its worth'
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    A dated note added at the thirtieth status review, after NOTE-1620 was
    read with its equations. The definition is unchanged.
- version: 3
  date: '2026-11-07'
  note: >-
    Provenance only: NOTE-1620 went to Read in the twenty-ninth and
    thirtieth status reviews, so "read Skimmed in" or "skimmed in"
    becomes "read in" (1 place). What the entry says is unchanged.
tags:
- operations-research
- agency
date: '2026-11-04'
line:
- readiness
summary: >-
  Filed at the owner's request on 2026-11-04, to account for a
  construction the readings of the pasted bibliography on emergency
  readiness surfaced and the record lacked. Its source is Larson and
  Odoni's Urban Operations Research, ch. 5 §5.4.1 ([LIT-2053](../literature.d/LIT-2053.md)), read as
  the neighbour standing in for Larson's hypercube paper ([LIT-2105](../literature.d/LIT-2105.md),
  Unavailable). The book gives it as a dispatch-order device and makes no
  claim about its value; that its use measures congestion and not its
  worth is the filer's reading of the construction. The wording is the
  filer's; adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-2105 — Unavailable; the paper the book stands in for, nothing here rests on it -->
<!-- inactive-ok-file: TERM-107 — Proposed; a term of the same filing, cited as filed -->

# TERM-112: unit of last resort: a response unit kept out of routine assignment and dispatched only when every regular unit is busy, so its record of use measures congestion, not its worth

## Definition

A **unit of last resort** is a response unit that a dispatch policy puts
last in every preference list, so that it is sent only when every regular
unit able to respond is busy. Larson and Odoni ([LIT-2053](../literature.d/LIT-2053.md), read in
[NOTE-1620](../notes.d/NOTE-1620.md); [THEORY-1394](../theory.d/THEORY-1394.md)), §5.4.1: "These units would not ordinarily be
used in the routine assignment of units to service requests; however,
they would be called upon during heavy workload conditions to avoid the
formation of (or reduce the probability of) queues." Their examples:
"sergeants' cars (police), mobile cardiac care units (emergency medical
services), social service supervisors (for nonscheduled home visits), or
other backup personnel". The hypercube model computes their workloads and
where they respond by giving them last preference.

The term's job is to name a capability whose use is a by-product of the
policy's ordering. How often such a unit is sent is the probability that
the regular units are all busy, times the demand then arriving. That
measures the congestion of the rest of the system. It does not measure
what the unit's response is worth when it is sent, and it falls as the
regular fleet grows or demand falls, whatever the value of the response
it gives on those rare occasions.

## Why it matters for readiness

A unit of last resort is the formal case of a capability whose
contribution shows only in saturation. Measured by
utilization, it looks idle by design; the less often it is needed, the
better the rest of the system is doing. So a rule that allocates by
observed use would cut it first, and at exactly the times it is needed
the cut would show. That inference is the filer's, not the book's.

## What it is not

- **Operational availability** ([TERM-055](TERM-055.md)): the chance a resource is
  deployed for a task by its deadline. A unit of last resort is a unit
  whose availability is high and whose use is low; the term names that
  role in a policy, not a probability.
- **A specialized unit.** Larson and Odoni treat matching a unit's
  capability to a neighbourhood's needs (bilingual or cardiac units)
  separately. A unit of last resort is defined by its place in the
  dispatch order, not by what it can do; a heavy rescue squad held for
  extrications is specialized, and is a unit of last resort only if it is
  also sent as general backup when the others are busy.
- **Slack** ([TERM-107](TERM-107.md), filed the same day): resources beyond what
  current output requires. A unit of last resort is a reserve whose
  output is small by design; whether it is useful or wasteful slack is
  the open question that term names.
- **Scenario-conditioned readiness** (A's term, [TERM-115](TERM-115.md)): a
  probability of effective response to an imposed contingency, which a
  unit of last resort raises in the saturation scenarios.

## What would settle it

A claim of the record's own stated in it, or a reading of Larson's 1974
paper confirming the construction there. Adopting it is the owner's call.

## Note of 2026-11-06: Larson and Odoni, read

[NOTE-1620](../notes.d/NOTE-1620.md) now reads §5.4 with its equations, and the quotations above
check. The model handles a unit of last resort only through its place in
the preference lists: its workload and response frequencies come out of
the same steady state as every other unit's, and nothing in §5.4 assigns
it, or any unit, a value. The definition and the filer's inference stand
as filed. No status changes.
