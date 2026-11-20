---
status: Draft
title: 'The batch of 2026-11-19 and 20: pull requests 541 to 545, parallel pull requests appending notes to the same entries'
version: 1
tags:
- record
- process
date: '2026-11-20'
reviews:
- ADR-068
- ADR-074
- ADR-108
- ADR-109
pull_requests:
- https://github.com/dmarx/nucleation/pull/541
- https://github.com/dmarx/nucleation/pull/542
- https://github.com/dmarx/nucleation/pull/543
- https://github.com/dmarx/nucleation/pull/544
- https://github.com/dmarx/nucleation/pull/545
discussions:
- https://claude.ai/code/session_01HcmtbsDR5i5G9oxErMDiB4
summary: >-
  Trigger 2 of [ADR-tmp714j2](../decisions.d/ADR-tmp714j2.md): five pull requests, one stacked on another
  and folded, merged on the owner's word. The costs were conflicts on
  dated notes appended to the same entries by parallel pull requests,
  twice on one of them; a branch that had to be remapped to concretized
  codes after main moved; a copy-lawfulness question the rule did not
  settle; and an inferred personal name nearly written into the record.
  What changes: a merge order for parallel pull requests, a question for
  the owner on how dated notes are filed, a wording question for [ADR-074](../decisions.d/ADR-074.md),
  and a rule against inferring names.
---
<!-- inactive-ok-file: ADR-tmp714j2 — Proposed or newly filed; the decisions this postmortem reviews -->

# POSTMORTEM-tmpe7ifr: The batch of 2026-11-19 and 20: pull requests 541 to 545, parallel pull requests appending notes to the same entries

## What happened

Five pull requests from one session: 541 (eight task-composition
readings), 542 (the backlog audit, 184 leads), 543 (the owner's
identifiability and localization claim), 544 (the owner's identity
projects, stacked on 543) and 545 (Kuhn). 541 had to merge main and remap
94 references to temporary codes once the earlier stack concretized. All
were green; the owner said to merge them. 544 was folded into 543, then
543, 541 and 542 merged cleanly; 545 conflicted twice.

## What it cost

1. **Notes appended to the same entries.** 541, 543 and 545 each appended a
dated note at the end of [CLAIM-754](../claims.d/CLAIM-754.md), [CLAIM-756](../claims.d/CLAIM-756.md), [CLAIM-758](../claims.d/CLAIM-758.md), [TERM-117](../terms.d/TERM-117.md) or
[TERM-131](../terms.d/TERM-131.md). Merged one after another, the last conflicted on five files;
after main concretized the earlier ones' codes, it conflicted again on
[TERM-117](../terms.d/TERM-117.md). Each was resolved by keeping both notes, and checked for
duplicates.
2. **Remapping after concretization.** A branch cut before a merge to main
carries the old temporary codes of entries main has since renumbered; 541
needed 94 replacements, done by script from the `formerly:` fields.
3. **A copy the rule did not settle.** The Structure of Scientific
Revolutions was read from a whole-book PDF in a course folder. [ADR-074](../decisions.d/ADR-074.md)
admits course copies of articles and excludes whole in-copyright books;
the filer asked rather than filed, and the owner ruled the copy lawful.
The ruling is recorded for that copy only.
4. **An inferred personal name.** In filing the owner's own projects, the
filer wrote a first name into two LIT citations that it had guessed, not
read. Caught before commit and replaced by the owner's GitHub handle.

## What changes

- Merge parallel pull requests one at a time, merging main into the next
before its merge, when they append to the same entries; or file dated
notes so that parallel additions do not collide. The second is a change to
how notes are filed, and is the owner's call.
- After a merge to main concretizes codes, merge main into every open branch
and remap by `formerly:` before further work on it.
- [ADR-074](../decisions.d/ADR-074.md): whether a whole book on a course page counts, generally, is open;
the owner's ruling covers one copy. A wording change would settle it.
- Never write a person's name that was inferred rather than read; cite by
what the source shows.
