---
status: Active
status_note: >-
  read in full 2026-11-14 ([NOTE-tmpbqaec](../notes.d/NOTE-tmpbqaec.md)) from the authors' arXiv v4
  (arXiv:2101.07049v4, 18 Oct 2022, "Preprint submitted to Chaos, Solitons
  & Fractals"); the publisher's version was not tried. Worth reading as
  the review that separates a pattern from its mechanism: purely
  competitive and scale-dependent-feedback models give the same
  gap–labyrinth–spot sequence and different collapses.
title: 'Integrating theory and experiments to link local mechanisms and ecosystem-level consequences of vegetation patterns in drylands'
version: 1
history:
- version: 1
  date: '2026-11-14'
  note: >-
    Registered and read on 2026-11-14. It was first sent to a reader as a
    stand-in for Sun et al. (2026, PNAS, doi:10.1073/pnas.2618656123)
    while that work was out of reach, and was then filed in its own right
    at the owner's request, as Sun et al.'s ref. 34. Citation from
    Crossref (no mailto): Ricardo Martinez-Garcia, Ciro Cabal, Justin M.
    Calabrese, Emilio Hernández-García, Corina E. Tarnita, Cristóbal
    López and Juan A. Bonachela, Chaos, Solitons & Fractals 166, 112881
    (issue January 2023). `published:` is the arXiv v1 date, 2021-01-18
    (ADR-002). Read by a delegated reader. The lead string-matched every
    quotation used here against the arXiv text.
tags:
- ecology
- complex-systems
date: '2026-11-14'
published: '2021-01-18'
arxiv: '2101.07049'
doi: '10.1016/j.chaos.2022.112881'
first_author: 'Martinez-Garcia'
keywords:
- 'vegetation patterns'
- 'drylands'
- 'scale-dependent feedback'
- 'nonlocal competition'
- 'desertification'
- 'kernel-based models'
- 'net interaction'
implementations: []
summary: >-
  Martinez-Garcia, Cabal, Calabrese, Hernández-García, Tarnita, López &
  Bonachela (2023), Chaos, Solitons & Fractals; arXiv 2021. A review. Models
  of dryland vegetation sit on a continuum from scale-dependent feedback
  (SDF: facilitation near a plant, competition farther off) to purely
  competitive feedback (PCF). Both give the gap–labyrinth–spot sequence
  along falling rainfall, but SDF models collapse abruptly with hysteresis
  and PCF models decline smoothly, so a pattern does not say which
  collapse follows. The authors propose transplants that measure the sign
  of the net plant interaction under canopy and in bare soil, and ask for
  kernels from measured root and crown extent, which are "rarely"
  measured.
---

# LIT-tmp5mwek: Integrating theory and experiments to link local mechanisms and ecosystem-level consequences of vegetation patterns in drylands

Ricardo Martinez-Garcia, Ciro Cabal, Justin M. Calabrese, Emilio
Hernández-García, Corina E. Tarnita, Cristóbal López and Juan A. Bonachela,
*Chaos, Solitons & Fractals* 166, 112881 (2023), doi:10.1016/j.chaos.2022.112881;
arXiv:2101.07049.

## Key takeaways

*From the reading, [NOTE-tmpbqaec](../notes.d/NOTE-tmpbqaec.md).*

- **A pattern does not identify its mechanism.** The two families of
  models give "visually indistinguishable patterns" but "predict
  contrasting desertification dynamics" (abstract).
- **Competition alone is enough.** "PCF is the most parsimonious feedback
  type that generates vegetation patterns" (p. 5). Short-range
  facilitation "might be secondary actors that sharpen the boundaries of
  clusters rather than being key for the instabilities" (p. 9).
- **Collapse differs by mechanism.** PCF transitions "do not show
  bistability and do not feature hysteresis loops" (p. 11). The Rietkerk
  SDF model has a hysteresis loop. The authors leave open whether the
  difference comes from "the absence of a positive feedback or the lack
  of diffusion".
- **The kernels are unmeasured.** Their scales "are rarely parameterized
  using field measurements of root extent and crown size" (p. 9).
- **A field test.** Transplants under canopy, in bare soil, and behind
  root barriers would read the sign of the net interaction (Table 2).

## Standing in the record

Filed on 2026-11-14 as Sun et al.'s ref. 34. That paper, filed in
dmarx/nucleation#494, models shrubs and grasses with competition and
facilitation kernels, and calls its mechanism a scale-dependent feedback.
This review is the yardstick for that label: it says competition alone
makes the patterns, and that matching pattern geometry cannot identify a
mechanism. The record held nothing on vegetation pattern formation,
scale-dependent feedback or nonlocal competition. Its nearest holdings are
Turing's diffusion-driven instability ([THEORY-543](../theory.d/THEORY-543.md)), which this review's
PCF instability does without, and the transitions question [QUESTION-281](../questions.d/QUESTION-281.md).
