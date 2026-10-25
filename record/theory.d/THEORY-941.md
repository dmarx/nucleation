---
number: 941
status: Proposed
formerly:
- THEORY-tmpri5hl
promote_when: >-
  The Main Theorem's proof (appendix, steps M1–M11) checked step by step by
  a second reader, or the result confirmed in a later treatment that proves
  it independently; and a simulation of regret matching in a game with
  correlated equilibria outside the convex hull of its Nash equilibria
  (chicken) whose empirical distributions enter and stay near the
  correlated-equilibrium set. It is refuted by a gap in the proof or by a
  game in which every player follows the procedure with μ above the stated
  bound and the empirical distribution stays away from the set with
  positive probability. Results about which correlated equilibrium is
  reached, or about players who do not observe one another, are wider than
  this and neither promote nor refute it.
title: 'If every player of a finite game switches from its last action to each other action with probability proportional to its positive conditional regret, the empirical distribution of play converges almost surely to the set of correlated equilibria'
version: 1
tags:
- game-theory
- learning-theory
date: '2026-10-24'
source:
- LIT-1521
summary: >-
  Hart & Mas-Colell (Econometrica 2000; handout 1996), [LIT-1521](../literature.d/LIT-1521.md), read in
  full in [NOTE-1142](../notes.d/NOTE-1142.md). Convergence is of time-averaged joint frequencies
  to a set, not of play to an equilibrium; the common history is the
  correlating device; inertia is needed; and interior correlated equilibria
  that are not pure Nash cannot be the limit.
---
<!-- inactive-ok-file: NOTE-1142 THEORY-414 CLAIM-443 — Proposed or new; the source and the accounts this bears on, named -->

# THEORY-941: If every player of a finite game switches from its last action to each other action with probability proportional to its positive conditional regret, the empirical distribution of play converges almost surely to the set of correlated equilibria

## Source

Sergiu Hart and Andreu Mas-Colell, "A simple adaptive procedure leading to
correlated equilibrium", *Econometrica* 68(5):1127–1150 (2000),
[LIT-1521](../literature.d/LIT-1521.md), read in full in [NOTE-1142](../notes.d/NOTE-1142.md): Main Theorem (p. 1131), the
Proposition and Theorem A (pp. 1133–1138), and the appendix.

## What was actually shown

- **The procedure.** Having last played j, play k ≠ j with probability
  R_t(j, k)/μ, where R_t(j, k) is the positive part of the average gain i
  would have had by playing k in every period it played j; otherwise play j.
  Players know their own payoffs and observe the history.
- **The theorem.** If all players follow it, z_t, the empirical
  distribution of action profiles, converges almost surely to the set of
  correlated equilibria.
- **Why regrets are the right measure.** D_t(j, k) is exactly the
  correlated-equilibrium constraint for (i, j, k) evaluated at z_t, so
  regrets vanish if and only if z_t approaches the set (Proposition,
  re-derived in the reading).
- **What it needs.** A positive probability of repeating: without it, in a
  2×2 coordination game, play can alternate forever between the two
  miscoordinated profiles (p. 1141).

## What this does not say

- That play converges to a correlated equilibrium. The time average
  approaches the set; it either converges to a pure Nash equilibrium or is
  infinitely often outside the set, and correlated equilibria that are
  interior and not pure Nash cannot be its limit (p. 1132).
- Which correlated equilibrium. Nothing selects among them.
- That the procedure is robust to sophisticated opponents. Only Theorem A's
  invariant-distribution variant is universally calibrated.

## Connections

- **[THEORY-414](THEORY-414.md).** Correlated-equilibrium play without a device or a
  represented rule. It supports [THEORY-414](THEORY-414.md)'s view that equilibrium alone is
  not institution, and shows what adaptive play lacks: selection and
  stability of one equilibrium.
- **[CLAIM-443](../claims.d/CLAIM-443.md).** Inertia as a condition of convergence, not only of
  persistence.
