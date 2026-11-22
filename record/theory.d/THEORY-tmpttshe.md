---
status: Proposed
promote_when: >-
  A reading of a primary source in the regret-rate line (for instance
  Cassel, Cohen & Koren 2020 or Jedra & Proutiere 2022) that establishes,
  from its proof, the identifiability dichotomy the title asserts: that
  general linear-quadratic control needs regret growing like √T, achieved
  when exploration is driven away from the optimal policy, exactly because
  the optimal (certainty-equivalent) policy makes essential parameters
  non-identifiable in closed loop, whereas problems whose
  non-identifiable parameters are unimportant admit log T. The review's
  statement of this does not suffice.
title: 'Optimal control of a system with unknown dynamics must probe it to learn, trading immediate performance for information, by acting on an extended state that adjoins an information state to the physical one; whether exploration must drive the system away from the optimal policy is set by closed-loop identifiability'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed Proposed from NOTE-tmpk22nd, the review's organizing account of
    dual control. The three clauses are the review's synthesis of
    established results (Feldbaum; Åström & Wittenmark; Lai & Wei; Cassel
    et al.; Jedra & Proutiere; Rantzer), not a new theorem; promote_when
    asks a primary source to carry the identifiability clause, which is
    the load-bearing one.
tags:
- control-theory
- mathematics
- learning-theory
date: '2026-11-22'
source:
- LIT-tmpbta8p
bears_on:
- QUESTION-374
---
<!-- inactive-ok-file: THEORY-tmpttshe — this account, filed Proposed in this batch (LEAD-145) -->

# THEORY-tmpttshe: Optimal control of a system with unknown dynamics must probe it to learn, trading immediate performance for information, by acting on an extended state that adjoins an information state to the physical one; whether exploration must drive the system away from the optimal policy is set by closed-loop identifiability

## Source

Meijer and Rantzer (2026), [LIT-tmpbta8p](../literature.d/LIT-tmpbta8p.md), read in
[NOTE-tmpk22nd](../notes.d/NOTE-tmpk22nd.md).

## The account

Dual control (Feldbaum, 1960) is the double task of a feedback controller
for a plant whose parameters are unknown: regulate it and, at the same
time, probe it, because "Without probing, you will not learn how the
system responds" and probing trades short-term performance for better
estimates. The review's organizing account has three parts.

1. **Probing is necessary; the controller acts on an extended state.** The
   optimal policy cannot be a function of the physical state alone; it
   depends on the accumulated history, compressed into an *information
   state* that, with the physical state, makes the optimal dual policy a
   function of a fixed-dimension extended state. Feldbaum posed this in
   Bellman's dynamic programming; the minimax line realizes it explicitly
   as the pair (x(t), Z(t)).

2. **The tradeoff is the value of information against immediate cost.**
   "Optimal controllers must balance immediate performance against the
   value of new information." Across the four strands the same structure
   recurs: aggressive probing improves estimates but can spoil
   performance, cautious control does the reverse.

3. **Closed-loop identifiability decides whether exploration must leave the
   optimal policy.** If the parameters the optimal policy fails to identify
   are unimportant, the issue can be ignored and log T regret is
   achievable; "if the optimal controller makes essential parameters
   non-identifiable … then exploration needs to drive the system away from
   optimality with higher regret", the √T regime.

## Scope

An account of the review's synthesis, attributed to Meijer and Rantzer and
to the primary works they survey. It is Proposed: the identifiability
dichotomy (part 3) is load-bearing and should be carried by a primary
source, not the review's summary, before the record accepts it.

## Bearing

It bears on [QUESTION-374](../questions.d/QUESTION-374.md): dual control is the limiting case in which
observing and acting are the *same* action rather than two draws on one
budget, so it marks the boundary of the question's shared-budget part. It
is the complement of [CLAIM-572](../claims.d/CLAIM-572.md)'s separated-budget model (which excludes
the dual-control case) and the unconstrained background to
[THEORY-1254](../theory.d/THEORY-1254.md)'s safety-constrained dual-control bound.
