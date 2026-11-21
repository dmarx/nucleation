---
number: 2158
status: Proposed
formerly:
- THEORY-tmpr5fuq
promote_when: >-
  Theorem 4 and Theorem 7, with the supplement's proofs (§1), confirmed as
  stated, with their conditions, by a second reading of the proofs or by
  an independent derivation or textbook restatement read by the record:
  that for i.i.d. input, a linear readout of N variables and infinite data
  the capacities for orthogonal functions of past inputs sum to at most N,
  and that with fading memory, N linearly independent variables and a
  complete basis they sum to N. Not met by simulations showing totals near
  N, which the paper already has.
title: "Dambre and colleagues show that for a dynamical system driven by independent identically distributed input and read out linearly from N observed variables, the capacities to reconstruct orthogonal functions of past inputs sum to at most N, and to exactly N over a complete basis when the system has fading memory and its variables are linearly independent, so that such systems differ in how they divide a fixed capacity between memory and nonlinear computation, not in its total"
version: 1
tags:
- complex-systems
- information-theory
date: '2026-11-21'
source:
- LIT-2971
bears_on:
- QUESTION-507
summary: >-
  Dambre, Verstraeten, Schrauwen and Massar (2012), [LIT-2971](../literature.d/LIT-2971.md), read in
  [NOTE-2244](../notes.d/NOTE-2244.md) with the supplement. The bound needs only i.i.d. input, a
  linear readout and infinite data; fading memory and full rank are the
  conditions for equality; unobserved noise is a further input and takes
  part of the total. The record uses it for [CLAIM-809](../claims.d/CLAIM-809.md)'s bound
  ([ARG-128](../arguments.d/ARG-128.md)) and [CLAIM-814](../claims.d/CLAIM-814.md), which is an instance of Theorem 7
  ([ARG-146](../arguments.d/ARG-146.md)). Its edge is the undriven system's stability edge, and its
  sweep is input scaling. Proposed until the theorems are confirmed.
---
<!-- inactive-ok-file: CLAIM-809 CLAIM-814 ARG-128 ARG-146 — Proposed; the claims that use this reading, and the arguments of 2026-11-21 -->

# THEORY-2158: Dambre and colleagues show that for a dynamical system driven by independent identically distributed input and read out linearly from N observed variables, the capacities to reconstruct orthogonal functions of past inputs sum to at most N, and to exactly N over a complete basis when the system has fading memory and its variables are linearly independent, so that such systems differ in how they divide a fixed capacity between memory and nonlinear computation, not in its total

## Source

Dambre, Verstraeten, Schrauwen and Massar, Scientific Reports 2: 514
(2012), [LIT-2971](../literature.d/LIT-2971.md), read in full with its Supplementary Information in
[NOTE-2244](../notes.d/NOTE-2244.md).

## The account

The capacity of a system X for a function z of past inputs is
C[X, z] = 1 − min MSE/⟨z²⟩ over linear readouts of its N observed
variables. For i.i.d. input, orthogonal z_l with finite fourth moments and
T → ∞, Σ_l C[X, z_l] ≤ N whatever the system (Theorem 4). If the system has
fading memory, its N variables are linearly independent, and the z_l tend
to a complete basis of the Hilbert space of fading-memory functions, the
sum tends to N (Theorem 7). So every such system has the same total; they
differ in how it is spread between linear memory and nonlinear functions.
With unobserved noise, a second i.i.d. input, the theorem holds over
functions of both inputs, and the measurable capacities, functions of the
signal alone, sum to less than N.

What could have come out otherwise: in simulation (a logistic map, a
50-node echo state network, a Gray–Scott reaction–diffusion system,
Legendre bases, T = 10⁶) the measured total could have fallen well short
of N inside the stable regime. It stays near N up to the undriven system's
bifurcation for small input scaling and drops after it; as input scaling
grows, linear memory gives way to nonlinear capacity.

## What this does not say

- Not that capacity peaks at a transition: the total is flat at N inside
  the fading-memory regime and falls past the edge. Its "edge" is the
  undriven system's loss of linear stability, not a collective critical
  point.
- Not how the allocation moves with distance from the edge: the paper
  sweeps input scaling and sampling period at a fixed spectral radius.
- Not anything for correlated input, where it calls the bound "largely a
  theoretical insight", or for nonlinear readouts.
- Not which allocation is useful: "Some systems may carry out more
  interesting computations than others".
