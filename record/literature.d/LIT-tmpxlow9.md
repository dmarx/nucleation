---
status: Active
status_note: >-
  read in full 2026-10-24 ([NOTE-tmp8ra24](../notes.d/NOTE-tmp8ra24.md)) from arXiv:nlin/0204057v2 (18 August
  2002); worth reading as a four-page derivation of the learning dynamics
  of softmax reinforcement learners with forgetting: two such agents follow
  coupled replicator equations plus a term α_X Σ_j x_j log(x_j/x_i), set by
  the rate at which reward memories decay, that pushes each agent towards
  uniform play. Without forgetting the system is conservative, Hamiltonian
  in zero-sum games, and in rock–scissors–paper it is chaotic for nonzero
  tie rewards; with forgetting it is dissipative, with limit cycles and
  chaotic attractors. The memory update is not Watkins's Q-learning: every
  action's memory is updated with its average reward at the same rate.
title: 'Coupled replicator equations for the dynamics of learning in multiagent systems'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Filed and read 2026-10-24 for the owner's question how the record
    stands on multi-agent reinforcement learning. Citation checked against
    Crossref (doi:10.1103/PhysRevE.67.015206): Yuzuru Sato and James P.
    Crutchfield, Physical Review E 67(1), article 015206, published online
    31 January 2003. Read in full from arXiv:nlin/0204057v2 (v1 24 April
    2002, v2 18 August 2002; Santa Fe Institute Working Paper 02-04-017),
    4 pp., under arXiv's default licence, extracted by pdftotext. The
    version of record was not read, so differences from v2 are not known.
    `published:` is v1's date under ADR-002. A grep of
    record/literature.d for the DOI, the arXiv id and "Crutchfield" with
    "replicator" found nothing; the record holds other Crutchfield papers
    on computational mechanics.
tags:
- game-theory
- learning-theory
- complex-systems
- anthology-candidate
date: '2026-10-24'
published: '2002-04-24'
arxiv: 'nlin/0204057'
doi: '10.1103/PhysRevE.67.015206'
first_author: 'Sato'
keywords:
- 'coupled replicator equations'
- 'multiagent reinforcement learning'
- 'Boltzmann action selection'
- 'memory decay'
- 'rock-scissors-paper'
- 'Hamiltonian chaos'
- 'deterministic chaos'
- 'collective learning dynamics'
implementations: []
summary: >-
  Sato & Crutchfield (2002; PRE 2003). Two agents choose by softmax over
  reward memories Q_i that decay at rate α. In the limit where learning is
  slow relative to play, each agent's choice distribution follows
  ẋ_i/x_i = β[(Ay)_i − x·Ay] + α Σ_j x_j log(x_j/x_i): a coupled
  replicator dynamic plus an entropy-like term towards uniform play. With
  α = 0 it is the conservative two-population replicator equation; with
  α > 0 it is dissipative. In rock–scissors–paper, simulations show
  quasiperiodic tori and Hamiltonian chaos without decay, and limit cycles,
  intermittency and chaotic attractors with it.
---
<!-- inactive-ok-file: NOTE-tmp8ra24 THEORY-tmp3wkwk THEORY-tmpev90a — filed from this reading, named -->

# LIT-tmpxlow9: Coupled replicator equations for the dynamics of learning in multiagent systems

Sato, Y. & Crutchfield, J. P. (2003). Coupled replicator equations for the
dynamics of learning in multiagent systems. *Physical Review E* 67:
015206. doi:10.1103/PhysRevE.67.015206. arXiv:nlin/0204057.

## Key takeaways

*From the reading, [NOTE-tmp8ra24](../notes.d/NOTE-tmp8ra24.md). Page numbers are arXiv v2's.*

- **Learning gives a game dynamics.** Two agents with no model of each
  other, each choosing by softmax over decaying reward memories, follow
  coupled replicator equations in the slow-learning limit. The agents
  "have no knowledge of a “game” in which they are playing", yet a game
  dynamics emerges (p. 2).
- **Forgetting is an entropy term.** Memory decay at rate α adds
  α Σ_j x_j log(x_j/x_i) to each action's growth rate, a pull towards
  uniform play. With α = 0 the system is the conservative multipopulation
  replicator equation, Hamiltonian in zero-sum games, and the time average
  of an interior orbit is the Nash equilibrium. With α > 0 phase volume
  contracts at rate (N − 1)(α_X + α_Y) ([THEORY-tmp3wkwk](../theory.d/THEORY-tmp3wkwk.md)).
- **Chaos in a three-action game.** Rock–scissors–paper with tie reward
  ε: tori and Hamiltonian chaos when the game is zero-sum, transients to
  heteroclinic cycles when it is not, and with decay limit cycles and
  chaotic attractors, the largest Lyapunov exponent positive over a large
  part of the ε_Y range ([THEORY-tmpev90a](../theory.d/THEORY-tmpev90a.md)).
- **Not Watkins's Q-learning.** Every action's memory is updated each step
  with its average reward. That is the full-information case the
  selection–mutation model of Q-learning assumes, not the case in which only
  the chosen action is updated ([NOTE-tmp43vkx](../notes.d/NOTE-tmp43vkx.md)).

## Why this is here

Filed 2026-10-24 when the owner asked how the record stands on multi-agent
reinforcement learning. It is the learning-side derivation of the coupled
dynamics the record's replicator reading of authority uses ([CLAIM-444](../claims.d/CLAIM-444.md)),
it shows that forgetting enters those dynamics as a force towards equal
shares, and it is a demonstrated case of cycles and chaos produced by
self-interested learners with no switching of regime ([CLAIM-451](../claims.d/CLAIM-451.md)). It
carries `anthology-candidate` because it is offered as a framework for
analysing multi-agent learning systems. It carries no instruction for ML
practice.
