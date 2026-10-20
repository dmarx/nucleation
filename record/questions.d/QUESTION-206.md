---
number: 206
status: Open
formerly:
- QUESTION-tmpuuniu
title: "Does stochastic gradient noise drive training into a mirror-symmetric subspace where it is a saddle, beyond the second-order, diagonal-Hessian argument, and does a trained network's distance to that subspace fall to zero past a threshold set by noise and curvature?"
version: 1
tags:
- learning-theory
- loss-landscapes
date: '2026-10-20'
line: 'learned-structure'
refines:
- QUESTION-058
summary: >-
  The promotion condition formerly on [THEORY-213](../theory.d/THEORY-213.md). [THEORY-213](../theory.d/THEORY-213.md) was narrowed
  and promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v2) to the exact half of Ziyin's
  Theorem 1: a mirror symmetry's subspace is invariant under gradient
  training, and weight decay above half the lower bound on the Hessian
  puts every minimum in it. The SGD half, attraction to the subspace even
  at a saddle, rests on a diagonal approximation and is open.
answered_by:
- THEORY-781
---

# QUESTION-206: Does stochastic gradient noise drive training into a mirror-symmetric subspace where it is a saddle, beyond the second-order, diagonal-Hessian argument, and does a trained network's distance to that subspace fall to zero past a threshold set by noise and curvature?

## Why it is a question

[THEORY-213](../theory.d/THEORY-213.md) holds the exact part of Ziyin (2024). Every mirror symmetry
makes its subspace invariant under GD and SGD. Strong enough weight decay
makes it the location of every minimum. The paper also argues that SGD
noise makes the subspace attractive even where gradient descent escapes
it, from the sign of a Lyapunov exponent. It derives the threshold only
after a second-order expansion and a diagonal approximation of the sample
Hessian, and calls the result qualitatively correct, not exact. Its
network evidence (ResNet18, transformers) was not checked. Until
2026-10-20 this was [THEORY-213](../theory.d/THEORY-213.md)'s promote_when.

## What would answer it

- A derivation of the SGD threshold without the diagonal approximation.
- A network with a known permutation, rotation or rescaling symmetry,
  trained with SGD across learning rates, batch sizes and weight decays,
  with a measured distance to the symmetric subspace (neuron coincidence,
  rank, sparsity). Past a threshold predicted from the noise and
  curvature, that distance should fall to zero. It should not when the
  symmetry is removed by reparametrization.

Against it: no dependence of the outcome on noise where the threshold
predicts one. What cannot settle it: more toy factorizations.
