---
number: 1395
status: Active
formerly:
- THEORY-tmphj1kw
title: 'Kaelbling, Littman and Cassandra restate, citing Smallwood and Sondik among others, that for a finite-state Markov process controlled through noisy observations the probability distribution over states is a sufficient statistic for control, show that the optimal value with finitely many steps left is the upper surface of finitely many linear functions of that distribution, hence piecewise-linear and convex, and credit Sondik with the first exact finite-horizon algorithm, whose worst case is exponential'
version: 3
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Filed Proposed from NOTE-1563, the reading in part of Kaelbling,
    Littman and Cassandra (LIT-2056), standing in for the unread
    Smallwood and Sondik (1973), LIT-2038.
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted by the twenty-ninth status review, at the status
    review's ruling (the owner delegated these rulings); ADR-065; ADR-047,
    kind 3. NOTE-1563 v2 reads in full the parts of the neighbour the title
    rests on (§§1, 3, 4.1–4.3, 4.5–4.6, 7). The title now reports the
    neighbour's account. The old title asserted Smallwood and Sondik's
    results directly. The neighbour cites them only for sufficiency,
    jointly with another work, and derives the piecewise-linear convex form
    itself. The attribution is recorded in LIT-2038's status note, and the
    original stays unread. The old title: Smallwood and Sondik: when a
    finite-state Markov process is controlled through noisy observations
    over a finite horizon, the probability distribution over its states is
    a sufficient statistic for control, and the optimal value with finitely
    many steps left is a piecewise-linear convex function of that
    distribution, so it can be computed by finitely many linear pieces. The
    old promote_when: "The original (Smallwood & Sondik 1973) is read and
    states that the state distribution is a sufficient statistic and that
    the finite-horizon optimal value is piecewise-linear and convex in it."
- version: 3
  date: '2026-11-11'
  note: >-
    Reading review of 2026-11-11 (by topic, second run, part P), under
    ADR-091 and ADR-tmpkuzwl. corroborates CLAIM-520 added. The claim's
    note of 2026-11-04: in a POMDP an information action "is only
    worthwhile when the value of the information ... exceeds the cost of
    gaining the information" (NOTE-1563), so "its conditional value of a
    corrective capacity falls out of a standard model". No other change.
tags:
- operations-research
- control-theory
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-2056
summary: >-
  Kaelbling, Littman and Cassandra (1998), [LIT-2056](../literature.d/LIT-2056.md), read in [NOTE-1563](../notes.d/NOTE-1563.md)
  (§§1, 3, 4.1–4.3, 4.5–4.6, 7, Appendix A). They restate the
  operations-research theory of partially observable Markov processes and
  cite Smallwood and Sondik (1973), [LIT-2038](../literature.d/LIT-2038.md), which is unread. The
  piecewise-linear convex value is the neighbour's own derivation, with
  discounting. Active as a report of the neighbour. It does not say that
  the pieces are few: exact solution is exponential in the worst case, and
  the infinite-horizon value may have infinitely many facets.
corroborates:
- CLAIM-520
---
<!-- inactive-ok-file: LIT-2038 — Unavailable; the unread original the neighbour cites, cited as open -->

# THEORY-1395: Kaelbling, Littman and Cassandra restate, citing Smallwood and Sondik among others, that for a finite-state Markov process controlled through noisy observations the probability distribution over states is a sufficient statistic for control, show that the optimal value with finitely many steps left is the upper surface of finitely many linear functions of that distribution, hence piecewise-linear and convex, and credit Sondik with the first exact finite-horizon algorithm, whose worst case is exponential

## Source

Smallwood and Sondik (1973), [LIT-2038](../literature.d/LIT-2038.md), the original, which was not read:
no lawful copy was found. Sourced to Kaelbling, Littman and Cassandra
(1998), [LIT-2056](../literature.d/LIT-2056.md), read in [NOTE-1563](../notes.d/NOTE-1563.md), which stands in for it at the owner's
request.

## What was actually shown

- **Sufficiency** (§3.2, p. 106): belief states "comprise a sufficient
  statistic for the past history and initial belief state of the agent",
  cited to [1,56], 56 being Smallwood and Sondik; so the optimal policy
  solves an MDP over beliefs (§3.4, p. 108).
- **Piecewise-linear convexity** (§4.1, p. 110): the value of a t-step
  policy tree is linear in the belief, and the optimal t-step value is the
  maximum over finitely many trees: "So, Vt is piecewise-linear and
  convex". This is the neighbour's own derivation, in the framework it
  takes from the operations-research literature, not a passage attributed
  to Smallwood and Sondik alone.
- **Computation** (§4.4, p. 114; §4.5, p. 117): Smallwood and Sondik
  construct the value function directly; their algorithm and Cheng's
  "still have worst-case running times exponential in at least one of the
  problem parameters". The first exact finite-horizon algorithm "was
  described by Sondik [56,58]".

## What this does not say

- That the original states these results in this form: it was not read,
  and the neighbour does not quote it.
- That the result holds for an undiscounted finite horizon as derived
  here: the neighbour's value functions carry a discount factor.
- That the number of linear pieces is small, or that exact solution is
  tractable: worst-case cost is exponential (p. 114).
- That the same holds for an infinite horizon: the discounted value stays
  convex but may have infinitely many facets (§4.6, p. 118).
- Anything about provisional dispatch, reassessment or cancellation, which
  is the pasted bibliography on emergency readiness's application, not the
  paper's or the neighbour's.
