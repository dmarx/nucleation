---
number: 929
status: Active
formerly:
- THEORY-tmp56jxv
title: 'A joint action-value that is a non-decreasing function of per-agent values, each conditioning only on its agent''s own history, makes the profile of the agents'' individually greedy actions a greedy joint action, which suffices for decentralised greedy execution and is strictly more expressive than a sum; it cannot represent a joint value in which an agent''s best action depends on what the others do at the same step'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings), under ADR-065 §5. A second checker followed the
    sufficiency step and both matrix examples and re-ran them by script
    with controls (status review 22). The body now states how the title's
    last clause is read: no action of the agent is best against every
    profile of the others' simultaneous actions. The old promote_when: A
    checked re-derivation recorded in this file of the sufficiency step
    (made in NOTE-1154) and of the two matrix examples, the additive
    impossibility for [[0, 1], [1, 8]] and the monotonic impossibility for
    [[2, 1], [1, 8]], which ADR-047 counts toward promotion. It is refuted
    by a non-decreasing mixing whose greedy profile is not a joint
    maximiser, or by a monotonic mixing of per-agent values that
    represents a payoff in which an agent's best action depends on the
    others' simultaneous actions. Nothing about StarCraft performance
    bears on it.
tags:
- game-theory
- learning-theory
date: '2026-10-24'
source:
- LIT-1503
- LIT-1510
summary: >-
  Rashid et al.'s QMIX (ICML 2018), read in full in [NOTE-1154](../notes.d/NOTE-1154.md), with
  QTRAN ([NOTE-1141](../notes.d/NOTE-1141.md)) for the strictness. Monotonicity is sufficient for
  the greedy-profile property and not necessary. It presupposes a real-
  valued joint value: what it adds is that each member's ranking of its
  own actions agrees with the collective's whatever the others do, an
  ordinal separability condition. It is Wolpert and Tumer's factoredness
  stated for values.
---
<!-- inactive-ok-file: NOTE-1154 NOTE-1141 — the readings this is filed from, named -->

# THEORY-929: A joint action-value that is a non-decreasing function of per-agent values, each conditioning only on its agent's own history, makes the profile of the agents' individually greedy actions a greedy joint action, which suffices for decentralised greedy execution and is strictly more expressive than a sum; it cannot represent a joint value in which an agent's best action depends on what the others do at the same step

## Source

Rashid, Samvelyan, Schroeder de Witt, Farquhar, Foerster & Whiteson,
[LIT-1503](../literature.d/LIT-1503.md), read in [NOTE-1154](../notes.d/NOTE-1154.md) from arXiv:1803.11485v2: Eqs. 4–5
(p. 4), section 4.1, supplement A (Table 3) and the two-step game
(Tables 1–2, supplement B). Strictness against IGM from Son et al.,
[LIT-1510](../literature.d/LIT-1510.md) ([NOTE-1141](../notes.d/NOTE-1141.md)).

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
  without monotonicity ([THEORY-933](THEORY-933.md)).
- **Anything under partial observability beyond a remark.** The paper says
  QMIX "cannot necessarily represent the value function" there.

## Note of 2026-10-30: the second check

The second check at the status review (ADR-065 §5) followed each step.

Sufficiency. Let ū^a maximise Q_a. For any joint action u, Q_a(ū^a) ≥
Q_a(u^a) for each a, and raising the arguments of a non-decreasing f one
at a time from Q(u) to Q(ū) never lowers it, so f(Q(ū)) ≥ f(Q(u)). With
ties the greedy profile may be one maximiser among several.

More than a sum. [[0, 1], [1, 8]] is monotonic: Q_1 = Q_2 = (0, 1) with
f(x, y) = x + y + 6xy, which is non-decreasing on [0, 1]², gives 0, 1, 1
and 8. A sum would need a₂ + b₂ = (a₁ + b₂) + (a₂ + b₁) − (a₁ + b₁) = 1 +
1 − 0 = 2, not 8.

Not every payoff. In [[2, 1], [1, 8]], suppose Q_1(A) ≤ Q_1(B). Then
f(Q_1(A), Q_2(A)) ≤ f(Q_1(B), Q_2(A)), which contradicts 2 > 1, so
Q_1(A) > Q_1(B). The same argument with the partner at B and 8 > 1 gives
Q_1(B) > Q_1(A).

The last clause of the title is read as: no action of the agent is best
against every profile of the others' simultaneous actions. So read, it
holds in general. Let x* maximise Q_a. If some action y did strictly
better than x* against some profile of the others, monotonicity would
force Q_a(y) > Q_a(x*). A weaker dependence, in which an action is best
everywhere but ties with another somewhere, is not what the clause
excludes.

A script (numpy, in the session's scratchpad) checked these steps. In 2000
random non-decreasing mixings of two or three agents, the greedy profile
was always a joint maximiser; as a control, a mixing decreasing in one
argument failed in 200 of 200 cases. A search over row and column
orderings found [[0, 1], [1, 8]] monotonic and not additive, and [[2, 1],
[1, 8]] not monotonic. In 3000 random 3 × 3 payoffs with integer values
from 0 to 3, ties included, none was monotonically representable unless
each agent had an action best against every action of the other; 2520 had
no such action.
