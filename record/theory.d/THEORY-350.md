---
number: 350
status: Active
formerly:
- THEORY-tmpntty3
title: "Under a budget on maintenance time, a stored view's upkeep depends on which other views are stored, so upkeep is not additive and adding a view can lower it, and greedily adding the single view of best saving per unit of upkeep can be arbitrarily bad; on OR view graphs a greedy over inverted tree sets gets 1 − 1/e of the saving of an optimum given as much upkeep, using up to twice the budget, if no tree-piece of the optimum alone exceeds the budget"
version: 1
tags:
- databases
- operations-research
date: '2026-10-15'
source:
- LIT-1092
- LIT-1080
- LIT-1091
extends:
- THEORY-356
summary: >-
  Gupta and Mumick (1999), [LIT-1092](../literature.d/LIT-1092.md), read in [NOTE-890](../notes.d/NOTE-890.md), with the proofs
  of the journal version (2005), [LIT-1080](../literature.d/LIT-1080.md), read in [NOTE-901](../notes.d/NOTE-901.md), and the
  superadditivity first noted by Gupta (1997), [LIT-1091](../literature.d/LIT-1091.md), read in [NOTE-889](../notes.d/NOTE-889.md).
  Minimizing query cost subject to a cap on total maintenance time, one stored
  view can make another cheaper to keep current, so saving per unit of upkeep is
  not monotone and single-view greedy fails without bound (Example 2). Grouping
  views into inverted tree sets restores a 1 − 1/e guarantee, proved in 2005
  (Theorem 8), for OR view graphs only, bicriteria, under an assumption on the
  optimum, with greedy stages exponential in general. The proof does not treat
  the negative effective costs the paper allows. Upkeep is a budget, not a cost
  traded against savings, and staleness and build cost are not modelled.
bears_on:
- QUESTION-114
---

# THEORY-350: Under a budget on maintenance time, a stored view's upkeep depends on which other views are stored, so upkeep is not additive and adding a view can lower it, and greedily adding the single view of best saving per unit of upkeep can be arbitrarily bad; on OR view graphs a greedy over inverted tree sets gets 1 − 1/e of the saving of an optimum given as much upkeep, using up to twice the budget, if no tree-piece of the optimum alone exceeds the budget

## Source

Gupta and Mumick (1999), [LIT-1092](../literature.d/LIT-1092.md), read in full in [NOTE-890](../notes.d/NOTE-890.md) from the
ICDT camera-ready (§§2, 4–7). Gupta and Mumick (2005), [LIT-1080](../literature.d/LIT-1080.md), read in
full in [NOTE-901](../notes.d/NOTE-901.md) (Section 6: Examples 1–2, Lemma 5, Theorems 8–10).
Gupta (1997), [LIT-1091](../literature.d/LIT-1091.md), read in [NOTE-889](../notes.d/NOTE-889.md), for the first statement of
the interaction and for the open problem the 1999 paper takes up.

## What was actually shown

**The model.** Each view v has a query frequency f_v and an update frequency
g_v. Total upkeep is U(M) = Σ over stored views of g_v × UC(v, M), where the
per-update cost UC depends on the stored set M. The problem minimizes
frequency-weighted query cost subject to U(M) ≤ S. Every stored view is
refreshed in each batch: "Usually, changes to the source data are queued and
propagated periodically to the warehouse views in a large batch update
transaction."

**Non-additivity.** "the maintenance cost of a view v depends on the set of
other materialized views". Gupta had already seen the effect in the objective:
"consider a view C1 which helps in maintaining another view C2. Hence, the
benefit of C1 ∪ C2 might be more than the sum of their benefits individually."
So the effective upkeep of adding a set, U(M ∪ C) − U(M), "may be negative".
In Example 2 the saving per unit of upkeep of {V2}, {V3} and {V2, V3} is 1, 1
and 7/4. With budget 4, single-view greedy takes {V1} (saving 5) where
{V2, V3, V4, V5} saves 11 at the same upkeep, and Figure 4 (Figure 5 in 2005)
makes the gap arbitrary: single-view greedy "could deliver an arbitrarily bad
solution". This is a counterexample, and settles the failure outright.

**The repair, on OR view graphs.** In an OR graph each view is maintained from
at most one other, so any solution splits into inverted tree sets whose
effective upkeeps sum to no more than the whole (Lemma 5, with the step now
justified: "as any view uses at most one view to help maintain itself"). A
greedy that adds whole inverted tree sets by best saving per unit of effective
upkeep returns M with U(M) ≤ 2S and saving at least 1 − 1/e of an optimal
solution whose upkeep is at most U(M), assuming no inverted tree set of the
optimum has upkeep above S (Theorem 8 of [LIT-1080](../literature.d/LIT-1080.md), proved; stated without
proof as Theorem 1 of [LIT-1092](../literature.d/LIT-1092.md)). On random OR graphs of 10 to 25 nodes the
greedy matched the exact A* optimum in 96% of instances.

## What this does not say

- **That the guarantee covers general view graphs.** It is for OR view graphs
  only. General AND-OR graphs get an exact A* search (Theorem 10, proved) with
  exponential worst-case time and space, and no approximation guarantee.
- **That the greedy is efficient.** A stage enumerates every inverted tree set,
  exponentially many in general. In a data-cube lattice the finest view has
  every other view as an ancestor, so a stage there is exponential too; the
  papers do not say so.
- **That the bound is unconditional.** It is bicriteria (up to 2S, compared with
  an optimum given as much) and assumes something about the unknown optimum.
  Without that assumption only half the optimum's saving per unit of upkeep is
  claimed (Theorem 9), which neither paper proves. The 2005 proof divides by
  effective upkeep, which the paper allows to be negative, and does not treat
  that case.
- **That upkeep is weighed against savings.** Upkeep is a constraint here. The
  model says which views to keep given so much maintenance time, not how much
  time is worth spending. Space and maintenance budgets are never combined.
- **That staleness or building is priced.** Every chosen view is refreshed in
  every batch; there is no stale answer, deferred refresh or first build.

## Connections

- [THEORY-356](THEORY-356.md) is the space- and count-budget case, where single-view greedy
  keeps its guarantee because saving is subadditive. This account is where that
  property fails.
- For [QUESTION-114](../questions.d/QUESTION-114.md) the finding constrains any joint cost model of
  precomputation: upkeep has to be priced for the stored set, not item by item.
  The record holds [LIT-1095](../literature.d/LIT-1095.md) ([THEORY-332](THEORY-332.md)) as nearer to a joint model.
