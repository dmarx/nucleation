---
status: Active
title: "On an n × n lattice whose nodes also get long-range links drawn with probability proportional to lattice distance to the power −r, a searcher that knows only the target's position and the links of nodes already reached delivers in expected time polylogarithmic in n only at r = 2: greedy routing then takes O((log n)²) steps, while for 0 ≤ r < 2 every such searcher needs Ω(n^((2−r)/3)) steps and for r > 2 Ω(n^((r−2)/(r−1))), even at r = 0 where short paths exist"
version: 1
tags:
- network-science
- information-retrieval
- mathematics
date: '2026-10-15'
source:
- LIT-tmp7dffg
summary: >-
  Kleinberg (2000), [LIT-tmp7dffg](../literature.d/LIT-tmp7dffg.md), read in [NOTE-tmpyzlig](../notes.d/NOTE-tmpyzlig.md). Proved for the
  two-dimensional lattice: with nodes, local links and the number of
  long-range links fixed, changing only the exponent r of the long-range
  link distribution moves the expected delivery time of the best
  decentralized searcher from O((log n)²) at r = 2 to a power of n at
  every other r, including r = 0, where paths of polylogarithmic length
  exist. The upper bound is proved only for one local and one long-range
  link per node; the k-dimensional statement (r = k) is asserted, not
  proved; the family is inverse power laws of a distance every node can
  compute, so it does not show that no other link structure is navigable.
supports:
- CLAIM-310
---

# THEORY-tmpdllj7: On an n × n lattice whose nodes also get long-range links drawn with probability proportional to lattice distance to the power −r, a searcher that knows only the target's position and the links of nodes already reached delivers in expected time polylogarithmic in n only at r = 2: greedy routing then takes O((log n)²) steps, while for 0 ≤ r < 2 every such searcher needs Ω(n^((2−r)/3)) steps and for r > 2 Ω(n^((r−2)/(r−1))), even at r = 0 where short paths exist

## Source

Kleinberg (2000), [LIT-tmp7dffg](../literature.d/LIT-tmp7dffg.md), STOC 2000, read in full in [NOTE-tmpyzlig](../notes.d/NOTE-tmpyzlig.md) from
the author's 14-page copy (also Cornell CS TR 99-1776): the model,
Theorems 1–3 and their proofs (Sections 2 and 3), and the conclusion.

## What was actually shown

**The model.** Nodes are the points of an n × n lattice with lattice
distance d. Each node links to every node within distance p and to q
further nodes drawn independently with probability proportional to
d(u, v)^(−r). A decentralized algorithm passes the message from holder to
contact knowing the lattice, the target's position, and the long-range
links of nodes the message has touched; "Crucially, u does not have
knowledge of the long-range contacts of nodes that have not touched the
message." Cost is the expected number of steps over the random network
and a uniformly random source and target.

**Theorem 2 (r = 2, p = q = 1).** Greedy routing, passing to the contact
nearest the target, delivers in at most α₂(log n)² expected steps. From
distance at most 2^(j+1), the chance per step of entering the ball of
radius 2^j around the target is at least 1/(128 ln(6n)), and there are at
most 1 + log n such halvings.

**Theorems 1 and 3 (lower bounds, any p, q).** For 0 ≤ r < 2 every
decentralized algorithm needs at least α_r n^((2−r)/3) expected steps
(n^(2/3) at r = 0, Theorem 1); for r > 2 at least α_r n^((r−2)/(r−1)).
The bounds hold even for algorithms that may jump to any contact of any
node already reached. For r < 2 links rarely land near the target; for
r > 2 no link long enough to cross the lattice quickly is likely to be met.

**What could have come out otherwise.** Some exponent other than 2 could
have admitted polylogarithmic delivery, or the r = 0 network, whose
shortest paths are polylogarithmic by random-graph results, could have
been searchable. The proofs rule both out within the family.

## What this does not say

- **That only one arrangement of links is navigable.** The result is
  about one family, inverse powers of lattice distance with constant p
  and q. Other constructions, hierarchical ones for instance, are not
  covered either way.
- **That r equals the dimension in general.** "In the k-dimensional
  case, a decentralized algorithm can construct paths of length polynomial
  in log n if and only if r = k" is stated in the introduction and not
  proved in this paper; the proofs are for two dimensions. The upper bound
  is proved only for p = q = 1.
- **That navigability belongs to the links alone.** Greedy routing works
  because every node can compute its contacts' distance to the target in
  a coordinate system all nodes share. The result is about links arranged
  relative to that metric; a collection with no such distance between its
  parts is outside it.
- **That greedy search fails for r ≠ 2 by a fixed amount, or always.**
  The bounds are on expected time over random source and target pairs,
  with unspecified constants; nothing is said about every pair or about
  finite n.
- **That real social networks have r = 2, or that Milgram's subjects
  routed greedily.** The paper offers a model consistent with the
  experiment, not a test of it. It also says nothing about the cost of
  building or maintaining such a network.

## Connections

- [CLAIM-310](../claims.d/CLAIM-310.md) (arrangements, not descriptions): this is a proved case of
  the "as arrangements" half. With the items, the space and the number of
  links fixed, the arrangement of links alone decides whether a local
  searcher finds a target in polylogarithmic or polynomial time.
- [THEORY-tmpry4qh](THEORY-tmpry4qh.md): slow-preprocessing DiskANN guarantees the same kind of
  progress deterministically, by building a graph in which some edge from
  every point moves a factor α closer to any target. [THEORY-tmpc25xn](THEORY-tmpc25xn.md): graph
  indexes built without that property can need a scan of a tenth of the
  points.
- [THEORY-358](THEORY-358.md): a parallel in form only (search cost flat or logarithmic
  against linear depending on arrangement); the mechanisms are unrelated.
- [NOTE-670](../notes.d/NOTE-670.md) cites the navigability of hyperbolic random graphs, a
  different construction from this lattice family.
