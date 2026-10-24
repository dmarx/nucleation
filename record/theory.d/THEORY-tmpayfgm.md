---
status: Proposed
promote_when: >-
  A checked re-derivation recorded in this file of Theorem 1's sufficiency
  and of the indicator construction showing single-state games satisfy
  IGM, which ADR-047 counts toward promotion for the demonstrated part;
  the count of 177 of 310 is the paper's single experiment, which ADR-047
  lets stand on one study read in full. It is refuted by an error in
  either derivation, or by a reproduction of the random-game experiment
  with the same methods in which VDN and QMIX fail in far fewer games. The
  title claims nothing about partially observable tasks, where IGM's
  content lies.
title: 'Individual-Global-Max, that the agents'' individually greedy actions form a greedy joint action, is strictly weaker than additive or monotonic factorisation: every single-state matrix game with a unique optimum satisfies it, yet in 177 of 310 random three-by-three two-agent games value-decomposition and monotonic mixing failed to learn the optimal joint action that an IGM-only method found; a sufficient condition is that the sum of individual values, shifted by a state value, equals the joint value at the greedy profile and bounds it from above elsewhere'
version: 1
tags:
- game-theory
- learning-theory
date: '2026-10-24'
source:
- LIT-tmpev178
summary: >-
  Son et al.'s QTRAN (ICML 2019), read in full in [NOTE-tmp457xj](../notes.d/NOTE-tmp457xj.md), with
  Theorem 1 and the single-state observation re-derived. IGM presupposes a
  real-valued joint value and constrains only the optimum: members may
  rank everything below it differently from the collective. With full
  observability it is nearly empty; its content is whether members acting
  on local histories can each pick their part of the optimum.
---
<!-- inactive-ok-file: NOTE-tmp457xj — the reading this is filed from -->

# THEORY-tmpayfgm: Individual-Global-Max, that the agents' individually greedy actions form a greedy joint action, is strictly weaker than additive or monotonic factorisation: every single-state matrix game with a unique optimum satisfies it, yet in 177 of 310 random three-by-three two-agent games value-decomposition and monotonic mixing failed to learn the optimal joint action that an IGM-only method found; a sufficient condition is that the sum of individual values, shifted by a state value, equals the joint value at the greedy profile and bounds it from above elsewhere

## Source

Son, Kim, Kang, Hostallero & Yi, [LIT-tmpev178](../literature.d/LIT-tmpev178.md), read in [NOTE-tmp457xj](../notes.d/NOTE-tmp457xj.md) from
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
