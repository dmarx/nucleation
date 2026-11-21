---
status: Draft
title: 'The owner''s rulings on the promotion pull request of 2026-11-21 and the hour after: one list of rulings became twelve pull requests, a promotion and a back-merge; what went right was ruling inline and choosing among filed alternatives, and what went wrong was the assistant reaching for a script or a memory where the tool already held the rule'
version: 1
tags:
- record
- process
date: '2026-11-21'
reviews:
- ADR-054
- ADR-071
- ADR-116
- ADR-121
- ADR-125
- ADR-127
- ADR-tmpg1n72
- ADR-tmpwgvwk
pull_requests:
- https://github.com/dmarx/nucleation/pull/582
- https://github.com/dmarx/nucleation/pull/587
- https://github.com/dmarx/nucleation/pull/588
- https://github.com/dmarx/nucleation/pull/589
- https://github.com/dmarx/nucleation/pull/591
- https://github.com/dmarx/nucleation/pull/592
- https://github.com/dmarx/nucleation/pull/593
- https://github.com/dmarx/nucleation/pull/594
- https://github.com/dmarx/nucleation/pull/595
- https://github.com/dmarx/nucleation/pull/596
- https://github.com/dmarx/nucleation/pull/597
- https://github.com/dmarx/nucleation/pull/598
- https://github.com/dmarx/nucleation/pull/599
discussions:
- https://claude.ai/code/session_01HcmtbsHCnWAcGaecC7H4Pn
summary: >-
  The owner asked for a retrospective ("file a retro while we wait on CI")
  while CI ran on pull request 594. It covers about 08:45 to 10:00 UTC on
  2026-11-21. The owner answered every open choice on the promotion pull
  request, 582, as indented bullets in its description. The assistant turned
  the answers into twelve pull requests, one per unit of work. The owner then
  merged the promotion, the back-merge landed, and a new promotion pull
  request, 599, was opened by the workflow for the first time. Going right:
  ruling inline was fast and complete; filed alternatives let the owner
  choose in four words; a delegated pipeline reproduced the manuscript's
  figures and made the census's staleness visible; the owner's questions
  found two of the assistant's errors. Going wrong: a census finding that
  rested on one reader's classification; a code in a title failing CI a
  fourth time when the tool that prevents it was already released; and a
  hand-written rewrite of codes, unneeded because luria repair does it,
  that also corrupted `formerly:` before it was reverted. Five
  recommendations, none yet a decision.
---
<!-- inactive-ok-file: ADR-127 ADR-116 ADR-tmpg1n72 ADR-tmpwgvwk — Proposed; decisions this reviews -->

# RETRO-tmp2wda2: The owner's rulings on the promotion pull request of 2026-11-21 and the hour after: one list of rulings became twelve pull requests, a promotion and a back-merge; what went right was ruling inline and choosing among filed alternatives, and what went wrong was the assistant reaching for a script or a memory where the tool already held the rule

## What it covers

From the owner's rulings on pull request 582 (about 08:45 UTC, 2026-11-21) to the promotion of that batch and the opening of 599 (about 10:00). In order:

- **The rulings.** The owner answered the description's list of choices waiting, with one indented bullet each. There were thirteen answers.
- **Twelve pull requests**, one per unit of work (ADR-071):
  - corrections: the `anthology-candidate` finding (587) and RETRO-004's summary (588);
  - a lead for a human coder (591);
  - anchoring restated in general terms and taken into the P9 account (592);
  - decisions: the work renamed (589, ADR-tmpwgvwk), cross-line accounts with an audit for missing lines (593, ADR-tmpg1n72), three alternatives on ADR-075's language (594), and a restart that keeps the dialectic's state (595, ADR-127 version 3);
  - the previous retrospective's responses (596);
  - the manuscript (597);
  - an analytics pipeline in Apache Hamilton (598).
- **The promotion.** At the owner's word ("merge 582 when it's ready … let's hold off on merging more stuff into staging until we've merged 582 into main first"), 582 went into main. The Docs run concretized the codes, and the back-merge brought staging level with main. The four open decision PRs were then brought up to date, three were merged, and the workflow opened 599 itself.

The devlog entries of 09:05:39 and 09:37:39, filed on pull request 594 as the work went, are read here. Neither is earmarked.

