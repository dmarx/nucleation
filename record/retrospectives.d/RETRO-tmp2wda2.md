---
status: Draft
title: 'The owner''s rulings on the promotion pull request of 2026-11-21 and the hour after: one list of rulings became twelve pull requests, a promotion and a back-merge; what went right was ruling inline and choosing among filed alternatives, and what went wrong was the assistant reaching for a script or a memory where the tool already held the rule'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    The owner's responses, the same hour: a go for recommendations 1 and 5;
    2 and 3 too broad as worded; 4 to be elaborated. Recorded under "The
    owner's responses", with 2 and 3 restated narrower and 4 set out. The
    recommendations as first written are kept above.
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

# RETRO-tmp2wda2: The owner's rulings on the promotion pull request of 2026-11-21 and the hour after: one list of rulings became twelve pull requests, a promotion and a back-merge; what went right was ruling inline and choosing among filed alternatives, and what went wrong was the assistant reaching for a script or a memory where the tool already held the rule

## What it covers

From the owner's rulings on pull request 582 (about 08:45 UTC, 2026-11-21) to the promotion of that batch and the opening of 599 (about 10:00). In order:

- **The rulings.** The owner answered the description's list of choices waiting, with one indented bullet each. There were thirteen answers.
- **Twelve pull requests**, one per unit of work ([ADR-071](../decisions.d/ADR-071.md)):
  - corrections: the `anthology-candidate` finding (587) and [RETRO-004](RETRO-004.md)'s summary (588);
  - a lead for a human coder (591);
  - anchoring restated in general terms and taken into the P9 account (592);
  - decisions: the work renamed (589, [ADR-tmpwgvwk](../decisions.d/ADR-tmpwgvwk.md)), cross-line accounts with an audit for missing lines (593, [ADR-tmpg1n72](../decisions.d/ADR-tmpg1n72.md)), three alternatives on [ADR-075](../decisions.d/ADR-075.md)'s language (594), and a restart that keeps the dialectic's state (595, [ADR-127](../decisions.d/ADR-127.md) version 3);
  - the previous retrospective's responses (596);
  - the manuscript (597);
  - an analytics pipeline in Apache Hamilton (598).
- **The promotion.** At the owner's word ("merge 582 when it's ready … let's hold off on merging more stuff into staging until we've merged 582 into main first"), 582 went into main. The Docs run concretized the codes, and the back-merge brought staging level with main. The four open decision PRs were then brought up to date, three were merged, and the workflow opened 599 itself.

The devlog entries of 09:05:39 and 09:37:39, filed on pull request 594 as the work went, are read here. Neither is earmarked.

## What went well, and why

- **Ruling inline worked.** The owner answered every item where it stood, in the description the items were already in. Each answer could be quoted exactly in the entry it changed. None was lost or misread. Two answers were questions ("don't we get this for free via git blame or git log?"), and those were answered and the recommendation withdrawn.
- **Alternatives let the owner choose cheaply.** The [ADR-075](../decisions.d/ADR-075.md) question went to the owner as three filed decisions with a table and a stated lean. The owner chose with "sure, go with A". The chosen one's skill wording was applied within minutes, and the others were kept as Rejected, not deleted.
- **One unit, one pull request, held under load.** Twelve units in an hour were filed on twelve branches. Each could be merged or held on its own, which is what let the owner hold four for review while the rest merged.
- **The delegated pipeline checked itself against the record.** A background agent built the analytics pipeline while the assistant filed the rest. Its tests reproduce the manuscript's figures exactly at the commits the manuscript read. It made the census's staleness visible as numbers: 13 decisions not yet coded, and 34 coded decisions whose status has changed since.
- **The owner's questions found the errors.** "the flag didn't change meaning" withdrew a census finding. "is this not something luria can already do for us?" found that a script duplicated `luria repair`. Both are in the next section.
- **The promotion workflow opened its own pull request** (599), the first time since the setting that blocked it was reported.

## What did not go well

- **A finding rested on one reader's classification.** The census's term audit classed [ADR-048](../decisions.d/ADR-048.md)'s rewording of the `anthology-candidate` blurb as a redefinition in place. [CLAIM-791](../claims.d/CLAIM-791.md), the manuscript's abstract and its results then made that its one instance of a change of meaning left untraced. The classification was the assistant's alone: the census's second coder checked the decisions, not the term events. The owner ruled that the flag had not changed meaning. The finding was withdrawn (587). That left the claim's distinctive half without a case, and the manuscript's E3 exception untested.
- **A code in a title failed docs-check a fourth time** (devlog, 09:05:39). Three alternative decisions were titled "Alternative A to [ADR-075](../decisions.d/ADR-075.md)'s step 5". The assistant's own retrospective, filed an hour earlier, had named the hazard. luria 1.11.0, already released, refuses such a title in `luria new`. The record still pins 1.10.0.
- **A script did what luria already does, and did it wrong** (devlog, 09:37:39). After the promotion the assistant wrote a script to swap the concretized codes into the four open branches. The script also rewrote the `formerly:` fields that must keep the old codes, in 24 entries on one branch. Three branches were pushed before the assistant noticed. The commits were reverted, and the rewrite was redone correctly. But none of it was needed. `luria repair`, which every pull request's docs-check runs, makes exactly that rewrite and skips `formerly:`. Old spellings also resolve through `formerly:` in the meantime. This is [ADR-054](../decisions.d/ADR-054.md)'s lesson again: a mechanical change CI already makes should not be made by hand.
- **An unchecked command result.** The first attempt to revert used `git revert -q`, which git rejected. The output was suppressed, and the assistant reported the next step before checking the log, which showed the revert had not happened. The second attempt checked.
- **A shared description was overwritten.** Another session rewrote 582's description at 08:08 and dropped the list of choices waiting. The assistant restored it. The owner's later rulings were written into the restored list.
- **The next step after the hold was not said.** When the hold on merging into staging lifted, the assistant reported what was waiting but not what it would do next. The owner had to ask: "you gonna open a new PR on staging or what?"

