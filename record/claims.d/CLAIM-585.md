---
number: 585
status: Proposed
formerly:
- CLAIM-tmpuk8gq
title: 'With several resources, the budgets that suffice for a transition form an upward-closed set whose minimal elements, when the transition paths are finitely many, form a Pareto frontier; the set need not be convex, so no threshold on a weighted total of the resources describes it'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a budget that suffices and a larger one
  that does not, a path in the toy that the budget (2, 2) covers, or
  weights w ≥ 0 and a threshold θ with {b : w·b ≥ θ} equal to the set of
  sufficient budgets in the toy. Not defeated by settings where the
  resources are freely convertible into one another, where a scalar
  threshold does exist; the claim is that the set need not be convex.
tags:
- mathematics
- operations-research
date: '2026-11-05'
line:
- readiness
- formal-apparatus
rests_on:
- CLAIM-571
uses:
- TERM-106
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4: transition
  budgets form an upward-closed set with a Pareto frontier of minimal
  elements, and in A's toy (3, 1) and (1, 3) work while (2, 2) does not.
  Stated and checked here for capacities held separately: a budget
  suffices when it covers some admissible path's peak in each resource.
  The toy's set is not convex, so no weighted total has a threshold that
  describes it. Mirth et al. note that the topological form of this needs
  multi-parameter persistence, which their paper does not develop. The
  construction is the filer's, from A's multi-resource budgets; adopting
  it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-571 THEORY-1420 CLAIM-354 CLAIM-555 — Proposed; A's proposals of 2026-11-04 and a reading's account, cited as filed, nothing here rests on their being settled beyond the rests_on -->
<!-- inactive-ok-file: NOTE-1585 CLAIM-563 NOTE-1609 NOTE-1568 — Proposed or new; the resource-bounded realizability readings of 2026-11-05, cited as open -->

# CLAIM-585: With several resources, the budgets that suffice for a transition form an upward-closed set whose minimal elements, when the transition paths are finitely many, form a Pareto frontier; the set need not be convex, so no threshold on a weighted total of the resources describes it

## The claim

**The construction.** Generalize [CLAIM-571](CLAIM-571.md) to m resources, each a
capacity held separately. Holding configuration q takes r(q) ∈ ℝ^m, and a
path γ needs its peak in each resource,

  ρ(γ) = (max_t r_1(γ(t)), …, max_t r_m(γ(t))).

The peaks may fall at different moments. A budget b ∈ ℝ^m suffices for the
transition A → B when b ≥ ρ(γ), componentwise, for some admissible path
γ. Write S(A, B) for the sufficient budgets.

- **Upward closed.** If b suffices and b′ ≥ b, then b′ ≥ ρ(γ) for the same
  path, so b′ suffices. S(A, B) is the union, over admissible paths, of
  the up-sets of their peak vectors.
- **A Pareto frontier.** When the admissible paths have finitely many
  peak vectors, the minimal elements of S(A, B) are the minimal ones
  among them, an antichain in the componentwise order, and S(A, B) is the
  up-set of that antichain. With infinitely many the infimum need not be
  attained: peaks (1 + 1/n, 1) for every n give no minimal element, only
  (1, 1) in the closure.
- **With one resource** S(A, B) is [B*, ∞), or (B*, ∞) when the infimum is
  not attained: the scalar threshold of [CLAIM-571](CLAIM-571.md).

**The toy.** A's: "(3,1) and (1,3) both work", while a budget of (2,2) admits neither route. Take two admissible paths with peaks (3, 1) and (1, 3). Then
S = up(3, 1) ∪ up(1, 3), the frontier is {(3, 1), (1, 3)}, and (2, 2)
covers neither: it falls short of (3, 1) in the first resource and of
(1, 3) in the second. Yet
(2, 2) is the midpoint of (3, 1) and (1, 3), and has the same total. So S
is not convex. Every set {b : w·b ≥ θ}, for weights w ≥ 0 and threshold
θ, is a half-space and convex, so none equals S. Checked by the filer.

**So there is no scalar threshold of the familiar kind.** A transition's
resource need is a frontier of alternatives. Two budgets with the same
total can differ in whether the transition is possible, and a budget can
be enlarged in total and still fall short if the increase is in the wrong
resource. A monotone scalar function with S as a superlevel set always
exists, for instance the indicator of S, so the point is not that no
scalar can be defined but that no weighted total can.

## What the reading adds

Mirth et al. ([NOTE-1616](../notes.d/NOTE-1616.md); [THEORY-1420](../theory.d/THEORY-1420.md)) give the one-resource case its
topology: sufficient budgets are the levels at which A and B share a
component of a sublevel set. With several resources the sublevel sets
are indexed by vectors and the topological summary is a multi-parameter
filtration. The paper mentions multi-parameter persistence only in
passing, in a citation, and gives no support for that extension. The
claim here does not need it: it is about which budgets suffice, not about
the topology of the sublevel sets.

## What it does not say

- **That organizations face several non-convertible resources.** Where
  every resource can be bought with one currency at the moment it is
  needed, the resources collapse into one and a scalar threshold returns.
  A: "money cannot always be converted into the resource needed on the relevant timescale." That is the condition under which the claim bites;
  whether it holds is empirical.
- **Anything about cumulative or rate-limited resources.** A path's need
  for those is not its peak.
- **Anything beyond inclusion.** The order is componentwise inclusion, the
  same order by which [CLAIM-354](CLAIM-354.md) compares what agents can viably reach; it
  leaves incomparable budgets incomparable.
- **The nerve over several acceptance sets** that [CLAIM-555](CLAIM-555.md) takes. That is
  a complex of demands, not of resources.

## Note of 2026-11-05: the resource-bounded realizability readings

Readings filed beside the pasted synthesis on resource-bounded realizability support the frontier and say what an enrichment must use to keep it. The readers of Lawvere ([NOTE-1585](../notes.d/NOTE-1585.md)) and of Marsden and Zwart ([NOTE-1602](../notes.d/NOTE-1602.md)) note that a product of two quantales gives each hom the componentwise infimum over paths. For the claim's two paths with peaks (3, 1) and (1, 3) that is (1, 1), which suffices for neither. So the hom must be an up-set of budgets, as the claim already has it. The derivation is the readers', and [CLAIM-563](CLAIM-563.md) records it.

The readers of Vipond ([NOTE-1609](../notes.d/NOTE-1609.md)) and of Botnan and Lesnick ([NOTE-1568](../notes.d/NOTE-1568.md)) find a topological counterpart, by analogy. Multiparameter persistence of sublevel sets is the right object, and its features need not be intervals. But the standard summaries are incomplete, so none is guaranteed to recover the frontier. No status changes.
