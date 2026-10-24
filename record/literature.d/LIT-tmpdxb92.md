---
status: Active
status_note: >-
  read in full 2026-10-24 ([NOTE-tmphgg8m](../notes.d/NOTE-tmphgg8m.md)) from arXiv v6 (21 July 2026, CC
  BY 4.0); worth reading as a proved aggregation result: in an infinite,
  well-mixed population, two imitation rules with no individual learning
  have the expected update of a single bandit-learning agent. Imitation of
  success gives Cross Learning (the Taylor replicator dynamic), the honey-bee
  weighted voter model gives what the authors call Maynard-Cross Learning
  (the Maynard-Smith replicator dynamic). The macro-agent is a stateless
  bandit policy over the members' types. The biological model is
  deliberately partial, the simulations qualitative, and pure imitation has
  no way back once a type is lost or the environment changes.
title: 'The Hive Mind is a Single Reinforcement Learning Agent'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Filed and read at the owner's request ("read and file this paper"),
    2026-10-24. Read in full from arXiv:2410.17517v6 (21 July 2026), the
    latest of six versions (v1 23 October 2024), licence CC BY 4.0, a
    31-page PDF extracted by pdftotext: abstract, sections 1–4, appendices
    A (proofs, checked line by line) and B (simulation details and
    figures, read from the text and captions). Not read: the reference list
    (skimmed), and the version of record in Swarm Intelligence
    (doi:10.1007/s11721-026-00264-7, published 17 October 2026 per
    Crossref), which was not sought; whether it differs from v6 is not
    known. `published:` is v1's date under ADR-002.
tags:
- complex-systems
- learning-theory
- game-theory
- agency
- anthology-candidate
date: '2026-10-24'
published: '2024-10-23'
arxiv: '2410.17517'
doi: '10.1007/s11721-026-00264-7'
first_author: 'Soma'
keywords:
- 'collective decision-making'
- 'weighted voter model'
- 'replicator dynamic'
- 'Cross Learning'
- 'multi-armed bandit'
- 'honey bee nest-site selection'
- 'imitation of success'
implementations:
- 'https://github.com/MISTLab/HiveMindRL'
summary: >-
  Soma, Bouteiller, Hamann and Beltrame show that in an infinite,
  well-mixed population, imitation of success has the expected update of a
  single Cross Learning bandit agent, and the weighted voter model of the
  honey-bee waggle dance the expected update of "Maynard-Cross Learning",
  π_a ← π_a + (r_k / v^π)(1[a = k] − π_a), which is the Maynard-Smith
  replicator dynamic. Each member is one parallel action sample of the
  population's policy, and the members themselves do not learn.
  Simulations, qualitative by the authors' account, show the result
  surviving moderate swarm and neighbourhood sizes, and finite
  populations losing options for good.
---
<!-- inactive-ok-file: NOTE-tmphgg8m THEORY-tmp3oyxw THEORY-tmp9g2s5 — filed from this reading, named -->

# LIT-tmpdxb92: The Hive Mind is a Single Reinforcement Learning Agent

Soma, Bouteiller, Hamann & Beltrame (2024; Swarm Intelligence 2026) —
[arXiv:2410.17517](https://arxiv.org/abs/2410.17517)

## Key takeaways

- **The equivalence.** Imitation of success aggregates into the Taylor
  replicator dynamic, which is the expected Cross Learning update
  (Proposition 1, which the authors call a consequence of known results).
  The weighted voter model aggregates into the Maynard-Smith replicator
  dynamic, the expected update of Maynard-Cross Learning (Proposition 2,
  the main result). The population vector and the policy are the same
  point on the simplex ([THEORY-tmp3oyxw](../theory.d/THEORY-tmp3oyxw.md)).
- **No member learns.** In the weighted voter model a bee broadcasts its
  type in proportion to its own quality sample and adopts the first type it
  perceives. "In the weighted voter model the individual bee itself is not
  modeled as an RL agent: it only “blindly” imitates its peers, irrespective
  of their payoffs!" (p. 10).
- **Members are parallel samples.** α = 1/N plays the part of a learning
  rate, so a large swarm is a bandit learner evaluating its policy in N
  environments at once.
- **Limits.** The model omits spontaneous commitment, stop signals, direct
  switches and quorum sensing. Simulations are "interpreted qualitatively
  rather than quantitatively" (p. 13). Finite populations can lose a type
  entirely, and pure imitation gives no way to re-explore after the
  environment changes ([THEORY-tmp9g2s5](../theory.d/THEORY-tmp9g2s5.md)).

## Why this is here

Read at the owner's request on 2026-10-24. It is a demonstrated case of an
organized whole that learns as one agent with no learning member, which
bears on the distributed-agency line, on [THEORY-043](../theory.d/THEORY-043.md)'s mind of mindless
agents, and on [CLAIM-tmp0qupq](../claims.d/CLAIM-tmp0qupq.md)'s learned prior ([NOTE-tmphgg8m](../notes.d/NOTE-tmphgg8m.md)). It carries
`anthology-candidate` because the authors offer it for designing collective
RL systems. It carries no instruction for ML practice.
