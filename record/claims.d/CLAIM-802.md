---
number: 802
status: Proposed
formerly:
- CLAIM-tmp85eq8
title: 'Phase transition as singularity resolution'
statement: >-
  Alternative reading (a) of the owner's suggestion on singularities: a
  phase transition in learning is the network carrying out a resolution of a
  singularity, so that in passing through the transition training performs,
  or passes through, a blow-up of a singular point of its parameter space
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that the map a blow-up adds cannot be a stage of training: that
  any trajectory of a network's parameters stays in the original parameter
  space, and that a model pulled back through a blow-up gives, at every
  point over a singular point, the distribution of that point, so that a
  transition read as a resolution changes nothing the network computes
  (CLAIM-305; ARG-132 argues it). A reading of "resolution" in a
  looser sense, such as leaving a singular stratum, does not save this
  reading; it is a different one.
tags:
- learning-theory
- mathematical-statistics
date: '2026-11-21'
line:
- learned-structure
bears_on:
- QUESTION-363
summary: >-
  One of two alternative readings of the owner's U23 in the exchange "Rich
  Get Richer Power Laws" ([CLAIM-834](CLAIM-834.md)): "singularity theory has an
  account for phase transitions in learning as resolutions of
  singularities that might be useful here". This is reading (a), the
  owner's words taken literally: training carries out a resolution. The
  other is reading (b), [CLAIM-823](CLAIM-823.md), A37's reframing. The owner
  chooses. The assistant's verdict, that [CLAIM-305](CLAIM-305.md) tells against this
  reading, is [ARG-132](../arguments.d/ARG-132.md). The statement of the reading is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2193 THEORY-2191 — Proposed; the readings of Yang and of Lee et al. filed 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-834 CLAIM-823 ARG-132 CLAIM-833 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->

# CLAIM-802: Phase transition as singularity resolution

**This is reading (a) of [CLAIM-834](CLAIM-834.md), the owner's U23, one of two
alternatives.** The other, reading (b), is [CLAIM-823](CLAIM-823.md). The owner
chooses.

## The claim

U23, verbatim: "singularity theory has an account for phase transitions in
learning as resolutions of singularities that might be useful here".

Read literally, "phase transitions … as resolutions of singularities" says
that what happens at a transition is a resolution: the network, as it
trains, carries out or passes through a blow-up of a singular point of its
parameter space, and that is what makes the transition. On this reading a
stage of learning would be a step in the resolution process, and the
network after a transition would sit in the resolved space, where the
degeneracy it had before is gone.

## Where it stands

The record holds a result against it. A blow-up is a proper map π from a
new space onto the old one, and the model on the new space is p(x | π(u)),
so every point over a singular point gives that point's distribution and
"States that no data could tell apart before" stay indistinguishable
([CLAIM-305](CLAIM-305.md), Active). A37 §3 makes the same point in the exchange:
resolution "doesn't mean that training literally performs an algebraic
blow-up. Resolution is an analytical tool that reveals the structure hidden
inside a singular parameterization." [ARG-132](../arguments.d/ARG-132.md) sets out the argument
from [CLAIM-305](CLAIM-305.md) against this reading and answers its critical questions.

## What it does not say

- Not that the owner meant this. The sentence admits both readings, and
  the record files both.
- Not the looser sense in which a network "resolves" a degeneracy by
  moving off a singular stratum, so that redundant parameters acquire
  separate effects. That is no blow-up; it is closer to A39 §6's feature
  differentiation ([CLAIM-833](CLAIM-833.md)) and to reading (b).

## Note of 2026-11-22: Yang, and Lee, Smith, Adam and Hoogland, read

Contrast and background; neither bears on this reading. Yang's transition
([THEORY-2193](../theory.d/THEORY-2193.md)) is a dynamical instability of a detached probe's loss
at a saddle, nothing like training carrying out a blow-up. Lee et al.'s
([THEORY-2191](../theory.d/THEORY-2191.md)) are posterior mass moving between two regions U and V;
no resolution appears.
