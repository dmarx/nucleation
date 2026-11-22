---
number: 209
status: Open
formerly:
- LEAD-tmpng7or
title: 'Write and try a protocol that reads which mechanism maintains an observed power law from how its cutoff, its rescaled distributions, its dynamics and its response to a symmetry-breaking field behave'
version: 1
stage: idea
method:
- formal
- empirical
tags:
- complex-systems
- natural-sciences
- mathematical-statistics
date: '2026-11-21'
line:
- formal-apparatus
advances:
- CLAIM-841
- CLAIM-829
- QUESTION-508
summary: >-
  The exchange "Rich Get Richer Power Laws" offers several tests to tell
  what keeps a power law in place: finite-size scaling and data collapse
  (A8 §6, A12 §8), the behaviour of the cutoff by mechanism (A24 §9), the
  dynamic exponent (A24 §6), probability currents and the time asymmetry
  of trajectories (A24 §1, §10), and the gap a symmetry-breaking field
  opens (A27 §6). It never puts them together, and the one it leans on,
  the cutoff, is a static feature, which the ledgers flag. The lead is to
  write them as one protocol and try it on simulated systems whose
  mechanism is known. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp6jdas THEORY-tmpw4qgu THEORY-tmphcnj3 — Proposed; the readings of 2026-11-22 cited in the notes -->
<!-- inactive-ok-file: CLAIM-841 CLAIM-829 CLAIM-803 CLAIM-846 CLAIM-850 — filed from the same exchange on 2026-11-21, Proposed or Open -->

# LEAD-209: Write and try a protocol that reads which mechanism maintains an observed power law from how its cutoff, its rescaled distributions, its dynamics and its response to a symmetry-breaking field behave

## Sketch

**Why.** [CLAIM-841](../claims.d/CLAIM-841.md) holds that a power law does not show criticality,
and A24 §1 that a stationary histogram cannot name its mechanism. The
exchange offers discriminating observations one at a time; A24 §9's
summary of them ("What is the tail actually measuring?") still reads the
mechanism from a static cutoff. A protocol that uses dynamics and
response as well would make [CLAIM-841](../claims.d/CLAIM-841.md) usable, and test
A10 §8's reading, which [CLAIM-829](../claims.d/CLAIM-829.md) states as the separation-of-scales
reading of the owner's U5, that the extremes near a continuous transition
follow the same law as the bulk: "The extreme events aren't governed by
fundamentally different rules", with A's hedge that this "is not
universally true for all heavy-tailed phenomena". An event above the
extrapolated law, a dragon king, is exactly an extreme with different
rules, and the data collapse is the check that tells the two apart.
[CLAIM-803](../claims.d/CLAIM-803.md) makes the general point that a distribution does not
identify its mechanism; [LEAD-211](LEAD-211.md) is the cutoff row of this lead's
protocol taken alone, as an early-warning sign; this lead subsumes its
cutoff test, and it stays a lead of its own for its comparison with the
variance warning.

**Observations, and what each mechanism predicts.**

| Observation | Tuned criticality | Symmetry (Goldstone, XY) | Flux (turbulence) | Growth (KPZ) | Mixture or heterogeneity |
|---|---|---|---|---|---|
| cutoff as the control parameter moves | grows on approach | none in the phase | set by injection and dissipation scales | none needed | fixed by the spread of rates |
| cutoff with system size L | ∝ L^D, with collapse s^(−τ) f(s/L^D) | ∝ L | fixed by viscous scale | W ∝ L^α | independent of L |
| dynamic exponent z, from C(r, t) = r^(−2Δ) F(t/r^z) | model's z | 1 or 2 by mode | from flux scaling | 3/2 in 1D | none |
| net probability currents, path-space KL(forward ‖ reversed) | zero for an equilibrium point (Ising), nonzero for an absorbing-state one (directed percolation) | zero at equilibrium | nonzero | nonzero | either |
| a small symmetry-breaking field μ | shifts the point | opens a gap, ξ ∼ √ρ_s/μ | no effect expected | depends | no effect |
| odd-order statistics of increments | zero in a Z₂-symmetric equilibrium model | zero (Gaussian) | nonzero (4/5 law) | nonzero skewness | either |

The table is a first draft from A's turns and the assistant's checks in
[CLAIM-846](../claims.d/CLAIM-846.md) and [CLAIM-850](../claims.d/CLAIM-850.md); writing the protocol includes
checking each cell.

**Trial.** Simulate one system per column where the answer is known:
critical branching at several R and sizes; the Gaussian spin-wave field
with and without μ; the linear shell cascade of [CLAIM-850](../claims.d/CLAIM-850.md) and, if
affordable, a shell model of turbulence; a 1D KPZ discretization; an
exponential mixture over a gamma spread of rates. Apply the protocol blind
to each and score how often it names the mechanism. Then add a
dragon-king case (one mechanism for the bulk, another for the top
events) and see whether the collapse check catches it ([CLAIM-829](../claims.d/CLAIM-829.md)).

**What would count.** The protocol names the mechanism in each simulated
case from observations a field study could make. If two columns cannot be
told apart by any row, that pair goes into [CLAIM-841](../claims.d/CLAIM-841.md) as a limit.

**Cost.** A few days of simulation and writing; no outside data. The
trajectory-level rows answer A24 §10's proposal of a "universality of
histories" for these cases only.

## Note of 2026-11-22: Clauset, Shalizi and Newman, read

**Method** (LIT-2987, NOTE-tmphbwdu, THEORY-tmpw4qgu). The protocol's
first step can use their nested likelihood-ratio test of a pure power law
against one with an exponential cutoff (§5.2, Tables 6.2–6.3), which
detects a cutoff in one sample; the cutoff form is "clearly favored" for
fires, flares, earthquakes and web hits (p. 26). The paper has nothing on
how a cutoff scales with system size, which is the protocol's own
step.
