---
status: Proposed
promote_when: >-
  A reading of Theorem 1 and its proof in Appendix B, or an independent
  derivation, confirming that μP satisfies the spectral scaling condition
  and is the unique stable abc-parametrization that does, and that the NTK
  parametrization makes updates vanish in spectral norm with width.
title: 'Yang, Simon and Bernstein show that hidden features and their per-step changes stay of order one per entry at every width when each weight matrix and each of its updates has spectral norm of order √(fan-out/fan-in), that μP is the unique stable abc-parametrization meeting this condition, and that standard and neural-tangent parametrizations violate it'
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-21'
source:
- LIT-tmpj34ir
corroborates:
- CLAIM-tmpqwoxz
summary: >-
  The spectral restatement of μP, bridging the width-exponent view
  ([THEORY-tmp7n7a9](THEORY-tmp7n7a9.md)) and the norm-based modular view ([THEORY-tmphj4hu](THEORY-tmphj4hu.md),
  [THEORY-tmpgdk30](THEORY-tmpgdk30.md)). Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-tmp7n7a9 THEORY-tmpgdk30 THEORY-tmphj4hu — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-tmpig1z0: Yang, Simon and Bernstein show that hidden features and their per-step changes stay of order one per entry at every width when each weight matrix and each of its updates has spectral norm of order √(fan-out/fan-in), that μP is the unique stable abc-parametrization meeting this condition, and that standard and neural-tangent parametrizations violate it

## Source

Yang, Simon and Bernstein, [LIT-tmpj34ir](../literature.d/LIT-tmpj34ir.md), read in [NOTE-tmpxtw1l](../notes.d/NOTE-tmpxtw1l.md) from arXiv 2310.17813v2 (14 May 2024).

## What was actually shown

Condition 1, Theorem 1, §§3.4, 5.1 and 5.3 as quoted in the NOTE.

## What this does not say

Nothing about depth, time or the singular spectrum of updates beyond their size; it does not concern orthogonalized updates.

## Connections

[THEORY-tmp7n7a9](THEORY-tmp7n7a9.md) (Yang and Hu); [THEORY-tmpgdk30](THEORY-tmpgdk30.md) (modular duality, whose linear-layer map carries the same √(fan-out/fan-in) factor).
