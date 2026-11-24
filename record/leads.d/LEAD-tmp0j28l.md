---
status: Open
title: 'Review for promotion the Proposed entries the record functionally treats as held, found from executed studies that reproduce, demonstrated claims whose premises are held, terms in settled use and entries that Active entries and manuscripts rely on, with reliance as a reason to review and never as warrant'
version: 1
stage: specified
priority: high
method:
- formal
- operationalization
tags:
- philosophy-of-science
- epistemology
date: '2026-11-24'
line:
- record-as-apparatus
advances:
- CLAIM-1099
- CLAIM-1093
- CLAIM-1180
- CLAIM-878
- CLAIM-921
- CLAIM-1115
- CLAIM-1190
- CLAIM-1000
- CLAIM-1202
- CLAIM-1185
- CLAIM-1095
- CLAIM-892
- TERM-165
- TERM-163
summary: >-
  The owner's proposal at U33 of the exchange "Memes, Contracts, and
  Systemic Normativity" (2026-11-24), quoting A51 ("Their status is not a
  reason to overlook the Active and demonstrated claims they integrate"):
  "we can probably also use this as an exercise to identify content on the
  record that is still in a proposed state but which the record
  functionally treats as Active and should probably be promoted." It is
  the owner's ADR-124 move of 2026-11-21 ("promote some ADRs that are
  functionally already adopted") carried from decisions to the argument,
  where a status is credence and not adoption, so reliance can start a
  review and cannot settle one. A53's candidate clusters, checked, are its
  first worklist; A53's discovery signals are its operationalization. The
  proposal is the owner's; the worklist, the checks and the signals' fit
  to the status-review worklist are the assistant's (Claude, in this
  session); adopting either is the owner's call.
---

<!-- inactive-ok-file: ADR-124 CLAIM-1000 CLAIM-1093 CLAIM-1099 CLAIM-1115 CLAIM-1190 CLAIM-478 CLAIM-892 TERM-165 CASE-163 CASE-164 CASE-315 CASE-326 CASE-343 CASE-346 CASE-397 CASE-401 CASE-412 CLAIM-1024 CLAIM-1156 CLAIM-891 SYNTHESIS-106 SYNTHESIS-111 SYNTHESIS-124 — Proposed; the candidates and the decision this lead extends, cited whatever their standing -->

# LEAD-tmp0j28l: Review for promotion the Proposed entries the record functionally treats as held, found from executed studies that reproduce, demonstrated claims whose premises are held, terms in settled use and entries that Active entries and manuscripts rely on, with reliance as a reason to review and never as warrant

## The proposal

The owner, at U33, on A51's remark that the syntheses' Proposed status "is
not a reason to overlook the Active and demonstrated claims they
integrate": "we can probably also use this as an exercise to identify
content on the record that is still in a proposed state but which the
record functionally treats as Active and should probably be promoted."

## What already covers part of it

- **Decisions**: ADR-124 and the adoption-review skill, at the owner's
  2026-11-21 "we're probably overdue to promote some ADRs that are
  functionally already adopted". It covers ADRs only, and its test, a
  decision in force, is adoption. U33 is the same move for claims, cases
  and terms, where a status is credence (ADR-059) and the test is ADR-057's.
- **Claims**: ADR-057's status review and its worklist
  (`record/status-review/worklist.py`). Run on this branch on 2026-11-24 it
  lists 178 claims "Ready for a ruling", CLAIM-1099, CLAIM-1115 and
  CLAIM-1190 among them, and ranks 484 Proposed entries by reach, the
  highest relied on by 21 entries (CLAIM-478). So A53's figure from
  ADR-057, that by 2026-10-30 "the largest measured reliance on a Proposed
  entry had fallen to one", is a month stale: reliance has grown back, and
  the ready group has not been worked since.

## What it adds

The worklist reads typed relations among claims. It does not read four
signals A53 §7 lists, each of which this filing found candidates by:

1. **An executed-study CASE that reproduces.** The status-review README
   (§2) promotes a CASE when it is demonstrated, as CASE-396 and
   CASE-390 were on a rerun. Five Proposed executed studies were rerun on
   2026-11-24 and reproduce exactly (CASE-315, CASE-326, CASE-343, CASE-346,
   CASE-401); two more were reproduced by the manuscript's fact-check
   (CASE-412, CASE-397).
2. **A TERM in settled use**: TERM-165 is the sole blocker of two claims.
3. **Manuscript membership** (the `works` field) and citation in the body
   of Active entries (CLAIM-577 and CLAIM-679 discuss CLAIM-1099), the
   evidence ADR-124's script reads for decisions as `inactive-ok`
   directives.
4. **A SYNTHESIS used as its scope's account.** None of the record's 125
   syntheses is Current; setting one Current is the owner's review of its
   map (ADR-084), not a ruling on its components.

## The caution

A53: "functional reliance should trigger a review, not automatically
establish warrant", or promotion by use would be the self-certification
the record's own CLAIM-1064 and CASE-397 model. Each candidate goes
through ADR-057's four criteria; reliance only puts it on the list. And a
mismatch can be fixed other than by promotion: narrowing a title, writing
a concession, moving a ground to `corroborated_by`, or a blocker note.

## The first worklist

The checked table of A53's 35 candidates, and one it missed (CASE-346), is
in the curation entry of 2026-11-24 20:56, section "U32 to U33". In
short: ten promotable now (seven executed studies whose runs reproduce,
CLAIM-1099 with its concession on CLAIM-1093 written, CLAIM-1000 and
CLAIM-892 with their studies); twelve after a stated fix (a narrowed
title, a concession, an independent re-derivation, a re-read of stored
results); three syntheses for the owner's map review; eleven kept, each
for a reason its own entry states.

## What would count

Done when a status-review pass has ruled on the worklist, each entry
promoted, narrowed or kept with a blocker note, and the discovery signals
either join the worklist script or are judged not worth it. Whether they
join it is a change to ADR-057's procedure, and waits on the owner.
