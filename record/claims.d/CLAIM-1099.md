---
number: 1099
status: Proposed
formerly:
- CLAIM-tmpg8yl2
title: Under a budget set each period to the last period's peak use, a redesigned
  transition is lost like the original unless its threshold is at most the cost
  of holding the present configuration, so redesign lowers the reserve a transition
  needs by the fall in its threshold and replaces the reserve only where it leaves
  no reconfiguration slack
version: 1
role: counter
warrant: demonstrated
defeated_if: An error in the derivation or in scratch/formal/redesign_reserve_check.py;
  or a budget rule of the peak type under which a transition whose threshold exceeds
  the holding cost is kept, or one at or below it lost.
tags:
- operations-research
- mathematics
- society-and-governance
date: '2026-11-23'
line:
- readiness
- realizability
rests_on:
- CLAIM-577
- CLAIM-679
- CLAIM-571
objects_to:
- CLAIM-1093
summary: 'A gap fill on the manuscript governance-of-possibility (A48 §9.3–9.4):
  its table gives the redesigned regime an "accessible transition capacity" of 2,
  a reserve of one unit above the holding cost that the text never states, and under
  its own §9.1 rule that capacity is gone after one period. Checked by scratch/formal/redesign_reserve_check.py.
  The wording is the assistant''s (Claude, in this session); adopting it is the
  owner''s call.'
---


# CLAIM-1099: Under a budget set each period to the last period's peak use, a redesigned transition is lost like the original unless its threshold is at most the cost of holding the present configuration, so redesign lowers the reserve a transition needs by the fall in its threshold and replaces the reserve only where it leaves no reconfiguration slack

## The derivation

Take §9.1's rule: the next period's budget is the last period's peak use
([CLAIM-577](CLAIM-577.md)). Holding A uses r(A) = 1, so after one holding period the
budget is 1. A transition is affordable when the budget is at least its
threshold, the least peak over its paths ([CLAIM-571](CLAIM-571.md)). So after a holding
period a transition is kept exactly when its threshold is at most r(A).

A48's redesigned path has threshold 2 > 1, so under the rule it is lost
after one period, as the original (threshold 3) is. The table's
"accessible transition capacity 2" for Regime III is a budget held at 2:
a reserve of 2 − r(A) = 1. Redesign therefore lowers the reserve a
transition needs from θ − r(A) to θ′ − r(A), and replaces the reserve
only when θ′ ≤ r(A), that is, when the transition needs no more than
holding does, which is [CLAIM-679](CLAIM-679.md)'s zero-slack limit. Otherwise reserve and
redesign are complements, not alternatives.

The script `scratch/formal/redesign_reserve_check.py` runs the four
regimes (I, II, III under the rule, III with a reserve of 2) and asserts
the kept-exactly-when condition for thresholds 1, 2 and 3.

## What it does not say

- Not that redesign is worthless: it halves the reserve in A48's numbers.
- Not that the rule is the only one: a redesign that raises ordinary use,
  a drill each period at the transition's peak, keeps the route funded by
  the rule itself, which is a third mechanism.

## Gap filled

A48 §9.3–9.4: the unstated reserve in Regime III's row of the table.

## Note of 2026-11-23: a gap of the manuscript governance-of-possibility

<!-- inactive-ok-block: CLAIM-878 — Proposed; the drill already held -->
Extension, the assistant's. A gap of the manuscript governance-of-possibility, §9.5 (GC5). In the manuscript's model the redesign without a reserve (III-a) does worse than no redesign (I): at p = 0.02, R(6) is 0.147 against 0.267, mean response 14.83 against 12.76 periods, output 0.758 against 0.787. Outside money raises the budget to the least threshold ([CLAIM-577](CLAIM-577.md)'s step 4), and the redesign makes the cheapest route the slower staged one. With each edge crossed with chance 0.5 a period, three edges take 6 periods on average against the original's 4, a difference of 2 against the 2.07 observed. That rests on two of the modeller's choices that the record does not hold: outside money buys the cheapest route, not the fastest, and the staged route is longer. If it bought the fastest, III-a would match I. So "Not that redesign is worthless" holds with a reserve; without one, redesign can do worse than none. The "third mechanism" of "What it does not say", a drill each period at the transition's peak, is [CLAIM-878](CLAIM-878.md)'s, already held: "A drill each period holds the budget". The note is the assistant's (Claude, in this session); adopting it is the owner's call.

## Note of 2026-11-23: the study filed

<!-- inactive-ok-block: CASE-412 CASE-397 — new; the study filed -->
The manuscript's study is now on the record as [CASE-412](../cases.d/CASE-412.md), which illustrates this claim: its tests check that a redesigned route is kept under the peak rule exactly when θ′ ≤ 1, and its regime without a reserve (III-a) loses the route and falls below no redesign at all. Its novel-demand variant, [CASE-397](../cases.d/CASE-397.md), shows the reserve this claim says redesign does not replace serving a route the specification did not name. The note is the assistant's (Claude, in this session); adopting it is the owner's call.
