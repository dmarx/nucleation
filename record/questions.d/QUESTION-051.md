---
number: 51
status: Open
formerly:
- QUESTION-tmp84iod
title: 'What structure does training for one classification task leave in a network''s last layers, and what does that structure cost for decisions and distributions the network was not trained on?'
version: 1
tags:
- representation-learning
- learning-theory
- information-geometry
date: '2026-10-12'
line: 'learned-structure'
answered_by:
- THEORY-083
- THEORY-104
- THEORY-085
summary: >-
  Filed in the fourth synthesis pass to give readings no question asked
  for a place in the argument. It bears on [QUESTION-010](QUESTION-010.md) and [CLAIM-164](../claims.d/CLAIM-164.md).
  [THEORY-083](../theory.d/THEORY-083.md), [THEORY-104](../theory.d/THEORY-104.md) and [THEORY-085](../theory.d/THEORY-085.md) answer it in part; the body gives
  each one's limit.
refined_by:
- QUESTION-tmpexxzn
---

# QUESTION-051: What structure does training for one classification task leave in a network's last layers, and what does that structure cost for decisions and distributions the network was not trained on?

## The question

Training a classifier past zero error drives its last layers toward a specific geometry, in which features collapse onto class means arranged as a simplex. The class means then dominate the curvature. The question is why training reaches this structure, and what the structure removes. The second part means: what can no longer be read from the top layers, and where in depth it can still be read.

## Why the record needs it

[QUESTION-010](QUESTION-010.md) asks whether a chain can keep what one task family needs while destroying what another needs. A trained network's layers are a chain of maps, so information about any target can only fall along them. What training adds is the choice of which information is spent. That makes these results a measured case for [QUESTION-010](QUESTION-010.md), though not an answer to it for reconstruction chains. [CLAIM-164](../claims.d/CLAIM-164.md) is touched: the class-mean span is the cluster that a spectral cut keeps.

## What the record holds

- [THEORY-083](../theory.d/THEORY-083.md): features collapse "onto their class means", toward a simplex equiangular tight frame, and the decision becomes "nearest class mean". Limit: it does not say why; balanced classes, last layer.
- [THEORY-104](../theory.d/THEORY-104.md): "in-distribution accuracy rises while out-of-distribution accuracy falls" across the last layers, so the best layer for a readout under shift "lies below the top". Limit: the layer is chosen on out-of-distribution data; the effect is weak for ViTs.
- [THEORY-085](../theory.d/THEORY-085.md): class-driven Fisher outliers "pair each class's feature mean with that class's own error mean". The class is a shared cause, and a class-blind factorization misplaces it. Limit: spectra are judged by eye on one MLP.

## What would answer it

A derivation showing why gradient descent on cross-entropy reaches collapse. Alongside it, a layer-by-layer measurement relating the degree of collapse to the loss of readability for held-out tasks, with the layer not chosen on test data.
