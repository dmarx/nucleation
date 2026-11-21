---
status: Proposed
title: 'Singularity theory''s account of phase transitions in learning as resolutions of singularities might be useful for the account of progressive, coarse-to-fine learning the exchange had built'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that singular learning theory adds nothing to the account of
  progressive learning under either reading of the suggestion: that no
  transition in learning is the network carrying out a resolution
  (reading a, CLAIM-tmp85eq8), and that representational stages, with
  local learning coefficients measured across them, coincide with no
  change in the dominant singular region and are fully accounted for by
  concentration, spectral detectability and cone geometry without
  singular geometry (reading b, CLAIM-tmpgzb8v). A transition the theory
  cannot compute for a large network does not defeat it; the claim is that
  the account might be useful, not that it is tractable everywhere.
tags:
- learning-theory
- loss-landscapes
- model-comparison
date: '2026-11-21'
line:
- learned-structure
grounds:
- THEORY-087
- THEORY-1275
- THEORY-975
- LIT-tmp3njir
- LIT-tmp0z602
- LIT-tmpv9upr
bears_on:
- QUESTION-363
- QUESTION-217
- QUESTION-tmpsy8qn
summary: >-
  The owner's U23 in the exchange "Rich Get Richer Power Laws"
  (2026-11-21), after the exchange had described progressive learning
  through concentration of measure, spectral detectability and entailment
  cones: "singularity theory has an account for phase transitions in
  learning as resolutions of singularities that might be useful here".
  The thesis and its wording are the owner's, at U23. "As resolutions of
  singularities" admits two readings that would be filed differently, and
  both are filed as alternatives for the owner to choose: (a) training
  carries out a resolution ([CLAIM-tmp85eq8](CLAIM-tmp85eq8.md)), and (b) a transition is a
  change of the dominant singularity, with resolution as the tool that
  computes its learning coefficients ([CLAIM-tmpgzb8v](CLAIM-tmpgzb8v.md), A37's reframing).
---

<!-- inactive-ok-file: LIT-tmp0z602 LIT-tmpv9upr CLAIM-tmpcbfdj CLAIM-tmp9bp04 CLAIM-tmp85eq8 CLAIM-tmpgzb8v ARG-tmpbmruy — Deferred works registered from the exchange and not yet read, or claims filed with this one -->

# CLAIM-tmpp83vc: Singularity theory's account of phase transitions in learning as resolutions of singularities might be useful for the account of progressive, coarse-to-fine learning the exchange had built

## The claim

U23, verbatim: "singularity theory has an account for phase transitions
in learning as resolutions of singularities that might be useful here".
"Here" is the exchange's account of progressive, coarse-to-fine learning,
which so far rested on concentration of measure, spectral detectability
(BBP) and entailment cones.

## Two readings, filed as alternatives

"As resolutions of singularities" can be read two ways, and they would be
filed differently, so each is filed as an alternative. The owner chooses.

- **Reading (a), training performs a resolution** ([CLAIM-tmp85eq8](CLAIM-tmp85eq8.md)): a
  phase transition is the network carrying out, or passing through, a
  blow-up of a singular point. The statement is the assistant's.
- **Reading (b), a change of the dominant singularity** ([CLAIM-tmpgzb8v](CLAIM-tmpgzb8v.md)):
  regions with different fits and learning coefficients compete in the
  free energy, the dominant one can switch as n grows, and resolution is
  how each coefficient is found. The wording is A's, at A37 §3 and §5.

The assistant's view, that the record's [CLAIM-305](CLAIM-305.md) tells against reading (a)
and leaves (b), is argued in [ARG-tmpbmruy](../arguments.d/ARG-tmpbmruy.md); it is a verdict on the
readings, not a choice between them for the owner.

## How the exchange developed it

- **Dynamics are separate.** "The fact that a singularity exists does not
  tell us when or whether gradient descent will move away from it" (A37
  §4). Plateaus near singularities are Amari's and Wei's work
  ([LIT-tmp0z602](../literature.d/LIT-tmp0z602.md), [LIT-tmpv9upr](../literature.d/LIT-tmpv9upr.md), unread). How slowly a flow leaves or
  reaches a singular point is not fixed by its learning coefficient
  ([CLAIM-tmpcbfdj](CLAIM-tmpcbfdj.md)).
- **Three transitions** (A37 §5): Bayesian (the dominant posterior region
  changes), dynamical (the optimizer's trajectory reorganizes) and
  semantic (a new distinction becomes stable and decodable). "These may
  be related, but they're not equivalent." The record holds the first two
  apart in [QUESTION-363](../questions.d/QUESTION-363.md). The third, and A43's split of the semantic event
  into encoded, stable and expressed, is added there as a dated note of
  this date.
- **A worked mechanism** in which a feature switches on at a threshold
  where the local coefficient dips from 1 to 3/4 is [CLAIM-tmp9bp04](CLAIM-tmp9bp04.md).

## A correction to A37's chart

A37 §5 illustrates the crossover with a chart captioned F_A = 0.02n +
0.3 ln n and F_B = 0.012n + 0.8 ln n. Its F_A series matches the caption.
Its F_B series does not: the chart gives F_B = 4.224, 5.708 and 18.908 at
n = 100, 200 and 1000, where the caption's formula gives 4.884, 6.639 and
17.526. Under the caption's formulas the crossover is at n ≈ 370 (solving
0.008n = 0.5 ln n), not between 200 and 300 as plotted. The assistant
checked both with `python3 -I` (`t5/check2.py`). The qualitative point
survives: the simpler region wins at small n and the richer one later.

## What it does not say

It does not say that every stage of learning is a singular transition,
nor that the Bayesian order in n is the training order in t. That bridge
is [QUESTION-363](../questions.d/QUESTION-363.md), open.
