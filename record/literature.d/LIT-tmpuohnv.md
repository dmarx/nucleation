---
status: Active
status_note: >-
  read in full 2026-10-15 from the VLDB Endowment's open copy of the proceedings
  paper (www.vldb.org/conf/2000/P144.pdf, pp. 144–155; the server needs a browser
  User-Agent). Worth reading as the source of the idea that a cached value can be
  held as an interval its source guarantees, so that staleness becomes a bounded,
  stated imprecision instead of an unknown error, and a query buys precision down
  by paying for exact reads; for SUM, choosing the cheapest reads that meet a width
  R is a 0/1 knapsack problem ([THEORY-tmp4ezx1](../theory.d/THEORY-tmp4ezx1.md)). For [QUESTION-114](../questions.d/QUESTION-114.md) it gives staleness
  a unit (bound width against a query's tolerance) and prices only the query side:
  the source's upkeep that makes the bound a guarantee, and the choice of bound
  widths, are assumed and uncosted, imprecision is a hard constraint rather than
  a loss, and a stale read can never be wrong. For [CLAIM-303](../claims.d/CLAIM-303.md) it sharpens "verification"
  into a per-use decision against a stated tolerance, but rests on a source that
  watches every copy, which a filed argument lacks, so it does not price the cost
  of reusing an obsolete conclusion; it does not bear on [CLAIM-308](../claims.d/CLAIM-308.md)'s rent-or-buy
  argument. [LIT-tmpgbn1t](LIT-tmpgbn1t.md) prices the upkeep side.
title: Offering a Precision-Performance Tradeoff for Aggregation Queries over Replicated
  Data
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: VLDB 2000. Not in Crossref
    (VLDB 2000 has no DOIs); the VLDB Endowment's copy is the source. VLDB 2000
    opened in Cairo on 10 September 2000, which `published:` uses. Not held in the
    Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2)
    for the title and authors found nothing. Read the same day (NOTE-tmpxqtc4).
tags:
- databases
- operations-research
date: '2026-10-15'
published: '2000-09-10'
url: https://www.vldb.org/conf/2000/P144.pdf
first_author: Olston
keywords: []
implementations: []
summary: >-
  Olston and Widom (2000), VLDB 2000. Olston and Widom propose TRAPP: caches hold,
  for each numeric value, an interval its source guarantees to contain the current
  value, the source pushing a refresh whenever the value leaves it. A query carries
  a precision constraint R, and the system chooses which values to fetch exactly
  so that the answer interval is at most R wide whatever the true values, at least
  total refresh cost. For SUM (and AVG without a predicate) that choice is a 0/1
  knapsack problem, NP-complete in general and polynomial with equal costs; COUNT
  and MIN have simple rules. Staleness becomes bounded imprecision, never error,
  and the cost of the source-side upkeep that guarantees this, and of setting the
  bound widths, is outside the optimization. The one experiment is 90 stock prices
  with random costs.
---

# LIT-tmpuohnv: Offering a Precision-Performance Tradeoff for Aggregation Queries over Replicated Data

Olston, C. and Widom, J. (2000). Offering a precision-performance tradeoff for aggregation queries over replicated data. In *Proc. VLDB 2000*, pp. 144–155.

## Key takeaways

Read in full ([NOTE-tmpxqtc4](../notes.d/NOTE-tmpxqtc4.md)). Olston and Widom propose TRAPP: caches hold, for each numeric value, an interval its source guarantees to contain the current value, the source pushing a refresh whenever the value leaves it. A query carries a precision constraint R, and the system chooses which values to fetch exactly so that the answer interval is at most R wide whatever the true values, at least total refresh cost. For SUM (and AVG without a predicate) that choice is a 0/1 knapsack problem, NP-complete in general and polynomial with equal costs; COUNT and MIN have simple rules. Staleness becomes bounded imprecision, never error, and the cost of the source-side upkeep that guarantees this, and of setting the bound widths, is outside the optimization. The one experiment is 90 stock prices with random costs.

## Why this is here

[QUESTION-114](../questions.d/QUESTION-114.md): cached values are held as intervals the source keeps valid, so a cached value is never wrong, only imprecise, and each query fetches the cheapest exact values that meet its precision. Staleness is a hard bound per query here; the trade against refresh cost is in [LIT-tmpgbn1t](LIT-tmpgbn1t.md).
