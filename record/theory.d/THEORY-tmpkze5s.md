---
status: Active
title: 'Approximating a chemical master equation by a Fokker–Planck or nonlinear Langevin equation gets the quasi-potential right only at the fixed points: between them it mis-estimates the barriers, so escape rates come out wrong by a factor exponential in system size and the approximation can pick the wrong one of two states as the long-run favourite, and its apparent entropy production vanishes at every steady state, missing the dissipation that sustains it'
version: 1
tags:
- thermodynamics
- natural-sciences
date: '2026-10-31'
source:
- LIT-tmpm46ks
- LIT-tmpkp8vh
summary: >-
  Falasco & Esposito (2025), LIT-tmpm46ks, §IV.D–E and §VII.A.1, read in
  NOTE-tmpf1zx4; Vellela & Qian (2009), LIT-tmpkp8vh, appendix A, read in
  NOTE-tmphrg34. Active: both formulas were checked on the Schlögl model,
  including Vellela & Qian's counterexample, where the exact and
  diffusion quasi-potentials favour different states. It does not say
  diffusion approximations fail near fixed points or for Gaussian
  fluctuations; there they are exact to leading order.
---

# THEORY-tmpkze5s: Approximating a chemical master equation by a Fokker–Planck or nonlinear Langevin equation gets the quasi-potential right only at the fixed points: between them it mis-estimates the barriers, so escape rates come out wrong by a factor exponential in system size and the approximation can pick the wrong one of two states as the long-run favourite, and its apparent entropy production vanishes at every steady state, missing the dissipation that sustains it

## Source

Falasco & Esposito (2025), LIT-tmpm46ks, §IV.D (eqs. 132–138), §IV.E
(eqs. 139–146), §VII.A.1 (eqs. 243–244, Fig. 4), read in NOTE-tmpf1zx4.
Vellela & Qian (2009), LIT-tmpkp8vh, appendix A (eqs. A1–A11) and footnote
5, read in NOTE-tmphrg34.

## What was actually shown

**The barrier.** For a one-step process in one dimension the exact
quasi-potential satisfies dI_ss/dc = ln(Σr₋/Σr₊), while truncating the
Kramers–Moyal expansion at second order gives dI_NLE/dc = −F/D =
2(Σr₋ − Σr₊)/(Σr₋ + Σr₊) (Falasco & Esposito eqs. 137–138; Vellela & Qian
eqs. A7–A8). The two agree to first order where F = 0 and nowhere else.
In the Schlögl model at k₋₂ = 3.5, the diffusion barrier falls short of
the exact one by δ = 0.0001 at Δμ = 4 (near the bifurcation), 0.019 at
4.5, 0.19 at 5 and 0.50 at 5.3 (my computation; Fig. 4's trend). At V ≈ 30,
δ ≈ 0.2 is a factor e⁶ ≈ 400 in the escape rate (§VII.A.1).

**The wrong winner.** Which of two states dominates as V → ∞ is the sign
of ∫ ln q between them for the master equation and of 2∫(q − 1)/(q + 1)
for the Fokker–Planck approximation, q = w/v (Vellela & Qian eq. A11).
At k = (3, 0.6, 0.25, 2.95), a = 1, b = 1.305 (footnote 5) I find +0.00166
and −0.00020: the master equation concentrates on the low state and the
diffusion approximation on the high one.

**The entropy production.** The path-probability entropy of a nonlinear
Langevin equation has mean F·D⁻¹·F (Falasco & Esposito eq. 144), which
is zero at any fixed point (eq. 145). A maintained nonequilibrium state
has a positive steady dissipation, ⟨σ̇_γ⟩ in eq. (225); the Langevin
description misses it entirely, keeping only the relaxation part.

**What could have failed.** Diffusion and jump descriptions share the
drift, the extrema and the curvatures at the extrema (Vellela & Qian
eqs. A9–A10). The barrier between them could have agreed too; it does not,
because the large-deviation form p ≍ e^{−VI} is not smooth on the jump
scale 1/V (Falasco & Esposito eqs. 132–133).

## What this does not say

- **That diffusion approximations are useless.** Near a fixed point, for
  Gaussian fluctuations (the linear noise approximation), and near a
  bifurcation where the barrier is small, they agree with the master
  equation to leading order.
- **That every continuum description fails.** In a continuous-space limit
  where jumps become infinitesimal the Einstein relation is restored and
  the Langevin description is accurate (Falasco & Esposito §V.A, not read).
- **Anything beyond one dimension** for the closed forms. The
  general-dimension statement rests on the review's argument, not on a
  computation here.
