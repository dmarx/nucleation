---
number: 1
status: Active
formerly:
- CASE-tmp11vtm
title: 'Two reset matrices: noncommuting and classical'
version: 1
standing: stipulated
tags:
- probabilistic-modeling
- mathematics
date: '2026-10-08'
line: pragmatic-transport
counterexample_to:
- CLAIM-073
summary: >-
  A30: on a two-state classical system, A resets to state 1 and B to
  state 2; AB = A and BA = B, so AB ≠ BA, and every state is an ordinary
  probability vector. Order dependence without nonclassical probability.
supports:
- CLAIM-041
---
<!-- inactive-ok-file: CLAIM-073 — Rejected; answered or abandoned, and cited as the history this entry answers -->

# CASE-001: Two reset matrices: noncommuting and classical

## The case

A30: "Take a classical system with two states, represented by a probability
vector p. Consider two stochastic update matrices: A = [[1,1],[0,0]],
B = [[0,0],[1,1]]. A resets the system to state 1; B resets it to state 2. Then
AB = A, BA = B, so AB ≠ BA. Yet this system is entirely classical."

## What it can show

That order dependence, and noncommuting operations, do not imply nonclassical
probability ([CLAIM-073](../claims.d/CLAIM-073.md), [CLAIM-041](../claims.d/CLAIM-041.md)). The manuscript §9 keeps the conclusion ("Generally
AB≠BA even in a finite classical Markov system") without the example.
