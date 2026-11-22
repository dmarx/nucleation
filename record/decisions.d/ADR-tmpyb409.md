---
status: Proposed
title: 'Lead workers and long computations persist their progress as they go, as delegated readers already do, on a branch of their own, so that a stop loses at most the step in hand'
version: 1
tags:
- record
- mechanism
date: '2026-11-22'
summary: >-
  Alternative (b) of two, filed on the owner's request of 2026-11-22 to
  stop losing work. It leaves [ADR-108](ADR-108.md) standing for readers and adds the two
  kinds of work that lost or risked work that day: lead workers, whose
  brief said to commit at the end, and long computations, whose results
  were held in memory until the end. Each pushes after every step from a
  branch of its own; a computation writes each item's result as it is
  produced, inside the repository, resumes by skipping what is written,
  and is checkpointed at least every ten minutes; a background run gets a
  time limit above twice its estimate and is restructured when its pace
  says it will not finish; the lead-worker brief moves into the
  repository as a skill. The alternative is [ADR-tmpvqx5l](ADR-tmpvqx5l.md), which supersedes
  [ADR-108](ADR-108.md) with one general rule. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: ADR-108 ADR-tmpvqx5l — Proposed or new; the decision this one sits beside, and the alternative to it -->

# ADR-tmpyb409: Lead workers and long computations persist their progress as they go, as delegated readers already do, on a branch of their own, so that a stop loses at most the step in hand

## Context

As in [ADR-tmpvqx5l](ADR-tmpvqx5l.md). In brief: on 2026-11-22 a lead worker's brief said to
commit at the end. The assistant's own sweep of the Unfetched works held
its results in memory and was stopped at 162 of 184 by a time limit it
could have foreseen, which lost the probe details. The briefs lived in
the scratchpad. [ADR-108](ADR-108.md)'s rule for readers covers none of these.

## Decision

1. **Lead workers** cut their branch and push it before their first
   substantive step, push after every record file created or edited and
   every computation finished, and keep
   `scratch/studies/<key>/PROGRESS.md` (what is done, what is next, the
   choices made), updated in the same push.
2. **Long computations**, delegated or the assistant's own, write each
   item's result to an append-only file in the repository's study
   directory, resume by skipping what is written, and are checkpointed by
   a commit at least every ten minutes. Bulk output and downloads stay in
   the scratchpad.
3. **Background runs** get a time limit above twice their estimate, and
   are stopped and restructured when their pace says they will not
   finish.
4. **The lead-worker brief** lives in the repository as the `run-lead`
   skill.

[ADR-108](ADR-108.md) stands unchanged for readers. Filers keep [ADR-tmp9sp9d](ADR-tmp9sp9d.md)'s
commit-by-list rule.

## First application

As in [ADR-tmpvqx5l](ADR-tmpvqx5l.md): the `run-lead` skill, and the rebuilt, checkpointed
sweep.

## Alternatives considered

- **[ADR-tmpvqx5l](ADR-tmpvqx5l.md):** one general rule superseding [ADR-108](ADR-108.md), which also
  covers filers and moves all working tables into the repository. It is
  broader. This one is narrower and leaves the reader rule where it is.
- **Status quo.** The sweep's loss repeats.

## Consequences

- Two decisions on one rule. Work of a kind neither names, such as a
  filer's drafts, stays uncovered.
