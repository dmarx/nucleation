---
status: Proposed
title: 'That asking and answering are each resource-bounded does not make them compete: a common budget, a common bottleneck or a sequential dependence supplies the coupling, and a shared deadline is not a shared pool of worker-hours, since independent processes can spend the same elapsed time at once'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An architecture in which asking and answering draw on separate pools,
  neither waits on the other and they share no bottleneck, yet more of one
  still leaves less for the other; or a showing that boundedness alone
  already entails one of the three couplings.
tags:
- operations-research
- epistemology
date: '2026-11-23'
line:
- readiness
- learning-and-inquiry
answers:
- QUESTION-tmp3cft4
rests_on:
- CLAIM-475
- CLAIM-tmpiwxla
uses:
- TERM-085
summary: >-
  A52 (intro, §4 and §8) of the exchange "Explain First Contact RL"
  (ChatGPT, 2026-11-23), answering the owner's U27 ([QUESTION-tmp3cft4](../questions.d/QUESTION-tmp3cft4.md)).
  A52 separates resource boundedness, resource coupling and resource
  competition: the first is held ([CLAIM-475](CLAIM-475.md)), the second follows in
  particular architectures, and the third "requires additional
  conditions". Its table marks "Any query and target necessarily compete
  for the same scarce capacity" as "Not established; false in general".
  The wording is A's (ChatGPT, at A52 of the exchange "Explain First
  Contact RL"); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpiwxla CLAIM-tmp2dr12 CLAIM-tmp4u0mj CASE-316 — Proposed; the construction this rests on and the entries filed with it -->

# CLAIM-tmpq4crr: That asking and answering are each resource-bounded does not make them compete: a common budget, a common bottleneck or a sequential dependence supplies the coupling, and a shared deadline is not a shared pool of worker-hours, since independent processes can spend the same elapsed time at once

## The claim

A52 distinguishes three things:

> 1. **Resource boundedness:** Formulating a query and realizing an answer each require finite resources.
> 2. **Resource coupling:** The resources consumed by one process affect what remains available to the other.
> 3. **Resource competition:** Under a binding shared constraint, allocating more resources to one process reduces what can be allocated to the other.

and three architectures (§4): sequential dependence, where "Time spent
querying reduces the horizon remaining for answering, even with separate
resources"; concurrent activity with a shared bottleneck, where the two
"directly compete for limited capacities while running"; and concurrent
activity with independent resources, where "their resource consumption
need not directly compete". With vector-valued costs, a shared pool is
C_Q(q) + C_A(q, π) ⪯ B, and separate pools are C_Q(q) ⪯ B_Q and
C_A(q, π) ⪯ B_A, "plus whatever timing and communication dependencies
connect them". So "resource-boundedness alone does not imply competitive
coupling. **A common budget, a common bottleneck, or a sequential
dependency supplies the coupling.**"

On the deadline: "a shared deadline is not identical to a shared pool of
worker-hours. Two independent activities can each use five minutes during
the same five-minute interval. They consume elapsed time simultaneously,
not ten minutes of calendar time."

## Why it is demonstrated

It follows from the constraint forms. Under separate pools with no
dependence the feasible set is a product, so raising one process's spend
leaves the other's feasible set unchanged. Under a shared pool or a
precedence it is not. [CLAIM-tmpiwxla](CLAIM-tmpiwxla.md)'s construction is the time case:
overlapping stages that do not compete contribute the longest of their
durations, not the sum.

## What it does not say

- Not that time is not shared. A sequential dependence couples asking and
  answering through the deadline even with separate personnel, which is
  A52 §2's T_Q(q) + T_A(q, π) ≤ H and [TERM-085](../terms.d/TERM-085.md)'s "Planning is not free".
- Not that separate pools leave the two independent. Their outputs still
  interact: a better question can make the answer cheaper (A52 §2). That
  interaction is a coupling of the outputs, not competition for inputs.

## Where it goes next

A52 §3's depth of inquiry under a shared deadline is [CLAIM-tmp2dr12](CLAIM-tmp2dr12.md), and
the set of questions both posable and answerable under a joint schedule is
[CLAIM-tmp4u0mj](CLAIM-tmp4u0mj.md). Competition among stages sharing reviewers is [CASE-316](../cases.d/CASE-316.md)'s.
