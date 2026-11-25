---
number: 9
status: Draft
formerly:
- RETRO-tmplxaev
title: "The lead backlog run: about 120 leads carried out by delegated workers, each on its own branch and pull request into staging, from 2026-11-22 to 2026-11-23; what went right was one lead per pull request with merge on green, alternatives filed instead of questions, honest negative results and each CI failure becoming a skill rule within the hour, and what went wrong was a blanket code rewrite in a merge that corrupted 28 formerly lists, a done-check that missed a finished lead, and conflicts and disk use left to pile up"
tags:
- record
date: '2026-11-23'
reviews:
- ADR-071
- ADR-109
- ADR-116
- ADR-121
- ADR-128
- ADR-139
- ADR-140
- ADR-141
- ADR-142
pull_requests:
- https://github.com/dmarx/nucleation/pull/623
- https://github.com/dmarx/nucleation/pull/642
- https://github.com/dmarx/nucleation/pull/644
- https://github.com/dmarx/nucleation/pull/664
- https://github.com/dmarx/nucleation/pull/667
- https://github.com/dmarx/nucleation/pull/690
- https://github.com/dmarx/nucleation/pull/697
- https://github.com/dmarx/nucleation/pull/741
- https://github.com/dmarx/nucleation/pull/746
- https://github.com/dmarx/nucleation/pull/751
- https://github.com/dmarx/nucleation/pull/752
- https://github.com/dmarx/nucleation/pull/757
- https://github.com/dmarx/nucleation/pull/770
discussions:
- https://claude.ai/code/session_01HcmtbsHCnWAcGaecC7H4Pn
summary: >-
  At the owner's request ("retro"), on 2026-11-23, after the stretch that
  began with "look for other leads on the record which you can address on
  your own. triage them, then work your way down the list by priority".
  The assistant triaged the open leads, then ran them through delegated
  workers under the run-lead skill: up to nine at once, then three, then
  one at a time at the owner's word. About 120 lead pull requests (623 to
  770) merged into staging, with the open-access sweep, the
  persist-as-you-go decisions and four rules added to the skill. Going
  well: one lead per branch and pull request, merged on green, kept
  staging moving and the promotion pull request current; workers filed
  rival readings as alternatives and stopped at bot checks; several
  studies pre-registered and reported failures plainly; each CI failure
  became a skill rule within the hour; and saved progress let workers
  stopped by usage limits resume. Going wrong: the assistant's own
  merge script rewrote temporary codes inside formerly lists on 28
  entries, found by the owner in another session and repaired there
  (pull request 757); a done-check missed a finished lead; dependent pull
  requests were merged out of order once; and branches cut before a
  promotion's back-merge conflicted repeatedly, while finished worktrees
  filled the disk to 99%. Six recommendations follow. The review is the
  assistant's (Claude, in this session); adopting them is the owner's
  call.
---
<!-- inactive-ok-file: ADR-115 ADR-116 ADR-141 ADR-142 CLAIM-510 — Proposed; the decisions this review assesses and the entries it names as examples -->

# RETRO-009: The lead backlog run: about 120 leads carried out by delegated workers, each on its own branch and pull request into staging, from 2026-11-22 to 2026-11-23; what went right was one lead per pull request with merge on green, alternatives filed instead of questions, honest negative results and each CI failure becoming a skill rule within the hour, and what went wrong was a blanket code rewrite in a merge that corrupted 28 formerly lists, a done-check that missed a finished lead, and conflicts and disk use left to pile up

## What it covers

From the owner's request of 2026-11-22 to triage the open leads and work down them by priority, to the owner's "retro" of 2026-11-23, about 03:30 UTC. The pull requests are the lead runs 623 to 770 (about 120, each titled with its lead), with these others:

