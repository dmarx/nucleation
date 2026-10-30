---
number: 456
status: Active
formerly:
- CLAIM-tmp2jayx
title: 'Maintaining a governing rule internally, by the organization''s own reciprocal production, can be more fragile than having it reset from outside: arrangements identical in ordinary operation can differ in which losses are repairable, and the self-produced rule can be lost to a double loss or an interruption of the work that produces it which outside reset survives'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted at the twentieth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings), with its ground
    CASE-161, whose figures were re-checked against the lab's stored
    results. A demonstrated existence result: nothing objects to it, and
    nothing in the record meets its defeated_if, since the three
    arrangements' undisturbed trajectories are identical in the stored
    results (v1.7: largest pre-intervention difference 0.0). The summary's
    "Proposed with its case" and the body's "Proposed" are dropped. The
    claim is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  A defect in CASE-161's runs that makes the three arrangements differ
  in ordinary operation, so that the comparison is not at matched
  behaviour; or a showing that the external reset in the lab is not a
  form of maintenance at all but a re-specification of the rule, so that
  nothing was compared. Not defeated by arrangements in which internal
  maintenance is the more robust one: the claim is that it can be the
  more fragile, not that it is.
tags:
- self-governance
- complex-systems
date: '2026-10-27'
line:
- distributed-agency
grounds:
- CASE-161
complements:
- CLAIM-414
summary: >-
  Stated in [CASE-161](../cases.d/CASE-161.md)'s "What it can show" ("internal maintenance can be
  the more fragile arrangement") and held by no claim, found in the audit
  of 2026-10-27. In the lab's 32-member population, with ordinary
  trajectories identical, reciprocal production restored one zeroed rule
  in 48 of 48 runs and both zeroed in 0 of 48, and lost both rules to an
  80-update producer outage in 48 of 48, where external reset restored
  every case. An existence result in one stipulated population. The edge: it says nothing against self-governance, only
  that self-production is not robustness.
---

# CLAIM-456: Maintaining a governing rule internally, by the organization's own reciprocal production, can be more fragile than having it reset from outside: arrangements identical in ordinary operation can differ in which losses are repairable, and the self-produced rule can be lost to a double loss or an interruption of the work that produces it which outside reset survives

## The claim

[CASE-161](../cases.d/CASE-161.md)'s v1.6 results, as stored, over 48 seeds with the three
arrangements' undisturbed trajectories identical: one rule zeroed once is
restored in 48 of 48 runs by reciprocal production and by external reset,
and in 0 of 48 with feedback only; both rules zeroed, reciprocal 0 of 48,
external 48 of 48; a producer team disabled for 80 updates, reciprocal
loses both rules in 48 of 48, external and feedback-only unaffected. The
case: "as [QUESTION-087](../questions.d/QUESTION-087.md) warns, that internal maintenance can be the more
fragile arrangement: here it fails on double loss and on a producer
outage, where outside reset does not."

[CLAIM-414](CLAIM-414.md) holds that matched trajectories conceal differences in how an
arrangement is maintained, and [CASE-161](../cases.d/CASE-161.md) is offered for it. This claim says
which way the concealed difference can cut. The record's vocabulary leans
the other way: [TERM-074](../terms.d/TERM-074.md)'s organizational maintenance and [CLAIM-424](CLAIM-424.md)'s
reflexive governance are capacities an organization has, and the
temptation is to read self-production as the robust case. A rule that
the organization's own processes produce depends on those processes, so
damage to them is damage to the rule; a rule reset from outside depends
on the outside.

## What it does not say

- **That outside maintenance is better.** It survives these damages
  because it does not depend on the producers; it has its own failure,
  dependence on the outside, which the runs do not test. [QUESTION-087](../questions.d/QUESTION-087.md) asks
  whether self-reproducing authority can be pathological by the
  organization's own standard, and this does not answer it.
- **Thresholds.** The survived outage lengths (32 and 36 updates, not 36
  and 40) are grid points under these laws, as the case says.
- **Anything beyond the stipulated population.** The case is an executed
  study in a lab model.
