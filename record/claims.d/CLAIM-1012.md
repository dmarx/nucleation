---
number: 1012
status: Proposed
formerly:
- CLAIM-tmp2oloi
title: 'Hardest queries are not good governance'
statement: >-
  Practical questions put to an organization can be modelled as queries met
  by realizations, and their relation as a robust interrogation game in
  which a respondent chooses a response policy against the strongest
  permitted queries; the game has diagnostic, adversarial and developmental
  forms that are not interchangeable, so maximizing the difficulty of
  queries is not good governance and the query side needs justified
  constraints
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that the three forms are interchangeable, so that a query policy
  good for one is good for the others; or that a query side choosing the
  hardest permitted queries reveals as much about the capacities worth
  maintaining as one choosing under justified constraints. That the minimax
  formula is strategic only under conditions (CLAIM-1032) narrows its
  formal part and does not defeat it.
tags:
- society-and-governance
- game-theory
- operations-research
date: '2026-11-23'
line:
- readiness
- learning-and-inquiry
rests_on:
- CLAIM-470
uses:
- TERM-115
- TERM-095
bears_on:
- QUESTION-524
summary: >-
  A50 §§1 and 3 of the exchange "Explain First Contact RL" (ChatGPT,
  2026-11-23), developing the owner's U26 ([CLAIM-1031](CLAIM-1031.md)). A query is a
  practical question addressed to an organization, an answer "a history
  that demonstrates the required capability"; the score R_S(q; H, B) is
  [TERM-115](../terms.d/TERM-115.md)'s readiness indexed by query and budget. A50 calls the minimax
  over response policies and query distributions "a robust interrogation
  game" and names three forms of it. [CLAIM-1032](CLAIM-1032.md) and [ARG-230](../arguments.d/ARG-230.md) say
  when the formula is a game. The wording is A's (ChatGPT, at A50 of the
  exchange "Explain First Contact RL"); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-1031 CLAIM-1032 ARG-230 — Proposed; the thesis this develops and the assistant's analysis of its formula, filed with it -->

# CLAIM-1012: Hardest queries are not good governance

## The claim

A50 §1 carries [CLAIM-470](CLAIM-470.md) from questions about the world to "practical
questions addressed to an organization", such as "Can this industrial
ecosystem replace a failed supplier within three days?" An answer "is no
longer merely a verbal proposition. It is a successful realization: a
history that demonstrates the required capability." With an acceptance
relation M(q, y) between queries and responses, the operational score is

R_S(q; H, B) = Pr under π_S(an acceptable answer to q is realized by H
within budget B),

"a demand-relative extension" of [TERM-115](../terms.d/TERM-115.md), evaluated "under the
organization's actual response policy, not merely under an ideal policy it
could theoretically implement" ([TERM-115](../terms.d/TERM-115.md) already says so).

A50 §3 makes it a game. The query side "chooses what to test, when, and
with what evidentiary standards"; the target side responds. With a loss
ℓ(q, a) for failing to answer adequately, the game is

inf over π ∈ Π(S) of sup over ρ ∈ 𝒫(Q) of E[ℓ(q, a)], q ~ ρ, a ~ P_π(· | q, S),

"a robust interrogation game: the respondent seeks a policy that performs
acceptably against the strongest permitted tests."

## Three forms

"But the adversarial formulation is only one instance":

| Game | Query-side objective | Target-side response |
|---|---|---|
| Diagnostic | Reveal actual capabilities and limitations | Produce observable behavior |
| Adversarial | Find failures, vulnerabilities, or inconsistencies | Resist, conceal, or correct them |
| Developmental | Generate informative challenges that extend capabilities | Learn new ways of answering |

"These are not interchangeable. In particular, maximizing the difficulty of
questions is not necessarily good governance. An interrogator that only
produces impossible, irrelevant, or illegitimate demands may reveal little
about the capacities worth maintaining. The query side itself needs
justified constraints."

## What it does not say

It gives a payoff only to the adversarial form, through ℓ; the diagnostic
and developmental forms' query-side objectives are named in the table, not
formalized ([QUESTION-524](../questions.d/QUESTION-524.md)). The assistant's analysis ([CLAIM-1032](CLAIM-1032.md),
argued in [ARG-230](../arguments.d/ARG-230.md)) shows that against any fixed policy the formula's
worst query distribution is a single query, so that the query side's mixing
does work only when one policy must serve several queries or the permitted
distributions are restricted; a restriction is where the "justified
constraints" on the query side enter the formula.

## Standing

Proposed, in A's voice.
