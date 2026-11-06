---
number: 1446
status: Active
formerly:
- THEORY-tmpcfriw
title: 'Majikes and colleagues find, across 34 designs of one 2D DNA origami rectangle annealed under deliberately poor conditions and scored by AFM classification, that defectivity tracks design-level aggregates: the skew of the distribution of loop-entropy penalties each fold would pay if it bound first and the measured melt temperature are its principal correlates, a linear combination of these with a staple-blocking metric collapses 28 of the designs onto one trend, and designs with more short folds at the expense of medium folds are more defective'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted at the status review's ruling (the owner
    delegated these rulings), under ADR-065: the title reports what
    Majikes and colleagues find for one shape, and NOTE-1639 reads the
    version of record in full. The collapse is narrowed to the 28
    designs it was fitted on (ADR-047 kind 3). The old title was
    'Majikes and colleagues find, across 34 designs of one 2D DNA
    origami rectangle annealed under deliberately poor conditions and
    scored by AFM classification, that defectivity tracks design-level
    aggregates: the skew of the distribution of loop-entropy penalties
    each fold would pay if it bound first and the measured melt
    temperature are its principal correlates, a linear combination of
    these with a staple-blocking metric collapses it onto one trend, and
    designs with more short folds at the expense of medium folds are
    more defective'. The condition asked for an independent study, and
    it moves unchanged to QUESTION-410, which lists it under this
    entry's code; this entry bears_on it: 'An independent study of
    several designs of one DNA origami shape, under its own anneal
    conditions and quality measure, finds defectivity or yield ordered
    by the skew of the first-fold loop-entropy penalty distribution (or
    an equivalent fold-distance metric) together with melt temperature,
    and finds a design that adds short folds at the expense of medium
    ones performing worse.'
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
source:
- LIT-2127
bears_on:
- QUESTION-410
summary: >-
  Majikes, Hasni, Haridas, Robertson, Pintar, Zwolak and Liddle (2026),
  [LIT-2127](../literature.d/LIT-2127.md), read in [NOTE-1639](../notes.d/NOTE-1639.md). Defectivity is a class-weighted AFM
  proxy for missing or blocked staples, useful for comparison only; the
  combination is fitted on 28 designs of one shape, with linear models,
  and a LASSO over more metrics swaps the blocking term for positive
  inter-domain cooperativity. The poor-anneal conditions are argued, in
  supplementary sections not read here, to preserve the ordering seen
  under standard anneals. The authors' reading that 2D origami assembly is
  funnel-like rather than path-like is their interpretation of the fit.
---

# THEORY-1446: Majikes and colleagues find, across 34 designs of one 2D DNA origami rectangle annealed under deliberately poor conditions and scored by AFM classification, that defectivity tracks design-level aggregates: the skew of the distribution of loop-entropy penalties each fold would pay if it bound first and the measured melt temperature are its principal correlates, a linear combination of these with a staple-blocking metric collapses 28 of the designs onto one trend, and designs with more short folds at the expense of medium folds are more defective

## Source

Majikes, Hasni, Haridas, Robertson, Pintar, Zwolak and Liddle (2026),
[LIT-2127](../literature.d/LIT-2127.md); read in [NOTE-1639](../notes.d/NOTE-1639.md).

## What was actually shown

- **The survey**: 34 designs of one rectangle (routings, seams, sequence
  rotations, staple motifs, lattices), each annealed at 0.375 nM scaffold
  and 5x staples from 80 °C to 4 °C in 45 min, imaged by liquid AFM and
  classed by eye; defectivity φ from about 10 to 35, with staple-pool
  variation ±2.8 the largest uncertainty.
- **Correlates**: φ falls with the skew of the first-fold loop-entropy
  penalty distribution and with measured melt and anneal temperatures.
- **Collapse** (Fig. 7): Tm, skew and blocking at "roughly equivalent
  weights of 33%, 32%, and 35%" order 28 designs on one trend.
- **Short folds hurt**: the design rotated to maximize short folds (skew
  −1.6) "performs objectively worse" than the original (skew 1.0).
- **Could have come out otherwise**: the metrics could have failed to
  order the designs, or more short folds, more nucleation points, could
  have helped.

## What this does not say

- That φ counts missing staples: it is "a very approximate substitute".
- That the trend holds for other shapes, 3D designs or standard anneals:
  one 2D shape, and the transfer rests on supplementary checks not read.
- That blocking is established as a principal factor: the LASSO prefers
  positive inter-domain cooperativity.
- That pathways do not matter: "funnel-like" is the authors' reading of an
  aggregate fit, not a test against pathway models.
