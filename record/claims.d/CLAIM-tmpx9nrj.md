---
status: Proposed
title: 'Possibility and realization are separate dimensions of a regulatory regime: its compatibility complex says which sets of public demands some attainable history meets, the probability of meeting them under a model of participants'' behaviour says how reliably the regime selects such a history, and a regime can improve either without the other'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A showing that every change of regime which raises the probability of
  meeting the demands also enlarges the compatibility complex, or that
  every enlargement raises that probability, so that the two never come
  apart; or that the probability of realization is not well defined
  without collapsing into the complex, for example because participants'
  behaviour cannot be modelled apart from the regime's attainable set.
tags:
- society-and-governance
- probabilistic-modeling
- operations-research
date: '2026-11-22'
line:
- realizability
- distributed-agency
rests_on:
- CLAIM-347
complements:
- CLAIM-357
- CLAIM-tmpk4bou
summary: >-
  A33 §8 of the exchange "Explain First Contact RL" (ChatGPT,
  2026-11-22): C(g; D) "concerns the structure of possibility", and
  P_D(g) = μ_g(⋂_{j∈D} V_j) "concerns the realization of those
  possibilities under a specified model". "A regulator may improve
  realized outcomes without expanding the compatibility complex", and "a
  technology-enabling regulation may expand the compatibility complex
  without causing firms to adopt the newly available solutions."
  [CLAIM-357](CLAIM-357.md) holds the deterministic half, structural infeasibility
  against realized violation; this adds a distribution over histories
  induced by participants' responses. The wording is A's (ChatGPT, in
  the exchange of 2026-11-22); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmphjm0q — Proposed; filed in this filing of 2026-11-22 -->

# Possibility and realization are separate dimensions of a regulatory regime: its compatibility complex says which sets of public demands some attainable history meets, the probability of meeting them under a model of participants' behaviour says how reliably the regime selects such a history, and a regime can improve either without the other

## The claim

Let μ_g be the distribution over industrial histories that regime g
induces under a model of participants' behaviour and disturbances, and
P_D(g) = μ_g(⋂_{j∈D} V_j). Then C(g; D), the compatibility complex
([CLAIM-347](CLAIM-347.md)), and P_D(g) measure different things.

**Construction.** Two attainable histories, h₁ meeting every demand and
h₂ meeting none. If participants choose h₂, D is a face of the complex
and P_D = 0. An incentive that moves their choice to h₁ leaves the
admissible set, and so the complex, unchanged, and makes P_D = 1:
realization improved without possibility. Conversely, a regime that
makes a new history h₃ attainable, meeting a set of demands that no
earlier history met, enlarges the complex. If no participant adopts h₃,
P_D is unchanged: possibility improved without realization.

[CLAIM-357](CLAIM-357.md) separates structural infeasibility from realized violation for
one actual update. This separates the attainable set from a distribution
over it, which is where strategic response enters (A31 §2: "It is not
enough for a desirable outcome to be possible").

## Use

A33 §8 joins the two to resilience R(g), accountability and revisability
A(g), and cost into a profile, Q(g) = (C(g; D), P_D(g), R(g), A(g),
−C(g)), "intentionally not a scalar objective". [CLAIM-tmphjm0q](CLAIM-tmphjm0q.md) holds the
objection that follows for "optimally".

## What it does not say

It does not say P_D(g) is known. It is relative to a behavioural model
(A31 §6: the formulation "assumes we can meaningfully estimate the
relevant costs, outcome probabilities, and fragility risks").
