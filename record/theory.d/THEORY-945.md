---
number: 945
status: Proposed
formerly:
- THEORY-tmpy4yji
promote_when: >-
  A checked derivation, recorded here, of the expansion that removes the
  first-order term and of the remainder bound (made when filed, from
  NOTE-1148), together with either a proof that reconciles the
  contraction condition (Boltzmann temperature above K/2) with the
  greedy-in-the-limit assumption, or an independent replication in which
  mean field Q-learning learns tasks of hundreds of homogeneous agents
  where independent learners fail. It is refuted if the expansion's
  first-order term does not vanish, or if replications with heterogeneous
  but exchangeable agents fail where the paper's succeed. Results for
  agents that are not exchangeable within a neighbourhood fall outside it
  and neither promote nor refute it.
title: 'When each agent''s Q-function is approximated as an average of pairwise terms and expanded about the mean action of its neighbours, the first-order term vanishes and the approximation error is a second-order remainder bounded by the curvature of the pairwise Q-function, leaving a two-body problem between an agent and its neighbours'' average; with homogeneous agents, mean field Q-learning converges to the Nash Q-value under assumptions the authors call strong, and learned tasks of 500 and 1000 agents where independent and centralized-critic baselines failed'
version: 1
tags:
- game-theory
- learning-theory
- complex-systems
date: '2026-10-24'
source:
- LIT-1512
summary: >-
  Yang et al. (2018), read in full in [NOTE-1148](../notes.d/NOTE-1148.md) from arXiv v5. The
  expansion and the remainder bound were re-derived when filed; the
  appendix states an equality where only an inequality holds, which leaves
  the bound intact. The cancellation of remainders is argued from
  homogeneity, not proved, and the contraction step needs a high
  temperature while the convergence theorem assumes a greedy limit. The
  approximation requires agents interchangeable within a neighbourhood.
---
<!-- inactive-ok-file: NOTE-1148 — the reading this is filed from -->

# THEORY-945: When each agent's Q-function is approximated as an average of pairwise terms and expanded about the mean action of its neighbours, the first-order term vanishes and the approximation error is a second-order remainder bounded by the curvature of the pairwise Q-function, leaving a two-body problem between an agent and its neighbours' average; with homogeneous agents, mean field Q-learning converges to the Nash Q-value under assumptions the authors call strong, and learned tasks of 500 and 1000 agents where independent and centralized-critic baselines failed

## Source

Yang, Luo, Li, Zhou, Zhang & Wang (2018), [LIT-1512](../literature.d/LIT-1512.md), read in
[NOTE-1148](../notes.d/NOTE-1148.md) from arXiv:1802.05438v5: section 3 (Eqs. 5–14, Theorem 1),
appendices B and D, and section 5.1 (Figure 3).

## What was actually shown

- **The expansion.** With a^k = ā^j + δa^{j,k} and Σ_k δa^{j,k} = 0, the
  first-order term of the Taylor expansion of Σ_k Q^j(s, a^j, a^k) about
  ā^j vanishes. Each second-order remainder is at most M‖δa‖² in absolute
  value, and ‖δa‖² ≤ 2(1 − ā_i) ≤ 2, for an M-smooth pairwise Q. Re-derived
  when filed; appendix B's Eq. 27 states the norm as an equality, which
  holds only as an upper bound.
- **The theorem.** Convergence to the Nash Q-value w.p.1 under infinite
  visitation with bounded rewards, a greedy-in-the-limit policy, and every
  stage game in training having a global optimum or a saddle point as its
  equilibrium. Proposition 1, which the proof uses, needs the Boltzmann
  temperature above K/2.
- **The experiment.** In Gaussian Squeeze with μ = 400 and σ = 200, MF-Q
  and MF-AC learn the optimal allocation with 500 and 1000 agents, while
  independent learners, FMQ, Rec-FMQ and a MADDPG variant fail.

## What this does not say

That the remainders cancel in general: that is argued from homogeneity,
and the bound does not make them small. That the method applies to agents
whose identity or role matters to their neighbours: the mean action
discards both. That it models several interacting populations or
timescales. Or that the stated convergence conditions can all hold at
once; the paper does not reconcile its high-temperature contraction with
its greedy limit.
