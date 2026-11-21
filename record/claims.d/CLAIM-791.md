---
number: 791
status: Proposed
formerly:
- CLAIM-tmpj5aiv
title: 'In this record a change to a vocabulary term was always announced by a decision, and was carried through the entries using the term whenever entries had to move, by removal or split; the audit found no term whose meaning changed in place, so it does not test whether entries follow a change of meaning alone'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Corrected at the owner's ruling on the promotion pull request, 582:
    "the flag didn't change meaning, visiting these is the responsibility
    of processes on the anthology to consider if they want to add these
    candidates or not. pretty sure no action is required on Nucleation's
    end." Version 1 read ADR-048's rewording of the anthology-candidate
    blurb as a redefinition in place that reached none of its 237 entries.
    The flag has always recorded that someone judged the anthology may
    want the work (ADR-005). ADR-048 changed what that implies about
    filing here, not what the flag records, and acting on a flag is the
    anthology's process. So nothing needed to be carried through, and the
    audit has no instance of a redefinition in place. Version 1's
    distinctive half, that entries do not follow where only a meaning
    changes, loses its case and is withdrawn. Version 1's title: "In this
    record a change to a vocabulary term was always announced by a
    decision, and was carried through the entries using the term whenever
    entries had to move, by removal or split, but not when only the term's
    meaning changed: the redefinition of anthology-candidate reached none
    of its 237 entries, so the record traces its grammar's changes where
    entries move and not where only a meaning does".
role: thesis
warrant: empirical
defeated_if: >-
  An event in the audited history in which a term change required
  entries to move, by removal or split, and the entries were not changed
  in the same unit of work; or a term change made with no decision record
  in its unit. Entries left untouched by a widening or a restatement do
  not defeat it, since the word still holds what it held.
tags:
- design-rationale
- philosophy-of-science
date: '2026-11-20'
line:
- record-as-apparatus
- records-of-inquiry
grounds:
- CASE-300
summary: >-
  A finding of the term audit in [CASE-300](../cases.d/CASE-300.md), filed at the owner's
  direction from the manuscript on the record. It measures [CLAIM-189](CLAIM-189.md)'s
  traceability, and [CLAIM-666](CLAIM-666.md)'s criterion for a faithful migration, against
  the record's own grammar. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-189 CLAIM-666 — Proposed; cited in this filing of 2026-11-20 -->

# CLAIM-791: In this record a change to a vocabulary term was always announced by a decision, and was carried through the entries using the term whenever entries had to move, by removal or split; the audit found no term whose meaning changed in place, so it does not test whether entries follow a change of meaning alone

## The claim

The term audit ([CASE-300](../cases.d/CASE-300.md)) found 34 events in the record's history: 25 declarations reworded and 9 terms removed. Every event came with a decision record in its unit of work. What happened to the entries carrying each term depended on the kind of change:

- **Removal.** Every entry carrying a removed term in use was changed in the same unit: `identity` 41 of 41, `self-and-personhood` 42 of 42, and the four SYNTHESIS terms [ADR-084](../decisions.d/ADR-084.md) removed.
- **Split.** The entries that moved were changed: `Deferred` 177 of 345, `ecology` 13 of 50, and the split lines.
- **Widening or restatement.** Almost nothing was touched, and nothing needed to be, because the word still holds what it held: `learning-theory` 1 of 92, and `anthology-candidate` 0 of 237. [ADR-048](../decisions.d/ADR-048.md) reworded the flag's blurb when it dropped the boundary of [ADR-001](../decisions.d/ADR-001.md). The flag still records what [ADR-005](../decisions.d/ADR-005.md) made it record, that someone judged the anthology may want the work; what changed is what that implies about the work's filing here. Whether to act on a flag is the anthology's process, not this record's.
- **Redefinition in place.** The audit found none.

## Why it matters

[CLAIM-189](CLAIM-189.md) (Proposed) holds that what a record can secure is traceability: change that is announced and located. For the record's own grammar, every change was announced, and where entries had to move, it was located in them.

[CLAIM-666](CLAIM-666.md) (Proposed) holds that a migration is faithful when it preserves the accountability structure. By that criterion the audited migrations were faithful where entries moved.

## What it does not say

- **That the record carries through a change of meaning alone.** No such change is in the audited history, so the claim says nothing about it. The predicted failure at that point (the manuscript's stage 5) is untested here.
- **That touching an entry means re-reading it.** The audit counts entries changed in the same unit, a proxy for re-reading.

## Reframings

**2026-11-21, the owner on pull request 582.** "the flag didn't change meaning, visiting these is the responsibility of processes on the anthology to consider if they want to add these candidates or not." Before: `anthology-candidate` was the claim's instance of a redefinition in place left untraced. After: it is a restatement that needed no carry-through, and the claim's second half is withdrawn for want of a case.
