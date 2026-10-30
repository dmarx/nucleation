---
number: 924
status: Active
formerly:
- THEORY-tmp0fsks
title: "When Elo ratings generate a win-probability matrix they are the row means of its log-odds; some set of Elo ratings reproduces a win-probability matrix exactly when its log-odds have no cyclic component, batch Elo otherwise matches only the row sums, and adding a copy of one agent shifts the batch Elo ratings of the others"
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings), under ADR-065 §5. Narrowed under ADR-047's "Where a
    narrowing's dropped claims go". A second checker followed Propositions
    1 and 3 and the copy example step by step and re-ran them by script
    with controls (status review 22); the algebra the body called "a line
    of algebra" is now written out in the note of 2026-10-30. The first
    clause of the title was narrowed: read unconditionally it is false,
    since batch Elo's fixed point differs from the row means of the
    log-odds whenever they have curl (in the copy example ±71.9 against
    ±95.4 Elo points). It is routed as kind 3, a clause shown false, in
    the note of 2026-10-30. The old title: "Elo ratings are the row means
    of a win-probability matrix's log-odds; they reproduce the matrix
    exactly when the log-odds have no cyclic component, and adding a copy
    of one agent shifts the ratings of the others". The old promote_when:
    A checked re-derivation recorded in this file, which the reading made
    (NOTE-1155) and which ADR-047 counts toward promotion. It is refuted
    by a win-probability matrix whose log-odds have nonzero curl on some
    triangle and are nonetheless exactly σ(r_i − r_j) for some ratings r,
    or by a batch Elo fixed point that does not match the observed row
    sums. The title is cardinal and says nothing about whether the wins
    cycle; an ordinal result neither promotes nor refutes it.
tags:
- game-theory
- mathematics
date: '2026-10-24'
source:
- LIT-1508
summary: >-
  Balduzzi et al. (2018), [LIT-1508](../literature.d/LIT-1508.md), Propositions 1 and 3 and appendix
  A, read from arXiv v2 in [NOTE-1155](../notes.d/NOTE-1155.md), proofs followed. When the
  log-odds are curl-free, Elo ratings are their row means; otherwise
  batch Elo's fixed point matches only row sums and differs from the
  row means. Elo fits exactly iff log-odds sum to zero around every
  triangle, so it has
  no predictive power in rock-paper-scissors, and duplicating an agent
  moves the ratings of agents that beat or lose to it. Cardinal
  throughout.
---
<!-- inactive-ok-file: CLAIM-451 — Proposed; named in prose, nothing here rests on it -->

# THEORY-924: When Elo ratings generate a win-probability matrix they are the row means of its log-odds; some set of Elo ratings reproduces a win-probability matrix exactly when its log-odds have no cyclic component, batch Elo otherwise matches only the row sums, and adding a copy of one agent shifts the batch Elo ratings of the others

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
  rises because it beats it. The row means of the log-odds here are ±95.4:
  with curl, the batch fixed point is not the row mean.

The reader re-derived both propositions. The steps are written out in the
note of 2026-10-30 below.

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

## Note of 2026-10-30: the re-derivation, written out

The second check at the status review (ADR-065 §5) followed each step.

1. Proposition 1. Batch Elo updates r_i ← r_i + η Σ_j (p_ij − σ(r_i −
r_j)), with p_ij the observed win rate. It is stationary exactly when Σ_j
σ(r_i − r_j) = Σ_j p_ij for every i, so only the row sums are fitted.

2. Proposition 3, forward. If p_ij = σ(r_i − r_j), then logit p_ij = r_i −
r_j, and (1/n) Σ_j logit p_ij = r_i − (1/n) Σ_j r_j = r_i when Σ r = 0.
The term j = i is logit ½ = 0 = r_i − r_i.

3. Proposition 3, converse. Write A_ij = log(p_ij / p_ji). It is
antisymmetric, and it is logit p_ij, since p_ij + p_ji = 1. If A_ij +
A_jk + A_ki = 0 for all i, j, k, then A_ij = A_ik + A_kj. Put r_i = (1/n)
Σ_k A_ik. Then r_i − r_j = (1/n) Σ_k (A_ik − A_jk) = (1/n) Σ_k (A_ik +
A_kj) = A_ij, so p_ij = σ(r_i − r_j). If some triangle sum is nonzero, no
ratings r have A_ij = r_i − r_j, since any such A sums to zero round
every triangle.

4. When the log-odds are curl-free, batch Elo reaches the row means. Those
ratings reproduce P, so they match its row sums, and the row-sum equations
are the Bradley–Terry likelihood equations, whose solution is unique up to
a shift.

5. Copies. Take rock-paper-scissors at 0.9, with A beating B, B beating C
and C beating A: every rating is 0. Add C′, a copy of C. By symmetry r_C =
r_C′ = 0 and r_A = −r_B = −x. B's observed row sum is 0.1 + 0.9 + 0.9 =
1.9, so the fixed point needs σ(2x) + 2σ(x) = 1.9, which gives x = 0.4140
in natural units, or 71.91 Elo points at 400/ln 10 points per unit. A
falls because it loses to the copied agent, and B rises because it beats
it. The row means of the log-odds are instead ±(ln 9)/4 = ±0.549, or
±95.42 Elo points.

A script (numpy, in the session's scratchpad) checked these steps. In five
random curl-free matrices of 3 to 7 agents, the row means of the log-odds
equalled the generating ratings and batch Elo converged to them. In five
random matrices with curl, batch Elo matched the row sums to 10⁻¹³, but
neither it nor the row means reproduced P (largest misfits 0.02 to 0.46),
and the two differed by up to 0.64. As a control, removing the cyclic part
of the same matrices made the row means fit exactly. The copy example's
fixed point came out at ±71.91 both by iterating the update and by
bisection on the equation in step 5.

## Note of 2026-10-30: the clause the narrowing drops

The title said, without condition, that Elo ratings are the row means of a
win-probability matrix's log-odds. That is the paper's gloss, "Elo is,
essentially, a uniform average in logit space" (p. 4), and Proposition 3
proves it only when the matrix is generated by ratings. With curl, batch
Elo's fixed point is not the row mean: in the copy example the row means
are ±95.4 Elo points and the fixed point ±71.9. Read unconditionally, the
clause is shown false, so it is recorded here only (ADR-047's kind 3), and
the title now states the condition.
