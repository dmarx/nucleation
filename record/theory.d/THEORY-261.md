---
number: 261
status: Proposed
formerly:
- THEORY-tmpfdzw6
promote_when: >-
  A reading of Chou (1989) or Keeler (1988), or of a simulation of the
  basic design at M of 10⁵ or more, confirming that with uniform random
  data and exact cues the fidelity follows Φ(ρ) with
  ρ² = pM/[1 + pT(1 + p²M)], that the best p is near (2MT)^−1/3, and that
  the number of words stored at fixed fidelity grows in proportion to M
  with N held fixed. It is refuted if capacity at fixed fidelity
  saturates in M at fixed N, or if the measured optimum p differs from
  (2MT)^−1/3 by more than the Poisson approximation can account for.
  Results for noisy cues or clustered data cannot settle it, since the
  claim is stated for neither.
title: 'In sparse distributed memory, recall of uniform random data is a signal-to-noise problem whose optimum activates about (2MT)^-1/3 of the hard locations, and capacity then grows with the number of hard locations, to about a tenth of them at 0.999 bit fidelity, not with the word length'
version: 1
tags:
- information-retrieval
- cognition
- neuroscience
date: '2026-10-14'
source:
- LIT-921
summary: >-
  Kanerva (1992), [LIT-921](../literature.d/LIT-921.md), §§3.5–3.7, read in full in [NOTE-779](../notes.d/NOTE-779.md), after
  Jaeckel (1989a). An approximate derivation for uniform random data and
  exact retrieval cues. It does not cover noisy cues, which lower
  capacity, or clustered data, which the uniform design handles badly,
  and it does not contain the critical-distance analysis that is
  sometimes attributed to it.
---
<!-- inactive-ok-file: CLAIM-180 — Proposed; open, and cited as open: a thesis of the nucleating-argument line under test -->
<!-- inactive-ok-file: LIT-928 — Deferred, unread; Kanerva's book, named as where the critical distance is derived, not leaned on -->

# THEORY-261: In sparse distributed memory, recall of uniform random data is a signal-to-noise problem whose optimum activates about (2MT)^-1/3 of the hard locations, and capacity then grows with the number of hard locations, to about a tenth of them at 0.999 bit fidelity, not with the word length

## Source

Pentti Kanerva (1992), "Sparse Distributed Memory and Related Models",
RIACS TR 92.10, [LIT-921](../literature.d/LIT-921.md), §§3.5–3.7, read in full in [NOTE-779](../notes.d/NOTE-779.md). The
analysis follows Jaeckel (1989a).

## What was actually shown

An approximate derivation. M hard locations with uniform random
addresses; T stored words, uniform random; each cue activates a location
with probability p. Retrieving a bit by its exact storage address, the
sum over activated locations has mean μ = pM (the target's own copies)
and variance σ² = pM[1 + pT(1 + p²M)], treating the overlap sizes as
independent Poisson variables. Bit fidelity is φ = Φ(μ/σ). Maximising
μ²/σ² over p gives p = (2MT)^−1/3. Capacity τ = T_max/M at fidelity φ
satisfies [Φ⁻¹(φ)]² = 1/[1/(pM) + τ(1 + p²M)], which tends to
τ = 1/[Φ⁻¹(φ)]² as M grows: 0.105 at φ = 0.999, and 0.096 for M = 10⁶.
The word length N does not appear, because addressing through the fixed
matrix A expands the input to M dimensions; the report sets this against
the Hopfield net, whose capacity "is limited by the word size".

The derivation could have failed: the cross-talk need not cancel, and
without the expansion the capacity would scale with N, as it does for a
correlation-matrix memory addressed directly by its inputs.

## What this does not say

- **Not for noisy cues.** The analysis uses the exact storage address.
  With approximate cues signal, noise and their ratio all fall, the best
  p is larger (by less than a factor of two), and capacity "goes down";
  the report does not compute by how much.
- **Not for real data.** Clustered data waste most uniformly placed
  locations (§8). The ten-per-cent figure is a baseline, and Kanerva's
  practical guide is 1–5% of M.
- **Not the critical distance.** How far a cue can be from its target and
  still converge under iterated reads is not analysed here, only
  illustrated (Figs. 2-1, 2-2). [LIT-269](../literature.d/LIT-269.md) and its reading [NOTE-242](../notes.d/NOTE-242.md) bear on
  that, and Kanerva's book ([LIT-928](../literature.d/LIT-928.md)) derives it.
- **Not a free lunch on hardware.** Capacity per storage element is the
  same as the Hopfield net's (Keeler 1988, cited, not shown); SDM buys
  independence from N with many more counters.
- **Not a claim about brains.** The cerebellar mapping is an outline with
  named discrepancies.

## Connections

- **[THEORY-272](THEORY-272.md)** holds Hopfield's attractor memory, whose capacity
  of about 0.15N the report equates with fidelity 0.995 at the same
  capacity per storage element.
- **[CLAIM-180](../claims.d/CLAIM-180.md)** uses SDM as its picture of retrieval by content. This
  account gives the load side of that picture: how many items a memory
  of a given size can hold before exact-cue recall fails. The report's
  zero-radius limit, an ordinary RAM, is the addressed case the claim
  contrasts with content.
