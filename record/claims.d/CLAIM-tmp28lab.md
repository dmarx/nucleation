---
status: Active
title: 'A search cut off before an exhaustive pass can establish absence when the arrangement certifies that the unsearched remainder cannot hold the item: a sorted table answers non-membership in a logarithmic number of probes, and the Threshold Algorithm stops early with its answer proved, so absence needs a certificate about the remainder, not exhaustion; similarity search in high dimension is where no such certificate exists'
version: 1
role: counter
tags:
- logic
- databases
- information-retrieval
date: '2026-10-15'
line: distributed-agency
objects_to:
- CLAIM-306
grounds:
- THEORY-340
- THEORY-tmp3ren6
- THEORY-tmpazpbe
- THEORY-tmpc74vc
summary: >-
  Filed at the owner's request, from the database readings set against
  [CLAIM-306](CLAIM-306.md)'s asymmetry: presence by one find, absence "only by exhausting the
  collection". Sorted order and the Threshold Algorithm each establish absence
  from part of the collection, because the arrangement bounds what the rest can
  hold. That meets [CLAIM-306](CLAIM-306.md)'s own defeat condition, and the claim is conceded:
  [CLAIM-tmpfpvgq](CLAIM-tmpfpvgq.md) restates it. Where the arrangement gives no bound, as in
  similarity search in high dimension, [CLAIM-306](CLAIM-306.md)'s asymmetry stands.
supports:
- CLAIM-tmpfpvgq
---
<!-- inactive-ok-file: THEORY-tmpc74vc — Proposed; one analysis under uniform data, cited for the regime it describes -->

# CLAIM-tmp28lab: A search cut off before an exhaustive pass can establish absence when the arrangement certifies that the unsearched remainder cannot hold the item: a sorted table answers non-membership in a logarithmic number of probes, and the Threshold Algorithm stops early with its answer proved, so absence needs a certificate about the remainder, not exhaustion; similarity search in high dimension is where no such certificate exists

## The objection

[CLAIM-306](CLAIM-306.md) holds that "absent" is shown "only by a pass that rules out every
place it could be", and is defeated by "a search procedure, under a
deadline shorter than an exhaustive pass, whose failure to find an item
licenses its absence with no assumption that the unsearched part would
also have failed".

Two of the record's readings supply such procedures.

- **A sorted table.** Membership in a static sorted set is decided by
  binary search, and a failed search is a proof of non-membership: the
  order guarantees that every unexamined key lies on the wrong side of
  the probes already made. Yao's question was only when this is the
  cheapest scheme ([THEORY-340](../theory.d/THEORY-340.md)); that it is correct for absence was never
  in doubt.
- **The Threshold Algorithm.** Over lists each sorted by one attribute,
  it stops as soon as the k-th best grade seen reaches the threshold
  formed from the last grades read under sorted access. Nothing unread can
  beat that threshold, so the answer is proved without reading the rest,
  and on every database it costs at most a constant times any correct
  algorithm that makes no wild guesses ([THEORY-tmp3ren6](../theory.d/THEORY-tmp3ren6.md)).

In both, the unsearched part is not assumed to fail. It is shown unable
to hold the item, by an invariant of the arrangement. So the asymmetry is
not between one find and an exhaustive pass. It is between one find and a
certificate about the remainder. Exhaustion is one certificate. Sorted
order, an index and a labelled compartment are others, and they can be far
cheaper.

## Where [CLAIM-306](CLAIM-306.md)'s asymmetry stands

When the arrangement gives no bound on the remainder, a failed search
certifies nothing short of exhaustion. That is the unsorted pile of
[CASE-094](../cases.d/CASE-094.md), and it is also, more surprisingly, similarity search in high
dimension. Where the nearest and farthest neighbours become nearly
equidistant ([THEORY-tmpazpbe](../theory.d/THEORY-tmpazpbe.md)), the bounds a partitioning index uses to
skip blocks prune almost nothing, and a correct search reads nearly every
block ([THEORY-tmpc74vc](../theory.d/THEORY-tmpc74vc.md), under uniform data). "There is nothing like it
here" then has no certificate cheaper than a scan, however the collection
is organized.

## What it does not say

- That the medic's search had a certificate. A cabinet of compartments
  searched by eye under stress has none of these invariants.
- That every arrangement certifies absence. A sort certifies absence only
  for the attribute it is sorted on; a query on another attribute is back
  to a scan.
- That the conceded claim was wrong about the medic. Its reading of
  [CASE-085](../cases.d/CASE-085.md) as a decision to stop, not an inference, is kept by the
  restatement.
