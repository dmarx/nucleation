---
number: 654
status: Active
formerly:
- THEORY-tmpwb4fb
title: "For full-state linear-quadratic regulation of a single-input plant, the return-difference identity keeps the sensitivity at or below 1 at every frequency, so the loop tolerates any gain increase, a gain cut to one half and at least 60° of phase error for any Q ≥ 0 and r > 0; the guarantee does not carry over when the state is replaced by an observer's estimate"
version: 1
tags:
- mathematics
- operations-research
date: '2026-10-16'
source:
- LIT-051
summary: >-
  Başar, Meyn & Perkins (2020), [LIT-051](../literature.d/LIT-051.md), graduate course notes read in full
  in [NOTE-062](../notes.d/NOTE-062.md), with every worked example recomputed. §10.6 derives |1 +
  L(jω)|² = 1 + |P(jω)|²/r ≥ 1 for the full-state loop, hence |S| ≤ 1 and
  the classical margins. The derivation is for one input; the multi-input
  version needs more, which the notes do not discuss. The Pendubot thread
  shows a controllable, observable plant whose one-sensor observer-based
  design has gain margin below 10⁻². The result is Kalman's and standard;
  the notes are an adequate free citation for it.
supports:
- CLAIM-tmpilfhr
---

<!-- inactive-ok-file: THEORY-325 — Proposed; named in Connections for contrast, not leaned on -->

# THEORY-654: For full-state linear-quadratic regulation of a single-input plant, the return-difference identity keeps the sensitivity at or below 1 at every frequency, so the loop tolerates any gain increase, a gain cut to one half and at least 60° of phase error for any Q ≥ 0 and r > 0; the guarantee does not carry over when the state is replaced by an observer's estimate

## Source

Başar, Meyn & Perkins (2020), *Lecture Notes on Control System Theory and
Design*, arXiv:2007.01367v2, [LIT-051](../literature.d/LIT-051.md), read in full in [NOTE-062](../notes.d/NOTE-062.md). The reader
recomputed the worked examples, including the Pendubot plant, its LQR poles
and its compensator.

## What was actually shown

**The setting.** Continuous-time, deterministic, linear time-invariant
plant ẋ = Ax + Bu with one input, cost weights Q ≥ 0 and r > 0, and the
infinite-horizon LQR gain K from the algebraic Riccati equation. The loop
gain broken at the input is L(s) = K(sI − A)⁻¹B.

**The identity (§10.6, eqs. 10.27–10.32).** The return-difference equation
gives |1 + L(jω)|² = 1 + |P(jω)|²/r ≥ 1 at every frequency, with P the
transfer function from input to the weighted output. So the sensitivity
S = 1/(1 + L) satisfies |S(jω)| ≤ 1. The Nyquist plot stays outside the
unit disk around −1, which gives infinite gain margin, tolerance of the
gain halved, and phase margin of at least 60° (p. 191). The same chapter
gives the symmetric root locus and Kalman's inequality.

**The counterexample to carrying it over (Chs 9–10).** The Pendubot is a
two-link underactuated pendulum. With one sensor it is controllable and
observable, but its transfer function has a zero at s ≈ +6.54 between two
unstable poles. Any stabilising compensator must then itself be unstable,
and the observer-based design has a compensator pole at s ≈ 46.4. Its gain
margin is "less than 10⁻²" (p. 192). [NOTE-062](../notes.d/NOTE-062.md) found that the printed
compensator, rounded to its printed precision, does not stabilise the
printed plant, which makes the fragility sharper than the notes say.
Full-state LQR on the same plant keeps the margins above.

**What could have come out otherwise.** The return difference could have
dipped below 1 at some frequency for some choice of Q, which would have
meant a margin that depends on the weights. It cannot, for any Q ≥ 0 and
r > 0.

## What this does not say

- **That the margins hold for multi-input LQR as stated.** The derivation is
  for a single input. The multi-input version needs more, for example a
  diagonal R, and the notes do not discuss it ([NOTE-062](../notes.d/NOTE-062.md), C5).
- **That an observer-based LQG design inherits them.** The Pendubot shows it
  does not. Controllable-and-observable says nothing about robustness; zeros
  and sensor choice do.
- **That the infinite-horizon LQR exists in the case used.** Existence,
  uniqueness and stability under stabilisability and detectability (Thm
  10.6) are stated without proof in the notes.
- **That the notes bridge control and reinforcement learning.** The 2024
  preface promises it; the text has no RL, no stochastic control and no
  discrete-time Riccati equation ([NOTE-062](../notes.d/NOTE-062.md), corrections).
- **That "60%" is meant.** p. 187 prints "phase margin at least 60%"; p. 191
  has 60°.

## Connections

- [THEORY-325](THEORY-325.md) holds that a non-normal linear system stable at every instant
  can be destabilised by time dependence. The margins here are for a fixed
  LTI loop and say nothing about time-varying perturbations of A.
