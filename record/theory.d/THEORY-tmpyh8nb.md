---
status: Proposed
promote_when: >-
  An experiment that separates spectral readout from gradient and
  frequency-threshold mechanisms in real axons: impose a periodic
  modulation of motor transport at a chosen frequency and see whether the
  steady length shifts as the model predicts, or show that the axon's
  signalling oscillation period scales with length and that its waveform
  after the first filtering stage changes with period. Refuted if imposed
  frequencies leave length unchanged or the oscillation is absent. Fitting
  the model's parameters to growth curves cannot settle it, nor can the
  qualitative match to "fewer motors, longer axons", which holds in the
  model only below a critical motor influx.
title: "The time-average of a single threshold (Hill) response to a periodic signal is independent of the signal's period for a fixed waveform, so a frequency cannot be read by one sigmoidal stage; two cascaded stages can read it, because the first changes the waveform with period; and a delayed kinesin–dynein signalling loop whose period grows with axon length, read out this way and coupled to protrusion and contraction, can hold an axon at a stable length"
version: 1
tags:
- neuroscience
- natural-sciences
date: '2026-10-16'
source:
- LIT-034
summary: >-
  Folz, Wettmann, Morigi & Kruse (2018; PRE 2019), [LIT-034](../literature.d/LIT-034.md), read in full in
  [NOTE-067](../notes.d/NOTE-067.md). The period independence is proved, for signals that differ by a
  time rescaling only; the two-stage readout is shown numerically and in
  the Heaviside limit; the loop's minimum length and ω ≈ √3 v/L for long
  axons come from linear stability analysis. The length control is a
  lumped delay-differential model with one parameter set and the motor
  velocity v never stated, so its absolute lengths, about 125 µm, cannot be
  reproduced. A proof of mechanism, not a model fitted to axons.
---

# THEORY-tmpyh8nb: The time-average of a single threshold (Hill) response to a periodic signal is independent of the signal's period for a fixed waveform, so a frequency cannot be read by one sigmoidal stage; two cascaded stages can read it, because the first changes the waveform with period; and a delayed kinesin–dynein signalling loop whose period grows with axon length, read out this way and coupled to protrusion and contraction, can hold an axon at a stable length

## Source

Frederic Folz, Lukas Wettmann, Giovanna Morigi and Karsten Kruse (2018),
"The sound of an axon's growth", *Physical Review E* 99, 050401 (2019),
[LIT-034](../literature.d/LIT-034.md), read in full with the SM in [NOTE-067](../notes.d/NOTE-067.md).

## What was actually shown

**One stage cannot read frequency (after Eq. 2).** For a response
f_κ(c) = cⁿ/(κⁿ + cⁿ) and any β > 0,
(1/T)∫₀^T f(c(t))dt = (β/T)∫₀^(T/β) f(c(βt))dt. A periodic input that only
changes period gives the same mean response. In the Heaviside limit the
mean is set by the fraction of the period above threshold (Eq. 3).

**Two stages can (Eq. 4, Fig. 2).** After one low-pass, saturating stage
the waveform of the intermediate signal changes with period, and a second
threshold stage turns that change into a change in mean: ⟨c_R⟩ increases
with T (shown for n = 4 and n = 50).

**The loop (Eqs. 5–9).** Kinesin carries a signal I from soma to growth
cone; dynein carries O back, suppressing I's release, with delay τ = L/v.
The loop oscillates only above a minimum length, from
J̄ sin(γτ√(J̄² − 1)) = 1 (Eq. 7), and its frequency falls with length,
ω ≈ √3 v/L for long axons (Eq. 9), matching full simulations (Fig. 3b).

**Length control (Eq. 10, Fig. 4).** L̇ = v_g c_I − v_s c_R: I drives
protrusion and the readout R drives contraction. From L = 0 the length
settles with oscillation under 1% of the mean. In the model, lowering
motor influx J₀ below a critical value lengthens the axon, as does
lowering dynein coupling, which matches the experimental finding that
fewer motors give longer axons. Gaussian delay noise (σ = 0.1τ₀) and lossy
transport leave the behaviour intact (SM Figs. S2–S3).

**What could have come out otherwise.** The cascade could have failed to
make the mean depend on period, and the coupled system could have
oscillated or run away instead of settling. Neither happened for the
parameter set used.

## What this does not say

- **That axons measure length this way.** The paper proposes no
  experiment that would tell spectral readout from gradient mechanisms,
  and its claim that gradients cannot work beyond a few micrometres is
  uncited. The authors note that sub-µm length oscillations would likely
  be masked by fluctuations in a real axon.
- **That the set point is robust.** One parameter set; sweeps cover only
  J_R, n, J₀ and J_O. Equal kinesin and dynein speeds are assumed and
  membrane tension is neglected. The model is lumped, and the authors say a
  spatial description of contractility is "most likely" needed.
- **That 125 µm means anything.** Lengths are in units of L_min = vτ_min,
  and v is not given anywhere.
- **That fewer motors always lengthen the axon.** Only below a critical
  J₀; above it length rises with J₀, and the paper does not say which side
  real axons are on.
- **That the steady state is a laser.** The gain–loss balance and
  phase-locking are an analogy (p. 4); phase-locking is not computed.
- **More than the stated scope of period independence.** The proof covers
  signals that differ by a rescaling of time with the same waveform; the
  whole mechanism depends on the waveform changing.

## Connections

- It builds on the delayed-feedback oscillator of Karamched and Bressloff
  (2015) and the motor-oscillation proposal of Rishal et al. (2012),
  neither held, and supplies the transduction they lacked.
