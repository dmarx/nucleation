---
number: 905
status: Proposed
formerly:
- THEORY-tmp9g2s5
promote_when: >-
  The authors' simulations (code at github.com/MISTLab/HiveMindRL) re-run
  or the version of record read, and an analysis of finite populations of
  pure imitators showing that a type absent from the population cannot
  return under either protocol, so that convergence after a change of the
  environment depends on a mechanism outside them. It is refuted by a pure
  imitation protocol of the kind studied that re-explores lost options
  without mutation, spontaneous commitment or heterogeneity.
title: 'In simulations of the two imitation protocols, populations small enough to be finite often settle on a suboptimal option because pure imitation can remove a type entirely, and once settled the protocols give no way to re-explore when the environment changes; variants in which members compare quality estimates converge faster than blind weighted voting, at the cost of more communication and comparison'
version: 1
tags:
- complex-systems
- learning-theory
date: '2026-10-24'
source:
- LIT-1484
summary: >-
  Soma et al.'s simulations and limits section, read in [NOTE-1132](../notes.d/NOTE-1132.md).
  With ten options and arbitrary parameters that the authors call
  qualitative, swarms of about 500 track the replicator dynamic and
  smaller ones often lock onto worse options. The authors state that pure
  imitation can delete a type and has no mechanism for escape in
  non-stationary environments. Hybrids that compare qualities are faster.
  Simulation-scoped, not a theorem.
---
<!-- inactive-ok-file: THEORY-899 — the reading and its companion THEORY -->

# THEORY-905: In simulations of the two imitation protocols, populations small enough to be finite often settle on a suboptimal option because pure imitation can remove a type entirely, and once settled the protocols give no way to re-explore when the environment changes; variants in which members compare quality estimates converge faster than blind weighted voting, at the cost of more communication and comparison

## Source

Soma et al., [LIT-1484](../literature.d/LIT-1484.md), read in [NOTE-1132](../notes.d/NOTE-1132.md): sections 4.2, 4.5 and
4.9.3 (pp. 12–14, 18), Figures 2b and 2d, appendix B.8.

## What was actually shown

- **Finite size.** Ten options, 1000 seeds. N = 500 follows the replicator
  dynamic, and "a number of scout bees that is too small often yields
  convergence to a sub-optimal nest site option" (p. 13). The parameters
  are arbitrary and the result qualitative by the authors' account.
- **No way back.** "Pure imitation can lead to situations in which a given
  type ceases to exist entirely in a finite population", and the protocols
  "don't provide a mechanism for escaping these strategies later on in
  non-stationary environments" (p. 18). Real colonies use spontaneous
  commitment, persistent stochastic allocation, or wandering workers.
- **Speed against bandwidth.** Three hybrids in which members compare
  qualities beat the weighted voter rule (Fig. 2d). The authors suggest
  blind imitation "uses minimal communication and cognition bandwidth"
  (p. 14), as an explanation, not a measurement.

## What it does not show

A general result for finite populations; the no-escape point is argued
from the protocol's structure, not proved. Nor anything about real bees,
whose nest-site process includes the mechanisms the model omits.
