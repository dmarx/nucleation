---
number: 747
status: Proposed
formerly:
- THEORY-tmp4ou43
promote_when: >-
  A quantitative comparison against filtered DNS, on at least one of the
  paper's flows, that reports error norms for the first-order finite-memory
  closure beside dynamic Smagorinsky (in energy, dissipation or subgrid
  transfer) rather than plotted curves alone, and that either fixes the
  memory length by a rule stated before the run or reports how the errors
  move as it varies. A comparison read off figures, or one whose memory
  length was tuned on the quantity scored, does not settle it.
title: 'In Fourier–Galerkin large-eddy simulation, a first-order finite-memory Mori–Zwanzig closure tracks filtered-DNS energy decay and dissipation on the viscous Burgers equation and on the incompressible Taylor–Green vortex, isotropic turbulence and channel flow about as well as dynamic Smagorinsky where that model is at home and better than Smagorinsky and the t-model on the transitional Taylor–Green vortex; the memory length that fits it is set by the cutoff, not by the flow alone, scaling in Burgers roughly as 0.2 over the spectral radius of the resolved variables'' Jacobian'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Proposed from NOTE-973. The comparisons are the paper's
    Figs. 3–9, read from the rendered pages at screen resolution; the
    paper reports no error norms. The memory-length scaling is its Fig. 2
    and §III.B.1. Proposed because the evidence is qualitative, from
    plots, and the memory lengths were tuned (Burgers) or preset without
    a stated rule (Navier–Stokes, τ₀ = 0.1). The structural account of
    the closure is THEORY-760.
tags:
- natural-sciences
- mathematics
date: '2026-10-20'
source:
- LIT-1259
summary: >-
  Parish and Duraisamy (2017), [LIT-1259](../literature.d/LIT-1259.md), read in [NOTE-973](../notes.d/NOTE-973.md). The
  closure is [THEORY-760](THEORY-760.md)'s finite Markovian augmentation. Here is how
  it did, as far as the paper's plots show: close to filtered DNS in
  integral quantities, comparable to dynamic Smagorinsky in equilibrium
  turbulence, clearly better on a transitional flow, and with the subgrid
  transfer peaked at the cutoff where DNS puts it but about 40% too deep.
  The paper calls the predictions "excellent" with no numbers. Its fitted
  memory length shortens as the resolved dynamics speed up, so the memory
  belongs to the cutoff as much as to the flow.
---
<!-- inactive-ok-file: CLAIM-331 — Proposed; the timescale claim this account bears on, nothing here rests on it -->

# THEORY-747: In Fourier–Galerkin large-eddy simulation, a first-order finite-memory Mori–Zwanzig closure tracks filtered-DNS energy decay and dissipation on the viscous Burgers equation and on the incompressible Taylor–Green vortex, isotropic turbulence and channel flow about as well as dynamic Smagorinsky where that model is at home and better than Smagorinsky and the t-model on the transitional Taylor–Green vortex; the memory length that fits it is set by the cutoff, not by the flow alone, scaling in Burgers roughly as 0.2 over the spectral radius of the resolved variables' Jacobian

## Source

Parish and Duraisamy (2017), *Physical Review Fluids* 2: 014604,
[LIT-1259](../literature.d/LIT-1259.md), read in full in [NOTE-973](../notes.d/NOTE-973.md) from arXiv:1611.03311v2.
§§III–V and Appendix B, Figs. 2–11.

## What was actually shown

**Memory length (Burgers, §III.B.1, Fig. 2).** Sixty runs over
ν ∈ {0.05, …, 0.0005}, cutoff k_c ∈ {8, 16, 32} and amplitude
U₀* ∈ {1, 2, 5, 10}, against 4096-mode DNS. For each, τ₀ of the
first-order model (FM1) was fitted by least squares on the dissipation
rate over t ∈ [0, 2]. Plotted against 1/ρ(∂R/∂u), the time-averaged
inverse spectral radius of the resolved Jacobian, the fits fall on one
line for k_c = 16 and 32 and on a steeper one for k_c = 8. The paper
gives τ₀ ≈ 0.2/ρ. Its reading: higher Reynolds number shortens the
memory, coarser resolution lengthens it, and "the inferred memory
length should not be viewed as a physical parameter." Appendix B samples
the slope as a Gaussian (the fits are bimodal) and finds the predicted
energy and dissipation "well concentrated", the subgrid term less so.

