---
status: Read
paper: 'LIT-tmp57hqx'
title: 'Chen, Tan and Yan — General-purpose mechanical computing by origami circuit reconfiguration'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the publisher's PDF
    (https://www.nature.com/articles/s41467-025-65464-x.pdf), 14 pages,
    CC BY-NC-ND 4.0; text extracted by pdftotext. Read in full: the
    abstract, introduction, Results (three conditions; basic logic; complex
    functions and the synthesis method; perception and addressing; the
    array architecture and scalability; functional reuse), the Discussion
    and the first paragraph of Methods. Skipped: the rest of Methods, all
    Supplementary Notes (including Note 4 on the synthesis algorithm and
    Note 10.4 on the neural-network weight update) and the Supplementary
    Videos.
date: '2026-11-05'
summary: >-
  Bistable Kresling units snapped by magnetic torque are non-volatile
  Buffer and NOT switches, several to a unit, with a synthesis method that
  minimizes the units a function needs. An array of one module per minterm
  is programmed to any combinational function by a robot, itself steered
  by origami logic along a designed layout of magnets, that activates the
  modules it passes. Adders, a subtractor, a multiplier and a self-reusing
  mobile adder are shown; the neural-network update is only described.
---
<!-- inactive-ok-file: THEORY-tmpj0xcg CLAIM-523 — Proposed or new; cited from the reading of Chen, Tan and Yan (2025) as open -->

# NOTE-tmp2uw2z: Chen, Tan and Yan — General-purpose mechanical computing by origami circuit reconfiguration

## Contribution

Multi-switch bistable units with logic minimization, cutting the units an
application-specific circuit needs; a spatial, minterm-based programmable
array of non-volatile mechanical switches, programmed by a robot that is
itself steered by origami logic; and schemes for input and output
expansion and for reusing one device across steps.

## Key insight

The authors name a trade-off between programmability and scalability:
coupled switches are hard to set independently. Laying the switches out in
space, one module per minterm, decouples them, and programming becomes a
matter of which addresses a mobile actuator visits. Programmability moves
from the wiring into a path.

## Assumptions

- **Magnetic fields** of designed direction and strength at designated
  positions; units spaced to limit cross-talk.
- **Electrical outputs**: conduction of embedded switches; the robot
  carries motors and power; results are read with LEDs, resistors and a
  wireless voltage logger.
- **Programming** sets the minterm activations; the array computes their
  sum, so the modules must be pre-built for every input combination.

## Key results

- **The trade-off (abstract).** "challenges remain in achieving
  general-purpose mechanical computing architecture due to the trade-off
  between programmability and scalability"; "switch coupling complicates
  independent activation, hindering programmability" (introduction).
- **Memory (Results).** "The bistability of Kresling origami imparts
  non-volatility to the mechanical computing system, enabling the
  switching state to be preserved without continuous energy input".
- **Durability (Results).** "Experimental results confirm negligible
  degradation after 10,000 compression cycles", for single units.
- **Economy (Results).** "For a 2-bit adder implementation, our design
  requires only 8 functional units versus 26 in the prior approach".
- **Generality (Results).** "Provided that the functional modules cover
  all minterms (i.e., all possible input combinations), the MPGA can be
  programmed to implement arbitrary combinational logic functions."
- **Scaling (Results).** "the system achieves scalability in computational
  complexity under unlimited computational resources".
- **Addressing (Results).** "the outputs of A0 and A1 were used to control
  the motors of the left and right wheels of a robot"; the authors add,
  "Importantly, the addressing robot itself is controlled by the mechanical
  computing system, preserving the system’s fully mechanical nature."
- **Neural networks (Results).** "Detailed implementation plans can be
  found in Supplementary Note 10.4"; not shown in the main text.

## Concepts

- **Buffer(i) / Not(i)**: a right- or left-handed bistable unit carrying i
  switches.
- **LF-QM**: Quine–McCluskey sum-of-products form, then local factoring to
  minimize literals.
- **MPGA (mechanical programmable gate array)**: spatially discrete logic
  modules with addresses, pre-routed so that activating a set of minterm
  modules programs a function.
- **Magnetic instruction**: a layout of magnetic fields that steers the
  robot along an address path.
- **Computation functional reuse**: a device whose outputs move it to
  memory positions, so intermediate results are stored and fed back.

## Connections

The companion of LIT-tmpmjw68, from the same group, which reconfigures by
moving elements inside gates and cubes rather than by addressing a spatial
array. Its array is a lookup table with a non-volatile memory of which
minterms are on, close to THEORY-609's case of input-output dependencies
with an input memory (LIT-404); an engineered instance, not a test.

## Bearing on the record

- **The synthesis's description.** The pasted synthesis on constraint
  architectures gives only the title, venue and DOI; the bibliography is
  right except that the authors are missing. As an example of the
  synthesis's points, it is a good case of memory held in configuration.
  Programming is external: the function is set by a magnet layout designed
  outside the device, which the robot only executes.
- **CLAIM-025 (regime, organization and capacity to transform persist or
  fail separately).** Supports, by a physical case: the minterm states
  (regime), the routing and module layout (organization) and the robot
  with its magnetic instructions (capacity to transform) are separate
  hardware, and the array keeps computing its function if the robot is
  removed.
- **CLAIM-523 (legibility, efficacy, correctability).** A weak analogy
  only: writing (magnetic activation), retaining (bistability) and reading
  (conduction) are separately engineered.
- **The authors' "fully mechanical nature"** is stronger than the
  apparatus: electric motors and voltage readout.
- **Not embodied cognition, and not learning.** The weight-update scheme
  is a counter adjusted by comparator output, an exhaustive search; it
  bears on none of the record's learning-in-physical-systems entries.
- Filed: THEORY-tmpj0xcg. No instruction for machine-learning practice.

## Limitations

- **Combinational logic** plus latches and a 2-bit counter; general-purpose
  only over pre-built minterm modules, 2^n per output.
- **Programming apparatus**: a designed magnetic layout and a powered
  robot.
- **Described, not shown**: the neural-network update and multi-bit reuse
  are in the Supplementary Information.
- **Robustness** reported for single units only.
- The authors themselves: "While current mechanical computing systems
  exhibit limitations in handling complex deep learning tasks compared to
  mature electronic systems".
