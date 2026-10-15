---
number: 333
status: Proposed
formerly:
- THEORY-tmp6l5jj
promote_when: >-
  An independent measurement, in another implementation or another paper, of
  cracking against a plain scan and an upfront sort on an in-memory column under
  random range queries, reporting per-query and cumulative cost over a long query
  sequence. It promotes the account if it shows the same shape: a first query
  close to a scan and far below a sort, per-query cost falling with use, and a
  break-even with sorting only after many queries. It refutes it if cracking's
  cumulative cost is not below sorting's over the early queries. Re-reading this
  paper's figures, an analysis without measurement, or a benchmark of a different
  adaptive index cannot settle it. The clause that only queried ranges get
  organized is not part of what promotion requires; only an experiment with a
  skewed or shifting workload that measures how much of the column stays
  unorganized bears on it.
title: "Database cracking, which partitions a copy of a column in place as a side effect of each range query, measured in memory on 10^7 integers under uniformly random ranges, costs about 40% more than a scan on the first query and far less than sorting, gets cheaper per query with use, and stays cumulatively cheaper than sort-then-search until about 10^5 queries; that only the queried ranges get organized is not tested"
version: 1
tags:
- databases
date: '2026-10-15'
source:
- LIT-1090
answers:
- QUESTION-114
summary: >-
  Idreos, Kersten and Manegold (2007), [LIT-1090](../literature.d/LIT-1090.md), read in [NOTE-892](../notes.d/NOTE-892.md). Each
  range select splits, in place, the pieces of a column copy that hold its bounds
  and records the boundaries in an AVL tree, so later queries touch only edge
  pieces. In MonetDB on 10^7 values the first such select took 0.38 s against
  0.27 s for a scan and about 3.3 s for sort-then-search, later selects 10 to
  100 microseconds, and sorting overtook cracking in total only after about 10^5
  queries. Every workload is uniformly random, so the paper's claim that only
  ranges of interest get organized is asserted from the mechanism, not measured;
  there is no cost model and no rule for when a reorganization pays.
---

# THEORY-333: Database cracking, which partitions a copy of a column in place as a side effect of each range query, measured in memory on 10^7 integers under uniformly random ranges, costs about 40% more than a scan on the first query and far less than sorting, gets cheaper per query with use, and stays cumulatively cheaper than sort-then-search until about 10^5 queries; that only the queried ranges get organized is not tested

## Source

Idreos, Kersten and Manegold (2007), [LIT-1090](../literature.d/LIT-1090.md), CIDR, read in full in
[NOTE-892](../notes.d/NOTE-892.md): the mechanism (§§3–5, Algorithms 1–2), Figures 2(a)–(c), 3, 4
and 5, and the research agenda of §8.

## What was actually shown

**The mechanism.** The first range query on an attribute copies the column.
Each select then finds, in a cracker index, the pieces that hold its bounds,
swaps values within those pieces so that values below, inside and above the
range are contiguous, records the new boundaries, and returns the result as a
slice. Pieces wholly inside the range are not touched. The paper's aim:
"index maintenance should be a byproduct of query processing, not of updates."

**The measurements** (MonetDB 5.0alpha, 2.4 GHz Athlon 64, 2 GB, in memory;
10^7 distinct integers; ranges v1 < A < v2 chosen at random):

- First query: "The sort loads the first query with an extra cost of 3 seconds,
  while a simple scan-select needs 0.27 seconds, and the first cracking
  operation costs 0.38 seconds."
- Later queries: per-query cost "highly depends on the size of the piece that
  is being physically reorganized", 10 to 100 microseconds over the run, against
  a few microseconds by binary search on a sorted column. Tuples touched fall by
  an order of magnitude within about ten queries.
- Break-even: for 10^7 values, sorting's cumulative cost drops below cracking's
  "at around 10^5 queries in our current implementation". On 4 × 10^7 values the
  advantage to cracking at 10^5 queries is larger.
- With appended batches and the cracker index discarded, cost rises after each
  batch and falls back within some hundreds of queries.

**What could have come out otherwise.** The first query could have cost a
multiple of a scan, or per-query cost could have stalled while the index grew;
the paper itself notes index upkeep grows with the number of pieces. Neither
happened in these runs. The authors confine the comparison: with a known
workload, time to prepare and no updates, "then sorting is a superior strategy."

## What this does not say

- **That organization follows the workload.** The paper claims "Only database
  portions of past interest are easily localized." Every experiment uses
  uniformly random ranges (or TPC-H query 6, parameters undescribed), so every
  region is eventually queried. That an unqueried region stays unsplit follows
  from the mechanism; how much stays unorganized under a skewed or shifting
  workload is not measured.
- **That there is a cost model.** No expression for per-query or total cost is
  given, and no rule for when a reorganization is worth making; the authors say
  one "is needed".
- **That reorganizing is free.** The first query costs about 30–40% over a scan
  and a full copy of the column per cracked attribute.
- **That it generalizes beyond this setting.** Range selections on an ordered
  key, in memory, one system. Updates, concurrency and out-of-memory data are
  open problems in the paper, and downstream operators had to be changed because
  cracking destroys row order.
- **That it is selective.** It reorganizes on every query whatever the chance of
  reuse, and it splits everything it searched, not only what it found.

## Connections

- For [QUESTION-114](../questions.d/QUESTION-114.md) this is sorting as amortized search in a literal sense,
  with a measured break-even against sorting up front; it does not price the
  terms the question needs in units that carry over.
- [CASE-094](../cases.d/CASE-094.md): the analogy holds for organizing as a by-product of retrieval
  and fails on the mechanism, as [NOTE-892](../notes.d/NOTE-892.md) sets out.
- [LIT-1085](../literature.d/LIT-1085.md) ([THEORY-344](THEORY-344.md)) places cracking among adaptive methods that trade
  read overhead against index-building over time.
- [THEORY-332](THEORY-332.md) prices the decision this paper leaves open: when to build and when
  to drop, against a build cost.
