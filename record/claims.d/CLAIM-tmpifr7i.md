---
status: Proposed
title: 'In the coupled meaning–influence model with declared demands, the frustration of satisfiable demands follows the allocation of influence when search and information are held fixed, but a captured allocation acts as a fixed weighting rule, so the model shows the governance-induced kind caused by allocation without showing conferral dynamics causing what no fixed weighting would'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-081, from the
    executed study CASE-tmpgustv.
role: thesis
warrant: empirical
defeated_if: >-
  Reruns of CASE-tmpgustv's protocol (scratch/studies/lead-081/), at other
  demand configurations, more demands or dimensions, another update map
  held fixed across rules, or an exact allocation oracle, in which changing
  only the conferral rule from scoring by agreement to scoring by each
  demand's own residual does not lower the share of steps with a
  satisfiable demand unmet by more than changes of step size, noise or
  conditioning do; or in which a captured allocation leaves satisfiable
  demands unmet in a way that no fixed weighting reproduces. A change to
  the scores that lets information pass through the update in Regime B
  does not count, and neither does a shorter run that stops before capture.
tags:
- self-governance
- complex-systems
- operations-research
date: '2026-11-22'
line:
- distributed-agency
- will-organization
grounds:
- CASE-tmpgustv
complements:
- CLAIM-500
- CLAIM-357
bears_on:
- QUESTION-124
summary: >-
  LEAD-081's experiment, run as CASE-tmpgustv. With the update map and the
  gradients the same under every rule, scoring components by agreement with
  the update made captures influence and leaves a satisfiable demand unmet
  on 0.95 of steps; scoring each by its own demand's residual gives 0.05.
  Step size, curvature and noise move the first rule less, and lower it
  only by stopping capture. So frustration follows the allocation, as
  CLAIM-500 and CLAIM-357 expect. But the captured state is a fixed
  weighting, a fixed uniform weighting fails about as often, and a fixed
  weighting chosen in hindsight does as well as the second rule. The model
  separates allocation from search and information. It does not separate
  conferral dynamics from a fixed weighting rule, which CLAIM-500's
  defeater counts as an optimizer mechanism. Whether that supports
  CLAIM-500 or leaves its stronger form open is left to the owner as two
  readings. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-500, CASE-tmpgustv, CLAIM-tmpifr7i — Proposed or new; the thesis the study tests and the entries this filing made -->

# CLAIM-tmpifr7i: In the coupled meaning–influence model with declared demands, the frustration of satisfiable demands follows the allocation of influence when search and information are held fixed, but a captured allocation acts as a fixed weighting rule, so the model shows the governance-induced kind caused by allocation without showing conferral dynamics causing what no fixed weighting would

## The claim

CASE-tmpgustv builds CASE-099's loop with three declared demands and an exact feasible-update oracle (CLAIM-365). The update map and the gradients are the same under every rule, and only the conferral rule changes. Three things follow in that model.

1. **Frustration follows the allocation.**
   - With every requirement satisfiable by some allocation, Regime A (scoring by agreement with the update made) leaves one violated on 0.953 of steps.
   - Regime B (scoring by each demand's own residual) gives 0.052, and an allocation oracle gives 0. Regime A is worse on all 200 paired instances.
   - Step size moves Regime A between 0.906 and 0.962, gradient noise to 0.68–0.70, and conditioning to 0.58. Every one of these leaves it far above Regime B, and the changes that lower it most also stop capture.
   - That is the intervention CLAIM-357 says identifying governance-induced frustration needs, "an intervention on the allocation with search and information held fixed", and the shape LEAD-081 counts as support.
2. **The captured allocation is a fixed weighting.**
   - Once capture is complete the update is a fixed vertex weighting.
   - A fixed uniform weighting fails on 0.89 of steps, without any conferral.
   - The best of 66 fixed weightings, chosen per instance in hindsight, does as well as Regime B (0.050, and 0 on 57 of 60 instances).
   - What the loop adds is endogeneity: it picks the weighting from the start's geometry (the nearest demand wins 54% of the time) and holds it. Without an oracle, Regime B is the rule that finds the right weighting.
3. **The local oracle can misclassify.** Where the demands are jointly infeasible, a captured allocation moves the state to where CLAIM-365's one-step residual is negative on 87% of steps. The local test then reports as governance-induced what is globally structural.

## Two readings, for the owner

CLAIM-500's defeater counts "a fixed weighting rule" among the optimizer mechanisms whose sufficiency would make the governance-induced category idle.

- **Reading 1: the result supports CLAIM-500.** A weighting is an allocation of influence. That the right one is found only by changing how conferral is earned, and not by any optimizer setting, is the work the category does.
- **Reading 2: it leaves CLAIM-500's stronger form unsupported.** Every observed failure is, once capture is complete, a fixed-weighting failure that an optimizer analysis given the weights describes without modelling conferral.

This claim is common ground between the two. It takes no side.

## What it does not say

- That any organization behaves so: the model is fictional, and its demands and scores are the modeller's (CLAIM-288).
- That search never matters: one update map was tried, and A40's representational kind, an available update no allocation reaches, never occurred.
- That capture occurs at symmetry by CLAIM-330's threshold. The γ sweep is consistent with a threshold in γ that depends little on memory, between γ = 1 and γ = 2 here, but it was not derived.
- QUESTION-124's persistence condition. The case gives Γ ≈ 0.15 sustained while Φ ≤ 0 under Regime A. It does not give a condition in the parameters, or a dependence on the norm.
