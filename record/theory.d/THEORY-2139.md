---
number: 2139
status: Proposed
formerly:
- THEORY-tmpig1z0
promote_when: >-
  A reading of Theorem 1 and its proof in Appendix B, or an independent
  derivation, confirming that μP satisfies the spectral scaling condition
  and is the unique stable abc-parametrization that does, and that the NTK
  parametrization makes updates vanish in spectral norm with width.
title: 'Spectral scaling keeps features order one'
statement: >-
  Yang, Simon and Bernstein show that hidden features and their per-step
  changes stay of order one per entry at every width when each weight matrix
  and each of its updates has spectral norm of order √(fan-out/fan-in), that
  μP is the unique stable abc-parametrization meeting this condition, and
  that standard and neural-tangent parametrizations violate it
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-21'
source:
- LIT-2947
corroborates:
- CLAIM-775
summary: >-
  The spectral restatement of μP, bridging the width-exponent view
  ([THEORY-2133](THEORY-2133.md)) and the norm-based modular view ([THEORY-2138](THEORY-2138.md),
  [THEORY-2136](THEORY-2136.md)). Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-2133 THEORY-2136 THEORY-2138 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2139: Spectral scaling keeps features order one

## Source

Yang, Simon and Bernstein, [LIT-2947](../literature.d/LIT-2947.md), read in [NOTE-2233](../notes.d/NOTE-2233.md) from arXiv 2310.17813v2 (14 May 2024).

## What was actually shown

Condition 1, Theorem 1, §§3.4, 5.1 and 5.3 as quoted in the NOTE.

## What this does not say

Nothing about depth, time or the singular spectrum of updates beyond their size; it does not concern orthogonalized updates.

## Connections

[THEORY-2133](THEORY-2133.md) (Yang and Hu); [THEORY-2136](THEORY-2136.md) (modular duality, whose linear-layer map carries the same √(fan-out/fan-in) factor).
