---
number: 261
status: Active
formerly:
- THEORY-tmpfdzw6
title: "In sparse distributed memory, recall of uniform random data from exact cues is a signal-to-noise problem whose optimum activates about (2MT)^-1/3 of the hard locations, and capacity then grows in proportion to the number of hard locations, rising toward about a tenth of them at 0.999 bit fidelity, not with the word length"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-261 (batch 050). The former promote_when accepted a simulation of
    the basic design at M of 10^5 or more; the record ran one (dated note
    below), and it confirms the Phi(rho) fidelity, the optimum near
    (2MT)^-1/3, and capacity in proportion to M with the word length fixed.
    The title now says exact cues, as the derivation assumes, and that
    capacity rises toward a tenth, since at M up to 2 x 10^5 it measured
    0.08 to 0.095.
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
<!-- inactive-ok-file: LIT-928 — Unavailable, unread; Kanerva's book, named as where the critical distance is derived, not leaned on -->

# THEORY-261: In sparse distributed memory, recall of uniform random data from exact cues is a signal-to-noise problem whose optimum activates about (2MT)^-1/3 of the hard locations, and capacity then grows in proportion to the number of hard locations, rising toward about a tenth of them at 0.999 bit fidelity, not with the word length

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

## Note of 2026-10-20: the basic design, simulated

Promotion audit, batch 050. The simulated design is Kanerva's basic SDM:

- M hard locations with uniform random n-bit addresses (n = 256, with
  n = 128 as a check).
- Activation is the Hamming ball of radius r, so p = P(Bin(n, ½) ≤ r).
- T uniform random N-bit words (N = 64, with N = 256 as a check) are
  written at uniform random addresses into ±1 counters.
- Each word is read at its exact storage address, and each bit is the sign
  of the summed counters. Fidelity is measured over 2,000 reads.

**Fidelity follows Φ(ρ), ρ² = pM/[1 + pT(1 + p²M)].**

| M = 10⁵ | T = 6,000 | 8,000 | 9,000 | 10,000 |
|---|---|---|---|---|
| measured | 0.99991 | 0.99953 | 0.99897 | 0.99864 |
| predicted | 0.99985 | 0.99929 | 0.99879 | 0.99811 |

At heavy load (T = 25,000), over six radii with p from 1.1 × 10⁻⁴ to
1.1 × 10⁻³, measured fidelity ran 0.962 to 0.973 against a predicted
0.956 to 0.971. The formula errs in two directions:

- It is slightly pessimistic at small p. It counts the variance of the
  target's own activation count as additive noise, but that count
  multiplies the correct bit.
- It is slightly optimistic at large p. Overlaps of Hamming balls vary
  more than Poisson.

**The optimum is near (2MT)^−1/3.** At M = 10⁵ and T = 25,000, measured
fidelity is highest at p = 4.4 × 10⁻⁴, and the formula's at 6.9 × 10⁻⁴
(adjacent radii). (2MT)^−1/3 = 5.85 × 10⁻⁴ lies between them.

**Capacity grows in proportion to M.** The largest T with fidelity
≥ 0.999 at each size:

| M | 25,000 | 50,000 | 100,000 | 200,000 |
|---|---|---|---|---|
| T | ≈ 2,000 | ≈ 4,000 | ≈ 8,900 | ≈ 19,000 |
| τ = T/M | 0.080 | 0.080 | 0.089 | 0.095 |

These rise toward the derivation's limit of 0.105. Word length does not
enter: N = 256 against N = 64 at M = 10⁵, T = 6,000 gave 0.99983 against
0.99991, within sampling error. An address length of 128 instead of 256
also changed nothing.

Chou (1989) and Keeler (1988) were not read. The simulation is the
evidence the former promote_when named as sufficient.
