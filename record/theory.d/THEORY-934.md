---
number: 934
status: Proposed
formerly:
- THEORY-tmpbq2nj
promote_when: >-
  A proof of the continuous-time limit for negative payoffs, which the
  authors state and omit (the regularity conditions of Norman's theorem
  fail at the boundary), checked in the journal version or supplied
  elsewhere; and the decomposition reproduced from the update rule by an
  independent derivation. It is refuted if the limit of the
  proportional-updating process differs from the stated equation in the
  interior of the simplex. Whether people probability-match is a separate
  question, and experimental results about it neither promote nor refute
  this.
title: 'Under Bush–Mosteller learning with negative payoffs, the continuous-time limit is a replicator term in benefits plus a probability-matching term, which alone drives choice probabilities to success probabilities'
version: 1
tags:
- game-theory
- learning-and-conditioning
date: '2026-10-24'
source:
- LIT-1505
summary: >-
  Börgers & Sarin (JET 1997; working paper 1993), [LIT-1505](../literature.d/LIT-1505.md), read in
  full in [NOTE-1149](../notes.d/NOTE-1149.md). When reinforcements may be negative, probability
  removed from a punished strategy is redistributed, and the limit is
  dp_j/dt = p_j(Ū_j* − p|Ũ|q) + Ū_j*(σ_j* − p_j). With payoffs of equal
  absolute size only the matching term remains. The limit is stated with
  its proof omitted.
---
<!-- inactive-ok-file: THEORY-938 — Proposed or new; the source and its sibling, named -->

# THEORY-934: Under Bush–Mosteller learning with negative payoffs, the continuous-time limit is a replicator term in benefits plus a probability-matching term, which alone drives choice probabilities to success probabilities

## Source

Börgers and Sarin, [LIT-1505](../literature.d/LIT-1505.md), Section 6 (pp. 19–25 of the 1995 working
paper), read in full in [NOTE-1149](../notes.d/NOTE-1149.md).

## What was actually shown

- **The rule.** A negative payoff takes probability |Ũ|p_j from the strategy
  played and gives it to the others, in proportion to their probabilities
  or to one chosen at random in that proportion. The two have the same
  expected motion.
- **The limit.** In terms of "benefits", events that raise j's probability,
  dp_j/dt = p_j(Ū_j* − p|Ũ|q) + Ū_j*(σ_j* − p_j), where σ_j* is the
  probability that j is reinforced and Ū_j* the expected size of its
  benefit. The first term is a replicator term in benefits, the second the
  "probability matching force". The proof is omitted; the authors say
  they "believe" Norman's conclusion extends because the irregularities
  lie only on the boundary (p. 20).
- **Cases.** All payoffs positive: σ_j* = p_j and the matching term
  vanishes, giving the replicator equation. All payoffs of one absolute
  size: the replicator term vanishes. In a one-player problem the choice
  probability goes to the probability μ of the state in which it pays
  (Example 2); in a ±0.5 matching pennies the mixed equilibrium is globally
  stable, which the authors call accidental (p. 25).
- **Aspirations.** With an aspiration level that tracks experienced payoff,
  some experiences fall below it, so the matching term is "in most cases
  unavoidable" (p. 26). That is reported from a companion paper.

## What this does not say

- That the process maximizes anything: its limit points are generally not
  Nash equilibria (p. 25).
- That human choice probability-matches for this reason. The authors cite
  the psychology only as a known association.

## Connections

The record's common-currency line asks when a negotiation's choices
follow an ordering of its options. This is a mechanism by which a
reinforcement learner settles at mixed choice where one option is
strictly better on expectation: a departure from maximizing produced by the
update rule, not by any failure of the options to be ordered.
