---
status: Proposed
title: 'Time for peak capacity: two cells that each need one unit of power for one minute need a peak of 2 under a one-minute deadline and a peak of 1 under a two-minute one, unless a coupling between them forbids folding one before the other'
version: 1
standing: fictional
kind: construction
tags:
- operations-research
- mathematics
date: '2026-11-05'
line:
- readiness
illustrates:
- CLAIM-296
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4: "two origami
  cells must each be actuated once. Each actuation requires one unit of
  power capacity for one minute." Folded together they need a peak of 2
  for one minute; in turn, a peak of 1 for two. The numbers are A's; the
  general count ⌈n/T⌉ and the coupled variant, in which the sequential
  schedule is not admissible and the peak stays 2 at any deadline, are
  the filer's. The energy is 2 unit-minutes throughout, so the
  requirement that changes with the deadline is the peak, and only where
  the constraints permit another schedule. The construction is the
  filer's, from A's time-for-peak example; adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmpbi4ca CASE-tmpoo2tj TERM-tmp26wo4 — Proposed; A's proposals of 2026-11-04 and the entries filed beside them, cited as filed -->

# CASE-tmpqk2kd: Time for peak capacity: two cells that each need one unit of power for one minute need a peak of 2 under a one-minute deadline and a peak of 1 under a two-minute one, unless a coupling between them forbids folding one before the other

## The case

**A's example.** A: "two origami cells must each be actuated once. Each
actuation requires one unit of power capacity for one minute."

- **Simultaneous**: both fold in the first minute. Peak 2, done in one
  minute.
- **Sequential**: one folds, then the other. Peak 1, done in two.

A: "If the deadline is one minute, the system needs the higher peak
capacity. If the deadline is two minutes, the system can accomplish the
same transformation with half the peak capacity."

**The general count (the filer's).** With n cells, each needing one unit
for one uninterrupted minute, and a deadline of T whole minutes, the
least peak is ⌈n/T⌉: at most P cells fold in each minute, so n ≤ PT. For
n = 2 it is 2 at T = 1 and 1 at T ≥ 2. The energy, 2 unit-minutes, is the
same under every schedule.

**The coupled variant (the filer's).** Suppose the two cells' folds are
linked, so that folding one while the other stays flat violates a loop
constraint and is not an admissible configuration. Then the sequential
schedule passes through an inadmissible state, only the simultaneous one
remains, and the peak is 2 at every deadline. A: "A lack of resources may
sometimes be compensated for by a longer reconfiguration horizon, but
only when the system's constraints permit an alternative schedule."

## What it can show

- **That peak capacity and cumulative expenditure are different
  constraints.** The same 2 unit-minutes can need a peak of 2 or of 1.
  A budget on energy does not fix the transition's feasibility; a cap on
  peak power together with a deadline does. These are two of the
  resource types of [TERM-tmp26wo4](../terms.d/TERM-tmp26wo4.md), and [CLAIM-tmpbi4ca](../claims.d/CLAIM-tmpbi4ca.md)'s bottleneck
  budget is the peak, at an unconstrained horizon.
- **That the deadline is part of the requirement.** What a system can do
  within a deadline is [CLAIM-296](../claims.d/CLAIM-296.md)'s relation among resource, task and
  deadline: here the same task, with the same resource, is feasible at
  T = 2 and not at T = 1 with one unit of peak.
- **That the substitution is a property of the constraints.** Whether
  time can stand in for peak capacity is decided by whether a sequential
  schedule is admissible, not by the resource. Kang, Kim, Yang and Ryu
  ([NOTE-tmpxbvec](../notes.d/NOTE-tmpxbvec.md)) design sequential deployment into a Kresling stack by
  ordering its cells' energy barriers: "each layer folds in a
  predetermined order dictated by its barrier height."
- **A's organizational reading.** "The heavy rescue squad's value isn't
  simply that technical rescue can eventually be performed. It's that the
  capability can be mobilized within a deadline." [CASE-tmpoo2tj](CASE-tmpoo2tj.md) is the
  record's case of a deadline-constrained extrication.

## What it cannot show

- **Anything about real actuators**, whose power and duration trade
  continuously and not in whole units and minutes.
- **That longer horizons are free.** A two-minute schedule is a minute
  longer; where the deadline is the contingency's, not the
  organization's, the organization does not choose it.
