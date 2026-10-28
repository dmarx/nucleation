---
number: 356
status: Active
formerly:
- THEORY-tmpxfpa7
title: "When stored views are never updated, greedily storing the view of largest marginal saving in query cost gets at least 1 − 1/e of the optimal saving on a data-cube lattice or any OR or AND view graph, against the optimum for the same number of views or for the space the greedy ends up using, which may exceed the budget by one view"
version: 1
tags:
- databases
- operations-research
date: '2026-10-15'
source:
- LIT-1094
- LIT-1091
- LIT-1080
summary: >-
  Harinarayan, Rajaraman and Ullman (1996), [LIT-1094](../literature.d/LIT-1094.md), read in [NOTE-895](../notes.d/NOTE-895.md);
  Gupta (1997), [LIT-1091](../literature.d/LIT-1091.md), read in [NOTE-889](../notes.d/NOTE-889.md); Gupta and Mumick (2005),
  [LIT-1080](../literature.d/LIT-1080.md), read in [NOTE-901](../notes.d/NOTE-901.md). A stored answer is worth the saving on
  every query derivable from it, less what answers already stored save, and
  greedy on that marginal saving gets 1 − ((k−1)/k)^k ≥ 1 − 1/e of the best
  saving for k views; under a space budget the same holds against the optimum
  in the space the greedy actually uses (up to one view over), or 0.63 − f when
  no view takes more than a fraction f of the budget. The bound is on saving
  against storing the base view alone, not on query cost, and it holds only with
  no updates: once upkeep enters the objective it is proved only for AND graphs
  in which every view is queried more often than it is updated.
extended_by:
- THEORY-350
bears_on:
- QUESTION-114
---

# THEORY-356: When stored views are never updated, greedily storing the view of largest marginal saving in query cost gets at least 1 − 1/e of the optimal saving on a data-cube lattice or any OR or AND view graph, against the optimum for the same number of views or for the space the greedy ends up using, which may exceed the budget by one view

## Source

Harinarayan, Rajaraman and Ullman (1996), [LIT-1094](../literature.d/LIT-1094.md), read in full in
[NOTE-895](../notes.d/NOTE-895.md) from the authors' January 1996 version (§§4.1–4.6). Gupta (1997),
[LIT-1091](../literature.d/LIT-1091.md), read in full in [NOTE-889](../notes.d/NOTE-889.md) (Theorems 3.1, 3.2, 4.1, 5.1).
Gupta and Mumick (2005), [LIT-1080](../literature.d/LIT-1080.md), read in full in [NOTE-901](../notes.d/NOTE-901.md), the
journal version of both ICDT papers (Theorems 1, 3, 4 and Section 4.3).

## What was actually shown

**The quantity.** Queries are views, a view can be computed from any stored
ancestor, and a query costs the rows of the cheapest stored view it can be read
from. The benefit of adding a view v to the stored set S is the sum, over every
view w derivable from v, of how much cheaper w becomes. It is marginal on S: in
Example 4.1 of [LIT-1094](../literature.d/LIT-1094.md) a view that "wasn't even close to the best choice at
the first round" is the greedy choice at the second.

**The count budget.** Greedy over k views, starting from the base (top) view,
gets total benefit at least 1 − ((k−1)/k)^k of the best k views: 3/4 at k = 2,
falling to 1 − 1/e ≈ 0.63. In the paper's words, "for no lattice whatsoever does
the greedy algorithm give a benefit less than 63% of the optimal benefit." The
bound holds unchanged when views are weighted by fixed query probabilities. The
proof in [LIT-1094](../literature.d/LIT-1094.md) is a sketch, and tightness is shown by example for k = 2
and only outlined for general k.

**The space budget.** Greedy by benefit per unit space can be crowded out:
"Choosing the small view excludes the large view, because there is not enough
space available for the large view after we choose the small." [LIT-1094](../literature.d/LIT-1094.md)
states, without a separate proof, a ratio of at least 0.63 − f when no view uses
more than a fraction f of the budget. Gupta proves the bicriteria form: the
greedy uses at most S + r space, r the largest view, and its benefit is at
least 1 − 1/e of the optimum achievable in that space. That is proved for AND
view graphs in [LIT-1091](../literature.d/LIT-1091.md) (Theorem 3.1) and for OR view graphs, which include
the cube lattice, in [LIT-1080](../literature.d/LIT-1080.md) (Theorem 1). Held to a hard budget, the better
of the greedy less its last view and the best single view gets (1 − 1/e)/2,
which [LIT-1080](../literature.d/LIT-1080.md) says "can be easily shown".

**What could have come out otherwise.** The guarantee rests on benefit being
subadditive over single views (the papers' "monotonicity property"). It holds
in these graphs without updates; Section 4.3 of both Gupta papers shows how
upkeep breaks it ([THEORY-350](THEORY-350.md)).

## What this does not say

- **That the greedy is near the cheapest design.** The bound is on the saving
  against storing the base view alone, not on total query cost, and none of the
  papers translates it into one.
- **That it holds with updates.** Every result above assumes static data. For
  data cubes Gupta sets updates aside outright: "As OLAP databases have very few
  or no updates, we assume that there are no update costs throughout this
  section". The one result with upkeep in the objective (Theorem 3.2 of
  [LIT-1091](../literature.d/LIT-1091.md), Theorem 4 of [LIT-1080](../literature.d/LIT-1080.md)) covers AND view graphs in which every
  view's update frequency is below its query frequency, and its proof needs
  bounds on maintenance cost that the model does not state. The journal version
  adds of its key lemma: "The claim doesn't hold for OR view graphs."
- **That building a view is priced.** Space stands in for the work of computing
  a view. No one-time build cost is in any objective here.
- **That selection is proved hard.** NP-completeness is asserted in
  [LIT-1094](../literature.d/LIT-1094.md) ("a straightforward reduction from Set-Cover") and NP-hardness in
  [LIT-1091](../literature.d/LIT-1091.md); neither gives the reduction. The 63% inapproximability for OR
  graphs is attributed to a personal communication, not proved.
- **That general AND-OR graphs are covered.** There the guarantee needs an
  AO-greedy that can take exponential time, with proof omitted.
- **That workloads may be uncertain.** Query frequencies are fixed and known.
  [LIT-1094](../literature.d/LIT-1094.md) names "dynamic materialization" as untested future work.

## Connections

- [THEORY-350](THEORY-350.md) is the same selection with upkeep as the budget, where the
  marginal-saving greedy fails. [THEORY-345](THEORY-345.md) is the access-path counterpart:
  choosing indexes, not stored answers.
- For [QUESTION-114](../questions.d/QUESTION-114.md) this is the precomputed-answer term the access-path
  readings lacked: reuse as weighted coverage of derivable queries, with
  diminishing returns. It prices storage, reuse and retrieval, and leaves out
  build cost, upkeep and staleness.
- [CLAIM-303](../claims.d/CLAIM-303.md)'s break-even ("worth its cost only when expected reuse covers it")
  takes a sharper form here: an item's worth depends on what else is stored, so
  a rule that judges each item alone can misjudge it either way.
