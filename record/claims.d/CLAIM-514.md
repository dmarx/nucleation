---
number: 514
status: Proposed
formerly:
- CLAIM-tmp4mq28
title: 'World-modeling is a family of resource-bounded capabilities for producing and using predictions about an environment''s possibilities and consequences, each relative to a declared family of questions; a world model in the representational sense is one possible realization of them, competent behaviour can determine environmental structure without identifying any internal mechanism, and producing, maintaining and revising world-modeling capabilities are further achievements, not prerequisites of agency in general'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A result that competence across a stated family of goals requires,
  under the agent's actual resources, a particular internal realization of
  predictive capability, so that capability and mechanism cannot come
  apart in that class. Or a showing that the query-relative capabilities
  always come together, so that one score of world-model possession loses
  nothing.
tags:
- agency
- cognition
- philosophy-of-science
date: '2026-10-31'
line:
- distributed-agency
rests_on:
- CLAIM-519
- CLAIM-513
uses:
- TERM-086
bears_on:
- QUESTION-362
summary: >-
  The owner's preferred formulation at the second review of the filing of
  the exchange "Analyze nucleation concepts" (2026-10-31). It joins the
  world-model thesis, which holds that behaviour does not identify a
  mechanism, and its counter from Richens et al., which holds that
  behaviour across goals determines the dynamics. Both are kept, with each
  stated about a different notion of world model. It "integrates the
  Richens result rather than rejecting it, preserves [the] original
  critique of folk-model attributions, and connects both to the larger
  Nucleation program." Proposed: a definition and an organizing thesis,
  with the study [CASE-187](../cases.d/CASE-187.md) as its test.
---
<!-- inactive-ok-file: CLAIM-519 QUESTION-362 TERM-086 — Proposed or Open; the premises and question this joins, cited as open -->

# CLAIM-514: World-modeling is a family of resource-bounded capabilities for producing and using predictions about an environment's possibilities and consequences, each relative to a declared family of questions; a world model in the representational sense is one possible realization of them, competent behaviour can determine environmental structure without identifying any internal mechanism, and producing, maintaining and revising world-modeling capabilities are further achievements, not prerequisites of agency in general

## The claim

**World-modeling competence.** Let 𝒬 be a declared family of questions
about environmental dynamics. Let q ∈ 𝒬 have correct answer P_q, and let L
be a proper predictive loss. An organization O has world-modeling
competence WM_{B,T,ε}(O; 𝒬) when there is a single procedure κ,
implementable by O, such that

  sup_{q ∈ 𝒬} E[L(κ(q), P_q)] ≤ ε,

with κ operating within budget B and deadline T.

The single-procedure condition matters. An outside oracle must not be
allowed to pick a different best answerer for each query.

The families are not interchangeable:
- observational predictions need not identify responses to intervention;
- interventional distributions need not fix counterfactuals at the level
  of the individual case.

Nothing in the definition requires an explicit generative model. A neural
predictor, predictive-state statistics, a database, a simulator or a
distributed system of specialized processes could each meet it. And like
the record's other capabilities, it need not grow monotonically. A
controller can get better at short-horizon action-conditioned prediction
while it gets worse at long-horizon forecasting. So the object is a
family of query-relative capabilities, not one score of world-model
possession.

**Where the two claims it rests on sit.**
- [CLAIM-513](CLAIM-513.md) is about the behaviourally encoded model: the policy
  determines the dynamics, recoverable by an external algorithm.
- [CLAIM-519](CLAIM-519.md) is about the realized mechanism: behaviour does not
  identify it.

They do not conflict once each is read as being about its own notion.
Recoverability from a policy does not imply that the agent can produce
the model on demand, simulate with it, or update it when wrong.

## What it does not say

- **That an explicit world model marks superior agency.** Its worth
  depends on the queries it serves, what it costs and the further inquiry
  it opens.
- **That the Richens result is an observer's fiction.** The recovered model
  is constrained by the behaviour. It is not arbitrary.
- **That competence is no evidence of a model.** It does not establish one.
  Under resource assumptions it can still favour one ([CLAIM-519](CLAIM-519.md)).
