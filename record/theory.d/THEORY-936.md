---
number: 936
status: Proposed
formerly:
- THEORY-tmpev90a
promote_when: >-
  Independent simulations of the stated equations (Eqs. 8–12) for
  rock–scissors–paper with the paper's parameters reproducing positive
  largest Lyapunov exponents over a substantial part of the ε_Y range with
  α = 0.01 and ε_X = 0.5, and the Hamiltonian chaos at ε_X = −ε_Y > 0
  without decay. It is refuted if the reported chaos is a numerical
  artifact (for example, it disappears under a more accurate integrator).
  Claims that chaos is typical of multi-agent learning in general are
  wider than this and are neither promoted nor refuted by it.
title: 'In two-agent rock–scissors–paper played by softmax reinforcement learners, nonzero tie rewards give quasiperiodic tori and Hamiltonian chaos without memory decay, and limit cycles and chaotic attractors with it, over a large share of the tie-reward range simulated'
version: 1
tags:
- game-theory
- complex-systems
- learning-theory
date: '2026-10-24'
source:
- LIT-1520
summary: >-
  Sato & Crutchfield (arXiv 2002; PRE 2003), [LIT-1520](../literature.d/LIT-1520.md), read in full in
  [NOTE-1144](../notes.d/NOTE-1144.md), pp. 2–3 and Figs. 1–3. Numerical results for one game, two
  agents and the parameters shown; the zero-decay, zero-sum case was first
  reported in Sato, Akiyama and Farmer (PNAS 2002), which is not held.
---
<!-- inactive-ok-file: NOTE-1144 THEORY-928 CLAIM-451 — Proposed or new; the source and the accounts this bears on, named -->

# THEORY-936: In two-agent rock–scissors–paper played by softmax reinforcement learners, nonzero tie rewards give quasiperiodic tori and Hamiltonian chaos without memory decay, and limit cycles and chaotic attractors with it, over a large share of the tie-reward range simulated

## Source

Sato and Crutchfield, [LIT-1520](../literature.d/LIT-1520.md), pp. 2–3 and Figures 1–3 of arXiv v2,
read in [NOTE-1144](../notes.d/NOTE-1144.md).

## What was actually shown

- **No decay, zero-sum** (ε_X = −ε_Y). Quasiperiodic tori only at ε = 0;
  for ε_X = −ε_Y > 0, Hamiltonian chaos, with a periodic orbit arbitrarily
  close to any chaotic one and the mixed Nash equilibrium unstable
  (Fig. 1).
- **No decay, not zero-sum.** Transients to heteroclinic cycles: time spent
  near the vertices grows when ε_X + ε_Y < 0, and chaotic transients
  persist when ε_X + ε_Y > 0.
- **Decay** (α_X = α_Y = 0.01, ε_X = 0.5). Limit cycles and chaotic
  attractors (Fig. 2). Across ε_Y ∈ [−1, 1] the largest Lyapunov exponent is
  "positive across a significant fraction of parameter space; indicating
  that chaos is common" (p. 3). Near zero-sum the agents can reach the
  stable Nash equilibrium.

## What this does not say

- That chaos is common in multi-agent learning generally. That is the
  authors' expectation for "high-dimensional and heterogeneous
  populations", stated, not shown.
- How large "a significant fraction" is. The figure was not inspected and
  the text gives no number.

## Connections

- **[CLAIM-451](../claims.d/CLAIM-451.md).** Persistent cycling and chaos from fixed, self-interested
  learning rules, with no regime switching and no preference instability.
  It also warns that behaviour that looks like switching between
  cooperation and competition can be one deterministic chaotic regime.
- **[THEORY-894](THEORY-894.md).** The ε = 0 game is harmonic, and its orbits never
  converge. How the tie rewards divide between potential and harmonic parts
  is not computed here or in the paper.
