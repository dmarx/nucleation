---
status: Active
title: 'In a driven chemical system with two stable states and a finite number of molecules, each maintained state is metastable: it is left by fluctuation after a time exponential in system size, set by a barrier in a nonequilibrium quasi-potential that closes at the saddle-node, and the long-run share of time in each state is fixed by the parameters and system size, not by the initial condition; the deterministic rate equation, where the initial condition decides, holds only on times short of that escape time'
version: 1
tags:
- thermodynamics
- natural-sciences
- complex-systems
date: '2026-10-31'
source:
- LIT-tmpkp8vh
- LIT-tmpm46ks
summary: >-
  Vellela & Qian (2009), LIT-tmpkp8vh, read in NOTE-tmphrg34, on the
  Schlögl model, with Falasco & Esposito's general frame (LIT-tmpm46ks,
  §§III.C, IV.H, VI; NOTE-tmpf1zx4). Active: the slow eigenvalue, the
  barriers, the initial-condition independence and the closing of the
  barrier at the fold were checked numerically on the paper's model. It
  does not say which state is the more stable without computing the
  quasi-potential, and the paper's own large-volume rate formula carries a
  spurious 1/V factor.
---

# THEORY-tmpwystk: In a driven chemical system with two stable states and a finite number of molecules, each maintained state is metastable: it is left by fluctuation after a time exponential in system size, set by a barrier in a nonequilibrium quasi-potential that closes at the saddle-node, and the long-run share of time in each state is fixed by the parameters and system size, not by the initial condition; the deterministic rate equation, where the initial condition decides, holds only on times short of that escape time

## Source

Vellela & Qian (2009), LIT-tmpkp8vh, §§2–4 and appendix A, read in
NOTE-tmphrg34 from the PMC copy. Falasco & Esposito (2025), LIT-tmpm46ks,
§III.C (multistability against metastability), §IV.H (eq. 157) and §VI,
read in NOTE-tmpf1zx4.

## What was actually shown

**The model.** A + 2X ⇌ 3X, B ⇌ X with A and B chemostatted, in volume V.
The rate equation ẋ = k₁ax² − k₂x³ − k₄x + k₃b has two stable states and
a saddle in a region of (a, b), which requires the chemostats out of
equilibrium, k₁k₄a ≠ k₂k₃b (Vellela & Qian eqs. 2.3, 3.6, 3.10). The
chemical master equation is a birth–death chain with a unique stationary
distribution p^ss_n ∝ Π λᵢ/μᵢ₊₁ (eq. 2.8), two-peaked where the rate
equation is bistable.

**The time scales.** The generator's second eigenvalue λ₁ is
exponentially small in V and equals −(r₊ + r₋), the sum of the escape
rates of a two-state reduction (§§3.4, 4.1); the other eigenvalues stay
of order one (Table 1: −1.64, −2.37, −3.18 at V = 100). Asymptotically
ln rᵢ ≈ −VΔuᵢ, with Δu the drop in the quasi-potential
u(x) = ∫ ln(J⁺/J⁻) from the stable state to the saddle (eqs. 3.29–3.30).
Checked on eq. (4.4)'s parameters: λ₁ from the full generator matches a
Kramers-type sum to four digits for V = 40–80, and ln|λ₁| falls at
−0.22 per unit V, the smaller of the two barriers (0.222 and 0.318).

**Initial-condition independence.** The long-run share of time near
each state is P₋/P₊ = r₊/r₋, set by u(x₋) − u(x₊) at leading order. For
large V the system "will almost surely be found in only one of two FCA.
Which state it ends up in depends solely on the parameter values ... and
not on the initial condition!" (§3.4). In Falasco & Esposito's terms the
V → ∞ and t → ∞ limits do not commute; the deterministic limit is
multistable while the mesoscopic law is unique (§III.C).

**Finite-size exchange of stability.** At a = 1, b = 2 the favoured state
moves from x₋ to x₊ as V grows (Fig. 4). Checked: the lower well holds
73%, 38% and 2% of the mass at V = 10, 20, 40. The O(1) prefactor of
the asymptotic ratio places the crossover at V ≈ 16.5.

**The fold (my check, not in either paper).** As b approaches the
saddle-node at b* = 3.278 (a = 1), the lower state's barrier closes as
(b* − b)^{3/2}: barrier/(b* − b)^{3/2} = 0.064 for b* − b from 0.1 to
0.001. So the lifetime e^{VΔu} collapses before the deterministic fold.

**What could have failed.** The slow eigenvalue might not have
separated from the rest, or the stationary weights might have depended on
initial data through a conserved quantity. Neither happens; the chain is
irreducible.

## What this does not say

- **That the more stable state is the deeper well of any energy.** The
  barrier is in a quasi-potential computed from the rates. Its sign is
  not given by the rate equation's "potential" ∫ẋ dx (Vellela & Qian
  footnote 1), nor reliably by a Fokker–Planck approximation
  (THEORY-tmpkze5s).
- **That the paper's asymptotic rates are right.** As printed,
  eqs. (3.29)–(3.30) carry a factor 1/V that puts them below the exact
  λ₁ by a factor growing like V (0.59V at V = 150). The paper's reported
  "breakdown" of asymptotics at small volume is mostly that factor
  (NOTE-tmphrg34).
- **That lifetime fixes stationary probability in general.** With two
  states it does, P₋/P₊ = τ₋/τ₊. With three or more attractors the
  routing between them matters, and Falasco & Esposito note that a
  long-lived dissipative state can be improbable (§VIII.B.6, citing Maes
  & Netočný, not read).
- **Anything about two or more species.** The closed-form stationary law
  is a one-dimensional accident; in higher dimension the quasi-potential
  must be found from a Hamilton–Jacobi equation (LIT-tmpm46ks, eq. 34).
- **That deterministic constructions such as CASE-tmpwxags or CASE-111 are
  wrong.** Their folds are the V → ∞ statements. What changes at finite
  size is that a maintained regime has a lifetime, and loses it before the
  fold.
