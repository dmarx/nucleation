---
number: 581
status: Active
formerly:
- CLAIM-tmpq06t8
title: 'Under peak-capacity costs on reversible moves, the transition threshold between configurations is an extended pseudo-ultrametric, so identifying configurations reachable within a budget is an equivalence relation at every budget and the identifications nest into one tree as the budget grows; under additive costs the threshold is only an extended pseudometric, budgeted identification need not be transitive, and no such tree exists'
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the twenty-fifth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings). Step 2 now
    defines identification within b by a path whose peak is at most b,
    which equals d ≤ b where the least peak is attained; before, its
    statement that the classes are components failed on infinite move
    graphs. A bullet says that the transitive closure under addition still
    gives a single-linkage tree, of classes that are not within-b
    identifications. THEORY-1420 moves from grounds to corroborated_by
    (ADR-058): step 3 cites Mirth et al. as what the merge tree is in
    persistence, and the argument does not use it. CLAIM-571 and CLAIM-563
    are promoted in the same review. The argument was re-derived step by
    step. No objection is on file, and nothing meets the defeat condition.
- version: 3
  date: '2026-11-06'
  note: >-
    Dated note added at the twenty-seventh status review (ADR-057), at the
    status review's ruling (the owner delegated these rulings), on the full
    reading of Lawvere (NOTE-1585); THEORY-1376, Active at the same review,
    is added to corroborated_by (ADR-058). No status change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: a reversible move graph with peak-cost
  composition in which d(x, z) > max(d(x, y), d(y, z)) for some x, y, z, or
  a budget at which "reachable within b" fails to be transitive; or an
  additive-cost example shown to be impossible. Not defeated by one-way
  moves, which the claim excludes (they break symmetry, CLAIM-591), nor
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
- CLAIM-571
- CLAIM-563
complements:
- CLAIM-590
- CLAIM-594
summary: >-
  The assistant's own proposition, filed on 2026-11-05 at the owner's
  invitation to contribute. Take configurations joined by reversible moves,
  each move with a peak requirement, and let d(x, y) be the least, over
  paths, of the largest requirement on the path ([CLAIM-571](CLAIM-571.md)'s threshold,
  identities free). Concatenating a path from x to y with one from y to z
  has peak max(d(x, y), d(y, z)), so d(x, z) ≤ max(d(x, y), d(y, z)): d is
  an extended pseudo-ultrametric (distinct states joined at no cost are at
  distance 0, unjoined ones at ∞; it is an ultrametric only when every pair of
  distinct states is separated by a positive cost). Hence at each budget b, "x and y can be turned into one
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
<!-- inactive-ok-file: CASE-tmpbbfq8 CLAIM-tmp2u6bs — Proposed; filed on 2026-11-12 from "Identify Synthesis Opportunities", cited in its note -->

# CLAIM-581: Under peak-capacity costs on reversible moves, the transition threshold between configurations is an extended pseudo-ultrametric, so identifying configurations reachable within a budget is an equivalence relation at every budget and the identifications nest into one tree as the budget grows; under additive costs the threshold is only an extended pseudometric, budgeted identification need not be transitive, and no such tree exists

## The claim

Let configurations be the vertices of a graph whose edges are reversible
moves, each with a nonnegative peak requirement w, and let d(x, y) be the
least, over paths from x to y, of the largest w on the path, with
d(x, x) = 0. This is the transition threshold of [CLAIM-571](CLAIM-571.md) with
identities free, and the hom of the max-enriched category of
[CLAIM-590](CLAIM-590.md).

1. **Pseudo-ultrametric.** A path from x to y followed by one from y to z
   is a path from x to z whose peak is the larger of the two peaks. So
   d(x, z) ≤ max(d(x, y), d(y, z)), the strong triangle inequality. With
   reversible moves d is symmetric. Distinct states joined by moves of zero
   cost have d = 0, and states in different components have d = ∞, so d is
   an extended pseudo-ultrametric; it is an ultrametric only when distinct
   states are always separated by a positive cost. Nothing below needs more
   than the strong triangle inequality.
