---
number: 5
status: Draft
formerly:
- RETRO-tmp0p4qy
title: 'The night of 2026-11-21 after the first retrospective: staging and its first promotion, the dialectic regime and the conventions it grew, a local reading of First Contact and an adoption review that adopted 34 decisions; what went right was fitting the tooling to the work and the owner steering by interjection, and what went wrong was a few errors of the assistant''s that the regime let travel further before the owner caught them'
version: 1
tags:
- record
- process
date: '2026-11-21'
reviews:
- ADR-116
- ADR-127
- ADR-121
- ADR-125
- ADR-124
- ADR-126
- ADR-120
- ADR-108
pull_requests:
- https://github.com/dmarx/nucleation/pull/564
- https://github.com/dmarx/nucleation/pull/565
- https://github.com/dmarx/nucleation/pull/566
- https://github.com/dmarx/nucleation/pull/567
- https://github.com/dmarx/nucleation/pull/568
- https://github.com/dmarx/nucleation/pull/569
- https://github.com/dmarx/nucleation/pull/570
- https://github.com/dmarx/nucleation/pull/571
- https://github.com/dmarx/nucleation/pull/572
- https://github.com/dmarx/nucleation/pull/573
- https://github.com/dmarx/nucleation/pull/574
- https://github.com/dmarx/nucleation/pull/575
- https://github.com/dmarx/nucleation/pull/576
- https://github.com/dmarx/nucleation/pull/577
- https://github.com/dmarx/nucleation/pull/578
- https://github.com/dmarx/nucleation/pull/579
- https://github.com/dmarx/nucleation/pull/580
- https://github.com/dmarx/luria/pull/402
- https://github.com/dmarx/luria/pull/403
discussions:
- https://claude.ai/code/session_01Hcmtbu5GVkUyn672wCPeC7
summary: >-
  The owner asked for a retrospective ("retro") at the end of the night of
  2026-11-21, after [RETRO-001](RETRO-001.md) earlier the same night. It reads the four
  devlog entries filed since (034912, earmarked by the owner; 042208;
  065344; and the night's pull requests), answers the earmark as
  [ADR-126](../decisions.d/ADR-126.md) requires, and follows up [RETRO-001](RETRO-001.md)'s five recommendations.
  Going right: staging removed stacking, the dialectic regime removed the
  permission handoff while the owner kept steering by interjection, the
  local reading of First Contact found what the anthology's did not, and a
  hazard that caught the assistant three times was removed upstream. Going
  wrong: errors of the assistant's own, including a self-correction that was
  itself wrong, that the regime filed fast and the owner had to catch; a
  ruling by ticked box missed; and the nightly Promote still bypassing the
  review point built for it. Six recommendations, none yet a decision.
---
<!-- inactive-ok-file: ADR-116 ADR-127 ADR-124 ADR-120 ADR-108 — Proposed or Active since tonight; the decisions this reviews -->

# RETRO-005: The night of 2026-11-21 after the first retrospective: staging and its first promotion, the dialectic regime and the conventions it grew, a local reading of First Contact and an adoption review that adopted 34 decisions; what went right was fitting the tooling to the work and the owner steering by interjection, and what went wrong was a few errors of the assistant's that the regime let travel further before the owner caught them

## What it covers

From [RETRO-001](RETRO-001.md) (about 00:30 UTC) to about 07:00 UTC on 2026-11-21: pull
requests 564 to 580 in this record and 402 and 403 in luria. In order:

- **Tooling.** The RETRO scheme (564); staging and the Promote workflow
  (565); the first promotion, by hand (566), which found that the back-merge
  ran only after a Promote run (567, [ADR-116](../decisions.d/ADR-116.md) version 2); the promotion pull
  request kept open by a workflow (577, [ADR-125](../decisions.d/ADR-125.md)); the nightly Promote
  moved to 03:45 Pacific (580).
- **The argument.** Predicates as constraints and stabilization in the
  control-theoretic sense (568); engineering as a form of inquiry (572);
  First Contact related to the account of learning occasioned by
  obstruction, then read locally (575).
- **Conventions.** Reframings in an entry's own prose (569, [ADR-120](../decisions.d/ADR-120.md));
  the dialectic regime (570, [ADR-127](../decisions.d/ADR-127.md)) and what it grew: several
  readings filed as alternatives, a go-ahead covering the whole message and
  adopting the stated lean, reporting every filing, raising doubts in the
  manner of crew resource management; the merge grant (573, [ADR-121](../decisions.d/ADR-121.md));
  earmarks (571, [ADR-126](../decisions.d/ADR-126.md)); the owner's rulings (578).
- **Upstream.** The hands-free regime as a luria decision (402); `luria new`
  refusing a title that cites a code (403).
- **Review.** The adoption review (579, [ADR-124](../decisions.d/ADR-124.md)), whose first pass
  adopted 34 decisions and left [ADR-108](../decisions.d/ADR-108.md) Proposed.

## What went well, and why

1. **Fitting the tooling to the work.** The owner's framing, after [CLAIM-541](../claims.d/CLAIM-541.md)
   on wu wei: stacks of pull requests were fighting how the work was done.
   Staging ended them: from 567 onward nothing was stacked, eleven pull
   requests merged into staging in an hour, and the batch checked clean
   together on [#576](https://github.com/dmarx/nucleation/issues/576). Keep: when a workaround recurs, change the tooling.
2. **The owner steered by interjection, not permission.** Once the regime
   was on, filings and merges went ahead with a report each turn, and the
   owner's turns went to the argument and to corrections: the pinned value
   is a descriptor; stabilization is the control-theoretic sense;
   "separable" had three readings; a go-ahead adopts the lean. Each
   correction became a revision before merge or a rule. Keep: the per-turn
   report and the one-commit-per-turn revert.
3. **Asking for several readings made ambiguity productive.** The owner's
   rule to file all valid readings turned one ambiguous word into three
   alternative decisions the owner could choose among (571), and a choice
   among two for the merge grant and the promotion pull request. The
   rejected readings stay on the record.
4. **A local reading paid.** The anthology's reading of First Contact served
   the anthology's purpose. Read in this record's context it found four
   things more, two of which corrected claims filed an hour earlier: the
   failing assistant was a prior study's, and the domain the score did not
   predict was a second assisted lander. Keep: when a held reading is used
   for a different question, read again.
5. **A hazard was removed upstream.** A code in a title failed docs-check
   on an argument earlier in the night and on a decision tonight, and was
   caught once more before a push. luria's own principle, that a guard that
   keeps catching you is a bug report about the workflow, led to luria#403:
   `luria new` now refuses such a title.
6. **Building found what review missed.** The first promotion showed the
   back-merge gap that the reviewed specification allowed ([CASE-299](../cases.d/CASE-299.md)),
   which became both a fix and an argument (engineering as inquiry).

## What did not go well

1. **A self-correction that was wrong.** In chat the assistant said a pinned
   value puts a feature in the conserved part; filing, it reversed this to
   "enforcing a pinned value erases where the entry started" and filed the
   reversal. The first statement was right; the owner caught it. The regime
   filed the reversal as fast as anything else, and a reversal of one's own
   statement is where a check pays most.
2. **A temporary code cited across pull requests.** Alternative decisions
   in [#571](https://github.com/dmarx/nucleation/issues/571) cited the regime decision's temporary code while it was in [#570](https://github.com/dmarx/nucleation/issues/570),
   and [#571](https://github.com/dmarx/nucleation/issues/571) went red. The rule (cut from staging once the cited unit has
   merged) was in CLAUDE.md; writing several related units quickly broke it.
3. **Reporting had to be asked for.** The owner asked what was being filed,
   and whether engineering as inquiry had already been discussed. That
   became the rule that every filing turn ends with a Filed block.
4. **A ruling missed.** The owner ruled by ticking two groups on [#579](https://github.com/dmarx/nucleation/issues/579)'s
   checklist. Editing a description sends no event, and the assistant read
   only the comment, then asked again (devlog note 065344).
5. **The review point can still be bypassed.** [#576](https://github.com/dmarx/nucleation/issues/576) waits for the owner,
   and the Promote run on main's old schedule, 10:37 UTC, would merge
   staging without that review. The move to 03:45 Pacific does not take
   effect until it reaches main.
6. **Reader branches still cannot be deleted** on the remote, as [RETRO-001](RETRO-001.md)
   found; one more tonight. The owner left [ADR-108](../decisions.d/ADR-108.md) Proposed, on the fence.
7. **A template cited a code** a fresh record cannot resolve (luria#402),
   caught by its tests.

## The earmarked note

**034912, earmarked by the owner on [#570](https://github.com/dmarx/nucleation/issues/570):** "this class of items should
probably have a referent so we can extend it later … a good example of
noticing a distinction." What came of it: a practice kept on purpose.
[ADR-127](../decisions.d/ADR-127.md) names the class (the argument schemes) rather than listing
schemes, and the move recurred twice that night, in the descriptor and
imposition distinction and in the tag-vocabulary case, where a closed list
turns descriptions into impositions. Still open: no sweep has looked for
other decisions that enumerate where they mean a class (recommendation 6).

## [RETRO-001](RETRO-001.md)'s recommendations, followed up

1. **Search before novelty** was followed: both the engineering and the
   First Contact filings searched the record first and cited what it held.
2. **Read CI before stacking** is moot under staging; its cousin, citing
   another unit's temporary code, recurred (above, 2).
3. **A cap on stack depth** is answered by staging, which removed stacks.
4. **Reader notes without remote branches** was not acted on; [ADR-108](../decisions.d/ADR-108.md) stays
   Proposed.
5. **A notice when a work member changes** was not acted on.

## Recommendations

None is yet a decision; each would be filed as one.

1. **Flag a self-reversal.** When the assistant reverses something it said,
   the report says so, as a CRM item, before or with the filing.
2. **Keep alternatives that cite each other in one pull request**, or cut
   the second from staging after the first merges.
3. **Read every channel a ruling can come by**: comments, review states and
   the description's checklist. Done for the adoption review; generalize to
   any pull request that offers the owner a checklist.
4. **Close the bypass.** Merge [#576](https://github.com/dmarx/nucleation/issues/576) before 10:37 UTC, or switch the schedule
   off for tonight; and decide whether the nightly Promote should merge
   without review at all now that a review point exists. For the owner.
5. **Revise [ADR-108](../decisions.d/ADR-108.md)**: reader notes in the scratchpad, or a branch deleted by
   the owner in batches. For the owner, who is on the fence.
6. **A sweep for enumerations that mean a class**, the earmark's follow-up:
   decisions and skills that list schemes, fields or kinds where a named
   class would extend.

## What it does not say

- Not that the regime is settled. It ran for a few hours; the errors above
  came in that time.
- Not how often building finds what review misses: one case.
