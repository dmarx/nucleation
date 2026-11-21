---
status: Proposed
title: 'Singular learning theory''s account of phase transitions in learning, as changes in which singularity dominates, may be useful for describing how a network''s representations reorganize in stages'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A study of a network that passes through representational stages, with
  local learning coefficients measured across them, in which the stages
  coincide with no change in the dominant singular region or its
  coefficient, and are fully accounted for by an account that uses no
  singular geometry, such as the order of the data's spectral modes
  alone; or a showing that the Bayesian order SLT predicts and the order
  of training's stages are unrelated in general. A transition SLT cannot
  compute for a large network does not defeat it; the claim is that the
  account is useful, not that it is tractable everywhere.
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
rests_on:
- CLAIM-305
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
  The thesis is the owner's. The title takes the reading on which the
  record can file it: transitions as changes of the dominant singularity,
  with resolution as the tool that computes their learning coefficients
  (A37 §3; CLAIM-305). The alternative reading is set out in the body.
---

<!-- inactive-ok-file: LIT-tmp3njir LIT-tmp0z602 LIT-tmpv9upr CLAIM-tmpcbfdj CLAIM-tmp9bp04 — Deferred works registered from the exchange and not yet read, or claims filed with this one -->

# CLAIM-tmpp83vc: Singular learning theory's account of phase transitions in learning, as changes in which singularity dominates, may be useful for describing how a network's representations reorganize in stages

## The claim

U23, verbatim: "singularity theory has an account for phase transitions
in learning as resolutions of singularities that might be useful here".
"Here" is the exchange's account of progressive, coarse-to-fine learning,
which so far rested on concentration of measure, spectral detectability
(BBP) and entailment cones.

## Two readings of "as resolutions of singularities"

The ledger notes that A37 reframed the owner's wording, and that the record
must say which reading it takes. There are two.

- **(a) Training performs a resolution.** A phase transition would be the
  network passing through, or carrying out, a blow-up of a singular
  point. The record does not support this. A blow-up reparametrizes the
  states and adds no observation (CLAIM-305). A37 §3 agrees: resolution
  "doesn't mean that training literally performs an algebraic blow-up.
  Resolution is an analytical tool that reveals the structure hidden
  inside a singular parameterization."
- **(b) A transition is a change of the dominant singularity, and
  resolution computes what decides it.** This is the reading the title
  files. Regions of parameter space with different learning coefficients
  compete in the free energy F ≈ nL + λ log n − (m − 1) log log n
  (THEORY-087). As n grows, the dominant region can switch from a simpler,
  worse-fitting one to a richer one, at n(L_A − L_B) ≈ (λ_B − λ_A) log n
  (A37 §5). The record holds such Bayesian transitions in a toy model, and
  their partial agreement with SGD's order (THEORY-1275, QUESTION-363).
  Resolution is how each λ is found.

On (b), what the owner's suggestion adds to the exchange is the proposal
that the stages of representational development are such switches, or at
least leave their mark in local learning coefficients. The record holds
one reading in favour: weight-refined coefficients of attention heads
diverge by function over training (THEORY-975). Hoogland et al.
(LIT-tmp3njir, unread) report stagewise changes in the coefficient in
transformers.

## How the exchange developed it

- **Dynamics are separate.** "The fact that a singularity exists does not
  tell us when or whether gradient descent will move away from it" (A37
  §4). Plateaus near singularities are Amari's and Wei's work
  (LIT-tmp0z602, LIT-tmpv9upr, unread). How slowly a flow leaves or
  reaches a singular point is not fixed by its learning coefficient
  (CLAIM-tmpcbfdj).
- **Three transitions** (A37 §5): Bayesian (the dominant posterior region
  changes), dynamical (the optimizer's trajectory reorganizes) and
  semantic (a new distinction becomes stable and decodable). "These may
  be related, but they're not equivalent." The record holds the first two
  apart in QUESTION-363. The third, and A43's split of the semantic event
  into encoded, stable and expressed, is added there as a dated note of
  this date.
- **A worked mechanism** in which a feature switches on at a threshold
  where the local coefficient dips from 1 to 3/4 is CLAIM-tmp9bp04.

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
is QUESTION-363, open.
