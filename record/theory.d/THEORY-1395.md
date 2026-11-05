---
number: 1395
status: Proposed
formerly:
- THEORY-tmphj1kw
promote_when: >-
  The original (Smallwood & Sondik 1973) is read and states that the state distribution is a sufficient statistic and that the finite-horizon optimal value is piecewise-linear and convex in it.
title: 'Smallwood and Sondik: when a finite-state Markov process is controlled through noisy observations over a finite horizon, the probability distribution over its states is a sufficient statistic for control, and the optimal value with finitely many steps left is a piecewise-linear convex function of that distribution, so it can be computed by finitely many linear pieces'
version: 1
tags:
- operations-research
- control-theory
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-2056
summary: >-
  Smallwood and Sondik (1973), [LIT-2038](../literature.d/LIT-2038.md), unread, as restated by Kaelbling, Littman and Cassandra (1998), [LIT-2056](../literature.d/LIT-2056.md), skimmed in [NOTE-1563](../notes.d/NOTE-1563.md) (§§3, 4.1–4.3, 4.5–4.6, 5.1–5.2). The neighbour cites Smallwood and Sondik, with one other work, for the sufficiency of the belief state, and derives the piecewise-linear convex value itself in the same framework; it credits Sondik with the first exact finite-horizon algorithm. Proposed until the original is read. It does not say that the finitely many pieces are few: exact solution is exponential in the worst case, and the infinite-horizon value may have infinitely many facets.
---
<!-- inactive-ok-file: LIT-2038 NOTE-1563 — Unavailable or Skimmed, and new; the unread original and the reading of the neighbour that stands in for it, cited as open -->

# THEORY-1395: Smallwood and Sondik: when a finite-state Markov process is controlled through noisy observations over a finite horizon, the probability distribution over its states is a sufficient statistic for control, and the optimal value with finitely many steps left is a piecewise-linear convex function of that distribution, so it can be computed by finitely many linear pieces

## Source

Smallwood and Sondik (1973), [LIT-2038](../literature.d/LIT-2038.md), the original, which was not read: no lawful copy was found. Sourced to Kaelbling, Littman and Cassandra (1998), [LIT-2056](../literature.d/LIT-2056.md), read in part in [NOTE-1563](../notes.d/NOTE-1563.md), which stands in for it at the owner's request.

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
- That the number of linear pieces is small, or that exact solution is
  tractable: worst-case cost is exponential (p. 114).
- That the same holds for an infinite horizon: the discounted value stays
  convex but may have infinitely many facets (§4.6, p. 118).
- Anything about provisional dispatch, reassessment or cancellation, which
  is the pasted bibliography on emergency readiness's application, not the
  paper's or the neighbour's.
