---
number: 376
status: Active
formerly:
- THEORY-tmpgvxim
title: "In a simulated single-client, read-only database answering selection queries on one relation, describing cached data by the predicates of past queries let each query be answered partly from cache, with only the remainder Q ∧ ¬V sent to the server; this matched page caching on a clustered index, beat it on an unclustered one, and, on an unindexed attribute with a disk cache, answered over 60% of 1% queries without contacting the server; the cost of computing probe and remainder queries was not charged"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-376 (batch 073, ADR-047 v3): one simulation study read in full in
    NOTE-904. The 60% figure now carries the condition under which it was
    measured (1% queries on an unindexed attribute with a disk cache), and
    the clustering comparison names the indexes. The promote_when, which
    asked for an implemented system or a simulation that charges the cache
    reasoning, moves unchanged to QUESTION-tmp4iwgh.
tags:
- databases
- information-retrieval
date: '2026-10-15'
source:
- LIT-1113
summary: >-
  Dar, Franklin, Jónsson, Srivastava and Tan (1996), [LIT-1113](../literature.d/LIT-1113.md), read in
  [NOTE-904](../notes.d/NOTE-904.md). In one simulator (one client, one server, a 10,000-tuple
  relation, 90% of queries in a hot 10%), semantic caching performed about
  like page caching on a clustered index, far better on an unclustered one,
  and on an unindexed attribute answered over 60% of 1% queries with no
  server scan. Space overhead depended on coalescing: 55 regions and about
  275 factors for 1% queries without it. The result is measured, not proved;
  updates, joins and the CPU cost of reasoning about the cache's contents
  were left out, so it does not show that predicate-described storage pays
  when finding the reusable part is costly.
---
<!-- inactive-ok-file: CLAIM-303 THEORY-375 — Proposed; the reuse-pricing claim this is set beside and the same paper's replacement results, named, not leaned on -->

# THEORY-376: In a simulated single-client, read-only database answering selection queries on one relation, describing cached data by the predicates of past queries let each query be answered partly from cache, with only the remainder Q ∧ ¬V sent to the server; this matched page caching on a clustered index, beat it on an unclustered one, and, on an unindexed attribute with a disk cache, answered over 60% of 1% queries without contacting the server; the cost of computing probe and remainder queries was not charged

## Source

Dar, Franklin, Jónsson, Srivastava and Tan (1996), [LIT-1113](../literature.d/LIT-1113.md), VLDB 1996,
pp. 330–341, read in full in [NOTE-904](../notes.d/NOTE-904.md) from the VLDB Endowment's copy.

## What was actually shown

The cached part of a relation is described by a constraint formula V. A
query Q splits into a probe Q ∧ V, answered locally, and a remainder
Q ∧ ¬V, sent to the server as a query. Cached tuples are grouped into
disjoint semantic regions shaped by past queries; a query overlapping n
regions can leave 2n + 1. Regions with equal replacement values are merged
when one is under 1% of the cache.

A simulation (CSIM; 250 Kb client cache; 4 Kb pages; 50 warm-up and 500
measured queries, three runs) compared this with page and tuple caching.
On the clustered indexed attribute all three were similar, tuple caching
worst through overhead. On the unclustered indexed attribute page caching
"performs far worse". On an unindexed attribute with a disk cache, where
every server request costs a full scan, "over 60% of the small (1%)
queries are answered completely from the client's cache", and semantic
caching was faster for small queries; once no query fits wholly in cache it
equals ignoring the cache. Overhead was 6.5% of the cache for page caching
and 15.2% for tuple caching; for semantic caching it depended on query size
and coalescing ("For 1% queries, there are 55 regions and nearly 275
factors" without coalescing), and was over four times higher in a
two-attribute space than in one, for small queries without coalescing.

Could have come out otherwise: the probe-and-remainder mechanism could
have lost to tuple caching through region overhead, or failed to find
whole answers in cache often enough to avoid server scans.

## What this does not say

- **That finding the reusable part is cheap.** "We also do not model the
  CPU cost of cache management at the client." The containment and
  difference computations on formulas, which need not be convex or
  connected, are free in every result.
- **Anything with updates.** The study is read-only; consistency,
  invalidation and staleness are absent.
- **Anything beyond selections on one relation.** Joins and general
  queries are future work in the paper.
- **That it holds outside one simulator.** No implemented system, one
  synthetic relation, one skewed workload; a tenfold scale-up gave
  "nearly identical" relative results.
- **That partial reuse of an argument works the same way.** The mechanism
  needs answers stored with a description in the language questions arrive
  in, so that overlap is computable.

## Connections

- [CLAIM-303](../claims.d/CLAIM-303.md) prices reuse per use at a fixed reconstruction cost; here the
  saving per use is the overlap of the new question with what is stored,
  and the access term c_a is a containment test, which the paper does not
  cost.
- [THEORY-375](THEORY-375.md): the same paper's replacement results.
- [THEORY-356](THEORY-356.md) and [THEORY-350](THEORY-350.md) (view selection under space and upkeep budgets)
  choose what to store ahead of queries; here everything fetched is stored
  and the question is what to drop.

## Note of 2026-10-20: narrowed and promoted

The promotion audit (batch 073) narrowed the title and promoted it on the
one study it rests on, under [ADR-047](../decisions.d/ADR-047.md) v3. [LIT-1113](../literature.d/LIT-1113.md) was read in full in
[NOTE-904](../notes.d/NOTE-904.md), with its tables and figures read from page images. The old title
gave "answered over 60% of small queries without contacting the server"
without its condition; the paper reports it for 1% queries on an unindexed
attribute with a disk cache, where every server request is a full scan,
and the title now says so (a correction, not a dropped thesis). "Good" and
"bad clustering" become the clustered and unclustered indexed attributes
the paper compared. The former promote_when moves unchanged to
[QUESTION-tmp4iwgh](../questions.d/QUESTION-tmp4iwgh.md).
