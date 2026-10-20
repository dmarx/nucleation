---
status: Open
title: 'How far is a periodic greedy that switches a capped number of page fragments between caching and materializing, to keep the share of fresh fragments served above a threshold, from the best plan that meets the same threshold?'
version: 1
tags:
- databases
- operations-research
date: '2026-10-19'
line: 'distributed-agency'
refines:
- QUESTION-114
summary: >-
  The promotion condition formerly on [THEORY-382](../theory.d/THEORY-382.md). [THEORY-382](../theory.d/THEORY-382.md) was promoted
  on 2026-10-19 ([ADR-047](../decisions.d/ADR-047.md) v3) on what Labrinidis and Roussopoulos measured:
  in one synthetic simulation with fixed costs, their OVIS greedy tracked
  the freshness threshold, answered faster than caching alone and
  recovered from overload. No run compares it with the best plan, and its
  optimality under the cap is asserted, not proved.
---

# QUESTION-tmpqzpcd: How far is a periodic greedy that switches a capped number of page fragments between caching and materializing, to keep the share of fresh fragments served above a threshold, from the best plan that meets the same threshold?

## Why it is a question

[THEORY-382](../theory.d/THEORY-382.md) holds that OVIS lies between all-materialized and caching
alone in one simulator, with uniform costs and single runs. It chooses
fragments by estimated speed gain alone, ignoring each one's cost in
freshness, and its estimates ignore that one fragment's refresh load
delays others through the shared queue. Whether it is near the best plan
under the same freshness threshold, or far from it, the evidence does not
say. Until 2026-10-19 this was [THEORY-382](../theory.d/THEORY-382.md)'s promote_when.

## What would answer it

- An analysis bounding the response time of OVIS(θ), or of any rule of
  its kind, against the best plan that meets the same freshness threshold:
  the best fixed plan, or an offline optimum over the same access and
  update streams.
- A measurement on a real server or a recorded web workload that compares
  it with that best plan.

What would not answer it: more synthetic simulations in which OVIS lies
between all-materialized and caching only. That is what [THEORY-382](../theory.d/THEORY-382.md)
already holds, and it says nothing about the distance to the best plan.
