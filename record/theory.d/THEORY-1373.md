---
number: 1373
status: Proposed
formerly:
- THEORY-tmp4458t
promote_when: >-
  A reading of the Supplementary Information or an independent build
  confirms that one fixed-wiring array of rotatable two-element gates
  realizes several distinct functions by element rotation and gate
  activation alone, with measured truth tables, and that the count of
  functions per element exceeds that of a gate array realizing the same
  functions by rewiring.
title: 'Combinational logic built from flat-foldable origami switches can be reconfigured by moving the switching elements rather than rewiring them, by rotating the two elements of a gate between series and parallel or by permuting elements among the blocks of a Rubik''s-cube arrangement, and so reaches more functions per element than a rewired gate array'
version: 2
history:
- version: 2
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-373 and QUESTION-388, at the reading review of
    2026-11-11 (by question, ADR-091). Both name Hu et al.'s origami logic
    as reconfiguration set from outside: QUESTION-388 quotes the reading,
    "The arrangement is the program, and the mechanism that changes it is
    separate from both the program and the computation"; QUESTION-373
    lists it under "A robot". No other change.
tags:
- natural-sciences
date: '2026-11-05'
source:
- LIT-2082
summary: >-
  Hu, Tan, Chen and Yan (2025), [LIT-2082](../literature.d/LIT-2082.md), read in [NOTE-1608](../notes.d/NOTE-1608.md). The
  rotatable gate, the 30-gate array and a third-order cube switching
  between full adder and full subtractor were built and tested over all
  inputs; the densities per cube order and the gate savings are counts
  against the authors' own baselines. It does not say that the computation
  is purely mechanical, since outputs and inter-gate signals are
  electrical, or that the material reconfigures itself.
bears_on:
- QUESTION-373
- QUESTION-388
---

# THEORY-1373: Combinational logic built from flat-foldable origami switches can be reconfigured by moving the switching elements rather than rewiring them, by rotating the two elements of a gate between series and parallel or by permuting elements among the blocks of a Rubik's-cube arrangement, and so reaches more functions per element than a rewired gate array

## Source

Hu, Tan, Chen and Yan (2025), [LIT-2082](../literature.d/LIT-2082.md); read in [NOTE-1608](../notes.d/NOTE-1608.md).

## What was actually shown

- **The gate**: two Buffer/NOT elements switched between series and
  parallel by rotation, giving AND or OR, with a thickness difference so
  that one compressive load encodes all four two-bit inputs.
- **The array**: 30 gates reconfigured among a 2-bit adder, subtractor,
  comparator and multiplier, counted as 20% fewer gates than a fixed
  circuit of 36 and 46.7% fewer than an FPGA/DPGA-style array of 44.
- **The cube**: a third-order prototype of 16 elements, 14 used, switched
  between full subtractor and full adder, outputs matching the truth
  tables for all inputs; densities 4.5, 81 and 1728 counted for orders two
  to four.

## What this does not say

- That the computation is mechanical throughout: inputs are compressions,
  outputs and signals between gates are electrical.
- That the device reconfigures itself: rotations are made by hand or by a
  servo.
- That a fourth-order cube was built or reaches 1728 in practice.
- Anything about durability, speed or error rates.
