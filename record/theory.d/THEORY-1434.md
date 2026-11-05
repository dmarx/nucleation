---
number: 1434
status: Proposed
formerly:
- THEORY-tmpykyk4
promote_when: >-
  A reading that checks Definition 3.9, Proposition 3.12 and the proof of
  Theorem 4.3 confirms that the paper defines the spare capacity of a PV
  program from the capacities and lock patterns and proves that every
  space of executions to the target is (spare capacity − 2)-connected, with
  deadlocks exactly at the vertices of spare capacity zero.
title: 'Raussen shows that for a concurrent PV program on shared resources of given capacities, a spare capacity computed from the program text bounds from below the connectivity of every space of executions to the target, so that spare capacity zero marks deadlocks, at least one excludes them, and at least two makes all executions equivalent'
version: 1
tags:
- mathematics
- operations-research
date: '2026-11-05'
source:
- LIT-2073
summary: >-
  Raussen (2021; Computational Geometry 2023), [LIT-2073](../literature.d/LIT-2073.md), read in part
  in [NOTE-1581](../notes.d/NOTE-1581.md), as the neighbour of Fajstrup, Goubault & Raussen 2006.
  Proposed: the proof of Theorem 4.3 was read, but Proposition 3.12's proof
  and the several-resource details of §§2.2.2–3.3 were not. It holds for
  linear PV programs with fixed capacities. It does not say anything about
  durations, energies or costs beyond feasibility, nor that the bound is
  tight in general.
---
<!-- inactive-ok-file: NOTE-1581 — Skimmed and new; cited from the reading of Raussen (2023) as open -->

# THEORY-1434: Raussen shows that for a concurrent PV program on shared resources of given capacities, a spare capacity computed from the program text bounds from below the connectivity of every space of executions to the target, so that spare capacity zero marks deadlocks, at least one excludes them, and at least two makes all executions equivalent

## Source

Raussen (2021; 2023), [LIT-2073](../literature.d/LIT-2073.md); read in [NOTE-1581](../notes.d/NOTE-1581.md).

## What was actually shown

- **The model** (§1.1): capacities κ(r), the forbidden region, executions
  as directed paths avoiding it.
- **Deadlocks** (Proposition 3.12(3)): a vertex is a deadlock "if and only
  if κ(X; v) = 0."
- **The theorem** (Theorem 4.3, proof read): path spaces to the target are
  (κ(X) − 2)-connected, by a local-to-global argument through Björner's
  nerve lemma.
- **Corollary 4.4**: κ(X) ≥ 1 gives a non-empty path space, κ(X) ≥ 2 a
  path-connected one, so all executions give the same result.

## What this does not say

- That the bound is tight in general: only under Proposition 4.6's
  hypothesis.
- Anything about programs that are not linear, except by unfolding.
- Anything about costs, durations or energies: capacities are hard
  constraints.
- That spare capacity at least two is desirable for computing: such a
  program "can thus not be used to solve a decision problem" (§1.2.1).
