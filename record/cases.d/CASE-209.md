---
number: 209
status: Proposed
formerly:
- CASE-tmpnqvjs
title: 'A repertoire broader than simultaneous capacity: a rescue squad that can serve either of two distant incidents cannot serve both at once, and serves both in turn only when the second''s deadline leaves time for the first job and the travel between them'
version: 1
standing: fictional
kind: construction
tags:
- operations-research
- society-and-governance
- mathematics
date: '2026-11-05'
line:
- readiness
illustrates:
- CLAIM-347
- CLAIM-567
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4: A's table of
  tasks simultaneously feasible (D_A ∩ D_B ∩ Q ≠ ∅), each separately
  feasible, and sequentially achievable, with "There is an admissible,
  sufficiently timely path from a state in D_A to one in D_B" for the
  last. The times are the filer's: a 30-minute job at A, 40 minutes'
  travel to B, and B's deadline at 60 or 90 minutes. Simultaneous implies
  sequential, which implies separate; the squad is separately feasible at
  both deadlines, sequentially only at 90, simultaneously never. "Its
  repertoire is broader than its simultaneous service capacity." The
  construction is the filer's, from A's table of simultaneous, separate
  and sequential capability; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-211 TERM-113 — Proposed; A's proposals of 2026-11-04, a case filed beside this one, and a held term, cited as filed -->

# CASE-209: A repertoire broader than simultaneous capacity: a rescue squad that can serve either of two distant incidents cannot serve both at once, and serves both in turn only when the second's deadline leaves time for the first job and the travel between them

## The case

**A's three properties**, for two tasks with goal sets D_A and D_B in the
configuration space Q:

- **Simultaneously feasible**: D_A ∩ D_B ∩ Q ≠ ∅.
- **Separately feasible**: D_A ∩ Q ≠ ∅ and D_B ∩ Q ≠ ∅.
- **Sequentially achievable**: "There is an admissible, sufficiently
  timely path from a state in D_A to one in D_B".

**How they are ordered (the filer's).** Simultaneous implies sequential:
a state in D_A ∩ D_B is itself a path of length zero from D_A to D_B, and
it is timely. Sequential implies separate: a path from a state in D_A to
one in D_B shows both nonempty. Neither converse holds, as the case shows.

**The case (the filer's times).** One heavy rescue squad. Incident A
needs it for 30 minutes of extrication from the time it arrives; B is
40 minutes' travel from A. The squad reaches either from quarters within
that incident's own deadline. D_A is the set of states at A, rigged for A's
job, and D_B the set at B, rigged for B's job. A is dispatched first, and B's deadline is
counted from the same moment, the squad arriving at A at once for
simplicity.

- **Simultaneously**: no state is at A and at B. D_A ∩ D_B = ∅.
- **Separately**: yes, at either deadline.
- **Sequentially, B's deadline 60 minutes**: the job at A and the travel
  take 30 + 40 = 70 > 60. Not achievable.
- **Sequentially, B's deadline 90 minutes**: 70 ≤ 90. Achievable.

Checked by the filer.

## What it can show

- **That a repertoire is not a simultaneous capacity.** A: "A heavy
  rescue squad may be qualified to handle several incident types, but it
  cannot be present at two distant incidents simultaneously. Its
  repertoire is broader than its simultaneous service capacity." In
  [CLAIM-347](../claims.d/CLAIM-347.md)'s terms {A, B} is a
  non-face of the squad's complex, while A and B are each vertices.
- **That the sequential property is a reachability property with a
  clock.** It sits between the two others as [CLAIM-567](../claims.d/CLAIM-567.md)'s
  reachability sits between feasibility and reliability, and the
  deadline decides it, as in [CASE-211](CASE-211.md).
- **What a design should aim at.** A: "The engineering problem is not
  simply to maximize the number of tasks the squad can perform. It is to
  optimize the system's ability to select and switch among those tasks
  under uncertain demand." Adding incident types to the repertoire adds
  vertices; it does not add faces or shorten the paths between them.
  Whether a second call finds a unit free is [TERM-113](../terms.d/TERM-113.md)'s reliable
  coverage, which counts the busy squad as unavailable.

## What it cannot show

- **That real incidents have these times**, or that a job at A can be
  neither shortened nor handed over. A second squad, or mutual aid, is a
  change of the system, not of this squad's properties.
- **Anything about uncertain demand.** Both incidents are given; the
  value of switching under a distribution of calls needs a queueing
  model the case leaves out.

## Note of 2026-11-07: restated as a result to be shown, from "Individuation, Possibility, and Disposition"

<!-- inactive-ok-block: CASE-210 — Proposed; the constructions A restates -->
A50 §10 and A52 §10 restate as a result still to be shown for dispositions: "A collection of locally demonstrated capacities is not necessarily a jointly exercisable capacity." CASE-209 already constructs that repertoire broader than simultaneous capacity, and [CASE-210](CASE-210.md) the two departments matched in ordinary operation that split under a deadline-constrained demand. A cites neither. No change.
