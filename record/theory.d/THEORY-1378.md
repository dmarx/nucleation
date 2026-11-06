---
number: 1378
status: Active
formerly:
- THEORY-tmp6sg3n
title: 'Gerardi and Maestri show that when a firm can offer a privately informed worker only short-term contracts, then as both become patient the unique limiting outcome is a pooling contract with no learning if the prior that the worker is low-cost is below a threshold, and immediate firing of the high-cost worker if it is above, both inefficient'
version: 2
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Filed Proposed from NOTE-1599, which read the statements of
    Propositions 2–3, not the proofs.
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted by the twenty-ninth status review, at the status review's
    ruling (the owner delegated these rulings); ADR-065. NOTE-1599 v2 reads
    the main text in full, including the main-text proofs of Lemma 5 and
    Proposition 3. It also checks the supplement's proof of Lemma 3, the
    reason separation with employment fails. The title reports what the
    authors show. The old promote_when asked for a second source: "A
    second source, such as a survey of dynamic contracting or a later
    paper, states that in an infinite-horizon screening model with
    short-term contracts and irreversible quitting, the patient limit is
    pooling with no learning below a prior threshold and firing of the
    high-cost type above it." That is an independent test, moved to
    QUESTION-tmpgjiy3.
tags:
- game-theory
date: '2026-11-04'
source:
- LIT-2046
summary: >-
  Gerardi and Maestri (2020), [LIT-2046](../literature.d/LIT-2046.md), read in [NOTE-1599](../notes.d/NOTE-1599.md): the main text in
  full, and the supplement's proof of Lemma 3 checked. The appendices'
  proofs were not checked line by line. Read as a stand-in for Freixas,
  Guesnerie and Tirole (1985), whose own two-period result it does not
  restate. It holds in the limit as patience tends to one, with two types
  and irreversible quitting; with rehiring the conclusion fails.
---
<!-- inactive-ok-file: LIT-2062 — Unfetched; the unread original this reading stands in for, cited as open -->

# THEORY-1378: Gerardi and Maestri show that when a firm can offer a privately informed worker only short-term contracts, then as both become patient the unique limiting outcome is a pooling contract with no learning if the prior that the worker is low-cost is below a threshold, and immediate firing of the high-cost worker if it is above, both inefficient

## Source

Gerardi and Maestri (2020), [LIT-2046](../literature.d/LIT-2046.md); read in [NOTE-1599](../notes.d/NOTE-1599.md) (journal
pagination). Registered as a stand-in for Freixas, Guesnerie and Tirole
(1985), [LIT-2062](../literature.d/LIT-2062.md), unread.

## What was actually shown

- **The patient limit** (abstract, p. 583; Propositions 2–3): "If the prior
  probability of the worker being productive is low, the firm offers a
  pooling contract and no information is ever revealed. In contrast, if
  this prior probability is high, the firm fires the unproductive worker at
  the beginning of the relationship." "In both cases, the limiting
  equilibrium allocation is inefficient." (p. 584).
- **Why** (Lemma 3, p. 595): above a patience threshold, separation with
  both types employed is impossible, so "the firm can learn the worker’s
  cost only by firing the high type."
- Could have come out otherwise: with impatient parties the firm learns the
  type for any prior (p. 584), and with rehiring a folk theorem gives
  near-commitment payoffs (Proposition 4). The result is specific to
  patience and irreversible quitting. Lemma 3 was checked from the
  supplement: the two incentive constraints give
  θ ≥ θ(qL − qH) ≥ δθqH*/(1 − δ), impossible above δ̂ = 1/(1 + qH*). At the
  threshold prior itself the limit is not unique (fn. 15, p. 595).

## What this does not say

- Anything at moderate patience: the result is a limit as δ → 1.
- That it holds when the worker can be rehired; there it fails.
- Anything about more than two types, or about hidden actions (quality is
  verifiable).
- What Freixas, Guesnerie and Tirole showed: their two-period planner–firm
  result is not restated here.
- Anything about budgets, slack or capabilities kept for rare events; the
  setting is a labour relationship.
- That a second source confirms it: that is [QUESTION-tmpgjiy3](../questions.d/QUESTION-tmpgjiy3.md).
