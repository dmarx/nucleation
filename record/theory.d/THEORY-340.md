---
number: 340
status: Active
formerly:
- THEORY-tmpczun3
title: "For answering membership in a static set of n keys with the fewest worst-case cell reads, sorted order with binary search is optimal only when the key universe exceeds a Ramsey-number threshold and table cells may hold nothing but stored keys or pointer symbols; it is beaten for small universes, and by two probes once one cell may hold an encoded value"
version: 1
tags:
- databases
- mathematics
date: '2026-10-15'
source:
- LIT-1097
summary: >-
  Yao (1981), [LIT-1097](../literature.d/LIT-1097.md), read in [NOTE-891](../notes.d/NOTE-891.md). In the setting later
  called the cell-probe model, where only cells read are counted and both
  the arrangement and the adaptive search are arbitrary, ⌈lg(n+1)⌉ probes
  are needed by any scheme whose cells hold only keys of the set or a fixed
  stock of pointer symbols, once the universe is astronomically large
  (Theorems 1 and 1′). One probe suffices for m ≤ 2n − 2 (Theorem 2), and
  with one extra cell holding any value two probes suffice for
  m ≥ 2^{16n²} (Theorem 3). Building the table is free, so the paper prices
  lookup only and says nothing about whether sorting pays for itself.
---

# THEORY-340: For answering membership in a static set of n keys with the fewest worst-case cell reads, sorted order with binary search is optimal only when the key universe exceeds a Ramsey-number threshold and table cells may hold nothing but stored keys or pointer symbols; it is beaten for small universes, and by two probes once one cell may hold an encoded value

## Source

Yao (1981), [LIT-1097](../literature.d/LIT-1097.md), "Should tables be sorted?", Journal of the ACM
28(3), read in full in [NOTE-891](../notes.d/NOTE-891.md), compared with the Stanford report
STAN-CS-79-753.

## What was actually shown

**The setting.** A static set S of n keys from {1, …, m}; queries "Is j in
S?". A table structure is any rule assigning each n-subset a table; a
search strategy is any fully adaptive sequence of probes. Cost is the
worst-case number of probes. Nothing is charged for building the table or
computing probe locations. The theorems fix n and let m grow.

**Sorted order is optimal, under two conditions (Theorems 1 and 1′).**
Lemma 1: a sorted table, or one under a fixed permutation, needs
⌈lg(n + 1)⌉ probes by any strategy when m ≥ 2n − 1. By Ramsey's theorem,
for m above N(n) = R(2n − 1, n, n!) any table structure behaves like a
permuted sorted table on some 2n − 1 keys, so f(n, m) = ⌈lg(n + 1)⌉.
Theorem 1′ extends this to tables of q cells holding keys of S or p
pointer symbols, covering hashing, search trees and linked lists, with
threshold R(2n − 1, n, (n + p)^q). Yao: "The numbers N(n) in Theorem 1
are extremely large even for moderate n. Thus the result is not too
useful in practical terms."

**Sorted order is beaten (Theorems 2 and 3).** For n = 2, m = 3 a cyclic
table answers in one probe. In general one probe suffices exactly up to
m = 2n − 2 for n > 2 (3 for n = 2), by an explicit scheme that decides
membership without locating the key. With a sorted table plus one cell
holding any integer in [1, m], two probes suffice once m ≥ 2^{16n²}: the
extra cell names a separator that fixes each key's position. Yao's
summary: "when the word size is large, sorted tables are optimal
structures if only the addressing power of a random-access machine can be
used, but far from optimal once arbitrary encoding of the information is
allowed in the table".

**What could have come out otherwise.** A scheme of keys and pointers
alone beating binary search above the threshold would refute Theorem 1′;
the constructions are explicit and checkable.

## What this does not say

- **That sorted storage beats other arrangements.** Under its conditions
  sorted order ties for best; outside them it is beaten.
- **Anything practical about thresholds.** No usable bound on N(n) is
  given, and the intermediate range of m is open except for a cited
  O(1)-probe result when m is polynomial in n.
- **Anything about the cost of arranging.** Building is free and
  unconstrained, so the paper bears nothing on whether sorting is
  amortized search, on build cost against later lookups, or on upkeep.
  Dynamic lower bounds are only conjectured.
- **Anything about averages, query mixes or update costs.** The cost is
  worst case per query.

## Connections

- [QUESTION-114](../questions.d/QUESTION-114.md) listed it as showing when sorted storage beats other
  arrangements; [NOTE-891](../notes.d/NOTE-891.md) found that description wrong. It supplies
  one side of the ledger, the lookup floor, and is not an answer to the
  question's trade.
- [THEORY-345](THEORY-345.md) prices indexes against a workload with building also free;
  [THEORY-338](THEORY-338.md) shows a fixed sorted order losing to a self-adjusting list
  when cost is scan depth. The three agree that the value of sorting
  depends on what else a cell or a step is allowed to do.
