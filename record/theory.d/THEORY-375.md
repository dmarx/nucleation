---
number: 375
status: Active
formerly:
- THEORY-tmpghhhx
title: 'In one simulator evicting whole query-shaped cache regions, no replacement value function was best on every workload: a value based on distance from the current query beat LRU where queries clustered around a hot region or wandered with loops, while MRU was best on regular cyclic paths, by up to 2.3 times over the distance value and 9.6 times over LRU; none of the functions weighs what a region would cost to fetch again, and nothing is proved'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed first. MRU's margin over LRU on the 32 × 32 square was 9.57,
    and 2.3 was its margin over the distance value (Table 3, NOTE-904);
    and 'larger than the cache' was never measured. Both are corrected as
    kind 3 of ADR-047's routing; whether cycle length relative to cache
    size decides the crossover is carried by QUESTION-tmpbumel. Old title:
    "In one simulator evicting whole query-shaped cache regions, no
    replacement value function was best on every workload: a value based
    on distance from the current query beat LRU where queries clustered
    around a hot region or wandered with loops, while MRU beat both, by up
    to 2.3 times, on regular cyclic paths larger than the cache; none of
    the functions weighs what a region would cost to fetch again, and
    nothing is proved". Promoted to Active under ADR-065, at the status
    review's ruling (the owner delegated these rulings). The title reports
    what one study, read in full in NOTE-904, measured, with the study's
    hedges kept, and nothing in the record contradicts it. The old
    promote_when read: "An analysis, competitive or under a stated
    distribution of query paths, that says when a value based on distance
    from the current query beats recency-based eviction, or experiments in
    another system that vary cycle length relative to cache size and
    recover the crossover. More runs of the same simulator on the same
    synthetic paths do not settle it." Its demand for an analysis, or for
    experiments in another system that recover the crossover, asks for an
    explanation and generality the title does not claim, and moves to
    QUESTION-tmpbumel.
tags:
- databases
- operations-research
date: '2026-10-15'
source:
- LIT-1113
summary: >-
  Dar, Franklin, Jónsson, Srivastava and Tan (1996), [LIT-1113](../literature.d/LIT-1113.md), read in
  [NOTE-904](../notes.d/NOTE-904.md). With semantic regions as the unit of eviction, Manhattan
  distance from the most recent query beat LRU at every query size on a
  skewed selection workload, and a directional variant was best or tied on
  random map paths (LRU within 1.06) and on lollipop paths circling a square
  five or more times; MRU won on a single circuit and on plain squares
  (Manhattan 2.29 and LRU 9.57 on the 32 × 32 square). The study is
  simulation only, with synthetic paths and no refetch cost in any value; it
  shows that the best forecast of reuse depends on the workload, not that
  semantic distance is a robust rule.
---

# THEORY-375: In one simulator evicting whole query-shaped cache regions, no replacement value function was best on every workload: a value based on distance from the current query beat LRU where queries clustered around a hot region or wandered with loops, while MRU was best on regular cyclic paths, by up to 2.3 times over the distance value and 9.6 times over LRU; none of the functions weighs what a region would cost to fetch again, and nothing is proved

## Source

Dar, Franklin, Jónsson, Srivastava and Tan (1996), [LIT-1113](../literature.d/LIT-1113.md), VLDB 1996,
Sections 3.3, 5.3 and 6, read in full in [NOTE-904](../notes.d/NOTE-904.md).

## What was actually shown

When space is short, "the semantic region with the lowest value and all
tuples within that region are discarded from the cache". Values compared:
recency per region (LRU, MRU); the negative Manhattan distance between the
region's centre of gravity and the most recent query's; and a directional
Manhattan distance −(d_par + d_perp) weighting regions ahead of, behind,
left and right of a moving user.

On selections over an unclustered indexed attribute with 90% of queries in
a hot 10%, Manhattan distance beat LRU at all query sizes, because cold
queries' regions lose value at the next hot query instead of ageing out.

On a map of 8,192 × 8,192 one-tuple cells with 128-tuple queries
(Table 3, relative response time, best = 1.00): on four random-path
settings the directional distance was best, LRU 1.01–1.06, MRU 1.04–2.24.
On squares MRU was best (32 × 32: distance 2.29, LRU 9.57; 160 × 160: both
1.22). On a lollipop path MRU won when the square was circled once and
distance won at 5, 10 and 50 circuits; break-even with MRU at 4 rounds.
"This query profile - predictable and cyclic - is ideal for MRU, which is
the clear winner." Footnote 7: with no loops "no value function will
perform well".

Could have come out otherwise: one value function could have been best on
every path.

## What this does not say

- **That semantic distance is robust in general.** The paper says it
  performs robustly across loop sizes; its own table has it 2.29 times
  slower than MRU on the small square.
- **Anything proved.** There is no competitive or average-case analysis;
  the crossover is not explained.
- **Anything about refetch cost.** No value includes it or region size,
  and regions are evicted whole: "Semantic caching discards entire regions
  from the cache, often resulting in poor cache utilization".
- **That it is a rent-or-buy rule.** These are rankings of what to drop,
  not break-even rules of the kind in [THEORY-348](THEORY-348.md).

## Connections

- [CLAIM-308](../claims.d/CLAIM-308.md) concedes that where reuse can be forecast a rule using the
  forecast can do better. Semantic distance is such a forecast; this
  result shows it winning where queries have semantic locality and losing
  on regular cycles, so the right forecast depends on the workload.
- [THEORY-338](THEORY-338.md) (move-to-front and LRU are competitive for lists and paging)
  gives worst-case guarantees for recency; nothing here gives one for
  distance.
- [THEORY-376](THEORY-376.md): the same paper's probe-and-remainder results.
