---
number: 166
status: Open
formerly:
- QUESTION-tmpzeamh
title: "Does the depth law of deep linear networks hold from starts off the decoupled set: learning time, counted in iterations at the stable step size, bounded in depth when every mode's initial end-to-end gain is of order one, and growing as a power of 1/ε when it is ε, for random orthogonal or small random weights not aligned with the task's singular vectors?"
version: 1
tags:
- learning-theory
date: '2026-10-19'
line: 'learned-structure'
refines:
- QUESTION-039
summary: >-
  The promotion condition formerly on [THEORY-187](../theory.d/THEORY-187.md), moved here unchanged when
  [THEORY-187](../theory.d/THEORY-187.md) was narrowed and promoted on 2026-10-19. The depth law is
  exact for decoupled, balanced starts on whitened inputs. Whether it holds
  from random orthogonal or small random weights is supported by one MNIST
  experiment and an argument from dynamical isometry, not derived.
---

# QUESTION-166: Does the depth law of deep linear networks hold from starts off the decoupled set: learning time, counted in iterations at the stable step size, bounded in depth when every mode's initial end-to-end gain is of order one, and growing as a power of 1/ε when it is ε, for random orthogonal or small random weights not aligned with the task's singular vectors?

## Why it is a question

[THEORY-187](../theory.d/THEORY-187.md), narrowed on 2026-10-19, holds the depth law of Saxe,
McClelland and Ganguli ([LIT-864](../literature.d/LIT-864.md)) for the start the exact theory covers:
whitened inputs and initial weights on the decoupled set, balanced across
layers. There each mode is a scalar, and the plateau and the iteration
count follow by integration. Until that date [THEORY-187](../theory.d/THEORY-187.md)'s promote_when
asked whether the same law holds from starts off the decoupled set. At the
owner's direction, from the promotion audit's batch 027 ([ADR-047](../decisions.d/ADR-047.md)), the
THEORY was narrowed and promoted on the exact case, and the condition moved
here unchanged.

It is open because off the decoupled set the modes couple, the scalar
reduction fails, and the paper's account of random orthogonal starts is an
argument from the isometry of the product of layers, with one MNIST
experiment (Fig. 6A, [NOTE-667](../notes.d/NOTE-667.md)). It refines [QUESTION-039](QUESTION-039.md)'s question of what
sets the moment at which a network acquires a structure.

## What would answer it

The condition formerly on [THEORY-187](../theory.d/THEORY-187.md), unchanged: a derivation, or a
controlled measurement across depths, showing that deep linear networks
started off the decoupled set behave the same way, with learning time,
counted in iterations at the stable step size, bounded in depth when the
initial end-to-end gain on every mode is of order one, and growing as a
power of 1/ε when it is ε. That means random orthogonal or random small
weights, not aligned with the task's singular vectors. More runs from
decoupled starts cannot settle it, since there the result is already
exact.
