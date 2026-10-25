---
status: Proposed
promote_when: >-
  A step-by-step re-derivation, recorded under ADR-047 v2, of Theorem
  4.1's bound through Lemmas B.1–B.9 (or of Theorem 4.3's, whose proof the
  paper omits), or a reading of an independent source that proves the
  same rates for approachability under partial monitoring. The cited
  lower bounds are not in question here; the upper bounds are what is not
  yet checked.
title: 'For Blackwell approachability of an approachable polytope under partial monitoring with a known signal law, there are efficient algorithms whose average vector payoff reaches the target at expected distance O(T^-1/3) for general signals and O(T^-1/2) when the signal law does not depend on the decision, the worst-case optimal rates for those two classes'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Proposed from NOTE-tmpfxkdt, as Kwon and Perchet's Theorems 4.1
    and 4.3 state it. The flag estimate on which the general algorithm
    rests is re-derived in THEORY-tmpjv5er. The rest of Theorem 4.1's proof
    was read in outline, and Theorem 4.3's proof is omitted in the paper.
    Hence Proposed.
tags:
- learning-theory
- game-theory
date: '2026-10-25'
source:
- LIT-tmpm3j41
summary: >-
  Kwon and Perchet (2017), [LIT-tmpm3j41](../literature.d/LIT-tmpm3j41.md), read in [NOTE-tmpfxkdt](../notes.d/NOTE-tmpfxkdt.md). The rates
  are for the average payoff's distance to the target, uniformly over
  Nature's choices, with approachability assumed (Perchet's condition).
  Optimal means not improvable in the worst case over games. It gives no
  guarantee for individual stages or rolling windows, and none when the
  signal law is unknown.
---
<!-- inactive-ok-file: CLAIM-357 — Proposed; the claim whose dated note cites this work, nothing here rests on it -->
<!-- inactive-ok-file: THEORY-tmpz3a05 — Proposed; the regret classification compared with, from this batch -->
# THEORY-tmp172nr: For Blackwell approachability of an approachable polytope under partial monitoring with a known signal law, there are efficient algorithms whose average vector payoff reaches the target at expected distance O(T^-1/3) for general signals and O(T^-1/2) when the signal law does not depend on the decision, the worst-case optimal rates for those two classes

## Source

Kwon and Perchet (2017), AISTATS, PMLR 54:604–613, [LIT-tmpm3j41](../literature.d/LIT-tmpm3j41.md), Theorems
4.1 and 4.3, read in [NOTE-tmpfxkdt](../notes.d/NOTE-tmpfxkdt.md) with the supplementary material.

## What was actually shown

Decisions I, Nature's actions J, a vector payoff g: I × J → ℝ^d and a
signal law s: I × J → Δ(S), all finite and known. The target is
C = ℝ^d_−, to which polytopes reduce, and it is assumed approachable. Then:

- **General signals (Theorem 4.1).** An algorithm that lifts the problem
  to full-information approachability in a space of flag estimates, and
  plays each decision with probability at least γ/|I| with
  γ ∝ T^{−1/3}, guarantees
  E[d₂(ḡ_T, C)] ≤ 12‖g‖^{1/3}(L_r|I||K||A|)^{2/3}T^{−1/3} + O(T^{−1/2}),
  against any choices of Nature.
- **Outcome-dependent signals (Theorem 4.3).** If s(i, j) = s(i′, j), the
  same construction with no exploration gives O(T^{−1/2}).
- **Optimality.** Both rates match lower bounds that already hold for
  regret minimization: Cesa-Bianchi, Lugosi and Stoltz's T^{−1/3} for
  general signals, and the full-information T^{−1/2}.

What could have failed: the earlier best rates, T^{−1/5} and
T^{−1/(I+3)}, might have been the truth for approachability, with its
set-valued compatible payoffs. The lifting shows that partial monitoring
costs approachability no more than it costs regret, in the worst case.

## What this does not say

- **Not a rate for every game.** "Cannot be improved" is worst case over
  signal structures. A particular game can do better, as Bartók et al.'s
  locally observable games do for regret ([THEORY-tmpz3a05](THEORY-tmpz3a05.md)).
- **Not a per-stage or windowed guarantee.** The average is compensatory:
  a coordinate alternating +1 and −1 has average 0 ∈ C and is approached
  while violated on half the stages. This is [CLAIM-357](../claims.d/CLAIM-357.md)'s caution.
- **Not when the target is unapproachable.** Approachability is assumed.
  Perchet's characterization is cited, not proved or made checkable.
- **Not with unknown signal laws, or laws that change.**
- **Not that the constants are small.** They grow with the size of the
  simplicial subdivision.

## Connections

- **[CLAIM-357](../claims.d/CLAIM-357.md).** The record's one-shot target {z : z_i ≤ 0} is this
  theorem's C. Its worst residual is a max. The approachability distance
  is the ℓ₂ norm of the positive part of the average.
- **[THEORY-tmpz3a05](THEORY-tmpz3a05.md).** The same exponents in average form: √T regret is
  T^{−1/2}, T^{2/3} is T^{−1/3}.
- **[THEORY-tmpjv5er](THEORY-tmpjv5er.md).** The floor in the general algorithm, and why the
  outcome-dependent case needs none.
