---
number: 135
status: Open
formerly:
- LEAD-tmpoe54n
title: 'Run individuation by probing at rising budgets'
version: 1
stage: specified
priority: medium
method:
- empirical
- formal
tags:
- mathematics
- individuation
- complex-systems
date: '2026-11-19'
line:
- realizability
- formal-apparatus
advances:
- QUESTION-382
- CLAIM-583
- CLAIM-322
operationalized_in:
- CASE-202
summary: >-
  Named in [CASE-202](../cases.d/CASE-202.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-202 — Proposed; cited in the backlog audit of 2026-11-19 -->
<!-- inactive-ok-file: CASE-tmpxkvpz CLAIM-tmpco6u9 — the executed study and finding filed from this lead's run of 2026-11-22 -->

# LEAD-135: Run individuation by probing at rising budgets

## What it would do

Run [CASE-202](../cases.d/CASE-202.md): probe a system for units at rising budgets and record when
the verdicts on its individuals stabilize.

Where the record names it:

- [CASE-202](../cases.d/CASE-202.md): "an explicit individuation-by-probing component"

## What would count

Verdicts that stabilize at a finite budget support [CLAIM-583](../claims.d/CLAIM-583.md); verdicts
that keep changing bear on [QUESTION-382](../questions.d/QUESTION-382.md).

## Note of 2026-11-22: run executed

Carried out in a delegated worktree. The individuation-by-probing component
of [CASE-202](../cases.d/CASE-202.md) was built in numpy over finite transition systems and run on
[CLAIM-583](../claims.d/CLAIM-583.md)'s seed pair: the distinguish-or-not verdict agrees under the
static probe family (budget 0), parts at a budget of one move, and stabilizes
there. A constructed family shows the stabilization budget can be set to any
finite length. The executed study is [CASE-tmpxkvpz](../cases.d/CASE-tmpxkvpz.md) and the finding
[CLAIM-tmpco6u9](../claims.d/CLAIM-tmpco6u9.md) (code: `scratch/studies/lead-135/`). The finite
stabilization budget is the support for [CLAIM-583](../claims.d/CLAIM-583.md) that "what would count"
names. Not run: [CASE-202](../cases.d/CASE-202.md)'s maintenance ([CLAIM-566](../claims.d/CLAIM-566.md)) and
architecture-change readouts, and a destructive probe for the control; these
remain. Status and stage unchanged; the owner marks the lead.
