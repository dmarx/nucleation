---
number: 157
status: Open
formerly:
- LEAD-tmpsn7tp
title: 'Measure the permutation-aligned barrier over several path families, and test whether alignment always removes the barrier between networks known to share a mechanism'
version: 1
stage: idea
priority: medium
method:
- empirical
tags:
- loss-landscapes
- representation-learning
date: '2026-11-19'
line:
- learned-structure
- pragmatic-transport
advances:
- QUESTION-069
- CLAIM-263
- CLAIM-187
summary: >-
  Named in [QUESTION-069](../questions.d/QUESTION-069.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-385 CLAIM-993 CLAIM-994 CLAIM-992 — new; LEAD-157's executed study, its finding and the two alternative readings, filed 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-263 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-157: Measure the permutation-aligned barrier over several path families, and test whether alignment always removes the barrier between networks known to share a mechanism

## What it would do

Align networks by permutation, measure the loss barrier along several path
families, and repeat for a pair built to share a mechanism.

Where the record names it:

- [QUESTION-069](../questions.d/QUESTION-069.md): "Phase III runs aligned by permutation, with the barrier
  measured on several path families. Alongside that, a pair of networks
  known to share a mechanism, tested for whether alignment always removes
  their barrier."

## What would count

A barrier that survives alignment between networks sharing a mechanism
defeats the reading that a surviving barrier marks a different mechanism
([CLAIM-263](../claims.d/CLAIM-263.md)); its removal supports it.

## Note of 2026-11-22: run at toy scale

Run by a delegated lead worker at toy scale on CPU, as [CASE-385](../cases.d/CASE-385.md). Small
two-hidden-layer ReLU MLPs were trained in numpy on a two-cue task, with a
cue-reliance test that uses no barrier saying which cue each net relies on.
Pairs were aligned four ways, and at width 5 by an exhaustive search over
permutations and rescalings. Barriers were measured on the straight line,
a trained Bezier curve and a trained polychain. A load-by-temperature grid
gave a phase-III analogue. Code, results and a rerun recipe are under
scratch/studies/lead-157/. By this lead's criterion, alignment does not
always remove the barrier between networks that share a mechanism: at
width 5, same-cue pairs keep barriers even under the full group, and an
exact rescaled copy keeps one under permutations alone. Also, different-cue
pairs connect at width 64 and above. [CLAIM-993](../claims.d/CLAIM-993.md) states the finding.
Whether it defeats [CLAIM-263](../claims.d/CLAIM-263.md) depends on the grain of "mechanism", so it is
filed as two alternatives for the owner: [CLAIM-994](../claims.d/CLAIM-994.md) (defeated) and
[CLAIM-992](../claims.d/CLAIM-992.md) (narrowed to preconditions). What remains is a probe on
which the two cues disagree, a rerun at a scale where [THEORY-112](../theory.d/THEORY-112.md)'s
measurements live, and Yang et al.'s actual phase III.
