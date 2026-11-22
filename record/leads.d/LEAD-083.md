---
number: 83
status: Open
formerly:
- LEAD-tmpehwvz
title: 'Measure compensation and entrainment in a mode that is dynamically closed but not a weakly coupled block, to see whether the block test misses a unit'
version: 1
stage: idea
priority: high
method:
- empirical
- formal
tags:
- individuation
- complex-systems
date: '2026-11-19'
line:
- distributed-agency
advances:
- QUESTION-218
- QUESTION-219
- CLAIM-157
summary: >-
  The direct defeat test of [CLAIM-157](../claims.d/CLAIM-157.md). Named in [QUESTION-218](../questions.d/QUESTION-218.md) and
  [QUESTION-219](../questions.d/QUESTION-219.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-tmpwyp15 CLAIM-tmpjwc0h — new; LEAD-083's study and claim of 2026-11-22 -->
<!-- inactive-ok-file: CASE-269 CLAIM-157 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-083: Measure compensation and entrainment in a mode that is dynamically closed but not a weakly coupled block, to see whether the block test misses a unit

## What it would do

Find or simulate a system with a closed mode that is not a gap-isolated
block (a flux pattern or a field excitation), perturb it, and measure
whether it compensates and entrains; [CASE-269](../cases.d/CASE-269.md)'s field testbed could carry
the arm for [QUESTION-219](../questions.d/QUESTION-219.md).

Where the record names it:

- [QUESTION-218](../questions.d/QUESTION-218.md): "If the mode compensates and entrains and the block test
  misses it, that meets [CLAIM-157](../claims.d/CLAIM-157.md)'s defeated_if"
- [QUESTION-219](../questions.d/QUESTION-219.md): "to a system where the block test fails"

## What would count

Compensation and entrainment where the block test sees no unit meets
[CLAIM-157](../claims.d/CLAIM-157.md)'s defeated_if. Their absence says the block is the better unit
and closure tracks something else.

## Note of 2026-11-22: the study run

[CASE-tmpwyp15](../cases.d/CASE-tmpwyp15.md) ran the lead's core arms, about twenty minutes of CPU. A
φ⁴ lattice kink (the field excitation, [CASE-269](../cases.d/CASE-269.md)'s first model) and the locked
cluster of a uniformly coupled Kuramoto population (a collective mode
with an environment) were each loaded and detuned, beside a two-block
control. Members compensate in all three (κ 1.00, 0.97, 1.00), and the
cluster's members entrain (0.91). The block test on members picks out
only the control: the kink's best segment ratio falls as the square of
the lattice spacing, and on coupling constants the cluster scores as
every set of its size does. [CLAIM-tmpjwc0h](../claims.d/CLAIM-tmpjwc0h.md) states the result.

What remains: the flux arm ([QUESTION-219](../questions.d/QUESTION-219.md)); entrainment for a field
excitation, which needs one with timing, such as an underdamped kink's
shape mode or a breather; noise, other load sizes and coupling
strengths; a measured closure (transfer entropy) for both modes; and
setting τ, without which the cluster's realized ratio of 0.81 has no
verdict. The lead's status and stage are the owner's.
