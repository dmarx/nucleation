---
status: Active
title: "When each cached value is an interval its source guarantees to contain the current value, and a query must return an answer interval no wider than R whatever the true values, choosing the cheapest set of exact reads for a SUM is a 0/1 knapsack problem, NP-complete in general and solved by taking the narrowest intervals first when read costs are equal, and for a COUNT with a selection predicate the cheapest choice is the ⌈|T?| − R⌉ cheapest undecided tuples"
version: 1
tags:
- databases
- operations-research
date: '2026-10-15'
source:
- LIT-tmpuohnv
answers:
- QUESTION-114
summary: >-
  Olston and Widom (2000), [LIT-tmpuohnv](../literature.d/LIT-tmpuohnv.md), read in [NOTE-tmpxqtc4](../notes.d/NOTE-tmpxqtc4.md). In TRAPP a cache
  holds intervals that sources keep valid by pushing a refresh whenever a value
  escapes, and each query names a width R its answer may have. The SUM answer
  is the sum of the intervals, so meeting R at least read cost is knapsack
  (profit = read cost, weight = width, capacity = R); COUNT under a predicate
  has a greedy optimum. Staleness becomes bounded imprecision, never error, and
  only the query-time cost of buying it down is optimized: the sources' upkeep,
  the choice of interval widths and any cost of imprecision are outside the
  model. The MIN rule's optimality proof is in an unread technical report.
---

# THEORY-tmp4ezx1: When each cached value is an interval its source guarantees to contain the current value, and a query must return an answer interval no wider than R whatever the true values, choosing the cheapest set of exact reads for a SUM is a 0/1 knapsack problem, NP-complete in general and solved by taking the narrowest intervals first when read costs are equal, and for a COUNT with a selection predicate the cheapest choice is the ⌈|T?| − R⌉ cheapest undecided tuples

## Source

Olston and Widom (2000), [LIT-tmpuohnv](../literature.d/LIT-tmpuohnv.md), VLDB 2000, pp. 144–155, read in full in
[NOTE-tmpxqtc4](../notes.d/NOTE-tmpxqtc4.md) from the VLDB Endowment's copy. Sections 3–6 carry the model and the
results; the proofs for MIN and MAX and the full AVG algorithm are in the
authors' technical report, which the reading did not see.

## What was actually shown

**The model.** Each numeric value V_i has one master at a source; a cache holds
[L_i, H_i]. The source "guarantees that the actual value for O will stay in this
bound, or if the value does exceed the bound then the source will immediately
send a new refresh." A query states a precision constraint R ≥ 0 on the width
of its answer [L_A, H_A]. If the cached bounds do not meet R, the cache picks a
set T_R of values to read exactly, each at a known cost C_i, with costs
additive. The set is chosen in advance, so R must hold for any true values
within the bounds. Time is frozen during a query, and insertions and deletions
reach every cache at once.

**SUM.** [L_A, H_A] = [Σ L_i, Σ H_i], so the width is the sum of the widths of
the values not read. Minimizing the cost of T_R subject to that sum being at
most R is maximizing the cost of the values kept, which is 0/1 knapsack with
profit C_i, weight H_i − L_i and capacity R, so the problem is NP-complete. The
paper uses Ibarra and Kim's approximation (within a fraction ε of the optimal
profit). With equal costs, keeping the narrowest intervals until the next would
exceed R is optimal. AVG without a predicate reduces to SUM with capacity
R·COUNT. Under a selection predicate on bounded columns, undecided tuples (T?)
have their intervals extended to include 0, and the problem stays a knapsack.

**COUNT with a predicate.** The answer is [|T⁺|, |T⁺| + |T?|], so its width is
|T?|, and each exact read removes one tuple from T?. Reading the ⌈|T?| − R⌉
cheapest tuples of T? is therefore optimal.

**MIN.** Reading every tuple with L_i < min_k H_k − R, regardless of cost, is
stated to be optimal; the proof is deferred to the technical report.

**The one experiment.** On 90 stock prices with the day's range as bounds and
random costs between 1 and 10, refresh cost fell continuously as R grew, from
about 4000 at R = 0 to near zero at R = 140.

## What this does not say

- **That staleness has been priced in full.** Only the per-query cost of
  exact reads is optimized. The sources' monitoring of every cached bound and
  the value-initiated refreshes it sends, which are what make a stale read
  safe, are assumed and never costed. How wide to make the bounds, which
  governs that upkeep, is outside the paper ([LIT-tmpgbn1t](../literature.d/LIT-tmpgbn1t.md) takes it up).
- **That imprecision has a cost.** R is a hard constraint the user sets. Nothing
  trades a wider answer against a cheaper one.
- **Anything about stale answers that are wrong.** Under the source's guarantee
  a cached interval is never wrong, only wide. A setting in which a copy can
  drift outside what it claims without anyone noticing is outside the model.
- **That it covers stored answers.** The cached items are base values; every
  aggregate is computed afresh at query time.
- **That the MIN rule's optimality, the AVG refresh choice or the square-root
  bound widths it mentions are established here.** All are deferred to a
  report the record has not read.
- **Anything for joins, batched refresh costs or reads chosen one at a time.**
  Joins have no algorithm; amortized costs and iterative refresh are future
  work.

## Connections

- [QUESTION-114](../questions.d/QUESTION-114.md): the first reading in that line to give staleness a unit,
  bound width against a stated tolerance, and to price buying it down per
  query. [THEORY-348](THEORY-348.md) forbids stale reads and [THEORY-350](THEORY-350.md) refreshes everything in
  a batch; neither prices a tolerated, bounded staleness.
- [THEORY-tmpsvwtz](THEORY-tmpsvwtz.md) and [THEORY-tmph9339](THEORY-tmph9339.md) (Olston, Loo and Widom 2001, [LIT-tmpgbn1t](../literature.d/LIT-tmpgbn1t.md))
  price the other side, the upkeep of keeping intervals valid against the
  fallbacks they cause, and take this paper's refresh selection as their
  query load.
- [CLAIM-303](../claims.d/CLAIM-303.md): per-use verification against a stated tolerance, with
  reconstruction chosen as a knapsack when imprecisions add. The guarantee
  rests on a source that watches every copy, which a filed argument lacks, so
  A11's cost of reusing an obsolete conclusion is assumed away, not priced.
