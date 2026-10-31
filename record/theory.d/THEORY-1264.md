---
number: 1264
status: Active
formerly:
- THEORY-tmpjzj2n
title: 'Far from equilibrium, the weak-noise escape rate from an attractor goes as the exponential of minus system size times a barrier in the quasi-potential, not in any free energy, and that barrier is bracketed by thermodynamics: it is at most the entropy produced in relaxing from the saddle into the attractor and at least minus the entropy produced along the most likely escape path; the two bounds coincide at detailed balance and separate by twice the dissipation of the probability circulation, so far from equilibrium they can be very loose'
version: 1
tags:
- thermodynamics
- mathematics
date: '2026-10-31'
source:
- LIT-1881
- LIT-1892
summary: >-
  Santolin, Freitas, Esposito & Falasco (2025), [LIT-1881](../literature.d/LIT-1881.md), read in
  [NOTE-1465](../notes.d/NOTE-1465.md), for overdamped diffusions; Falasco & Esposito (2025),
  [LIT-1892](../literature.d/LIT-1892.md), §IV.H and appendix A, read in [NOTE-1472](../notes.d/NOTE-1472.md), for jump
  processes with a macroscopic limit. Active: the derivation is two lines
  from the orthogonal decomposition of the drift and was checked on a
  linear nonequilibrium diffusion. It does not say that the more
  dissipative state lives longer, and in the one worked
  far-from-equilibrium chemical example the bracket is very loose.
---
<!-- inactive-ok-file: THEORY-671 — Proposed; named as an account this bears on -->

# THEORY-1264: Far from equilibrium, the weak-noise escape rate from an attractor goes as the exponential of minus system size times a barrier in the quasi-potential, not in any free energy, and that barrier is bracketed by thermodynamics: it is at most the entropy produced in relaxing from the saddle into the attractor and at least minus the entropy produced along the most likely escape path; the two bounds coincide at detailed balance and separate by twice the dissipation of the probability circulation, so far from equilibrium they can be very loose

## Source

Santolin et al. (2025), [LIT-1881](../literature.d/LIT-1881.md), §§IV–VIII (eqs. 32, 45, 61–76),
read in full in [NOTE-1465](../notes.d/NOTE-1465.md). Falasco & Esposito (2025), [LIT-1892](../literature.d/LIT-1892.md),
§IV.B (eq. 119), §IV.H (eqs. 157–166), §VII.A.1 and appendix A, read in
[NOTE-1472](../notes.d/NOTE-1472.md).

## What was actually shown

**The rate.** With P_ss ≍ e^{−ΩI_ss} for a large parameter Ω (a volume, an
inverse noise strength), the escape rate from stable point xᵢ through
saddle x_ν is r ≍ e^{−Ω[I_ss(x_ν) − I_ss(xᵢ)]} (Santolin eq. 63; Falasco &
Esposito eq. 157). This is Freidlin–Wentzell theory. I_ss is the
quasi-potential, a Lyapunov function of the noiseless dynamics, equal to
the free energy (Massieu potential) only at detailed balance.

**The bracket.** Write the drift as u = −d·∇I_ss + v with v·∇I_ss = 0
(Santolin eq. 45; Falasco & Esposito eq. 71). Relaxation follows
ẋ = v − d∇I_ss and the instanton ẋ = v + d∇I_ss (eq. 61). The entropy
flow along either is ∓ΔI_ss plus σ_a = ∫ v·d⁻¹·v ≥ 0 (eqs. 68–70). Hence
σ_{ν→i} = σ_a + ΔI_ss ≥ ΔI_ss and σ_{i→ν} = σ_a − ΔI_ss ≥ −ΔI_ss (eqs.
72–73), and −σ_{ν→i} ≤ lim Ω⁻¹ ln r ≤ σ_{i→ν} (eq. 76). For jump
processes the same bracket follows from the emergent second law and a
Jensen argument for the adiabatic part along instantons (Falasco &
Esposito eq. 160, appendix A). At detailed balance v = 0, the instanton is
the reversed relaxation, and the bounds meet. To first order in the
nonconservative force, I_ss = ϕ plus that force's dissipation along the
detailed-balanced relaxation, and the bracket is again an equality
(Falasco & Esposito eq. 120; Santolin eq. 38).

**A check.** On dx = −Ax dt + √2 dW with A = [[1, g], [−g, 2]] (closed-form
I_ss), both inequalities hold for g = 0, 0.5, 1.5 and 3, and
σ_relax − ΔI = σ_inst + ΔI in each case. The bracket widens fast with g:
at g = 3, ΔI = 0.80, σ_relax = 4.0 and σ_inst = +2.4. The escape path
then produces entropy, and the upper bound on ln r is positive, which is
vacuous.

**What could have failed.** The circulation's contribution could have
differed between relaxation and escape, which would break the common σ_a.
Orthogonality makes it identical on both.

## What this does not say

- **That the longest-lived attractor is the most dissipative.** The bound
  ranks lifetimes by path entropies only where it is tight. Falasco &
  Esposito show that steady dissipation and lifetime agree only "under
  some peculiar conditions" ([THEORY-1270](THEORY-1270.md)).
- **That the bounds are useful far from equilibrium.** In the Schlögl
  model, where bistability exists only far from equilibrium, the path
  entropies "are very large, thus making the bound (160) very loose"
  (Falasco & Esposito §VII.A.1). Santolin et al.'s numerical case is a
  weak shear.
- **That the path entropies are finite as stated.** Between fixed points
  of a nonequilibrium dynamics the integrals diverge, because a
  maintained fixed point dissipates at a steady rate forever. The
  endpoints must be taken on balls of radius O(Ω^{−1/2}) (Falasco &
  Esposito, appendix A), so the bounds carry a cutoff.
- **Anything about prefactors.** Only the exponential order is
  controlled; at moderate Ω the prefactor can change the rate by orders of
  magnitude, and for the Schlögl model it even decides which state is
  favoured at small V ([THEORY-1273](THEORY-1273.md)).
- **Limit cycles or chaotic attractors**, which both papers set aside.
