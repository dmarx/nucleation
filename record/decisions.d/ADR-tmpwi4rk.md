---
status: Active
title: 'Whenever staging is ahead of main, a pull request from staging into main is open for the owner, kept by a workflow: on every push to staging, a job opens one if none is open, so the review point exists without anyone remembering it'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Filed and ruled on the same night, before merging: the owner chose among
    the two readings with "577-automate this". This reading is adopted, and
    the job is written in the same pull request.
tags:
- record
- process
date: '2026-11-21'
summary: >-
  The owner's request of 2026-11-21, read as something the tooling keeps.
  The alternative to [ADR-tmp6xm7w](ADR-tmp6xm7w.md), which has the assistant keep it.
---
<!-- inactive-ok-file: ADR-116 ADR-tmp6xm7w — Proposed; the staging decision, the grant this review point goes with, the regime, and the two readings -->

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

A job on every push to staging (`.github/workflows/promotion-pr.yml`,
running `.github/scripts/promotion-pr.sh`) checks whether staging's content
differs from main's and whether a pull request from staging into main is
open, and opens one if not, with a description generated from the merge
commits since main: one line per pull request merged into staging. It tests
a content diff, not a commit count, because right after a promotion the
back-merge leaves staging one merge commit ahead of main with the same tree.
The owner reviews and merges it as in
[ADR-tmp6xm7w](ADR-tmp6xm7w.md).

The job uses the REST API, and runs only on pushes to staging and by hand.
The back-merge from main into staging ([ADR-116](ADR-116.md), version 2) pushes with the
workflow token and starts no run, which is right: after a promotion the two
agree. A pull request the job opens with that token starts no docs-check of
its own; each pull request into staging was checked, and Promote lints the
merged tree before it pushes. The repository must allow GitHub Actions to
create pull requests.

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

The job, in this pull request, run dry against the repository on
2026-11-21: with pull request 576 open it reported one already open; with
that check bypassed it would have opened one listing the merges since main;
on equal trees the content test passes over. Pull request 576 was opened by
hand meanwhile, and the job takes over from the next push to staging after a
promotion.
