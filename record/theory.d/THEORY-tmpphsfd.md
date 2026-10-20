---
status: Proposed
promote_when: >-
  A direct measurement of the maps between independently trained latent
  spaces, on the encoders and data where anchor-based transfer has been
  shown: the residual of the best orthogonal-times-scalar map (orthogonal
  Procrustes on normalised embeddings) against the residual of the best
  general linear map, on held-out samples, together with stitched
  performance. The account is promoted if the conformal residual is close to
  the linear one where stitching works and the gap grows where it fails
  (cross-architecture, distant languages, an anchor count below the latent
  width). It is refuted if stitching through cosine profiles succeeds where
  the best conformal map leaves a large residual that a linear map removes,
  or fails where the conformal residual is small and the anchors cover the
  data. More stitching tables of the kind the source reports cannot settle
  it, since they do not separate distortion from anchor coverage.
title: 'Independently trained neural encoders of the same data learn latent spaces that differ mainly by an angle-preserving map, a rotation or reflection times a rescaling, so their cosine similarities to shared anchor samples agree across seeds, architectures and languages, as Moschella et al. propose'
version: 1
tags:
- representation-learning
- anthology-candidate
date: '2026-10-20'
source:
- LIT-849
extends:
- THEORY-175
summary: >-
  Moschella, Maiorca, Fumero, Norelli, Locatello & Rodolà (2022; ICLR 2023),
  [LIT-849](../literature.d/LIT-849.md), read in [NOTE-652](../notes.d/NOTE-652.md). The hypothesis behind relative representations,
  filed apart from what their experiments measured ([THEORY-175](THEORY-175.md)) under
  [ADR-047](../decisions.d/ADR-047.md) v4. The source assumes it and tests it only through its
  consequences; it never fits a map between two spaces.
---

# THEORY-tmpphsfd: Independently trained neural encoders of the same data learn latent spaces that differ mainly by an angle-preserving map, a rotation or reflection times a rescaling, so their cosine similarities to shared anchor samples agree across seeds, architectures and languages, as Moschella et al. propose

## Source

Moschella, Maiorca, Fumero, Norelli, Locatello & Rodolà (2022; ICLR 2023),
[LIT-849](../literature.d/LIT-849.md), read in [NOTE-652](../notes.d/NOTE-652.md). The hypothesis is the paper's motivation (§1,
§3): that the latent spaces of networks trained on the same data differ, up
to training noise, by transformations that preserve angles, so that a
representation built from cosines to anchors is shared between them.

## What is asserted

That the difference between two independently trained latent spaces is
mainly an angle-preserving map: an orthogonal map times a positive scalar,
the class under which cosine profiles to anchors are exactly invariant. If
it holds, cosine profiles to matched anchors agree across seeds,
architectures and, with parallel anchors, languages, and a decoder trained
on one encoder's profiles reads another's.

## What the record holds toward it

[THEORY-175](THEORY-175.md), which is Active, holds the exact invariance class and what the
experiments measured: relative vectors agreeing at cosine 0.86–0.97,
untrained decoders transferring with loss, and nearest-neighbour overlap of
only 0.10–0.39. That evidence fits "approximately angle-preserving, with
distortion large enough to scramble most neighbours". It is a consequence
the hypothesis predicts, and one that a larger, non-conformal difference
with good anchor coverage could also produce.

## What this does not say

- That the residual difference is small in any stated norm. The source
  reports no residual.
- That transfer needs no correspondence. The anchors are paired samples.
- That cosine is identified where a representation is fixed only up to an
  invertible linear map ([THEORY-018](THEORY-018.md)).

## What would confirm or reject it

The promote_when: a fitted conformal map and a fitted linear map between
two trained spaces, with held-out residuals, set against stitched
performance. [QUESTION-211](../questions.d/QUESTION-211.md) asks the same.
