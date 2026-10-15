---
status: Active
title: "When stored views are never updated, greedily storing the view of largest marginal saving in query cost gets at least 1 − 1/e of the optimal saving on a data-cube lattice or any OR or AND view graph, against the optimum for the same number of views or for the space the greedy ends up using, which may exceed the budget by one view"
version: 1
tags:
- databases
- operations-research
date: '2026-10-15'
source:
- LIT-tmptn63k
- LIT-tmpn0tsb
- LIT-tmp28bff
answers:
- QUESTION-tmplg07t
summary: >-
  Harinarayan, Rajaraman and Ullman (1996), [LIT-tmptn63k](../literature.d/LIT-tmptn63k.md), read in [NOTE-tmpb6yin](../notes.d/NOTE-tmpb6yin.md);
  Gupta (1997), [LIT-tmpn0tsb](../literature.d/LIT-tmpn0tsb.md), read in [NOTE-tmp4p0w6](../notes.d/NOTE-tmp4p0w6.md); Gupta and Mumick (2005),
  [LIT-tmp28bff](../literature.d/LIT-tmp28bff.md), read in [NOTE-tmpuaboe](../notes.d/NOTE-tmpuaboe.md). A stored answer is worth the saving on
  every query derivable from it, less what answers already stored save, and
  greedy on that marginal saving gets 1 − ((k−1)/k)^k ≥ 1 − 1/e of the best
  saving for k views; under a space budget the same holds against the optimum
  in the space the greedy actually uses (up to one view over), or 0.63 − f when
  no view takes more than a fraction f of the budget. The bound is on saving
  against storing the base view alone, not on query cost, and it holds only with
  no updates: once upkeep enters the objective it is proved only for AND graphs
  in which every view is queried more often than it is updated.
extended_by:
- THEORY-tmpntty3
---

# THEORY-tmpxfpa7: When stored views are never updated, greedily storing the view of largest marginal saving in query cost gets at least 1 − 1/e of the optimal saving on a data-cube lattice or any OR or AND view graph, against the optimum for the same number of views or for the space the greedy ends up using, which may exceed the budget by one view

## Source

Harinarayan, Rajaraman and Ullman (1996), [LIT-tmptn63k](../literature.d/LIT-tmptn63k.md), read in full in
[NOTE-tmpb6yin](../notes.d/NOTE-tmpb6yin.md) from the authors' January 1996 version (§§4.1–4.6). Gupta (1997),
[LIT-tmpn0tsb](../literature.d/LIT-tmpn0tsb.md), read in full in [NOTE-tmp4p0w6](../notes.d/NOTE-tmp4p0w6.md) (Theorems 3.1, 3.2, 4.1, 5.1).
Gupta and Mumick (2005), [LIT-tmp28bff](../literature.d/LIT-tmp28bff.md), read in full in [NOTE-tmpuaboe](../notes.d/NOTE-tmpuaboe.md), the
journal version of both ICDT papers (Theorems 1, 3, 4 and Section 4.3).

## What was actually shown

**The quantity.** Queries are views, a view can be computed from any stored
ancestor, and a query costs the rows of the cheapest stored view it can be read
from. The benefit of adding a view v to the stored set S is the sum, over every
view w derivable from v, of how much cheaper w becomes. It is marginal on S: in
Example 4.1 of [LIT-tmptn63k](../literature.d/LIT-tmptn63k.md) a view that "wasn't even close to the best choice at
the first round" is the greedy choice at the second.

**The count budget.** Greedy over k views, starting from the base (top) view,
gets total benefit at least 1 − ((k−1)/k)^k of the best k views: 3/4 at k = 2,
falling to 1 − 1/e ≈ 0.63. In the paper's words, "for no lattice whatsoever does
the greedy algorithm give a benefit less than 63% of the optimal benefit." The
bound holds unchanged when views are weighted by fixed query probabilities. The
proof in [LIT-tmptn63k](../literature.d/LIT-tmptn63k.md) is a sketch, and tightness is shown by example for k = 2
and only outlined for general k.

