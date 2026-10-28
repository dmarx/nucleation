---
number: 51
status: Open
formerly:
- QUESTION-tmp84iod
title: 'What structure does training for one classification task leave in a network''s last layers, and what does that structure cost for decisions and distributions the network was not trained on?'
version: 2
history:
- version: 2
  date: '2026-10-14'
  note: >-
    Kornblith et al. (2021), which the body named as unheld and worth
    filing, is filed as LIT-1044 and read in full (NOTE-762). The
    account filed from it, THEORY-246, is added to answered_by and to
    the list of what the record holds, with its limit, and the sentence
    calling the work unheld is replaced.
tags:
- representation-learning
- learning-theory
- information-geometry
date: '2026-10-12'
line: 'learned-structure'
answered_by:
- THEORY-104
- THEORY-085
- THEORY-286
summary: >-
  Filed in the fourth synthesis pass to give readings no question asked
  for a place in the argument. It bears on [QUESTION-010](QUESTION-010.md) and [CLAIM-164](../claims.d/CLAIM-164.md).
  [THEORY-083](../theory.d/THEORY-083.md), [THEORY-104](../theory.d/THEORY-104.md) and [THEORY-085](../theory.d/THEORY-085.md) answer it in part; the body gives
  each one's limit.
refined_by:
- QUESTION-080
- QUESTION-181
- QUESTION-192
- QUESTION-202
- QUESTION-236
bearing:
- THEORY-246
- THEORY-294
- THEORY-278
- THEORY-083
---
<!-- inactive-ok-file: THEORY-286 — Proposed; partial answers filed today, cited with their limits -->

# QUESTION-051: What structure does training for one classification task leave in a network's last layers, and what does that structure cost for decisions and distributions the network was not trained on?

## The question

Training a classifier past zero error drives its last layers toward a specific geometry, in which features collapse onto class means arranged as a simplex. The class means then dominate the curvature. The question is why training reaches this structure, and what the structure removes. The second part means: what can no longer be read from the top layers, and where in depth it can still be read.

## Why the record needs it

[QUESTION-010](QUESTION-010.md) asks whether a chain can keep what one task family needs while destroying what another needs. A trained network's layers are a chain of maps, so information about any target can only fall along them. What training adds is the choice of which information is spent. That makes these results a measured case for [QUESTION-010](QUESTION-010.md), though not an answer to it for reconstruction chains. [CLAIM-164](../claims.d/CLAIM-164.md) is touched: the class-mean span is the cluster that a spectral cut keeps.

## What the record holds

- [THEORY-083](../theory.d/THEORY-083.md): features collapse "onto their class means", toward a simplex equiangular tight frame, and the decision becomes "nearest class mean". Limit: it does not say why; balanced classes, last layer.
- [THEORY-104](../theory.d/THEORY-104.md): "in-distribution accuracy rises while out-of-distribution accuracy falls" across the last layers, so the best layer for a readout under shift "lies below the top". Limit: the layer is chosen on out-of-distribution data; the effect is weak for ViTs.
- [THEORY-085](../theory.d/THEORY-085.md): class-driven Fisher outliers "pair each class's feature mean with that class's own error mean". The class is a shared cause, and a class-blind factorization misplaces it. Limit: spectra are judged by eye on one MLP.
- [THEORY-278](../theory.d/THEORY-278.md): under MSE a trained classifier stays near the least-squares classifier for its features, and on that path a re-whitened gradient flow on unconstrained features drives the class-separation singular values to infinity at equal rates, which is collapse. Limit: MSE, unconstrained features and a modified flow, not gradient descent on cross-entropy.
- [THEORY-286](../theory.d/THEORY-286.md): under class imbalance unregularized cross-entropy prefers simplex-encoded-label interpolation, not the simplex ETF, which it is only for balanced or binary data. Limit: an endpoint for unconstrained features; it does not show that gradient descent reaches it.
- [THEORY-294](../theory.d/THEORY-294.md): lazy-regime training of a wide shallow network does not collapse its features, so collapse needs feature learning. Limit: proved for one-dimensional, two-class data; higher dimensions are measured.
- [THEORY-246](../theory.d/THEORY-246.md): among ImageNet-trained ResNet-50s, objectives that raise penultimate class separation (R² 0.349 for softmax to 0.845 for squared error) give fixed features that transfer worse to datasets with other classes (Spearman ρ = −0.93 over nine losses; mean linear transfer 75.9% to 48.3%), and the differences lie in the last few blocks, which fine-tuning rebuilds. Limit: networks early-stopped near 92% training accuracy, not in the terminal phase; one dataset and a correlation across losses, with one temperature sweep; transfer read only at the penultimate layer; for the same classes under input shift the more separated losses do slightly better, so the cost is for new classes.

The derivation for cross-entropy asked for below is still open: the held derivations are for MSE or for an endpoint, and all remove the data. For the second half the record now holds a direct measurement: Kornblith et al. (2021), [LIT-1044](../literature.d/LIT-1044.md), read in [NOTE-762](../notes.d/NOTE-762.md) and filed as [THEORY-246](../theory.d/THEORY-246.md). It measures the cost at the penultimate layer for new class partitions only, short of the terminal phase, and does not read the earlier layers, so the layer-by-layer half of what would answer it is still open.

## What would answer it

A derivation showing why gradient descent on cross-entropy reaches collapse. Alongside it, a layer-by-layer measurement relating the degree of collapse to the loss of readability for held-out tasks, with the layer not chosen on test data.
