---
number: 962
status: Active
formerly:
- THEORY-tmpwtj3m
title: 'In a finite partial-monitoring game, the signals of a set D of actions determine the expected loss difference of actions i and j under every outcome distribution iff ℓ_i − ℓ_j lies in the sum of the row spaces of their signal matrices; when it does not, two outcome distributions differing along a vector in the common kernel give every action in D the same signal law and reverse the preference between i and j, so no amount of play restricted to D can learn the comparison'
version: 2
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Active from NOTE-1164. The condition is Bartók et al.'s
    Definitions 5–6 and the first step of their Theorem 4. Both directions
    are re-derived below step by step, which meets the condition for
    Active under ADR-047 v2. Its application to the approach–avoid game,
    and the variants with suppressed feedback and a costly check, are the
    record's.
- version: 2
  date: '2026-10-25'
  note: >-
    From the reading of Lattimore and Szepesvári (LIT-1524, NOTE-
    tmpkgxba). The Source notes that Bartók et al.'s Theorem 4 takes this
    step with D = {i, j} where it needs D = N⁺_{i,j} (THEORY-961), so
    the lemma as stated, for general D, is the corrected form. THEORY-
    tmpyulw1 is added beside THEORY-964. The account is unchanged.
tags:
- learning-theory
- game-theory
date: '2026-10-25'
source:
- LIT-1528
summary: >-
  Bartók, Foster, Pál, Rakhlin and Szepesvári (2014), [LIT-1528](../literature.d/LIT-1528.md), read
  in [NOTE-1164](../notes.d/NOTE-1164.md). Observability in partial monitoring is a
  linear-algebra condition on the loss and signal matrices: a comparison
  is learnable from some actions exactly when its loss difference is in the
  span of their signal row spaces. Global and local observability are the
  two choices of D the classification uses. It says what can be
  estimated, not how fast; the rates are [THEORY-964](THEORY-964.md).
supports:
- CLAIM-446
answers:
- QUESTION-272
extended_by:
- THEORY-961
presupposed_by:
- THEORY-963
---
<!-- inactive-ok-file: THEORY-964 — Superseded by THEORY-963; the classification this lemma feeds, filed from the same reading -->
<!-- inactive-ok-file: CLAIM-446 — Proposed; the claim whose example is worked here, nothing here rests on it -->
# THEORY-962: In a finite partial-monitoring game, the signals of a set D of actions determine the expected loss difference of actions i and j under every outcome distribution iff ℓ_i − ℓ_j lies in the sum of the row spaces of their signal matrices; when it does not, two outcome distributions differing along a vector in the common kernel give every action in D the same signal law and reverse the preference between i and j, so no amount of play restricted to D can learn the comparison

## Source

Bartók, Foster, Pál, Rakhlin and Szepesvári (2014), *Mathematics of
Operations Research* 39(4):967–997, [LIT-1528](../literature.d/LIT-1528.md), read in [NOTE-1164](../notes.d/NOTE-1164.md) from
the authors' preprint of March 2013. The condition is their Definitions 5
(global observability, from Piccolboni and Schindelhauer) and 6 (local
observability). The necessity argument is the first paragraph of the proof
of their Theorem 4, taken there with D = {i, j}; the proof needs
D = N⁺_{i,j}, as Lattimore and Szepesvári's footnote corrects
([THEORY-961](THEORY-961.md)). The lemma as stated here, for general D, is the
corrected form. The derivation below is the record's.

## What was actually shown

A finite game has actions 1, …, N and outcomes 1, …, M. Action i has loss
vector ℓ_i ∈ ℝ^M and signal matrix S_i ∈ {0,1}^{s_i×M}, where (S_i)_{σ,m} = 1
when outcome m gives symbol σ under action i. Each column of S_i has exactly
one 1, so 1ᵀS_i = 1ᵀ. Under an outcome distribution p ∈ Δ_M, playing i shows
a symbol with law S_i p. Let D be a set of actions, A_D the matrix whose
column blocks are S_kᵀ for k ∈ D, and d = ℓ_i − ℓ_j.

