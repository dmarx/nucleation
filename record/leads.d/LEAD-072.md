---
number: 72
status: Open
formerly:
- LEAD-tmpbxhk1
title: 'Build signalling estimators with bias correction and a stated sampling error, or a signalling test with a stated null, and apply them to the published systems with their occurrence counts'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    A dated note records what the worker for this lead did on
    2026-11-22: the estimators, interval and test (CLAIM-937), their
    check by enumeration and simulation and the application to LIT-842's
    printed systems (CASE-359), and why LIT-851 could not be used.
    Status and stage unchanged; marking it done is the owner's.
stage: idea
priority: medium
method:
- formal
tags:
- contextuality
- mathematical-statistics
date: '2026-11-19'
line:
- pragmatic-transport
advances:
- CLAIM-105
- CLAIM-235
- CLAIM-125
summary: >-
  Named in [CLAIM-235](../claims.d/CLAIM-235.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-937 CASE-359 — new; what LEAD-072 filed on 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-105 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-072: Build signalling estimators with bias correction and a stated sampling error, or a signalling test with a stated null, and apply them to the published systems with their occurrence counts

## What it would do

Derive the estimators or the test, and apply them to [LIT-851](../literature.d/LIT-851.md)'s data.

Where the record names it:

- [CLAIM-235](../claims.d/CLAIM-235.md): "Estimators with bias correction and a stated sampling error,
  or a test for signalling with a stated null hypothesis, applied to
  [LIT-851](../literature.d/LIT-851.md)'s systems with their occurrence counts."

## What would count

Estimators with stated error meet [CLAIM-235](../claims.d/CLAIM-235.md)'s request and let [CLAIM-105](../claims.d/CLAIM-105.md)'s
judgement of the published tests be made.

## Note of 2026-11-22: what was done, and what remains

The worker for this lead derived the estimators and the test and checked
them ([CLAIM-937](../claims.d/CLAIM-937.md), [CASE-359](../cases.d/CASE-359.md); scratch/studies/lead-072).

- **No unbiased estimator of Δ exists** at any finite count, since Δ is
  not a polynomial in the probabilities; "bias correction" can only
  reduce the bias. The root of the unbiased estimate of each squared
  difference roughly halves the plug-in's bias at zero signalling and
  falls short where signalling is large.
- **A stated sampling error valid at every count**: simultaneous
  Clopper-Pearson intervals for the 2k context marginals give an
  interval for Δ with coverage at least 1 − α. The approximate Newcombe
  interval undercovers.
- **A test with a stated null** (no content signals): per-content
  Fisher exact tests, Bonferroni over contents, size at most α. No valid
  5% test can find a content signalling from two or fewer occurrences in
  each context.

**The application to [LIT-851](../literature.d/LIT-851.md) is blocked twice.** Its appendix prints
proportions and err(Δ), not occurrence counts ([NOTE-654](../notes.d/NOTE-654.md)), and its only
open copy, UCL Discovery eprint 10146180, answered with a Cloudflare
challenge (HTTP 403) on 2026-11-22; the Semantic Scholar API answered
HTTP 429. Neither was retried. The tools were applied instead to the
three binary systems [LIT-842](../literature.d/LIT-842.md) prints as fractions (arXiv:2107.14589v1),
with counts taken as each row's least common denominator.

**What remains:** [LIT-851](../literature.d/LIT-851.md)'s per-system occurrence counts, from the
authors or from Wang's thesis if it prints them (UCL Discovery eprint
10193159, behind the same challenge), and then a run of apply.py on
them. The estimator half of [CLAIM-235](../claims.d/CLAIM-235.md)'s request is met; the data half is
not.
