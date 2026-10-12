---
status: Deferred
status_note: 'filed 2026-10-12 from the owner''s papers-feed, not read. Registered for [QUESTION-008](../questions.d/QUESTION-008.md), where it makes bisimulation distances between Markov chains measurable from sample trajectories alone. No NOTE is filed, and it stays Deferred until it is read, not on merit.'
title: 'Distances for Markov chains from sample streams'
version: 1
history:
- version: 1
  date: '2026-10-12'
  note: >-
    Filed, not read. Found in the owner's papers-feed snapshot of 2026-10-11 by embedding similarity to QUESTION-008
    and judged from the abstract. Citation checked against arXiv and Crossref on 2026-10-12: Sergio Calo, Anders
    Jonsson, Gergely Neu et al., arXiv:2505.18005, Advances in Neural Information Processing Systems 38 (NeurIPS
    2025), submitted 2025-05-23, which is the `published:` date. Not held in the Anthology of the SOTA: a grep of its
    record/ (clone at commit d8b5ba5) for the identifier and title found nothing.
tags:
- mathematics
- probabilistic-modeling
- anthology-candidate
date: '2026-10-12'
published: '2025-05-23'
arxiv: '2505.18005'
doi: '10.52202/085713-4493'
first_author: 'Calo'
keywords:
- 'bisimulation metrics'
- 'Markov chains'
- 'optimal transport'
- 'stochastic optimization'
- 'sample complexity'
implementations: []
summary: >-
  Calo et al. (2025). The paper gives a stochastic optimization method that estimates bisimulation metrics between
  Markov chains from sample trajectories, without a model of the transition dynamics. The method rests on a new
  linear-programming formulation of bisimulation metrics, solved by a stochastic primal-dual method. It gives
  sample-complexity guarantees and an empirical evaluation. Not read.
---
<!-- inactive-ok-file: QUESTION-008 — Deferred; the question this work was filed for, on a set-aside line -->

# LIT-tmp82q00: Distances for Markov chains from sample streams

Sergio Calo, Anders Jonsson, Gergely Neu, Ludovic Schwartz and Javier Segovia-Aguas (2025), *Advances in Neural Information Processing Systems 38* (NeurIPS 2025).

Filed for [QUESTION-008](../questions.d/QUESTION-008.md): a way to estimate bisimulation distances between Markov chains from sample streams alone. That would make approximate bisimulation measurable for systems whose update structure is not known.

*Seeded from the abstract, not a reading. A reading should check the claim above first.*
