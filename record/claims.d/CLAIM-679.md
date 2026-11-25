---
number: 679
status: Active
formerly:
- CLAIM-tmpfrjqq
title: 'For a fixed architecture and one resource that must be held at each moment, cutting the resource an organization holds toward what holding its present configuration requires leaves that configuration feasible and removes exactly the transitions whose threshold lies between the old holding and the new, so that at the limit the organization can still hold where it is and can reach no configuration whose transition carries any reconfiguration slack'
version: 4
history:
- version: 2
  date: '2026-11-17'
  note: >-
    A dated note: A64 §6 of the exchange "Assess Depp Heard Abuse"
    gives the claim's structure with an adversary, a small added cost
    that moves a remedy across the claimant's budget, and points to
    the claim without its code. No other change.
- version: 3
  date: '2026-11-18'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings; ADR-057). Its one premise, CLAIM-571, is Active, and the
    construction under it, CASE-233, was promoted at the same review after
    a step-by-step re-derivation. The derivation was re-checked: with
    R(H) the targets whose bottleneck budget is at most H, R is monotone
    in H, so a cut from H1 to H2 removes exactly the targets with
    H2 < B*(A, B) ≤ H1 and adds none; at H = r(A), since
    B*(A, B) ≥ max(r(A), r(B)), what is left is the targets with
    B*(A, B) = r(A), each with zero slack in TERM-106's unqualified
    sense σ, so no transition with positive σ, and no target costing more
    than A to hold, stays in reach. The title's slack is σ, as TERM-106
    reads an unqualified use; under the one-sided σ_A the limit clause
    holds exactly. Reachability at a holding equal to B* is the defeat
    condition's stipulation. No objection is on file, nothing meets the
    defeat condition, and the instance (7, 7, 13) checks. The text is
    unchanged.
- version: 4
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144), the owner's
    manuscript from the exchange "Explain First Contact RL": A48 §9.1
    states it: cutting to the holding cost keeps the configuration and
    removes the transition. No other change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation from CLAIM-571: a transition whose bottleneck
  budget lies between the old and the new holding that remains reachable
  after the cut, or one outside that interval that the cut makes
  unreachable, under CLAIM-571's scope (a fixed architecture, one
  resource held at each moment, reachability meaning the holding is at
  least the bottleneck budget). Not defeated by organizations that can
  borrow, change architecture or hold several resources, which the scope
  excludes and CLAIM-579 and CLAIM-587 treat; nor by cuts that are
  justified on other grounds, which the claim does not judge.
tags:
- society-and-governance
- operations-research
- complex-systems
date: '2026-11-13'
line:
- readiness
rests_on:
- CLAIM-571
uses:
- TERM-106
complements:
- CLAIM-579
- CLAIM-587
summary: >-
  A's sentence, from A20 §IV of the exchange "Analyze technological
  civilization trap" (2026-11-13): "A society can become more efficient
  at reproducing its current organization while becoming less capable of
  transforming that organization." The first filing recorded it on
  [CLAIM-571](CLAIM-571.md) as a label with its parameter, what "efficient" means, left
  open. A20 §IV fixes it: an organization "that maximizes short-term
  efficiency may eliminate resources that appear unnecessary for current
  operations". With efficiency read as cutting the resource held toward
  what the present configuration requires, the sentence follows from
  [CLAIM-571](CLAIM-571.md) and [TERM-106](../terms.d/TERM-106.md), exactly and for any target: the cut removes
  every transition whose threshold lies above the new holding and at or
  below the old. A20 §IV's hypothetical of two arrangements costing seven
  units each with a transition peak of thirteen is the instance.
  Demonstrated; the derivation is in the body. Filed on 2026-11-13 from
  the items the first filing left. The wording is A's; adopting it is the
  owner's call.
works:
- governance-of-possibility
---

# CLAIM-679: For a fixed architecture and one resource that must be held at each moment, cutting the resource an organization holds toward what holding its present configuration requires leaves that configuration feasible and removes exactly the transitions whose threshold lies between the old holding and the new, so that at the limit the organization can still hold where it is and can reach no configuration whose transition carries any reconfiguration slack

## The sentence and its parameter