| Pull request | What it did |
|---|---|
| 642 | Persist-as-you-go: [ADR-141](../decisions.d/ADR-141.md) and [ADR-142](../decisions.d/ADR-142.md), filed as alternatives, with a demonstration |
| 644, 649, 652 | The Unfetched works swept through open-access interfaces, and the readings that sweep made possible |
| 664, 690, 697, 752 | Rules added to the run-lead skill after failures: stop only your own processes; relation fields take the kinds docs/record.md names; never write to shared paths; no codes in an excuse's reason beyond those it excuses |
| 667 | An audit of 33 backlog leads: two asked for what the record already held |
| 741 | [LEAD-215](../leads.d/LEAD-215.md)'s missing `history:`, which failed the Promote workflow's lint and skipped its back-merge |
| 757 | The repair, by another session, of the formerly lists this stretch broke (below) |

The devlog notes it reads are those of 2026-11-22 at 04:15:00 (a usage limit stopping all filers at once), 10:40:30 (work held until the end put at risk), 15:59:10 (one shell command breaking /dev/null for every worker), and 2026-11-23 at 00:53:40 (the formerly lists) and 01:05:31 (study scripts resumable only when nothing went wrong). No earmarked note is open: the one of 2026-11-21 at 22:30:41 was answered by [RETRO-008](RETRO-008.md) and [ADR-140](../decisions.d/ADR-140.md).

## What went well, and why

- **One lead, one branch, one pull request, merged on green.** Under [ADR-071](../decisions.d/ADR-071.md) as changed by [ADR-116](../decisions.d/ADR-116.md), with [ADR-121](../decisions.d/ADR-121.md)'s merge on green, about 120 leads reached staging in two days without a revert. Each pull request carried its own result, its alternatives and what waited on the owner. The promotion pull request (743) was kept in [ADR-128](../decisions.d/ADR-128.md)'s marked sections, with the description read just before each write, and holds every lead's choices in one place.
- **Rival readings were filed, not asked about.** Almost every lead ended with two or three alternatives filed as claims, the worker's lean named. That is [ADR-140](../decisions.d/ADR-140.md)'s first rule holding under delegation: the brief said so, and the workers did it. Examples: the three readings of [CLAIM-510](../claims.d/CLAIM-510.md)'s condition ([LEAD-164](../leads.d/LEAD-164.md)); direction or capacity for [CLAIM-404](../claims.d/CLAIM-404.md)'s "resources" ([LEAD-015](../leads.d/LEAD-015.md)); what "without penalties" means in [LEAD-181](../leads.d/LEAD-181.md)'s test.
- **Negative and partial results were reported as such.** [LEAD-107](../leads.d/LEAD-107.md) found the workbench reconstructions cannot run its tests and said so, with its single coder's audit of its own rules. [LEAD-106](../leads.d/LEAD-106.md) found no study of the design [QUESTION-303](../questions.d/QUESTION-303.md) needs. [LEAD-191](../leads.d/LEAD-191.md) could not reanalyse [LIT-844](../literature.d/LIT-844.md)'s data, and did the narrower analysis the published counts allowed. [LEAD-183](../leads.d/LEAD-183.md) pre-registered its predictor, recorded both amendments before the runs they governed, and filed the registered predictor's failure to transfer.
- **The workers kept the outside rules.** They stopped at every bot check (Cloudflare, Anubis), sent no email address anywhere, and read only lawful copies, recording each block in the work's status note.
- **Each CI failure became a skill rule within the hour.** A CLAIM code under `bears_on` ([LEAD-020](../leads.d/LEAD-020.md)) became 690. A worker that moved a file onto /dev/null became 697. Two crashes of the repair step's prune ([LEAD-145](../leads.d/LEAD-145.md), [LEAD-106](../leads.d/LEAD-106.md)) traced to a lead's code in its excuses' reasons became 752; the next run ([LEAD-189](../leads.d/LEAD-189.md)) passed first time once the rule was applied.
- **Saved progress paid for itself.** Under [ADR-141](../decisions.d/ADR-141.md) and [ADR-142](../decisions.d/ADR-142.md), workers pushed each commit as they made it and kept a progress file. When usage limits stopped workers ([LEAD-105](../leads.d/LEAD-105.md) among them), each was resumed from its own branch with one message, and nothing was redone.

## What did not go well

