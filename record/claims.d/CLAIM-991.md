---
number: 991
status: Proposed
formerly:
- CLAIM-tmpq92r4
title: 'Competence fixes readable, not answerable, queries'
statement: >-
  Among agents matched in competence on a goal family, competence fixes
  which predictive and interventional queries can be read out of each agent
  but not which the agent can answer within its own resources: in a small
  deterministic gridworld a planner on a learned transition table, a
  goal-conditioned value learner and a bank of occupancy predictors trained
  on the same experience answer every query family equally well when a
  transition table is read out of them, while within each agent's own
  per-decision computation each answers a different family
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  A matched-competence comparison in this class, with the per-decision
  budget stated, in which the agents' within-budget query competences
  coincide across the declared families, so that one score of query
  competence loses nothing. Or an error in the study's cost accounting that
  moves a family across the budget for some agent so that the families no
  longer separate. Not defeated by a cheaper procedure for some family
  that the agent does not itself run, which is the distinction the claim
  draws; nor by the families separating differently under another budget,
  which the claim allows.
tags:
- agency
- cognition
- representation-learning
date: '2026-11-22'
line:
- distributed-agency
grounds:
- CASE-384
corroborates:
- CLAIM-514
bears_on:
- QUESTION-362
summary: >-
  From the run of [CASE-187](../cases.d/CASE-187.md) for [LEAD-160](../leads.d/LEAD-160.md) ([CASE-384](../cases.d/CASE-384.md)). With goal success
  matched exactly, reading a transition table out of each agent gives
  equally accurate answers to next-state, distance, occupancy and
  post-intervention queries for all three, at every level of competence.
  Within each agent's own per-decision computation, the planner answers
  next states and distances, the value learner distances and the
  occupancy predictors occupancies; none answers the interventional
  families. This is [QUESTION-362](../questions.d/QUESTION-362.md)'s "recoverable is not available" as a
  measured result, and independent evidence for [CLAIM-514](CLAIM-514.md)'s family of
  query-relative capabilities. Toy scale, tabular, one budget choice. The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CASE-384 CLAIM-514 — new or Proposed; the study that grounds this claim and the thesis it corroborates -->

# CLAIM-991: Competence fixes readable, not answerable, queries

## The claim

[CASE-384](../cases.d/CASE-384.md) matched three architectures exactly on goal success.
It asked five query families of each:
- next state;
- shortest distance;
- random-walk occupancy;
- distance after a passage is blocked;
- occupancy after a passage is blocked.

Two results hold together.

- **Read-out answers are linked to competence.** Read a transition table
  out of each agent's internals, then compute the answer from it. Accuracy
  is then identical across the three, family by family, at every level of
  competence tested. All three are perfect at full coverage.
- **Within-budget answers come apart.** Restrict each agent to the
  computation it spends choosing one action. Each then answers a
  different family:
  - the planner answers next states and distances;
  - the value learner answers distances, from log-values;
  - the occupancy predictors answer occupancies, by averaging demons.

  Under the planner's larger budget, applied to all three, the value
  learner also answers next states and the predictors blocked
  occupancies. Read-out procedures cost 16,000 to a million operations
  against budgets of 4 and 256.

So "the agent can answer predictive queries" is not one capability, and
competence on the goals does not fix which of them an agent has. That is
[CLAIM-514](CLAIM-514.md)'s family of query-relative, resource-bounded capabilities
measured once. It is also [QUESTION-362](../questions.d/QUESTION-362.md)'s "what an investigator can
recover from an agent is not what the agent can recover from itself".

## What it does not say

- **That the read-out is not the agent's.** Whether a procedure belongs to
  the agent is a stipulation about what the organization includes. The
  claim reports both answers and does not settle it.
- **Anything beyond the class.** The setting is tabular and deterministic,
  with reach goals. In it a value table encodes the next state trivially.
  Richens et al.'s composite-goal extraction ([CLAIM-513](CLAIM-513.md)) is neither
  tested nor needed.
- **That the budgets are canonical.** Another budget moves the boundary.
  The claim is that some boundary separates families by architecture at
  matched competence.
