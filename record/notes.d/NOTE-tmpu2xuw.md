---
status: Read
paper: 'LIT-tmpmjw68'
title: 'Hu, Tan, Chen and Yan — Spatially programmable origami networks for mechanical computing'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the publisher's PDF
    (https://www.nature.com/articles/s41467-025-64956-0.pdf), 15 pages,
    CC BY-NC-ND 4.0; text extracted by pdftotext. Read in full: the
    abstract, introduction, Results (design concept, Buffer/NOT element and
    reconfigurable gate, 2D meta-array, 3D reprogrammable logic cube,
    robot), Discussion, and the Methods on fabrication and mechanical
    testing. Skipped: the rest of Methods (gate and cube fabrication, robot
    electronics), all Supplementary Information, including the
    combinatorial derivations, and the Supplementary Movies.
date: '2026-11-05'
summary: >-
  Flat-foldable origami switches make Buffer and NOT elements; a gate of
  two is turned from AND to OR by rotating them from series to parallel,
  and a Rubik's-cube arrangement changes the sum-of-products function its
  columns compute by permuting elements. A 30-gate array realizes four
  2-bit functions; a third-order cube switches between full adder and full
  subtractor; a second-order cube, rotated by a servo, drives a robot's
  path decisions. Inputs are mechanical; outputs and inter-gate signals are
  electrical.
---
<!-- inactive-ok-file: THEORY-tmp4458t — Proposed; cited from the reading of Hu et al. (2025) as open -->

# NOTE-tmpu2xuw: Hu, Tan, Chen and Yan — Spatially programmable origami networks for mechanical computing

## Contribution

Gate-internal reconfiguration, AND to OR by rotating two switching
elements, as a way to cut the redundant cells that reconfigurable
mechanical logic otherwise needs; a Rubik's-cube mapping of
sum-of-products logic with a count of reachable functions per cube order;
and reconfigurable electromechanical logic as a robot's decision module.

## Key insight

What a fixed circuit computes can be changed by where its elements sit
rather than by how they are wired: rotating two elements turns series into
parallel, and permuting cube blocks changes which elements share a column.
The arrangement is the program, and the mechanism that changes it is
separate from both the program and the computation.

## Assumptions

- **Quasi-static compression**; the two-bit input is set by the order in
  which a thin and a thick cell flatten under one load, with a casing to
  realize input (0,1).
- **Electrical outputs**: an element's output is conduction; gates cascade
  through coils driving magnets onto the next gate.
- **Combinational functions** in minimized sum-of-products form;
  "computational density" is the number of realizable functions per
  element, by the authors' formulas.

## Key results

- **The element (Results).** An origami cell "possessing pseudo single
  degree-of-freedom and flat-foldable deformation characteristics".
- **Gate savings (abstract).** "By rotating intra-gate elements to modify
  AND/OR-based Boolean cascades, the design reduces gates by 46.7%
  compared to standard arrays".
- **Meta-array (Results).** "Our work achieves a 20% reduction in gate
  count compared to a nonreconfigurable circuit utilizing 36 AND, OR, NOT,
  and XOR gates."
- **Why a cube (Results).** "the origami switching elements lack
  inter-gate combinability, and each logic gate requires individual control
  of control nodes".
- **Density (Results).** "their computational density can reach 4.5, 81,
  and 1728", for cubes of order two, three and four, by counting.
- **Prototype (Results).** The built third-order cube "implements both
  full-subtractor and full-adder logic functions using only fourteen
  Buffer/NOT origami switching elements", with measured outputs matching
  the truth tables.
- **Robot (Results).** A half-subtractor output d = 0 "triggers a
  transition to half-adder logic"; the rotation is made by a servo-driven
  rotating mechanism.
- **Signals (Results).** "The system employs electromagnetic actuation for
  force input generation and electrical signal output".

## Concepts

- **Buffer / NOT element**: a cell that conducts only when flat-folded, or
  only when not.
- **Reconfigurable gate**: two elements whose relative rotation changes
  series to parallel (AND to OR, NOR to NAND).
- **Reprogrammable gate meta-array**: fixed wiring whose function changes
  by converting and activating gates.
- **Reprogrammable logic cube**: a Rubik's-cube arrangement of elements in
  corner and edge blocks, whose permutations change the series groupings.
- **Computational density**: realizable functions per element.

## Connections

It builds on reconfigurable mechanical logic from metamaterial processors
(Jiao et al.) and on FPGA and DPGA gate arrays as its baseline. Its
companion paper from the same group, [LIT-tmp57hqx](../literature.d/LIT-tmp57hqx.md), moves programmability
into a spatial array addressed by a robot. On the record's side, [LIT-404](../literature.d/LIT-404.md)
and [THEORY-609](../theory.d/THEORY-609.md) say what makes a physical system implement a computation:
this device is an engineered instance of the right input-output
dependencies, tested over all inputs for each function, not a test of
that account.

## Bearing on the record

- **The synthesis's description.** The pasted synthesis on constraint
  architectures gives only the title, venue and DOI; the bibliography is
  right except that the authors are missing. Where the synthesis
  contrasts programmable with self-governing reconfiguration, this device
  comes closest of its works to the second form, but not in the material:
  the cube's configuration is updated from its own output only through a
  servo and relay electronics. The density of 1728 is a count for an
  unbuilt fourth-order cube.
- **[CLAIM-025](../claims.d/CLAIM-025.md) (regime, organization and capacity to transform persist or
  fail separately).** Supports, by a clean physical case: the function
  computed (operative regime), the block arrangement fixing it
  (organization) and the rotating mechanism (capacity to transform) are
  separate parts, and the third can be removed while the first two remain.
- **[CLAIM-480](../claims.d/CLAIM-480.md) (composing interactions makes constraints).** Qualifies,
  weakly: series and parallel composition yields a new function, not a new
  mechanical constraint.
- **The authors' framing.** "materials no longer passively execute
  algorithms – they become the algorithm" (introduction) is stronger than
  the apparatus, whose computation is mechanical switching of electrical
  circuits.
- **Not embodied cognition.** The robot uses the device as a switching
  circuit; nothing here bears on the record's embodied-cognition entries.
- Filed: [THEORY-tmp4458t](../theory.d/THEORY-tmp4458t.md). No instruction for machine-learning practice.

## Limitations

- **Combinational logic only**; propagation and reconfiguration rely on
  electromagnets, servos, relays and external power.
- **Counted, not built**: the 1728 density; the gate savings are against
  the authors' own baseline counts.
- **One robot demonstration**, two left-turn manoeuvres on one mixed path.
- **No durability, error rates or speed** in the main text.
