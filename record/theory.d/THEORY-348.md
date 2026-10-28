---
number: 348
status: Active
formerly:
- THEORY-tmplx6hr
title: "When staying in one state costs a fixed amount per request and leaving it costs a fixed one-time price, switching once the extra cost paid for staying equals that price is within 2 of the offline optimum on every request sequence, and no deterministic online rule does better; with a third option the best guaranteed ratio rises to 3"
version: 1
tags:
- databases
- mathematics
date: '2026-10-15'
source:
- LIT-1096
summary: >-
  Karlin, Manasse, Rudolph and Sleator (1988), [LIT-1096](../literature.d/LIT-1096.md), read in
  [NOTE-893](../notes.d/NOTE-893.md). A snoopy cache holding a shared block pays 1 per write to
  keep it current, or drops it and pays p to fetch it again on a later
  read. Dropping once the writes charged since the last read have cost p
  is strongly 2-competitive (Theorems 3.1 and 4.1); with a read- or
  write-through option the deterministic lower bound is 3 (Theorem 3.3).
  It is the first competitive analysis of a rent-or-buy decision, though
  the paper never uses the name, and its instance is when to stop
  maintaining a copy. Prices are fixed and known, the guarantee is worst
  case only, stale reads are forbidden rather than priced, and the
  authors call the practical significance "unclear".
supports:
- CLAIM-308
bears_on:
- QUESTION-114
---
<!-- inactive-ok-file: CLAIM-303 — Proposed; named as a claim this account bears on, not leaned on -->

# THEORY-348: When staying in one state costs a fixed amount per request and leaving it costs a fixed one-time price, switching once the extra cost paid for staying equals that price is within 2 of the offline optimum on every request sequence, and no deterministic online rule does better; with a third option the best guaranteed ratio rises to 3

## Source

Karlin, Manasse, Rudolph and Sleator (1988), [LIT-1096](../literature.d/LIT-1096.md), Algorithmica 3,
"Competitive snoopy caching", read in full in [NOTE-893](../notes.d/NOTE-893.md) from a scan of
the published article.

## What was actually shown

**The setting.** Caches on a shared bus serve a sequence of reads and
writes. A cache holding a replicated block pays one bus cycle for every
write to it by another processor; dropping the block is free now and
costs p, a block fetch, at the next read. An online algorithm "is
c-competitive (or simply competitive) if its cumulative cost on any
sequence (plus a constant) is within a factor of c of the cost of the
optimal off-line algorithm on the same sequence".

**The rule.** Algorithm dsc keeps a counter per cached block, set to p on
a fetch and decremented for each write charged to that cache; at zero the
block is dropped. The paper states the principle generally: "the change
from a state A to a state A' is made when the cost of making the change
equals the extra cost incurred due to being in state A instead of A'."

**The bounds.** Theorem 4.1: C_dsc(σ) ≤ 2·C_A(σ) + k for every sequence
and every algorithm A, online or offline. Theorem 3.1: no deterministic
online algorithm guarantees better than 2; the adversary reads the moment
a block is dropped, so between two reads with k writes the online rule
pays k + p and the offline one min(k, p). Theorem 3.3: with Supplythrough
and Updatethrough (serving a request without taking the block) the lower
bound is 3, and the algorithm given (Theorem 6.1) is 3-competitive
ignoring writebacks, 4 counting them. Theorem 3.2: no online algorithm is
best in a strong sense. With associative caches the bound becomes the
paging ratio of Sleator and Tarjan (Theorems 5.1–5.4).

**What could have come out otherwise.** A single request sequence on
which dsc paid more than twice the offline optimum, beyond the additive
constant, would refute Theorem 4.1; one online rule guaranteeing a ratio
below 2 would refute Theorem 3.1.

## What this does not say

- **That the bound survives changing prices.** r and p are constants the
  algorithm knows; the bound is about uncertainty in the sequence only.
  When the per-use cost drifts, as a search does when a pile grows or
  copies are added, the counting rule still makes sense but its ratio is
  not proved here.
- **That it covers many options.** The 2 needs exactly two states. A third
  raises the deterministic bound to 3, and nothing here bounds the
  general case.
- **That it is the source of the name or the orientation.** The paper never
  says rent, buy or ski. Its rent is upkeep on an idle copy and its
  purchase is reacquiring what was dropped: when to stop maintaining, not
  when to build. Reading it as when to make a bin, or when to file an
  argument, applies the symmetric principle in the mirror direction; that
  transposition is the record's ([NOTE-893](../notes.d/NOTE-893.md)), not the paper's.
- **Anything about staleness or precomputed answers.** Coherence is
  enforced, so a stale read has no price; copies are of stored data, not
  computed results.
- **That worst-case optimality is best on average.** No distribution over
  requests is used. Where one is known, a rule using it may do better; the
  authors call the practical significance "unclear".
- **Anything for randomized rules.** All lower bounds are deterministic.

## Connections

- [QUESTION-114](../questions.d/QUESTION-114.md): a worst-case rule for when a costly one-time
  reorganization pays without a forecast of use. Make it when the extra
  search already spent equals its cost. When the purchase is nearly free,
  as in setting a found brick aside ([CASE-094](../cases.d/CASE-094.md)), the rule says switch
  at once. It answers the question's "paid once" term under fixed prices
  and two options.
- [THEORY-338](THEORY-338.md) is the method's source; the two results are the
  question's two worst-case answers, reorganizing at use when that is
  free, and a costly reorganization at the break-even point.
- [CLAIM-303](../claims.d/CLAIM-303.md) holds that recurrence is evidence of reuse, not the criterion.
  Under worst-case evaluation, recurrences weighted by reconstruction cost
  are the criterion and within 2 ([NOTE-893](../notes.d/NOTE-893.md)); this bears against that
  clause where no distribution over reuse is available.
- Bruno and Chaudhuri 2007 ([LIT-1095](../literature.d/LIT-1095.md)) build and drop indexes by a
  rule of this shape without citing it.
- [THEORY-386](THEORY-386.md) (Olston, Loo and Widom 2001): once staleness is
  tolerated, the two-state choice becomes a continuum of interval widths
  with an interior optimum, and keeping or dropping a copy is its endpoint.
  Their adaptive width rule, like the break-even rule, needs no forecast,
  but it is justified in expectation, not in the worst case, so it neither
  extends nor weakens the factor of 2.
