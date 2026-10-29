---
status: Active
status_note: >-
  read in full 2026-10-29 (NOTE-tmpohrox) from arXiv v1; worth reading as
  the first method to learn a causal abstraction map from paired
  interventional samples without the structural equations, and for what
  it shows unintentionally: its do-calculus term is constant on the
  feasible set as written, so its gains come from an
  intervention-compatibility cost.
title: 'Causal Optimal Transport of Abstractions'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A7 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is arXiv v1 2023-12-13 (CLeaR 2024,
    PMLR 236) (ADR-002).
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full from arXiv 2312.08107v1 (13 December 2023), the only
    arXiv version, 31 pp. (NOTE-tmpohrox); the CLeaR proceedings version
    was not read. Status Deferred → Active; summary rewritten from the
    text and corrected: the exchange's description had the do-calculus
    constraints doing the causal work, and as written they cannot
    (THEORY-tmp1lvzk). The citation stands.
tags:
- causality
- mathematics
date: '2026-10-29'
published: '2023-12-13'
arxiv: '2312.08107'
first_author: 'Felekis'
keywords:
- 'causal abstraction'
- 'structural causal models'
- 'multi-marginal optimal transport'
- 'interventional data'
implementations: []
summary: >-
  Felekis et al. (2023; CLeaR 2024). COTA learns a stochastic map from a
  low-level causal model's states to a high-level one's, given both DAGs,
  the map between their interventions and samples of each paired
  interventional distribution, without the structural equations. It
  solves one entropic optimal-transport problem per intervention, with a
  cost that rewards states compatible with the same paired interventions
  and a term meant to impose do-calculus relations between the plans.
  As written that term depends only on the plans' marginals, which the
  transport constraints fix, so it is constant on the feasible set. The
  reported gains over non-causal transport come from the compatibility
  cost, and reverse when the intervention set is small.
---

# LIT-tmpdrddx: Causal Optimal Transport of Abstractions

Felekis, Y., Zennaro, F. M., Branchini, N., & Damoulas, T. (2024). Causal optimal transport of abstractions. *CLeaR 2024*, PMLR 236, 462–498.

## Why this is here

A7's bridge between pragmatic transport and distributed agency: a correspondence that respects interventions, not only observations, so that systems matched on relational statistics but different under perturbation are told apart ([CLAIM-414](../claims.d/CLAIM-414.md), [CASE-179](../cases.d/CASE-179.md), [THEORY-849](../theory.d/THEORY-849.md)). A good abstraction still does not settle constitution ([CLAIM-150](../claims.d/CLAIM-150.md)).

The reading (NOTE-tmpohrox) corrects this in part. COTA does fit every
paired interventional distribution, not only the observational one, so a
held-out intervention can expose a bad map. But it assumes the two models
are related and learns a map; it does not tell systems apart. Its target
notion is Rubenstein et al.'s one-distribution exact transformation,
relaxed and made stochastic, which is weaker than THEORY-849's reading of
causal abstraction and open to CLAIM-399's objection. And its do-calculus
term, the part said to carry the causal structure, is inert as written
(THEORY-tmp1lvzk).
