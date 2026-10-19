---
status: Open
title: "In hyperbolic neural networks on tree-like data, does the advantage over Euclidean networks go with the Möbius bias translations and the distance-based output layer, the only operations through which curvature acts, or do networks without them keep it?"
version: 1
tags:
- representation-learning
date: '2026-10-19'
line: 'learned-structure'
refines:
- QUESTION-025
summary: >-
  The promotion condition formerly on [THEORY-566](../theory.d/THEORY-566.md), moved here unchanged when
  [THEORY-566](../theory.d/THEORY-566.md) was promoted on 2026-10-19 on its structural claim. That the
  curvature of Ganea et al.'s networks acts only through two operations is
  settled; whether their gains on tree-like data come from those two
  operations is untested, since no ablation removes either.
---

# QUESTION-tmpa5vf9: In hyperbolic neural networks on tree-like data, does the advantage over Euclidean networks go with the Möbius bias translations and the distance-based output layer, the only operations through which curvature acts, or do networks without them keep it?

## Why it is a question

[THEORY-566](../theory.d/THEORY-566.md), promoted on 2026-10-19, holds a structural fact about Ganea,
Bécigneul and Hofmann's hyperbolic networks ([LIT-879](../literature.d/LIT-879.md)): lifted linear maps
and nonlinearities compose to a Euclidean composition read through the
chart at the origin, so the curvature acts only through the Möbius bias
translations and the distance-based output layer. Until that date
[THEORY-566](../theory.d/THEORY-566.md)'s promote_when asked for an ablation tying the networks' gains
to those two operations, which the title does not claim and the body
disclaims. At the owner's direction, from the promotion audit's batch 027
([ADR-047](../decisions.d/ADR-047.md)), the THEORY was promoted on the structural claim, and the
condition moved here unchanged.

It is open because the paper's comparisons are of whole hyperbolic and
Euclidean networks, at dimension 5, with best-of-three runs, on one
synthetic task whose tree-likeness is not measured and on embeddings fitted
to the hierarchy being classified ([NOTE-686](../notes.d/NOTE-686.md)). It refines [QUESTION-025](QUESTION-025.md),
which lists encodings of hierarchy.

## What would answer it

The condition formerly on [THEORY-566](../theory.d/THEORY-566.md), unchanged: an ablation on tree-like
data that removes, in turn, the Möbius bias translations and the
distance-based hyperbolic output layer from Ganea et al.'s networks, with
several seeds and a measure of the data's tree-likeness. The account that
the curvature matters through those operations is supported if the
advantage over Euclidean networks goes with them, and refuted if networks
without them keep it. More benchmark comparisons of whole hyperbolic and
Euclidean networks cannot settle it.
