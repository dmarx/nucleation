---
status: Proposed
title: 'A proposed study: for each generation of image model, the number of generations of one character at which training a character LoRA becomes cheaper than conditioning on references, at matched identity fidelity'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    At the owner's review of dmarx/nucleation#482: the crossover allows an
    up-front cost on the reference route too, and costs are counted per
    acceptable output, retries included.
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
- THEORY-tmpvarvt
- THEORY-tmplz597
- THEORY-tmpdzbq1
summary: >-
  A's proposal, from the exchange "Identify Synthesis Opportunities"
  (2026-11-08, A18), to measure the crossover the owner's case
  [CASE-tmp40vka](CASE-tmp40vka.md) turns on: "whether improved reference conditioning raises
  the number of times a character must be reused before training a LoRA
  pays off". A's patch held the design, which the export does not carry;
  A's turn gives only its aim, "a quality-matched comparison across
  generations and reuse counts", and that it "measures that crossover
  rather than assuming its direction". The arms and measures below are the
  filer's spelling-out of that sentence, to meet what a proposed study
  must state. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpvarvt THEORY-tmplz597 THEORY-tmpdzbq1 THEORY-tmpgxdpz — Proposed; the readings of 2026-11-12, cited in its note -->
<!-- inactive-ok-file: CASE-tmp40vka — Proposed; the owner's case this study would measure -->
<!-- inactive-ok-file: THEORY-331 — Proposed; the lifetime-compute objective the design borrows -->
<!-- inactive-ok-file: SYNTHESIS-015 — Proposed; the account A proposed to revise -->

# CASE-tmp3isyl: A proposed study: for each generation of image model, the number of generations of one character at which training a character LoRA becomes cheaper than conditioning on references, at matched identity fidelity

## What would be measured

For a set of characters and, in each model generation of [CASE-tmp40vka](CASE-tmp40vka.md)'s
table, one trained route (a character LoRA, or DreamBooth or Textual
Inversion where that was the practice) and one reference route (an
adapter, an in-context editor or a reference-conditioned model):

- **up-front cost** of each route, F_train (preparing the training
  images and fitting) and F_ref (preparing the reference sheet or set),
  in compute and in hours of work;
- **cost per acceptable output** of each route, c_train and c_ref, in
  compute and wall-clock, counting the retries needed to get an output
  that meets the fidelity target, not only the time of one generation;
- **identity fidelity** of each route's outputs, by a fixed identity
  measure and by raters blind to the route, with the routes tuned to a
  common fidelity target;
- from these, the **crossover** n* = (F_train − F_ref) / (c_ref − c_train),
  the number of acceptable outputs of one character past which the
  trained route is cheaper at that fidelity, and how n* moves across
  generations. It is a positive crossover in that direction only when
  training costs more up front and less per acceptable output; otherwise
  one route dominates and there is no crossover.

The objective is [THEORY-331](../theory.d/THEORY-331.md)'s: total cost of reaching a fixed quality,
counting the uses as well as the preparation. [THEORY-342](../theory.d/THEORY-342.md)'s measurement,
the exchange rate between training and per-use compute at fixed
strength, is the model of a quality-matched comparison.

## Main threat to inference

Matching fidelity across models that differ in everything else. A18:
"H3 is primarily a video-generation model, for example, so comparing its
one-frame workflow with older native image models requires careful
controls." An identity measure tuned to one generation's failure modes
can favour it. The hours of human work in F_train and F_ref are also hard to measure
and can dominate it.

## What each outcome would show

- **n* rises across generations**: better reference conditioning has
  moved the break-even toward computing on demand, as the owner's U6
  suggests, and for these two strategies the trade is one dial whose
  setting follows relative costs, as [QUESTION-095](../questions.d/QUESTION-095.md) conjectures.
- **n* is flat or falls**: reference routes improved in fidelity without
  becoming cheaper per use, or trained routes became cheaper to make,
  and the thread's judgement reflects quality, not cost.
- **No common fidelity target is reachable by both routes** in some
  generation: there the choice is not a cost trade at all, and the case
  would need restating.

## Provenance

A numbered this study 235 and the owner's case 234, in a bundle never
committed; neither number is on the record. A's patch also revised
[SYNTHESIS-015](../syntheses.d/SYNTHESIS-015.md) to integrate both; that revision was not made here (see the
curation entry of 2026-11-12 for this exchange).

## Note of 2026-11-12: what the readings give the design

- **F and c_ref for one generation.** PhotoMaker's Table 1 ([THEORY-tmpvarvt](../theory.d/THEORY-tmpvarvt.md))
  gives, on one V100, DreamBooth 1284 s per subject and reference routes of
  10–12 s per image. It does not give DreamBooth's per-image cost after
  training, so n* cannot be computed from it.
- **F for 2022.** DreamBooth ([THEORY-tmplz597](../theory.d/THEORY-tmplz597.md)): about five A100-minutes per
  subject on Stable Diffusion.
- **Fidelity targets.** DreamBooth's DreamBench and DINO measure, and
  FLUX.1 Kontext's character-reference cases with a face-embedding measure
  and multi-turn drift ([THEORY-tmpdzbq1](../theory.d/THEORY-tmpdzbq1.md)), which adds fidelity across
  successive uses.
- **The main threat, seen.** PhotoMaker's rankings change with the metric:
  IP-Adapter leads on face similarity, PhotoMaker on DINO and CLIP-I,
  DreamBooth on CLIP-T. InstantID's comparison with character LoRAs
  ([THEORY-tmpgxdpz](../theory.d/THEORY-tmpgxdpz.md)) has no measure at all, which is why the study is
  needed.
