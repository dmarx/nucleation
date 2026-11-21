---
status: Proposed
title: "Alternative reading (b) of the owner's suggestion on singularities: a phase transition in learning is a change in which singular region of parameter space dominates, as the sample size grows, between regions that fit differently and have different learning coefficients, and resolution of singularities is the tool that computes those coefficients"
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A study of a network that passes through representational stages, with
  local learning coefficients measured across them, in which the stages
  coincide with no change in the dominant singular region or its
  coefficient and are fully accounted for by an account that uses no
  singular geometry, such as the order of the data's spectral modes
  alone; or a showing that the Bayesian order in sample size and the
  order of training's stages are unrelated in general. A transition the
  theory cannot compute for a large network does not defeat it; the claim
  is that the account is useful, not that it is tractable everywhere.
tags:
- learning-theory
- loss-landscapes
- model-comparison
date: '2026-11-21'
line:
- learned-structure
rests_on:
- CLAIM-305
grounds:
- THEORY-087
- THEORY-1275
- THEORY-975
- LIT-tmp3njir
bears_on:
- QUESTION-363
- QUESTION-217
- QUESTION-tmpsy8qn
summary: >-
  One of two alternative readings of the owner's U23 in the exchange "Rich
  Get Richer Power Laws" ([CLAIM-tmpp83vc](CLAIM-tmpp83vc.md)): "singularity theory has an
  account for phase transitions in learning as resolutions of
  singularities that might be useful here". This is reading (b), the
  reframing A gave in reply: transitions are changes of the dominant
  singularity, and resolution is how their learning coefficients are
  found. The other is reading (a), [CLAIM-tmp85eq8](CLAIM-tmp85eq8.md), the owner's words taken
  literally. The owner chooses. The wording is A's (the other assistant in
  the exchange "Rich Get Richer Power Laws", A37); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpp83vc CLAIM-tmp85eq8 ARG-tmpbmruy LIT-tmp3njir — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21, or a Deferred work registered from it and not yet read -->

# CLAIM-tmpgzb8v: Alternative reading (b) of the owner's suggestion on singularities: a phase transition in learning is a change in which singular region of parameter space dominates, as the sample size grows, between regions that fit differently and have different learning coefficients, and resolution of singularities is the tool that computes those coefficients

**This is reading (b) of [CLAIM-tmpp83vc](CLAIM-tmpp83vc.md), the owner's U23, one of two
alternatives.** The other, reading (a), is [CLAIM-tmp85eq8](CLAIM-tmp85eq8.md). The owner
chooses.

## The claim

A37 reframes the owner's "as resolutions of singularities". Resolution, at
A37 §3, "doesn't mean that training literally performs an algebraic
blow-up. Resolution is an analytical tool that reveals the structure hidden
inside a singular parameterization": it brings the loss to a normal form
from which the learning coefficient λ and its multiplicity m are read
([CLAIM-305](CLAIM-305.md): "what the resolution buys is a normal form for the divergence,
and so the learning coefficient").

The transition is then a competition. Regions of parameter space with
different fits and different learning coefficients contribute free
energies F ≈ nL + λ log n − (m − 1) log log n (A37 §5; [THEORY-087](../theory.d/THEORY-087.md)). A
simpler region with worse fit and smaller λ can dominate at small n and a
richer one later, with the crossover where "n(L_A − L_B) ≈ (λ_B − λ_A) log
n" (A37 §5). "At that point, the dominant contribution to the Bayesian
posterior can switch between different representational structures." The
record holds such Bayesian transitions in a toy model, and their partial
agreement with SGD's order ([THEORY-1275](../theory.d/THEORY-1275.md), [QUESTION-363](../questions.d/QUESTION-363.md)).

On this reading the owner's suggestion proposes that the stages of
representational development are such switches, or at least leave their
mark in local learning coefficients. The record holds one reading in
favour: weight-refined coefficients of attention heads diverge by function
over training ([THEORY-975](../theory.d/THEORY-975.md)). Hoogland and colleagues ([LIT-tmp3njir](../literature.d/LIT-tmp3njir.md),
Deferred: registered, not read) report stagewise changes in the coefficient
in transformers.

## What it does not say

- Not that the Bayesian order in n is the training order in t. A37 §5
  keeps three transitions apart, Bayesian, dynamical and semantic: "These
  may be related, but they're not equivalent." The bridge is
  [QUESTION-363](../questions.d/QUESTION-363.md), open.
- Not that every stage of learning is a singular transition.
- Not that it is the owner's meaning. It is A's reframing of the owner's
  words; reading (a) keeps them literal. [ARG-tmpbmruy](../arguments.d/ARG-tmpbmruy.md) gives the
  assistant's reason to prefer (b), which the owner may not share.
