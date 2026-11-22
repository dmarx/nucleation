---
status: Proposed
title: 'Fit to engagement data and stability over time favour clusters that exposure made, and classes a platform uses, over genres that exist in preferences, so neither can warrant an engagement category as a kind; a closure test conditioned on exposure and scored on randomized exposure, against a control partition built from exposure, can tell them apart'
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  A world in which clusters made by exposure alone, with no structure in
  preferences, pass the closure test conditioned on exposure and scored on
  randomized exposure (a class model keeping a clear share of an
  item-level model's held-out gain over the degree model), or do better on
  it than the control partition built from exposure; or a variant of the
  laboratory in which planted genres, unused, fit raw counts better and
  are more stable than exposure-made clusters of the same number and
  size, so that fit and stability would after all rank them correctly.
tags:
- network-science
- philosophy-of-science
- individuation
date: '2026-11-22'
line:
- formal-apparatus
- pragmatic-transport
grounds:
- CASE-tmpw8bs2
bears_on:
- QUESTION-028
- QUESTION-113
- QUESTION-276
summary: >-
  From the run of [CASE-296](../cases.d/CASE-296.md)'s laboratory for [LEAD-030](../leads.d/LEAD-030.md) ([CASE-tmpw8bs2](../cases.d/CASE-tmpw8bs2.md)). Clusters
  that exposure alone made were recovered exactly, fitted raw counts better
  than planted genres (9.6 against 3.7 millinats per cell over the
  degree-only model) and were perfectly stable (ARI 1.00 against 0.49);
  planted genres became stable only when the platform used them (0.89).
  Conditioned on exposure and scored on randomized exposure, the closure
  test kept 0.86 of the item-level gain for planted genres and −0.01 for
  the exposure-made clusters, equal to both control partitions. The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CASE-296 — Proposed; the case whose test this claim reports -->
<!-- inactive-ok-file: CASE-tmpw8bs2 — new; the study this claim reports -->

# CLAIM-tmpvn59f: Fit to engagement data and stability over time favour clusters that exposure made, and classes a platform uses, over genres that exist in preferences, so neither can warrant an engagement category as a kind; a closure test conditioned on exposure and scored on randomized exposure, against a control partition built from exposure, can tell them apart

## The claim

[QUESTION-028](../questions.d/QUESTION-028.md) asks for a criterion, stated before the data, that a
compressible category could fail. [QUESTION-113](../questions.d/QUESTION-113.md) lists persistence under
refinement among the criteria for a category worth naming. In
[CASE-tmpw8bs2](../cases.d/CASE-tmpw8bs2.md), two of the obvious candidates rank the classes the wrong
way.

- **Fit.** A degree-corrected block model on raw engagement counts gained
  9.6 millinats per cell over the degree-only model for clusters that
  exposure alone had made, and 3.7 for genres planted in preferences.
  Using the classes to steer exposure raised it further (to 41.1 for
  planted genres), whether or not preferences moved.
- **Stability.** Re-inferred after fifteen periods, the exposure-made
  clusters matched the first inference with ARI 1.00; the planted genres,
  unused, with 0.49, and with 0.89 once the platform steered by them.

[CASE-296](../cases.d/CASE-296.md)'s closure test does better on two conditions. Conditioned on
exposure (fitted on exposed pairs only, so that a missing engagement is
not a dislike) and scored on randomized exposure, the planted genres kept
0.86 [0.79, 0.93] of an item-level model's held-out gain over the degree
model, and the exposure-made clusters −0.01, equal to a partition by
popularity and to co-clusters of the exposure matrix. Not conditioned, the
test's own control still caught the confound: the genre partition did no
better than the exposure partition (9.6 against 9.6). So the control
partition is the part of the test that cannot be dropped.

The criterion this suggests for engagement categories is a version of
[QUESTION-028](../questions.d/QUESTION-028.md)'s "independently generalizable": the category must keep its
predictive share when exposure is changed by the analyst, and must beat a
partition built from exposure alone. It is necessary in this model, not
shown sufficient: classes reshaped by their own use pass it too
([CLAIM-tmph4j0u](CLAIM-tmph4j0u.md)), which is [CLAIM-402](CLAIM-402.md)'s caution.

## What it does not say

That fit and stability are worthless: both are high for planted genres
that the platform uses. That the test works on real data, where exposure
is logged imperfectly and cannot always be randomized. That passing it
makes a category a real kind; the question stays open.
