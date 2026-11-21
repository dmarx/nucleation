---
status: Proposed
title: 'Whenever staging is ahead of main, a pull request from staging into main is open for the owner, kept by a workflow: on every push to staging, a job opens one if none is open, so the review point exists without anyone remembering it'
version: 1
tags:
- record
- process
date: '2026-11-21'
summary: >-
  The owner's request of 2026-11-21, read as something the tooling keeps.
  The alternative to [ADR-tmp6xm7w](ADR-tmp6xm7w.md), which has the assistant keep it.
---
<!-- inactive-ok-file: ADR-116 ADR-tmpq5b9e ADR-tmp6xm7w — Proposed; the staging decision, the grant this review point goes with, the regime, and the two readings -->

# ADR-tmpwi4rk: Whenever staging is ahead of main, a pull request from staging into main is open for the owner, kept by a workflow: on every push to staging, a job opens one if none is open, so the review point exists without anyone remembering it

## Context

The owner, 2026-11-21: "let's make part of the convention be that whenever staging is ahead of main, there's an open PR waiting for me"

Staging holds work that has passed its own pull request's check and has not
reached main ([ADR-116](ADR-116.md)). The owner's review is the promotion from staging to
main, which they named their primary intervention point when granting the
assistant merges into staging ([ADR-tmpq5b9e](ADR-tmpq5b9e.md)). A review point needs a place
to review: one pull request from staging into main, listing the batch and
the choices waiting in it. On the night of 2026-11-21 staging was 59 commits
ahead of main with no such pull request; the first promotion (pull request
566) had been opened by hand, once.

The request has two readings, filed as alternative decisions under the
dialectic regime's rule for several readings: [ADR-tmp6xm7w](ADR-tmp6xm7w.md), a convention the
assistant keeps; ADR-tmpwi4rk, a workflow that keeps it. The owner chooses.

## Decision

A job on every push to staging checks whether staging is ahead of main and
whether a pull request from staging into main is open, and opens one if not,
with a description generated from the merge commits since main: one line
per pull request merged into staging. The owner reviews and merges it as in
[ADR-tmp6xm7w](ADR-tmp6xm7w.md).

The job is not written in this pull request. A change to CI waits for the
owner under the regime; if this reading is chosen, the job is its first
application. The back-merge from main into staging ([ADR-116](ADR-116.md), version 2) is
a push the workflow token makes, which starts no run, so the job would also
run after the Docs run on main, as the back-merge does.

## Alternatives considered

- **[ADR-tmp6xm7w](ADR-tmp6xm7w.md)**, the assistant keeping it by convention.
- **Status quo.**

## Consequences

- The review point exists whoever merged into staging, the assistant, the
  owner or another session, and needs no one to remember it.
- The generated description lists what merged, not the choices waiting on
  the owner; the assistant can still add those.
- One more workflow, with a token allowed to open pull requests.

## First application

None yet: the job is written if this reading is chosen. Pull request 576
was opened by hand meanwhile.
