---
number: 338
status: Active
formerly:
- THEORY-tmpb49hk
title: "For a list searched from the front, where reaching the i-th item costs i, moving each found item to the front costs at most twice what any rule costs on the same sequence, including rules that know the future (four times counting its own moves), a fixed order by access frequency is within no constant factor, and paying to rearrange ahead of need never helps; for paging, no online rule beats the offline optimum by less than n/(n − n_MIN + 1), and LRU meets that bound"
version: 1
tags:
- databases
- mathematics
date: '2026-10-15'
source:
- LIT-1093
summary: >-
  Sleator and Tarjan (1985), [LIT-1093](../literature.d/LIT-1093.md), read in [NOTE-903](../notes.d/NOTE-903.md). With no
  probabilistic assumption, move-to-front on a sequentially scanned list is
  within 2 of the best algorithm in its class on every sequence, the rival
  being free to rearrange as it goes and to know the whole future; a list
  sorted once by frequency, transpose and frequency count are not within
  any constant; and any algorithm can be replaced by one no more expensive
  that makes no paid rearrangement (Theorem 3). For paging the online
  price of not knowing the future is n/(n − n_MIN + 1), the size of fast
  memory when the memories are equal. It is one list, or one two-level
  memory, with uniform items: it says nothing about bins, partitions or
  search that is not a scan.
bears_on:
- QUESTION-114
---

# THEORY-338: For a list searched from the front, where reaching the i-th item costs i, moving each found item to the front costs at most twice what any rule costs on the same sequence, including rules that know the future (four times counting its own moves), a fixed order by access frequency is within no constant factor, and paying to rearrange ahead of need never helps; for paging, no online rule beats the offline optimum by less than n/(n − n_MIN + 1), and LRU meets that bound

## Source

Sleator and Tarjan (1985), [LIT-1093](../literature.d/LIT-1093.md), Communications of the ACM 28(2),
read in full in [NOTE-903](../notes.d/NOTE-903.md) from the published article on Sleator's
page: Theorems 1–6, with the formulas checked against page images.

## What was actually shown

**The model.** An unsorted list for access, insert and delete, searched
from the front: "Accessing or deleting the ith item in the list costs i.
Inserting a new item costs i + 1, where i is the size of the list before
the insertion." After an access an item may be moved forward free; any
other exchange of adjacent items costs 1. The comparison class is every
algorithm that works this way, online or offline.

**Move-to-front is within 2 (Theorem 1).** For any algorithm A and any
sequence s from the empty set, C_MF(s) ≤ 2C_A(s) + X_A(s) − F_A(s) − m,
where X and F count A's paid and free exchanges. In the paper's words,
"The constant factor is 2 if we do not count the updating cost incurred
by move-to-front and 4 if we do", and "What this means is that knowledge
of future operations cannot significantly help to reduce the cost of
current operations." Differing initial lists add at most n(n−1)/2.
Moving partway, at least k/d − 1 places, keeps a factor d times worse
(Theorem 2), and the bound extends to position costs with nonincreasing
increments (Theorem 4).

**Static and counting rules are not.** Transpose and frequency count are
within no constant factor, and "The same example with the insertions
omitted shows that using a static list ordered by decreasing access
frequency is not within a constant factor of optimal."

**Rearranging ahead does not pay (Theorem 3).** "Let A be an algorithm
for a sequence s of insertions and accesses. Then there is another
algorithm for s that is no more expensive than A and does no paid
exchanges." The proof postpones each paid exchange past the next access,
where it becomes free or costs nothing extra.

**Paging (Theorems 5–6).** With n_A pages of fast memory against Belady's
MIN with n_MIN, every online rule faults at least n_A/(n_A − n_MIN + 1)
times as often as MIN on arbitrarily long sequences, and LRU and FIFO
meet that up to an additive n_MIN. With equal memories the ratio is n:
"any on-line paging algorithm makes a number of faults in the worst case
that exceeds the minimum by a factor equal to the size of fast memory."
A larger cache restores a constant.

**What could have come out otherwise.** The bounds are worst case over
all sequences, so a single sequence on which move-to-front paid more than
twice the best algorithm would refute Theorem 1. The proofs are by a
potential function (inversions between the two lists), and the negative
results are explicit sequences.

## What this does not say

- **That moving the found item is within 2 of the best arrangement in
  general.** The rival is the best algorithm in one class: a single list,
  scanned one item at a time, uniform items, cost by position. Hash
  tables, trees, bins and any search that skips the scan are outside it.
- **That sorting never pays.** Theorem 3 is about paid exchanges in that
  list. Replacing a scan by a choice of bin and a scan within it is a
  different cost function, and nothing here prices it.
- **That prediction is worthless everywhere.** In the list it buys at
  most a factor of 2. In paging with equal memories it can buy a factor
  of n.
- **Anything about the physical cost of moving items, the arrival of new
  kinds, staleness, upkeep or precomputed answers.** None is in the
  model; bookkeeping is free.
- **That the competitive ratio predicts practice.** The bounds are worst
  case; average behaviour is not measured here.

## Connections

- [QUESTION-114](../questions.d/QUESTION-114.md): within one pile searched from the top, sorting ahead
  of need does not pay, and setting the found item on top, as in
  [CASE-094](../cases.d/CASE-094.md), is within 2 of the best possible policy. This answers the
  question for that model, and against its framing of sorting as a
  one-off payment against later retrievals.
- [THEORY-348](THEORY-348.md) takes this paper's method, quotes its paging bound, and
  applies the same worst-case comparison to a one-time cost weighed
  against a per-use cost. The 2s have different sources.
- [QUESTION-095](../questions.d/QUESTION-095.md)'s caching reading gets one term from the paging half: the
  price of not knowing future requests under a fixed cache.
