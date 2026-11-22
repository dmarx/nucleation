---
number: 67
status: Open
formerly:
- LEAD-tmpb4tsj
title: 'Build the finite evaluative-transport construction: three overlapping contexts, comparisons on overlaps, derived transport, and the null of trivial holonomy'
version: 1
stage: idea
priority: medium
method:
- formal
tags:
- mathematics
- ethics
date: '2026-11-19'
line:
- pragmatic-transport
advances:
- QUESTION-130
summary: >-
  Named in [QUESTION-130](../questions.d/QUESTION-130.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-tmpmov06, CASE-tmpg9x2o — Proposed; filed 2026-11-22 carrying out this lead -->

# LEAD-067: Build the finite evaluative-transport construction: three overlapping contexts, comparisons on overlaps, derived transport, and the null of trivial holonomy

## What it would do

Construct the null first: three contexts with different local coordinates
and trivial holonomy; then a case with nontrivial holonomy.

Where the record names it:

- [QUESTION-130](../questions.d/QUESTION-130.md): "That would prove that perspectival plurality does not
  imply nontrivial gauge curvature."

## What would count

The null answers the first part of [QUESTION-130](../questions.d/QUESTION-130.md) by construction.

## Note of 2026-11-22: carried out

Done by a delegated worker on 2026-11-22, branch claude/lead-067-holonomy-null. Code, 18 tests and results are under scratch/studies/lead-067/.

- **The null, first.** Three contexts in random O(d) frames represent one configuration, and the transport is derived by orthogonal fit on each overlap's shared commitments. The derived transports are then the frame changes and the holonomy is I. That is proved in [CLAIM-tmpmov06](../claims.d/CLAIM-tmpmov06.md) (i) and checked in 3000 draws.
- **Then a nontrivial case.** In ℝ², each overlap is fitted exactly, and each context holds an internal angle between the commitments it shares with its two neighbours. The holonomy is the sum of those angles ([CLAIM-tmpmov06](../claims.d/CLAIM-tmpmov06.md) (iii)). A curved-chart variant gives the spherical excess ([CASE-tmpg9x2o](../cases.d/CASE-tmpg9x2o.md)).
- **Found along the way.**
  - With exact and determined overlaps, H = I exactly when the three contexts glue into one configuration up to frames, so a nontrivial holonomy is a gauge-invariant discrepancy among the contexts' comparisons.
  - An overlap that does not determine its fit leaves the holonomy to the modeller.
  - Noise gives a measurable null, about 1.3σ median at ten anchors per overlap, and with three anchors it can flip a fit's orientation.

What would count, per this lead, is met: the null answers the first part of [QUESTION-130](../questions.d/QUESTION-130.md) by construction. What remains is outside this lead: whether measured evaluative contexts have representations of this kind. Marking the lead Done, and splitting [QUESTION-130](../questions.d/QUESTION-130.md), are the owner's.
