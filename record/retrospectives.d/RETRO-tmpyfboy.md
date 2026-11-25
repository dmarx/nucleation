---
status: Draft
title: "The governance-of-becoming stretch, 2026-11-24 to 2026-11-25: an exchange filed, a manuscript series drafted, reviewed, refreshed and rewritten, and two recomputation passes; what went right was independent review, joins testing, fact-checking and reruns by readers who did no drafting, each of which found real errors, and what went wrong was a search for work already done that missed held results three times, joins filed as notes before they were tested, drafts written as audits of the record rather than as manuscripts, and steps held for the owner that the owner did not mean to hold"
tags:
- record
date: '2026-11-25'
reviews:
- ADR-068
- ADR-075
- ADR-104
- ADR-121
- ADR-127
- ADR-139
- ADR-143
- ADR-tmpenzcn
- ADR-tmpw306d
pull_requests:
- https://github.com/dmarx/nucleation/pull/787
- https://github.com/dmarx/nucleation/pull/788
- https://github.com/dmarx/nucleation/pull/791
- https://github.com/dmarx/nucleation/pull/792
- https://github.com/dmarx/nucleation/pull/793
- https://github.com/dmarx/nucleation/pull/794
- https://github.com/dmarx/nucleation/pull/796
- https://github.com/dmarx/nucleation/pull/797
- https://github.com/dmarx/nucleation/pull/798
- https://github.com/dmarx/nucleation/pull/799
- https://github.com/dmarx/nucleation/pull/803
- https://github.com/dmarx/nucleation/pull/804
- https://github.com/dmarx/nucleation/pull/808
- https://github.com/dmarx/nucleation/pull/810
- https://github.com/dmarx/nucleation/pull/812
- https://github.com/dmarx/nucleation/pull/813
- https://github.com/dmarx/nucleation/pull/814
discussions:
- https://claude.ai/code/session_01Hcmtbr5ERpRT8U5QiG9535
summary: >-
  At the owner's request ("retro while we wait on CI"), on 2026-11-25.
  The stretch began with a pasted share of the exchange "Memes, Contracts,
  and Systemic Normativity" on 2026-11-24 and ran under the dialectic
  regime: the exchange filed by nine parallel filers; the work
  governance-of-becoming registered; a series of articles drafted in three
  Parts, each reviewed, joins-tested and fact-checked by readers who had
  not drafted; Part I refreshed to A51's order; an audit of what was left
  out; two passes of reruns by a second session, promoting eleven
  entries and freeing four more under the owner's delegation; and, at the
  owner's ruling of [ADR-tmpw306d](../decisions.d/ADR-tmpw306d.md), the whole series rewritten as a
  manuscript. Going well: every independent pass found real errors, and
  saved progress let workers stopped by usage limits resume. Going
  wrong: the search for held work missed results three times, the fix
  moving each time; joins were filed as notes before their test; the
  drafts became audits of the record; and the assistant held for the
  owner steps the owner meant to delegate. Six recommendations follow.
  The review is the assistant's (Claude, in this session); adopting them
  is the owner's call.
---

# RETRO-tmpyfboy: The governance-of-becoming stretch, 2026-11-24 to 2026-11-25: an exchange filed, a manuscript series drafted, reviewed, refreshed and rewritten, and two recomputation passes; what went right was independent review, joins testing, fact-checking and reruns by readers who did no drafting, each of which found real errors, and what went wrong was a search for work already done that missed held results three times, joins filed as notes before they were tested, drafts written as audits of the record rather than as manuscripts, and steps held for the owner that the owner did not mean to hold

## What it covers

From the owner's paste of the exchange "Memes, Contracts, and Systemic
Normativity" (2026-11-24) to the rewrite of the series under [ADR-tmpw306d](../decisions.d/ADR-tmpw306d.md)
(2026-11-25), in one session under the dialectic regime ([ADR-127](../decisions.d/ADR-127.md)). The
pull requests are listed above; the devlog notes it reads are those of
2026-11-24 20:19, 20:58 and 22:29 and of 2026-11-25 03:30, 07:20 and
07:25. The note of 07:46 belongs to another session's stretch (the
atlas) and is not reviewed here, though its lesson, that procedure is
filed as decision and not as inquiry, bears on this one.

