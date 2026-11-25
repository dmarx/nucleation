---
number: 1081
status: Active
formerly:
- CLAIM-tmpdpnid
title: 'Bound operators delegate only to their own side'
statement: >-
  In a grant game on a population, operators bound by both grant conditions
  delegate their whole budget and only to operators on their own side of the
  decision, and under leave-one-out delegation the authority they pass
  beyond one hop also stays on their own side; the reward for realized
  policy does the aligning, the insensitivity of own authority removes what
  returns to oneself, and authority-seekers delegate at about chance under
  recursive delegation and not at all under a bound rule
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings; ADR-057): its ground CASE-420 went Active at this
    review; the defeat condition is not met on the rerun.
role: thesis
warrant: demonstrated
defeated_if: >-
  A rerun of the study's code (scratch/studies/lead-190/) in which
  operators under one-hop or leave-one-out aggregation with the
  realized-policy objective delegate less than their budget, or to their
  own side at no more than chance, or in which the authority they pass
  two hops or more goes to the other side; or in which authority-seekers
  under recursive delegation align their grants with their side beyond
  chance.
tags:
- self-governance
- game-theory
date: '2026-11-23'
line:
- distributed-agency
grounds:
- CASE-420
corroborates:
- CLAIM-285
complements:
- CLAIM-1147
bears_on:
- QUESTION-090
summary: >-
  The comparison [CLAIM-285](CLAIM-285.md)'s defeat condition names, run as a grant game
  among 20 operators on 30 populations. Bound operators (one-hop or
  leave-one-out authority, reward for realized policy) delegated their
  whole budget, all of it to their own side, against a chance share of
  0.47. Under leave-one-out, 43% of the authority their budgets placed
  travelled two hops or more, all of it to their own side, and none came
  back to them. Unbound operators (recursive authority, reward for
  authority held) delegated 0.96 of their budget, 0.52 of it to their own
  side, and recovered 0.15 of a unit each. The realized-policy objective
  aligned grants under recursive aggregation too. Authority-seekers under
  a bound rule never delegated. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-285 CLAIM-281 — Proposed; the claims tested, cited as open -->

# CLAIM-1081: Bound operators delegate only to their own side

## The claim

[CLAIM-285](CLAIM-285.md)'s defeat condition includes "a population model in which operators bound by the constraint stop delegating, or delegate no better than at random". Its notes say no such model had been run. [CASE-420](../cases.d/CASE-420.md) ran one.

- **Setup.** Twenty operators with preferred policies on two sides, budgets of 1, and damping η = 0.5. The decision is the authority-weighted mean of preferences ([CLAIM-375](CLAIM-375.md)). Operators move their grants by exact gradient ascent on their own objective less a quadratic grant cost.
- **Measures.** The first is the budget delegated. The second is the share of grants going to one's own side, against the chance share of 0.47. The third, beyond one hop, is the reach R_ik: authority at k per unit of i's budget. Its indirect part is what i's own grants do not carry directly.

Averaged over 30 populations:

1. **Bound operators delegate, and to aligned others.** Under one-hop aggregation they delegated their whole budget, 100% of it to their own side. The same held under leave-one-out damped delegation ([CLAIM-502](CLAIM-502.md)), which keeps the first condition beyond one hop.
2. **Beyond one hop, the authority stays aligned.** Under leave-one-out, 43% of the reach of a bound operator's budget was indirect, and all of it landed on its own side. None returned to it. Raising a grant there is not guaranteed to move the decision toward the granter: [CLAIM-285](CLAIM-285.md)'s note of 2026-10-30 records 1,772 such moves in 2,141 trials. In the population the incentive still sorted every grant.
3. **Unbound operators recycle and do not align.** Recursive aggregation with the reward for authority held is the unbound cell. These operators delegated 0.96 of their budget, 0.52 ± 0.14 of it to their own side, which is about chance and below it at N = 40 (0.43 against 0.49). Each recovered 0.15 of a unit of authority through cycles.
4. **What each condition does.**
   - With the realized-policy reward under recursive aggregation, grants were aligned 100%, and the authority returning to oneself fell to 0.03.
   - With the authority reward under one-hop or leave-one-out, nobody delegated: the gradient is the cost alone.
   - So the second condition, the reward for realized policy, does the aligning. The first, own authority insensitive to own grants, removes the return to oneself and the reason to delegate for authority's sake.

Linear cost and N = 40 gave the same pattern. Under linear cost the game cycles, so the measures there are time averages.

## What it does not say

- That the bound game is good for the organization. Every grant goes to one's own side, and within it to its extremes ([CLAIM-1147](CLAIM-1147.md)). When the same grant also sets whose evidence one reads, the population splits into factions that read only their own side ([CLAIM-1029](CLAIM-1029.md)). So [CLAIM-285](CLAIM-285.md)'s incentive works as it says, and with scalar grants it produces exactly what [CLAIM-281](CLAIM-281.md) warns of.
- That operators resist collusion, which [CLAIM-285](CLAIM-285.md) also disclaims. Coalitions were not modelled.
- That operators are exact optimizers in any real case. They are here by construction.
