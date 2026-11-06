---
number: 212
status: Active
formerly:
- CASE-tmpsbhp8
title: 'Three demands and four configurations: each pair of demands is jointly met at some cost, the pairs enter the budgeted complex at budgets 1, 2 and 3, and the triple never does, so raising the budget relieves scarcity and leaves the frustration where it was'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings; ADR-057): a construction whose facts are its definition
    (ADR-042). Its budgeted complexes at every budget, and the
    implications its note of 2026-11-05 lists, were re-run by a second
    checker with python3 -I, with controls
    (scratch/formal/case212_check.py). Standing fictional is kept.
standing: fictional
kind: construction
tags:
- mathematics
- operations-research
- society-and-governance
date: '2026-11-05'
line:
- realizability
illustrates:
- CLAIM-586
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4: the
  resource-parameterized complex K(b). A gives the definition and a
  flat-foldable vertex as its mechanical case, without numbers; the four
  configurations, their costs and the demands they meet are the filer's.
  As the budget rises from 1 to 3 the complex gains the pairs {2,3},
  {1,2} and {1,3} in turn and becomes the hollow triangle; the triple is
  met by no configuration and enters at no budget. Two of the missing
  pairs at budget 1 are scarcity; the missing triple is frustration. The
  construction is the filer's, from A's resource-parameterized
  compatibility complex; adopting it is the owner's call.
---

# CASE-212: Three demands and four configurations: each pair of demands is jointly met at some cost, the pairs enter the budgeted complex at budgets 1, 2 and 3, and the triple never does, so raising the budget relieves scarcity and leaves the frustration where it was

## The case

**The construction (the filer's).** One resource. Four configurations,
each with what holding it costs and the demands it meets:

| configuration | cost R(q) | demands met |
|---|---|---|
| q₁ | 1 | {1} |
| q₂₃ | 1 | {2, 3} |
| q₁₂ | 2 | {1, 2} |
| q₁₃ | 3 | {1, 3} |

No configuration meets all three. K(b), the sets of demands some
configuration costing at most b meets ([CLAIM-586](../claims.d/CLAIM-586.md)):

- **b < 1**: no demand is met; only the empty set.
- **1 ≤ b < 2**: the vertices 1, 2, 3 and the edge {2, 3}.
- **2 ≤ b < 3**: adds {1, 2}.
- **b ≥ 3**: adds {1, 3}. Every pair is a face; the triple is not. This
  is K_Q, the complex with no budget, a hollow triangle.

Checked by the filer.

## What it can show

- **Scarcity and frustration in one picture.** At b = 1 the complex lacks
  {1, 2}, {1, 3} and {1, 2, 3}. The first two are short of resources:
  budgets of 2 and 3 admit them. The triple is a minimal non-face of K_Q,
  frustrated in [TERM-060](../terms.d/TERM-060.md)'s structural sense: no budget admits it while
  the four configurations and their demands are fixed. A: "independently
  plausible local folds may be globally incompatible because of loop
  closure or collisions." Each pair is plausible; the three together
  close no loop.
- **That a total is not a combination.** A: "An organization may have
  adequate total staffing yet lack the right combinations of skills at
  the right locations and times." A budget of 3 covers every
  configuration there is, and still no configuration meets all three
  demands.
- **What raising the budget buys.** Going from 1 to 3 is relief in
  [CLAIM-347](../claims.d/CLAIM-347.md)'s sense twice over, and leaves the minimal conflict
  untouched. Relieving it needs a new configuration, a change of
  architecture.

## What it cannot show

- **That organizations have such costs**, or demands with crisp
  acceptance sets. The table is invented to make the three budgets
  distinct.
- **Anything about paths.** Each face is met by some affordable
  configuration; whether the organization can move there is not asked.
- **What a hollow triangle means operationally**: whether the three
  demands can be met in turn, two at a time, is a question about
  sequencing, not about the complex.

## Note of 2026-11-05: the resource-bounded realizability readings

For the filing from the pasted synthesis on resource-bounded realizability, the reader of Ignatov ([NOTE-1593](../notes.d/NOTE-1593.md), read in part) worked this case's four configurations as a formal context, and the filer rechecked it by enumeration. For 1 ≤ b < 2, with q₁ and q₂₃ affordable, demands 2 and 3 imply each other, and {1, 2} and {1, 3}, met by no affordable configuration, vacuously imply all three demands. At b ≥ 2, q₁₂ breaks 2 → 3; at b ≥ 3, q₁₃ breaks 3 → 2. Only the triple keeps an empty extent at every budget, which is the frustration the case identifies. So as the budget rises the complex grows and the valid implications shrink, the antitone family of [CLAIM-564](../claims.d/CLAIM-564.md). The derivation is the reader's, from A's construction, not Ignatov's. No status changes.
