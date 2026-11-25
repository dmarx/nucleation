---
number: 663
status: Proposed
formerly:
- CLAIM-tmpyc5md
title: 'The distinctions of the PASS@(k,T) analysis are the record''s distinctions of resource-bounded realization: its capability boundary is reachability by a given process under a budget, its efficiency is reliable attainment, and its interaction depth is a resource index, so whether an intervention expands what an organization can do or only makes it more reliable is the record''s question of reachable against reliably reached'
version: 2
history:
- version: 2
  date: '2026-11-18'
  note: >-
    Carries distributed-agency after its own line(s) under ADR-085,
    which it takes part in: bears_on QUESTION-279 (distributed-
    agency). Found at the line audit of 2026-11-18. No other change.
role: thesis
warrant: interpretive
defeated_if: >-
  The correspondence fails at a step the conclusion needs: the capability
  boundary is shown to be a property of the target and not of the process
  (feasibility rather than reachability), or reliability in the paper's
  sense (single-attempt success) is shown not to be CLAIM-567's reliable
  attainment, or interaction depth is shown not to be a resource under
  which reachable sets are monotone. Defeated as a contribution if the
  mapping adds no distinction, measure or test to CLAIM-567 and CLAIM-560.
tags:
- mathematics
- learning-theory
- operations-research
date: '2026-11-12'
line:
- realizability
- formal-apparatus
- distributed-agency
grounds:
- THEORY-1703
complements:
- CLAIM-567
- CLAIM-560
bears_on:
- QUESTION-279
summary: >-
  The owner's, U21 of the exchange "Medical Ethics and Media
  Enshitification" (2026-11-11): the discussion of who identifies
  normative demands "reminds me of the distinctions examined by the
  PASS@(k,T) work, and Nucleation's earlier engagement with resource
  boundedness and tolerance regions". The paper was read ([LIT-2441](../literature.d/LIT-2441.md),
  [THEORY-1703](../theory.d/THEORY-1703.md)). Its capability boundary maps onto [CLAIM-567](CLAIM-567.md)'s
  reachability by a process, its efficiency onto reliable attainment, and
  its depth T onto [CLAIM-560](CLAIM-560.md)'s resource index. The mapping holds with two
  qualifications, argued in [ARG-093](../arguments.d/ARG-093.md). A44's extensions are
  [CLAIM-662](CLAIM-662.md) and [CASE-249](../cases.d/CASE-249.md).
---
<!-- inactive-ok-file: THEORY-1703 ARG-093 CASE-249 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: CLAIM-555 — Proposed; the tolerance-indexed complex the owner's "tolerance regions" names -->

# CLAIM-663: The distinctions of the PASS@(k,T) analysis are the record's distinctions of resource-bounded realization: its capability boundary is reachability by a given process under a budget, its efficiency is reliable attainment, and its interaction depth is a resource index, so whether an intervention expands what an organization can do or only makes it more reliable is the record's question of reachable against reliably reached

## The claim

The owner, U21, on A42's question of how an organization identifies the
demands it is to be judged by: "reminds me of the distinctions examined by
the PASS@(k,T) work, and Nucleation's earlier engagement with resource
boundedness and tolerance regions".

The mapping, from the paper as read ([NOTE-1749](../notes.d/NOTE-1749.md)) to the record:

| PASS@(k,T) (Zhai and colleagues) | the record |
|---|---|
| capability boundary B_T(π): problems solved at least once under unlimited re-sampling at depth T | reachable: an admissible path leads to the target ([CLAIM-567](CLAIM-567.md)), for this process |
| efficiency: higher PASS@(1,T) on problems already in the boundary | reliably reached: the process ends there with high probability ([CLAIM-567](CLAIM-567.md)) |
| interaction depth T | a resource index under which reachable sets grow ([CLAIM-560](CLAIM-560.md)) |
| capability expansion against efficiency improvement | enlarging the reachable set against raising reliability inside it |

A44 §1 puts the three questions in organizational terms: "Is an acceptable
resolution possible? Can the organization discover it? Can it reliably
identify and implement it under the resources it actually has?" and says
what the paper adds: "an empirical strategy for examining the probability
of discovering a satisfactory trajectory across different exploration
budgets". The compatibility complex "normally records existence, not how
likely a particular organization is to find a witness."

"Tolerance regions" is [CLAIM-555](CLAIM-555.md)'s acceptance set at tolerance ε,
A_i(ε_i) = {θ : L_i(θ) ≤ ε_i}, with [CLAIM-537](CLAIM-537.md) and [CLAIM-550](CLAIM-550.md)'s tolerances
beside it. The paper has none: its success is exact match. A44's
tolerance-indexed generalization is [CASE-249](../cases.d/CASE-249.md).

## Two qualifications ([ARG-093](../arguments.d/ARG-093.md))

