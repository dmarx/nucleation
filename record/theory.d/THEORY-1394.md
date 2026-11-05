---
number: 1394
status: Proposed
formerly:
- THEORY-tmph4325
promote_when: >-
  The balance equations and performance-measure formulas of §5.4 checked
  against the equation images or the print edition, confirming that the
  model's state is the busy or free status of each of N distinguishable
  units, that transitions follow fixed-preference dispatch from atoms
  generating Poisson calls, and that each unit's workload, the
  inter-district dispatch fractions and the mean travel times are computed
  from the steady-state probabilities of that chain.
title: "Larson and Odoni's hypercube model represents an urban emergency service's N distinguishable units, each busy or free, as a Markov chain on the vertices of an N-cube under fixed-preference dispatch from point sources of Poisson calls, and from its steady state computes each unit's workload, the inter-district dispatch fractions and the mean travel times"
version: 1
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-2053
summary: >-
  Larson and Odoni (1981), [LIT-2053](../literature.d/LIT-2053.md), chapter 5, §§5.4–5.5, read in
  prose in [NOTE-1620](../notes.d/NOTE-1620.md); the textbook restatement of the model introduced
  in Larson (1974), [LIT-2105](../literature.d/LIT-2105.md), which could not be read. Proposed: the
  prose states the state space, the dispatch rule, the assumptions and
  which measures are computed, but the equations are images and were not
  seen. It says nothing about valuing a unit, and the basic model evaluates
  response areas a user supplies rather than optimizing them.
---
<!-- inactive-ok-file: NOTE-1620 LIT-2105 — Skimmed or Unavailable, and new; the reading this account comes from and the unread original it restates, cited as open -->

# THEORY-1394: Larson and Odoni's hypercube model represents an urban emergency service's N distinguishable units, each busy or free, as a Markov chain on the vertices of an N-cube under fixed-preference dispatch from point sources of Poisson calls, and from its steady state computes each unit's workload, the inter-district dispatch fractions and the mean travel times

## Source

Larson and Odoni (1981), [LIT-2053](../literature.d/LIT-2053.md); read in [NOTE-1620](../notes.d/NOTE-1620.md), the prose of
§§5.4–5.5. The model is Larson (1974), [LIT-2105](../literature.d/LIT-2105.md), unread.

## What was actually shown

- **The state space.** "The model's name derives from the state space
  describing the availabilities of servers" (§5.4); each server is busy or
  free, so the state is a vertex of an N-cube, with a tail of queue states
  when a queue is allowed.
- **Dispatch.** A fixed preference list per atom: "the ordered list of
  preferences does not change with the state of the system" (§5.4.2).
- **The assumptions.** Nine, including atoms as points, independent Poisson
  arrivals per atom, one unit per call and exponential service (§5.4.2).
- **The measures.** The book names and illustrates for N = 3 the unit
  workloads, the dispatch fractions by unit and atom, the inter-district
  dispatch fractions and the travel times (§§5.4.3–5.4.4); the formulas
  themselves are images and were not seen.
- **Workload sharing.** Backup dispatching makes the units' workloads "more
  evenly distributed than the workloads of the primary response areas"
  (§5.4.4).

## What this does not say

- That a unit has a value, or that its worth depends on the others' states:
  that framing is the pasted bibliography's, not the book's.
- That the model optimizes locations or districts: in the basic model
  "Response areas were not optimized in any sense" (§5.4.5), and the
  trade-offs are left to "the user of the model, not by the model itself"
  (§5.4.1).
- Anything about priority dispatching, multiple units per call, or systems
  where travel time dominates service time, which the basic model excludes.
- What the 1974 paper itself contains beyond the model the book restates.
