---
number: 1115
status: Proposed
formerly:
- CLAIM-tmpj15c6
title: "At one budget, the questions an agent can formulate and the answers it can attain once a question is supplied do not fix which question–answer pairs it can attain together, but their budget-indexed families do when the costs of formulating and answering compose by a declared rule; what is left over is the rule, and where the way a question is formulated changes what answering it costs, not even the least costs fix it"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  Budget-indexed query and conditional answer frontiers, with an additive
  rule declared, that fail to fix the jointly attainable pairs at some
  budget; or a rerun of the four constructions below that does not reproduce
  them.
tags:
- mathematics
- operations-research
- epistemology
date: '2026-11-23'
line:
- learning-and-inquiry
- realizability
uses:
- TERM-092
complements:
- CLAIM-1025
summary: >-
  The assistant's gap fill for A58 §2 of the exchange "Explain First Contact RL" (2026-11-23). A58 says the
  joint inquiry relation "cannot be reconstructed from two independent
  frontiers" and proves it with two relations that share their projections.
  That shows only that a relation is not its projections; an answer frontier
  indexed by question already tells A58's pair apart. The gap is what the
  irreducibility does rest on. Four constructions, checked with python3 -I:
  one budget does not fix the joint pairs; the frontiers at every budget do,
  under an additive rule; the rule itself (sequential against parallel)
  matters; and when the formulation chosen changes the cost of answering,
  least costs overstate what is jointly attainable. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-1016 CLAIM-1025 — Proposed; the claim this supports, its argument, the authorization fill and the bounds filed from A52 and A54 -->

# CLAIM-1115: At one budget, the questions an agent can formulate and the answers it can attain once a question is supplied do not fix which question–answer pairs it can attain together, but their budget-indexed families do when the costs of formulating and answering compose by a declared rule; what is left over is the rule, and where the way a question is formulated changes what answering it costs, not even the least costs fix it

## The gap

A58 §2: "the inquiry frontier cannot be adequately described by separately
listing its query and answer components", shown by 𝓕_1 = {(q_1, a_1),
(q_2, a_2)} and 𝓕_2 = {(q_1, a_2), (q_2, a_1)}, equal projections onto
Q and onto A. True, and true of every relation. A58 itself defines the
answer frontier per question; indexed so, 𝓕_1 and 𝓕_2 differ already (the
check below). The argument the claim needs is §1's, the shared budget, and
it was not worked out.

## The derivation

Write c_Q(q) for the least cost of formulating q, c_A(q, a) for the least
cost of producing and evaluating a when q is supplied, Q_ask(B) =
{q : c_Q(q) ≤ B} and A_cond(B) = {(q, a) : c_A(q, a) ≤ B}.

1. **One budget does not fix the joint pairs.** System 1: c_Q = 10,
   c_A = 10. System 2: c_Q = 2, c_A = 10. At B = 12 both have
   Q_ask = {q} and A_cond = {(q, a)}. Under sequential spending the
   joint pairs are those with c_Q + c_A ≤ B: none for system 1 (20 > 12),
   (q, a) for system 2 (12 ≤ 12).
2. **The families over budgets do, under a declared rule.** From Q_ask(B)
   and A_cond(B) for every B the least costs are recovered as the least B at
   which each item appears, and with the additive rule the joint set at every
   B follows. Checked on both systems over B = 0…39: the recovered joint set
   equals the true one at every budget.
3. **The rule matters.** c_Q = c_A = 6, horizon 10: sequential, 12 > 10,
   not jointly attainable; in parallel (the maximum, 6 ≤ 10), attainable. So
   the frontiers with their costs still need the schedule: A58's
   "Parallelism and managerial authorization therefore belong to the inquiry
   frontier itself".
4. **Formulation can change the cost of answering.** Two ways to formulate
   q: one costs 2 and leaves an answer costing 9, the other costs 6 and
   leaves 3. Least costs are 2 and 3, sum 5. True joint cost: 9 (6 + 3).
   At B = 5 and B = 8 the least costs say attainable and it is not; at 9 and
   11 both agree. Where formulating is part of answering, even the
   budget-indexed frontiers overstate the joint set, and the relation must be
   stated over processes, as A58's 𝓕 is.

The check is a short script run with `python3 -I` on 2026-11-23; it printed
each result above, and that the indexed answer frontiers of A58's 𝓕_1 and
𝓕_2 differ.

## Beside the bounds from A52 and A54

[CLAIM-1025](CLAIM-1025.md), filed from A52 §7 and A54 §7 the same day, gives the bounds
the separate frontiers do fix: an outer bound, each process fitting alone,
and an inner bound, the two run one after the other. Constructions 1 and 3
are its organizations in miniature. Construction 4 qualifies its inner
bound: that bound adds the least cost of posing to the least cost of
answering, and holds when the cost of answering does not depend on how the
question was posed. Where it does, the true joint cost can exceed the sum of
the least costs (9 against 5 above), so a question inside the computed inner
bound can still be jointly out of reach.

## What follows

A58's conclusion stands on its §1, not its §2: the joint relation is a site
of its own because the coupling (the composition rule, the schedule, and
what formulating does to answering) is not in either frontier. "Changes to
the coupling between the two processes can expand, contract, or reshape the
frontier even when their separately measured capabilities remain
unchanged" (A58 §3) is construction 1 read the other way. An authorization
stage is one more cost in the same composition ([CLAIM-1016](CLAIM-1016.md)).

## Standing

Proposed, the assistant's.
