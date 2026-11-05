---
number: 1436
status: Proposed
formerly:
- THEORY-tmpzs387
promote_when: >-
  A reading confirms that the paper's optimisation results and prototypes
  (Figs. 2, 4 and 6) show these fits with grouped actuators, and that Fig.
  4d shows error decreasing with diminishing returns as actuators are
  added.
title: 'Liu, Zhang and Fang show that an origami spring, modelled as a chain of one-degree-of-freedom cells by adding virtual creases, can be fitted to a range of 3D curves when its cells are grouped to share a few actuators, with fitting error falling as actuators are added and each added actuator gaining less'
version: 1
tags:
- control-theory
- mathematics
date: '2026-11-05'
source:
- LIT-2077
summary: >-
  Liu, Zhang and Fang (2023), [LIT-2077](../literature.d/LIT-2077.md), read in [NOTE-1558](../notes.d/NOTE-1558.md) (the main
  text; the supplement skipped). Proposed: the figures were read by caption
  and text, and the experimental comparisons are in the unread supplement.
  It is kinematic and about static shapes. It does not say how good the
  virtual-crease model is for a flexible spring, that the grouping found is
  optimal or unique, or anything about moving between shapes.
---

# THEORY-1436: Liu, Zhang and Fang show that an origami spring, modelled as a chain of one-degree-of-freedom cells by adding virtual creases, can be fitted to a range of 3D curves when its cells are grouped to share a few actuators, with fitting error falling as actuators are added and each added actuator gaining less

## Source

Liu, Zhang and Fang (2023), [LIT-2077](../literature.d/LIT-2077.md); read in [NOTE-1558](../notes.d/NOTE-1558.md).

## What was actually shown

- **The model** (p. 3): with virtual creases "The simplified unit cell is a
  one-degree-of-freedom system."
- **Full actuation** (p. 4): C, J and spiral curves fitted with "errors of
  the three approximations are all found to be less than 0.66%".
- **Grouped actuators** (pp. 5–6): two actuators for the C and spiral, three
  for the J; for a sinusoid a "structure with only 2 actuators is
  insufficient for accurate approximation". The fits could have needed one
  actuator per cell; they did not.
- **Diminishing returns** (p. 6): "the rate of improvement in fitting error
  diminishes as more independent actuators are introduced."
- **Prototypes** (pp. 8–9): C, J and spiral shapes reproduced, with
  shortfalls near the drive end from gravity and friction.

## What this does not say

- That the rigid-folding model describes a flexible spring well: the
  approximation is asserted, and the authors name its limits.
- That a given grouping is the best or the only one: the outputs "are not
  unique".
- Anything about transitions between shapes, their cost, or bottlenecks
  along the way; the pasted synthesis on constraint architectures files it
  under resource-constrained reconfiguration, which goes beyond it.
- That the trade-off is feasibility against a budget: it is accuracy
  against actuator count.
