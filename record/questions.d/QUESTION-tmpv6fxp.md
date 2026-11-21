---
status: Open
title: 'Do well-separated levels in a chain''s time geometry require separated rates: must a chain whose log commute-time metric has levels spaced well beyond its defect from an ultrametric have rates that differ by large factors between levels, or can the shape and entropy of the state space alone space them?'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Restated after the reading of Bovier and colleagues (NOTE-tmpjot4l).
    The logarithm of any metric is nearly an ultrametric, so tree-likeness
    alone needs no rate gaps; the question is about the spacing of levels.
    Bovier and colleagues' times combine rates with masses, capacities and
    entropic prefactors, so separation can come from geometry. Previous
    title: "Does a time geometry that is tree-like with well-separated
    levels require separated time scales: must a chain whose log
    commute-time metric is close to an ultrametric, with levels spaced
    well beyond its defect, have rates that differ by large factors
    between levels?".
tags:
- mathematics
- complex-systems
date: '2026-11-20'
line:
- formal-apparatus
- distributed-agency
summary: >-
  The converse of [CLAIM-tmpxi826](../claims.d/CLAIM-tmpxi826.md), which shows that separated time scales
  make the log commute-time geometry tree-like. The spacing argument
  suggests the converse: levels a distance Δ apart in that geometry differ
  in commute time by a factor e^Δ. But commute time mixes rates with the
  sizes and shapes of the blocks, so a large factor could come from
  geometry rather than from rate gaps. Filed with the assistant's
  hierarchy-and-hyperbolicity claims of 2026-11-20.
---
<!-- inactive-ok-file: CLAIM-tmpxi826 CLAIM-tmpy75jv — Proposed; filed in this contribution of 2026-11-20 -->

# QUESTION-tmpv6fxp: Do well-separated levels in a chain's time geometry require separated rates: must a chain whose log commute-time metric has levels spaced well beyond its defect from an ultrametric have rates that differ by large factors between levels, or can the shape and entropy of the state space alone space them?

## What makes it open

[CLAIM-tmpxi826](../claims.d/CLAIM-tmpxi826.md) goes one way: rates ε^U with small ε give a log commute-time
metric within a constant of log(1/ε) times an ultrametric. The other way is
not shown. Commute time is n·R_eff, and effective resistance depends on the
graph as well as the rates: a long thin path of equal-rate edges has large
resistance with no rate gap at all. So a tree-like time geometry might arise
from the shape of the state space alone, as [THEORY-193](../theory.d/THEORY-193.md)'s growth process makes
a hyperbolic graph with no rates in it.

## What would count as an answer

- A proof that, on graphs of bounded degree or bounded size, a log
  commute-time metric within c of an ultrametric whose levels are spaced by
  more than k·c forces rate ratios of at least e^(k′c) between levels; or
- a family of chains with equal rates whose log commute-time metrics are
  tree-like with spacing growing beyond their defect, showing that shape
  alone suffices; and then a statement of which hierarchies are of time
  scales and which of shape.

It bears on [CLAIM-tmpy75jv](../claims.d/CLAIM-tmpy75jv.md): if shape alone can make the tree, "one rate gap
does two jobs" holds only where the tree comes from rates.