**The space budget.** Greedy by benefit per unit space can be crowded out:
"Choosing the small view excludes the large view, because there is not enough
space available for the large view after we choose the small." [LIT-tmptn63k](../literature.d/LIT-tmptn63k.md)
states, without a separate proof, a ratio of at least 0.63 − f when no view uses
more than a fraction f of the budget. Gupta proves the bicriteria form: the
greedy uses at most S + r space, r the largest view, and its benefit is at
least 1 − 1/e of the optimum achievable in that space. That is proved for AND
view graphs in [LIT-tmpn0tsb](../literature.d/LIT-tmpn0tsb.md) (Theorem 3.1) and for OR view graphs, which include
the cube lattice, in [LIT-tmp28bff](../literature.d/LIT-tmp28bff.md) (Theorem 1). Held to a hard budget, the better
of the greedy less its last view and the best single view gets (1 − 1/e)/2,
which [LIT-tmp28bff](../literature.d/LIT-tmp28bff.md) says "can be easily shown".

**What could have come out otherwise.** The guarantee rests on benefit being
subadditive over single views (the papers' "monotonicity property"). It holds
in these graphs without updates; Section 4.3 of both Gupta papers shows how
upkeep breaks it ([THEORY-tmpntty3](THEORY-tmpntty3.md)).

## What this does not say

- **That the greedy is near the cheapest design.** The bound is on the saving
  against storing the base view alone, not on total query cost, and none of the
  papers translates it into one.
- **That it holds with updates.** Every result above assumes static data. For
  data cubes Gupta sets updates aside outright: "As OLAP databases have very few
  or no updates, we assume that there are no update costs throughout this
  section". The one result with upkeep in the objective (Theorem 3.2 of
  [LIT-tmpn0tsb](../literature.d/LIT-tmpn0tsb.md), Theorem 4 of [LIT-tmp28bff](../literature.d/LIT-tmp28bff.md)) covers AND view graphs in which every
  view's update frequency is below its query frequency, and its proof needs
  bounds on maintenance cost that the model does not state. The journal version
  adds of its key lemma: "The claim doesn't hold for OR view graphs."
- **That building a view is priced.** Space stands in for the work of computing
  a view. No one-time build cost is in any objective here.
- **That selection is proved hard.** NP-completeness is asserted in
  [LIT-tmptn63k](../literature.d/LIT-tmptn63k.md) ("a straightforward reduction from Set-Cover") and NP-hardness in
  [LIT-tmpn0tsb](../literature.d/LIT-tmpn0tsb.md); neither gives the reduction. The 63% inapproximability for OR
  graphs is attributed to a personal communication, not proved.
- **That general AND-OR graphs are covered.** There the guarantee needs an
  AO-greedy that can take exponential time, with proof omitted.
- **That workloads may be uncertain.** Query frequencies are fixed and known.
  [LIT-tmptn63k](../literature.d/LIT-tmptn63k.md) names "dynamic materialization" as untested future work.

## Connections

- [THEORY-tmpntty3](THEORY-tmpntty3.md) is the same selection with upkeep as the budget, where the
  marginal-saving greedy fails. [THEORY-tmpktrsb](THEORY-tmpktrsb.md) is the access-path counterpart:
  choosing indexes, not stored answers.
- For [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md) this is the precomputed-answer term the access-path
  readings lacked: reuse as weighted coverage of derivable queries, with
  diminishing returns. It prices storage, reuse and retrieval, and leaves out
  build cost, upkeep and staleness.
- [CLAIM-303](../claims.d/CLAIM-303.md)'s break-even ("worth its cost only when expected reuse covers it")
  takes a sharper form here: an item's worth depends on what else is stored, so
  a rule that judges each item alone can misjudge it either way.