**Burgers (Figs. 3–5).** With 32 modes against 2048-mode DNS (ν = 0.01,
U₀* = 1, τ₀ = 0.135), FM1–FM3 follow the energy, the dissipation rate
with both its peaks, and the mean subgrid term. FM2 and FM3 also follow
the spectrum at t = 2 at all wavenumbers. The t-model overpredicts the
subgrid term after t ≈ 0.5, and Smagorinsky gets its time course wrong.
In the coarsest extra case (k_c = 8, U₀* = 5), FM1 misses the second
dissipation peak.

**Navier–Stokes.** All runs at 32³ or 64³ with τ₀ = 0.1.

- *Isotropic turbulence* (64³, from 512³ DNS, Re_λ ≈ 200, t = 4,
  Fig. 6). Spectra are comparable to dynamic Smagorinsky. In the subgrid
  transfer spectrum, FM1 alone puts the drain near the cutoff (k ≈ 33) as
  DNS does (k ≈ 31). Its peak is about −5 × 10⁻⁴ against DNS's
  −3.5 × 10⁻⁴, and it shows slight backscatter below k ≈ 17. Both
  Smagorinsky models drain at low k. The paper: "it is perhaps not
  prudent to conclude that the M-Z-based models performed significantly
  better than the Smagorinsky models."
- *Taylor–Green vortex* (32³, Re = 800 and 1600, Figs. 7–8). Smagorinsky
  dissipates from t = 0, though the flow starts resolved. The t-model
  over-dissipates after early times and needed a smaller time step. FM1
  follows energy and dissipation, including the double peak near t = 8,
  and the spectra at t = 5 and 10.
- *Channel flow* (Re_τ = 180, 32 × 64 × 32, Fig. 9, pressure effects of
  coarse-graining neglected). FM1 and dynamic Smagorinsky give similar
  mean profiles and Reynolds stresses, both near the DNS of Moser, Kim
  and Mansour and better than no model.

What could have failed: FM1 has one constant, held at 0.1 across all
four Navier–Stokes flows. It could have done as badly as the t-model on the
Taylor–Green vortex, and the Burgers fits could have scattered with no
relation to the resolved timescale.

## What this does not say

- **Not that the closure is more accurate than dynamic Smagorinsky in
  general.** On isotropic turbulence and channel flow it is comparable;
  its advantage is shown on a flow that starts resolved, where, in the
  paper's words, traditional subgrid models "do not perform well"
  because they are "designed for fully developed turbulent flows".
- **Not "excellent", quantitatively.** No error norm is reported
  anywhere. The comparisons are curves, and this account is read from
  them.
- **Not that the memory length is a property of the flow.** It moves
  with the cutoff. Part of Fig. 2's collapse may be dimensional: at fixed
  k_c every timescale of Burgers scales with 1/(U₀k_c) and 1/(νk_c²), as
  ρ does. The paper does not test τ₀ against another timescale.
- **Not that the τ₀ = 0.1 of the Navier–Stokes runs follows from the
  Jacobian rule.** The paper names a second heuristic (the time step
  scaled by the ratio of grid size to Kolmogorov scale) and does not say
  which, if either, produced 0.1.

## Connections

- **[THEORY-760](THEORY-760.md)** is what the closure is: a finite Markovian
  augmentation with an exponential kernel and no error bound. This
  account is how well it worked.
- **[CLAIM-331](../claims.d/CLAIM-331.md).** Turbulence is the third source of slowness in the
  claim's note of 2026-10-19: no gap between resolved and unresolved
  scales. Here the fitted memory is about a fifth of the fastest resolved
  timescale. So the eliminated scales' influence decays faster than any
  resolved mode moves, a ratio set by the cutoff, not a spectral gap.
  That fits the claim's "characteristically slower", and shows the
  ordering is graded and moves with the chosen cut.
- **[QUESTION-219](../questions.d/QUESTION-219.md).** What the closure carries is the energy flux
  across the cutoff (T^{SGS} = u*·w^{(0)}). It gets the flux's location
  right, which Smagorinsky does not, by carrying it as a relaxing state
  variable. Eyink and Aluie ([LIT-1239](../literature.d/LIT-1239.md), unread) are the record's
  pending source on how local that transfer is.
