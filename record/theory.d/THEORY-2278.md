---
number: 2278
status: Proposed
formerly:
- THEORY-tmp1pfm4
promote_when: >-
  A reading of the paper's figures confirms the melting peaks the text
  reports for the small origamis (B1 at 48.5 °C alone and 51.5 °C with B2
  in the outer position, 41.5 °C and 50 °C in the inner, B1m from 67 °C to
  72 °C), and an independent measurement, by another group or readout, of
  a DNA construction with at least two staples finds a staple's melting
  temperature higher when a neighbouring staple is already bound than
  when it is absent. Not met by a model fit of large origamis alone, which
  is how the paper reaches them.
title: 'Staple folding is cooperative in DNA origami'
statement: >-
  Arbona, Aimé and Elezgaray find, by UV-absorption melting of three-strand
  DNA constructions, that a staple's melting peak rises by 1.5 to 8.5 °C
  when a neighbouring staple is already folded and that the inner crossover
  position costs more than the outer, and that a local-equilibrium model
  with neighbour-dependent crossover penalties and no misfolds reproduces
  the annealing–melting hysteresis of four origamis of about 200 staples
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23 from the reading NOTE-2393
    (text and captions in full, figure images not read).
tags:
- natural-sciences
- thermodynamics
- complex-systems
date: '2026-11-23'
source:
- LIT-3148
bears_on:
- QUESTION-380
summary: >-
  In "small origamis" of one 64-base scaffold and two staples, a staple's
  melting peak rises when the other is folded (48.5 to 51.5 °C outer, 41.5
  to 50 °C inner, 67 to 72 °C and +1.5 °C for a second pair), and the inner
  position, where the path between a crossover's ends runs through the
  staple, costs more than the bulge-forming outer one. A model of local
  equilibria conditioned on bound neighbours, with a strong-correlation
  closure and no misfolds or kinetics, fits the annealing and melting
  curves and the hysteresis (4 to 10 K) of four rectangular M13 origamis.
---

# THEORY-2278: Staple folding is cooperative in DNA origami

Arbona, Aimé and Elezgaray (2013; arXiv 2011), [LIT-3148](../literature.d/LIT-3148.md), read in [NOTE-2393](../notes.d/NOTE-2393.md).

## The finding

Three staple configurations on one scaffold, melted with and without the
partner staple, by UV absorption. The partner can only have helped or not
helped; that it helps in all four comparisons, and by more in the inner
position (8.5 °C) than the outer (3 °C), could have come out otherwise.
The model, fitted on these constructions, is then applied to four large
origamis whose annealing and melting curves, and the size of the
hysteresis between them, it reproduces. The authors' reading: "the folding
of each staple is strongly dependent on the existence of a nearby cluster
of folded staples", and high-GC staples act as "initial nuclei".

## What it does not show

- **That nuclei can hurt.** Misfolded configurations are excluded by
  hypothesis, so in the model a bound neighbour can only help; nothing here
  bears on a nucleus that lowers the chance of the target.
- **Staple-resolved coupling in a large origami.** Coupling is measured
  between two staples; for 200 staples it is a model term that improves a
  fit of bulk curves.
- **Kinetics.** The model is local equilibrium at each temperature step;
  the hysteresis is put down to neighbourhoods differing between the ramps,
  not to trapping.
