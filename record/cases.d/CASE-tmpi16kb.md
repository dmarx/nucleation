---
status: Active
title: 'Building the record''s staging branch found a requirement no one had stated: at the first promotion, merged by hand, the workflow that was to merge main back into staging never ran, because it ran only after promoting something itself'
version: 1
standing: documented
kind: specimen
tags:
- software-engineering
- design-rationale
- philosophy-of-technology
date: '2026-11-21'
line:
- record-as-apparatus
illustrates:
- CLAIM-tmphigw4
- CLAIM-tmpm9ep1
summary: >-
  The record's own tooling, 2026-11-21. Documented in ADR-116's history and
  pull requests 565, 566 and 567.
---
<!-- inactive-ok-file: ADR-116 CLAIM-tmphigw4 CLAIM-tmpm9ep1 — Proposed; the decision whose application this is, and the claims it illustrates -->

# CASE-tmpi16kb: Building the record's staging branch found a requirement no one had stated: at the first promotion, merged by hand, the workflow that was to merge main back into staging never ran, because it ran only after promoting something itself

## What happens

On 2026-11-21 the owner proposed a staging branch with a nightly promotion
into main, and ADR-116 specified it: work merges into staging, a Promote
workflow merges staging into main, concretizes the codes, and merges main
back into staging (pull request 565). The first promotion was made by hand,
as pull request 566. Answering the owner's question whether the back-merge
would stay a manual step, the assistant read the workflow and found that
every Promote job, the back-merge included, ran only when staging was ahead
of main. After a hand merge main is ahead, so the back-merge would never
run, and a later promotion would merge a staging still holding temporary
codes into a main that had made them permanent. The owner then asked why
the back-merge could not follow any merge into main; the answer exposed a
second requirement, that it wait for the docs run, since that run's commit
is pushed with a token that starts no workflow. Both went into pull request
567 and ADR-116's version 2.

## What it shows

The specification was written, reviewed and passed CI. The missing
requirement appeared only once the thing existed and was used in a way
the specification allowed, a promotion by hand, but its author had not
pictured. Building revised the specification, which is the reflexive case of
CLAIM-tmphigw4, and what was learned was about how a record's memory has to
work across branches, which is CLAIM-tmpm9ep1.

## What it cannot show

One case, in tooling the assistant wrote, found by the assistant reading its
own workflow. It does not show how often building finds what review misses.
