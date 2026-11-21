---
status: Draft
title: 'The session of 2026-11-20 and 21: from an entry''s life cycle to transformer depth in six stacked pull requests and a round of sixteen readings; what went right was the record as memory, the owner''s challenges and reading after filing; what went wrong was claims stated before the record was searched, and a red check left unlooked-at'
version: 1
tags:
- record
- process
date: '2026-11-21'
reviews:
- ADR-068
- ADR-071
- ADR-108
- ADR-114
pull_requests:
- https://github.com/dmarx/nucleation/pull/558
- https://github.com/dmarx/nucleation/pull/559
- https://github.com/dmarx/nucleation/pull/560
- https://github.com/dmarx/nucleation/pull/561
- https://github.com/dmarx/nucleation/pull/562
- https://github.com/dmarx/nucleation/pull/563
discussions:
- https://claude.ai/code/session_01Hcmtbu5GVkUyn672wCPeC7
summary: >-
  The first retrospective under the RETRO scheme, asked for by the owner on
  2026-11-21 ("A lot of stuff seems to be clicking right now, and we should
  document what seems to be going right"). It reads the three devlog entries
  of 2026-11-21. Going right: the record held most formal pieces, the
  owner's challenges improved two claims, delegated readers corrected three
  and confirmed others. Going wrong: six results stated before the record or
  a triviality check would have caught them, a docs-check failure unseen
  across five stacked pull requests, reader branches the proxy would not
  delete. Five recommendations, none yet a decision.
---
<!-- inactive-ok-file: CLAIM-635 — Proposed; cited as open -->
<!-- inactive-ok-file: ADR-068 ADR-108 ADR-114 CLAIM-478 POSTMORTEM-tmpynplw — Proposed or newly filed; the decisions reviewed and the entries filed beside this -->

# RETRO-tmp50h9d: The session of 2026-11-20 and 21: from an entry's life cycle to transformer depth in six stacked pull requests and a round of sixteen readings; what went right was the record as memory, the owner's challenges and reading after filing; what went wrong was claims stated before the record was searched, and a red check left unlooked-at

## What it covers

One working session of the owner with the assistant, 2026-11-20 into 2026-11-21.
The owner asked a run of connected questions: how narrowing degrees of freedom
by constraint relates to an entry's life cycle; how that stabilization relates
to the record's account of contraction; whether they are one phenomenon; then
drift, hierarchy and hyperbolicity, μP and depth scaling, and what transformer
depth organizes. Each was answered in chat, then filed at the owner's word, one
unit per pull request ([ADR-071](../decisions.d/ADR-071.md)), stacked because each cited the last's codes:
pull requests 558 to 562. The owner then asked to read everything identified as
due; sixteen readers read fourteen works and four neighbours, filed as pull
request 563 ([ADR-068](../decisions.d/ADR-068.md), [ADR-108](../decisions.d/ADR-108.md), [ADR-114](../decisions.d/ADR-114.md)).

Notes taken for this review: the devlog entries of 2026-11-21, 00:31:48 (reading
after filing), 00:31:49 (the record as memory and the owner's challenges) and
00:31:51 (the wrong theories and the red check). They were written at the end of
the session, not during it; from now on they are written as the work goes.

## What went well, and why

1. **The record did its job as memory.** Every question's formal core was
   partly held already: [CLAIM-635](../claims.d/CLAIM-635.md), [THEORY-960](../theory.d/THEORY-960.md), [CLAIM-581](../claims.d/CLAIM-581.md), Saxe's and
   Schoenholz's readings, and Freidlin–Wentzell once found. New results were
   joins between held entries. Why: the record's closed vocabularies and
   relations made the search cheap. Keep: search before answering, every time.
2. **The owner's challenges were the best edits.** "Isn't stabilization just
   monotone contraction?" and "rate differences" rather than "scale separation"
   each turned a weaker claim into a stronger one, and the second led to
   finding an error. Why: the assistant answered in chat first and filed only on
   the owner's word, so challenges landed before filing. Keep: answer, let the
   owner push, then file.
3. **Filing with recollections marked, then reading.** Claims that leaned on
   unread works said so in their text and named the reading in their defeaters.
   The readings then confirmed two recollections and corrected three framings,
   each correction going straight into a new version. Why: the marking made the
   claims' dependence on the reading explicit and checkable. Keep.
4. **Parallel readers with a recheck clause.** Sixteen readers in about four
   minutes, each returning a verdict on the record's characterization and a
   search of the record with what the reading surfaced. The rechecks found held
   entries the assistant had missed or denied. Keep the clause in the brief.
5. **Checking by simulation before asserting.** Twelve short scripts, each
   kept in its curation entry. One check caught a misreading before the owner
   built on it.

## What did not go well

1. **Six results stated before the record or a triviality check would have
   caught them.** Listed in the devlog entry of 00:31:51: a result offered as new
   that [CLAIM-635](../claims.d/CLAIM-635.md) held; a mechanism split the owner had to merge; a misread
   statistic; a hyperbolicity bound true of every chain; a "not held" that was
   held; a theory cited for more than it says. All were caught before merging,
   but only one by the assistant's own check.
2. **A red check unlooked-at.** Pull request 558 failed docs-check on a code in a
   title, and five pull requests were stacked on it before CI was read. See the
   postmortem filed beside this ([POSTMORTEM-tmpynplw](../postmortems.d/POSTMORTEM-tmpynplw.md)).
3. **Pace against review.** Six pull requests in a day, stacked six deep, with
   hundreds of new entries in the last. The owner cannot review at that pace,
   and a stack that deep turns one fix into six merges (the title fix had to be
   merged forward through every branch, with one conflict).
4. **Housekeeping the environment would not allow.** Sixteen reader branches
   could not be deleted (HTTP 403), against [ADR-108](../decisions.d/ADR-108.md).
5. **A manuscript out of step.** [CLAIM-478](../claims.d/CLAIM-478.md) took a new version, and its
   manuscript (cost-structure-of-possibility, §2.2) still states the old
   wording. Nothing tells a work's owner when a member claim changes.

## Recommendations

None is yet a decision; each would be filed as one, named here in `prompted`.

1. **Search before novelty, and a triviality check before a bound.** Before
   calling a formal result new, search the record for its objects; before
   stating a bound as content, ask whether it holds of every instance.
   Candidate for the read-and-file skill's step 12.
2. **Read CI after every push, and before stacking.** No pull request is based
   on another whose docs-check has not passed. Candidate for CLAUDE.md's
   working section.
3. **A cap on stack depth.** Two or three, after which the batch waits for
   review or merges. For the owner to set.
4. **Reader notes without remote branches** where the environment cannot delete
   them: keep the notes in the scratchpad and commit them only if the reading
   is abandoned. A revision of [ADR-108](../decisions.d/ADR-108.md).
5. **A notice when a work member changes.** When a claim in a `works` vocabulary
   takes a new version, the filing's curation entry names the work and the
   section to revise. Small; could be a line in the read-and-file skill.

## What it does not say

Nothing about whether the session's claims are right; that is their statuses'
business. It reviews how the work went.
