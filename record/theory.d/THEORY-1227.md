---
number: 1227
status: Active
formerly:
- THEORY-tmp1drab
title: 'Haken, Kelso and Bunz model the switch of rhythmic bimanual coordination from anti-phase to in-phase at a critical frequency as the loss of one stable state of an order parameter, relative phase, derived from two coupled oscillators; Kelso, Scholz and Schöner report the variability of relative phase rising before the switch in the anti-phase pattern only, in a few subjects and with no statistical test'
version: 1
tags:
- behavioral-integration
- complex-systems
- embodied-cognition
date: '2026-10-30'
source:
- LIT-588
- LIT-1851
extends:
- THEORY-069
supports:
- CLAIM-172
summary: >-
  What the Haken–Kelso–Bunz paper proposes and what the first report of
  critical fluctuations measured, split from [THEORY-069](THEORY-069.md) by the
  twenty-third status review on [THEORY-1110](THEORY-1110.md)'s pattern ([ADR-058](../decisions.d/ADR-058.md), [ADR-065](../decisions.d/ADR-065.md)),
  so that a claim needing only the model and that report can stand on it.
  Both papers are read in full ([NOTE-1424](../notes.d/NOTE-1424.md), [NOTE-1433](../notes.d/NOTE-1433.md)). Whether the switch
  is a nonequilibrium phase transition with critical slowing and
  hysteresis as its warning signs, which needs relaxation-time and
  hysteresis data neither paper shows, stays [THEORY-069](THEORY-069.md)'s question,
  Proposed.
---
<!-- inactive-ok-file: THEORY-069 — Proposed; the account this is split from, which holds the question whether the switch is the transition it proposes -->

# THEORY-1227: Haken, Kelso and Bunz model the switch of rhythmic bimanual coordination from anti-phase to in-phase at a critical frequency as the loss of one stable state of an order parameter, relative phase, derived from two coupled oscillators; Kelso, Scholz and Schöner report the variability of relative phase rising before the switch in the anti-phase pattern only, in a few subjects and with no statistical test

## Source

- Haken, Kelso and Bunz (1985), [LIT-588](../literature.d/LIT-588.md), read in full in [NOTE-1424](../notes.d/NOTE-1424.md): a
  theory paper with one simulation and no new data. Its figures were not
  viewed; what they show is taken from their captions and the text.
- Kelso, Scholz and Schöner (1986), [LIT-1851](../literature.d/LIT-1851.md), read in full in [NOTE-1433](../notes.d/NOTE-1433.md),
  figures included.

## What was proposed and what was measured

**The model ([LIT-588](../literature.d/LIT-588.md), §§2–3).** Relative phase φ between the hands is the
order parameter, "created by the cooperation of the individual components"
and in turn governing them (pp. 348–349). It moves in a potential
V = −a cos φ − b cos 2φ: in-phase and anti-phase are both stable while
|b| > |a|/4, and only in-phase below it, b/a falling as movement frequency
rises. The φ equation is derived from two self-sustained oscillators, one
per hand, whose coupling must be nonlinear and involve delay or
derivatives; the authors say the choice "is not unique" (p. 351). One
simulation with small noise shows the switch. The data modelled are
Kelso's earlier experiments, summarized and not shown: two stable phase
relations, an abrupt switch from anti-phase to in-phase at a critical
frequency, and the system staying in-phase when the frequency is lowered
(p. 348).

**The fluctuations ([LIT-1851](../literature.d/LIT-1851.md)).** As wrist or finger movement is paced
faster, the standard deviation of relative phase rises as the anti-phase
pattern nears the switch, peaks in the transition and falls once in-phase
is reached; started in-phase, the same movement shows neither the switch
nor the rise (Figs. 1–4). The wrist data average 30 runs on four of the ten
subjects run, the finger data ten runs of one representative subject of
seven. No statistical test is reported. The authors read it as critical
fluctuations, "one of the key features of a nonequilibrium phase
transition" (p. 283).

## What this does not say

- That the switch is a nonequilibrium phase transition with critical
  slowing and hysteresis as early warning. Critical slowing is predicted in
  [LIT-1851](../literature.d/LIT-1851.md), which calls its own evidence "very preliminary"; hysteresis is
  reported from Kelso's experiments in [LIT-588](../literature.d/LIT-588.md) with no data. That is
  [THEORY-069](THEORY-069.md)'s question.
- That the fluctuations hold across subjects. Most subjects run are not
  shown, and in the transition region the measure partly reflects the
  switch itself ([NOTE-1433](../notes.d/NOTE-1433.md), Limitations).
- That the result is replicated. Both papers are by the model's authors.
- That HKB-like dynamics reaches beyond bimanual movement. Kelso's later
  extensions are reported in [THEORY-069](THEORY-069.md), from [LIT-601](../literature.d/LIT-601.md).

## Connections

- [CLAIM-172](../claims.d/CLAIM-172.md) draws its criterion of a combined form from this model: a pair
  whose relative phase has its own attractors, fluctuations and switch.
- [THEORY-069](THEORY-069.md) is the general account, Proposed, with the promote_when this
  entry does not meet.
