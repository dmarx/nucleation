---
number: 340
status: Open
formerly:
- QUESTION-tmpbumel
title: 'When does a cache replacement value based on distance from the current query beat recency-based eviction: does a competitive analysis, or an analysis under a stated distribution of query paths, say so, and do experiments in another system that vary cycle length relative to cache size recover the crossover with MRU?'
version: 1
tags:
- databases
- operations-research
date: '2026-10-30'
line: distributed-agency
summary: >-
  The promotion condition formerly on [THEORY-375](../theory.d/THEORY-375.md), moved here when the
  status review of 2026-10-30 promoted it under [ADR-065](../decisions.d/ADR-065.md). Dar et al.'s
  crossover between distance and MRU is simulated on synthetic paths and
  not explained.
---

# QUESTION-340: When does a cache replacement value based on distance from the current query beat recency-based eviction: does a competitive analysis, or an analysis under a stated distribution of query paths, say so, and do experiments in another system that vary cycle length relative to cache size recover the crossover with MRU?

## Why it is a question

[THEORY-375](../theory.d/THEORY-375.md) reports one simulator ([LIT-1113](../literature.d/LIT-1113.md), read in [NOTE-904](../notes.d/NOTE-904.md)): distance
from the current query beat LRU where queries clustered or wandered with
loops, and MRU was best on regular cyclic paths. The paper gives no
analysis of the crossover, and [NOTE-904](../notes.d/NOTE-904.md) notes that its numbers point to
cycle length relative to cache size without testing it. Which property of
a workload decides between a forecast by content and eviction by recency
is open.

## What would answer it

An analysis, competitive or under a stated distribution of query paths,
that says when a value based on distance from the current query beats
recency-based eviction, or experiments in another system that vary cycle
length relative to cache size and recover the crossover. More runs of the
same simulator on the same synthetic paths do not settle it.
