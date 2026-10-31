---
number: 187
status: Active
formerly:
- CASE-tmp1a9u5
title: 'A proposed study: agents matched on competence over a declared family of goals, one planning with an explicit transition model, one a directly learned goal-conditioned policy, one a distributed predictive-state controller, compared on the original goals, on on-demand predictive and interventional queries, under targeted internal interventions, and after environmental change and damage to their predictive machinery, to find which world-modeling achievements are linked and which come apart under matched resources'
version: 1
standing: stipulated
kind: proposed-study
tags:
- agency
- cognition
- representation-learning
date: '2026-10-31'
line: distributed-agency
illustrates:
- CLAIM-514
- CLAIM-519
- CLAIM-513
summary: >-
  Proposed by the owner at the second review of the filing of the
  exchange "Analyze nucleation concepts" (2026-10-31), as the experiment
  that would sharpen the world-model distinction. Not run; its
  architectures, tasks and margins are left to a preregistration.
---
<!-- inactive-ok-file: CLAIM-514 CLAIM-519 QUESTION-362 — Proposed or Open; the claims it would test and the question it serves, cited as open -->

# CASE-187: A proposed study: agents matched on competence over a declared family of goals, one planning with an explicit transition model, one a directly learned goal-conditioned policy, one a distributed predictive-state controller, compared on the original goals, on on-demand predictive and interventional queries, under targeted internal interventions, and after environmental change and damage to their predictive machinery, to find which world-modeling achievements are linked and which come apart under matched resources

## The design

There are three architectures, matched on competence over a declared goal
family:
- an explicit transition model with planning;
- a goal-conditioned policy learned directly;
- a distributed predictive-state controller.

Each is tested four ways, independently specified:

| test | what it isolates |
|---|---|
| the original goal family | ordinary behavioural competence |
| on-demand predictive and interventional queries | operational world-modeling competence, in [CLAIM-514](../claims.d/CLAIM-514.md)'s sense |
| targeted interventions on internals | the realized mechanism |
| environmental change, and damage to the predictive machinery | modeling corrigibility and reconstruction |

**Matching.** Comparisons must account for memory, computation and
training history. A lookup-table controller can be far more expensive than
a compact learned model, so equal competence at unequal cost is itself a
result to report, not a confound to hide.

## What it would show

The point is not which architecture does best. It is which achievements
are linked and which come apart, under matched conditions.
- If competence on the goals predicts query competence across all three
  architectures, the two are linked in this class.
- If one architecture answers queries no better than chance while matching
  the others on goals, they come apart.
- If targeted interventions separate architectures that the first two
  tests do not, mechanism is underdetermined by capability, as
  [CLAIM-519](../claims.d/CLAIM-519.md) holds.
- Recovery after damage to the predictive machinery tests the
  maintenance-and-revision row of [QUESTION-362](../questions.d/QUESTION-362.md).

Ordinary competence identifies less than targeted interventions on the
machinery that sustains it ([CLAIM-414](../claims.d/CLAIM-414.md), [CASE-161](CASE-161.md)).

**Not tested.** The design does not test Richens et al.'s theorem, which
is about full goal-conditioned policies in fully observed environments.
It asks what that theorem leaves open.
