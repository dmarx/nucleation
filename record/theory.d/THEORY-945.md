---
number: 945
status: Active
formerly:
- THEORY-tmpy4yji
title: 'When each agent''s Q-function is approximated as an average of pairwise terms and expanded about the mean action of its neighbours, the first-order term vanishes and the approximation error is a second-order remainder bounded by the curvature of the pairwise Q-function, leaving a two-body problem between an agent and its neighbours'' average; Yang et al. state that with homogeneous agents mean field Q-learning converges to the Nash Q-value under three assumptions, one of which they call a strong constraint, by a proof whose contraction step needs a temperature above K/2 while its greedy-in-the-limit assumption needs the temperature to fall to zero; in their Gaussian Squeeze runs with 500 and 1000 agents, mean field Q-learning and actor-critic learned the optimal allocation where independent learners, FMQ, Rec-FMQ and a MADDPG variant failed'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed and promoted to Active at the status review's ruling (the
    owner delegated these rulings), under ADR-065 §5 and §3 and ADR-047's
    "Where a narrowing's dropped claims go". A second checker (the
    twenty-fourth status review) re-derived the expansion, the remainder
    bound, the norm inequality and Proposition 1's constant, and checked
    them by script with controls; the steps are in the note of 2026-10-30.
    The title was narrowed in three ways. The convergence theorem is
    attributed, with the gap the reading found in its proof. The
    experiment is named as the one task it was, at two sizes. And "the
    authors call strong" now names the one assumption they call so. The
    old title, which the paper asserts, is kept as THEORY-tmp3xe34,
    Proposed, which extends this entry and inherits the promote_when
    (ADR-047, kind 1). The old title: When each agent's Q-function is approximated as an average of pairwise terms and expanded about the mean action of its neighbours, the first-order term vanishes and the approximation error is a second-order remainder bounded by the curvature of the pairwise Q-function, leaving a two-body problem between an agent and its neighbours' average; with homogeneous agents, mean field Q-learning converges to the Nash Q-value under assumptions the authors call strong, and learned tasks of 500 and 1000 agents where independent and centralized-critic baselines failed. The old promote_when:
    A checked derivation, recorded here, of the expansion that removes the first-order term and of the remainder bound (made when filed, from NOTE-1148), together with either a proof that reconciles the contraction condition (Boltzmann temperature above K/2) with the greedy-in-the-limit assumption, or an independent replication in which mean field Q-learning learns tasks of hundreds of homogeneous agents where independent learners fail. It is refuted if the expansion's first-order term does not vanish, or if replications with heterogeneous but exchangeable agents fail where the paper's succeed. Results for agents that are not exchangeable within a neighbourhood fall outside it and neither promote nor refute it.
tags:
- game-theory
- learning-theory
- complex-systems
date: '2026-10-24'
source:
- LIT-1512
summary: >-
  Yang et al. (2018), read in full in NOTE-1148 from arXiv v5. The
  expansion and the remainder bound were re-derived when filed and
  second-checked on 2026-10-30; the appendix states an equality where
  only an inequality holds, which leaves the bound intact. The
  convergence theorem is reported, not held. Its contraction step needs a
  high temperature while it assumes a greedy limit, and the cancellation
  of remainders is argued from homogeneity, not proved. The approximation
  requires agents interchangeable within a neighbourhood. Whether the
  method works as claimed is THEORY-tmp3xe34.
---

<!-- inactive-ok-file: THEORY-tmp3xe34 — Proposed; the wide form this entry was narrowed from, which extends it -->

# THEORY-945: When each agent's Q-function is approximated as an average of pairwise terms and expanded about the mean action of its neighbours, the first-order term vanishes and the approximation error is a second-order remainder bounded by the curvature of the pairwise Q-function, leaving a two-body problem between an agent and its neighbours' average; Yang et al. state that with homogeneous agents mean field Q-learning converges to the Nash Q-value under three assumptions, one of which they call a strong constraint, by a proof whose contraction step needs a temperature above K/2 while its greedy-in-the-limit assumption needs the temperature to fall to zero; in their Gaussian Squeeze runs with 500 and 1000 agents, mean field Q-learning and actor-critic learned the optimal allocation where independent learners, FMQ, Rec-FMQ and a MADDPG variant failed

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

## Note of 2026-10-30: the re-derivation, written out

The second check at the status review (ADR-065 §5) followed each step.

1. **The first-order term.** Write a^k = ā + δa^k with ā = (1/N) Σ_k a^k,
so Σ_k δa^k = 0. Taylor's theorem about ā gives Q(a^k) = Q(ā) +
∇Q(ā)·δa^k + R_k. The gradient is taken at the same point for every k, so
Σ_k ∇Q(ā)·δa^k = ∇Q(ā)·Σ_k δa^k = 0.

2. **The remainder.** R_k = ½ δa^kᵀ ∇²Q(ξ_k) δa^k for some ξ_k on the
segment. If the Hessian's norm is at most M, then |R_k| ≤ (M/2)‖δa^k‖²,
which is within the entry's M‖δa‖².

3. **The norm.** For a one-hot a^k = e_i, ‖e_i − ā‖² = 1 − 2ā_i + ‖ā‖².
Since ‖ā‖² ≤ Σ_j ā_j = 1, this is at most 2(1 − ā_i) ≤ 2. Equality holds
only when ‖ā‖² = 1, that is, when ā is itself one-hot. So appendix B's
Eq. 27 holds as an upper bound, not as an equality.

4. **Proposition 1's constant.** For binary actions the Boltzmann
response is σ((Q₁ − Q₀)/T). The logistic's slope is at most ¼, and Q₁ −
Q₀ is 2K-Lipschitz when each is K-Lipschitz. So the response is
K/(2T)-Lipschitz, and it is a contraction only when T > K/2. Assumption
2, a greedy-in-the-limit policy, needs T → 0.

A script (numpy, in the session's scratchpad, s945_mf.py) checked these
steps. It drew 2,000 random cases with 2 to 7 actions and 2 to 59
neighbours, and a smooth pairwise Q(a) = aᵀWa + b·a + s sin(c·a) whose
Hessian is bounded by M = 2‖sym W‖ + |s|‖c‖². The first-order sum was at
most 1.9 × 10⁻¹⁴. The largest |R_k| was 0.997 of (M/2)‖δa^k‖². The norm
identity and the bound 2(1 − ā_i) ≤ 2 held for every neighbour term. Over
2,000 random K-Lipschitz pairs on [0, 1] the response's slope reached at
most 0.995 of K/(2T). It had three controls, each of which had to fail,
and each did. Expanding about a point other than the mean left a
first-order term in all 2,000 cases. Eq. 27 as an equality failed for
60,434 neighbour terms. With Q₁ − Q₀ = 2Kp at T = 0.4 < K/2, the slope
was 1.25, so the response was not a contraction.

## Note of 2026-10-30: the clauses the narrowing drops

The title stated as fact that mean field Q-learning converges to the Nash
Q-value under the authors' assumptions. The record found that the proof
needs a temperature above K/2 for its contraction, while it assumes a
greedy limit. So convergence is reported, not held. The title also said
"tasks" of 500 and 1000 agents where it was one task at two sizes. The
wide form, which the paper asserts, is kept as THEORY-tmp3xe34, Proposed,
which extends this entry and inherits the old promote_when (ADR-047's kind
1). The plural "tasks" was a mis-statement and is recorded here only.
