---
number: 498
status: Answered
formerly:
- QUESTION-tmp1j2mq
title: 'Do records kept of each capacity a response needs identify a reserve''s readiness for a contingency or only bound it, and which verdicts that rise with readiness can they settle?'
version: 1
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-20'
line:
- readiness
refines:
- QUESTION-395
summary: >-
  The part of [QUESTION-395](QUESTION-395.md) the record has answered, split off under [ADR-049](../decisions.d/ADR-049.md)
  at the status review of 2026-11-20. Records kept per capacity (rosters,
  training assessments, equipment availability, turnout times) fix only
  the capacities' marginal probabilities, which bound readiness between
  the Fréchet bounds and identify it only when the dependence is known.
  They refute a required readiness when the weakest capacity falls below
  it, certify it only when the shortfalls together stay within its margin,
  and leave the band between to joint evidence ([CLAIM-632](../claims.d/CLAIM-632.md)). The other
  observations, interventions and models the parent lists, and the weighing
  against cost, stay with [QUESTION-395](QUESTION-395.md).
---

# QUESTION-498: Do records kept of each capacity a response needs identify a reserve's readiness for a contingency or only bound it, and which verdicts that rise with readiness can they settle?

## Answer

[CLAIM-632](../claims.d/CLAIM-632.md) (Active, demonstrated) answers it. Where a response succeeds
exactly when each of n complementary capacities holds ([CLAIM-587](../claims.d/CLAIM-587.md)), records
of each capacity give the marginals Pᵢ, and readiness ([TERM-115](../terms.d/TERM-115.md)) lies in
[max(0, ΣPᵢ − (n − 1)), min Pᵢ]. Every value in that interval is attained by
some joint distribution, so the records identify readiness only when the
dependence is known or the interval is a point. For a verdict that rises
with readiness they settle it where it holds at the lower bound or fails at
the upper one; for a floor r*, they refute exactly when min Pᵢ < r* and
certify exactly when Σ(1 − Pᵢ) ≤ 1 − r*. Where each capacity only decays
between record and need ([CLAIM-558](../claims.d/CLAIM-558.md)), a refutation from records outlasts the
record and a certification does not.

## What it leaves to [QUESTION-395](QUESTION-395.md)

The other evidence the parent lists, incident histories, response-time
distributions, coverage simulations and counterfactual stress tests, beyond
[CLAIM-632](../claims.d/CLAIM-632.md)'s remark that joint evidence such as a deadline-bound exercise
decides the band between the bounds; and how evidence of readiness is
weighed against the capability's cost and its alternatives.
