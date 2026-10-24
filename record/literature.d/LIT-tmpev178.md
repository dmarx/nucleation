---
status: Active
status_note: >-
  read in full 2026-10-24 (NOTE-tmp457xj) from arXiv v1 (14 May 2019, the
  ICML version with its supplement, arXiv non-exclusive licence); worth
  reading for the Individual-Global-Max condition, that the agents'
  individually greedy actions form a greedy joint action, and for showing
  it strictly weaker than additive or monotonic factorisation. The
  authors' own supplement notes that every single-state matrix game
  satisfies it, so IGM has bite only where each agent sees part of the
  state; it is a condition on whether members acting on local information
  can jointly reach the collective optimum, not a condition for a common
  currency. Evidence is matrix games, Gaussian squeeze and a predator-prey
  variant.
title: 'QTRAN: Learning to Factorize with Transformation for Cooperative Multi-Agent Reinforcement Learning'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Filed and read 2026-10-24, registered for its Individual-Global-Max
    condition with works from multi-agent reinforcement learning after the
    owner asked how the record stands on MARL. Citation checked against the
    arXiv abstract page: Son, Kim, Kang, Hostallero & Yi, Proceedings of
    the 36th International Conference on Machine Learning, PMLR 97, 2019
    (arXiv comment "Accepted to ICML 2019"). PMLR issues no DOI.
    `published:` is arXiv v1, 14 May 2019, the only version. Read from
    arXiv:1905.05408v1, an 18-page PDF (main text and supplement)
    extracted by pdftotext, the supplement's proofs also read from a
    layout extraction; figures read from captions.
tags:
- game-theory
- learning-theory
- anthology-candidate
date: '2026-10-24'
published: '2019-05-14'
arxiv: '1905.05408'
first_author: 'Son'
keywords:
- 'multi-agent reinforcement learning'
- 'value function factorization'
- 'Individual-Global-Max'
- 'IGM'
- 'centralized training with decentralized execution'
- 'non-monotonic games'
implementations:
- 'https://github.com/Sonkyunghwan/QTRAN'
summary: >-
  Son, Kim, Kang, Hostallero & Yi define Individual-Global-Max (IGM): a
  joint action-value is factorised by per-agent values when the joint
  argmax is the profile of individual argmaxes. Additivity (VDN) and
  monotonicity (QMIX) are sufficient for it; QTRAN instead trains the sum
  of individual values plus a state value to equal the joint value at the
  greedy profile and to bound it elsewhere (Theorem 1), a condition also
  necessary up to positive rescaling. On 310 random 3×3 matrix games it
  learned the optimum in all, VDN and QMIX failed in 177; it also did
  better on Gaussian squeeze and a penalised predator-prey task.
---
<!-- inactive-ok-file: THEORY-tmpayfgm — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: CLAIM-403 CLAIM-436 CLAIM-440 — Proposed; the claims this reading bears on, named, nothing here rests on them -->

# LIT-tmpev178: QTRAN: Learning to Factorize with Transformation for Cooperative Multi-Agent Reinforcement Learning

Son, Kim, Kang, Hostallero & Yi (2019), ICML — arXiv:1905.05408

## Key takeaways

- **IGM.** Individual value functions [Q_i] "satisfy IGM" for Q_jt when
  argmax over joint actions of Q_jt equals the vector of each agent's
  argmax of Q_i (Definition 1). "Simply put, the optimal joint actions
  across agents are equivalent to the collection of individual optimal
  actions of each agent" (p. 3).
- **Additivity and monotonicity are only sufficient.** "Additive
  decomposability and monotonicity are only sufficient — somewhat
  excessively restrictive — for factorizability" (p. 1).
- **A condition that is sufficient and, up to rescaling, necessary.**
  Σ_i Q_i(u_i) − Q_jt(u) + V_jt equals 0 at the greedy profile and is
  ≥ 0 elsewhere (Theorem 1, proof re-derived when read); a stronger
  variant (Theorem 2) keeps the transformed value tracking the joint one
  for non-optimal actions.
- **IGM is cheap in single-state games.** "Since matrix games always
  satisfy IGM conditions, QTRAN-base always trains the optimal action for
  all 310 cases" (supplement, p. 17). VDN and QMIX matched it in 114 and
  fell short in 177.
- **Non-monotonic tasks.** In predator-prey with a penalty P for a lone
  capture, the gap to VDN and QMIX widened as P grew; with four predators
  and P ≥ 1 they learned to avoid the prey (Figure 4).

## Why this is here

Registered 2026-10-24 by the lead for IGM as "a precise condition for a
collective common currency" (CLAIM-436, CLAIM-440). The reading narrows
that (NOTE-tmp457xj). IGM presupposes a real-valued joint value Q_jt, so it
is not a condition for a currency; it is a condition for decentralising a
currency already given. And because any single-state game with a unique
optimum satisfies it, its content lies in partial observability: whether
each member's local view suffices to pick its part of the collective
optimum. Its nearest record analogue is legibility and access (CASE-124,
CLAIM-403), not ordering. Filed as THEORY-tmpayfgm. It carries
`anthology-candidate` as a multi-agent RL method and no instruction for
practice here.
