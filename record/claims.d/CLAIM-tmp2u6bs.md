---
status: Proposed
title: 'Peak-capacity thresholds do not fix cumulative transition costs: two systems can have the same threshold between every pair of configurations, and so the same hierarchy of budgeted classes, while the least cumulative cost of a transition differs between them by any factor'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a pair of configurations in CASE-tmpbbfq8
  whose peak threshold differs between the chain and the complete graph,
  or a least cumulative cost from 0 to n other than n in the chain and 1
  in the complete graph. Also defeated as a claim of its own if an entry
  already states that a system's peak thresholds leave its cumulative
  costs undetermined; CLAIM-571 says only that a cumulative path costs its
  integral and not its peak, and CLAIM-581 that additive costs give no
  equivalence, neither that agreement in every peak threshold leaves the
  cumulative costs free. CLAIM-581's note of 2026-11-05 on replicating
  tiles observes that "a threshold on peak alone does not price the
  transition", from two protocols at similar peaks; that is an
  observation in a note, without a construction, and corroborates this.
tags:
- mathematics
- operations-research
date: '2026-11-12'
line:
- realizability
- formal-apparatus
grounds:
- CASE-tmpbbfq8
summary: >-
  A's proposal, from the exchange "Identify Synthesis Opportunities"
  (2026-11-08, A11 and A12), where A put it as "Peak-budget reachability
  does not determine cumulative transition expenditure". [CLAIM-571](CLAIM-571.md) makes
  the threshold for a held capacity the least peak over paths, and
  [CLAIM-581](CLAIM-581.md) shows those thresholds form an ultrametric whose classes nest.
  This claim says that structure carries no information about what a
  transition spends: the chain and the complete graph of [CASE-tmpbbfq8](../cases.d/CASE-tmpbbfq8.md)
  agree in every threshold and differ in least spend by a factor of n.
  Filed with its construction as a case, at the owner's instruction (U5).
  The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpbbfq8 — Proposed; the construction this claim rests on, filed with it -->

# CLAIM-tmp2u6bs: Peak-capacity thresholds do not fix cumulative transition costs: two systems can have the same threshold between every pair of configurations, and so the same hierarchy of budgeted classes, while the least cumulative cost of a transition differs between them by any factor

## The claim

A, at A12: "two systems can have identical peak-budget reachability at
every budget but different minimum cumulative transition costs", and at
A11, the stronger form: "on a family of finite transition systems, the
same peak-budget reachability hierarchy can coexist with cumulative
shortest-path costs that differ by an arbitrarily large factor".

**Proof.** [CASE-tmpbbfq8](../cases.d/CASE-tmpbbfq8.md). On configurations 0 to n, with every
configuration and every move needing one unit of held capacity and every
move spending one unit, the chain and the complete graph join every pair
at peak budget 1 and none below. So [CLAIM-571](CLAIM-571.md)'s threshold B*(x, y) is 1
for every pair in both, and [CLAIM-581](CLAIM-581.md)'s ultrametric, with the classes it
induces at each budget, is the same. The least cumulative cost from 0 to
n is n in the chain, which must take n moves, and 1 in the complete
graph. For any factor k, n > k separates them by more than k.

## Why it matters on the record

A's reason, at A12: "a reachability hierarchy cannot, by itself, tell us
how much work a transition requires." [CLAIM-581](CLAIM-581.md) reads its hierarchy of
kinds as one that "falls out of the resource semantics". This claim
marks what that hierarchy forgets: two systems sorted alike into kinds at
every budget can differ without bound in what moving between kinds
costs. [TERM-105](../terms.d/TERM-105.md) keeps peak capacity and cumulative expenditure apart as
types; this shows that knowing every threshold of the first does not
bound the second.

The record had met the point empirically. [CLAIM-581](CLAIM-581.md)'s note of 2026-11-05
on the replication readings compares Zhou et al.'s cycle of about 2 h
with He et al.'s 24 cycles of about 730 h "at similar peaks", and
concludes that "a threshold on peak alone does not price the
transition". This claim is the formal version: not only do the costs
differ in those systems, the whole threshold structure can agree while
they differ without bound.

## What it does not say

- That cumulative cost is independent of peak cost in every system. A
  move's spend can be tied to its peak by the physics; the claim is that
  the threshold structure alone does not fix it.
- Anything for several resources ([CLAIM-585](CLAIM-585.md)) or for budgets that mix the
  two types.
- That the converse holds. Whether cumulative costs fix the peak
  thresholds is not asked here.
