---
number: 1196
status: Proposed
formerly:
- THEORY-tmp1ykjb
title: During a visual decision task, neurons within a single area of mouse cortex rarely form discrete functional types, yet the task conditions the area distinguishes are linearly separable in nearly every way
version: 1
tags:
- neuroscience
- cognition
date: '2026-10-30'
source:
- LIT-708
extends:
- THEORY-124
promote_when: >-
  A second recording, not the IBL Brainwide Map, analysed for both halves of
  the claim: neuron types tested against a covariance-matched unimodal null
  in each area, and separability tested over the conditions each area
  distinguishes. It should differ from the source in the way that most
  threatens the claim: several tasks, or one with many more variables, or a
  less-trained animal, or another species such as monkey prefrontal cortex,
  where categorical results have been reported. The claim holds if
  non-sensory areas again fail the null while their distinguishable
  conditions stay separable in nearly every split. It is refuted if
  non-sensory areas there broadly form types beyond the null, or if their
  distinguishable conditions sit in near-degenerate, for example collinear,
  geometry, so that many dichotomies fail. It is also weakened if
  separability falls well below 1 under a stricter criterion, such as a
  fixed accuracy threshold in the large-N limit. Further analyses of the IBL
  data cannot settle it, since they share the task, the variables and the
  animals.
summary: >-
  The wide form of Posani et al. (2026), [LIT-708](../literature.d/LIT-708.md), kept here when the status
  review of 2026-10-30 narrowed [THEORY-124](THEORY-124.md) to what their analysis of the IBL
  Brainwide Map measured and promoted it ([ADR-065](../decisions.d/ADR-065.md); [ADR-047](../decisions.d/ADR-047.md), kind 1). The
  paper asserts that cortical representations are rarely categorical and
  highly separable. One task, overtrained mice, eight variables and a
  lenient separability criterion.
---

# THEORY-1196: During a visual decision task, neurons within a single area of mouse cortex rarely form discrete functional types, yet the task conditions the area distinguishes are linearly separable in nearly every way

## Source

[LIT-708](../literature.d/LIT-708.md), read in full in [NOTE-549](../notes.d/NOTE-549.md). What the source measured is [THEORY-124](THEORY-124.md), which this entry extends.

## The claim

Within a single area of mouse cortex, neurons do not sort into discrete
functional types, yet the conditions the area distinguishes sit in general
position, so a linear readout can split them nearly every way; the authors
read this as cortex prioritizing diversity over categorical structure.

## What would settle it

The promote_when, carried word for word from [THEORY-124](THEORY-124.md) when that entry was narrowed. More readings of the same source cannot settle it.
