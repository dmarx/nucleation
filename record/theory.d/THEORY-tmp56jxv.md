---
status: Proposed
promote_when: >-
  A checked re-derivation recorded in this file of the sufficiency step
  (made in NOTE-tmpoitn8) and of the two matrix examples, the additive
  impossibility for [[0, 1], [1, 8]] and the monotonic impossibility for
  [[2, 1], [1, 8]], which ADR-047 counts toward promotion. It is refuted
  by a non-decreasing mixing whose greedy profile is not a joint
  maximiser, or by a monotonic mixing of per-agent values that represents
  a payoff in which an agent's best action depends on the others'
  simultaneous actions. Nothing about StarCraft performance bears on it.
title: 'A joint action-value that is a non-decreasing function of per-agent values, each conditioning only on its agent''s own history, makes the profile of the agents'' individually greedy actions a greedy joint action, which suffices for decentralised greedy execution and is strictly more expressive than a sum; it cannot represent a joint value in which an agent''s best action depends on what the others do at the same step'
version: 1
tags:
- game-theory
- learning-theory
date: '2026-10-24'
source:
- LIT-tmp3ztxf
- LIT-tmpev178
summary: >-
  Rashid et al.'s QMIX (ICML 2018), read in full in NOTE-tmpoitn8, with
  QTRAN (NOTE-tmp457xj) for the strictness. Monotonicity is sufficient for
  the greedy-profile property and not necessary. It presupposes a real-
  valued joint value: what it adds is that each member's ranking of its
  own actions agrees with the collective's whatever the others do, an
  ordinal separability condition. It is Wolpert and Tumer's factoredness
  stated for values.
---
<!-- inactive-ok-file: NOTE-tmpoitn8 NOTE-tmp457xj THEORY-tmpayfgm — the readings this is filed from and its companion, named -->

# THEORY-tmp56jxv: A joint action-value that is a non-decreasing function of per-agent values, each conditioning only on its agent's own history, makes the profile of the agents' individually greedy actions a greedy joint action, which suffices for decentralised greedy execution and is strictly more expressive than a sum; it cannot represent a joint value in which an agent's best action depends on what the others do at the same step

## Source

Rashid, Samvelyan, Schroeder de Witt, Farquhar, Foerster & Whiteson,
LIT-tmp3ztxf, read in NOTE-tmpoitn8 from arXiv:1803.11485v2: Eqs. 4–5
(p. 4), section 4.1, supplement A (Table 3) and the two-step game
(Tables 1–2, supplement B). Strictness against IGM from Son et al.,
LIT-tmpev178 (NOTE-tmp457xj).

## What was actually shown

- **Sufficiency.** If Q_tot = f(Q_1, …, Q_n; s) with f non-decreasing in
  each Q_a, then for any joint action u,
  f(Q_1(ū^1), …, Q_n(ū^n)) ≥ f(Q_1(u^1), …, Q_n(u^n)), since each
  Q_a(ū^a) ≥ Q_a(u^a). Re-derived when filed. Ties can make the greedy
  profile one maximiser among several.
- **More than a sum.** [[0, 1], [1, 8]] is monotonic and not additive:
  a₁ + b₁ = 0, a₁ + b₂ = 1, a₂ + b₁ = 1 force a₂ + b₂ = 2. QMIX learned it
  exactly (0.00, 1.00, 1.00, 8.00); VDN did not, and took the suboptimal
  first move.
- **Not every payoff.** [[2, 1], [1, 8]] is not monotonically
  representable: with the partner at A, agent 1 must rank A over B (2 > 1),
  with the partner at B, B over A (8 > 1), and no single Q_1 does both.
- **Not necessary.** That same matrix satisfies the greedy-profile property
  (both agents' values preferring B give the optimum 8), so monotonicity
  is stronger than what decentralised greedy action needs; QTRAN's 177 of
  310 random games are the systematic version.

## What this does not say

- **That monotonic mixing gives a common currency.** The joint value is
  real-valued by assumption; the condition concerns how members' rankings
  relate to it.
- **That a non-monotonic task cannot be decentralised.** IGM can hold
  without monotonicity (THEORY-tmpayfgm).
- **Anything under partial observability beyond a remark.** The paper says
  QMIX "cannot necessarily represent the value function" there.
