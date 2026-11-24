---
number: 230
status: Open
formerly:
- LEAD-tmppzp9z
title: Extend the readiness simulator to two capacity resources, a cumulative cost
  of transition and several contingencies with different deadlines, and test whether
  readiness stays a step function of the reserve, whether a drill still holds the
  budget as a reserve does, and how the ranking of reserve against redesign changes
version: 1
stage: specified
method:
- formal
tags:
- operations-research
- society-and-governance
date: '2026-11-23'
line:
- readiness
advances:
- CLAIM-585
- CLAIM-646
- CLAIM-878
- CLAIM-1099
presupposes:
- LEAD-226
summary: 'A gap of the manuscript governance-of-possibility, §9.10 (GC7): its model
  has one capacity resource, no cumulative cost and one deadline per contingency.
  Extends [LEAD-226](LEAD-226.md). The design is fixed here. The wording is the assistant''s
  (Claude, in this session); adopting it is the owner''s call.'
---

<!-- inactive-ok-file: CLAIM-646 CLAIM-878 — Proposed; what this would test -->

# LEAD-230: Extend the readiness simulator to two capacity resources, a cumulative cost of transition and several contingencies with different deadlines, and test whether readiness stays a step function of the reserve, whether a drill still holds the budget as a reserve does, and how the ranking of reserve against redesign changes

## The design

Start from the manuscript's model (scratch/manuscripts/governance-of-possibility/analysis/),
which carries out [LEAD-226](LEAD-226.md), with its regimes, seeds and do(c)
readiness. Three arms, each run alone:

1. **Two resources.** Crew and equipment, each held at each moment; each
   configuration has a pair of requirements and each path a pair of peaks,
   with the original path peaking in crew and the staged one in equipment.
   Budget rules apply per resource. Sweep reserves over a grid of pairs
   from 0 to 2 in steps of 0.25.
2. **Cumulative cost.** Besides the capacity held, each transition period
   spends money at its requirement from a per-period money budget set by
   the peak rule on last period's spending. Two architectures with equal
   thresholds and least cumulative costs in ratio 1 : 3 ([CLAIM-646](../claims.d/CLAIM-646.md)'s
   construction).
3. **Several deadlines.** Two contingencies, one needing B by τ₁ = 3, one
   needing a third configuration by τ₂ = 12, scored as a vector of
   readiness at the two deadlines.

## Checks the record can run

- **Arm 1.** [CLAIM-585](../claims.d/CLAIM-585.md) predicts that the reserves sufficient for each path
  form an upward-closed set with a frontier that need not be convex. If
  readiness over the grid is constant on the regions the paths' peaks bound
  and jumps only at their edges, the step function of the manuscript's
  §9.7 survives two resources; if it varies within a region, it does not.
- **Arm 2.** [CLAIM-878](../claims.d/CLAIM-878.md) says its drill accounting fails for "budgets in
  money or hours". If a drill still keeps the money budget at the
  transition's cost per period at no more than a reserve's cost, that
  limit is wrong in this model.
- **Arm 3.** If one regime is first at both deadlines, the profile adds
  nothing to a single deadline; the manuscript's §6 predicts crossings.
