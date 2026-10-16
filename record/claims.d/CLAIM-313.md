---
number: 313
status: Proposed
formerly:
- CLAIM-tmpie11s
title: 'A fixed number of bins realizes one partition only when each item is stored once: with copies, overlapping partitions coexist, as hashing-based similarity search stores each item in many partitions and pays for it in space, so sortings conflict as arrangements only under a one-copy constraint, which binds bricks but not index entries'
version: 1
role: counter
warrant: demonstrated
tags:
- databases
- information-retrieval
- design-rationale
date: '2026-10-15'
line:
- formal-apparatus
- distributed-agency
objects_to:
- CLAIM-310
grounds:
- THEORY-388
- THEORY-372
summary: >-
  Filed at the owner's request, from the readings on locality-sensitive
  hashing (Indyk and Motwani 1998; Andoni, Laarhoven, Razenshteyn and
  Waingarten 2017) set against [CLAIM-310](CLAIM-310.md)'s premise that "a set of k bins
  realizes one partition of the collection at a time". That holds when each
  item is in one place. An index can hold many copies, and hashing-based
  similarity indexes do exactly that, trading the space of the copies against
  query time on an exact curve. It narrows [CLAIM-310](CLAIM-310.md) to collections whose items
  cannot be copied, which includes the LEGO case; it does not touch the claim
  about descriptions.
---

# CLAIM-313: A fixed number of bins realizes one partition only when each item is stored once: with copies, overlapping partitions coexist, as hashing-based similarity search stores each item in many partitions and pays for it in space, so sortings conflict as arrangements only under a one-copy constraint, which binds bricks but not index entries

## The objection

[CLAIM-310](CLAIM-310.md) locates the conflict between sortings in arrangements: "A set
of k bins realizes one partition of the collection at a time." For bricks
that is true, because a brick is in one bin. It is not a fact about bins.
It is a fact about items that cannot be copied.

An index stores references, and references can be copied. Locality-
sensitive hashing builds many hash tables over the same points, each a
different partition, and stores every point in each ([THEORY-388](../theory.d/THEORY-388.md)).
Andoni et al. give the exact price ([THEORY-372](../theory.d/THEORY-372.md)). With each point in
about n^{ρu} lists, a query scans about n^{ρq} of them, and the two
exponents trade along a curve that no hashing-based scheme beats on
random instances. More partitions held at once cost more space and buy
faster queries.

So where items can be copied, several sortings can be arrangements at
once, and the trade [CLAIM-310](CLAIM-310.md) describes becomes a trade of space against
query time, not a choice of one partition. Which partitions to keep, and
how many copies, still depends on the query mix. That part of [CLAIM-310](CLAIM-310.md)
is not touched.

## What it does not say

- That [CLAIM-310](CLAIM-310.md) is wrong about the LEGO case. Bricks are not copied, and
  a builder's k bins do realize one partition.
- That copies are free. Their cost is the point: on the hashing curve,
  each cut in query time is paid for in space.
- That the hashing results transfer to sorting by discrete attributes.
  They concern approximate near-neighbour search. The general point, that
  copies let partitions coexist, needs no theorem. A library catalogue
  filed by author, title and subject at once is an example.
- Anything about descriptions. [CLAIM-310](CLAIM-310.md)'s claim that sortings never
  conflict as descriptions stands.

## How [CLAIM-310](CLAIM-310.md) could answer

It could state the one-copy condition in its title and defeat condition.
Or it could count copies as bins, so that k copies of each item across
k bins realize k partitions, and the budget becomes a budget on storage.
