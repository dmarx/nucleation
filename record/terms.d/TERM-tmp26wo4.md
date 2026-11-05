---
status: Proposed
title: 'resource constraint, by type: a fixed stock, an instantaneous capacity, a rate limit, a cumulative expenditure, a replenishable reserve and a deadline, which bound different functions of a path and are not one budget'
version: 1
tags:
- operations-research
- control-theory
- mathematics
date: '2026-11-05'
line:
- distributed-agency
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4: a table of
  six resource types, M ≤ M_max, r(q,u) ≤ B, ‖u(t)‖ ≤ U_max, ∫ c dt ≤ E,
  ḃ = s(t) − c and T ≤ T_max, and a combined model with configuration,
  architecture, reserve and competency dynamics. Filed as a term, not a
  claim: it names the distinction other entries are stated in. Each type
  bounds a different function of a transition path (a quantity held, its
  supremum, the supremum of its rate, its integral, a running balance,
  its duration), so meeting one says nothing of another. "These are not
  equivalent problems." The wording is A's; adopting it is the owner's
  call.
---
<!-- inactive-ok-file: TERM-tmp2ysyt TERM-tmp46hcg CLAIM-tmpbi4ca CLAIM-tmpuk8gq CLAIM-tmp4g8e1 CLAIM-tmpancvu CASE-tmpqk2kd CASE-tmp0g3pa CASE-tmpe3itu CASE-tmp0s6cg — Proposed; A's proposals of 2026-11-04 and the entries filed beside them, cited as filed -->

# TERM-tmp26wo4: resource constraint, by type: a fixed stock, an instantaneous capacity, a rate limit, a cumulative expenditure, a replenishable reserve and a deadline, which bound different functions of a path and are not one budget

## Definition

A resource constraint on a transition is a bound on some function of the
path the system takes, and its type is which function. A's table, with
what each bounds made explicit by the filer, for a path q(t), input u(t)
and expenditure c(t) over [0, T]:

| type | A's form | what it bounds |
|---|---|---|
| fixed stock | M ≤ M_max | a quantity held, the same along the path |
| instantaneous capacity | r(q,u) ≤ B | the supremum of a requirement along the path |
| rate limit | ‖u(t)‖ ≤ U_max | the supremum of the input, how fast the path is driven |
| cumulative expenditure | ∫ c dt ≤ E | the integral of the expenditure |
| replenishable reserve | ḃ = s(t) − c, b ≥ 0 | a running balance, at every moment |
| deadline | T ≤ T_max | the path's duration |

A: "Two schedules could use the same total energy but require different
peak power. A transition could satisfy an annual expenditure budget but
fail because sufficient trained staff are not simultaneously available. A
system could possess adequate equipment but lack the actuator authority
to use it. These are not equivalent problems."

**Not one budget.** Because each bounds a different function of the path,
a path can meet one and fail another, and no single number orders paths
by all of them. CASE-tmpqk2kd holds the integral fixed at 2 unit-minutes
while the peak is 2 or 1 by the deadline. CASE-tmp0s6cg holds the stock
fixed while the capacity it supplies changes with configuration.
CASE-tmpe3itu is the rate limit and its placement, A's "actuator
authority". CASE-tmp0g3pa is a replenishable reserve with carry-over.
CLAIM-tmpbi4ca's bottleneck budget is the instantaneous-capacity case
alone, and CLAIM-tmpuk8gq shows that even several capacities do not
reduce to a weighted total.

**A's combined model.** With q the configuration, z the architecture, b a
reserve and k a competency:

  q̇ = f(q,z,u,w), ż = g(q,z,u,w), ḃ = s(t) − c(q,z,u), k̇ = −Dk + βm(t),

subject to F(q,z) = 0, b ≥ 0 and k ≥ k_min. The competency equation is a
replenishable stock that decays without practice m(t), the mechanism of
CLAIM-tmp4g8e1. A adds that when architectural changes are discrete "the
z dynamics would more naturally be modeled as a hybrid system with
switching rules and costs."

## What it is not

- **The three reserves** of TERM-tmp2ysyt (operational, reconfiguration,
  competency). Those sort reserves by what they are held for; this sorts
  constraints by what function of a path they bound. A reconfiguration
  reserve can be a capacity, a balance or a stock.
- **Organizational slack** (TERM-tmp46hcg), which is a quantity measured
  against current output, of any type.
- **A claim that organizations face all six.** Which bind is empirical;
  where every resource is convertible into one currency on the timescale
  that matters, several collapse into one, as CLAIM-tmpuk8gq notes for
  capacities.

## What would settle it

Adoption by the owner, or a claim of the record's own stated in it. One
candidate is CLAIM-tmpancvu, which states a form's three resource
requirements in these types.
