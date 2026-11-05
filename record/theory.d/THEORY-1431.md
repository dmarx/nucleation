---
number: 1431
status: Proposed
formerly:
- THEORY-tmpx5uxp
promote_when: >-
  A reading or replication confirms, in experiment or in a validated
  mechanical model, that a linear readout trained on the configuration
  sequence of a multistable origami reservoir classifies better than the
  same readout on the raw inputs, and that retaining part of the
  configuration between steps lowers error on a sequential memory task.
title: 'A multistable origami metamaterial driven by a fixed sequence of tension and compression can serve as the reservoir of a reservoir computer: a trained linear readout of its sequence of stable configurations classifies inputs better than the same readout of the raw inputs, and a retained buffer of cells carries input history'
version: 1
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
source:
- LIT-2026
summary: >-
  Liu, Fang, Xu and Wang (2023), [LIT-2026](../literature.d/LIT-2026.md), read in [NOTE-1600](../notes.d/NOTE-1600.md). The
  comparison with the raw inputs (90.4% against 87.2% on binarized MNIST)
  and the memory result are simulations with a least-action model; the
  experiment covers ten 5×4-pixel digits on a 4×2-cell prototype. It does
  not say that the material learns: only the linear readout is trained.
---

# THEORY-1431: A multistable origami metamaterial driven by a fixed sequence of tension and compression can serve as the reservoir of a reservoir computer: a trained linear readout of its sequence of stable configurations classifies inputs better than the same readout of the raw inputs, and a retained buffer of cells carries input history

## Source

Liu, Fang, Xu and Wang (2023), [LIT-2026](../literature.d/LIT-2026.md); read in [NOTE-1600](../notes.d/NOTE-1600.md).

## What was actually shown

- **In experiment**: a 3D-printed 4×2-cell prototype, written row by row
  with two transitions per row, gives 60 features from which a logistic
  readout recognizes ten 5×4-pixel digits, and noisy versions.
- **In simulation**: binarized MNIST (4500 training, 1000 test images) at
  90.4% with three transitions against 87.2% for the readout on raw
  inputs, best 91.8%; a 5-bit memory task, run recursively through a buffer
  zone, with error near zero at 200 cells.
- **A failing rule**: under all-compression the structure always reaches
  one fully compressed configuration and the input is lost.

## What this does not say

- That the metamaterial is trained or learns: the readout is.
- That the advantage over raw inputs, or the memory result, has been shown
  in hardware.
- That the gain is large: three points on reduced MNIST.
