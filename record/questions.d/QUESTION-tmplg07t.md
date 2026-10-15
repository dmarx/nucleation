---
status: Open
title: Is sorting a collection amortized search, and does physical database design,
  where a table is stored in one order and every further index is paid for in space
  and upkeep, give the joint cost
  model that the question on amortized retrieval lacks?
version: 1
tags:
- information-retrieval
- cognition
- operations-research
date: '2026-10-15'
line: distributed-agency
refines:
- QUESTION-095
summary: >-
  The LEGO parable ([CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md)) is [QUESTION-095](QUESTION-095.md)'s trade in its plainest form.
  Sorting spends search once, against retrievals later, and leaves the result in
  the world, as the cockpit's speed bugs do. [CLAIM-tmpjmtw0](../claims.d/CLAIM-tmpjmtw0.md) adds that one set of
  bins realizes one partition, chosen against a query mix. A database table is stored
  in one physical order, and every further index costs space and work on every insert.
  Choosing indexes for a workload is a studied problem with explicit cost models.
  This asks whether that model is the one [QUESTION-095](QUESTION-095.md) is looking for.
---
<!-- inactive-ok-file: CLAIM-303 CLAIM-tmp6u639 CLAIM-tmpjmtw0 — Proposed or new; open claims cited as open, nothing here rests on their being settled -->

# QUESTION-tmplg07t: Is sorting a collection amortized search, and does physical database design, where a table is stored in one order and every further index is paid for in space and upkeep, give the joint cost model that the question on amortized retrieval lacks?

## Why it is a question

[QUESTION-095](QUESTION-095.md) asks whether leaving a computation's result where it can be
read cheaply is the same trade as amortizing the computation. Its
citation search found pieces and no joint cost model. The LEGO
collection has every part of the trade, with nothing hidden:

- **Paid once.** Sorting N bricks takes about one pass. Pulling one
  hard-to-find kind out of a bin costs about one search, m/(c+1) items
  for c copies among m others ([CLAIM-tmp6u639](../claims.d/CLAIM-tmp6u639.md)). If that is done when the brick is
  found anyway, as in [CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md), it costs nothing more.
- **Saved each time.** Each later retrieval skips that search, so a bin
  pays when expected retrievals times search saved exceed its cost.
  That is [CLAIM-303](../claims.d/CLAIM-303.md)'s condition, "worth its cost only when expected reuse
  covers it", with the terms countable.
- **Staleness.** New bricks arrive unsorted and bins drift as the
  collection grows. The arrangement has upkeep, as a filed argument does
  ([QUESTION-098](QUESTION-098.md)).
- **One arrangement.** One set of bins realizes one partition ([CLAIM-tmpjmtw0](../claims.d/CLAIM-tmpjmtw0.md)),
  chosen against what the builder searches for. A database table has the
  same constraint and the same remedy. A secondary index serves other
  queries at a cost in space and in work on every insert.

The candidate: the index-selection problem in database physical design
is a worked cost model for this trade. It covers a workload of queries,
a budget of space and upkeep, and arrangements that serve some queries
at others' expense. If so, [QUESTION-095](QUESTION-095.md)'s three cases are instances of
it, with retrieval cost counted as computation.

## What would answer it

A reading of the index-selection literature, with a test: does its cost
model price the cockpit's bugs, a filed argument and a LEGO bin with the
same terms, and does it handle cues and search that pops out ([CLAIM-tmpjmtw0](../claims.d/CLAIM-tmpjmtw0.md) part
3), which a database lookup does not have? The record holds no work from
that literature. Registering one is the first step.