2. **Equivalence at every budget.** For each b, let x ≈_b y iff some
   path joins x and y whose largest move cost is at most b; on a finite
   move graph, where the least peak is attained, this is d(x, y) ≤ b. It
   is reflexive, symmetric and, since two such paths concatenate into one
   whose peak is the larger of theirs (as in 1), transitive. Its classes
   are the connected components of the graph of moves costing at most b.
3. **Nesting.** If b ≤ b′ then ≈_b refines ≈_b′. The classes form one tree
   as b runs from 0 up: the merge tree, or single-linkage dendrogram, which
   is what zero-dimensional sublevel-set persistence records (Mirth et al.,
   [NOTE-1616](../notes.d/NOTE-1616.md)).
4. **Additive costs differ.** If costs add along a path, d is an extended
   pseudometric, for the same reasons,
   ([CLAIM-563](CLAIM-563.md)'s sum base), and x ≈_b y need not be transitive: costs
   0.6 and 0.6 put x, y and y, z within 1 while x, z are 1.2 apart. No
   single tree of classes exists.

Checked numerically with python3 -I: on 3,000 random symmetric move graphs
of eight configurations, no violation of the ultrametric inequality under
max; under addition, budgeted identification at b = 1 was intransitive in
2,108 of them.

## Identity is free; holding is not

The identity here costs nothing: d(x, x) = 0 says only that staying put
needs no move. It says nothing about what it costs to occupy or maintain x,
which is [CLAIM-571](CLAIM-571.md)'s holding requirement r(x) and [TERM-106](../terms.d/TERM-106.md)'s
endpoint cost. A state can be identical to itself in this category and
unaffordable to sustain; the two are kept apart, and the merge tree above
is of reachability among states, not of their upkeep.

## Correction of 2026-11-05

The claim first called d an ultrametric and the additive threshold a
metric. A, reading this pull request, pointed out that distinct states
joined at zero cost are at distance 0, so the peak threshold is a
pseudo-ultrametric (and extended, being ∞ between components) and the
additive one an extended pseudometric, and that a free identity is not a
free occupation of a state. Both are corrected above; the result, nested
equivalence classes under peak costs, needs only the strong triangle
inequality and stands.

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
- **The resource semantics is an individuation choice.** [TERM-105](../terms.d/TERM-105.md)'s
  distinction between instantaneous capacity and cumulative expenditure,
  which looked like bookkeeping, decides whether a system's configurations
  fall into nested kinds. A system limited by peak capacity (staff on duty,
  clearance, a footprint) has a tree of kinds; one limited by spending does
  not.
- **The degree-4 vertex.** In [CASE-206](../cases.d/CASE-206.md)'s vertex, with identities free,
  the two folded states fall into one class at b ≥ 1 + √3/2 and are apart
  below it, which is [CLAIM-590](CLAIM-590.md)'s sublevel groupoid stated as a tree.

## What it does not say

- With one-way moves d is not symmetric ([CLAIM-591](CLAIM-591.md)), and ≈_b must be
  replaced by mutual reachability within b, which is still transitive but
  coarser than either direction alone.
- With several resources a budget is a vector and the sets of sufficient
  budgets are up-sets ([CLAIM-585](CLAIM-585.md)); the classes then form a
  multiparameter structure, not a tree.
- It says nothing about which semantics a given organization obeys; that is
  empirical.
- That additive costs give no hierarchy at all. The transitive closure of
  budgeted identification under addition does nest into a single-linkage
  tree, but its classes join states more than b apart, so they are not
  classes of what can be turned into one another within b.

## Note of 2026-11-05: A's fourth paste, and the assistant's contributions

[CASE-199](../cases.d/CASE-199.md), A's U/L/R toy, is an instance with one-way moves: under peak costs mutual reachability within a budget stays transitive, all three states joining at 3; under additive costs it is intransitive at budgets 3 to 5 (U within reach of L and of R both ways, L and R 6 apart). No status changes.

## Note of 2026-11-05: the DNA origami readings

Read on the owner's request to connect the record's realizability inquiry to DNA origami; the works were chosen by the assistant.

**Sobczak, "Investigations of the DNA origami folding process".** Sobczak's dissertation (2018), [LIT-2138](../literature.d/LIT-2138.md), read in part in [NOTE-1644](../notes.d/NOTE-1644.md), qualifies the
claim's applicability: folding and unfolding differ by 5–10 °C and by orders of magnitude in time,
so origami folding does not satisfy the reversible-moves premise, and the merge-tree structure need
not hold for it.

**Wagenbauer, Wachauf and Dietz, "Quantifying quality in DNA self-assembly".** Wagenbauer, Wachauf and Dietz (2014), [LIT-2128](../literature.d/LIT-2128.md), read in [NOTE-1637](../notes.d/NOTE-1637.md), qualify the choice of
cost: hours at a fixed 52 °C "did not reach the slightly lower level" of defects of a 16 h ramp,
while a 1.5 h three-step schedule gave quality "comparable to that obtained from 16-h long
annealing". The resource that decides completeness is neither total time nor a single peak
temperature but the path through temperature.

No status changes.

## Note of 2026-11-05: the further DNA origami readings

The works cited in A's two syntheses on DNA origami, pasted by the owner on 2026-11-05, read in this pull request.

**Ni, Zhou, Zhu, Bershadsky, Ai, Wang, Sha, Seeman and Chaikin, "Cooperativity, entropy, and effective concentration in DNA origami self-replication".** Ni et al. (2026), [LIT-2124](../literature.d/LIT-2124.md), qualify the claim. In their replication cycle, temperature acts as a peak cost: the separation step needs about 50 °C. Each cycle also spends about 21 h of cooling, an additive cost. Which cost governs whether a cycle succeeds is not compared, so the paper does not show reachability set by the peak alone.

No status changes.

## Note of 2026-11-05: the readings on correction, repair, replication and nucleation barriers

Read at the owner's invitation to add readings to the DNA origami filing; the works were chosen by the assistant.

**Zhou, Sha, Ni, Seeman and Chaikin, "Mutations in artificial self-replicating tiles".**

- Each replication cycle spends both a peak and time.
- Zhou's cycle takes about 2 h. He et al.'s 24 cycles took about 730 h (from Zhang et al. 2025; about 30 h a cycle, my arithmetic) at similar peaks.
- So the additive cost varies widely while the peak is about fixed, and a threshold on peak alone does not price the transition.
- He's protocol was not read.

No status changes.

## Note of 2026-11-06: Claude, read

Lawvere: "An R_cart-category is just an ultrametric space" (1973, p. 152; [NOTE-1585](../notes.d/NOTE-1585.md)), where R_cart is [0, ∞] with max as tensor and the metric spaces are his generalized ones, without symmetry, separation or finiteness. That is independent support for reading the peak-cost threshold as an extended pseudo-ultrametric. [THEORY-1376](../theory.d/THEORY-1376.md) corroborates. No status change.

## Note of 2026-11-12: a construction from "Identify Synthesis Opportunities"

In the exchange of 2026-11-08 (https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44, A11 and A12), A built a chain and a complete graph on the same configurations, filed as CASE-tmpbbfq8. Every pair has threshold 1 in both, so this claim's ultrametric and its classes are the same in both; the least cumulative cost from one end to the other is n against 1. It illustrates the step above that under additive costs "within budget of each other" is not an equivalence: in the chain at budget 1, 0 is within budget of 1 and 1 of 2, and 0 not of 2. A's claim that the threshold structure does not fix cumulative costs is filed as CLAIM-tmp2u6bs, Proposed; it states formally what the note of 2026-11-05 on replicating tiles observed. No status change.