- **The assistant's merge script corrupted 28 formerly lists.** To resolve [#746](https://github.com/dmarx/nucleation/issues/746)'s conflicts, the assistant built a map from every temporary code to its concrete code and rewrote every temporary code in the files the branch touched. That was right for citations and wrong for `formerly:`, where the temporary code is the point: each list came to name its own entry. The assistant's check before pushing looked at what had been deleted and at the branch's own additions, not at front-matter fields. The owner found the damage in another session; that session traced it to the merge commit, restored 56 entries (these 28 and 28 older ones), added a rule to the run-lead skill, and proposed a lint check upstream (devlog, 2026-11-23 00:53:40). The other session caught what the assistant should have. The rewrite was also probably unnecessary: [CASE-333](../cases.d/CASE-333.md) lists its temporary code as an alias, and the repair step resolves links through aliases.
- **A done-check missed a finished lead.** The assistant dispatched [LEAD-038](../leads.d/LEAD-038.md) after a grep for dated notes on the wrong heading pattern; the lead had been filed that morning and promoted. The worker found it at step 1 and filed nothing, so the cost was one short run. Checking for a changelog fragment named for the lead found the rest.
- **Dependent pull requests merged out of order.** The merge helper was called on three pull requests at once and merged [LEAD-164](../leads.d/LEAD-164.md)'s (744) before [LEAD-177](../leads.d/LEAD-177.md)'s (740), whose entries 744 cited. Excuse lines kept staging green, so nothing broke; the order had been stated and was not kept.
- **Conflicts after each promotion, resolved by hand, one at a time.** When the Promote workflow's lint failed on [LEAD-215](../leads.d/LEAD-215.md), its back-merge was skipped, and staging and main disagreed about which codes were concrete. Every branch cut before the fix (741) then conflicted on the codes it cited: [#741](https://github.com/dmarx/nucleation/issues/741) itself twice, then 745, 746 and 756. Each was resolved correctly in the end, but by hand, and [#746](https://github.com/dmarx/nucleation/issues/746)'s resolution is the one that broke the formerly lists.
- **Finished worktrees filled the disk.** A worker reported 750 MB free. The 148 worktrees of finished workers held 26 GB. Removing the 137 that were clean and pushed freed 24 GB; 11 with uncommitted changes were kept for the owner. Nothing cleaned them as the workers finished.
- **No devlog notes were filed during the stretch.** [ADR-115](../decisions.d/ADR-115.md) asks for notes as the work goes, going right as well as going wrong. The assistant filed none in two days of work, so this review was written from the conversation and the pull requests, and the notes it reads were filed by other sessions.
- **The triage overstated what workers could do.** Three high-priority leads (058, 085, 091) need experiments run with delegated agents, and the workers have no tool to start agents. The triage marked them feasible; that came to light only when they reached the top of the list.

## Recommendations

1. **Never rewrite codes in a merge resolution.** Resolve conflicts by keeping both sides, and let the repair step spell targets through aliases. If a code must be rewritten, rewrite only citations in the body, never front matter. Run the check the other session added (no entry's `formerly` contains its own code) before pushing any merge. The skill now carries the rule; this recommendation extends it to the assistant's own merges, not only the workers'.
2. **Decide "already done" by the changelog fragment and the lead's dated notes, together,** and refresh the triage list from staging before each dispatch rather than from the triage file.
3. **Merge one pull request at a time when one cites another,** in the stated order, and say the order in the turn before merging.
4. **Merge the fix to a failed promotion before anything else,** and cut no new lead branch from staging until it has landed. That keeps every branch on one side of the code change.
5. **Remove a worker's worktree when its pull request merges,** after checking it is clean and its head is pushed.
6. **File a devlog note when each batch closes,** going right and going wrong, as [ADR-115](../decisions.d/ADR-115.md) asks, so the next review reads notes and not a transcript. Mark in the triage which leads need tools a worker lacks.

[ADR-141](../decisions.d/ADR-141.md) and [ADR-142](../decisions.d/ADR-142.md) are alternatives and wait on the owner; this run is evidence for the rule they share, not for either over the other.

## What it does not say

- That the workers' science is settled. Every result here waits on the owner's choices, collected in the promotion pull request's choices section.
- That delegation should slow down. The faults above were the assistant's, in merging and housekeeping, not the workers' filings.
