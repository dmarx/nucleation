---
number: 924
status: Proposed
formerly:
- THEORY-tmp0fsks
promote_when: >-
  A checked re-derivation recorded in this file, which the reading made
  (NOTE-1155) and which ADR-047 counts toward promotion. It is refuted
  by a win-probability matrix whose log-odds have nonzero curl on some
  triangle and are nonetheless exactly σ(r_i − r_j) for some ratings r, or
  by a batch Elo fixed point that does not match the observed row sums.
  The title is cardinal and says nothing about whether the wins cycle; an
  ordinal result neither promotes nor refutes it.
title: "Elo ratings are the row means of a win-probability matrix's log-odds; they reproduce the matrix exactly when the log-odds have no cyclic component, and adding a copy of one agent shifts the ratings of the others"
version: 1
tags:
- game-theory
- mathematics
date: '2026-10-24'
source:
- LIT-1508
summary: >-
  Balduzzi et al. (2018), [LIT-1508](../literature.d/LIT-1508.md), Propositions 1 and 3 and appendix
  A, read from arXiv v2 in [NOTE-1155](../notes.d/NOTE-1155.md), proofs followed. Elo is the
  uniform average of log-odds, and a fixed point matches only row sums.
  It is exact iff log-odds sum to zero around every triangle, so it has
  no predictive power in rock-paper-scissors, and duplicating an agent
  moves the ratings of agents that beat or lose to it. Cardinal
  throughout.
---
<!-- inactive-ok-file: CLAIM-451 — Proposed; named in prose, nothing here rests on it -->

# THEORY-924: Elo ratings are the row means of a win-probability matrix's log-odds; they reproduce the matrix exactly when the log-odds have no cyclic component, and adding a copy of one agent shifts the ratings of the others

## Source

Balduzzi, Tuyls, Pérolat & Graepel, [LIT-1508](../literature.d/LIT-1508.md), read in [NOTE-1155](../notes.d/NOTE-1155.md)
from arXiv:1806.02643v2: Proposition 1 (p. 3), Proposition 3 (p. 4) and
appendix A (p. 12), with the proofs on p. 13.

## What was actually shown

- **Proposition 1.** Batch Elo updates are stationary exactly when, for
  every agent, the predicted win probabilities against all others sum to
  the observed ones. Only the row sums are fitted.
- **Proposition 3.** If p_ij = σ(r_i − r_j) with Σr = 0, the row mean of
  logit P is r. An Elo rating generating P exists if and only if
  log(p_ij/p_ji) + log(p_jk/p_kj) + log(p_ki/p_ik) = 0 for all i, j, k. On
  the complete graph that is the Hodge statement that a curl-free flow is
  a gradient ([THEORY-894](THEORY-894.md)).
- **Copies** (appendix A). Rock-paper-scissors at win rate 0.9 gives
  every agent rating 0. Copying C moves A and B apart. The paper prints
  ±63; the batch fixed point at the stated α, recomputed by the reader, is
  ±71.9. Either way A falls because it loses to the duplicated agent, and B
  rises because it beats it.

The reader re-derived both propositions; each is a line of algebra.

## What this does not say

- **That Elo fails when wins cycle and succeeds when they do not.** The
  condition is on log-odds, cardinal. A record whose wins are acyclic can
  have curl and be misfit by Elo; the condition is not [TERM-077](../terms.d/TERM-077.md)'s ordinal
  one, and [CLAIM-434](../claims.d/CLAIM-434.md) holds the reason they come apart.
- **That a curl-free fit means the agents differ in one skill.** It means
  the log-odds are additive; nothing about mechanism.
- **That only copies distort Elo.** Any change to the evaluated population
  moves the row means. Copies are the clean case.

## Connections

Bears on [CLAIM-451](../claims.d/CLAIM-451.md) only negatively: in a fully cyclic record every
option gets the same Elo, so a scalar mean cannot tell cyclic tension from
indifference. The copy effect is the simplest form of a scoring layer that
can be moved without changing what is scored. That is the kind of route
that [CASE-124](../cases.d/CASE-124.md)'s μ arrow and [CASE-155](../cases.d/CASE-155.md)'s share-dependent scoring
formalize.
