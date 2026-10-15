---
status: Open
title: Is sorting a collection amortized search, and does physical database design,
  where a table is stored in one order and every further index is paid for in space
  and upkeep, give the joint cost
  model that the question on amortized retrieval lacks?
version: 1
tags:
- information-retrieval
- databases
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
<!-- inactive-ok-file: CLAIM-303 — Proposed; open claims cited as open, nothing here rests on their being settled -->

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

## Candidates, from a survey of 2026-10-15, and four readings

At the owner's request ("I'm wondering if maybe we could benefit from some
work at the intersection of database theory and information retrieval"),
a survey looked for work joining the two. Citations were checked against
Crossref. It found no paper that gives one cost model covering bugs,
filing and bins.

**Read the same day, at the owner's request.** Each split off one part of
the trade, and three of the four corrected how the survey had described
them.

- **Finkelstein, Schkolnick and Tiberio 1988** ([LIT-tmpbs1gh](../literature.d/LIT-tmpbs1gh.md), [NOTE-tmphbty9](../notes.d/NOTE-tmphbty9.md)).
  It chooses indexes and the one clustered order per table ("records can be
  ordered only one way") against a weighted workload, with the System R
  optimizer's own estimates. Costs are access, update, index upkeep and
  storage. The model is **steady-state per period** and has no term for
  the one-time cost of building an index or sorting a table, so it does
  not price "paid once". It chooses ways to reach stored data, not
  precomputed answers, so it does not cover the cockpit's bugs. Upkeep is
  charged at each insert. Letting bricks pile up and sorting later is not
  modelled. It supports [CLAIM-tmpjmtw0](../claims.d/CLAIM-tmpjmtw0.md)'s "one arrangement" and its
  dependence on the query mix, the latter by construction.
- **Yao 1981** ([LIT-tmpxy7er](../literature.d/LIT-tmpxy7er.md), [NOTE-tmp60fit](../notes.d/NOTE-tmp60fit.md)). "Founding cell-probe paper"
  holds. "When sorted order beats other arrangements" does not. Sorted
  order with binary search is optimal only for astronomically large
  universes and cells that hold nothing but keys. For small universes, or
  with one cell of arbitrary encoding, other arrangements beat it. It counts
  lookup cost only, building the table is free, so it says nothing on
  amortization.
- **Idreos, Kersten and Manegold 2007, database cracking** ([LIT-tmpmqtpm](../literature.d/LIT-tmpmqtpm.md),
  [NOTE-tmp6iazx](../notes.d/NOTE-tmp6iazx.md)). It is **amortized search, measured**. Each range query
  partitions in place the part of a copied column it touched, so the index
  grows from use. On 10⁷ integers the first query costs about 40% more
  than a scan, against about 12 times a scan for sorting first. Later
  queries are microseconds, and sorting upfront wins in total only after
  about 10⁵ queries. The claim that only regions of interest get organized
  is asserted, not tested: every workload was uniform. As an analogue of
  [CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md)'s setting a found brick aside, it holds in principle
  (reorganization as a by-product of search) and fails in mechanism.
  Cracking splits everything it searched, needs a sortable key, and
  reorganizes on every query whatever the chance of reuse. The authors say
  a cost model "is needed".
- **Sleator and Tarjan 1985** ([LIT-tmpt85t0](../literature.d/LIT-tmpt85t0.md), [NOTE-tmpy8giy](../notes.d/NOTE-tmpy8giy.md)). For one list
  searched from the front, move-to-front costs at most twice what any
  rule costs on the same sequence, **including rules that know the future
  and rearrange as they go**. A fixed order by access frequency is within
  no constant factor. Their Theorem 3: paying to rearrange ahead of need
  never beats moving the found item for free. In that model sorting ahead
  does not pay, and **[CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md)'s practice of setting a brick aside when
  it is found is the near-optimal one**. The model is one pile, where cost
  is depth, so bins are outside it. The paging half prices not knowing
  future requests (a ratio up to the cache size), for [QUESTION-095](QUESTION-095.md)'s
  caching reading, and nothing on precomputation or staleness.

**What the four give the question.** No joint model. They price separate
terms: steady-state upkeep against per-query savings (Finkelstein), the
cost of the lookup alone (Yao), a measured break-even between organizing
up front and organizing as a by-product of search (cracking), and the price
of not knowing future requests (Sleator and Tarjan). The cockpit's case,
a precomputed answer, is not in any of them. The survey's pointer for it
is Harinarayan, Rajaraman and Ullman 1996 on choosing which answers to
precompute (SIGMOD, 10.1145/233269.233333), not yet read. The finding that
most changes this question is Sleator and Tarjan's: under uncertainty about
what will be wanted, reorganizing at the moment of use is within a
constant of the best possible, so "sorting is amortized search" may be
the wrong framing of what a good collector does.

**Not read.** Comer 1978 (optimal index selection is NP-complete),
Chaudhuri and Narasayya 1997, Karlin et al. 1988 and Bruno and Chaudhuri
2007 (rent-or-buy, applied to indexes), and Athanassoulis et al. 2016
(the RUM conjecture). Kirsh 1995 ([LIT-1076](../literature.d/LIT-1076.md), [NOTE-871](../notes.d/NOTE-871.md)) is already held.
The learned-index line (Kraska et al. 2018) belongs in the anthology.
