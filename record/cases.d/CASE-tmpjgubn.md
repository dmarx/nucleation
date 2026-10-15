---
status: Active
title: 'Two builders sorting one collection: the brick that one bins as red and
  two-wide and the other as a curved connector has a bin that respects both, and
  what the builders cannot share is an arrangement, not a description'
version: 1
standing: fictional
kind: construction
tags:
- contextuality
- information-retrieval
- mathematics
date: '2026-10-15'
line: formal-apparatus
illustrates:
- CLAIM-037
- CLAIM-131
supports:
- CLAIM-tmpjmtw0
summary: >-
  The example the owner's LEGO monograph (Mathematics of Meaning, "The Lego Parable")
  uses for contextuality, rebuilt. As descriptions the two sortings always share
  a joint refinement, the product bin, as [MOM-CLM-137](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-137.md) shows, so they illustrate
  the non-contextual case of [CLAIM-037](../claims.d/CLAIM-037.md) and [CLAIM-131](../claims.d/CLAIM-131.md). As arrangements, with a fixed
  number of bins, they compete, and which wins depends on the queries made and on
  what stands out within a bin. Fictional: the builders and the collection are invented.
---
<!-- inactive-ok-file: LIT-tmp9g55n LIT-tmp95pcw — Deferred; works registered unread, cited for what they would be read for, not leaned on -->
<!-- inactive-ok-file: CLAIM-037 CLAIM-tmpjmtw0 — Proposed or new; open claims cited as open, nothing here rests on their being settled -->

# CASE-tmpjgubn: Two builders sorting one collection: the brick that one bins as red and two-wide and the other as a curved connector has a bin that respects both, and what the builders cannot share is an arrangement, not a description

## The case

The monograph's Example 3.4 (Part II, chapter 3): "Builder A places brick
b in “red-sloped bin”. Builder B places b in “curved-connector bin”. There
is no binning system in which both can be respected without
contradiction."

**As descriptions.** A sorting rule is a function from bricks to values,
f: B → V_f. For any two, h(b) = (f(b), g(b)) is a sorting that refines
both, and f and g are its two projections. So the bin *red, two-wide,
curved, connector* respects both builders. [MOM-CLM-137](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-137.md) makes the point
in general: the product map is always a joint refinement, so the
monograph's definition of commutation failure is satisfied by no pair of
sortings. [MOM-ARG-047](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/arguments.d/ARG-047.md) adds that the events such sortings generate are a
subalgebra of the power set of B, and so distributive; it is the lattice
of partitions, not of events, that fails distributivity. A brick has all
its properties at once. That is a hidden-variable model, the
non-contextual case of [CLAIM-037](../claims.d/CLAIM-037.md), and a compatible family of sortings
glues as [CLAIM-131](../claims.d/CLAIM-131.md) says sections of an event sheaf do.

**As arrangements.** A worked instance, fixed here for the claim it
supports. The collection is 1,000 bricks: ten part shapes in ten colours,
ten copies of each kind. There are ten bins, so the product's hundred
cells cannot each have one.

- **By shape.** Each bin holds a hundred bricks of one shape in ten
  colours. To fetch a red 2×4, open the 2×4 bin and find red.
- **By colour.** Each bin holds a hundred bricks of one colour in ten
  shapes. Open the red bin and find the 2×4.

If the remaining search is serial, both cost the same. The ten copies of
the wanted kind sit among ninety others, and the expected number of
others examined before the first copy is 90/11 ≈ 8.2. That figure is
m/(c+1) for m distractors and c copies in random order, and the record
re-checked it by simulation ([CLAIM-tmp6u639](../claims.d/CLAIM-tmp6u639.md)). The arrangements come apart in two
ways the count leaves out:

1. **What stands out in the bin.** Ten distinct colours in a shape bin
   can be told apart at a glance. Ten similar shapes in a colour bin
   cannot. That is the owner's black brick ([CASE-tmpd5exw](CASE-tmpd5exw.md)), and the
   visual-search literature's similarity effect ([LIT-tmp9g55n](../literature.d/LIT-tmp9g55n.md), [LIT-tmp95pcw](../literature.d/LIT-tmp95pcw.md), unread).
   Then sorting by shape leaves the easy search for search time.
   Collections with near-identical colours reverse this. LEGO's two
   greys, the older and the bluish ones, are the familiar instance.
2. **What the builder asks for.** A builder who wants *any red piece
   that fits* opens one bin under the colour sort and ten under the
   shape sort. A builder who wants *any 2×4* has the opposite costs. A
   hundred bins would serve both, at ten times the bins. Finding the
   bin then becomes a search of its own: if bins are found by scanning
   their labels, the expected cost is about k/2 + N/(2k) for N bricks
   in k bins, least near k = √N. Labelled bins in a fixed place, which
   spatial memory finds at once, take most of that cost away.

## What it can show

That "no shared sorting" is false of descriptions and true of
arrangements under a budget. The builders do not disagree about any
brick. They disagree about which partition the bins should realize. That
choice is a trade among bins, search time and query mix, not a failure
of global truth assignment.

## What it cannot show

- Contextuality of any kind. Real contextuality needs observables with no
  pre-existing joint value. [MOM-CLM-137](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-137.md) lists measurements that disturb,
  non-commuting operators, and partial functions on context-dependent
  domains. None of these is a LEGO brick.
- That builders in fact choose as the cost model predicts. Nothing was
  measured.
