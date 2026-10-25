---
number: 899
status: Proposed
formerly:
- THEORY-tmp3oyxw
promote_when: >-
  A checked re-derivation recorded in this file, which the reading made
  (NOTE-1132) and which ADR-047 counts toward promotion, together
  with the version of record (Swarm Intelligence 2026) read and found to
  state the same propositions. It is refuted if the expected one-step
  change of the population vector under either protocol, with infinite
  population, large well-mixed neighbourhoods and evaluation decoupled
  from imitation, differs from the stated replicator dynamic. The title
  claims nothing about real swarms or about agency beyond the identity of
  expected updates; a result about those neither promotes nor refutes it.
title: 'In an infinite, well-mixed population whose members each sample the quality of their own type, imitation of success has the expected update of a single Cross Learning bandit agent (the Taylor replicator dynamic), and the weighted voter model, in which members broadcast their type in proportion to their sample and adopt the first type they perceive, has the expected update of Maynard-Cross Learning, π_a ← π_a + (r_k / v^π)(1[a = k] − π_a), the Maynard-Smith replicator dynamic; the population vector is the policy and no member learns'
version: 1
tags:
- learning-theory
- complex-systems
- game-theory
date: '2026-10-24'
source:
- LIT-1484
summary: >-
  Soma et al.'s Propositions 1 and 2, read in full from arXiv v6 in
  [NOTE-1132](../notes.d/NOTE-1132.md), with both proofs and the aggregation in Eqs. 8–14
  re-derived. An exact identity of expected updates under idealizing
  assumptions: infinite N, large well-mixed neighbourhoods, and imitation
  decoupled from evaluation. Each member is one parallel action sample,
  α = 1/N plays the learning rate, and the macro-policy is a stateless
  bandit policy over the members' types.
supports:
- CLAIM-444
---
<!-- inactive-ok-file: NOTE-1132 — the reading this is filed from -->

# THEORY-899: In an infinite, well-mixed population whose members each sample the quality of their own type, imitation of success has the expected update of a single Cross Learning bandit agent (the Taylor replicator dynamic), and the weighted voter model, in which members broadcast their type in proportion to their sample and adopt the first type they perceive, has the expected update of Maynard-Cross Learning, π_a ← π_a + (r_k / v^π)(1[a = k] − π_a), the Maynard-Smith replicator dynamic; the population vector is the policy and no member learns

## Source

Soma, Bouteiller, Hamann & Beltrame, [LIT-1484](../literature.d/LIT-1484.md), read in [NOTE-1132](../notes.d/NOTE-1132.md)
from arXiv:2410.17517v6: Propositions 1 and 2 (pp. 7–11), Lemmas 1 and 2
with their proofs (pp. 20–21).

## What was actually shown

- **Imitation of success.** Inflow to type a from b is π_b π_a E[r_a], and
  the net change is π_a(q_a − v), the Taylor replicator dynamic. The
  expected Cross Learning update, Σ_k π_k dπ_a(k), is the same (Lemmas 1
  and 2).
- **Weighted voter.** Bee i of type k, with sample r_k⁽ⁱ⁾, draws from type a
  an expected flow (1/N)(r_k⁽ⁱ⁾ / v) π_a. Summed over bees this is
  (π_a / v)(q_a − v), the Maynard-Smith dynamic, and it equals the expected
  1-MCL update (Eqs. 10–14).
- **The reading.** The bee "only “blindly” imitates its peers, irrespective
  of their payoffs!" (p. 10), so the reward-driven policy improvement
  exists only at the level of the population.

The derivation was re-checked step by step when filed.

## What it does not show

That honey-bee swarms follow this dynamic: the weighted voter model omits
spontaneous commitment, stop signals, direct switches and quorum sensing.
That the swarm is an agent in any sense beyond this identity. Or anything
for finite populations, where the authors' simulations show options lost
for good ([THEORY-905](THEORY-905.md)).
