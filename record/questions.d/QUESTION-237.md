---
number: 237
status: Open
formerly:
- QUESTION-tmp4iwgh
title: 'Does semantic caching keep its ordering against page caching once probe and remainder computation and region upkeep are charged, or in an implemented client-server system?'
version: 1
tags:
- databases
- information-retrieval
date: '2026-10-20'
line: nucleating-argument
summary: >-
  The promotion condition formerly on [THEORY-376](../theory.d/THEORY-376.md), moved unchanged when that
  account was narrowed and promoted on 2026-10-20 on the one simulation it
  rests on ([ADR-047](../decisions.d/ADR-047.md) v3). Open: whether semantic caching's advantage survives
  charging the client for reasoning about what its cache holds.
---

# QUESTION-237: Does semantic caching keep its ordering against page caching once probe and remainder computation and region upkeep are charged, or in an implemented client-server system?

## Why it is a question

[THEORY-376](../theory.d/THEORY-376.md) holds what Dar, Franklin, Jónsson, Srivastava and Tan ([LIT-1113](../literature.d/LIT-1113.md))
simulated: describing cached data by the predicates of past queries matched
page caching on a clustered index, beat it on an unclustered one, and on an
unindexed attribute with a disk cache answered over 60% of 1% queries
without the server. The simulation charged nothing for computing probe and
remainder queries, whose formulas need not be convex or connected, or for
maintaining region descriptions. The saving it measured is the gross
saving.

## What would answer it

The condition as it stood, unchanged: a measurement in an implemented
client-server system, or a simulation that charges the client for
computing probe and remainder queries and for maintaining region
descriptions, that reproduces the ordering (semantic caching about equal to
page caching under good clustering, better under bad clustering, and faster
when queries are answered wholly from cache). A further simulation that
leaves reasoning about cache contents free does not answer it.
