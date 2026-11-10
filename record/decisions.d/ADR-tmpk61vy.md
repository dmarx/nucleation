---
status: Proposed
title: 'An entry carries every line whose argument it takes part in: a line it answers, refines, objects to or bears on through one of that line''s entries; resting on or using an entry of another line is a dependency across lines, not participation, and stays a reported crossing'
version: 2
history:
- version: 2
  date: '2026-11-10'
  note: >-
    At the owner's ruling on the record-wide sweep: the rule is applied
    until nothing changes. A line an entry gains counts for the entries
    that answer, refine, object to or bear on it, so the rule cascades.
    On the record of 2026-11-10 it converged after four rounds (56, 22,
    12 and 2 entries).
tags:
- record
date: '2026-11-10'
summary: >-
  `line` takes several values, and a line is "a named line of the record's
  own argument, so that a line can be set aside as a whole and what depends
  on it can be found" ([ADR-032](ADR-032.md)). Nothing said when an entry should carry a
  second line. [ADR-082](ADR-082.md) answered it for one case, the split of
  nucleating-argument: a moved entry keeps the old line when it answers,
  refines or objects to one of that line's entries. This decision makes the
  rule general and adds `bears_on`: an entry carries a line when it answers,
  refines, objects to or bears on one of that line's entries. Resting on
  or using one does not count; that is a dependency the `argument` chain
  reports as a crossing, which is what [ADR-032](ADR-032.md) meant it to do. Neither does
  `complements` alone. The demonstration gives the line to the eleven
  entries among the lint's 79 cross-line steps that bear on a question of
  the premise's line. The other 55 entries the rule reaches record-wide
  are listed for a follow-up sweep. Rejected: counting `complements`;
  counting `rests_on`; leaving it to judgement entry by entry.
---
<!-- inactive-ok-file: ADR-082 ADR-083 — Proposed; the split's decisions this generalizes -->

# ADR-tmpk61vy: An entry carries every line whose argument it takes part in: a line it answers, refines, objects to or bears on through one of that line's entries; resting on or using an entry of another line is a dependency across lines, not participation, and stays a reported crossing

## Context

A line is "a named line of the record's own argument, so that a line can be
set aside as a whole and what depends on it can be found" (the `lines`
vocabulary, [ADR-032](ADR-032.md)). Two things follow from that purpose:

- **Setting a line aside should take with it the entries that are part of
  its argument.** An entry that answers one of the line's questions, or
  objects to one of its claims, is part of that argument.
- **It should not take with it entries that only depend on the line.**
  Those are found through the dependency. The `argument` chain reports a
  `rests_on` step that crosses lines because "that is how a line set aside
  reaches back into one still standing".

The record had no rule for when an entry carries a second line. The lint
sweep of 2026-11-10 (dmarx/nucleation#446) found 79 `rests_on` steps
between claims that share no line. Most are what [ADR-032](ADR-032.md) meant to report:
a claim in one line resting on a claim in another. But some of the
dependent claims also argue inside the premise's line, so they are missing
a line.

[ADR-082](ADR-082.md) already gave the rule for one case, the split of
nucleating-argument. A moved entry keeps the old line when it answers,
refines or objects to one of that line's entries. It drops the old line
when it only rests on or uses one. The owner pointed out that `line` takes
several values. Carrying both is legitimate where it is apt.

## Decision

- **An entry carries a line when it takes part in that line's argument.**
  It does when one of these relations points at an entry of the line:
  - `answers`: it is an answer to one of the line's questions;
  - `refines`: it sharpens one of the line's questions;
  - `objects_to`: it is in one of the line's objection threads;
  - `bears_on`: it is evidence for or against one of the line's questions,
    or a premise of one.

  Its first line stays its first, and the added line goes after it.
- **It is applied until nothing changes (version 2).** A line an entry
  gains counts like any other, so an entry that refines, answers, objects
  to or bears on a newly lined entry gains the line too. The owner chose to
  follow this cascade to its end rather than stop after one step.
- **Dependency is not participation.** `rests_on`, `grounds` and `uses`
  pointing into another line make a dependency across lines. The `argument`
  chain reports it as a crossing, and it does not add a line.
- **`complements` alone does not add a line.** It says two entries answer
  different parts of one question, and that question's line is reached
  through `answers` or `bears_on` if the entry argues it. Counted on its own,
  `complements` would spread lines along chains of complementary claims that
  each sit in their own inquiry.
- **[ADR-082](ADR-082.md)'s rule is this rule applied to a split.** It is unchanged.
- **Demonstration ([ADR-071](ADR-071.md)).** The eleven entries among the lint's 79
  crossings that bear on a question of the premise's line now carry that
  line, each with a history note:
  - [CLAIM-532](../claims.d/CLAIM-532.md), [CLAIM-544](../claims.d/CLAIM-544.md), [CLAIM-553](../claims.d/CLAIM-553.md), [CLAIM-554](../claims.d/CLAIM-554.md), [CLAIM-613](../claims.d/CLAIM-613.md) and [CLAIM-619](../claims.d/CLAIM-619.md)
    (will-organization) gain distributed-agency;
  - [CLAIM-549](../claims.d/CLAIM-549.md) (will-organization, formal-apparatus) gains
    distributed-agency;
  - [CLAIM-586](../claims.d/CLAIM-586.md) (realizability, formal-apparatus) gains distributed-agency;
  - [CLAIM-621](../claims.d/CLAIM-621.md) (pragmatic-transport) gains distributed-agency;
  - [CLAIM-611](../claims.d/CLAIM-611.md) (distributed-agency, realizability) gains formal-apparatus;
  - [CLAIM-615](../claims.d/CLAIM-615.md) (distributed-agency) gains realizability.

  That clears twelve of the crossings. The 67 that remain are dependencies,
  reported as [ADR-032](ADR-032.md) intends.

## Alternatives considered

- **Count `complements` too.** 35 of the 79 dependents complement a claim
  of the premise's line. A complement relation joins claims across
  inquiries readily, and following it would give most of the record's
  claims most of its lines, which would empty "set a line aside" of
  meaning.
- **Count `rests_on`.** Then every crossing would vanish by definition, and
  the argument chain would no longer show how one line reaches into
  another, which is [ADR-032](ADR-032.md)'s reason for reporting it.
- **Judge each entry by reading it.** The relations already state the
  participation. A rule over them can be checked, and a reviewer can
  overrule an entry where a relation was filed loosely.

## Consequences

- **The rule reaches beyond the lint's crossings.** Applied across the
  record, it would add a line to 66 entries, through 51 `bears_on`,
  17 `refines`, 9 `objects_to` and 1 `answers` relations. The eleven here
  are its first application. The other 55 are a follow-up sweep, once the
  owner has seen the rule work.
- **Filing gets a check.** Whoever files an entry that answers, refines,
  objects to or bears on another line's entry adds that line. A pattern
  over these four relations could report a missing line mechanically.
- **A line's account ([ADR-083](ADR-083.md)) may now integrate these entries.** The
  accounts of the lines that gained entries are not changed here.
