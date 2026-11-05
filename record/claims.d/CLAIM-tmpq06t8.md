---
status: Proposed
title: 'Under peak-capacity costs on reversible moves, the transition threshold between configurations is an ultrametric, so identifying configurations reachable within a budget is an equivalence relation at every budget and the identifications nest into one tree as the budget grows; under additive costs the threshold is only a metric, budgeted identification need not be transitive, and no such tree exists'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: a reversible move graph with peak-cost
  composition in which d(x, z) > max(d(x, y), d(y, z)) for some x, y, z, or
  a budget at which "reachable within b" fails to be transitive; or an
  additive-cost example shown to be impossible. Not defeated by one-way
  moves, which the claim excludes (they break symmetry, CLAIM-tmpy685m), nor
  by several resources at once, where a budget is a vector and the claim is
  stated for one.
tags:
- mathematics
- individuation
- operations-research
date: '2026-11-05'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-tmpbi4ca
- CLAIM-tmp7bxc0
complements:
- CLAIM-tmpxcbet
grounds:
- THEORY-tmpqzxwh
summary: >-
  The assistant's own proposition, filed on 2026-11-05 at the owner's
  invitation to contribute. Take configurations joined by reversible moves,
  each move with a peak requirement, and let d(x, y) be the least, over
  paths, of the largest requirement on the path ([CLAIM-tmpbi4ca](CLAIM-tmpbi4ca.md)'s threshold,
  identities free). Concatenating a path from x to y with one from y to z
  has peak max(d(x, y), d(y, z)), so d(x, z) ≤ max(d(x, y), d(y, z)): d is
  an ultrametric. Hence at each budget b, "x and y can be turned into one
  another within b" is an equivalence relation, its classes are the
  components of the budget-b move graph, and as b grows the classes only
  merge, forming one dendrogram, the merge tree of zero-dimensional
  sublevel persistence (Mirth et al.). Under additive costs d is a
  metric and budgeted identification is intransitive in general. So which
  resource semantics governs a system decides whether "the same thing,
  within budget" sorts its configurations into a hierarchy of kinds at all.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CASE-tmpe48yq CLAIM-tmp7bxc0 CLAIM-tmpbi4ca CLAIM-tmpuk8gq CLAIM-tmpxcbet CLAIM-tmpy685m TERM-tmp26wo4 — Proposed or Skimmed; entries filed in this pull request, cited as open -->
<!-- inactive-ok-file: CASE-tmp0d5si — Proposed or new; entries of 2026-11-05 from A's fourth paste and the assistant, cited as open -->

# CLAIM-tmpq06t8: Under peak-capacity costs on reversible moves, the transition threshold between configurations is an ultrametric, so identifying configurations reachable within a budget is an equivalence relation at every budget and the identifications nest into one tree as the budget grows; under additive costs the threshold is only a metric, budgeted identification need not be transitive, and no such tree exists

## The claim

Let configurations be the vertices of a graph whose edges are reversible
moves, each with a nonnegative peak requirement w, and let d(x, y) be the
least, over paths from x to y, of the largest w on the path, with
d(x, x) = 0. This is the transition threshold of [CLAIM-tmpbi4ca](CLAIM-tmpbi4ca.md) with
identities free, and the hom of the max-enriched category of
[CLAIM-tmpxcbet](CLAIM-tmpxcbet.md).

1. **Ultrametric.** A path from x to y followed by one from y to z is a
   path from x to z whose peak is the larger of the two peaks. So
   d(x, z) ≤ max(d(x, y), d(y, z)). With reversible moves d is symmetric.
2. **Equivalence at every budget.** For each b, the relation x ≈_b y iff
   d(x, y) ≤ b is reflexive, symmetric and, by 1, transitive. Its classes
   are the connected components of the graph of moves costing at most b.
3. **Nesting.** If b ≤ b′ then ≈_b refines ≈_b′. The classes form one tree
   as b runs from 0 up: the merge tree, or single-linkage dendrogram, which
   is what zero-dimensional sublevel-set persistence records (Mirth et al.,
   [NOTE-tmpwvb9j](../notes.d/NOTE-tmpwvb9j.md)).
4. **Additive costs differ.** If costs add along a path, d is a metric
   ([CLAIM-tmp7bxc0](CLAIM-tmp7bxc0.md)'s sum base), and x ≈_b y need not be transitive: costs
   0.6 and 0.6 put x, y and y, z within 1 while x, z are 1.2 apart. No
   single tree of classes exists.

Checked numerically with python3 -I: on 3,000 random symmetric move graphs
of eight configurations, no violation of the ultrametric inequality under
max; under addition, budgeted identification at b = 1 was intransitive in
2,108 of them.

## What it adds

- **Kinds as well as individuals.** Under peak costs, a budget sorts
  configurations into classes of "what this system can become within b",
  and the classes at a larger budget are unions of those at a smaller. A
  hierarchy of kinds falls out of the resource semantics, with no
  classification imposed from outside. Under additive costs it does not:
  "within budget of each other" is a similarity, not a sameness. That
  parallels the pasted synthesis on resource-bounded realizability, which
  notes that its observational similarity at a tolerance "need not be
  transitive".
- **The resource semantics is an individuation choice.** [TERM-tmp26wo4](../terms.d/TERM-tmp26wo4.md)'s
  distinction between instantaneous capacity and cumulative expenditure,
  which looked like bookkeeping, decides whether a system's configurations
  fall into nested kinds. A system limited by peak capacity (staff on duty,
  clearance, a footprint) has a tree of kinds; one limited by spending does
  not.
- **The degree-4 vertex.** In [CASE-tmpe48yq](../cases.d/CASE-tmpe48yq.md)'s vertex, with identities free,
  the two folded states fall into one class at b ≥ 1 + √3/2 and are apart
  below it, which is [CLAIM-tmpxcbet](CLAIM-tmpxcbet.md)'s sublevel groupoid stated as a tree.

## What it does not say

- With one-way moves d is not symmetric ([CLAIM-tmpy685m](CLAIM-tmpy685m.md)), and ≈_b must be
  replaced by mutual reachability within b, which is still transitive but
  coarser than either direction alone.
- With several resources a budget is a vector and the sets of sufficient
  budgets are up-sets ([CLAIM-tmpuk8gq](CLAIM-tmpuk8gq.md)); the classes then form a
  multiparameter structure, not a tree.
- It says nothing about which semantics a given organization obeys; that is
  empirical.

## Note of 2026-11-05: A's fourth paste, and the assistant's contributions

[CASE-tmp0d5si](../cases.d/CASE-tmp0d5si.md), A's U/L/R toy, is an instance with one-way moves: under peak costs mutual reachability within a budget stays transitive, all three states joining at 3; under additive costs it is intransitive at budgets 3 to 5 (U within reach of L and of R both ways, L and R 6 apart). No status changes.