**If.** Suppose d = Σ_{k∈D} S_kᵀ v_k for some vectors v_k. Then
dᵀp = Σ_k v_kᵀ(S_k p) for every p, so the expected loss difference is a
fixed linear function of the signal laws of the actions in D. The averages
of the observed symbol indicators converge to S_k p, which gives an unbiased
estimate (Bartók et al.'s observer vectors).

**Only if.** Suppose d ∉ Im A_D. Write d = a + v with a ∈ Im A_D and
v ⊥ Im A_D. Then v ≠ 0, and since (Im A_D)^⊥ = Ker A_Dᵀ, S_k v = 0 for every
k ∈ D. Also dᵀv = vᵀv > 0. Because 1ᵀS_k = 1ᵀ, 1ᵀv = 1ᵀS_k v = 0, so v moves
along the simplex. Take p₀ in the relative interior of Δ_M and ε > 0 small
enough that p± = p₀ ± εv ∈ Δ_M. Then S_k p₊ = S_k p₋ for every k ∈ D: every
action in D shows the same signal law under the two distributions. But
dᵀ(p₊ − p₋) = 2ε‖v‖² ≠ 0. Choosing p₀ on the set where dᵀp₀ = 0, which
Theorem 4 does by taking it on the shared boundary of two neighbouring
cells, makes i strictly better under one and j under the other. So no
function of any number of signals from D decides the comparison.

**The two observability conditions** are this lemma with two choices of D.
Global observability takes D = all actions for every pair. Local
observability takes, for neighbouring i and j, D = N⁺_{i,j}, the actions
optimal on the boundary between them. Those are the actions a learner can
play near that boundary without paying a constant loss.

**The approach–avoid game** ([CLAIM-446](../claims.d/CLAIM-446.md)'s note of 2026-10-25). Outcomes are
(dangerous, safe). ℓ_avoid = (0, c), ℓ_approach = (H, 0), S_avoid = [1 1] and
S_approach = I₂, with H, c > 0. With p the probability of danger, avoid is
optimal for p ≥ c/(H + c), so the cells are two segments meeting at one
point, the actions are neighbours and N⁺ = {avoid, approach}. The vector d
is not in Im S_avoidᵀ = span(1, 1): its kernel vector is v = (1, −1), and
dᵀv = −(H + c) ≠ 0. Avoid's signal never decides the comparison. With
approach included the span is ℝ², and the pair is locally observable.
Recomputed by least squares at H = 5, c = 1: residual 4.24 for avoid alone,
0 for both.

Two variants, by the same lemma:

- **Feedback suppressed.** If approach shows one symbol whatever the
  outcome, then S_approach = [1 1] and Im A = span(1, 1) for D = all
  actions. The game is not globally observable, and v = (1, −1) still
  separates.
- **A costly check.** Add an action with loss (k, k) and S = I₂, and make
  approach uninformative. The check is optimal where k ≤ min(Hp, c(1 − p)),
  that is p ∈ [k/H, 1 − k/c]. That set is empty when k > Hc/(H + c). In
  that case the check is dominated and not in N⁺_{avoid,approach}, so the
  pair is not locally observable, though the game is globally observable
  through the check. When k < Hc/(H + c), the check has a cell between the
  other two, the neighbour pairs become avoid–check and check–approach,
  and each is locally observable through the check's own signal. Checked
  numerically with H = 5, c = 1 and k = 0.5, 0.8, 0.9.

What could have failed: the comparison might have been learnable from D by
some non-linear use of the signals even outside the span. The kernel
construction rules that out. Two distributions that every action in D
renders identically cannot be told apart by any statistic.

## What this does not say

- **Not the rates.** That a comparison is learnable from D says nothing
  about how fast. The classification (Θ̃(√T), Θ(T^{2/3}), Θ(T)) is
  [THEORY-964](THEORY-964.md) as Bartók et al. state it, and [THEORY-963](THEORY-963.md) for every
  finite game. The lemma is one step of their lower bound, not the
  bound.
- **Not that a learner restricted to D has high regret in its own game.**
  Regret is measured against the actions available. A learner allowed only
  avoid has one action and zero regret by definition. What fails is
  learning the comparison with approach, and the cost of that appears as
  regret in the larger game.
- **Not about anxiety.** That avoidance, safety behaviour or checking has
  these loss and signal matrices is [CLAIM-446](../claims.d/CLAIM-446.md)'s interpretive premise, not
  something the lemma shows.
- **Not about random or changing signals.** §6.3 of the paper extends the
  condition to random signals, with the matrix of signal laws Ξ in place
  of S. A signal structure that changes during play is outside it.

## Connections

- **[CLAIM-446](../claims.d/CLAIM-446.md).** This is the formal content of "under the avoidance that
  authority selects, the hypotheses ... predict the same observation": the
  vector v = (1, −1) is the pair H_D versus H_S, and S_avoid v = 0.
- **[QUESTION-031](../questions.d/QUESTION-031.md).** A condition on a probe family, checkable before any
  data, under which agreement on every probe implies agreement on a stated
  decision. Here the decision family is the pairwise comparisons, and the
  probes are the actions' signal matrices. It is an answer for that
  decision family only, and for deterministic or known-law signals.
- **[QUESTION-271](../questions.d/QUESTION-271.md)** asks when bandit-style feedback suffices. The lemma says
  which comparisons the played actions can resolve at all.
- **[THEORY-755](THEORY-755.md).** Both are kernel conditions on a linear map: a coarse
  description closes when the dynamics carry no component the summary
  cannot see, and a comparison is learnable when the loss difference has
  no component the signals cannot see.
- **[THEORY-963](THEORY-963.md).** Lattimore and Szepesvári's classification for all
  finite games, beside [THEORY-964](THEORY-964.md). Its local observability is this
  lemma with D = N_ab, and its corrected lower bound takes the kernel
  vector of the stacked signal matrices of N_ab, as here
  ([THEORY-961](THEORY-961.md)).
