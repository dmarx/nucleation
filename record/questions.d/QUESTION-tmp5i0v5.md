---
status: Open
title: 'Does keeping a maintained organization precise cost dissipation in proportion to the precision, so that how exactly a self-maintaining structure holds its state is bounded by what it spends, and does that bound separate organizations that persist from structures that merely last?'
version: 1
tags:
- thermodynamics
- complex-systems
date: '2026-11-11'
line:
- distributed-agency
summary: >-
  Raised by the second by-topic reading review of 2026-11-11 ([ADR-091](../decisions.d/ADR-091.md),
  [ADR-tmpkuzwl](../decisions.d/ADR-tmpkuzwl.md)). The record holds five readings in stochastic
  thermodynamics that no claim uses, and its claims on maintained
  organization ([CLAIM-604](../claims.d/CLAIM-604.md), [CLAIM-516](../claims.d/CLAIM-516.md), [CLAIM-521](../claims.d/CLAIM-521.md)) speak of upkeep drawn
  from a flux without pricing it. The thermodynamic uncertainty relation
  ([THEORY-1268](../theory.d/THEORY-1268.md)) prices a precise current in dissipation; the question asks
  whether that price applies to an organization's maintenance and whether
  it tells a maintained organization from a structure that merely decays
  slowly. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: ADR-091 ADR-tmpkuzwl — Proposed; the reading review that raised it -->

# QUESTION-tmp5i0v5: Does keeping a maintained organization precise cost dissipation in proportion to the precision, so that how exactly a self-maintaining structure holds its state is bounded by what it spends, and does that bound separate organizations that persist from structures that merely last?

## Why it is a question

The record's maintained organizations draw their upkeep from a flux.
[CLAIM-604](../claims.d/CLAIM-604.md) gives a structure repaired at a rate proportional to its intact
share an ignition threshold and a supply level below which it goes out.
[CLAIM-516](../claims.d/CLAIM-516.md) says a capacity that persists, where every capacity turns over,
needs a cycle in its production graph. [CLAIM-521](../claims.d/CLAIM-521.md) says an organization's
present coupling need not reveal the stability of the process maintaining
it. None of them says what the maintenance costs, or whether its cost
limits how exactly the organization holds its state.

Stochastic thermodynamics has results that would say so:

- **The thermodynamic uncertainty relation** ([THEORY-1268](../theory.d/THEORY-1268.md)): in a
  nonequilibrium steady state, a current precise to ε costs at least
  2k_BT/ε² of dissipation. If an organization's maintenance is such a
  current, its precision has a price.
- **Heat against reversal** ([THEORY-679](../theory.d/THEORY-679.md)): the heat a transition releases
  is bounded below by the log-odds against its reversal, and for a
  replicator the bound grows with the copy's durability and the speed of
  copying.
- **The thermodynamic space of a driven network** ([THEORY-1261](../theory.d/THEORY-1261.md)): at
  stationarity each reaction's affinity is bounded by the cycle affinities
  of the extremal pathways; without driving the space collapses to
  equilibrium.
- **Fluctuation theorems** ([THEORY-431](../theory.d/THEORY-431.md)): they constrain fluctuations of
  entropy production, not which steady state a system reaches.
- **Driven outcomes** ([THEORY-831](../theory.d/THEORY-831.md)): under a protocol fixed in advance, the
  log-odds of two outcomes split into state counts, reversal probabilities
  and the heat of the paths reaching them.

## Why it is open here

Two things are not settled. Whether an organization's maintenance is a
current in the relation's sense: [CLAIM-604](../claims.d/CLAIM-604.md)'s repair flux is a rate, but
the relation needs a counted current in a thermodynamically consistent
Markov network. And whether the bound discriminates: a structure that
lasts because it decays slowly ([CLAIM-604](../claims.d/CLAIM-604.md)'s metastable case, [THEORY-1273](../theory.d/THEORY-1273.md))
may hold its state precisely at small cost, which would make precision a
poor mark of maintenance.

## What would count as an answer

- A mapping of one of the record's maintained organizations ([CLAIM-604](../claims.d/CLAIM-604.md)'s
  flame, [CLAIM-516](../claims.d/CLAIM-516.md)'s capacities) onto a Markov network in which its
  maintenance is a current, with the relation's bound computed for it.
- Or an argument that maintenance is not a current in that sense, so the
  bound does not apply.
- Either way, a comparison with a slowly decaying structure of the same
  state precision, showing whether the bound tells them apart.
