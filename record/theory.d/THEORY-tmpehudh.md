---
status: Proposed
promote_when: >-
  A held reading, or a reproduction in the record, confirms for the BTW
  sandpile that the avalanche-size distribution is a power law whose
  cutoff grows with lattice size, reached from generic initial conditions
  with no tuned parameter.
title: "Bak, Tang and Wiesenfeld propose that spatially extended threshold systems in two or more dimensions relax to a critical state as an attractor, with no parameter tuned, because relaxation stops where clusters of minimally stable sites cease to percolate; in a sandpile automaton they find power-law cluster sizes (τ ≈ 0.98 in 2D, 1.35 in 3D) cut off by the system size, and spectra ω^(−1.58) and ω^(−1.1), and conjecture that this is the common mechanism of 1/f noise and fractals"
version: 1
tags:
- complex-systems
- natural-sciences
date: '2026-11-22'
source:
- LIT-2992
bears_on:
- QUESTION-508
corroborates:
- CLAIM-841
summary: >-
  Bak, Tang and Wiesenfeld (1987), LIT-2992, read in full in
  NOTE-tmpnl00y. The founding letter of self-organized criticality: a
  critical point "reached by starting far from equilibrium", with the
  percolation-of-minimal-stability heuristic, the sandpile automaton, and
  power laws judged by eye over two decades. It states no slow-drive,
  time-scale or conservation condition. It corroborates CLAIM-841's
  bullet that SOC reaches a critical point without outside tuning
  (ARG-tmp1zu0m), and its finite-size cutoff, asserted without data, is
  reproduced in CLAIM-tmpfwwrf (ARG-tmpb6zg7). Proposed until the reading
  is confirmed.
---
<!-- inactive-ok-file: CLAIM-841 CLAIM-tmpfwwrf ARG-tmp1zu0m ARG-tmpb6zg7 — Proposed or new; the claim this reading corroborates, the reproduction and the arguments filed with it -->

# THEORY-tmpehudh: Bak, Tang and Wiesenfeld propose that spatially extended threshold systems in two or more dimensions relax to a critical state as an attractor, with no parameter tuned, because relaxation stops where clusters of minimally stable sites cease to percolate; in a sandpile automaton they find power-law cluster sizes (τ ≈ 0.98 in 2D, 1.35 in 3D) cut off by the system size, and spectra ω^(−1.58) and ω^(−1.1), and conjecture that this is the common mechanism of 1/f noise and fractals

## Source

Bak, Tang and Wiesenfeld (1987), "Self-Organized Criticality: An
Explanation of 1/f Noise", Physical Review Letters 59, 381–384,
LIT-2992, read in full from a course copy in NOTE-tmpnl00y.

## The account

"The critical point in the dynamical systems studied here is an attractor
reached by starting far from equilibrium: The scaling properties of the
attractor are insensitive to the parameters of the model" (p. 381). The
system "will become stable precisely at the point when the network of
minimally stable states has been broken down to the level where the noise
signal cannot be communicated through infinite distances" (p. 382); in one
dimension "the dynamics is trivial". The sandpile automaton (z → z − 4,
neighbours +1, z = 0 on the boundary; "There are no parameters since a
shift in K simply shifts z") gives D(s) ~ s^(−τ), τ ≈ 0.98 in 2D and 1.35
in 3D, "linear over two decades"; "The falloff at the largest cluster
sizes is due to finite-size effects, as we checked by comparing
simulations for different array sizes" (p. 383). Lifetimes give
S(ω) ≈ ω^(−1.58) in 2D and ω^(−1.1) in 3D (p. 384).

## What would have come out otherwise

The relaxed state could have had a characteristic cluster size
independent of the lattice; the cluster-size curve could have bent over
well inside the lattice size.

## What it does not license

- That a straight log-log line shows criticality: the paper infers it so
  (p. 383), and the record holds the inference insufficient (CLAIM-841,
  CLAIM-803).
- That slow drive, separated time scales or conservation are the
  conditions for SOC: the paper names none of them.
- Its exponents: τ ≈ 0.98 counts affected sites after a probe of the
  relaxed pile, from 50 × 50 lattices, coarse-grained, with no error
  estimate. The record's reproduction (CLAIM-tmpfwwrf) finds an apparent
  τ near 1.05–1.1 for the toppling count under slow drive.
