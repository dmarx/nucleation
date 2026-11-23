---
status: Open
title: What object secures readiness again after each retuning, a family of demand
  specifications closed under the move from D to each alternative with readiness
  for the family required again from there, or a viability kernel defined recursively
  over sequences of changes, and do the two coincide?
version: 1
tags:
- control-theory
- mathematics
- society-and-governance
date: '2026-11-23'
line:
- realizability
- readiness
summary: 'A gap of the manuscript governance-of-possibility, §8.6 (GA3): the second-order
  kernel of [TERM-tmpz28l1](../terms.d/TERM-tmpz28l1.md)''s note of 2026-11-23 "secures one retuning", and the
  manuscript names two stronger objects that the record holds neither of. The wording
  is the assistant''s (Claude, in this session); adopting it is the owner''s call.'
---

<!-- inactive-ok-file: TERM-tmpz28l1 — Proposed or Open; the construction this extends and the simulator that could test it -->

# QUESTION-tmpxcoa5: What object secures readiness again after each retuning, a family of demand specifications closed under the move from D to each alternative with readiness for the family required again from there, or a viability kernel defined recursively over sequences of changes, and do the two coincide?

## What makes it open

[TERM-tmpz28l1](../terms.d/TERM-tmpz28l1.md)'s second-order kernel, V_adaptive = Viab(M_D ∩ ⋂_{D′∈𝔇}
T_{D→D′}), keeps a route from D to each declared D′. Nothing requires a
route onward from D′. An ecosystem that spends its whole reserve reaching
readiness for D′ satisfies the construction and may arrive with no route
anywhere else. Under the peak budget rule this is the ordinary case: a
transition made leaves the budget at its peak for one period, and after a
period of holding the routes onward are gone ([CLAIM-577](../claims.d/CLAIM-577.md)).

Two candidates, from the manuscript's §8.6:

1. **Closure.** A family 𝔇 closed under the move from D to D′, with the
   readiness set at D′ itself required to be the M_adaptive of the family
   seen from D′.
2. **Recursion.** A kernel over sequences of changes: the largest family of
   sets V_D, one for each D in 𝔇, such that V_D is viable within M_D and
   from each of its states each D′ is reachable, affordably and safely
   within H, into V_{D′}. The operator taking such a family to the next is
   monotone in the sets it is given, so a largest fixed point exists
   (Knaster–Tarski); whether iteration reaches it, and whether it agrees
   with the closure, is not settled. That observation is the assistant's.

## What would count as an answer

A definition with a separating case: a state ready for one retuning and
not for two, and the condition under which the closure and the recursion
coincide. [LEAD-tmpnblsf](../leads.d/LEAD-tmpnblsf.md)'s simulator, with a second contingency after the
first, would exhibit the case in a model.
