---
number: 182
status: Open
formerly:
- LEAD-tmpwq9wf
title: 'Find or run an adequately powered Contextuality-by-Default test on human pragmatic judgements, with signalling accounted for and outcome coding fixed in advance'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    A dated note records what the worker for this lead did on 2026-11-22:
    the literature check, the design (CASE-329) and its power
    simulation (CASE-328). operationalized_in CASE-329 added.
    Status and stage unchanged; marking it done is the owner's.
stage: idea
priority: high
method:
- reading
- empirical
tags:
- contextuality
- philosophy-of-language
date: '2026-11-19'
line:
- pragmatic-transport
advances:
- CLAIM-009
- CLAIM-105
- CLAIM-325
- CLAIM-219
- CLAIM-037
summary: >-
  It decides the contextuality strand of the pragmatic-transport line.
  Named in [CLAIM-009](../claims.d/CLAIM-009.md) and [CLAIM-105](../claims.d/CLAIM-105.md). Filed by the backlog audit of
  2026-11-19.
operationalized_in:
- CASE-329
---
<!-- inactive-ok-file: CASE-329 CASE-328 CLAIM-895 CLAIM-896 THEORY-2226 LIT-3100 LIT-3099 LIT-3101 — new; what this lead's work filed on 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-009 CLAIM-105 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-182: Find or run an adequately powered Contextuality-by-Default test on human pragmatic judgements, with signalling accounted for and outcome coding fixed in advance

## What it would do

Check the literature for such a test; failing one, design it with
signalling estimators, a power analysis and the outcome coding fixed
before data.

Where the record names it:

- [CLAIM-009](../claims.d/CLAIM-009.md): "It waits on a Contextuality-by-Default analysis of human
  pragmatic judgements that robustly finds or excludes contextuality."
- [CLAIM-105](../claims.d/CLAIM-105.md): "documents that no adequately powered CbD test on pragmatic
  judgements has been run."

## What would count

Robust contextuality supports [CLAIM-009](../claims.d/CLAIM-009.md) and defeats [CLAIM-325](../claims.d/CLAIM-325.md)'s null;
robust absence does the reverse.

## Note of 2026-11-22: the check made and the design drafted

**The literature check** (scratch/studies/lead-182/search.md). Europe PMC
and arXiv were searched for Contextuality-by-Default tests on human
pragmatic or meaning judgements since [CASE-053](../cases.d/CASE-053.md)'s search of 2026-10-10;
OpenAlex refused (rate limit without a key) and was not retried. No
powered test on pragmatic judgements was found. One new CbD test on
elicited judgements turned up, Bruza, Lee and Hoyte (2025) on real and
AI-generated faces ([LIT-3100](../literature.d/LIT-3100.md), Unfetched: every lawful route met an
obstacle); its content is perceptual. Wang and Sadrzadeh (2024) measure
signalling in garden-path sentences on BERT's probabilities
([LIT-3101](../literature.d/LIT-3101.md)). The Snow Queen study, which [CASE-053](../cases.d/CASE-053.md) read, now has an
entry ([LIT-3099](../literature.d/LIT-3099.md)). Lo, Sadrzadeh and Mansfield's generalised Winograd
schema was read ([THEORY-2226](../theory.d/THEORY-2226.md)).

**The design** is [CASE-329](../cases.d/CASE-329.md): free per-question answers in a
four-context cyclic layout, Winograd and indirect-request items, one
presentation an item, a fixed sign pattern from a pilot, the plug-in
statistic for detection and a conservative bound for absence.

**The power analysis** was run by simulation, as the lead's `empirical`
method allows ([CASE-328](../cases.d/CASE-328.md)). Accounting for signalling is what costs:
the plug-in estimate is biased upward when true signalling is small
([CLAIM-896](../claims.d/CLAIM-896.md)), so a violation of Lo et al.'s size needs about 1,600
valid respondents a context when items signal and over 4,000 when they
do not, against the 650 [CASE-053](../cases.d/CASE-053.md) estimated with signalling assumed away.
Absence can be certified only by a conservative bound, and only where
signalling is small. The design also met a constraint of its own:
pooling counterbalanced cells can manufacture contextuality
([CLAIM-895](../claims.d/CLAIM-895.md)).

**What remains.** The study itself: writing and piloting the items,
fixing the leans the design lists as the owner's, and a budget for some
10,000 respondents. Reading Bruza et al. needs a copy the owner supplies
or a host allowed.
