---
number: 936
status: Proposed
formerly:
- CLAIM-tmp4223o
title: 'Suppression vs removal is elicitation-relative'
statement: >-
  In a small network trained with a benign trigger-conditioned behaviour,
  fine-tuning against the trigger that drives the behaviour's expression to
  zero leaves it recoverable on items never retrained by a cheap
  intervention on the trigger's pathway, to a degree that falls with longer
  fine-tuning and nearly vanishes under weight decay, while sampling and
  brief retraining of the whole network recover almost none of it; so
  whether the behaviour was suppressed or removed is settled only relative
  to a declared family of elicitation procedures and their budget
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant with the executed study of LEAD-082,
    as the finding that study supports.
role: thesis
warrant: empirical
defeated_if: >-
  A run of the same design (a trigger-conditioned arbitrary map, a
  fine-tune that silences it, recovery scored on items never retrained,
  a control that never learned the map) in which gate-only retraining or
  a fitted activation vector recovers no more on held-out items than in
  the control; or one in which every elicitation family tested gives the
  same verdict for every arm, so that the choice of family makes no
  difference.
tags:
- representation-learning
- learning-theory
- agency
date: '2026-11-22'
line:
- learned-structure
- realizability
grounds:
- CASE-357
complements:
- CLAIM-697
uses:
- TERM-118
summary: >-
  From the toy-scale run of [CASE-275](../cases.d/CASE-275.md) ([CASE-357](../cases.d/CASE-357.md)). At width 128 over
  five seeds, every fine-tune that showed the trigger drove the triggered
  map's expression to zero, yet retuning only the first layer on 6 of 24
  symbols brought it back on the other 18 at 18 to 31%, and one vector
  added to the first layer at 44 to 53%, against 0 to 1% in a network that
  never learned it; full retraining recovered 3 to 11% at one learning
  rate and about 0 at a lower one, and sampling's coverage at 1000 draws
  was 0.2 to 4%. Longer fine-tuning lowered the residue; weight decay
  nearly removed it. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-275 CASE-357 CLAIM-697 TERM-118 — Proposed or new; the design, the study this rests on, the claim it complements and the term it uses -->

# CLAIM-936: Suppression vs removal is elicitation-relative

## The claim

[CASE-357](../cases.d/CASE-357.md) trained a two-layer network to apply one arbitrary relabelling
under ordinary contexts and another when a trigger token is present, then
fine-tuned the trigger out. Four findings carry the claim.

- **Expression goes to zero; the store does not.** In every arm that showed
  the trigger in fine-tuning, the triggered map was never the network's
  answer, and its probability under sampling was near zero. Yet the map came
  back on symbols the recovery never touched when only the first layer was
  retrained on 6 symbols, or when one vector was fitted there. Since the map
  is arbitrary, that can only come from what the network kept.
- **The silencing is at the gate.** The trigger stayed decodable and kept
  its first-layer direction, while its linearized effect on the output
  fell from about 11 to about 0; a doubled push along the direction still
  produced the map on ordinary inputs in 19 to 29% of cases.
- **It is graded.** The residue fell with fine-tuning length and nearly
  vanished under weight decay.
- **The verdict depends on the family.** Sampling and brief full retraining
  read every suppression arm as removed; gate-only retraining and a fitted
  vector read all but the weight-decay arm as masked.

So [TERM-118](../terms.d/TERM-118.md)'s masking and removal are not properties of the network
alone but of the network with a declared family of elicitations and a
budget, as [CLAIM-697](CLAIM-697.md) says of dispositions in general. In this setting the
family has to include interventions on internals before the difference is
visible at all.

## What it does not say

- That a language model behaves the same way. The study is a toy-scale
  stand-in; [CASE-357](../cases.d/CASE-357.md) lists what an LM-scale version would add.
- Which family the record should declare for "removed". [CASE-357](../cases.d/CASE-357.md)
  files the two readings as alternatives for the owner.
- Anything about finking or mimicking, which the study did not test.
