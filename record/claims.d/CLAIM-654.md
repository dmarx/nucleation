---
number: 654
status: Proposed
formerly:
- CLAIM-tmpff0cq
title: 'Reachability by a given process grows with the budget when the process''s choices do not depend on how much budget remains and success means reaching the target within the budget; a process whose choices depend on the remaining budget can reach a target at a small budget and miss it at a larger one, though the admissible-path reachability of the same architecture grows with the budget'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below or in CASE-245. As a contribution,
  defeated if CLAIM-560 or CLAIM-567 already states that monotonicity in
  the budget holds for the admissible-path filtration and not for a
  process whose policy varies with the budget. CLAIM-560 states the first
  half for paths and is silent on processes; CLAIM-567 defines reliable
  attainment for a process and is silent on budgets.
tags:
- mathematics
- operations-research
- learning-theory
date: '2026-11-12'
line:
- realizability
- formal-apparatus
complements:
- CLAIM-560
- CLAIM-567
grounds:
- CASE-245
bears_on:
- QUESTION-279
summary: >-
  The assistant's, the second of the ideas offered after filing the
  exchange "Medical Ethics and Media Enshitification" (2026-11-11), which
  the owner accepted on 2026-11-12. It marks the scope of [CLAIM-560](CLAIM-560.md)'s
  monotonicity. The reachability filtration grows with the budget because
  it counts paths; what a given process reaches grows only if the process
  does not change with the budget. The owner's PASS@(k,T) link
  ([CLAIM-663](CLAIM-663.md)) needs this premise, and [ARG-093](../arguments.d/ARG-093.md) noted its absence.
  The proof is the assistant's; [CASE-245](../cases.d/CASE-245.md) is the construction, and
  [ARG-086](../arguments.d/ARG-086.md) weighs it. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-245 ARG-086 CLAIM-663 ARG-093 THEORY-1703 — Proposed; filed from the exchange of 2026-11-11 and its follow-up -->

# CLAIM-654: Reachability by a given process grows with the budget when the process's choices do not depend on how much budget remains and success means reaching the target within the budget; a process whose choices depend on the remaining budget can reach a target at a small budget and miss it at a larger one, though the admissible-path reachability of the same architecture grows with the budget

## The claim

Let a process run on an architecture for at most b steps, and let success
be visiting the target at some step ≤ b.

**Monotone case (proof).** If the process's choice at each step depends on
the history and not on the steps remaining, then its first b steps have
the same law whether the budget is b or b + 1. Couple the two runs on
those steps. Every run that visits the target within b steps does so
within b + 1. So P(success by b) ≤ P(success by b + 1), and the set of
targets reached with positive probability grows with b. The same holds
with any resource in place of steps, if the process's choices do not read
the remaining resource.

**Non-monotone case ([CASE-245](../cases.d/CASE-245.md)).** A process that takes s → g with one
step left and s → t (an absorbing trap) with more reaches g at b = 1 and
never at b ≥ 2. A path to g exists at every b ≥ 1.

## Where it sits

- [CLAIM-560](CLAIM-560.md)'s reachability filtration is the admissible-path one, and it
  grows with the budget. This claim is the limit of that monotonicity: it
  does not pass to what a particular adaptive process reaches.
- [CLAIM-567](CLAIM-567.md)'s "reliably reached" is a property of a process. Indexed by
  budget, it can fall as the budget rises.
- PASS@(k,T) ([THEORY-1703](../theory.d/THEORY-1703.md)) states monotonicity in T on the ground that
  "unused rounds are simply not exercised", which is the monotone case's
  premise. A trained policy whose behaviour depends on its turn budget
  violates it. The paper's Figure 1 shows per-depth estimates that fall
  with T in places (for the base model on comparison questions, 0.32 at
  T = 2 and 0.20 at T = 3, k = 1). That is a possible witness only: each
  depth is a separate set of 64 rollouts per problem, and the drop may be
  sampling noise.

## What it does not say

That budget-dependent processes are common or bad: spending a larger budget
on exploration is often right. It says only that monotonicity in the
budget is a property of paths, and of processes only under the stated
premise.

## Note of 2026-11-12: What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents? (Zhu, Jin, Tu, Men, Hao, Li, Liu, Zhao 2026), read

From the reading in [NOTE-1769](../notes.d/NOTE-1769.md) ([LIT-2414](../literature.d/LIT-2414.md)), the reader's assessment as
checked by the filer: **supports** its premise case. In Zhu et al. the
policy is told "the total and remaining budget" in the prompt, so its
choices depend on the remaining budget; Pass@T for such a policy need not be
monotone in T, and BudgetMix deliberately trains that dependence.
