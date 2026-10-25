---
status: Active
status_note: >-
  read in full 2026-10-24 ([NOTE-tmpoitn8](../notes.d/NOTE-tmpoitn8.md)) from arXiv v2 (6 June 2018, the
  ICML camera-ready, arXiv non-exclusive licence); worth reading for one
  structural condition: if the joint action-value is non-decreasing in
  each agent's own value, the profile of individually greedy actions is a
  greedy joint action, so a collective can act on a common value while
  each member consults only its own. The condition is sufficient, not
  necessary, and it cannot represent a joint value in which one agent's
  best action depends on what the others do at the same step. Its
  evidence is a two-step matrix game and StarCraft II win rates on six
  small maps.
title: 'QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Filed and read 2026-10-24, registered with works from multi-agent
    reinforcement learning after the owner asked how the record stands on
    MARL. Citation checked against the arXiv abstract page: Rashid,
    Samvelyan, Schroeder de Witt, Farquhar, Foerster & Whiteson,
    Proceedings of the 35th International Conference on Machine Learning,
    PMLR 80, 2018 (arXiv comment "Camera-ready version"). PMLR issues no
    DOI and Crossref has no record. `published:` is arXiv v1, 30 March
    2018, under ADR-002. Read from arXiv:1803.11485v2 (6 June 2018), a
    14-page PDF (8 pages and a 6-page supplement) extracted by pdftotext;
    the learning-curve figures were read from their captions and the text.
tags:
- game-theory
- learning-theory
- anthology-candidate
date: '2026-10-24'
published: '2018-03-30'
arxiv: '1803.11485'
first_author: 'Rashid'
keywords:
- 'multi-agent reinforcement learning'
- 'value function factorisation'
- 'monotonicity'
- 'mixing network'
- 'hypernetworks'
- 'centralised training with decentralised execution'
- 'StarCraft II'
implementations: []
summary: >-
  Rashid et al. represent a team's joint action-value Q_tot as a mixing of
  per-agent values Q_a(τ^a, u^a) constrained by ∂Q_tot/∂Q_a ≥ 0, with
  non-negative mixing weights produced from the global state by
  hypernetworks. Monotonicity makes the joint argmax the profile of
  individual argmaxes, so execution is decentralised and maximisation is
  linear in the number of agents. It represents more than a sum (VDN),
  learning the optimal policy of a two-step game VDN misses, and beat VDN
  and independent Q-learning on six StarCraft II maps; it cannot represent
  joint values in which an agent's best action depends on the others'.
---
<!-- inactive-ok-file: THEORY-tmp56jxv — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: CLAIM-436 CLAIM-440 — Proposed; the claims this reading bears on, named, nothing here rests on them -->

# LIT-tmp3ztxf: QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning

Rashid, Samvelyan, Schroeder de Witt, Farquhar, Foerster & Whiteson (2018),
ICML — arXiv:1803.11485

## Key takeaways

- **The condition.** "We only need to ensure that a global argmax
  performed on Qtot yields the same result as a set of individual argmax
  operations performed on each Qa" (p. 2), and monotonicity,
  ∂Q_tot/∂Q_a ≥ 0, is one way to ensure it. The authors call such
  functions "sufficient but not necessary to satisfy (4)" (p. 4).
- **The state enters non-monotonically.** Mixing weights are generated
  from the state by hypernetworks with an absolute-value activation, so the
  state can reshape the mixing freely while each agent's value can only
  push the total up.
- **What it cannot represent.** "any value function for which an agent's
  best action depends on the actions of the other agents at the same time
  step will not factorise appropriately" (p. 5). The supplement's example
  is the payoff matrix [[2, 1], [1, 8]] (Table 3b).
- **Two-step game.** QMIX learned the payoffs of state 2B exactly
  (0, 1, 1, 8) and the optimal return of 8; VDN learned −1.87 … 6.51 and
  took the suboptimal 7 (Table 2).
- **StarCraft II.** QMIX was strongest on six maps, with its largest
  margins on heterogeneous teams; ablations show both state conditioning
  and non-linear mixing are needed there (Figures 3–4).

## Why this is here

Registered 2026-10-24 by the lead as "a precise condition for a collective
common currency" bearing on [CLAIM-436](../claims.d/CLAIM-436.md) and [CLAIM-440](../claims.d/CLAIM-440.md). The reading supports
a narrower statement ([NOTE-tmpoitn8](../notes.d/NOTE-tmpoitn8.md)). Monotonic mixing is a condition
under which a collective's ordering of joint actions is consistent with
each member's ordering of its own, given its local information. It is a
separability condition, not a currency condition: Q_tot is already a
real-valued function, so the currency is assumed, and what monotonicity
adds is that each member's ranking of its own actions does not depend on
the others' actions. That is the condition under which [CLAIM-440](../claims.d/CLAIM-440.md)'s
negotiation would never need to be had at execution time. QTRAN
([LIT-tmpev178](LIT-tmpev178.md)) shows the argmax condition itself is weaker. Filed as
[THEORY-tmp56jxv](../theory.d/THEORY-tmp56jxv.md). It carries `anthology-candidate` as a multi-agent RL
method and no instruction for practice here.
