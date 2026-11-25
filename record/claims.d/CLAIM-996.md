---
number: 996
status: Proposed
formerly:
- CLAIM-tmp04pr7
title: 'Permission to inquire is a second-order query'
statement: >-
  Permission to pursue an inquiry is a second-order query, formulated by the
  proponent and evaluated by the authority within their own budgets, so the
  questions an organization authorizes are a subset of those its members can
  ask, and an authorization can take so long that the opportunity it
  authorizes has closed, whatever the verdict
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Authorization processes whose formulation and evaluation draw on no budget
  or deadline shared with the inquiry they authorize, so that their duration
  never bears on whether the authorized inquiry can still be carried out; or a
  showing that, wherever prior authorization is required, the authorized
  questions coincide with the askable ones.
tags:
- society-and-governance
- operations-research
- epistemology
date: '2026-11-23'
line:
- distributed-agency
- learning-and-inquiry
rests_on:
- CLAIM-475
complements:
- CLAIM-732
- CLAIM-523
uses:
- TERM-064
- TERM-092
summary: >-
  A56 §§2–3 of the exchange "Explain First Contact RL" (ChatGPT, 2026-11-23), developing the owner's U29
  ([CLAIM-1065](CLAIM-1065.md)): "Asking permission is itself a resource-bounded inquiry,
  directed at an authority whose capacity to understand and evaluate the
  request is also resource-bounded." It defines an authorization frontier
  inside the askable questions, an authorization cost (infinite where no
  procedure exists), and a deadline on permission, investigation and
  realization together. [CLAIM-732](CLAIM-732.md) is the nearest antecedent, for objections;
  [CLAIM-1016](CLAIM-1016.md) (the assistant's) says what the frontier assumes about the
  unit of authorization. The wording is A's (ChatGPT's, at A56 of the exchange "Explain First Contact RL"); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-1065 CLAIM-732 CLAIM-1016 CASE-386 — Proposed; the owner's thesis this develops, the antecedent, the gap fill and A58's joint relation -->

# CLAIM-996: Permission to inquire is a second-order query

## The claim

A56 §2. An employee with a proposal q must first answer the manager's
implicit question, whether it is credible, valuable and appropriate enough
to authorize. The organization is then allocating resources to "decide which
questions are permitted to become actionable inquiries". The chain is
formulation by the employee (m_q = e(q)), evaluation by the manager
(j = d(m_q)), authorization, then investigation, with each step bounded:
C_e(e, q) ≤ B_e and C_m(d, m_q) ≤ B_m. "Legibility is relational": the same
proposal can be cheap to evaluate in a specialist community and costly to
justify up a hierarchy ([TERM-064](../terms.d/TERM-064.md)).

A56 §3. Let Q^ask(S) be the questions a perspective can formulate
([TERM-092](../terms.d/TERM-092.md)'s askable set) and Q^auth(S) those it can obtain permission to
investigate adequately under the institution's arrangement G. Where prior
authorization is required, Q^auth(S) ⊆ Q^ask(S), and the gap is a class of
"organizationally suppressed possibilities", "though exclusion is not
automatically unjustified". The authorization cost is

  C_perm(q; S, G) = inf over σ ∈ Σ_G(q) of C(σ),

the cheapest procedure by which a proponent can formulate, communicate,
justify and obtain authorization for q, set to +∞ where none exists. For a
sequential workflow,

  T_perm(q; S, G) + T_investigate(q) + T_realize(q) ≤ H_q,

and with overlapping activities the dependency schedule replaces the sum, as
A56 says. Hence: "Permission to pursue a possibility can be so expensive that
exercising the permission, once obtained, is no longer feasible." "And this
is not a question of whether the manager eventually says yes."

The deadline step is a construction: given the sum and the horizon, a long
enough authorization closes the window whatever its verdict. The rest is
interpretive, a reading of organizations in these terms.

A54 §1's worked case, an opportunity open for ten days lost under a
workflow of formulating, justifying, approving and implementing, is
[CASE-386](../cases.d/CASE-386.md).

## What it does not say

That authorization is wasteful, or that the excluded questions deserved
pursuit. A56 marks both: exclusion "is not automatically unjustified".

## Neighbours

[CLAIM-732](CLAIM-732.md)'s six stages of an effective objection include legibility and
uptake by an authorized channel; this is the same structure for a request to
inquire, with the authorization's duration counted against the inquiry's own
deadline. [CLAIM-523](CLAIM-523.md) keeps legibility, efficacy and correctability apart; A56's
closing synthesis: "making an idea legible is not the same as granting it authority, and
granting it authority is not the same as enabling its realization", which is
[CLAIM-523](CLAIM-523.md)'s and [CLAIM-403](CLAIM-403.md)'s point and is not filed again.

## A gap, filled

The inclusion and the cost are stated per question: authorization is granted
to a formulated proposal, between formulating and investigating. A56's own
remedies, an exploratory budget and staged approval, grant authority before
any particular question is formulated. [CLAIM-1016](CLAIM-1016.md) (the assistant's)
works out what follows. A58 adds that authorization belongs to the joint
inquiry relation itself ([CLAIM-1190](CLAIM-1190.md)).

## Standing

Proposed, in A's voice.
