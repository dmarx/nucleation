---
status: Proposed
promote_when: >-
  An independent analysis or experiment on residual networks with
  one-layer blocks confirming that stability and nontriviality require α ≥
  ½ and α + γ = 1, that under α = γ = ½ each block contributes Θ(1/√L) at
  initialization and Θ(1/L) from training with depthwise continuity
  exponent ½, and that for blocks of two or more layers the 1/√L scaling
  linearizes the interactions within each block.
title: 'Yang, Yu, Zhu and Hayou show that in the infinite-width-then-depth limit of residual networks with one-layer blocks, training is stable and nontrivial only when the branch multiplier exponent is at least one half and the two exponents sum to one, and that Depth-μP, both exponents one half, uniquely maximizes feature diversity, each block contributing an independent order 1/√L at initialization and a correlated order 1/L through its update; for deeper blocks no parametrization keeps their layers interacting without instability or redundancy'
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-21'
source:
- LIT-tmp4peep
summary: >-
  The depth side of the record's drift reading of residual networks
  (CLAIM-tmp2yj4t): the diffusive and systematic rows in the paper's own
  terms, and deeper blocks as a clash between them. Proposed until its
  promote_when is met.
---
<!-- inactive-ok-file: CLAIM-tmp2yj4t CLAIM-tmphedau LIT-tmp4peep NOTE-tmppdqgb THEORY-tmp7n7a9 THEORY-tmpybeh6 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-tmpbyw89: Yang, Yu, Zhu and Hayou show that in the infinite-width-then-depth limit of residual networks with one-layer blocks, training is stable and nontrivial only when the branch multiplier exponent is at least one half and the two exponents sum to one, and that Depth-μP, both exponents one half, uniquely maximizes feature diversity, each block contributing an independent order 1/√L at initialization and a correlated order 1/L through its update; for deeper blocks no parametrization keeps their layers interacting without instability or redundancy

## Source

Yang, Yu, Zhu and Hayou, LIT-tmp4peep, read in NOTE-tmppdqgb from arXiv 2310.02244v5 (12 Oct 2023).

## What was actually shown

Table 1, eq. (1), the two contributions on p. 3, Claims 7.1–7.5, Definition 7.6 and §§9.2–9.3 as quoted in the NOTE.

## What this does not say

Nothing about networks without skips, trained behaviour beyond the limit, or blocks of depth two or more beyond the impossibility; the results are claims with heuristic proofs.

## Connections

THEORY-tmpybeh6 (Bordelon and colleagues, the same rows by DMFT); THEORY-tmp7n7a9 (the width side); CLAIM-tmphedau (the drift table it instantiates).
