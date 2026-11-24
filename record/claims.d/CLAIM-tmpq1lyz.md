---
status: Proposed
title: 'In the seeded fold model, a transient seed leaves a maintained organization only inside the bistable window and only by carrying the state past the unstable threshold, a brief seed needing exactly that threshold and a slower one more; the meme enters only as a scalar forcing, so the model expresses the environment''s receptivity but not which organization a seed nucleates'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation or the check below, for the model
  ḃ = μb + κb² − b³ + αm(t) with b ≥ 0 and κ > 0 as A4 §3 states it. Not
  defeated by a richer model: the claim is about A4's.
tags:
- mathematics
- cultural-evolution
- complex-systems
date: '2026-11-24'
line:
- transient-support
- formal-apparatus
rests_on:
- CLAIM-463
grounds:
- CASE-111
complements:
- CLAIM-tmpgvsgg
bears_on:
- QUESTION-tmprvnp0
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A4 §3 of the exchange "Memes, Contracts, and
  Systemic Normativity" (ChatGPT, 2026-11-24), which adds a meme to
  [CASE-111](../cases.d/CASE-111.md)'s fold, ḃ = μb + κb² − b³ + αm(t), and says "In the bistable
  regime, the meme need only push the system past an unstable threshold"
  and that the model "produces a fundamentally different account of
  memetic effectiveness". The window, the threshold and how it grows with
  the seed's duration are derived and checked by script (python3 -I); the
  model's one-dimensional forcing is what limits what it can show. The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmp4uj40 — Proposed, Deferred or Rejected; entries filed from the exchange 'Memes, Contracts, and Systemic Normativity' and held entries it is read against, cited whatever their standing -->

# CLAIM-tmpq1lyz: In the seeded fold model, a transient seed leaves a maintained organization only inside the bistable window and only by carrying the state past the unstable threshold, a brief seed needing exactly that threshold and a slower one more; the meme enters only as a scalar forcing, so the model expresses the environment's receptivity but not which organization a seed nucleates

## The gap

A4 §3 takes [CASE-111](../cases.d/CASE-111.md)'s boundary-maintenance fold and adds "a transient
memetic intervention", ḃ = μb + κb² − b³ + αm(t), where b is "the
intensity of organizational activity", μ "prevailing environmental
conditions", κ "endogenous reinforcement", m(t) "exposure to the meme"
and α "the receptivity of the organization". It says the meme "need only
push the system past an unstable threshold", and draws three
consequences: "The same meme, introduced into different environments, may
have radically different consequences. Conversely, different memes can
nucleate the same organizational regime. Neither informational fidelity
nor replication rate is sufficient to characterize this behavior." It
states no window, no threshold and no dependence on how the seed is
delivered.

## The derivation

With m = 0, the equilibria other than b = 0 solve b² − κb − μ = 0:

  b± = (κ ± √(κ² + 4μ)) / 2.

- **The window.** Both are real and positive exactly when
  −κ²/4 < μ < 0 ([CASE-111](../cases.d/CASE-111.md)'s bistable range). Then b = 0 and b₊ are stable
  and b₋ is the unstable threshold between them. For μ ≥ 0, b = 0 is
  unstable and any positive activity grows to b₊: no seed is needed, as
  past a spinodal. For μ < −κ²/4 there is no maintained state and no seed
  makes one.
- **A brief seed.** An impulse of total size I = α∫m dt moves b from 0 to
  I at once; afterwards the system flows to b₊ exactly when I > b₋(μ).
- **A slower seed.** During a pulse of finite length, the activity built
  up decays back toward 0 while b < b₋, so more total exposure is needed.
- **Receptivity.** b₋ rises from 0 as μ → 0⁻ to κ/2 as μ → −κ²/4. Near the
  upper edge a vanishing seed suffices; near the lower edge the seed must
  be large and the maintained state b₊ it reaches is close to the
  threshold, so the organization nucleated there is fragile.

## The check

By script (python3 -I), κ = 2, b(0) = 0, square pulses of amplitude A and
length T, Euler steps of 0.002 to t = 300, the critical A·T by bisection:

| μ | b₋ | b₊ | A·T at T = 0.01 | T = 0.5 | T = 2 |
|---|---|---|---|---|---|
| −0.05 | 0.0253 | 1.9747 | 0.0253 | 0.0254 | 0.0257 |
| −0.25 | 0.1340 | 1.8660 | 0.1340 | 0.1367 | 0.1449 |
| −0.50 | 0.2929 | 1.7071 | 0.2931 | 0.3041 | 0.3388 |
| −0.75 | 0.5000 | 1.5000 | 0.5005 | 0.5263 | 0.6084 |
| −0.95 | 0.7764 | 1.2236 | 0.7772 | 0.8189 | 0.9524 |

At μ = +0.1 a start of 0.001 grows to b₊ = 2.0488 unaided; at μ = −1.1 a
start of 1.5 decays to 0. A4's "laboratory" fixes κ = 2 and lets μ run
from −0.99 to −0.01, inside the window, so it shows neither edge.

## What follows for A4

- **Receptivity is expressed.** "The same meme, introduced into different
  environments, may have radically different consequences" holds in the
  model, through b₋(μ).
- **Specificity is not.** The meme enters only through the scalar αm(t),
  and the model has one maintained state. Two memes with the same αm(t)
  are the same input, and every successful seed reaches the same b₊. So
  "different memes can nucleate the same organizational regime" is built
  in, and the converse, that different seeds nucleate different regimes,
  which A4 §8 tests as "Nucleation specificity", cannot be expressed.
- **Transmission is absent.** The model has no copying, so it can neither
  show nor refute that "informational fidelity" or "replication rate" is
  insufficient. That is [CLAIM-tmp4uj40](CLAIM-tmp4uj40.md)'s question, for data.

The model is [CLAIM-463](CLAIM-463.md)'s hysteresis with a pulse; what it adds is the
threshold for a transient seed, and the lesson is that a test of
nucleation specificity needs more than one maintained regime and a seed
with more than one dimension ([LEAD-tmpiktom](../leads.d/LEAD-tmpiktom.md)).
