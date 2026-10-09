---
number: 125
status: Proposed
formerly:
- CLAIM-tmpnyfix
title: 'Directed transport between empirical models whose covers change has two open problems: when it preserves decision-relevant information, and how it extends to signalling data'
version: 1
role: thesis
defeated_if: >-
  An existing framework characterizes, for stochastic maps between
  empirical models with different covers, when they preserve
  decision-relevant information (an informativeness order such as
  Blackwell's, relative to a stated family of decisions), and extends that
  characterization, or the classification of classical transports, to
  signalling data.
tags:
- contextuality
- mathematics
date: '2026-10-09'
line: pragmatic-transport
rests_on:
- CLAIM-121
- CLAIM-070
grounds:
- THEORY-174
- LIT-846
- LIT-847
- LIT-845
- THEORY-156
supersedes:
- CLAIM-100
summary: >-
  [CLAIM-100](CLAIM-100.md) narrowed. Simulations between empirical models already give
  directed stochastic transport between scenarios whose covers change,
  and settle when it preserves global compatibility. What is left open is
  decision-relevant information and signalling data.
---
<!-- inactive-ok-file: THEORY-174 THEORY-156 — Proposed; cited as readings the claim stands on, not as settled -->
<!-- inactive-ok-file: CLAIM-001 — Proposed; open, and cited as the objection the superseded claim drew -->
<!-- inactive-ok-file: CLAIM-100 — Superseded; replaced, and cited as the history this entry narrows -->

# CLAIM-125: Directed transport between empirical models whose covers change has two open problems: when it preserves decision-relevant information, and how it extends to signalling data

## The claim

[CLAIM-100](CLAIM-100.md) posed the extension of sheaf-theoretic contextuality to directed
transport between observational scenarios whose covers change as the open
mathematical problem. It took that problem from A93's research opportunity
and A94's bridge question: "Under what conditions can a directed stochastic
transport preserve the decision-relevant information of a context-indexed
empirical model while changing its observational cover or global
compatibility structure?"

Half of that question is answered. Simulations between empirical models map
each target measurement to a jointly measurable set of source measurements,
so they are directed, stochastic and free to change the cover:

- Karvonen 2018 ([LIT-846](../literature.d/LIT-846.md)) builds the category of empirical models;
- Abramsky, Barbosa, Karvonen and Mansfield 2019 ([LIT-847](../literature.d/LIT-847.md)) give simulations
  as morphisms of a comonad;
- Barbosa, Karvonen and Mansfield, "Closing Bell" ([LIT-845](../literature.d/LIT-845.md)), characterise
  in Theorem 44, as corrected in arXiv v2, exactly which maps between model
  sets are classical transports.

Such transports preserve noncontextuality and cannot raise the noncontextual
fraction ([THEORY-174](../theory.d/THEORY-174.md)). The manuscript's Propositions 1 and 2 ([CLAIM-121](CLAIM-121.md),
[CLAIM-070](CLAIM-070.md)) are special cases of Karvonen's natural transformations.

Two parts remain open, and they are this claim:

1. **Decision-relevant information.** None of these works compares source
   and target models by what they let a decision-maker do. The comparison
   the bridge question asks for is an informativeness order in Blackwell's
   sense ([THEORY-156](../theory.d/THEORY-156.md)), relative to a family of decisions, taken across a
   change of cover. When a classical or contextual transport preserves that
   order is not addressed.
2. **Signalling data.** All three works assume no-signalling models: their
   compatibility condition generalises no-signalling. Pragmatic judgements
   need not satisfy it. Contextuality-by-Default ([LIT-777](../literature.d/LIT-777.md)) treats
   inconsistently connected systems within one scenario, but not transport
   between scenarios.

## What it does not say

It does not say the global-compatibility problem is open: for no-signalling
models and non-adaptive procedures it is settled. It does not say that
diffusion or any other practice fails to transport meaning; [CLAIM-001](CLAIM-001.md)'s
objection was to [CLAIM-100](CLAIM-100.md) and concerned covers, which this claim no longer
holds open. Nor does it say the two open parts are hard. It says only that
the literature read here does not settle them.

## Prior art

The simulations works above come first. Gogioso and Pinzani's topology and
geometry of causality ([LIT-808](../literature.d/LIT-808.md), [LIT-788](../literature.d/LIT-788.md)) define empirical models on any
open cover, with a lattice of covers and restriction to finer ones, but
within one family of spaces rather than as transport between scenarios.
