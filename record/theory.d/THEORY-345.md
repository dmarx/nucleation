---
number: 345
status: Active
formerly:
- THEORY-tmpktrsb
title: "Choosing indexes for a known mix of queries and updates, to minimize query cost plus a per-index upkeep, is NP-hard as the number of attributes and query types grows, and the tools built for it choose one stored order and a set of secondary indexes per table by searching configurations costed with the query optimizer's own estimates, optimal at best relative to those estimates, with no proved guarantee for their heuristics and no term for the one-time cost of building"
version: 1
tags:
- databases
- operations-research
date: '2026-10-15'
source:
- LIT-1089
- LIT-1084
- LIT-1083
summary: >-
  Piatetsky-Shapiro (1983), [LIT-1089](../literature.d/LIT-1089.md), read in [NOTE-902](../notes.d/NOTE-902.md); Finkelstein,
  Schkolnick and Tiberio (1988), [LIT-1084](../literature.d/LIT-1084.md), read in [NOTE-898](../notes.d/NOTE-898.md);
  Chaudhuri and Narasayya (1997), [LIT-1083](../literature.d/LIT-1083.md), read in [NOTE-900](../notes.d/NOTE-900.md).
  Minimum set cover reduces to choosing single-attribute secondary indexes
  under a known workload with a fixed upkeep per index. DBDSGN chooses the
  one clustered order and the secondary indexes per table against a
  frequency-weighted sum of access, update and upkeep costs plus storage,
  read from the System R optimizer; AutoAdmin picks at most k indexes by
  greedy search over what-if indexes. The model is steady state over a
  fixed workload: it prices upkeep against per-query savings, not a
  one-off build or sort against later lookups, and its optimality is
  relative to the optimizer's estimates, never to measured execution.
bears_on:
- QUESTION-114
---
<!-- inactive-ok-file: LIT-1086 — Unavailable; named only to say what is not cited for the hardness -->

# THEORY-345: Choosing indexes for a known mix of queries and updates, to minimize query cost plus a per-index upkeep, is NP-hard as the number of attributes and query types grows, and the tools built for it choose one stored order and a set of secondary indexes per table by searching configurations costed with the query optimizer's own estimates, optimal at best relative to those estimates, with no proved guarantee for their heuristics and no term for the one-time cost of building

## Source

Piatetsky-Shapiro (1983), [LIT-1089](../literature.d/LIT-1089.md), SIGMOD Record 13(2), read in
[NOTE-902](../notes.d/NOTE-902.md). Finkelstein, Schkolnick and Tiberio (1988), [LIT-1084](../literature.d/LIT-1084.md),
ACM TODS 13(1), read in [NOTE-898](../notes.d/NOTE-898.md). Chaudhuri and Narasayya (1997),
[LIT-1083](../literature.d/LIT-1083.md), VLDB '97, read in [NOTE-900](../notes.d/NOTE-900.md). All read in full.

## What was actually shown

**Hardness (Piatetsky-Shapiro).** Given a relation, transaction
frequencies and value statistics, "we want to select the set of indices
which minimizes the average transaction cost." The reduction builds one
relation with one attribute per subset of a set-cover instance, one
conjunctive equality query per element, one update per attribute, equal
selectivity 1/NR, single-attribute indexes, a scan costing NR against one
access through an index, and a uniform upkeep per index smaller than that
saving. The cheapest index set is then a minimum cover. Only the
optimization version is stated, the proof is a half-page sketch (sound
for the instance), and there is no storage or build cost. The author
expected the result to turn effort "toward heuristic algorithms".

**The model in practice (Finkelstein et al.).** For each table, choose
"the ordering rule for the stored records (which determines the
clustered index, if any)" and a set of nonclustered indices, minimizing a
weighted sum of access, tuple-update and index-maintenance costs plus a
weighted storage term, under an optional page limit. Weights may encode
frequency or importance. Without replication, "records can be ordered
only one way", and the
best clustering of one table can depend on another's through the join
method. Costs are the optimizer's: "When we speak of costs in the rest of
this paper, we mean the optimizer's cost estimates; actual execution
costs are explicitly referenced as such." Propositions 1 and 2 make any
configuration's cost the minimum over atomic configurations with one
index per table, so few optimizer calls are needed. With full search,
"the optimal index configurations are found (if we assume the costs
furnished by the optimizer are the actual execution costs)". The
elimination and beam heuristics are claimed to work in experiments not
reported; validation is one worked example.

**The tool (Chaudhuri and Narasayya).** At most k indexes, minimizing
"the sum of the optimizer estimated costs for all the SQL statements in
the workload", with hypothetical indexes costed by loading their
statistics. No frequency weights, no storage term, no build cost.
Candidates are the union of single-query best configurations; enumeration
is an exhaustive seed of m indexes then greedy additions. On five TPC-D
workloads Greedy(2, 4) matched the exhaustive optimum on four and was
within 1% on the fifth, and the whole tool ran in 10–24% of a baseline's
time at 0–7% worse estimated cost. Its one stated guarantee, for
candidate selection, holds only with no updates and no bound on k; the
authors say a greedy step "can be in principle arbitrarily bad".

## What this does not say

- **That a given design problem is hard.** NP-hardness is about growth in
  attributes and query types. A handful of attributes is enumerable;
  Piatetsky-Shapiro reports an exact O(2^√M log M) algorithm for M domains.
- **That the recommended designs are best in execution.** Every optimality
  claim and every quality figure is by the optimizer's estimates.
- **That greedy index selection is near-optimal in general.** The TPC-D
  results are evidence on five workloads, not a bound.
- **That the model prices organizing ahead.** None of the three has a cost
  for building an index or sorting a table. The trade priced is a
  per-period rate of savings against per-period upkeep (and, in
  Finkelstein et al. only, storage): steady state, fixed workload, no
  drift, no deferred upkeep.
- **That it covers precomputed answers or anything like pop-out.** These
  are access paths to stored data; residual predicates are checked tuple
  by tuple.
- **That Comer 1978 proved it.** Finkelstein et al. cite Comer for
  NP-hardness; the record could not obtain it ([LIT-1086](../literature.d/LIT-1086.md), Unavailable),
  and Piatetsky-Shapiro, which the record cites for the workload result,
  does not mention it.

## Connections

- [QUESTION-114](../questions.d/QUESTION-114.md): a part-answer. Physical database design gives an
  exact, workload-weighted model of the steady-state part of the trade,
  and nothing for "paid once", staleness or precomputation.
- [CLAIM-310](../claims.d/CLAIM-310.md)'s "one arrangement" and its dependence on the query mix
  are instances here, the latter by construction, so not a test of its
  defeat condition. The k of AutoAdmin counts secondary orders, not bins.
- [THEORY-348](THEORY-348.md) is where a build cost enters; Harinarayan et al.
  ([LIT-1094](../literature.d/LIT-1094.md)) prove a greedy guarantee for the stored-answer analogue.
- [THEORY-340](THEORY-340.md) is the lookup-cost floor, with building free.
