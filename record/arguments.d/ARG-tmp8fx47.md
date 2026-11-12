---
status: Proposed
title: 'The graph that asserted an inference nobody made shows that preserving the old graph through a migration can preserve a false dependency'
version: 1
form: existence
grounds:
- CASE-131
concludes:
- CLAIM-tmpefs1h
tags:
- epistemology
- design-rationale
date: '2026-11-12'
line:
- records-of-inquiry
- record-as-apparatus
summary: >-
  From the exchange "luria experiment design" (2026-11-10), A25: "Preserving
  the original graph exactly would preserve the false dependency in
  CASE-131." The inference from CASE-131 to the negative half of
  CLAIM-tmpefs1h, that preserving the graph is not a criterion of a
  faithful migration. Proposed. CASE-131 is documented, and the relation
  was removed before merge, so the migration it supports is a stipulated
  counterfactual: had the forced relation been merged before ADR-044, a
  graph-preserving migration would have carried it. The case shows the
  negative half; the positive criterion rests on CLAIM-250, not on the
  case. The observation is A's (ChatGPT's); the wording is the
  assistant's (Claude, in this session), and adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmpefs1h — filed from the same exchange, Proposed; the claim this argument concludes -->
<!-- inactive-ok-file: CLAIM-250 — Proposed; cited for what each holds, not as settled -->

# ARG-tmp8fx47: The graph that asserted an inference nobody made shows that preserving the old graph through a migration can preserve a false dependency

## The inference

1. CASE-131: CLAIM-310 was filed with `supports: CLAIM-296` because it gave
   evidence for CLAIM-296. The link fixer wrote the converse, `rests_on`,
   onto CLAIM-296, which said CLAIM-296 could not stand without CLAIM-310.
   That was false: CLAIM-296 had been argued before CLAIM-310 existed.
   Under the grammar of the day, evidential support had no relation of its
   own, so the false dependency was the grammar's, not anyone's assertion.
2. Suppose the relation had been merged, and ADR-044's `corroborates` then
   introduced by a migration.
3. A migration that preserves the graph maps each old relation to its
   counterpart. `rests_on` has a counterpart, itself, so CLAIM-296 still
   rests on CLAIM-310 after the migration.
4. So a graph-preserving migration carries a dependency nobody asserted
   into the new grammar. Preserving the graph is not sufficient for a
   faithful migration, which is the negative half of CLAIM-tmpefs1h.

## Critical questions

- **Is the case an instance of the kind the conclusion is about?** Yes for
  the forced relation: CASE-131's own account is that the grammar forced
  the move, and the history shows the converse was written by the tool.
  No for the migration: in fact the relation was removed before merge, so
  step 2 is stipulated. The stipulation is coherent, since nothing about
  the grammar of the day prevented the merge.
- **Could a graph-preserving migration have been smarter?** A migration
  that recognized converses written by the tool and reassigned them would
  not be graph-preserving; it would be applying the claim's criterion,
  which separates written-by-the-tool from asserted.
- **Does one case support the positive criterion?** No. It shows one
  criterion fails. That the accountability structure is the right thing to
  keep rests on CLAIM-250, which is Proposed, and on the absence, so far,
  of a migration that kept it and still lost something the record needed.
