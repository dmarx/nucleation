---
status: Proposed
title: 'A delegated reader keeps running notes in the repository, outside the record, on a branch of its own that it pushes as it reads, so the owner can see a reading in flight; the notes are removed when the reading is filed, and no downloaded text is ever committed'
version: 1
tags:
- record
date: '2026-11-19'
summary: >-
  ADR-068's eighth invariant had readers draft outside the repository,
  so a long reading showed nothing until its report came back. The owner
  asked on 2026-11-19 for readers' notes to be version-controlled and
  visible in flight, and removed when filed. The owner proposed
  record/workbench.d, but it is a luria journal, "dated and never
  rewritten" and rendered (133 entries), so a reader's transient notes
  would break its contract. Instead a reader writes only
  scratch/readers/<key>.md, outside record/, in its own worktree on a
  branch claude/readers/<key> with no pull request, and commits and
  pushes after each step. Readers still do not write to the record. The
  filer files from the final report and deletes the branch. Downloaded
  texts stay out of the repository. Changes ADR-068's eighth invariant;
  the rest stands. Rejected: the workbench; readers pushing to the filing
  branch; the filer saving reports after the fact.
---
<!-- inactive-ok-file: ADR-068 — Proposed; the decision whose eighth invariant this one changes -->

# ADR-tmpnswfy: A delegated reader keeps running notes in the repository, outside the record, on a branch of its own that it pushes as it reads, so the owner can see a reading in flight; the notes are removed when the reading is filed, and no downloaded text is ever committed

## Context

ADR-068's eighth invariant: "Readers do not write to the record. A
delegated reader drafts outside the repository, and the filer files."
Readers' drafts lived in the session's scratchpad, invisible to the
owner until the reader returned, and lost with the container.

The owner, 2026-11-19, asked for the workbench to serve as "a version
controlled scratchpad, so the readers file to the workbench directly,
and workbench isn't treated as part of the record", to "expose in-flight
reader notes to me, which can be helpful if the reader's are taking a
long time", and not to be persistent: "when the filer files, it would
remove/move the associated notes".

record/workbench.d is not outside luria. It is a configured journal
(luria.yaml, `journals.workbench`), rendered to docs/workbench, whose
blurb says its entries are "dated and never rewritten" (ADR-032); it
held 133 entries on that date. Removing notes from it would break that
contract, and every push would put half-written notes on the site. The
repository's `scratch/` folder, outside record/, already holds working
material luria does not read.

## Decision

1. **Where.** A delegated reader writes its running notes to one file,
   `scratch/readers/<key>.md`, and nothing else in the repository. The
   file is not part of the record: luria does not read it, nothing cites
   it, and the filer files from the reader's final report as before.
2. **On a branch of its own.** Each reader works in its own git worktree
   on a branch `claude/readers/<key>`, cut from the filing branch, with
   no pull request, so pushes trigger no CI and readers do not contend
   with each other or with the filing branch. It commits and pushes after
   each meaningful step: a copy located, a section read, bearings
   searched. A rejected push is followed by a pull and a second push,
   never a force-push.
3. **What may be committed.** Working notes and short verbatim quotes.
   Never a downloaded text, a PDF or a long excerpt: downloads stay in the
   session's scratchpad. The repository is public.
4. **Removed when filed.** When the reading is filed, the filer deletes
   the reader's branch. Its history goes with it; what matters is in the
   NOTE, the THEORY and the curation entry.
5. **Readers still do not write to the record.** ADR-068's eighth
   invariant now reads: "Readers do not write to the record. A delegated
   reader drafts outside the record, in running notes it pushes on a
   branch of its own (ADR-tmpnswfy), and the filer files."

The first application is the reading of Brown and colleagues (GPT-3) and
Howard and Ruder (ULMFiT) on 2026-11-19, whose readers worked on
`claude/readers/gpt3` and `claude/readers/ulmfit`.

## Alternatives considered

- **The workbench.** Its contract is permanence, and it is rendered.
- **Readers pushing to the filing branch.** Every push would run CI, and
  readers would race each other and the bot's repair commits.
- **The filer saving each report as a workbench entry after the fact.**
  Keeps the invariant unchanged, but shows nothing in flight, which was
  the point.
- **Status quo.** A long reading stays a black box.

## Consequences

- The owner can watch a reading on GitHub as it happens, branch by
  branch.
- Readers need git and a worktree; the brief says how, and forbids
  touching anything but their notes file.
- Reader branches are transient. A reader's notes outlive the container
  only until the filing.
