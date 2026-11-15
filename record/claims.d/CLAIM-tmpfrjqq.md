---
status: Proposed
title: 'For a fixed architecture and one resource that must be held at each moment, cutting the resource an organization holds toward what holding its present configuration requires leaves that configuration feasible and removes exactly the transitions whose threshold lies between the old holding and the new, so that at the limit the organization can still hold where it is and can reach no configuration whose transition carries any reconfiguration slack'
version: 1
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
---

# CLAIM-tmpfrjqq: For a fixed architecture and one resource that must be held at each moment, cutting the resource an organization holds toward what holding its present configuration requires leaves that configuration feasible and removes exactly the transitions whose threshold lies between the old holding and the new, so that at the limit the organization can still hold where it is and can reach no configuration whose transition carries any reconfiguration slack

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
