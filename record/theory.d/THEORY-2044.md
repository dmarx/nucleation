---
number: 2044
status: Proposed
formerly:
- THEORY-tmprqrdn
title: 'Wang and Slotine show that if an auxiliary system with the actual state as input is contracting, every trajectory of the actual system acquires exponentially any smooth property one of its solutions has, though the actual system need not be contracting; for identical units with symmetric positive-definite diffusive coupling on a connected graph this gives global exponential synchronization above a threshold set by the Laplacian''s spectrum, with the common phase left to initial conditions'
version: 1
source:
- LIT-2837
tags:
- control-theory
- mathematics
- complex-systems
date: '2026-11-19'
promote_when: >-
  Theorem 1's virtual-system argument and Theorem 6's bound are rederived
  step by step from the paper, and a numerical check on a small network
  (four diffusively coupled Van der Pol oscillators on a ring, say) shows
  synchrony from arbitrary initial conditions above the threshold of eq.
  13, with a common phase that varies with the initial conditions.
corroborates:
- CLAIM-481
bears_on:
- QUESTION-063
- QUESTION-147
summary: >-
  From the reading of [LIT-2837](../literature.d/LIT-2837.md) in [NOTE-2096](../notes.d/NOTE-2096.md). The partial
  contraction the reading of Lohmiller and Slotine found missing.
  Proposed until its promote_when is met.
---

# THEORY-2044: Wang and Slotine show that if an auxiliary system with the actual state as input is contracting, every trajectory of the actual system acquires exponentially any smooth property one of its solutions has, though the actual system need not be contracting; for identical units with symmetric positive-definite diffusive coupling on a connected graph this gives global exponential synchronization above a threshold set by the Laplacian's spectrum, with the common phase left to initial conditions

## The account

Take the actual system ẋ = f(x, x, t) and build an auxiliary system
ẏ = f(y, x, t), with x entering as an input. If the auxiliary system is
contracting in y and one of its particular solutions has a smooth
property (equal components, lying on a manifold), every trajectory of
the actual system acquires the property exponentially (Theorem 1). The
actual system need not contract: what is contracted is the distance to
the property, and what lies along it is kept, so synchronized
oscillators keep their limit cycle with a common phase that the initial
conditions fix.

For n identical units with symmetric positive-definite diffusive
coupling on a connected graph, synchrony is global and exponential when
λm+1 of the weighted Laplacian exceeds the largest eigenvalue of the
symmetric part of the uncoupled Jacobian (Theorem 6); the same bound
applies to symmetric subgroups. Long-range links count more than short
ones, a ring's threshold diverges with its size, and a leader fixes the
phase that peers leave free (Theorem 7).

## Evidence

Proofs in the paper, with worked examples (Van der Pol and
FitzHugh–Nagumo oscillators, gaits, flocking). The conditions are
sufficient; the auxiliary system has to be found case by case.
