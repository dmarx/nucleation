---
status: Proposed
title: 'Acquisition order on a known tree with each level''s strength set independently, in kernel, deep linear and small ReLU learners'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-052. Code, tests
    and results are committed under scratch/studies/lead-052/.
standing: documented
kind: executed-study
tags:
- learning-theory
- representation-learning
date: '2026-11-22'
line:
- learned-structure
draws_on:
- THEORY-186
- THEORY-086
- THEORY-187
bears_on:
- QUESTION-217
- QUESTION-039
summary: >-
  The study LEAD-052 asks for. Eight items on a binary tree of depth 3;
  inputs and targets written in the tree's Haar basis with a strength per
  level, c for inputs and g for targets, set freely and then rotated at
  random, so the tree fixes the distinctions and c and g fix how strong
  each level is. Acquisition of a level is the first time the network's
  own output recovers 90% of that level's target. Exact kernel flow (linear
  and infinite-width ReLU NTK), NTK-parametrized ReLU networks of width 64
  to 4096, deep linear networks of two and three layers, and two-layer ReLU
  networks from small and order-one scale, over a 9 × 9 grid of target
  strengths and a 7 × 7 grid of input against target strengths, three
  seeds each. The kernel learners and the width-2048 network order the
  levels by input strength alone and ignore the targets; the two-layer
  linear network orders them by the product c·g in every cell of the
  first grid; the small-scale ReLU network keeps that direction but
  compresses its spread, so many cells become simultaneous. No arm
  ordered the levels by tree depth as such. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-186 — Proposed; the deep linear solution, used as the method this study checks against -->
<!-- inactive-ok-file: CLAIM-tmpzujm1 CLAIM-tmp0h57p — new; the claims this study grounds, filed 2026-11-22 -->

# CASE-tmp7n58t: Acquisition order on a known tree with each level's strength set independently, in kernel, deep linear and small ReLU learners

## What was done

LEAD-052 asks to train on synthetic data with a known tree, with the
spectral strength of each level varied independently of the tree, and to
map when acquisition is coarse-first, fine-first, simultaneous or mixed,
in deep linear, kernel-regime and small nonlinear networks. Done on
2026-11-22 with numpy on CPU (scratch/studies/lead-052/: README.md with
the derivation and every table, eleven tests, results/runs.jsonl with
2699 runs, one per line).

- **Data.** The tree's levels are the Haar levels of R⁸: level 1 the root
  split, level 2 the two splits below it, level 3 the four leaf pairs.
  X = √N H diag(c) R_in and Y = √N H diag(g) R_out, so on level ℓ the
  input covariance is c_ℓ² and the input–output correlation has singular
  value c_ℓ g_ℓ.
- **Measure.** QUESTION-217's T_ℓ(δ), with the network's output as the
  decoder: the first time ‖P_ℓ(F − Y)‖²/‖P_ℓY‖² ≤ 0.1. Two levels tie when
  the later time is within 1.25 of the earlier; robustness at δ = 0.5 and
  0.02 and ties at 1.1 and 1.5.
- **Grids.** E1: inputs flat, targets g = (1, a, b), log₂ a and log₂ b
  from −2 to 2 (81 cells). E2: c_ℓ and g_ℓ geometric in the level, ratios
  2^(±0.5) (49 cells). E3: the transition, by width and initial scale, on
  three target profiles.

## What came out

| learner | E1: cells C / F / S / M | E1: matches order by c·g | exponent of T on g (E1) | E2: exponents on g, c |
|---|---|---|---|---|
| exact kernels (linear, ReLU NTK) | 0 / 0 / 81 / 0 | 0.01 | 0 | 0; −2.0 (linear), −1.14 (NTK) |
| ReLU, NTK parametrization, width 2048 | 1 / 0 / 79 / 1 | 0.03 | −0.04 | 0.00; −1.15 |
| deep linear, two layers | 14 / 14 / 1 / 52 | 1.00 | −0.92 | −0.95; −1.12 |
| deep linear, three layers | 14 / 14 / 1 / 52 | 1.00 | −1.26 | −1.83; −1.07 |
| two-layer ReLU, small scale | 35 / 12 / 18 / 16 | 0.42 | −0.36 | −0.42; −0.43 |
| two-layer ReLU, width 64, scale 1 | 8 / 18 / 10 / 45 | 0.80 | −0.43 | −0.34; −1.10 |

- **Kernel learners.** With tree-symmetric inputs every kernel of inner
  products and norms commutes exactly with the level projectors, so each
  level relaxes as exp(−2μ_ℓt/N) and T_ℓ = N ln(1/δ)/(2μ_ℓ), with μ_ℓ set by
  the inputs alone (README, Derivation 1–2). The exact kernels and the
  width-2048 network bore this out: simultaneous in 79 to 81 of 81 cells
  when inputs are flat, whatever the targets; in E2 the boundary is the
  line ρ_in = 1, the same in every column.
- **Deep linear.** The decoupled solution orders levels by c_ℓ g_ℓ
  (Derivation 3). The trained two-layer network matched that order in all
  81 cells of E1 and 44 of 49 in E2, from random small weights; in the cell checked against the
  formula, its times came within 10% of it. Its E2 boundary is the
  anti-diagonal ρ_in ρ_out = 1. The three-layer network ordered the same
  in E1 but weighed target strength more than input strength in E2, which
  the two-layer formula does not predict.
- **Small-scale ReLU.** No cell, at any threshold tried, went
  coarse-first where the two-layer linear network went fine-first, or the
  reverse. But the spread of times was compressed, T ∝ (c·g)^(−0.4)
  roughly: weaker levels were acquired soon after the strongest (at
  g = (1, 1, 4), times 2.4, 2.5, 2.1 against the linear network's 5.5,
  5.5, 1.5), so 18 E1 cells and 34 of 49 E2 cells were simultaneous.
- **Transition.** In NTK parametrization the target order held at width
  64, faded at 256 and was gone at 1024 and 4096. In standard
  parametrization at width 64 it held at every initial scale from 0.003
  to 3.

## What it can show

A documented run of a stated design, so it shows what these learners did
on these data. It shows that in this family the order of acquisition is
not fixed by the tree: the same tree gives coarse-first, fine-first,
simultaneous or mixed acquisition according to where the strength sits,
and the same data give different phases for different learners, because
a kernel reads only the input strengths and a deep linear network the
product. It cannot show what happens off tree symmetry, where
[K, P_ℓ] ≠ 0, nor for sampled or noisy items, hidden-layer decoders,
larger trees, other optimizers or bigger networks; and it does not
explain the ReLU network's compression or the three-layer network's
weighting.
