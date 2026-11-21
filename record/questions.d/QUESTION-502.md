---
number: 502
status: Open
formerly:
- QUESTION-tmpvcusw
title: 'Do networks trained with orthogonalized updates, steepest descent in the spectral norm, learn the structure of their data in a different order from networks trained by gradient descent: is the coarse-to-fine progressive differentiation that gradient descent shows on hierarchically structured data weaker, absent or reversed?'
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-20'
line:
- learned-structure
summary: >-
  [CLAIM-774](../claims.d/CLAIM-774.md) shows that in a two-layer linear network, equalizing the
  rates of singular directions within a layer reverses and compresses the
  order in which modes are learned. Saxe and colleagues read the gradient
  descent order as progressive differentiation of a hierarchy of
  categories ([THEORY-186](../theory.d/THEORY-186.md)). Whether the reversal survives nonlinearity,
  depth, momentum and noise, and shows in networks trained with such
  updates in practice, is open.
---
<!-- inactive-ok-file: CLAIM-774 THEORY-186 — Proposed or Deferred; filed in this contribution of 2026-11-20, and the reading it qualifies -->

# QUESTION-502: Do networks trained with orthogonalized updates, steepest descent in the spectral norm, learn the structure of their data in a different order from networks trained by gradient descent: is the coarse-to-fine progressive differentiation that gradient descent shows on hierarchically structured data weaker, absent or reversed?

## What makes it open

[CLAIM-774](../claims.d/CLAIM-774.md) is a derivation for a two-layer linear network from small
weights, checked by simulation. Three things stand between it and trained
networks: nonlinearity, which couples modes; momentum, which smooths the
polar step; and the Newton–Schulz approximation to the polar factor that
practical implementations use ([LIT-2952](../literature.d/LIT-2952.md)), which does not set every
singular value exactly to one.

## What would count as an answer

A network trained on data with a known hierarchy (Saxe and colleagues'
tree-structured items, or a hierarchical generative model), once by gradient
descent and once with orthogonalized updates at matched loss, with the time at
which each level of the hierarchy is learned measured in each. Reversal,
compression, or no difference.
