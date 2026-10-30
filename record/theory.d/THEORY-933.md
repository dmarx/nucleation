---
number: 933
status: Active
formerly:
- THEORY-tmpayfgm
title: 'Individual-Global-Max, that the agents'' individually greedy actions form a greedy joint action, is strictly weaker than additive or monotonic factorisation: every single-state matrix game with a unique optimum satisfies it, yet in 177 of 310 random three-by-three two-agent games value-decomposition and monotonic mixing failed to learn the optimal joint action that an IGM-only method found; a sufficient condition is that the sum of individual values, shifted by a state value, equals the joint value at the greedy profile and bounds it from above elsewhere'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings), under ADR-065 §5. A second checker followed Theorem
    1's sufficiency and the indicator construction and re-ran them by
    script with controls (status review 22). The count of 177 of 310
    stands on the one study, read in full in NOTE-1141, as the
    promote_when says. One caveat is added to the body: that additive or
    monotonic factorisation implies IGM needs a unique optimum. The old
    promote_when: A checked re-derivation recorded in this file of Theorem
    1's sufficiency and of the indicator construction showing single-state
    games satisfy IGM, which ADR-047 counts toward promotion for the
    demonstrated part; the count of 177 of 310 is the paper's single
    experiment, which ADR-047 lets stand on one study read in full. It is
    refuted by an error in either derivation, or by a reproduction of the
    random-game experiment with the same methods in which VDN and QMIX
    fail in far fewer games. The title claims nothing about partially
    observable tasks, where IGM's content lies.
tags:
- game-theory
- learning-theory
date: '2026-10-24'
source:
- LIT-1510
summary: >-
  Son et al.'s QTRAN (ICML 2019), read in full in [NOTE-1141](../notes.d/NOTE-1141.md), with
  Theorem 1 and the single-state observation re-derived. IGM presupposes a
  real-valued joint value and constrains only the optimum: members may
  rank everything below it differently from the collective. With full
  observability it is nearly empty; its content is whether members acting
  on local histories can each pick their part of the optimum.
---

# THEORY-933: Individual-Global-Max, that the agents' individually greedy actions form a greedy joint action, is strictly weaker than additive or monotonic factorisation: every single-state matrix game with a unique optimum satisfies it, yet in 177 of 310 random three-by-three two-agent games value-decomposition and monotonic mixing failed to learn the optimal joint action that an IGM-only method found; a sufficient condition is that the sum of individual values, shifted by a state value, equals the joint value at the greedy profile and bounds it from above elsewhere

## Source

Son, Kim, Kang, Hostallero & Yi, [LIT-1510](../literature.d/LIT-1510.md), read in [NOTE-1141](../notes.d/NOTE-1141.md) from
arXiv:1905.05408v1: Definition 1 and Theorem 1 (pp. 2–3), the proofs in
supplement B, and supplement D (Table 6).

## What was actually shown

- **Definition.** [Q_i] satisfy IGM for Q_jt under τ when argmax_u Q_jt(τ, u)
  is the vector of argmax_{u_i} Q_i(τ_i, u_i).
- **Sufficient condition (Theorem 1).** With V_jt = max_u Q_jt − Σ Q_i(ū_i),
  if Σ Q_i(u_i) − Q_jt(u) + V_jt is 0 at ū and ≥ 0 elsewhere, then
  Q_jt(ū) = Σ Q_i(ū_i) + V_jt ≥ Σ Q_i(u_i) + V_jt ≥ Q_jt(u). Re-derived when
  filed. Necessary up to a positive rescaling of the Q_i, given strict gaps
  (Proposition 1).
- **Single-state games.** "Since matrix games always satisfy IGM
  conditions" (supplement D). For a unique optimum u*, Q_i(u_i) = 1 if
  u_i = u*_i and 0 otherwise factorises it; checked when filed.
- **The experiment.** 310 random 3×3 games, payoffs in [0, 1], full
  exploration: QTRAN-base found the optimum in all; VDN and QMIX matched it
  in 114 and both missed it in 177; they differed in 19 (Table 6).

## What this does not say

- **That IGM is a condition for a common currency.** Q_jt is given; IGM
  concerns decentralising it.
- **That IGM-satisfying members agree with the collective.** Only at the
  top; below it their rankings can disagree.
- **Which partially observable tasks satisfy IGM.** The paper gives no
  characterisation and no example of a task outside it.
- **That QTRAN learns better in general.** Its other evidence is two small
  environment families.

## Note of 2026-10-30: the second check

The second check at the status review ([ADR-065](../decisions.d/ADR-065.md) §5) followed each step.

Theorem 1. With V_jt = max_u Q_jt − Σ Q_i(ū_i), the condition at ū gives
Q_jt(ū) = Σ Q_i(ū_i) + V_jt. Since each ū_i maximises Q_i, Σ Q_i(ū_i) ≥ Σ
Q_i(u_i), and the condition elsewhere gives Σ Q_i(u_i) + V_jt ≥ Q_jt(u).
So ū is a joint maximiser.

Single-state games. With a unique optimum u*, the values Q_i(u_i) = 1 if
u_i = u*_i and 0 otherwise have the unique maxima u*_i, and their profile
u* is the unique joint maximiser.

Strictness. [[2, 1], [1, 8]] satisfies IGM with Q_1 = Q_2 = (0, 1), and it
is not monotonically representable ([THEORY-929](THEORY-929.md)). The experiment's counts
add up: 114 + 177 + 19 = 310.

That additive or monotonic factorisation implies IGM needs a unique
optimum, which Definition 1's "the vector of argmaxes" presupposes: [[1,
1], [0, 1]] is monotonic, but its set of joint maximisers is not a product
of individual ones.

A script (numpy, in the session's scratchpad) checked these steps. In 2000
random constructions meeting Theorem 1's condition, the greedy profile was
always a joint maximiser; as a control, violating the bound at one
non-greedy profile made it fail in 200 of 200. Indicator values recovered
the optimum in 1000 random 3 × 3 games. Of 2000 random 3 × 3 games with
uniform payoffs, only 8 were monotonically representable.
