---
number: 2137
status: Proposed
formerly:
- THEORY-tmph10k5
promote_when: >-
  The proofs of Corollary 2.6 with Lemma 2.5, Theorem 3.5, and Theorem 5.1
  with Lemma 5.3 checked, confirming the three statements under
  Definitions 1.1 and 1.2.
title: 'Metastable exit times are mass over capacity'
statement: >-
  Bovier, Eckhoff, Gayrard and Klein hold that for a reversible Markov chain
  with generically separated metastable points, minus the logarithm of the
  capacity between them is an ultrametric up to an additive ln 3, the mean
  time to leave a point's valley is the valley's mass over that capacity up
  to a factor 1 + o(1), and each metastable point owns one low-lying
  eigenvalue equal to the inverse of that time, with an eigenvector near the
  valley's indicator
version: 1
tags:
- probabilistic-modeling
- mathematics
- complex-systems
date: '2026-11-21'
source:
- LIT-2951
bears_on:
- QUESTION-501
- QUESTION-500
summary: >-
  The sharp, large-N metastability result the record lacked beside its
  logarithmic Freidlin–Wentzell holdings ([THEORY-1366](THEORY-1366.md), [THEORY-1370](THEORY-1370.md)). It
  bears on the record's commute-time tree ([CLAIM-780](../claims.d/CLAIM-780.md)) by giving its
  general reversible counterpart with a size-independent slack. Proposed
  until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-1366 THEORY-1370 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-780 THEORY-2141 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2137: Metastable exit times are mass over capacity

## Source

Bovier, Eckhoff, Gayrard and Klein, [LIT-2951](../literature.d/LIT-2951.md), read in [NOTE-2225](../notes.d/NOTE-2225.md) from arXiv math/0007160v1 (26 Jul 2000).

## What was actually shown

Under Definitions 1.1 and 1.2: Corollary 2.6 and (2.27), the ln 3 almost-ultrametric; Theorem 1.3, exit times, eigenvalues and exponential laws; Theorem 5.1 and Lemma 5.3, the ordering of eigenvalues by nested exclusion sets.

## What this does not say

Nothing about finite rate ratios, commute times, or degenerate (non-generic) landscapes; it is not a small-noise ε^U result.

## Connections

[THEORY-1366](THEORY-1366.md) (Freidlin and Wentzell, logarithmic asymptotics); [THEORY-1370](THEORY-1370.md) (Berglund on Kramers' law, whose promote_when names a later paper by the same group); [CLAIM-581](../claims.d/CLAIM-581.md) (the peak-cost ultrametric); [THEORY-2141](THEORY-2141.md) (Bachas and Huberman: dynamics on the tree).