## What went well, and why

- **Ruling inline worked.** The owner answered every item where it stood, in the description the items were already in. Each answer could be quoted exactly in the entry it changed. None was lost or misread. Two answers were questions ("don't we get this for free via git blame or git log?"), and those were answered and the recommendation withdrawn.
- **Alternatives let the owner choose cheaply.** The ADR-075 question went to the owner as three filed decisions with a table and a stated lean. The owner chose with "sure, go with A". The chosen one's skill wording was applied within minutes, and the others were kept as Rejected, not deleted.
- **One unit, one pull request, held under load.** Twelve units in an hour were filed on twelve branches. Each could be merged or held on its own, which is what let the owner hold four for review while the rest merged.
- **The delegated pipeline checked itself against the record.** A background agent built the analytics pipeline while the assistant filed the rest. Its tests reproduce the manuscript's figures exactly at the commits the manuscript read. It made the census's staleness visible as numbers: 13 decisions not yet coded, and 34 coded decisions whose status has changed since.
- **The owner's questions found the errors.** "the flag didn't change meaning" withdrew a census finding. "is this not something luria can already do for us?" found that a script duplicated `luria repair`. Both are in the next section.
- **The promotion workflow opened its own pull request** (599), the first time since the setting that blocked it was reported.

## What did not go well

- **A finding rested on one reader's classification.** The census's term audit classed ADR-048's rewording of the `anthology-candidate` blurb as a redefinition in place. CLAIM-tmpj5aiv, the manuscript's abstract and its results then made that its one instance of a change of meaning left untraced. The classification was the assistant's alone: the census's second coder checked the decisions, not the term events. The owner ruled that the flag had not changed meaning. The finding was withdrawn (587). That left the claim's distinctive half without a case, and the manuscript's E3 exception untested.
- **A code in a title failed docs-check a fourth time** (devlog, 09:05:39). Three alternative decisions were titled "Alternative A to ADR-075's step 5". The assistant's own retrospective, filed an hour earlier, had named the hazard. luria 1.11.0, already released, refuses such a title in `luria new`. The record still pins 1.10.0.
- **A script did what luria already does, and did it wrong** (devlog, 09:37:39). After the promotion the assistant wrote a script to swap the concretized codes into the four open branches. The script also rewrote the `formerly:` fields that must keep the old codes, in 24 entries on one branch. Three branches were pushed before the assistant noticed. The commits were reverted, and the rewrite was redone correctly. But none of it was needed. `luria repair`, which every pull request's docs-check runs, makes exactly that rewrite and skips `formerly:`. Old spellings also resolve through `formerly:` in the meantime. This is ADR-054's lesson again: a mechanical change CI already makes should not be made by hand.
- **An unchecked command result.** The first attempt to revert used `git revert -q`, which git rejected. The output was suppressed, and the assistant reported the next step before checking the log, which showed the revert had not happened. The second attempt checked.
- **A shared description was overwritten.** Another session rewrote 582's description at 08:08 and dropped the list of choices waiting. The assistant restored it. The owner's later rulings were written into the restored list.
- **The next step after the hold was not said.** When the hold on merging into staging lifted, the assistant reported what was waiting but not what it would do next. The owner had to ask: "you gonna open a new PR on staging or what?"

## Recommendations

1. **Bump the pinned luria to 1.11.0**, in the docs workflow and wherever sessions install it, so that a code in a title is refused when written. This is a CI change, for the owner.
2. **Check the tool before scripting a mechanical change to the record.** Read `luria --help` and the list of repairs in `luria repair --help` first. After a promotion, do nothing to open branches: their next docs-check repairs them.
3. **Have a second reader check any classification a finding rests on**, or put it to the owner. That applies to the term audit's kinds of change as much as to the census's decisions.
4. **Append to a shared description; do not rewrite it.** Where a workflow writes the description, as the Promotion PR workflow now does, check after each push that additions survive.
5. **When a hold lifts, say the next step and take it** in the same turn.

## What it does not say

- Not that twelve pull requests in an hour was too many. Each was one unit, and the owner reviewed them at their own pace. What strained was the reporting around them, not their number.
- Not that the three corrected errors were caught by procedure. Two were caught by the owner's questions and one by the assistant reading a file. No check would have caught them.