- The boundary is relative to a stochastic policy, not a move rule. A
  policy can behave differently with more budget, and the paper's own
  estimates fall with T in places, though its stated monotonicity says
  they should not. [CLAIM-560](CLAIM-560.md)'s reachable sets are monotone in the budget
  because the move rule is fixed.
- Success is judged by an oracle. In the record's setting the evaluator is
  part of the organization and can be wrong, which A44 §5 separates as
  "Oracle-assessed availability" from "Operational success".

## What it does not say

That reinforcement learning or any training method is a model of
organizational change. That a finite failure to find a solution shows
none exists: the paper's boundary at n = 64 means solved once in 64 rollouts, and
A44 says "an institutional claim that no acceptable remedy exists requires
more than repeated unsuccessful searches", which is [QUESTION-279](../questions.d/QUESTION-279.md).

## Note of 2026-11-12: What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents? (Zhu, Jin, Tu, Men, Hao, Li, Liu, Zhao 2026), read

From the reading in [NOTE-1769](../notes.d/NOTE-1769.md) ([LIT-2414](../literature.d/LIT-2414.md)), the reader's assessment as
checked by the filer: **supports, with the claim's qualification
sharpened**. Zhu et al. use the same metric and find (a) boundary expansion
along K and (b) that the ordering of two policies' success is not stable
across T: an advantage at large T can vanish or reverse at small T. That is
the record's distinction in action (what is reachable under a resource vs
reached), and it shows the resource index matters to which process "can do
more". Its finding that RL improves composition of locally plausible steps,
not per-step choice, is a third distinction the CLAIM does not draw:
reliability of a long path vs quality of each move.

## Note of 2026-11-15: the single-turn sources of the PASS@(k,T) dispute, read

<!-- inactive-ok-file: THEORY-1880 THEORY-1908 THEORY-1899 THEORY-1896 THEORY-1672 — Proposed; the single-turn readings of 2026-11-15 and the multi-turn account they are set beside, cited as the sources and an instance of the claim's columns, nothing here rests on them -->

The dispute PASS@(k,T) extends to agents is now held at its source.
- Brown et al. ([THEORY-1894](../theory.d/THEORY-1894.md)) supply the coverage metric, pass@k estimated per problem.
- Yue et al. ([THEORY-1880](../theory.d/THEORY-1880.md)) find single-turn RLVR raising pass@1 and lowering pass@k at large k, and read it as sharpening within the base model's prior.
- Liu et al.'s ProRL ([THEORY-1908](../theory.d/THEORY-1908.md)) contests this after long, diversity-preserving training from a distilled start model, with pass@k up to 128, and agrees with Yue on math.
- Meng et al. ([THEORY-1899](../theory.d/THEORY-1899.md)) find the RL-base difference sparse at the token level, mostly reallocation among tokens the base model already ranks.
- Balasubramanian and Kasiviswanathan ([THEORY-1896](../theory.d/THEORY-1896.md)) prove that a tilt of a frozen reference only reweights the modes it holds.

All five use the claim's two columns, boundary as reachability under a budget and pass@1 as reliability. Yue's crossover shows them moving in opposite directions under one intervention, which the agentic papers show only weakly (Zhai's bridge questions); [THEORY-1880](../theory.d/THEORY-1880.md) now corroborates the claim for that reason. The readings also bear on the claim's "expands what an organization can do": in the single-turn case, expansion is disputed and, where found, conditional on task and on the budget at which the boundary is read, as Zhu et al. ([THEORY-1672](../theory.d/THEORY-1672.md)) found for depth. No status change.

## Note of 2026-11-19: the exchange "Topological protection explained"

A69 §4 and A71 §4 set sophisticated active inference ([THEORY-426](../theory.d/THEORY-426.md)) beside this claim. Recursive planning selects trajectories prospectively, so an action with little immediate value can be chosen for the later observation it opens; PASS@(k,T) scores how reliably trajectories succeed at each budget. A69 §4: "The connection isn't an identity of metrics". A71 §4 calls them complements, "Policy selection" and "Resource-indexed outcome evaluation", not one measure, which fits this claim's columns: the planner is a process, and the metric reads its reachability and reliability under a budget.

A's proposal (A69 §4) is to judge an epistemic planner "by the resource-bounded repertoire of successful trajectories it actually produces", and to tell better selection among existing trajectories from expansion of the repertoire. That is this claim's question of reachable against reliably reached, asked of a planner. Nothing was run.

No status change.

## Note of 2026-11-23: the internal evaluator's errors are chosen, from [LEAD-181](../leads.d/LEAD-181.md)

The claim's second qualification separates "Oracle-assessed availability"
from "Operational success", the evaluator being part of the organization.
[CASE-396](../cases.d/CASE-396.md) shows the gap made by the organization's own choice: under a
penalty on recognized violations the institution's internal count ends
near 0 while the independent count is about 3.4 to 6.1, because it learns
not to inquire. The study did not use the tolerance axis or the breadth and
depth budgets of [CASE-249](../cases.d/CASE-249.md)'s pass rate. No status change.
