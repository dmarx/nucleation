---
status: Open
title: 'Measure how much a distinction matters to the record by perturbation: change one entry, one relation or one rule in a frozen copy and diff the findings, as a dry-run impact report'
version: 1
stage: idea
priority: medium
method:
- empirical
- operationalization
tags:
- design-rationale
- software-engineering
date: '2026-11-26'
line:
- record-as-apparatus
advances:
- CLAIM-tmpxl7dc
- CLAIM-469
- CLAIM-664
summary: >-
  From A25 §§4, 11 and 12 of the exchange "Alignment consequences
  brainstorm" (ChatGPT, 2026-11-26): measure Δ_M(R, δ), the symmetric
  difference of findings, for single perturbations of a frozen copy of the
  record, and report it before a change is made, "a hypothetical `luria
  impact` operation". Part of it exists: retiring an entry already reports
  what rests on it and leaves each dependant to judgment ([CLAIM-664](../claims.d/CLAIM-664.md)). The
  wording is A's (ChatGPT, in the exchange of 2026-11-26); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpxl7dc ARG-tmpsis1z — Proposed; the claim this would test and its argument -->

# LEAD-tmpj44my: Measure how much a distinction matters to the record by perturbation: change one entry, one relation or one rule in a frozen copy and diff the findings, as a dry-run impact report

## What to do

1. Take the tree at one commit. Run `luria lint` and the reports once and
   keep the findings, F_M(R).
2. **Entry perturbations.** For a sample of entries, change the status (an
   Active claim to Rejected, a LIT to Unavailable), rerun, diff. Report
   for each the findings added and removed, the dependants named, and the
   time the run took.
3. **Relation perturbations.** Move a `grounds` entry to `corroborates`,
   drop a `rests_on`, add an `objects_to`; diff as above.
4. **Grammar perturbations.** Apply a candidate change to `luria.yaml` (a
   new `fail_on` check, a relation made required, a status split) to the
   unchanged tree; diff. Keep apart the two kinds [ARG-tmpsis1z](../arguments.d/ARG-tmpsis1z.md) separates:
   a rule that changes findings on perturbations already expressible, and
   one that makes new perturbations expressible.
5. **As a dry run.** For a proposed change in a pull request, print the
   same diff before it merges: findings added, dependants that need a
   judgment, references that need none. A25 §12's fictional report has
   this shape and says "Effects outside the represented dependency graph
   are unknown."

## What it would move

- [CLAIM-tmpxl7dc](../claims.d/CLAIM-tmpxl7dc.md): step 4 is its test. A grammar change whose diff is empty
  on R and non-empty on some δ is an instance; none found across the
  record's `fail_on` history would count against the claim's generality.
- [CLAIM-469](../claims.d/CLAIM-469.md): a measure of which distinctions the apparatus "keeps,
  enforces and propagates".
- [CLAIM-664](../claims.d/CLAIM-664.md): whether the dependants a retirement reports are the ones a
  reviser then changes.

## What it does not measure

Attention, decision and action, A25 §11's other three components. A's own
experiment table (A25 §13: equivalent bodies of knowledge under different
governing architectures) is [LEAD-155](LEAD-155.md)'s design, not this one's.
