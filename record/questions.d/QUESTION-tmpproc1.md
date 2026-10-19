---
status: Open
title: 'When are the optimal representations of an information-bottleneck or rate–distortion objective at two budgets nested, so that the coarser optimum is a function of the finer, and when does raising the budget reorganize the optimum into a partition incomparable with the last?'
version: 1
tags:
- information-theory
- learning-theory
- representation-learning
date: '2026-10-19'
line: learned-structure
refines:
- QUESTION-tmp8qovh
summary: >-
  A2 of the exchange of 2026-10-19 on coarse-to-fine processes, which
  called it "the most consequential missing bridge". A hierarchy of
  optimal abstractions needs more than an optimum at each budget: it needs
  the optima to be compatible. [NOTE-676](../notes.d/NOTE-676.md) gets nesting by restricting the
  encoder to prunings of a fixed tree; nothing in the record says when it
  holds without that restriction. Rate–distortion theory's answer is
  successive refinability (Equitz and Cover, registered unread).
---
<!-- inactive-ok-file: LIT-tmp25otd — Deferred; works registered unread, cited as open, nothing here rests on them -->
<!-- inactive-ok-file: THEORY-163 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
# QUESTION-tmpproc1: When are the optimal representations of an information-bottleneck or rate–distortion objective at two budgets nested, so that the coarser optimum is a function of the finer, and when does raising the budget reorganize the optimum into a partition incomparable with the last?

## Why it is a question

A2: "Changing β does not, in general, guarantee that the new optimal
representation refines the previous one. The optimizer can reorganize
categories rather than simply subdivide them." The question is when there
are optima Z_{β₂} and Z_{β₁}, β₂ > β₁, with X → Z_{β₂} → Z_{β₁} a Markov
chain. If none exist, an optimal learner's trajectory may merge or
reshuffle categories rather than split them, and a coarse-to-fine reading
of it is wrong.

## What the record holds

- [NOTE-676](../notes.d/NOTE-676.md) (G-tree search, [LIT-868](../literature.d/LIT-868.md)): with the encoder restricted to
  prunings of a fixed quadtree, the compression trade-off gives nested
  coarse-grainings "by construction", and the tree that solves IB with
  side information is a pruning of the plain IB tree at the same β. The
  nesting is imposed, not found.
- [NOTE-631](../notes.d/NOTE-631.md) and [THEORY-163](../theory.d/THEORY-163.md) (colour naming): annealing β gives a hierarchy
  of categories with bifurcations. Whether those splits nest is not tested.
- Successive refinement of information ([LIT-tmp25otd](../literature.d/LIT-tmp25otd.md), unread): the
  classical rate–distortion result that a source is refinable without loss
  exactly when the optimal descriptions form such a Markov chain, and that
  some sources are not.

## What would count as an answer

A structural condition on P(X, Y) that guarantees nested IB optima, or a
small discrete distribution whose optima at two budgets are incomparable
partitions. A2's second project proposes the search: four to eight states,
all deterministic encoders enumerated by their partitions, optima found at
several β, and the refinement relation between them inspected. A2's own
limit: deterministic enumeration "does not settle the unrestricted
stochastic-encoder version of successive refinement."
