---
number: 186
status: Open
formerly:
- QUESTION-tmpbr2ll
title: "In a second system with a known reciprocal coupling and one unit driven at graded strengths, does the measured transfer-entropy asymmetry grow to one-way flow under strong drive while the coupling stays symmetric?"
version: 1
tags:
- information-theory
- causality
- natural-sciences
- thermodynamics
date: '2026-10-19'
line: 'distributed-agency'
summary: >-
  The promotion condition formerly on [THEORY-275](../theory.d/THEORY-275.md), moved here when
  [THEORY-275](../theory.d/THEORY-275.md) was narrowed to the one bead system of [LIT-947](../literature.d/LIT-947.md) and promoted
  on 2026-10-19 ([ADR-047](../decisions.d/ADR-047.md) v3). In that system the one-way regime under
  strong drive is a simulation of the fitted model, not a measurement.
---

# QUESTION-186: In a second system with a known reciprocal coupling and one unit driven at graded strengths, does the measured transfer-entropy asymmetry grow to one-way flow under strong drive while the coupling stays symmetric?

## Why it is a question

In two hydrodynamically coupled beads, with one trap moved by a recorded
drive, delayed mutual information and transfer entropy read the
inter-bead flow both ways at moderate drive. In numerics of the fitted
linear model they read it one way at strong drive. The coupling tensor
stays symmetric throughout ([THEORY-275](../theory.d/THEORY-275.md), from [LIT-947](../literature.d/LIT-947.md) read in [NOTE-788](../notes.d/NOTE-788.md)). The
strong-drive regime is beyond that experiment, and the system is linear,
Gaussian and two-body. Whether directional information measures in
general follow a one-sided drive rather than the coupling's symmetry is
therefore open. Until 2026-10-19 this was [THEORY-275](../theory.d/THEORY-275.md)'s promote_when.

## What would answer it

A second system, experimental or exactly solvable, in which units with a
known reciprocal coupling are driven on one side at graded strengths. The
transfer-entropy asymmetry between them must grow with the drive to
one-way flow while the coupling stays symmetric, and it must be measured,
not only simulated, in the strong-drive regime. An exact derivation of
the strong-drive limit in the linear Gaussian pair would settle that case
analytically. There, delayed-MI asymmetry is c_xy(τ)² − c_yx(τ)².

It would answer no if directional measures between reciprocally coupled
units stay symmetric under strong one-sided drive, or if they recover the
coupling's symmetry without the drive being recorded or intervened on.

What would not answer it: systems whose coupling is itself asymmetric, or
further cases in the moderate regime alone, where flow is already two-way.
