---
status: Proposed
promote_when: >-
  An independent proof or a simulation of a large population with
  Lorentzian frequencies, started off the manifold, confirms what the
  title says: that the order parameter converges to the reduced dynamics
  whenever the frequency spread is nonzero, with no further condition on
  rates, and that the distribution itself need not converge. A sharper
  rate than the bound Δ is not required.
title: 'Ott and Antonsen show that for infinitely many phase oscillators whose phase velocity carries only the first harmonic of the phase, with a Lorentzian frequency distribution of nonzero width Δ, the order parameter is attracted at long times to the dynamics on their reduced manifold, by phase mixing at a rate of at least Δ and with no condition on any other rate, though the distribution itself need not converge; with Δ = 0, motion off the manifold can persist'
version: 1
tags:
- complex-systems
- mathematics
date: '2026-11-22'
source:
- LIT-tmpd7koy
extends:
- THEORY-tmpmvcnr
bears_on:
- QUESTION-391
summary: >-
  Ott and Antonsen (2009), [LIT-tmpd7koy](../literature.d/LIT-tmpd7koy.md), read in full in [NOTE-tmp5oph4](../notes.d/NOTE-tmp5oph4.md),
  as a supplement to the 2008 paper ([THEORY-tmpmvcnr](THEORY-tmpmvcnr.md)), whose open question
  it answers for the order parameter. The closed law is reached from
  outside the manifold whenever frequencies are spread; it fails without
  spread ([QUESTION-391](../questions.d/QUESTION-391.md)). It is what makes the 2008 reduction a serious
  candidate defeater of [CLAIM-478](../claims.d/CLAIM-478.md); the verdict is filed as alternatives
  ([CLAIM-tmpa694z](../claims.d/CLAIM-tmpa694z.md), [CLAIM-tmpervl4](../claims.d/CLAIM-tmpervl4.md)). Proposed until the attraction is
  confirmed independently.
---
<!-- inactive-ok-file: THEORY-tmpmvcnr CLAIM-tmpa694z CLAIM-tmpervl4 — Proposed or new; the 2008 reading and the verdict filed from these -->
<!-- inactive-ok-file: CLAIM-478 — Proposed; the claim this reading was read against -->

# THEORY-tmp0d58z: Ott and Antonsen show that for infinitely many phase oscillators whose phase velocity carries only the first harmonic of the phase, with a Lorentzian frequency distribution of nonzero width Δ, the order parameter is attracted at long times to the dynamics on their reduced manifold, by phase mixing at a rate of at least Δ and with no condition on any other rate, though the distribution itself need not converge; with Δ = 0, motion off the manifold can persist

## Source

Ott and Antonsen (2009), "Long Time Evolution of Phase Oscillator Systems",
*Chaos* 19: 023117, [LIT-tmpd7koy](../literature.d/LIT-tmpd7koy.md), read from the arXiv preprint in
[NOTE-tmp5oph4](../notes.d/NOTE-tmp5oph4.md).

## The account

Split the distribution's positive-harmonic part into the manifold's
inhomogeneous solution and a homogeneous remainder. The remainder need not
vanish: with no coupling each harmonic keeps its size (eq. 11). But its
frequency-weighted integral, which is what enters the order parameter,
decays, as rotating components with different frequencies dephase; for a
Lorentzian of width Δ the n-th harmonic's integral decays as e^{−nΔt}
(eq. 13). With coupling, an integration along characteristics bounds the
decay exponent below by (t − T)Δ for any time course of the mean field, so
the order parameter obeys the reduced equation at long times whenever
Δ > 0. The manifold is "inertial" in a frequency-weighted metric, not for
the distribution. With Δ = 0, as in Watanabe and Strogatz's identical
oscillators, long-time motion off the manifold exists.

## Bearing

- [QUESTION-391](../questions.d/QUESTION-391.md): the reduced law ceases to hold as the frequency spread
  vanishes, when phase mixing stops; an instance of an effective law
  failing as suppressed degrees of freedom come back.
- [CLAIM-478](../claims.d/CLAIM-478.md)'s defeater (a): the attraction's condition names no ratio of
  rates. Whether that meets (a) is contested; see [CLAIM-tmpa694z](../claims.d/CLAIM-tmpa694z.md) and
  [CLAIM-tmpervl4](../claims.d/CLAIM-tmpervl4.md).
