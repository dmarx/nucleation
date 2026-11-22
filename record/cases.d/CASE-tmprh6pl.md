---
status: Proposed
formerly:
- CASE-tmprh6pl
title: 'An executed enumeration shows the self-consistent factorizations of a fixed coupling matrix are single-linkage dendrogram cuts, hence a nested chain: over 12000 random families no two crosscut, exact symmetry does not force a tie, and grain is the only multiplicity'
version: 1
standing: documented
kind: executed-study
tags:
- individuation
- agency
- complex-systems
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
bears_on:
- QUESTION-032
- QUESTION-035
illustrates:
- CLAIM-174
- CLAIM-170
summary: >-
  The assistant's run for LEAD-109, in numpy, to settle whether a fixed
  level and target admit several self-consistent factorizations into
  agents. A level is modelled as a fixed set of regimes with a fixed
  symmetric coupling matrix; a factorization as a partition into blocks;
  the admission test's first condition ([CLAIM-157](../claims.d/CLAIM-157.md),
  priced by [CLAIM-154](../claims.d/CLAIM-154.md)) as a near-decomposable gap. Exhaustive
  enumeration over 2000 random six-regime couplings at six thresholds
  (12000 non-empty families) found no two factorizations that crosscut;
  every family is a nested chain with a unique finest member. The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-157 CLAIM-170 CLAIM-174 — Proposed (CLAIM-154 Active); the admission test this run enumerates, open -->

# CASE-tmprh6pl: An executed enumeration shows the self-consistent factorizations of a fixed coupling matrix are single-linkage dendrogram cuts, hence a nested chain: over 12000 random families no two crosscut, exact symmetry does not force a tie, and grain is the only multiplicity

## The model

A **fixed level of description** is modelled as a fixed set of *n* regimes
with a fixed symmetric coupling matrix *M* (M[i,j] ≥ 0 the interaction
strength). A **factorization** is a partition *P* of the regimes into
blocks, each a candidate agent ([CLAIM-170](../claims.d/CLAIM-170.md)). The admission
test ([CLAIM-174](../claims.d/CLAIM-174.md)) is applied per block:

- **Test 1** (one system; [CLAIM-157](../claims.d/CLAIM-157.md), [TERM-049](../terms.d/TERM-049.md),
  priced by [CLAIM-154](../claims.d/CLAIM-154.md)): a block is near-decomposable
  ([LIT-905](../literature.d/LIT-905.md)) when gap(P) = b(P)/a(P) > τ, where a(P) is the
  strongest coupling *P* cuts and b(P) is the weakest within-block
  single-linkage merge level (the max-bottleneck spanning tree). A lone
  regime imposes no within-constraint.
- **Tests 2–3** (goal-directed description beats a device one by the Occam
  cost, [LIT-911](../literature.d/LIT-911.md); and adaptation, [LIT-909](../literature.d/LIT-909.md)):
  per-block gates, modelled by [CLAIM-154](../claims.d/CLAIM-154.md)'s rule, reify iff
  d′² > Occam. A factorization *into agents* requires every block to pass.

## The run

`scratch/studies/lead-109/` (python3 -I, numpy, BLAS threads 1; seconds).
Ten pytest tests; `run.py` writes `results.json`.

1. **Crosscutting disagreement does not occur.** The partitions clearing
   test 1 are exactly cuts of *M*'s single-linkage dendrogram, so they are
   totally nested (a chain under refinement). Over 2000 random six-regime
   couplings × six thresholds (12000 non-empty families): **0**
   crosscutting families; every one a nested chain with a unique finest
   member; largest family 6.
2. **Exact symmetry does not force a tie.** On the symmetric 4-ring the two
   rotation-related pairings {01,23} and {12,30} both have gap 1.0 and
   neither clears any τ > 1; they never both clear, because each pair
   straddles a strong edge.
3. **Grain multiplicity is real.** In a two-level (watchmaker) hierarchy
   the fine partition (gap 3.33) and the coarse whole (gap ∞) both clear
   test 1; under the full agent tests both the two-agent and the one-agent
   factorizations can hold at once. They are nested, differing only in
   grain — [CLAIM-170](../claims.d/CLAIM-170.md)'s room-vs-pair, and the
   actor-critic-vs-one-agent-graph [CLAIM-174](../claims.d/CLAIM-174.md) cites
   from Kenton et al. ([LIT-909](../literature.d/LIT-909.md)).

## What it shows

The self-consistent factorizations at a fixed level and target form a
nested hierarchy of coarsenings of a unique finest partition. Agents never
disagree about co-grouping two strongly-coupled regimes; the only
indeterminacy is how coarse to go. Tests 2–3 only prune the chain. This is
[CLAIM-tmpm2589](../claims.d/CLAIM-tmpm2589.md)'s evidence.

## Its limits

A symmetric, non-negative, static coupling matrix, and test 1 enumerated
exactly while tests 2–3 are stipulated per-block verdicts rather than a
full Orseau–Kenton computation on dynamics. Directed or time-lagged
coupling ([CLAIM-157](../claims.d/CLAIM-157.md)'s one-way drive and storage route) is not
modelled; the single-linkage nesting argument assumes the gap is read off
edge weights. The enumeration is to n = 6 (Bell(6) = 203 partitions).
