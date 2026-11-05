---
status: Proposed
title: 'With observational indistinguishability refining as the observing budget grows and peak-cost mutual reachability coarsening as the acting budget grows, the budget pairs at which everything indistinguishable is mutually reachable form an up-set and those at which everything mutually reachable is indistinguishable form a down-set, with boundaries given by the largest peak distance within an observational class and the least observing budget that separates two mutually reachable states'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument or the formulas: under nested probe families and
  peak-cost mutual reachability, a pair (o, a) in the first set with a
  larger pair outside it, or a pair in the second set with a smaller pair
  outside it; or a system in which the least acting budget putting O_o
  inside A_a differs from the largest peak distance between two states
  O_o identifies, or in which A_a ⊆ O_o fails while o is below every
  budget separating a pair A_a joins. Not defeated by probe families that
  are not nested, or by additive costs, under which A_a is not an
  equivalence; the claim excludes both.
tags:
- mathematics
- individuation
- epistemology
date: '2026-11-05'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-tmpg7w69
- CLAIM-tmpq06t8
complements:
- CLAIM-tmp42yq0
grounds:
- CASE-tmp0d5si
bears_on:
- QUESTION-tmp3icc7
summary: >-
  A's construction, from A's reading of this pull request on 2026-11-05,
  made exact by the assistant. Let O_o be indistinguishability under the
  probes affordable at observing budget o, finer as o grows ([CLAIM-tmpg7w69](CLAIM-tmpg7w69.md)),
  and A_a mutual reachability within acting budget a under peak costs,
  coarser as a grows ([CLAIM-tmpq06t8](CLAIM-tmpq06t8.md)). The pairs (o, a) with O_o ⊆ A_a,
  where everything an observer cannot tell apart the system can turn into
  one another, form a set closed upward in both budgets; the pairs with
  A_a ⊆ O_o form a set closed downward; on both, O_o = A_a. The boundaries
  are explicit: the least a with O_o ⊆ A_a is the largest peak distance
  between two states O_o identifies, and A_a ⊆ O_o holds exactly when o is
  below the least observing budget that separates some pair A_a joins.
  Checked on 2,000 random systems and exhaustively on A's U/L/R toy. Under
  a shared budget o + a ≤ B, the two boundaries pose an allocation between
  telling apart and becoming. The construction is A's; the boundary
  formulas and checks are the assistant's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpg7w69 CLAIM-tmpq06t8 CLAIM-tmp42yq0 CASE-tmp0d5si CASE-tmpe48yq — Proposed; entries of this pull request, cited as open -->

# CLAIM-tmpatpn9: With observational indistinguishability refining as the observing budget grows and peak-cost mutual reachability coarsening as the acting budget grows, the budget pairs at which everything indistinguishable is mutually reachable form an up-set and those at which everything mutually reachable is indistinguishable form a down-set, with boundaries given by the largest peak distance within an observational class and the least observing budget that separates two mutually reachable states

## The claim

Fix the states of one system. For an observing budget o, let O_o be the
relation "no probe costing at most o tells them apart"; with nested probe
families, o ≤ o′ gives O_o′ ⊆ O_o ([CLAIM-tmpg7w69](CLAIM-tmpg7w69.md)). For an acting budget a,
let A_a be mutual reachability within a under peak costs; with reversible
moves, or with mutual reachability taken both ways, a ≤ a′ gives
A_a ⊆ A_a′ ([CLAIM-tmpq06t8](CLAIM-tmpq06t8.md)). Both are equivalence relations. Define

  S = {(o, a) : O_o ⊆ A_a},  T = {(o, a) : A_a ⊆ O_o}.

1. **S is an up-set.** Raising o shrinks O_o and raising a enlarges A_a, so
   an inclusion that holds still holds.
2. **T is a down-set,** by the same two monotonicities read the other way.
3. **Agreement.** On S ∩ T, O_o = A_a: what the observer cannot tell apart
   is exactly what the system can turn into one another. S ∩ T can be
   empty.
4. **The boundary of S.** For each o, the least a with (o, a) ∈ S is
   a_S(o) = max{d(x, y) : x O_o y}, the largest peak distance between two
   states the observer identifies at o (taking the larger direction when
   moves are one-way). It falls as o rises.
5. **The boundary of T.** Let β(x, y) be the least observing budget whose
   probes separate x and y. Then (o, a) ∈ T exactly when
   o < min{β(x, y) : x A_a y, x ≠ y}. The bound falls as a rises.

Checked with python3 -I: on 2,000 random systems of six states with random
peak costs and four probes of random cost, both boundary formulas agreed
with the definitions at every grid point.

## The worked case

On [CASE-tmp0d5si](../cases.d/CASE-tmp0d5si.md)'s states with A's one-way costs read as peak costs, the
three states become mutually reachable only at a = 3. With two probes of
the assistant's choosing, "flat or folded" at cost 1 and "which side" at
cost 2:

| | a < 3 | a ≥ 3 |
|---|---|---|
| o < 1 | T only | S and T |
| 1 ≤ o < 2 | T only | S only |
| o ≥ 2 | S and T | S only |

The two partitions agree in two regions: below o = 1 and from a = 3, all
three states are one class both ways; from o = 2 and below a = 3, all three
are distinct both ways. Between them, at o in [1, 2) and a ≥ 3, the
system can turn L into R while the observer can tell U from them but not
L from R.

## What it adds

- **A computable invariant of two-budget individuation.** [CLAIM-tmp42yq0](CLAIM-tmp42yq0.md)
  says the outside and inside partitions move in opposite directions; this
  gives the two boundaries at which one contains the other, and the region
  where they coincide, as numbers to compare across systems.
- **An allocation problem.** Where observing and acting share one budget,
  o + a ≤ B, the boundaries say what each split buys: enough acting budget
  to make every indistinguishable pair reachable, or little enough that
  everything reachable stays indistinguishable. [QUESTION-tmp3icc7](../questions.d/QUESTION-tmp3icc7.md) asks
  where that trade bites.

## What it does not say

- It needs nested probe families and peak-cost reachability. Under
  additive costs A_a is not an equivalence, and S and T must be restated
  for a similarity.
- It says nothing about whether either partition constitutes the system's
  identity; that stays with the distinction between identification and
  constitution ([CLAIM-150](CLAIM-150.md), [QUESTION-284](../questions.d/QUESTION-284.md)).
- On the degree-4 vertex ([CASE-tmpe48yq](../cases.d/CASE-tmpe48yq.md), with the assistant's probe
  model) the partitions agree non-trivially in one window, where both pick
  out the flat state and the four half-branches; with the costs of the
  side and depth probes swapped the window disappears. So a non-trivial
  agreement is a fact about the mechanism and the cost of observing it
  together, not about either alone.
