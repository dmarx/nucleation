---
status: Proposed
title: 'Natschläger, Bertschinger and Legenstein show, by an annealed mean-field theory and simulation, that random networks of binary threshold gates driven by a random binary input have an order-to-chaos line where a single flipped input bit flips on average one node (K·P_bf = 1), that a separation measure corrected for initial-condition and input-drive separation peaks near that line, that a trained linear readout performs best near it on delayed parity and random Boolean functions of recent inputs, averaged over many tasks, and that a local synaptic-scaling rule drives networks to the line'
promote_when: >-
  An independent study or replication in driven random threshold or
  Boolean networks finds task-averaged readout performance on nonlinear
  functions of recent inputs maximal near the damage-spreading critical
  line K·P_bf = 1, and the corrected separation measure peaking there.
version: 1
tags:
- neuroscience
- complex-systems
- information-theory
date: '2026-11-22'
source:
- LIT-tmpdsowv
bears_on:
- QUESTION-507
summary: >-
  The NIPS 2004 companion (LIT-tmpdsowv) of Bertschinger and Natschläger's
  Neural Computation paper (LIT-2991, unreachable), read in its place in
  NOTE-tmpi5t3r. The edge of chaos here is a damage-spreading line,
  K·P_bf = 1, crossing a wide range of mean activity; order is fading
  memory, and chaos fails because the state carries "spurious"
  information about initial conditions. The optimum is averaged over many
  tasks by design, with no per-task optima, so it qualifies rather than
  defeats CLAIM-809 (ARG-tmp2zz6k).
---
<!-- inactive-ok-file: LIT-2991 ARG-tmp2zz6k CLAIM-809 CLAIM-814 CLAIM-850 THEORY-tmpye6xs THEORY-2041 — Unavailable, Proposed or new; the work this stands in for and the entries it bears on -->

# THEORY-tmps8t83: Natschläger, Bertschinger and Legenstein show, by an annealed mean-field theory and simulation, that random networks of binary threshold gates driven by a random binary input have an order-to-chaos line where a single flipped input bit flips on average one node (K·P_bf = 1), that a separation measure corrected for initial-condition and input-drive separation peaks near that line, that a trained linear readout performs best near it on delayed parity and random Boolean functions of recent inputs, averaged over many tasks, and that a local synaptic-scaling rule drives networks to the line

## Source

Natschläger, Bertschinger and Legenstein, "At the Edge of Chaos:
Real-time Computations and Self-Organized Criticality in Recurrent Neural
Networks", NIPS 17 (2004), LIT-tmpdsowv, read from the proceedings PDF in
NOTE-tmpi5t3r, as a stand-in for LIT-2991.

## What was actually shown

- Eq. 1: the critical line α* = 1 is K·P_bf = 1, P_bf "the probability
  (averaged over the inputs and the network activity) that a node will
  change its output if a single out of its K input bits is flipped".
- §3: fading memory "is equivalent to the requirement that all state
  differences vanish, i.e. being in the ordered phase"; in chaos the state
  "contains “spurious” information about the initial conditions".
- §4: "the N M -separation peaks very close to the critical line"
  (numerical estimates, fn. 4).
- §5: "The highest performance is clearly achieved for parameter values
  close to the critical line", on delayed 3-bit parity and 50 random
  Boolean functions of 5 inputs, with networks "not optimized for any
  specific task".
- §6: a margin-based estimate of each node's P_bf and a scaling rule
  toward 1/K bring networks from either phase to the line.

What could have failed: performance could have peaked deep in the
ordered phase, where fading memory is strongest, or NM-separation could
have peaked away from where performance does; neither did.

## What this does not say

- Not per-task optima: the paper warns that a network "specifically
  designed for a single task will not show a good performance in this
  setup", and reports averages over tasks.
- Not a bound on total capacity, nor how capacity is shared among tasks.
- Not branching criticality of activity: activity "can vary considerably"
  across the parameter plane. That K·P_bf = 1 is a branching ratio of one
  for perturbations is the reader's and filer's inference, not the
  paper's.
- Not a general law: §7's "general property of input driven dynamical
  systems" is a hypothesis it supports for one model class.

## Connections

Qualifies CLAIM-809 (ARG-tmp2zz6k). Bears on QUESTION-507 (points 1 and
2) and CLAIM-850. Contrast with CLAIM-814 and THEORY-tmpye6xs; parallel to
THEORY-2041.
