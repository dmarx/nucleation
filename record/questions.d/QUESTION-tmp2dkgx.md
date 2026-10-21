---
status: Answered
title: 'Does exact dynamical closure of an aggregate require a nearly decomposable block, or can a collective variable be exactly dynamically independent when no partition of the units is weakly coupled?'
version: 1
tags:
- complex-systems
- information-theory
- mathematics
date: '2026-10-21'
line: distributed-agency
refines:
- QUESTION-221
summary: >-
  The converse half of [QUESTION-221](QUESTION-221.md), split off under [ADR-049](../decisions.d/ADR-049.md) and answered
  by [CLAIM-388](../claims.d/CLAIM-388.md): closure does not require a nearly decomposable block. In a
  linear Gaussian VAR(1) with uniform coupling, the sum of all units is
  exactly dynamically independent at every stable coupling strength,
  while every partition couples as strongly across its edges as within
  them. The forward bound stays with [QUESTION-221](QUESTION-221.md).
answered_by:
- CLAIM-388
---

# QUESTION-tmp2dkgx: Does exact dynamical closure of an aggregate require a nearly decomposable block, or can a collective variable be exactly dynamically independent when no partition of the units is weakly coupled?

## Answer

It does not require one. [CLAIM-388](../claims.d/CLAIM-388.md) (Active, demonstrated) makes A5's
two-unit example exact for n units. Take a stable linear Gaussian VAR(1)
with uniform coupling among n units. The sum of all units is exactly
dynamically independent at every stable coupling strength, by
[THEORY-733](../theory.d/THEORY-733.md)'s sufficiency condition. Every partition of the units into two
or more groups couples as strongly across its edges as within them. So
"Exact aggregation ⇏ near-decomposability", in A5's words.

The result is about partitions of the units. In the eigenbasis of the
coupling matrix the same system is exactly decomposable, which is the
point: the closed variable is not a block of units.

## What it leaves to [QUESTION-221](QUESTION-221.md)

The forward direction: whether weak coupling into a block bounds the
dynamical dependence of its aggregate. [CLAIM-390](../claims.d/CLAIM-390.md) bounds it for the
block's full state, and [CLAIM-386](../claims.d/CLAIM-386.md) gives the aggregate's one-step
deterministic defect, but neither bounds the aggregate's dependence.
[CLAIM-388](../claims.d/CLAIM-388.md) also does not say that the closed sum is one system. That is
[QUESTION-218](QUESTION-218.md).
