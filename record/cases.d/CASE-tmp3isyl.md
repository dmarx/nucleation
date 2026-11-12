---
status: Proposed
title: 'A proposed study: for each generation of image model, the number of generations of one character at which training a character LoRA becomes cheaper than conditioning on references, at matched identity fidelity'
version: 1
standing: stipulated
kind: proposed-study
tags:
- learning-theory
date: '2026-11-12'
line:
- distributed-agency
bears_on:
- QUESTION-095
draws_on:
- THEORY-331
- THEORY-342
summary: >-
  A's proposal, from the exchange "Identify Synthesis Opportunities"
  (2026-11-08, A18), to measure the crossover the owner's case
  CASE-tmp40vka turns on: "whether improved reference conditioning raises
  the number of times a character must be reused before training a LoRA
  pays off". A's patch held the design, which the export does not carry;
  A's turn gives only its aim, "a quality-matched comparison across
  generations and reuse counts", and that it "measures that crossover
  rather than assuming its direction". The arms and measures below are the
  filer's spelling-out of that sentence, to meet what a proposed study
  must state. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmp40vka — Proposed; the owner's case this study would measure -->
<!-- inactive-ok-file: THEORY-331 — Proposed; the lifetime-compute objective the design borrows -->
<!-- inactive-ok-file: SYNTHESIS-015 — Proposed; the account A proposed to revise -->

# CASE-tmp3isyl: A proposed study: for each generation of image model, the number of generations of one character at which training a character LoRA becomes cheaper than conditioning on references, at matched identity fidelity

## What would be measured

For a set of characters and, in each model generation of CASE-tmp40vka's
table, one trained route (a character LoRA, or DreamBooth or Textual
Inversion where that was the practice) and one reference route (an
adapter, an in-context editor or a reference-conditioned model):

- **up-front cost** F of the trained route: preparing the training
  images and fitting, in compute and in hours of work;
- **per-generation cost** of each route, c_train and c_ref, in compute
  and wall-clock;
- **identity fidelity** of each route's outputs, by a fixed identity
  measure and by raters blind to the route, with the routes tuned to a
  common fidelity target;
- from these, the **crossover** n* = F / (c_ref − c_train), the number of
  generations of one character past which the trained route is cheaper at
  that fidelity, and how n* moves across generations.

The objective is THEORY-331's: total cost of reaching a fixed quality,
counting the uses as well as the preparation. THEORY-342's measurement,
the exchange rate between training and per-use compute at fixed
strength, is the model of a quality-matched comparison.

## Main threat to inference

Matching fidelity across models that differ in everything else. A18:
"H3 is primarily a video-generation model, for example, so comparing its
one-frame workflow with older native image models requires careful
controls." An identity measure tuned to one generation's failure modes
can favour it. The hours of human work in F are also hard to measure
and can dominate it.

## What each outcome would show

- **n* rises across generations**: better reference conditioning has
  moved the break-even toward computing on demand, as the owner's U6
  suggests, and for these two strategies the trade is one dial whose
  setting follows relative costs, as QUESTION-095 conjectures.
- **n* is flat or falls**: reference routes improved in fidelity without
  becoming cheaper per use, or trained routes became cheaper to make,
  and the thread's judgement reflects quality, not cost.
- **No common fidelity target is reachable by both routes** in some
  generation: there the choice is not a cost trade at all, and the case
  would need restating.

## Provenance

A numbered this study 235 and the owner's case 234, in a bundle never
committed; neither number is on the record. A's patch also revised
SYNTHESIS-015 to integrate both; that revision was not made here (see the
curation entry of 2026-11-12 for this exchange).
