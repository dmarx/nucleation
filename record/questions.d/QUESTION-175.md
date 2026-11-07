---
number: 175
status: Open
formerly:
- QUESTION-tmpqtbzj
title: "From generic small initialization, does gradient flow on a symmetrized Barlow Twins loss with a linear or fixed-kernel model follow the aligned trajectory, learning the top eigenvectors one at a time in order of eigenvalue?"
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-10-19'
line: 'learned-structure'
refines:
- QUESTION-039
summary: >-
  Filed when the promotion audit (batch 036, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted [THEORY-229](../theory.d/THEORY-229.md) to initialization aligned with the top eigenvectors.
  Simon et al.'s Result 4.6, for generic small initialization, is an
  informal derivation; the former promote_when asked for its proof, and
  this question holds it.
---

# QUESTION-175: From generic small initialization, does gradient flow on a symmetrized Barlow Twins loss with a linear or fixed-kernel model follow the aligned trajectory, learning the top eigenvectors one at a time in order of eigenvalue?

## Why it is a question

[THEORY-229](../theory.d/THEORY-229.md) now holds what Simon et al. ([LIT-242](../literature.d/LIT-242.md)) prove: from a small
initialization aligned with the top eigenvectors of the pairs' symmetrized
cross-correlation, at a common scale, each mode evolves on its own and
rises at a time set by its eigenvalue and the initial scale, larger
eigenvalues first; and the top spectral solutions are exactly the
minimum-norm zero-loss ones. Their Result 4.6 says a generic small
initialization approaches the aligned trajectory as its scale goes to
zero, but they call it a Result "because we give an informal derivation
rather than a formal proof", checked numerically at d = 3 and on 500
CIFAR-10 crop pairs ([NOTE-741](../notes.d/NOTE-741.md)).

## What would answer it

A formal proof of Result 4.6, or of the same stepwise order for a second
spectral self-supervised loss on a linear or fixed-kernel model, would
answer it yes in the regime it claims. A linear or fixed-kernel case of
this loss, from vanishing generic initialization with distinct positive
eigenvalues, that does not reach the minimum-norm solution or learns a
lower mode first, would answer it no. More ResNet runs showing stepwise
rank growth do not settle it, since the theory does not cover a moving
tangent kernel.
