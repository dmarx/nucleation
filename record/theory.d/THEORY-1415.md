---
number: 1415
status: Proposed
formerly:
- THEORY-tmpop5d8
promote_when: >-
  A reading confirms, in this paper or a replication, that with equal
  folding and unfolding orders every state of an N-barrel stack is
  reachable by uniaxial loading, and that defect states exist which no
  uniaxial protocol from the main graph reaches and whose exits by erasure
  or shift are not reversed by reversing the load.
title: 'A series stack of decoupled bistable Kresling barrels is a Preisach memory whose reachable states are fixed by the order of the switching thresholds, while hidden elastic degrees of freedom admit defect states that the loading protocol cannot reach and can leave only irreversibly'
version: 2
history:
- version: 2
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-373, at the reading review of 2026-11-11 (by
    question, ADR-091). The question names it as its case of a hand: "the
    defect states are reached only by twisting by hand"; its own text,
    defect states "reached by twisting by hand", which "the loading
    protocol cannot reach". No other change.
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
source:
- LIT-2072
summary: >-
  Jules, Reid, Daniels, Mungan and Lechenault (2022), [LIT-2072](../literature.d/LIT-2072.md), read
  in [NOTE-1617](../notes.d/NOTE-1617.md). Shown in experiment on one four-barrel stack and its
  softer twin, with the Preisach graph confirmed and defect states found by
  twisting by hand. It does not say that the 64 counted states were all
  observed (39 of 48 single-defect states were), that the readout
  identifies every state, or that loading alone can create a defect in a
  decoupled stack.
corroborates:
- CLAIM-591
bears_on:
- QUESTION-373
---

# THEORY-1415: A series stack of decoupled bistable Kresling barrels is a Preisach memory whose reachable states are fixed by the order of the switching thresholds, while hidden elastic degrees of freedom admit defect states that the loading protocol cannot reach and can leave only irreversibly

## Source

Jules, Reid, Daniels, Mungan and Lechenault (2022), [LIT-2072](../literature.d/LIT-2072.md); read in
[NOTE-1617](../notes.d/NOTE-1617.md).

## What was actually shown

- **The Preisach memory** (§II.A–B): four modules of pattern angle 74° to
  82°, measured singly for their thresholds and then stacked, switch in the
  same order under compression and extension, so all 16 states are stable
  and reachable, as the model predicts from the threshold order.
- **The defects** (§II.C): stable configurations with a pair of
  half-folded barrels, reached by twisting by hand; 39 of the 48 possible
  single-defect states were observed before the sample was too damaged, and
  two-defect states were unstable.
- **Unreachability** (§II.C): the largest strongly connected component is
  the main graph, with "no transition from a reachable microstate to a
  defective configuration".
- **Irreversible exits** (§II.D): erasure to the main cycle or a shift of
  the defect to a stiffer module; a few observed transitions contradict
  these rules, which the authors put down to crease aging.

## What this does not say

- That the stack has 64 observed states: the 64 is 16 + 48 counted.
- That the defect states are reachable by any loading of the decoupled
  stack: only a coupled pattern (appendix C) forms them spontaneously.
- That height and stiffness identify each state: the authors say they do
  not, unequivocally.
- That the memory scales: the authors expect reading to fail beyond a few
  barrels with their materials.
