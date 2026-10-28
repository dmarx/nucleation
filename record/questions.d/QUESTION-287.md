---
number: 287
status: Answered
formerly:
- QUESTION-tmpf2ohw
title: 'In a deterministic singularly perturbed system whose eliminated variable is fast and contracting and whose reduced system is contracting, does the memoryless quasi-steady-state reduction predict the coarse variable with an error bounded uniformly in time in terms of the eliminated dynamics?'
version: 1
tags:
- complex-systems
- mathematics
- natural-sciences
date: '2026-10-27'
line: distributed-agency
refines:
- QUESTION-222
summary: >-
  The fast contracting case of [QUESTION-222](QUESTION-222.md), split off by the status
  review of 2026-10-27 under [ADR-049](../decisions.d/ADR-049.md), because [THEORY-773](../theory.d/THEORY-773.md) (Active) settles
  it. No memory coordinate is needed: the reduction on the slow manifold
  stays within O(ε) of the true slow trajectory for all t ≥ 0, with every
  constant explicit, set by the fast contraction rate λ_z, the reduced
  contraction rate λ_x and the manifold's drift.
---

# QUESTION-287: In a deterministic singularly perturbed system whose eliminated variable is fast and contracting and whose reduced system is contracting, does the memoryless quasi-steady-state reduction predict the coarse variable with an error bounded uniformly in time in terms of the eliminated dynamics?

## The question

[QUESTION-222](QUESTION-222.md) asks, for a stated class, when a coarse variable whose
reduced dynamics carry memory admits a finite Markovian augmentation with
prediction error bounded in terms of the eliminated dynamics. The fast,
contracting, deterministic class is one where the augmentation can be
empty. This question asks whether the bound holds there.

## The answer

[THEORY-773](../theory.d/THEORY-773.md), Active, from Del Vecchio and Slotine with their Theorem 3's
hypothesis corrected, answers yes. For ẋ = f(x, z, t), εż = g(x, z, ε),
with g contracting in z at rate λ_z, the reduced system on z = γ(x)
contracting at rate λ_x, f α-Lipschitz in z, |∂γ/∂x · f| ≤ d along the
trajectory and g K-Lipschitz in ε:

- the fast state is within χ_z e^{−λ_z t/ε}|z(0) − γ(x(0))| +
  εχ_z(d + K)/λ_z of the manifold, and
- the slow state is within χ_x|x(0) − x_γ(0)|e^{−λ_x t} +
  ε[C₁(e^{−λ_x t} − e^{−λ_z t/ε}) + C₂(1 − e^{−λ_x t})] of the reduced
  trajectory, for all t ≥ 0.

So k = 0 memory coordinates, and the error is O(ε) with constants in
λ_z, λ_x, d and K. Partial contraction of f in x alone is not enough.
Slow or noisy eliminated variables remain [QUESTION-222](QUESTION-222.md)'s.
