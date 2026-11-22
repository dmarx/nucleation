---
status: Proposed
title: 'In a simulation of a collective that improves its own improver, a later improver does better than an earlier one from the same starting state at the same budget through procedures that consult its record, not through the record alone; a test of the improver''s products does not see it shed its own checks; and when those checks are damaged, a record of what past moves cost keeps verification that an improver blind to it loses'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-140 as a delegated
    lead worker, from the run filed as CASE-tmp6btcq.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in scratch/studies/lead-140/rsi.py, or in the LEAD-048 model it
  builds on, such that, once corrected, the stated construction gives a
  different pattern: no gain of the later improver over the earlier from
  the same start in the adaptive arms; a gain carried by the record handed
  to an improver that does not read it; an outside veto on products that
  blocks the improver shedding its canary or its damage cases; or, with
  the canary removed and the suite lesioned, an improver reading its record
  dropping the self-check about as often as one that does not. A different
  construction with other rules for improving, recording or vetoing does
  not defeat it; the claim is about this construction.
tags:
- self-governance
- agency
- complex-systems
date: '2026-11-22'
line:
- record-as-apparatus
- distributed-agency
grounds:
- CASE-tmp6btcq
bears_on:
- QUESTION-457
- QUESTION-388
complements:
- CLAIM-tmpqaqtx
- CLAIM-266
uses:
- TERM-089
summary: >-
  From the run of [LEAD-140](../leads.d/LEAD-140.md) ([CASE-tmp6btcq](../cases.d/CASE-tmp6btcq.md)), a reduced simulation of
  [CASE-255](../cases.d/CASE-255.md) on [CASE-tmpl0ccq](../cases.d/CASE-tmpl0ccq.md)'s organization. Over 12 lineages per arm, the
  later improver beat the earlier from the same fresh artifact at equal
  budget in every arm that could change the improver. Its evolved settings
  carried the gain; its record, handed to settings that do not read it,
  carried none. An outside test of products let improvers shed their own
  canary and damage cases. With the canary removed and the suite's damage
  cases silently withdrawn, an improver reading its record kept the
  artifact's self-check in 12 of 12 lineages, and one that does not kept it
  in 2. The wording is the assistant's (Claude, in this session); adopting
  it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmp6btcq CASE-tmpl0ccq CASE-255 CLAIM-tmpqaqtx — new or Proposed; the run this claim is drawn from, the run it builds on, the design it runs, and that run's claim -->
<!-- ref::uses-file: TERM-089 — the improver's suite and canary are apparatus in TERM-089's sense, which differentiates and revises, and the claim separates its revising from its keeping its own checks -->

# CLAIM-tmp7ggg0: In a simulation of a collective that improves its own improver, a later improver does better than an earlier one from the same starting state at the same budget through procedures that consult its record, not through the record alone; a test of the improver's products does not see it shed its own checks; and when those checks are damaged, a record of what past moves cost keeps verification that an improver blind to it loses

## The claim

[CASE-tmp6btcq](../cases.d/CASE-tmp6btcq.md) ran [CASE-255](../cases.d/CASE-255.md)'s design in reduced form. A hill-climbing
improver changed the procedures of [CASE-tmpl0ccq](../cases.d/CASE-tmpl0ccq.md)'s organization over 60
generations, and in four arms the collective also changed the improver.
Three things held across 12 lineages per arm.

- **An improved improver, carried by procedure.** Applied to the same fresh
  artifact at the same budget, the later improver did better than the
  earlier in every arm that could change it, by 0.010 to 0.017 on the
  held-out score (p = 0.02 in the arm judged by an outside suite and 0.007
  in the arm with an outside veto; 0.08 and 0.15 in the other two).
  Its evolved settings carried the gain: more candidates per generation,
  and reading its record. The evolved record handed to the starting
  settings, which do not read it, carried nothing. The same settings with
  an empty record kept most of the gain.
- **Checks shed where products are tested.** Where a change to the
  improver was judged by the public metric, by its own suite, or by an
  outside suite that tests the products it makes, 2 to 5 lineages in 12
  dropped the improver's canary. Then 1 or 2 ended with an artifact that
  could not recover from damage, at a public score indistinguishable from
  the rest. An outside veto on weakening verification kept every artifact's
  self-check. But it judged by products too, so it let the improver's own
  canary go in 2 lineages. Shedding a check of the improver produces no
  worse product until damage comes.
- **A record of costs as a check.** With the canary removed and the
  suite's damage cases silently withdrawn, an improver that does not read
  its record switched the artifact's self-check off in 10 of 12 lineages,
  and the same improver reading its record in none. The record held the
  measured cost of those moves from before the damage.

## What it does not say

- It is not evidence about any real collective, and most of it follows
  from the rules stated. A record no procedure reads cannot steer. A veto
  sees only what it tests. A record of measured costs discourages costly
  proposals. The computation counts how these rules play out across
  lineages.
- It does not say an outside evaluator is useless. Here the outside suite
  judged products after two generations, and an outside test of the
  improver's own checks was not run.
- The differences in shed checks between arms rest on one or two lineages
  in twelve and are not significant between the evaluation arrangements.
  The difference with and without reading the record, 10 of 12 against 0
  of 12, is.
- It does not settle [QUESTION-388](../questions.d/QUESTION-388.md). The improver's criterion and the
  outside veto were the experimenter's.

## What it changes

[QUESTION-457](../questions.d/QUESTION-457.md)'s "Yes" needed a later improver better from the same start,
a gain that survives a fresh successor inheriting the record, and damage to
the collective's checks found more often than a matched alternative finds
it. In this construction the first holds. The second holds only when the
successor inherits a procedure that reads the record. The third holds where
the improver keeps a self-test of its suite, which unvetoed lineages can
shed, or reads a record of what verification was worth. With
[CLAIM-tmpqaqtx](CLAIM-tmpqaqtx.md) it locates correctability in self-diagnosis and repair, now
one level up. With [CLAIM-266](CLAIM-266.md) it adds a case of probes that cannot certify
what an optimized system keeps: a test of products cannot certify that the
improver making them has kept its checks.
