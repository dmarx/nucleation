---
number: 1500
status: Proposed
formerly:
- THEORY-tmp4fe10
promote_when: >-
  The published Nature Photonics version checked against arXiv v3 for the
  existence window (SI eq. 18), the attribution of the transmission steps
  to soliton number and the sentence on random seeding; and a reading of
  the cited existence analysis of the driven, damped nonlinear Schrödinger
  equation (Barashenkov and Smirnov 1996, the paper's ref. 30) confirming
  the window √3 < ζ0 < π²f²/8 under the conditions the paper uses.
title: 'Temporal dissipative solitons in a continuously pumped Kerr microresonator, held by the pump against cavity loss, exist only in a window of normalized detuning between √3 and π²f²/8, form spontaneously from noise-seeded modulation when the pump laser is swept from the upper onto the lower branch of the Kerr-bistable resonance, show as discrete steps in transmission, one per soliton number, whose number varied between simulated scans with the random seeding, and persist with a shape fixed by resonator and pump until the pump is switched off or the detuning is pushed beyond the small thermal triangles'
version: 1
tags:
- natural-sciences
- complex-systems
date: '2026-11-06'
source:
- LIT-2204
bears_on:
- QUESTION-281
- QUESTION-085
- QUESTION-398
summary: >-
  Herr, Brasch, Jost, Wang, Kondratiev, Gorodetsky and Kippenberg (2014),
  [LIT-2204](../literature.d/LIT-2204.md), read in [NOTE-1692](../notes.d/NOTE-1692.md) from arXiv v3; experiment in one
  MgF2 resonator, simulation of the coupled-mode (Lugiato-Lefever)
  equations without thermal effects, and approximate analytics. Proposed:
  the window rests on an infinite-domain analysis the record has not read,
  and the equations were read from a page image because extraction drops
  square roots. It does not say that formation shows hysteresis (no
  reverse sweep is reported), how fast a soliton vanishes after switch-off
  (not measured), or how the number of solitons varies between
  experimental runs (reported for simulations only).
---
# THEORY-1500: Temporal dissipative solitons in a continuously pumped Kerr microresonator, held by the pump against cavity loss, exist only in a window of normalized detuning between √3 and π²f²/8, form spontaneously from noise-seeded modulation when the pump laser is swept from the upper onto the lower branch of the Kerr-bistable resonance, show as discrete steps in transmission, one per soliton number, whose number varied between simulated scans with the random seeding, and persist with a shape fixed by resonator and pump until the pump is switched off or the detuning is pushed beyond the small thermal triangles

## Source

Herr et al. (2014), [LIT-2204](../literature.d/LIT-2204.md); read in [NOTE-1692](../notes.d/NOTE-1692.md) (arXiv:1211.0733v3).

## What was actually shown

- **Supply.** The solitons "rely on the double balance between parametric
  gain and resonator loss on the one hand and nonlinearity and
  diffraction or dispersion on the other hand" (p. 1); "their persistence
  requires a source of energy for replenishment" (SI §IX).
- **The window** (SI §§II–III, pp. 13–14, equations read from the page
  image): the cw bistability needs ζ0 > √3, and the existence condition
  h > 2γ/π gives ζ0max = π²f²/8 (eq. 18). From an analysis on an infinite
  domain, said to agree with simulations with periodic boundaries for a few
  hundred modes.
- **Formation.** In the experiment the steps begin where the PDH signal
  crosses zero, the effective zero detuning, as the pump is swept down from
  the upper branch onto the lower (p. 2); the ramp runs in that direction
  "in order to first follow the upper branch before jumping onto the lower
  branch" (SI §VI). In simulation the solitons "emerge from the modulated
  intracavity waveform" (p. 3).
- **Steps are soliton numbers.** In simulation each step is a state of
  fewer pulses; analytic step heights (SI eq. 20, linear in N) match the
  simulated steps (p. 3); one, two and five solitons are seen in the
  experiment (Fig. 4).
- **Variation.** "the number and height of steps fluctuate in repeated
  numerical scans as a result of random seeding of the optical modes
  (corresponding to vacuum fluctuations)" (p. 3).
- **Fixed form.** "The complex numbers C1 and C2 are fully determined by
  the resonator parameters and the pump conditions" (p. 3); only N and the
  positions are free.
- **Persistence and its end.** "Once generated, the solitons remain stable
  until the pump laser is switched off" (p. 3), "for hours" (SI §VI); "a
  hypothetical disturbance in the laser detuning larger than the length of
  the small thermal triangles would terminate the soliton operation"
  (p. 4).

## What this does not say

- **Not hysteresis.** Formation depends on the path, upper branch first;
  the paper does not use the word hysteresis and reports no reverse sweep,
  so whether the states hold on sweeping back is not shown.
- **Not a decay law.** No decay after the pump is switched off is
  measured or computed. The end at switch-off is asserted; that it is fast
  follows only from the cavity decay rate (κ/2π = 450 kHz), which is the
  reader's inference, not the authors'.
- **Not experimental statistics.** The run-to-run variation in soliton
  number is shown for simulations; the paper says it agrees with the
  experiment and gives no counts.
- **Not robustness tested.** That the attractor is "highly stable and
  robust against fluctuations" is cited to other work, not tested here;
  noise-driven escape between soliton numbers is not studied.
- **Not a threshold alone.** The range is bounded above as well as below.
- **Not self-maintenance.** Beyond the thermal self-stability, a single
  feedback of the pattern on its own effective detuning, the soliton does
  nothing to keep its supply.
- **Not general.** One resonator, simulations without thermal effects,
  and an approximate soliton solution.
