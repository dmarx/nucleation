---
status: Proposed
title: Sorting schemes over objects with determinate properties never conflict as
  descriptions, since the product of any sortings refines them all; they conflict
  as arrangements, since a fixed number of bins realizes one partition, and which
  costs least depends on what is searched for and on what stands out within a bin
version: 1
role: thesis
defeated_if: >-
  A cost model of retrieval from a sorted collection in which the cheapest arrangement
  for a fixed number of bins does not depend on the query mix, or does not depend
  on how easily the attributes left unsorted are searched. Or a pair of sortings
  of objects with determinate properties that has no joint refinement, which would
  also refute MOM-CLM-137.
tags:
- information-retrieval
- contextuality
- cognition
date: '2026-10-15'
line:
- formal-apparatus
- distributed-agency
grounds:
- CASE-tmpjgubn
- CASE-tmpd5exw
complements:
- CLAIM-131
- CLAIM-037
summary: >-
  What is directionally right in the owner's LEGO monograph, as Mathematics of Meaning
  graded it. Its contextuality claim is empty: any sortings of bricks share a joint
  refinement ([MOM-CLM-137](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-137.md)), and the events they generate stay Boolean ([MOM-ARG-047](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/arguments.d/ARG-047.md)).
  Its intuition that builders cannot share a sorting is true of arrangements. One
  set of bins realizes one partition, the product may need more bins than there
  are, and the cheapest choice depends on what each builder searches for and on
  what stands out within a bin ([CASE-tmpjgubn](../cases.d/CASE-tmpjgubn.md)). The disagreement is a trade, not
  a failure of global truth. Proposed: the cost model is the record's, and the visual-search
  finding it uses is unread.
illustrated_by:
- CASE-tmpd5exw
---
<!-- inactive-ok-file: LIT-tmp9g55n LIT-tmp95pcw — Deferred; works registered unread, cited for what they would be read for, not leaned on -->
<!-- inactive-ok-file: CLAIM-037 CLAIM-296 CASE-tmpd5exw CASE-tmpjgubn — Proposed or new; open claims cited as open, nothing here rests on their being settled -->

# CLAIM-tmpjmtw0: Sorting schemes over objects with determinate properties never conflict as descriptions, since the product of any sortings refines them all; they conflict as arrangements, since a fixed number of bins realizes one partition, and which costs least depends on what is searched for and on what stands out within a bin

## The claim

**As descriptions, no conflict.** For sortings f: B → V_f and g: B → V_g
of the same bricks, h = (f, g) refines both. [MOM-CLM-137](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-137.md): "the product map
is always a joint refinement", so no pair of sortings fails to commute,
and a brick's having all its properties at once is "exactly the
non-contextual" case. That is [CLAIM-037](CLAIM-037.md)'s distinction between formal
contextuality and ordinary context dependence, and [CLAIM-131](CLAIM-131.md)'s
observation that compatible sections of an event sheaf glue. Two
builders who bin the same brick differently are attending to different
coordinates of one value.

**As arrangements, a real trade.** A set of k bins realizes one partition
of the collection at a time. Three things then decide which partition
serves a builder, and none of them is a fact about any brick ([CASE-tmpjgubn](../cases.d/CASE-tmpjgubn.md)):

1. **The bin budget.** The product of the sortings serves every query and
   may need far more bins than are available. If bins are found by
   scanning, more bins also means more scanning. The expected cost
   k/2 + N/(2k) is least near k = √N.
2. **The query mix.** A query that names the sorted attribute opens one
   bin, and a query that leaves it open opens all of them. Builders who
   ask for different things are best served by different partitions.
3. **What stands out within a bin.** If the attribute left unsorted pops
   out, search within the bin is nearly free. If it is similar across
   binmates, search is serial and slow ([CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md)). So sort by what does not
   stand out and search by what does. Which attributes those are depends
   on the collection and on the searcher.

**What survives of the monograph's "Sheafification as Descriptive Compromise".**
Builders who must share one set of bins can take the common refinement
(the meet of their partitions, which costs bins) or the finest common
coarsening (the join, which loses distinctions one of them needed). The
partition lattice is where the non-distributivity the monograph looked
for lives ([MOM-ARG-047](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/arguments.d/ARG-047.md)). It is a lattice of schemes, not of events, and
the compromise is priced in bins and lost distinctions, not in truth.

## Why it is Proposed

Part 1 is elementary. Part 2 is a definition. Part 3 rests on the
similarity effect in visual search, which the record has registered
([LIT-tmp9g55n](../literature.d/LIT-tmp9g55n.md), [LIT-tmp95pcw](../literature.d/LIT-tmp95pcw.md)) and not read. The claim as a whole is a cost model nobody
has fitted to anyone's collection.

## What it does not say

- Not that sorting is never contextual. Observables with no pre-existing
  joint value can be. [MOM-CLM-137](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-137.md) names disturbing measurements and
  partial functions on context-dependent domains. LEGO bricks are not
  among them.
- Not that arrangement changes what is true of the collection. It changes
  what can be found in time, which is [CLAIM-296](CLAIM-296.md)'s subject, and this claim
  supports that one: changing the arrangement alone changes the cost of
  retrieval.
