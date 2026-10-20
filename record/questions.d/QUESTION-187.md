---
number: 187
status: Open
formerly:
- QUESTION-tmps5cfz
title: "Does greedy layered search on the graph HNSW actually builds take expected O(log N) distance computations to a stated recall, under a stated condition on the data such as bounded doubling dimension?"
version: 1
tags:
- databases
- information-retrieval
- network-science
date: '2026-10-19'
line: 'distributed-agency'
summary: >-
  The promotion condition formerly on [THEORY-365](../theory.d/THEORY-365.md), moved here when
  [THEORY-365](../theory.d/THEORY-365.md) was narrowed to what [LIT-1098](../literature.d/LIT-1098.md) measured and promoted on
  2026-10-19 ([ADR-047](../decisions.d/ADR-047.md) v3). The paper derives O(log N) search only for
  exact Delaunay layers of bounded degree. It measures logarithmic scaling
  only at d = 8 and saturating ef only at d = 4, and at d = 128 its
  scaling departs from a logarithm.
answered_by:
- THEORY-tmp880z4
---

# QUESTION-187: Does greedy layered search on the graph HNSW actually builds take expected O(log N) distance computations to a stated recall, under a stated condition on the data such as bounded doubling dimension?

## Why it is a question

Malkov and Yashunin ([LIT-1098](../literature.d/LIT-1098.md), read in full in [NOTE-916](../notes.d/NOTE-916.md)) argue that
search costs a bounded amount per layer over O(log N) layers. That holds
if each layer is an exact Delaunay graph of bounded mean degree. HNSW
builds a different graph: a fixed number of links per element, pruned
heuristically. Delaunay degree grows exponentially with dimension. What
the paper measures for the graphs it builds is in [THEORY-365](../theory.d/THEORY-365.md):

- at d = 8, cost no worse than logarithmic, and below NSW's at every
  size;
- at d = 4, a beam width that saturates;
- at d = 128, on 200M SIFT vectors, a departure from a logarithm.

Until 2026-10-19 the proof asked for here was [THEORY-365](../theory.d/THEORY-365.md)'s promote_when.

## What would answer it

A proof that greedy layered search on the graph HNSW actually builds takes
expected O(log N) distance computations to reach a stated recall, under a
stated condition on the data such as bounded intrinsic or doubling
dimension. The graph must have a fixed number of pruned links per
element, not be an exact Delaunay graph. It would be refuted for that
class by a family of datasets meeting the condition on which the cost
needed for a fixed recall grows faster than log N.

What would not answer it: more benchmarks at fixed dimension. They
re-establish low-dimensional measurements that are already held. They
cannot reach the sizes at which the paper says the high-dimensional case
could be checked.