## Recommendations

1. **Bump the pinned luria to 1.11.0**, in the docs workflow and wherever sessions install it, so that a code in a title is refused when written. This is a CI change, for the owner.
2. **Check the tool before scripting a mechanical change to the record.** Read `luria --help` and the list of repairs in `luria repair --help` first. After a promotion, do nothing to open branches: their next docs-check repairs them.
3. **Have a second reader check any classification a finding rests on**, or put it to the owner. That applies to the term audit's kinds of change as much as to the census's decisions.
4. **Append to a shared description; do not rewrite it.** Where a workflow writes the description, as the Promotion PR workflow now does, check after each push that additions survive.
5. **When a hold lifts, say the next step and take it** in the same turn.

## The owner's responses, 2026-11-21

1. **Bump luria to 1.11.0.** "go". Done in pull request 601. All nine pins move. Diffing the two wheels shows the only other change is a commented-out template note.
2. **Check the tool before scripting.** "2 should be narrower than any mechanical change, should reflect on whether it's reasonable that the luria CLI might be able to handle the thing first." Restated: before writing a script that changes the record's files, ask whether the change is the kind the luria CLI exists to make, such as rewriting codes, linking references, completing relations, scaffolding entries, or migrating a field. If it plausibly is, read the relevant `luria … --help` first. A one-off edit of content, or a change luria has no reason to know about, needs no such check.
3. **A second reader for classifications.** The owner's skepticism "might be just a response to the word 'any'". Restated: when a finding turns on an interpretive classification, and one reader made it, have that classification checked before the finding is filed, by a second reader or by the owner. An interpretive classification here means one like whether a term's meaning changed, or whether a change was a revision. Classifications read off a field, a count or a diff need no second reader.
4. **Shared PR descriptions.** To be elaborated; see the next section.
5. **When a hold lifts, say the next step and take it.** "go". Filed as a convention in its own pull request.

## Shared PR descriptions, elaborated

**The failure.** The promotion pull request's description was edited by three writers. The workflow wrote it on opening. The assistant in this session added the choices waiting on the owner. Another session, tending the same pull request, rewrote it at 08:08 to fix its account of the batch. GitHub keeps one body and the last write wins. The other session read the description, rebuilt it from what it knew, and wrote it back. The list of choices, which it had not written, was dropped without anyone deciding to drop it. Nothing failed loudly. The assistant found the loss only because it re-read the description before its own next edit.

**What is not the problem.** The workflow. `promotion-pr.sh` writes the body once, when it opens the pull request, and never again, so additions made after that survive its later runs. Recommendation 4's second half, to check after each push that a workflow-written body keeps additions, is withdrawn.

**The proposal: sections with owners, and a check before writing.**

- **Sections.** A shared description is divided into sections, each opened by a marker naming what it holds, such as `<!-- section: batch -->` and `<!-- section: choices -->`. Each writer edits only the sections it is responsible for and copies the others through byte for byte. The batch table is kept by whoever merges into staging. The choices are kept by whoever adds them. The owner's inline rulings live inside the choices section and are never removed by anyone but the owner.
- **Read, then write, then check.** Read the body and its `updated_at` immediately before writing. Write only if `updated_at` is unchanged. Otherwise read again and merge the change into the newer body. After writing, read the body back once to confirm.
- **Additions, not reconstructions.** A writer who finds the body wrong corrects the line that is wrong, and does not regenerate the body from its own picture of the batch.

**Alternatives considered.**

- **Choices as comments, not in the description.** Comments are append-only, so nothing is lost. But the owner's inline rulings worked because each answer sat under its question in one place. Comments scatter that.
- **A file on staging holding the choices**, regenerated into the description. It is durable and reviewable, but heavier than the problem, and a file merged into main then needs clearing.
- **One writer only.** All edits go through the session that opened the description. That is simple, but it does not fit a record where several sessions merge into staging in one night.

**Lean:** sections with owners plus the read-then-write check. It keeps the owner's way of ruling, and costs one extra read per edit. If the owner agrees, it would be filed as a short convention, with this pull request description as its first application.

## What it does not say

- Not that twelve pull requests in an hour was too many. Each was one unit, and the owner reviewed them at their own pace. What strained was the reporting around them, not their number.
- Not that the three corrected errors were caught by procedure. Two were caught by the owner's questions and one by the assistant reading a file. No check would have caught them.
