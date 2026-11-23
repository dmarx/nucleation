---
number: 80
status: Open
formerly:
- LEAD-tmpdnvzr
title: 'Run the readiness simulator twice, with each period''s budget set to the last period''s peak spending and with carry-over'
version: 1
stage: specified
priority: high
method:
- formal
tags:
- operations-research
- society-and-governance
date: '2026-11-19'
line:
- readiness
- formal-apparatus
- realizability
advances:
- CLAIM-577
- QUESTION-394
summary: >-
  [QUESTION-394](../questions.d/QUESTION-394.md) calls it the cheapest test of [CLAIM-577](../claims.d/CLAIM-577.md) and gives the
  design. Named in [QUESTION-394](../questions.d/QUESTION-394.md). Filed by the backlog audit of 2026-11-19.
---

# LEAD-080: Run the readiness simulator twice, with each period's budget set to the last period's peak spending and with carry-over

## What it would do

Run A's simulator in the two budget regimes.

Where the record names it:

- [QUESTION-394](../questions.d/QUESTION-394.md): "A's simulator is also the cheapest test of [CLAIM-577](../claims.d/CLAIM-577.md)."

## What would count

Capability lost without carry-over and kept with it supports [CLAIM-577](../claims.d/CLAIM-577.md) in
its first organizational test.

## Note of 2026-11-22: run, with a corollary

<!-- inactive-ok-block: CASE-315 CLAIM-878 CASE-200 — new or Proposed; filed for this lead, and CASE-200's rule run as filed -->
The simulator [QUESTION-394](../questions.d/QUESTION-394.md) records from A was built and run under spend-matching and under carry-over, 300 runs of ten years per configuration ([CASE-315](../cases.d/CASE-315.md); code, tests and outputs under scratch/studies/lead-080/). The lead's "what would count" is met: under spend-matching the heavy rescue squad is lost for good, and under full carry-over it is kept in every run. The study adds what makes a period quiet: a month in which nothing at all mobilizes the squad, so the dispatch policy and the drill schedule decide how long it survives the rule; that is filed as [CLAIM-878](../claims.d/CLAIM-878.md), a corollary of [CLAIM-577](../claims.d/CLAIM-577.md). Since the lead does not say which carry-over rule it means, two were run: rolling over what the peak rule leaves unspent, which holds the budget, and [CASE-200](../cases.d/CASE-200.md)'s base-plus-balance rule, which never loses the squad but rations one used every month to every other month. What remains: [QUESTION-394](../questions.d/QUESTION-394.md)'s own question, the policy ranking across congestion, geography, substitutes, accuracy and coverage cost, which this run does not sweep; and a budget kept in money or hours rather than at the period's peak, under which a cancelled dispatch would hold far less of it. The lead stays Open.

## Note of 2026-11-23: the manuscript governance-of-possibility

<!-- inactive-ok-block: ADR-tmpsfjxu CASE-315 LEAD-tmpnblsf — Proposed or new; the work, the run and the extension -->
Parallel. A48 §9.6 of the owner's manuscript (ADR-tmpsfjxu) proposes,
without a design, the study this lead partly ran (CASE-315); its redesign
and novel-harm arms are new, and are LEAD-tmpnblsf.
