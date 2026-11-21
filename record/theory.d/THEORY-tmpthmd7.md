---
status: Proposed
title: 'Song, Ahn and Yun find that in small-learning-rate SGD on small MLP, CNN and Transformer classifiers the stochastic gradient lies mostly in the span of the training-loss Hessian''s top-k eigenvectors, k the number of classes, yet projecting each update onto that span stops the training loss falling while projecting it onto the complement trains as fast as SGD; the alignment comes from gradient noise across a steep valley, or from self-stabilizing oscillation at the Edge of Stability, and vanishes under small-step full-batch gradient descent'
promote_when: >-
  An independent study, on at least one architecture or dataset not in the
  paper, finds that top-k-projected SGD stalls while complement-projected
  SGD keeps pace with SGD, and that the top-k alignment of the gradient
  disappears under full-batch gradient descent at the same small learning
  rate.
version: 1
tags:
- loss-landscapes
- learning-theory
date: '2026-11-21'
source:
- LIT-2973
corroborates:
- CLAIM-835
summary: >-
  Song, Ahn and Yun, [LIT-2973](../literature.d/LIT-2973.md), read in [NOTE-tmpw0eql](../notes.d/NOTE-tmpw0eql.md). Gradient alignment
  with the dominant Hessian subspace is not where training happens: the
  loss falls along a steep valley's flat floor, in the complement of the
  top k. A weak instance of a model's rankings of directions disagreeing
  ([CLAIM-835](../claims.d/CLAIM-835.md)), within one metric.
---
<!-- inactive-ok-file: CLAIM-835 TERM-137 THEORY-078 ARG-139 — Proposed or new; the reading this account comes from and the claim it bears on -->

# THEORY-tmpthmd7: Song, Ahn and Yun find that in small-learning-rate SGD on small MLP, CNN and Transformer classifiers the stochastic gradient lies mostly in the span of the training-loss Hessian's top-k eigenvectors, k the number of classes, yet projecting each update onto that span stops the training loss falling while projecting it onto the complement trains as fast as SGD; the alignment comes from gradient noise across a steep valley, or from self-stabilizing oscillation at the Edge of Stability, and vanishes under small-step full-batch gradient descent

## Source

Song, Ahn and Yun, "Does SGD really happen in tiny subspaces?", ICLR 2025,
[LIT-2973](../literature.d/LIT-2973.md), read from the arXiv e-print 2405.16002 in [NOTE-tmpw0eql](../notes.d/NOTE-tmpw0eql.md).

## What was actually shown

- Dom-SGD "fails to further decrease the training loss"; Bulk-SGD "is as
  effective as SGD in decreasing the training loss" (§§3.2–3.3), on
  MNIST-5k, CIFAR10-5k and SST2-1k, from a switch at mid-training.
- Under full-batch GD in the small-step regime the "alignment disappears
  as soon as we switch to GD" (§4.1); smaller batches and injected noise
  raise it.
- At the Edge of Stability, and with SAM, the projected variants behave
  the same way (§5).
- The mechanism, a valley "steep along the dominant subspace and flat
  along the bulk subspace" whose floor descends along the bulk (§4.3), is
  "one plausible explanation", supported by a two-dimensional toy and by
  how far the weights move.

What could have failed: Dom-SGD could have trained, or Bulk-SGD stalled,
or the alignment survived full-batch descent; none did, in the runs shown.

## What this does not say

- Not that small-curvature directions are "important" in a ranking: the
  bulk is the whole complement of the top k, and the result is a dynamical
  one, the stiff directions having reached their floor.
- Nothing about representations, features or decodability; "learning" is
  training-loss descent.
- Not tested at scale, nor with learning-rate schedules.

## Connections

[CLAIM-835](../claims.d/CLAIM-835.md) (weak corroboration, within one metric; [ARG-139](../arguments.d/ARG-139.md)). [TERM-137](../terms.d/TERM-137.md)'s
sense 3. [THEORY-731](THEORY-731.md) and [THEORY-078](THEORY-078.md) say what spans the dominant subspace.
[THEORY-082](THEORY-082.md): momentum and Adam raising the bulk step is a change of the
metric of descent.
