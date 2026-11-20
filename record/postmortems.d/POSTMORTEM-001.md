---
number: 1
status: Draft
formerly:
- POSTMORTEM-tmp5eoc7
title: 'The batch of 2026-11-19: pull requests 535 to 540, a stacked series folded top-down'
version: 1
tags:
- record
- process
date: '2026-11-20'
reviews:
- ADR-068
- ADR-108
- ADR-109
pull_requests:
- https://github.com/dmarx/nucleation/pull/535
- https://github.com/dmarx/nucleation/pull/536
- https://github.com/dmarx/nucleation/pull/537
- https://github.com/dmarx/nucleation/pull/538
- https://github.com/dmarx/nucleation/pull/539
- https://github.com/dmarx/nucleation/pull/540
discussions:
- https://claude.ai/code/session_01HcmtbsDR5i5G9oxErMDiB4
summary: >-
  Trigger 2 of [ADR-110](../decisions.d/ADR-110.md): six pull requests, five of them a stack built
  on a schema change and folded top-down into main. Everything landed
  green. The costs were a stack forced by putting readings on the schema
  pull request, codes split at hyphens by the filer's line-wrapping, a bot
  repair colliding with an unpulled second commit, an owner review that
  had to be merged up four branches, and reader branches the session could
  not delete. What changes: four small rules, and the reader-branch ending
  [ADR-108](../decisions.d/ADR-108.md) left open.
---
<!-- inactive-ok-file: ADR-108 ADR-110 POSTMORTEM-002 — Proposed or newly filed; the decisions this postmortem reviews -->

# POSTMORTEM-001: The batch of 2026-11-19: pull requests 535 to 540, a stacked series folded top-down

## What happened

Pull request 535 filed the follow-up turns of an exchange. The LEAD scheme
went on 536, based on 535, with ten pilot leads; 538 (GPT-3 and ULMFiT),
539 (data scheduling) and 540 (fifteen follow-up readings) each stacked on
the one before, because each cited leads the previous one filed. 537
(reader notes, [ADR-108](../decisions.d/ADR-108.md)) stood alone on main. The owner asked for all to be
merged; 537 went first, then 540 was merged into 539, 539 into 538, 538
into 536, 536 into 535, and 535, with main merged in, into main. Each head
was green before its fold; the intermediate merge commits were not
re-checked, the final one was.

## What it cost

1. **A stack forced by a schema change.** Readings that cited the pilot leads
had to wait on 536, so four content pull requests stacked on a schema pull
request. [POSTMORTEM-002](POSTMORTEM-002.md) already recommends landing a schema change
alone and early.
2. **Codes split at hyphens.** The filer's line-wrapping broke codes such as
[THEORY-2058](../theory.d/THEORY-2058.md) across lines (THEORY- / tmp1b3hj), which the linter does
not read as codes. Found while resolving a conflict on 540; fixed on 535,
538, 539 and 540.
3. **A bot repair against an unpulled commit.** The second commit on 540 was
made before pulling CI's repair of the first, which conflicted on every
file both touched; the commit was rebuilt by script on top of the repair.
4. **An owner review four branches down.** The owner's comment on 539
concerned a lead filed on 536; the fix went on 536 and was merged up
through 538, 539 and 540, with one conflict on the lead itself.
5. **Small faults found on the way.** A history in ascending order failed
docs-check on 537; a dangling note code (a reading's NOTE cited by the
wrong temporary code) was found on 539 and fixed there.
6. **Reader branches left over.** [ADR-108](../decisions.d/ADR-108.md)'s reader branches could not be
deleted from the session (the git proxy refuses branch deletion); six now
wait on the owner.

## What changes

- Wrap prose with break_on_hyphens off, so codes are never split. (Applied
to the filer's tools during the batch.)
- Pull before every second commit on a branch CI repairs; CLAUDE.md already
says so, and the batch shows why.
- Keep stacks shallow: a reading that cites a lead on an unmerged schema
pull request can cite it by the pull request in prose, and stand on main.
- [ADR-108](../decisions.d/ADR-108.md)'s end of procedure (delete, or commit the notes' removal on the
reader branch) is still open; until the owner rules, reader branches
accumulate and are listed for deletion at each batch close.
