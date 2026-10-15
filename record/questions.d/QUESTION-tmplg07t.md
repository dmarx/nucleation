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

## Candidates, from a survey of 2026-10-15

At the owner's request ("I'm wondering if maybe we could benefit from some
work at the intersection of database theory and information retrieval"),
a survey looked for work joining the two. Citations were checked against
Crossref; none of these is registered or read yet. The survey found no
paper that gives one cost model covering bugs, filing and bins. It found
an exact model for databases, and a framework for when doing work early
pays that does not depend on the medium.

- **Physical design as a cost model.** Finkelstein, Schkolnick and Tiberio
  1988 (ACM TODS, 10.1145/42201.42205) choose indexes and the one
  clustered order per table against a query workload, weighing query
  benefit against update and storage cost. Comer 1978 (ACM TODS,
  10.1145/320289.320296) proves optimal index selection NP-complete.
  Harinarayan, Rajaraman and Ullman 1996 (SIGMOD, 10.1145/233269.233333)
  choose which answers to precompute under a space budget, the nearest
  thing to speed bugs. Chaudhuri and Narasayya 1997 (VLDB) is the
  workload-driven practice.
- **Should the collection be sorted at all?** Yao 1981, "Should tables be
  sorted?" (JACM, 10.1145/322261.322274), the founding cell-probe paper:
  when storage in sorted order beats other arrangements for lookup.
- **Indexing as a side effect of search.** Idreos, Kersten and Manegold
  2007, "Database cracking" (CIDR). Each query partly sorts the column it
  touches, so the index grows from use, which is [CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md)'s practice
  of setting a brick aside when it is found.
- **When paying early pays, online.** Sleator and Tarjan 1985 (CACM,
  10.1145/2786.2793): move-to-front lists are within a constant of the
  best arrangement, which is putting the brick just used on top, made
  rigorous. Karlin et al. 1988 (Algorithmica, 10.1007/BF01762111):
  rent-or-buy, deciding when to stop paying per use and pay once. Bruno
  and Chaudhuri 2007 (ICDE, 10.1109/ICDE.2007.367928) apply it to
  building and dropping indexes as the workload shifts.
- **The trade stated as a triangle.** Athanassoulis et al. 2016, the RUM
  conjecture (EDBT): no access method is best at once on read cost,
  update cost and memory. It is a conjecture, not a proof.

Kirsh 1995 ([LIT-1076](../literature.d/LIT-1076.md), read in [NOTE-871](../notes.d/NOTE-871.md)) is already held. It is the
cognitive counterpart, with Tarjan's amortization cited by name. The
learned-index line (Kraska et al. 2018) is machine learning and belongs
in the anthology.
