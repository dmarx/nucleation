---
number: 81
status: Open
formerly:
- QUESTION-tmp4j05x
title: 'When the relative scale of a network''s layers sets its learning regime under gradient flow, does that regime survive SGD, whose minibatch noise drives the relative scale toward balance, and on what timescale compared with learning?'
version: 1
tags:
- learning-theory
- representation-learning
- loss-landscapes
date: '2026-10-13'
line: learned-structure
refines:
- QUESTION-039
summary: >-
  Two readings meet here. Under gradient flow, the relative scale of
  adjacent layers is conserved and sets whether learning is rich or lazy
  ([THEORY-212](../theory.d/THEORY-212.md), Dominé et al.). Under SGD, that scale is not
  conserved: minibatch noise drives it toward the point where the layers'
  gradient noise balances, at a rate set by η/S ([THEORY-211](../theory.d/THEORY-211.md), Ziyin et al.).
  If the drift is fast compared with learning, an unbalanced start chosen
  to be lazy would drift toward balance and richness. If it is slow, the
  regime set at initialization stands. Neither paper addresses the other.
  Drawn by the assistant from reading both, and filed at the owner's
  request.
---
<!-- inactive-ok-file: THEORY-212 THEORY-186 — Proposed; the two accounts this question sets against each other, and the balanced case, open -->

# QUESTION-081: When the relative scale of a network's layers sets its learning regime under gradient flow, does that regime survive SGD, whose minibatch noise drives the relative scale toward balance, and on what timescale compared with learning?

## The question

[THEORY-212](../theory.d/THEORY-212.md) (Dominé et al.) says that in a two-layer linear network
the relative scale λ of the layers decides between rich and lazy
learning. That holds because gradient flow conserves λ. [THEORY-211](../theory.d/THEORY-211.md)
(Ziyin et al.) says that under SGD the same quantity is driven toward
balance, d(‖u‖² − ‖w‖²)/dt = −T(uᵀC₁u − wᵀC₂w) with T = η/S, plus weight
decay. The question is which wins.

- **If the drift is fast compared with learning,** an unbalanced, lazy
  start would move toward balance while it learns, and the regime would
  shift toward rich during training.
- **If it is slow,** learning finishes in the regime the initialization
  set, and balance arrives only later, at stationarity.
- **If the noise-balanced point is not λ = 0,** SGD would select its own
  regime, set by the data's noise structure, regardless of
  initialization.

## Why the record needs it

[QUESTION-039](QUESTION-039.md) asks what sets when and how structure is acquired.
[THEORY-212](../theory.d/THEORY-212.md) answers with the initialization. [THEORY-211](../theory.d/THEORY-211.md) implies that,
under the optimizer actually used, the initialization's say may be
temporary. Which is true decides whether "the initialization sets the
regime" is a fact about networks trained with SGD, or only about gradient
flow.

## What the record holds

- **[THEORY-212](../theory.d/THEORY-212.md):** the regime as a function of a conserved λ, under
  gradient flow.
- **[THEORY-211](../theory.d/THEORY-211.md):** the law of balance. Its two-layer linear example reaches
  uᵢ² = wᵢ² at stationarity. That is a statement about the end of
  training, not about the transitions.
- **[THEORY-186](../theory.d/THEORY-186.md) and [THEORY-187](../theory.d/THEORY-187.md):** the balanced case's stage-like learning.
- **[LIT-1012](../literature.d/LIT-1012.md) (Neural Mechanics):** weight decay also drives the
  conserved quantity toward zero, as e^{−2λt} for weight decay λ, plus a
  gradient-norm term whose sign is not fixed.

## What would answer it

- **A measurement:** two-layer or deeper networks trained with SGD from
  unbalanced starts, tracking λ(t) and the NTK's movement against the
  learning curve, at several η/S.
- **Or a derivation:** comparing the drift rate TC₀ with the rate of the
  slowest singular-value transition.
