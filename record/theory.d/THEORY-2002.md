---
number: 2002
status: Proposed
formerly:
- THEORY-tmp17fdp
title: 'Structure learning''s problem is generating models'
statement: >-
  Neacsu and colleagues argue that, within active inference, structure
  learning is Bayesian model selection by model evidence over a supplied set
  of alternative models, done offline by refitting or by Bayesian model
  reduction or expansion, and that its open problem is not choosing among
  the alternatives but generating them
version: 1
source:
- LIT-2835
tags:
- neuroscience
- philosophy-of-science
date: '2026-11-19'
promote_when: >-
  A second reading of the review (§§3.3–3.4 and 4.2) confirming that it
  defines Structure Learning as offline Bayesian model selection by model
  evidence, in two flavours (refitting; reduction or expansion), and names
  the generation of the hypothesis space as the open problem.
summary: >-
  From the reading of [LIT-2835](../literature.d/LIT-2835.md) in [NOTE-2092](../notes.d/NOTE-2092.md). Neacsu, So, Rutar, da
  Costa, Adams and Friston (2026), Minds and Machines 36:33, DOI
  10.1007/s11023-026-09787-8 (open access). A conceptual review. It
  surveys what "structure learning" means across developmental, cognitive
  and machine-learning work, then defines Structure Learning in active
  inference as offline Bayesian model selection by model evidence, by
  refitting or by Bayesian model reduction or expansion. It names the open
  problem as generating the hypothesis space, not choosing within it. It
  reports no results. Here because the exchange called it the most useful
  single paper for what the free-energy literature covers. It maps that
  literature fairly but leaves active, data-choosing structure learning to
  [LIT-2815](../literature.d/LIT-2815.md). It agrees with [THEORY-564](THEORY-564.md)'s framing that reduction, not
  expansion, is the open half. Read in its NOTE (skimmed in part).
---
<!-- inactive-ok-file: THEORY-564 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: NOTE-2092 — Skimmed; cited in this filing of 2026-11-19 -->

# THEORY-2002: Structure learning's problem is generating models

## The account

The review separates three levels of free-energy optimisation: inference about states, parametric (Dirichlet, Hebbian-like) learning, and structure learning. It identifies the last with Bayesian model selection by model evidence, done offline either by refitting a model under alternative priors (phenotyping) or by Bayesian model reduction or expansion of accumulated posteriors (synthetic agents). The general literature's many "structure learning" phenomena fall at different levels. Statistical learning and online adaptive generalisation, for instance, need not be structure learning. The authors take the framework's open problem to be where the alternative hypotheses come from. They suggest generating them by grammar-like transformations of a parent model, constrained by neural architecture.

## What it does not show

- No result that structure learning in active inference recovers true structure at any rate. It is a definitional and interpretive review.
- Nothing on choosing data to learn structure. Active selection by model information gain is [LIT-2815](../literature.d/LIT-2815.md)'s contribution.
- The integrative mapping of phenomena onto levels is argued, not tested.