A20 §IV of the exchange (https://chatgpt.com/share/6af6b47c-8b0c-83ea-ae04-3e3eb2649597):

> A society can become more efficient at reproducing its current
> organization while becoming less capable of transforming that
> organization.

The open parameter was "efficient". A20 §IV fixes it in the sentence
before: "An organization that maximizes short-term efficiency may
eliminate resources that appear unnecessary for current operations." So:
an organization at configuration A holds an amount H of the resource, and
a cut that keeps A feasible lowers H toward r(A), what holding A requires.
That is more efficient at reproducing A in the plain sense that the same
configuration is held on less.

## The derivation

[CLAIM-571](CLAIM-571.md)'s scope: a fixed architecture, one resource that must be held at
each moment. Its bottleneck budget B*(A, B) is the least, over admissible
paths from A to B, of the peak requirement along the path, +∞ if none.
The organization can reach B from A with holding H exactly when
H ≥ B*(A, B). Write R(H) = {B : B*(A, B) ≤ H}.

1. **A stays feasible.** Every cut considered keeps H ≥ r(A).
2. **The cut removes exactly an interval of thresholds.** R is monotone
   in H. Cutting from H₁ to H₂ < H₁ removes from R exactly the targets
   with H₂ < B*(A, B) ≤ H₁, and adds none.
3. **At the limit.** At H = r(A), R(H) = {B : B*(A, B) = r(A)}. Since
   B*(A, B) ≥ max(r(A), r(B)) ([CLAIM-571](CLAIM-571.md)), these are the targets that cost
   no more than A to hold and whose transition needs nothing beyond A's own
   requirement: zero reconfiguration slack ([TERM-106](../terms.d/TERM-106.md)). Every transition
   with positive slack, and every target that costs more than A to hold,
   is out of reach.

So the organization becomes no less able to hold A and strictly less able
to move, whenever some target's threshold lay in the interval cut. That is
A's sentence, with "efficient" fixed.

## The instance

A20 §IV's hypothetical, labelled by A as such: two arrangements each
require seven units, and the transition between them peaks at thirteen,
since it means "temporarily operating both infrastructures, retraining
personnel, and maintaining essential services during the transition".
r(A) = r(B) = 7, B*(A, B) = 13, slack 6. Any holding from 7 up to but not
including 13 keeps A and cannot reach B. A cut from 13 to 12.9 is already
fatal to the transition; a cut from 20 to 13 costs it nothing. The first
filing noted this example on [CLAIM-571](CLAIM-571.md).

## What it does not say

- Not that efficiency is bad. A: "Not unlimited reserves. Not inefficiency
  for its own sake. But sufficient and appropriately situated resources
  for justified change."
- Not that holding more is enough. [CLAIM-579](CLAIM-579.md): a reserve is described by
  where it can be applied, and ample slack can sit away from the
  bottleneck. [CLAIM-587](CLAIM-587.md): where response needs several complementary
  capacities, one's utilization need not track response capability.
- Not which transitions an organization ought to keep within reach. That
  is a judgment the derivation leaves to whoever cuts.

## Note of 2026-11-17: the adversarial instance, from "Assess Depp Heard Abuse"
<!-- inactive-ok-file: CASE-287 CLAIM-748 — filed from the exchange "Assess Depp Heard Abuse" on 2026-11-17, Proposed -->

A64 §6 of the exchange "Assess Depp Heard Abuse" (https://chatgpt.com/share/6afcb46d-83a8-83e9-9c85-4a0c3604405b, 2026-11-16) proves "**Proposition 3 — Procedural feasibility crossing**": with C_B^J(u) the least a claimant must spend to reach remedy J under an opponent's conduct u, C_B^J(u_0) ≤ K_B < C_B^J(u_1) makes J reachable under u_0 and not under u_1. Its instance: enforcement needs $98,000, the claimant has $100,000, and $5,000 of unnecessary expense removes the remedy. A: "It connects to Nucleation's work on slack and reconfiguration capacity", which is this claim, uncited.

The structure is this claim's, with two differences. Here a cut in the resource held removes exactly the transitions whose threshold lies between the old holding and the new; there an added requirement removes exactly the objectives whose cost it pushes past the holding. And here the resource is held at each moment, while A64's is a budget spent over the dispute. Both say that what is lost is fixed by which thresholds fall in the gap, so a small change near a boundary can remove a whole option. A64 adds the adversary: "**An adversary possesses procedural foreclosure power when its available choices can move another party's justified corrective objective across a resource-feasibility boundary.**" Rechecked in [CASE-287](../cases.d/CASE-287.md); it grounds [CLAIM-748](CLAIM-748.md).

No status changes.

## Note of 2026-11-23: the manuscript governance-of-possibility

<!-- inactive-ok-block: ADR-144 — Proposed; the work and the fill this note names -->
Extension. In A48 §9.3 of the owner's manuscript ([ADR-144](../decisions.d/ADR-144.md)), this
claim's zero-slack limit is what decides whether a redesigned transition can
replace a reserve: only a redesign whose threshold is at most the holding
cost does ([CLAIM-1099](CLAIM-1099.md)).

## Note of 2026-11-23: a gap of the manuscript governance-of-possibility

<!-- inactive-ok-block: CLAIM-646 — Proposed; the cumulative-cost limit -->
Converse, the assistant's. A gap of the manuscript governance-of-possibility, §9.7 (GC3). For one capacity held at each moment and finitely many paths, a path is affordable exactly when the budget is at least its peak ([CLAIM-571](CLAIM-571.md)). With path thresholds θ₁ < … < θ_k, the set of affordable paths is constant on each interval [θ_j, θ_{j+1}). Where readiness depends on the budget only through that set (more budget does not cross a path faster), readiness is a step function of the reserve B − r(q), with steps only at θ_j − r(q). A reserve strictly between two thresholds buys exactly what the lower one buys, and costs more. This claim is the downward half: cutting the holding removes exactly the transitions whose thresholds fall in the gap. The manuscript's study shows both in its model: R(6) = 0.269 for every reserve from 0 to 1.75 in the original architecture and 0.907 at 2; in the redesigned one, 0.151 from 0 to 0.75, 0.664 from 1 to 1.75 and 0.907 at 2 (scratch/manuscripts/governance-of-possibility/analysis/results.json, read with python3 -I). It need not hold with several resources, where the sufficient budgets form an upward-closed set with a Pareto frontier ([CLAIM-585](CLAIM-585.md)), or with cumulative costs ([CLAIM-646](CLAIM-646.md)). The note is the assistant's (Claude, in this session); adopting it is the owner's call. No status change.