The work, in order: the exchange filed ([#787](https://github.com/dmarx/nucleation/issues/787), [#792](https://github.com/dmarx/nucleation/issues/792)), with a manuscript
recovered from hidden turns and an account of it; a back-merge repaired
([#788](https://github.com/dmarx/nucleation/issues/788)); the work governance-of-becoming registered ([ADR-tmpenzcn](../decisions.d/ADR-tmpenzcn.md)); Part I
drafted, reviewed and revised ([#791](https://github.com/dmarx/nucleation/issues/791), [#793](https://github.com/dmarx/nucleation/issues/793)); a status pass at the owner's
word ([#794](https://github.com/dmarx/nucleation/issues/794)) and reruns ([#797](https://github.com/dmarx/nucleation/issues/797)); Part II drafted, reviewed and revised
([#796](https://github.com/dmarx/nucleation/issues/796), [#798](https://github.com/dmarx/nucleation/issues/798), [#799](https://github.com/dmarx/nucleation/issues/799)); Part III drafted and reviewed ([#803](https://github.com/dmarx/nucleation/issues/803), [#808](https://github.com/dmarx/nucleation/issues/808)); Part I
refreshed to A51's order, with Article 2 folded and refreshed ([#804](https://github.com/dmarx/nucleation/issues/804)); an
audit of what was left out and its filings ([#804](https://github.com/dmarx/nucleation/issues/804)); a skill change ([#810](https://github.com/dmarx/nucleation/issues/810));
the series rewritten as a manuscript ([#812](https://github.com/dmarx/nucleation/issues/812)); and a recomputation pass
with its promotions ([#813](https://github.com/dmarx/nucleation/issues/813), [#814](https://github.com/dmarx/nucleation/issues/814)).

## What went well, and why

- **Independent readers found real errors every time.** The check of the
  exchange's account found 9 of 43 sampled links wrong; Part I's
  fact-check made 38 fixes; Part II's found 17, the refresh's 14, the
  rewrite's 23; the left-out audit sorted 98 items and found 17 manuscript
  fixes and 24 record filings. None changed an argument, and each would
  have shipped. The pattern worth keeping: a reader who did not draft,
  given the text and the record and no account of how the drafting went
  (write-manuscript step 7).
- **The joins test was honest.** Of 19 joins in Part III one passed, and of
  17 in Part II one passed in a corrected form. The low rate is the test
  working: most joins were restatements or failed, and none failed was
  asserted afterward. One join reader rechecked a computation from the
  claim's stated model rather than the script, which served as the
  second-session check the claim needed ([CLAIM-tmp6nzs1](../claims.d/CLAIM-tmp6nzs1.md)).
- **Reruns by a second session paid for themselves.** Two passes reran
  about thirty entries. Most reproduced, so eleven were promoted under the
  owner's delegation and [CLAIM-1114](../claims.d/CLAIM-1114.md)'s promotion freed four more ([#814](https://github.com/dmarx/nucleation/issues/814)).
  The ones that did not reproduce in full were the point: three studies
  each misstate a sentence ([CASE-365](../cases.d/CASE-365.md), [CASE-367](../cases.d/CASE-367.md), [CASE-347](../cases.d/CASE-347.md)), and one
  derivation fails at a step ([CLAIM-tmp9ia3w](../claims.d/CLAIM-tmp9ia3w.md)).
- **Parallel work in files of its own.** One worker per article or per
  group of turns, in one checkout or a worktree ([ADR-139](../decisions.d/ADR-139.md)), each listing the
  files it touched, kept conflicts to appended notes, which kept both
  sides. Merging each pull request on green kept staging moving ([ADR-121](../decisions.d/ADR-121.md)).
- **Owner corrections were absorbed in place.** A51's order ("my bad
  let's do a51"), "don't be shy" for Article 2, the hands-free reading of
  the regime (devlog 07:20) and [ADR-tmpw306d](../decisions.d/ADR-tmpw306d.md) each changed the plan within
  the hour, and each change was recorded where the next reader looks.
- **Saved progress survived usage limits.** Workers stopped three times
  by the limit, and once by a worker restart, resumed from their files.

## What did not go well

- **The search for work already done missed held results three times.**
  Part I's audit of A49 searched filed leads, not executed studies
  (devlog 22:29). Part II's digests searched by the article's words
  (03:30). Part III's digests searched by mechanism, as told, and still
  missed the hidden-subsidy runs, the seed-withdrawal assemblies, a study
  of real organizations and the rival literatures read (07:25). Each fix
  named a cause, and the cause was wrong twice. The third diagnosis is that
  a digester searches from what it expects the article to need, and the
  region searchers of the review, with no draft to defend, found what the
  digesters missed. The cost: three drafts told studies "not done" that
  were done, and three rounds of corrections.
- **Joins were filed as notes before their test.** Part III's drafts'
  joins went onto their components as dated notes, then to the [ADR-075](../decisions.d/ADR-075.md)
  reader, who found the question "does an entry state it?" circular and
  two of the notes wrong ([CLAIM-tmphq6hp](../claims.d/CLAIM-tmphq6hp.md), [CLAIM-741](../claims.d/CLAIM-741.md)). The notes had to be
  corrected in place.
- **The drafts became audits of the record.** The write-manuscript skill
  asked each step to cite its entry "with its standing", and each review's
  corrections added more of the same: who made an entry Active, voices by
  turn, Limits sections, step-3a tables in the text. By Part III a reader
  outside the record would have met the record's bookkeeping in every
  paragraph. The owner ruled ([ADR-tmpw306d](../decisions.d/ADR-tmpw306d.md)) that a manuscript argues for
  its reader, and eight articles were rewritten. The apparatus survived in
  files of its own, so nothing checked was lost; but the form should have
  been noticed earlier, since each review was in effect asking for more
  apparatus and no one asked who the text was for.
- **The exchange's synthesis became a ledger and a dumping ground.**
  [SYNTHESIS-tmp4tvbr](../syntheses.d/SYNTHESIS-tmp4tvbr.md) retold the exchange and then took every join verdict
  of three Parts, and parallel branches appending to it conflicted twice.
  [ADR-tmpw306d](../decisions.d/ADR-tmpw306d.md) retires exchange syntheses; the verdicts belong in the
  syntheses of the lines the joins advance.
- **The assistant held steps the owner meant to delegate.** It asked for
  go-aheads on reruns, revision plans and a skill change that the regime,
  as the owner reads it, already allowed (devlog 07:20). Each ask cost a
  round trip.
- **A choice was put in codes the owner could not read.** "keep A49's
  order; continue with Part II" was given to a question that named A49 and
  A51 without saying what they were, and the owner then asked "what did i
  just greenlight?". Nothing was built on the mistaken choice, but only
  because the owner asked.
- **Counts were copied from summaries.** The review's "19 joins" (there
  were 17) passed into an account and a README before a fact-check counted
  the table.
- **Fan-out was heavy.** About sixty delegated workers ran over the
  stretch. Most earned their cost, but several briefs were written after
  the workers they governed had started, and two workers edited a file
  another was still writing.

## Recommendations

1. **Search for held work as its own job, before drafting, by readers who
   are not drafting, region by region.** Done in [#810](https://github.com/dmarx/nucleation/issues/810) (write-manuscript
   step 3a). Its first application is the next Part to be drafted.
2. **File a join only after its [ADR-075](../decisions.d/ADR-075.md) verdict.** Done in [#810](https://github.com/dmarx/nucleation/issues/810) (step 6).
3. **Write the manuscript for its reader from the first draft.** [ADR-tmpw306d](../decisions.d/ADR-tmpw306d.md)
   and [#812](https://github.com/dmarx/nucleation/issues/812) do this. The write-manuscript skill could add that each article
   has an apparatus file from the start, so reviews have somewhere to put
   what they find other than the argument.
4. **Narrow the dialectic regime's list of held steps to the owner's
   reading** (devlog 07:20): merges into main, outside services, status
   changes on the owner's own entries, and anything hard to undo. A
   revision of [ADR-127](../decisions.d/ADR-127.md) is the place; that is the owner's to adopt. The
   owner added a rule on 2026-11-25, when the assistant left an owner's
   question Open beside its now-Active answer: "if you think it's
   legitimately answered, mark it answered. whether or not a question has
   been satisfactorily answered shouldn't be a matter of opinion". A
   status that follows from the record by a stated rule (a question with
   Active answers to each part is Answered, [ADR-049](../decisions.d/ADR-049.md)) is applied, whoever
   filed the entry; what waits is a judgement only the owner can make.
5. **Put every choice in words the owner can act on without the record
   open:** what each option means and what it changes, before any code.
6. **Make a skipped back-merge visible** (devlog 20:19). Whether
   `back-merge` should still wait on `docs-lint` is a CI choice for the
   owner; at least the skip should raise a notice where the promotion is
   watched.

## What it does not say

That the manuscript is right about its subject, or that the entries
promoted in the stretch are true: it reviews how the work went. That the
fan-out's cost was too high: no measure of it was kept. Nor that the
owner's corrections were avoidable in every case; the A51 order and the
rewrite under [ADR-tmpw306d](../decisions.d/ADR-tmpw306d.md) were the owner's decisions about the work,
not errors found in it. The review is the assistant's (Claude, in this
session); adopting its recommendations is the owner's call.
