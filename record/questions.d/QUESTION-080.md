---
number: 80
status: Open
formerly:
- QUESTION-tmpexxzn
title: 'When a trained network''s parameters keep moving after its loss has converged, what about the network stays fixed, and is the last-layer geometry of neural collapse among the things that do?'
version: 1
tags:
- learning-theory
- loss-landscapes
- representation-learning
date: '2026-10-13'
line: learned-structure
refines:
- QUESTION-051
summary: >-
  The record holds two pictures of the end of training. In one, the last
  layer converges to a fixed geometry through the terminal phase
  ([THEORY-083](../theory.d/THEORY-083.md), neural collapse). In the other, the parameters never stop:
  they sample a stationary distribution at constant speed ([THEORY-209](../theory.d/THEORY-209.md)).
  The two may describe different regimes. The terminal phase of neural
  collapse is cross-entropy training past zero error, with no finite
  minimum, while the limiting dynamics assume a quadratic minimum.
  Nothing in the record relates them. Drawn by the assistant from the
  reading of Kunin et al., and filed at the owner's request.
bearing:
- THEORY-211
---
<!-- inactive-ok-file: THEORY-083 THEORY-209 THEORY-085 THEORY-210 THEORY-286 — Proposed; the two pictures of the end of training and the readings that bear on relating them, open -->

# QUESTION-080: When a trained network's parameters keep moving after its loss has converged, what about the network stays fixed, and is the last-layer geometry of neural collapse among the things that do?

## The question

[THEORY-083](../theory.d/THEORY-083.md) (Papyan, Han & Donoho) says that through the terminal phase of
training a classifier's last-layer features collapse onto their class
means, which converge to a simplex equiangular tight frame. Its own
summary says "the dynamics are unexplained". [THEORY-209](../theory.d/THEORY-209.md) (Kunin et al.)
says that a converged network is not at a point. It keeps moving at a
constant speed, sampling a stationary distribution whose shape the
optimizer sets.

Both are accounts of what training leaves once it has converged. The
question is what is fixed while the parameters move: the function, the
features, the last-layer geometry, or only the loss.

## Why the record needs it

[QUESTION-051](QUESTION-051.md) asks what structure training for one task leaves in the last
layers. If neural collapse is a fixed point of the features while the
parameters keep diffusing, the structure [QUESTION-051](QUESTION-051.md) asks about is a
property of the stationary distribution, not of a single trained network.
If collapse erodes or fluctuates during the limiting dynamics, then
measurements of it depend on when training was stopped.

## What the record holds

- **[THEORY-083](../theory.d/THEORY-083.md):** collapse through the terminal phase, measured under one
  protocol with cross-entropy, weight decay and training past zero error.
- **[THEORY-209](../theory.d/THEORY-209.md):** limiting dynamics under a quadratic minimum. The
  ResNet-18 tests are resumed training at the last hyperparameters, where
  the loss has plateaued.
- **The regimes may differ.** With cross-entropy on separable data there
  is no finite minimum without weight decay, so the quadratic assumption
  fails there. With weight decay there is one, but [THEORY-083](../theory.d/THEORY-083.md)'s protocol
  is not the resumed training [THEORY-209](../theory.d/THEORY-209.md) measures.
- **[THEORY-085](../theory.d/THEORY-085.md):** the Hessian's top eigenspace is made of class outliers
  tied to class means. That is where [THEORY-209](../theory.d/THEORY-209.md)'s isotropy was tested, and
  also where collapse lives.
- **[THEORY-210](../theory.d/THEORY-210.md):** along symmetry directions, SGD drifts conserved
  quantities toward balance. That is motion that need not change the
  features at all.
- **[THEORY-278](../theory.d/THEORY-278.md):** under MSE with no weight decay, on the central
  path, collapse is a limit approached at rate t^(1/4), not a fixed
  point, and the orientation it approaches is set by the singular vectors
  at the start of the path. The degree of collapse then depends on when
  training stops, and the shape on where it started.
- **[THEORY-286](../theory.d/THEORY-286.md):** under class imbalance and weight decay, the
  last-layer geometry depends on the decay's strength, and the approach
  to it is slow and slows with imbalance. So the geometry is not a
  property of the task alone, and measurements of it depend on when
  training stops.

## What would answer it

Neural-collapse metrics (within-class variability, the simplex ETF
geometry, classifier alignment) tracked through limiting dynamics at a
plateau, as in [THEORY-209](../theory.d/THEORY-209.md)'s protocol, with the parameter speed and
diffusion measured at the same time. Or a derivation of collapse as a
property of SGD's stationary distribution rather than of a limit point.
