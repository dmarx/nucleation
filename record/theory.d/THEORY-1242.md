---
number: 1242
status: Proposed
formerly:
- THEORY-tmpqpx0q
promote_when: >-
  A primary study, read by the record, that computes ideal-observer
  performance for one visual task at successive stages of the visual system
  (stimulus, retinal image, receptor absorptions or ganglion-cell output)
  and measures human performance across the same conditions. It promotes the
  empirical clause if human performance follows the late-stage ideal across
  conditions while falling below it by a roughly constant factor; it refutes
  it if the pattern across conditions departs from that ideal's. Another
  review restating the logic, or a further fit of a single ideal at one
  stage, cannot settle it: the clause is about the comparison across stages.
title: 'In early-vision tasks, human performance varies across conditions as the information available at the retinal output does, while falling well below the retinal-stage ideal, so substantial losses lie in central factors'
version: 1
tags:
- cognition
- neuroscience
- probabilistic-modeling
date: '2026-10-30'
source:
- LIT-1055
extends:
- THEORY-336
summary: >-
  The thesis Geisler's review asserts, filed beside [THEORY-336](THEORY-336.md) by the status
  review of 2026-10-30 ([ADR-065](../decisions.d/ADR-065.md) §3; [ADR-047](../decisions.d/ADR-047.md) kind 1). [THEORY-336](THEORY-336.md), Active,
  holds what the review reports; whether the parallel holds is this entry's
  question, and none of the primary stage-by-stage studies (Geisler 1989;
  Banks, Geisler and Bennett 1987) is read.
---

# THEORY-1242: In early-vision tasks, human performance varies across conditions as the information available at the retinal output does, while falling well below the retinal-stage ideal, so substantial losses lie in central factors

## Source

Geisler (2011), [LIT-1055](../literature.d/LIT-1055.md), read in full in [NOTE-870](../notes.d/NOTE-870.md) from the NIH author
manuscript. The review asserts the thesis as its account of the studies that
added biological constraints to the ideal observer one at a time: "the variation
in human performance across conditions is often predicted by the information
available in the retinal responses", and "the suboptimal performance of human
observers implies substantial contributions of central factors."

## Where the evidence stands

What the review reports, and the logic of constrained ideals it rests on, is
[THEORY-336](THEORY-336.md), Active, which this entry extends: that entry is the reading, this
one the thesis. None of the primary stage-by-stage studies is read; the
2026-10-20 audit found Geisler (1989) and Banks, Geisler and Bennett (1987)
closed. The `promote_when` above is [THEORY-336](THEORY-336.md)'s condition before the status
review of 2026-10-30 promoted it, carried here word for word, because it asks
what would make the thesis true and not what the review says.

## What this does not say

- That the gap below the ideal identifies its cause. The review says the
  opposite: far-below-ideal performance leaves many models standing.
- That every loss beyond the retina is in the input. The review names residual
  losses in the decision rule (uncertainty, nonlinearities, inefficient
  pooling).
