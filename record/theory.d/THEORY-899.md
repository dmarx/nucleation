---
number: 899
status: Active
formerly:
- THEORY-tmp3oyxw
title: 'In an infinite, well-mixed population whose members each sample the quality of their own type, imitation of success has the expected update of a single Cross Learning bandit agent (the Taylor replicator dynamic), and the weighted voter model, in which members broadcast their type in proportion to their sample and adopt the first type they perceive, has the expected update of Maynard-Cross Learning, π_a ← π_a + (r_k / v^π)(1[a = k] − π_a), the Maynard-Smith replicator dynamic; the population vector is the policy and no member learns'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings), under ADR-065 §5. A second checker followed both
    propositions and the aggregation step by step and re-ran them by
    script with controls (status review 22). The demand for the version of
    record (Swarm Intelligence 2026) is dropped under ADR-065 §4: no
    discrepancy between versions is named, and NOTE-1132 records the copy
    read (arXiv v6). The old promote_when: A checked re-derivation
    recorded in this file, which the reading made (NOTE-1132) and which
    ADR-047 counts toward promotion, together with the version of record
    (Swarm Intelligence 2026) read and found to state the same
    propositions. It is refuted if the expected one-step change of the
    population vector under either protocol, with infinite population,
    large well-mixed neighbourhoods and evaluation decoupled from
    imitation, differs from the stated replicator dynamic. The title
    claims nothing about real swarms or about agency beyond the identity
    of expected updates; a result about those neither promotes nor refutes
    it.
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

## Note of 2026-10-30: the second check

The second check at the status review ([ADR-065](../decisions.d/ADR-065.md) §5) followed each step.

Imitation of success. A revising member of type b meets a member of type a
with probability π_a and adopts a with probability equal to that member's
sample, whose mean is q_a. The inflow to a from b is π_b π_a q_a, so the
inflow to a is π_a q_a. The outflow from a is π_a Σ_b π_b q_b = π_a v. The
net change per revision is π_a(q_a − v), the Taylor replicator dynamic.
Cross Learning with action k drawn from π and reward r has expected update
E[r(1[a = k] − π_a)] = Σ_k π_k q_k (1[a = k] − π_a) = π_a q_a − π_a v, the
same.

Weighted voter. Each member broadcasts its type in proportion to its
sample, so in a large well-mixed neighbourhood the first type perceived is
a with probability π_a q_a / v. The reviser's expected change of share is
π_a q_a / v − π_a = (π_a / v)(q_a − v), the Maynard-Smith replicator
dynamic. The expected Maynard-Cross Learning update, Σ_k π_k (q_k / v)(1[a
= k] − π_a), is the same. With one of N members revising per step, each is
scaled by α = 1/N.

A script (numpy, in the session's scratchpad) checked these. In 1000
random cases of 2 to 6 types, the four expected updates agreed exactly as
stated. A member-level simulation of the weighted voter (N = 4000, 4000
revisions, π = (.5, .3, .2), q = (.3, .6, .9)) gave a drift, in units of
1/N, of (−.217, .064, .153) against the predicted (−.206, .053, .153),
within one standard error. As a control, an unweighted voter gave (−.003,
−.007, .010), zero within noise.
