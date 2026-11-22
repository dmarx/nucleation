---
status: Proposed
title: 'A test of whether a forgotten association survives that counts it retained when any of several readers (other cues, runner-up answers, probes at several layers, partial reversion of the update) recovers it overstates retention badly unless each reader is scored against a matched world in which the association never held, because the readers'' chance hits add up'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant from the run of LEAD-043
    (CASE-tmprir2y), as a delegated worker.
role: thesis
warrant: empirical
defeated_if: >-
  In a rerun with the same kind of reader battery, the union of the
  readers recovers values that a matched-world model never held at a rate
  near the single-reader chance rate (about one in the number of possible
  values), so that an uncontrolled union would not have overstated
  retention; or a correction that needs no matched world (a permutation of
  the labels within the same model, or a multiple-comparison bound on the
  readers) reproduces the matched-world baseline closely enough that the
  twin adds nothing.
tags:
- representation-learning
- philosophy-of-science
- learning-theory
date: '2026-11-22'
line:
- learned-structure
- pragmatic-transport
grounds:
- CASE-tmprir2y
bears_on:
- QUESTION-010
summary: >-
  A methodological finding from CASE-tmprir2y. Eleven readers were applied
  to every forgotten fact in a toy transformer: another cue, the runner-up
  answer, a logit lens and linear and MLP probes at three layers, and
  reverting each block's update. Read against the matched twin's values,
  which the model never held, at least one reader recovered the value in
  28 to 46 percent of facts, across all nine arms. Each reader alone hits
  by chance about one time in sixteen. Without the twin, a union test would
  have called nearly half of a never-learned table retained. This is what
  the note of 2026-11-15 on QUESTION-010 proposed the matched worlds for,
  and the run shows the control is needed, not only cheap. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CASE-tmprir2y CASE-274 — new or Proposed; the run this rests on and the design it reduces -->

# CLAIM-tmpqvkag: A test of whether a forgotten association survives that counts it retained when any of several readers (other cues, runner-up answers, probes at several layers, partial reversion of the update) recovers it overstates retention badly unless each reader is scored against a matched world in which the association never held, because the readers' chance hits add up

## The claim

CASE-274's outcome table asks, for each apparently forgotten association,
whether any of several readers finds it. CASE-tmprir2y ran eleven such
readers on a toy transformer. Against the model's own forgotten values the
union recovered 87 to 98 percent in the unlearning, overwriting and
new-task arms; against the twin's values, which the model never held, it
recovered 28 to 46 percent. The average forgotten fact was found by 2.8 to
3.6 readers; the average never-held value by 0.4 to 1.0. So the evidence
for survival is the gap and the count, not the union, and a survival test
without a matched world, or at least a per-reader false-positive rate,
would have overstated it by a factor of up to two.

In the toy, random facts make the chance rate known (1/16 per reader). In
a language model, where a value can be inferred from correlates, the chance
rate is not known, and the matched world is what supplies it. This is the
use the note of 2026-11-15 on QUESTION-010 proposed.

## What it does not say

It does not say that readers are unreliable one at a time; most single
readers sat near 1/16 on the twin's values. It says that their union does
not.
