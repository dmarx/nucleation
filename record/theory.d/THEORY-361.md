---
number: 361
status: Active
formerly:
- THEORY-tmp095vr
title: "When every object but one has full grade in exactly one of two attribute-sorted lists and the one has full grade in both, finding it under min takes at least about half the objects' worth of accesses for any algorithm that only reads the lists from the top and looks up objects already seen, and, with the tied objects in random order, about as many in expectation even for algorithms that may look up any object; a query on one attribute alone costs k accesses whatever the number of objects"
version: 1
tags:
- databases
- information-retrieval
date: '2026-10-15'
source:
- LIT-1115
summary: >-
  Fagin, Lotem and Naor (2001; full version read as arXiv cs/0204046v1),
  [LIT-1115](../literature.d/LIT-1115.md), read in [NOTE-924](../notes.d/NOTE-924.md): Example 6.3 and Theorem 6.4, the
  paper's proof that no algorithm is instance optimal once lucky lookups
  are allowed. With 2n + 1 objects, n + 1 high in each list and only one
  high in both, an algorithm that cannot guess must read at least n + 1
  entries before it sees the target, and on a randomized family any
  deterministic algorithm needs at least n + 1 accesses in expectation.
  The paper uses the case to bound instance optimality. That it explains
  linear conjunction-search slopes in human vision is the record's
  analogy, not the paper's claim.
supports:
- CLAIM-310
---
<!-- inactive-ok-file: LIT-1081 — Unavailable; the rival account of visual search, named as unread -->

# THEORY-361: When every object but one has full grade in exactly one of two attribute-sorted lists and the one has full grade in both, finding it under min takes at least about half the objects' worth of accesses for any algorithm that only reads the lists from the top and looks up objects already seen, and, with the tied objects in random order, about as many in expectation even for algorithms that may look up any object; a query on one attribute alone costs k accesses whatever the number of objects

## Source

Fagin, Lotem and Naor (2001), [LIT-1115](../literature.d/LIT-1115.md), read in full in [NOTE-924](../notes.d/NOTE-924.md)
from the authors' full version (arXiv cs/0204046v1): Example 6.3, Theorem
6.4 and its proof, Section 6's discussion of ties, and footnote 9.

## What was actually shown

**The database (Example 6.3).** Objects 1, …, 2n + 1, two lists, t = min,
k = 1. In L1 objects 1, …, n + 1 have grade 1 and the rest 0; L2 lists
the objects in reverse order, so n + 1, …, 2n + 1 have grade 1. Every
object except n + 1 has grade 1 in one list and 0 in the other; object
n + 1 alone has 1 in both and is the unique answer. It sits in the middle
of both lists, at the bottom of a block of ties. An algorithm that guesses
it and looks it up twice can halt at once, but "at least n + 1 sorted
accesses would be required before algorithm A would even see the winning
object" for any algorithm that makes no wild guesses.

**The randomized family (Theorem 6.4).** With L1's order drawn uniformly
at random and L2 its reverse, any deterministic algorithm, guessing
allowed, needs at least n + 1 accesses in expectation before it sees the
winner, and the same holds for probabilistic algorithms that never err
(by Yao's principle). The paper's conclusion is that no algorithm is
instance optimal over all correct algorithms for min of two lists, and
that "The heart of this example ... is the fact that there may be multiple
objects with the same grade in some list."

**The single-attribute case.** With one list, the threshold is the last
grade read, and the threshold algorithm stops after k sorted accesses
whatever N is. That follows from the algorithm's definition; the paper
states the related fact that for max "TA halts after k rounds of sorted
access".

**What could have come out otherwise.** An algorithm that, on the
randomized family, found the winner in fewer than n + 1 expected accesses
would refute the bound.

## What this does not say

- **That human conjunction search is linear for this reason.** Treisman
  and Gelade's conjunction displays ([THEORY-358](THEORY-358.md)) have this structure: each
  distractor carries one of the target's two features and the target
  carries both. The paper's lower bound is a count of accesses under an
  access model of sorted lists and lookups. Reading feature maps as sorted
  lists is the record's analogy. The bound fits the direction of
  [THEORY-358](THEORY-358.md)'s contrast without bearing on its mechanism, feature
  integration against similarity ([LIT-1081](../literature.d/LIT-1081.md)).
- **Anything about the absent case or the 1:2 slope ratio.** The paper
  does not analyse a database with no target.
- **That conjunctive queries are always linear.** This is the
  anti-correlated case. When the two lists' orderings are independent,
  Fagin's Algorithm is reported to cost O(√(Nk)) for two lists
  ([THEORY-379](THEORY-379.md)). When the attributes are positively correlated the cost
  can be far lower. The cost of a conjunctive query depends on how the
  attributes co-occur, not on the query alone.
- **That ties are needed for slow search.** Ties are what defeat instance
  optimality here. With distinct grades and a strictly monotone t, TA is
  instance optimal even against guessing algorithms (Theorem 6.5). The
  paper does not say what an anti-correlated database with distinct grades
  costs.
- **Anything about bins.** A list sorted by the conjunction itself would
  answer this query in k accesses. Which lists to keep is outside the
  model.

## Connections

- [THEORY-358](THEORY-358.md): the same structure of target and distractors, priced in
  accesses instead of milliseconds. It reproduces the feature/conjunction
  contrast's direction and size class (constant against linear), and
  nothing finer.
- [CLAIM-310](../claims.d/CLAIM-310.md), part 3: sorting on one attribute leaves a one-attribute
  search within the bin. On the record's reading, not the paper's, that
  is a scan of one list's tied block in this model, linear in the block's
  size unless the remaining attribute is also sorted within it. The access
  model has no counterpart of pop-out within a bin.
- [THEORY-363](THEORY-363.md) is the result this case limits.
