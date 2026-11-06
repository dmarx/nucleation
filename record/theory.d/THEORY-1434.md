---
number: 1434
status: Active
formerly:
- THEORY-tmpykyk4
title: 'Raussen shows that for a concurrent PV program on shared resources of given capacities, a spare capacity computed from the program text bounds from below the connectivity of every space of executions to the target, so that spare capacity zero marks deadlocks, at least one excludes them, and at least two makes all executions equivalent'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    At the twenty-ninth status review, at the status review's ruling (the
    owner delegated these rulings; ADR-065), on NOTE-1581 v2, which reads
    the paper in full: promoted Proposed → Active, and promote_when
    deleted. It asked that "A reading that checks Definition 3.9,
    Proposition 3.12 and the proof of Theorem 4.3 confirms that the paper
    defines the spare capacity of a PV program from the capacities and lock
    patterns and proves that every space of executions to the target is
    (spare capacity − 2)-connected, with deadlocks exactly at the vertices
    of spare capacity zero"; that reading was made and confirms it. A
    misstated join lemma in Proposition 3.12's proof (k + l + 1 for
    k + l + 2) does not affect the result. Corrected in the body: the bound
    is attained at a vertex of minimal spare capacity (Corollary 4.7).
tags:
- mathematics
- operations-research
date: '2026-11-05'
source:
- LIT-2073
summary: >-
  Raussen (2021; Computational Geometry 2023), [LIT-2073](../literature.d/LIT-2073.md), read in full in
  [NOTE-1581](../notes.d/NOTE-1581.md) from arXiv v3, as the neighbour of Fajstrup, Goubault & Raussen
  2006. Active: the definition, the deadlock characterization and the bound
  are proved in the text, resting on a cited colimit decomposition and
  Björner's nerve theorem. It holds for linear PV programs with fixed
  capacities. It does not say anything about durations, energies or costs
  beyond feasibility. The bound is exact at a vertex of minimal spare
  capacity and only a lower bound elsewhere.
---
# THEORY-1434: Raussen shows that for a concurrent PV program on shared resources of given capacities, a spare capacity computed from the program text bounds from below the connectivity of every space of executions to the target, so that spare capacity zero marks deadlocks, at least one excludes them, and at least two makes all executions equivalent

## Source

Raussen (2021; 2023), [LIT-2073](../literature.d/LIT-2073.md); read in [NOTE-1581](../notes.d/NOTE-1581.md).

## What was actually shown

- **The model** (§1.1): capacities κ(r), the forbidden region, executions
  as directed paths avoiding it.
- **Deadlocks** (Proposition 3.12(3)): a vertex is a deadlock "if and only
  if κ(X; v) = 0."
- **The theorem** (Theorem 4.3, proof read; exact at a vertex of minimal spare capacity, Corollary 4.7): path spaces to the target are
  (κ(X) − 2)-connected, by a local-to-global argument through Björner's
  nerve lemma.
- **Corollary 4.4**: κ(X) ≥ 1 gives a non-empty path space, κ(X) ≥ 2 a
  path-connected one, so all executions give the same result.

## What this does not say

- That the bound is tight from every source: it is attained at a vertex
  of minimal spare capacity (Corollary 4.7, from Proposition 4.6), and
  elsewhere is only a lower bound.
- Anything about programs that are not linear, except by unfolding.
- Anything about costs, durations or energies: capacities are hard
  constraints.
- That spare capacity at least two is desirable for computing: such a
  program "can thus not be used to solve a decision problem" (§1.2.1).
