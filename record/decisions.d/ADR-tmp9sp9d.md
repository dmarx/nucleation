---
status: Active
title: "Parallel filing in one working tree commits only the files each worker lists, pulls CI's repair only between workers, sequences writers after the work they describe, and commits only when the edit before it succeeded"
version: 1
tags:
- record
date: '2026-11-21'
summary: >-
  Active at the owner's "adopt" of 2026-11-21, which accepted the
  retrospective [RETRO-tmpd00ym](../retrospectives.d/RETRO-tmpd00ym.md) and its recommendations 2 to 4. On the
  evening of 2026-11-21 up to nine delegated workers wrote in one
  checkout. A commit swept up another worker's uncommitted note; CI's
  repairs, pulled in mid-work, conflicted with files still being edited;
  a manuscript section was refreshed while the readings it described were
  still being filed; and a commit went ahead after the edit script before
  it had failed. Decided: in a shared working tree commit only the files a
  worker lists; pull CI's repair only between workers; sequence a writer
  after the work it describes, or follow it with a pass replacing
  "being read" mentions with codes; and gate each commit on the edit
  before it. Rejected: a worktree per worker for record edits, which
  splits one unit of work across branches.
---
<!-- inactive-ok-file: ADR-108 — Accepted, Proposed or new; the review, the sibling decision, and reader branches -->

# ADR-tmp9sp9d: Parallel filing in one working tree commits only the files each worker lists, pulls CI's repair only between workers, sequences writers after the work they describe, and commits only when the edit before it succeeded

## Context

The `read-and-file` skill delegates readers and drafters in parallel (step 6). Readers write running notes on branches of their own ([ADR-108](ADR-108.md)), but drafters and filers write the record in the filing branch's one checkout. On 2026-11-21 that meant five drafters at once, then two filers and two manuscript writers. [RETRO-tmpd00ym](../retrospectives.d/RETRO-tmpd00ym.md) found four faults:

- **A commit swept up another worker's file.** A commit of the assistant's own files took in a filer's uncommitted note (28ec330cf).
- **Repairs pulled in mid-work conflicted.** CI's repairs conflicted with files still being edited, three times. Each was resolved with `--ours` after reading the conflict, the practice a devlog note of the same morning warned about.
- **A writer outran its material.** A manuscript section described readings as "being read" that landed before the writer finished.
- **A commit did not wait for its edit.** An edit script failed on a line wrap, and the commit chained after it in the same shell call went ahead without the edit.

## Decision

- **Commit by list.** While any worker is writing, the filer commits only the files a worker has reported as its own. Each worker's brief asks it to list them. No `git add -A`, and no directory-wide add, while another worker runs.
- **Pull CI's repair between workers.** The filer pulls the branch, bringing in CI's repair commit, only when no worker is writing. A conflict with a repair is read hunk by hunk before either side is taken. A repair only adds link targets, so taking the worker's side and letting the next repair re-add them is safe after that reading.
- **Writers after their material.** A writer whose subject is still being filed is started after it lands, or is followed by a pass that replaces "being read" and "being filed" mentions with codes. That pass is not left to the fact-check.
- **Gate each commit on its edit.** An edit and the commit after it run so that the commit happens only if the edit succeeded and its check passed: one script that edits, checks and exits non-zero on failure, then `&&`, or `set -e`.

## Alternatives considered

- **A worktree per worker for record edits,** as readers have. It isolates writes, but it splits one unit of work across branches that then have to be merged, and the units would cite each other's temporary codes.
- **One worker at a time.** Safe, but it gives up the parallelism that made a 646 KB source fileable in an evening.
- **Status quo.** Faults like the four above, each caught late or by the owner.

## Consequences

- The `read-and-file` skill's steps 6 and 11 gain the rules, in this pull request.
- Briefs ask workers to list their files.
