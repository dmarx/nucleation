---
number: 211
status: Open
formerly:
- QUESTION-tmpqgnk6
title: 'How far are independently trained latent spaces from a cosine-preserving map: is the held-out residual of the best orthogonal-times-scalar map close to that of the best linear map where anchor-based stitching works, and does the gap grow where it fails?'
version: 1
tags:
- representation-learning
date: '2026-10-20'
line: 'pragmatic-transport'
summary: >-
  The promotion condition formerly on [THEORY-175](../theory.d/THEORY-175.md). [THEORY-175](../theory.d/THEORY-175.md) was promoted
  on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v3) on its invariance, re-derived, and on what
  Moschella et al. measured: independently trained encoders agree in
  their cosine profiles to matched anchors only approximately, enough for
  untrained decoder transfer with loss, while their nearest neighbours
  mostly differ. The source never fits a map between two spaces.
---

# QUESTION-211: How far are independently trained latent spaces from a cosine-preserving map: is the held-out residual of the best orthogonal-times-scalar map close to that of the best linear map where anchor-based stitching works, and does the gap grow where it fails?

## Why it is a question

[THEORY-175](../theory.d/THEORY-175.md) says relative representations are blind to exactly the maps
that preserve cosines to the anchors, and that trained encoders agree in
them only approximately. It does not say how far trained spaces are from
such a map, since the source reports no residual. Whether stitching works
because the spaces nearly differ by an orthogonal map times a scalar, or
because the anchors cover the data, the evidence does not separate. Until
2026-10-20 this was [THEORY-175](../theory.d/THEORY-175.md)'s promote_when.

## What would answer it

- On the encoders and data where anchor-based transfer has been shown, the
  held-out residual of orthogonal Procrustes on normalised embeddings
  against that of the best general linear map, reported with stitched
  performance.
- The comparison across the conditions where stitching weakens
  (cross-architecture, distant languages, fewer anchors than latent
  dimensions).

What would not answer it: more stitching tables of the kind the source
reports. They do not separate distortion from anchor coverage.
