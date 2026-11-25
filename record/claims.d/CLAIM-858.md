---
number: 858
status: Proposed
formerly:
- CLAIM-tmpfwwrf
title: 'BTW sandpile avalanches follow a power law'
statement: >-
  In the two-dimensional Bak–Tang–Wiesenfeld sandpile, driven one grain at a
  time with open boundaries and nothing tuned, the avalanche-size
  distribution is a power law whose cutoff grows with lattice size, roughly
  as L^2.5 between L = 16 and 128, with an apparent exponent near 1.1 that
  drifts upward with L
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A correct implementation of the same rules (topple at z ≥ 4, four
  neighbours +1, grains lost at the open boundary, one grain at a uniform
  random site per step, full relaxation between grains, transients
  discarded) whose avalanche-size cutoff, measured as ⟨s²⟩/⟨s⟩ or as the
  size where the complementary distribution falls below 10^(−4), does not
  grow with L over the same range; or whose mean avalanche size departs
  from the exact value (1/L²)·1ᵀΔ^(−1)1 given below, which would show this
  simulation wrong.
tags:
- complex-systems
- natural-sciences
date: '2026-11-22'
line:
- formal-apparatus
grounds:
- LIT-2992
bears_on:
- QUESTION-508
corroborates:
- CLAIM-841
summary: >-
  A reproduction, filling the gap that Bak, Tang and Wiesenfeld ([LIT-2992](../literature.d/LIT-2992.md))
  assert their cutoff is finite-size "as we checked by comparing
  simulations for different array sizes" (p. 383) and show no data. The
  2-D sandpile, slowly driven, at L = 16, 32, 64 and 128: the mean
  avalanche size matches Dhar's exact value to within 0.2 per cent at
  every size; the cutoff ⟨s²⟩/⟨s⟩ goes 92, 467, 2,607, 15,822, growing as
  L^2.48 (local slopes 2.34, 2.48, 2.60), and the size at which the
  complementary distribution falls below 10^(−4) as L^2.58; the
  log-binned slope below the cutoff gives τ ≈ 1.05, 1.07, 1.10 at L = 32,
  64, 128, and the scaling relation τ = 2 − 2/D gives 1.19. Nothing was
  tuned. It meets the promote_when of [THEORY-2179](../theory.d/THEORY-2179.md) for the 2-D case.
  The wording is the assistant's (Claude, in this session); adopting it
  is the owner's call.
---
<!-- inactive-ok-file: THEORY-2179 CLAIM-841 CLAIM-803 — Proposed or new; the reading this reproduction checks, the argument filed with it, and the claims it bears on -->

# CLAIM-858: BTW sandpile avalanches follow a power law

## The gap it fills

Bak, Tang and Wiesenfeld ([LIT-2992](../literature.d/LIT-2992.md), [NOTE-2269](../notes.d/NOTE-2269.md)) read criticality off a
straight log-log line over two decades on a 50 × 50 lattice and say "The
falloff at the largest cluster sizes is due to finite-size effects, as we
checked by comparing simulations for different array sizes" (p. 383),
with no data for the comparison. That check is the one [LEAD-211](../leads.d/LEAD-211.md) and
[CLAIM-803](CLAIM-803.md) treat as the dynamical test of a critical power law. This claim
runs it.

## The run (the assistant's, with python3 -I and numpy)

- **Rules.** An L × L grid of integers z, all zero at the start. Each step
  adds one grain at a uniformly random site; every site with z ≥ 4
  topples, losing 4 and giving 1 to each neighbour, grains crossing the
  edge are lost; toppling repeats until every z < 4. The avalanche size s
  is the number of topplings. Topplings are done in parallel sweeps
  (each unstable site topples ⌊z/4⌋ times per sweep), which by the
  abelian property gives the same final state and the same count.
- **Protocol.** The first 4L² grains are discarded as transient; then
  10⁶ grains at L = 16, 5 × 10⁵ at 32, 2 × 10⁵ at 64 and 10⁵ at 128 are
  recorded, seeds 11 to 14. Wall time 1.3, 1.6, 2.8 and 8.4 minutes, run side by side.
- **Check of the code.** The mean number of topplings per added grain is
  known exactly (Dhar): ⟨s⟩ = (1/L²)·1ᵀΔ^(−1)1, Δ the lattice Laplacian
  with open boundaries, computed here by separation of variables. Exact:
  11.34, 40.58, 153.04, 593.89. Simulated: 11.3, 40.6, 153.1, 593.6.
- **The script** (btw.py, analyse.py and dhar.py, about 80 lines in all)
  is kept in the session's scratchpad, not in the repository; it is
  described fully above and reruns in minutes.

## Results

| L | grains | P(s > 0) | ⟨s⟩ | ⟨s²⟩/⟨s⟩ | s where P(S ≥ s) < 10⁻⁴ | largest s | τ, log-binned slope |
|---|---|---|---|---|---|---|---|
| 16 | 10⁶ | 0.409 | 11.3 | 92 | 402 | 522 | (window too short) |
| 32 | 5 × 10⁵ | 0.426 | 40.6 | 467 | 2,170 | 3,279 | 1.05 |
| 64 | 2 × 10⁵ | 0.437 | 153.1 | 2,607 | 13,573 | 15,026 | 1.07 |
| 128 | 10⁵ | 0.442 | 593.6 | 15,822 | 84,693 | 106,525 | 1.10 |

Moments are over avalanches with s ≥ 1; ⟨s⟩ in the fourth column is over
all grains. τ is the slope of the log-binned density over
10 ≤ s ≤ s₄/30, s₄ the size in the sixth column.

- **The cutoff grows with L.** ⟨s²⟩/⟨s⟩ rises by factors 5.08, 5.58 and
  6.07 per doubling of L, local exponents 2.34, 2.48 and 2.60; a fit over
  all four sizes gives D ≈ 2.48. The 10⁻⁴ size grows as L^2.58. The
  exponents still rise with L, so these are effective values, not the
  asymptotic D.
- **The bulk is a power law** with an apparent τ of 1.05 to 1.10 that
  drifts upward with L. With ⟨s⟩ ∝ L² (slope 1.90 here, 2 asymptotically)
  and finite-size scaling P(s) = s^(−τ) f(s/L^D), the relation
  τ = 2 − 2/D gives 1.19 at D = 2.48. The two estimates disagree by about
  0.1, the size of the corrections to scaling at these lattice sizes;
  neither is a measurement of the asymptotic τ.
- **Nothing was tuned.** The run starts from an empty grid, far from the
  stationary state, and the drive fills it; the mean heights of the final
  configurations were 2.00, 2.08, 2.11 and 2.11. The only parameter, the
  threshold, shifts z and nothing else, as the letter says. Other
  starting configurations were not tried.

## What it does not say

- Not the letter's exponent. Its τ ≈ 0.98 counts sites affected by one
  probe of a pile relaxed from z ≫ K; this counts topplings under slow
  drive, a different observable and protocol.
- Not that the sandpile is critical in every sense. A cutoff growing with
  system size is one discriminating observation among those [CLAIM-841](CLAIM-841.md)
  lists; no data collapse, no response to a control parameter
  and no second observable was tested here.
- Not the asymptotic exponents, which these sizes cannot give. The upward
  drift of both τ and D shows corrections to scaling at work; the record
  holds no reading on the sandpile's exponents beyond the letter.
- Not anything about real systems. A model shows a cutoff that grows with
  size; whether a physical avalanche record does is [LEAD-211](../leads.d/LEAD-211.md)'s question.
