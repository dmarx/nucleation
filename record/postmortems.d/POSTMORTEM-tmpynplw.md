---
status: Draft
title: 'A code in an argument''s title failed docs-check on pull request 558, and the failure went unread while five more pull requests were stacked on it'
version: 1
tags:
- process
- ci
date: '2026-11-21'
reviews:
- ADR-054
- ADR-071
pull_requests:
- https://github.com/dmarx/nucleation/pull/558
- https://github.com/dmarx/nucleation/pull/559
- https://github.com/dmarx/nucleation/pull/563
discussions:
- https://claude.ai/code/session_01Hcmtbu5GVkUyn672wCPeC7
summary: >-
  What went wrong: an argument filed on 2026-11-20 had a code in its title;
  CI's repair linked the code in the body heading, so title and heading
  disagreed and docs-check failed on pull requests 558 and 559. The
  assistant did not read CI after pushing, and stacked four more pull
  requests on the failing one. Found on 2026-11-21 when reviewing the
  session; fixed on the base branch and merged forward through five
  branches, one with a conflict. What changes: read CI after each push and
  before stacking (recommended in the session's retrospective).
---
<!-- inactive-ok-file: RETRO-tmp50h9d — Proposed or newly filed; the decision whose procedure was in play, and the retrospective filed beside this -->

# POSTMORTEM-tmpynplw: A code in an argument's title failed docs-check on pull request 558, and the failure went unread while five more pull requests were stacked on it

## What happened

On 2026-11-20 the assistant filed an argument applying the record's
conservation results to restatement, with a title that named a claim by its
code. CI's repair turned the code in the body heading into a link; the title,
which repair does not link, then disagreed with the heading, and lint failed:
"`title:` and the body heading disagree". The record's rule, in the read-and-file
skill, is that titles and headings carry no codes; the assistant had applied it
to another title the same day.

Docs-check on pull request 558 failed at 00:10 on 2026-11-21, and on 559, which
contains the same file. The assistant did not read CI after pushing either.
Pull requests 560 to 563 were stacked on them. The failure was found when the
owner asked for a retrospective and the assistant gathered the session's CI
status.

## Why

- **No step reads CI after a push.** CLAUDE.md says to fix what docs-check names
  if it goes red, but nothing in the working loop looks. [ADR-054](../decisions.d/ADR-054.md) moved checking
  to CI; it did not say who reads CI's result.
- **Stacking hid it.** Each later pull request was based on the failing branch;
  their diffs did not show the file, and nothing stopped a branch being based on
  a red one.
- **The rule is applied by memory.** "No codes in titles" is prose in a skill,
  checked by lint only after repair, so a slip shows only in CI.

## What it cost

One fix on the base branch, then five merges forward, one with a conflict on
the same file; about a session-hour of CI. No entry was wrong in substance, and
nothing merged red.

## What changes

Recommended in [RETRO-tmp50h9d](../retrospectives.d/RETRO-tmp50h9d.md) (recommendations 2 and 3): read CI after every
push, base no pull request on one whose docs-check has not passed, and cap the
depth of a stack. A check that titles carry no codes before pushing would catch
this class locally; it is a candidate for a pre-push hook, for the owner to
decide.
