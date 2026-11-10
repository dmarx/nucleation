---
number: 238
status: Open
formerly:
- QUESTION-tmpcef4k
title: 'Does database cracking keep its measured costs against a scan and an upfront sort in another implementation, measured over a long sequence of random range queries?'
version: 1
tags:
- databases
date: '2026-10-20'
line: distributed-agency
summary: >-
  The promotion condition formerly on [THEORY-333](../theory.d/THEORY-333.md), moved unchanged when that
  account was promoted on 2026-10-20 on the one study it rests on ([ADR-047](../decisions.d/ADR-047.md)
  v3). Open: whether cracking's measured first-query overhead, per-query
  convergence and break-even against sort-then-search hold outside Idreos,
  Kersten and Manegold's MonetDB runs.
refines:
- QUESTION-114
---

# QUESTION-238: Does database cracking keep its measured costs against a scan and an upfront sort in another implementation, measured over a long sequence of random range queries?

## Why it is a question

[THEORY-333](../theory.d/THEORY-333.md) holds what Idreos, Kersten and Manegold ([LIT-1090](../literature.d/LIT-1090.md)) measured in
MonetDB on 10^7 integers under uniformly random ranges: a first cracking
select about 40% dearer than a scan and far cheaper than sorting, per-query
cost falling with use, and sorting overtaking cracking in cumulative cost
only after about 10^5 queries. That is one implementation on one machine
with no variance reported. Until 2026-10-20 the account's promote_when
asked for an independent measurement, and under [ADR-047](../decisions.d/ADR-047.md) v3 that request
moves here.

## What would answer it

The condition as it stood, unchanged: an independent measurement, in
another implementation or another paper, of cracking against a plain scan
and an upfront sort on an in-memory column under random range queries,
reporting per-query and cumulative cost over a long query sequence. It is
answered yes if the ordering and the order of magnitude of the break-even
hold, and no if cracking's first query costs a multiple of a scan or its
per-query cost stalls as the index grows.
