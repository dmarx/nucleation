---
number: 75
status: Open
formerly:
- LEAD-tmpcu27l
title: 'Run the staging experiment: states A and B with a staging state C, measuring the bottleneck budget, the least time at budget and the readiness, to produce the four kinds of case'
version: 1
stage: specified
priority: medium
method:
- formal
tags:
- operations-research
- society-and-governance
- mathematics
date: '2026-11-19'
line:
- realizability
- readiness
advances:
- QUESTION-392
operationalized_in:
- CASE-198
summary: >-
  Named in [QUESTION-392](../questions.d/QUESTION-392.md). Filed by the backlog audit of 2026-11-19.
---

# LEAD-075: Run the staging experiment: states A and B with a staging state C, measuring the bottleneck budget, the least time at budget and the readiness, to produce the four kinds of case

## What it would do

Build the small model with a staging state and compute, over parameters,
the bottleneck budget, least time at budget and readiness.

Where the record names it:

- [QUESTION-392](../questions.d/QUESTION-392.md): "reachable but too expensive, reachable only through an
  architectural change, or reachable only when temporary reserve capacity is
  available."

## What would count

Cases of all four kinds answer [QUESTION-392](../questions.d/QUESTION-392.md) by construction; kinds that
cannot occur narrow it.

## Note of 2026-11-22: carried out
<!-- inactive-ok-file: CASE-tmp17sbe CLAIM-tmpmvt0a — new; the executed study of this lead and the claim filed from it -->

Run by a delegated worker on branch claude/lead-075-staging-state. The model ([CASE-198](../cases.d/CASE-198.md)'s, with states (q, z), one capacity, a crease constraint as a variant, crossing and switching times, a background load and a temporary reserve for readiness), its 14 pytest tests and its results are under scratch/studies/lead-075/, whose README states each modelling choice the lead left open and the reason for it. Filed: [CASE-tmp17sbe](../cases.d/CASE-tmp17sbe.md) (executed-study) and [CLAIM-tmpmvt0a](../claims.d/CLAIM-tmpmvt0a.md) (demonstrated thesis). All four kinds of case occur, each on an open region of budget and reserve, so "what would count" is met: no kind is ruled out. What remains: readiness under policies other than the fastest admissible one ([TERM-115](../terms.d/TERM-115.md)'s actual policy), several resources, and a staging architecture faster than the home one. The stage and status are the owner's to set.
