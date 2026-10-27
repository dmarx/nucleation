---
status: Active
title: 'On a connected graph whose edges carry phase shifts αᵢⱼ = −αⱼᵢ, the edge relations zⱼ = e^{iαᵢⱼ}zᵢ have a common nonzero solution, equivalently the twisted Laplacian Lα = δα*δα has a zero mode, exactly when the phase accumulated around every cycle is 0 mod 2π; otherwise each relation can be met alone but not all together, and the smallest eigenvalue of Lα, positive, measures the residual incompatibility, which on an isolated ℓ-cycle is largest at holonomy π'
version: 1
tags:
- network-science
- mathematics
date: '2026-10-27'
source:
- LIT-tmpre2ri
summary: >-
  Torres-Hugas, Duch, Gómez and Arenas (2026), [LIT-tmpre2ri](../literature.d/LIT-tmpre2ri.md), read in
  [NOTE-tmpb8jge](../notes.d/NOTE-tmpb8jge.md) from the arXiv preprint v2. The criterion is stated in the
  paper with an energy argument (pp. 2–3) and is the standard one for
  discrete magnetic and connection Laplacians, which it cites; the
  spanning-tree step the paper omits is written out below. The
  isolated-cycle spectrum is in closed form (eqs. 29–32). Both were
  checked numerically. Active: a theorem, with the qualification that it
  concerns the relaxed linear problem, not the phase dynamics.
---
<!-- inactive-ok-file: CLAIM-tmpdjt64 CLAIM-tmpywecm — Proposed or new; the claims this criterion bears on, cited as open -->

# THEORY-tmpoeig9: On a connected graph whose edges carry phase shifts αᵢⱼ = −αⱼᵢ, the edge relations zⱼ = e^{iαᵢⱼ}zᵢ have a common nonzero solution, equivalently the twisted Laplacian Lα = δα*δα has a zero mode, exactly when the phase accumulated around every cycle is 0 mod 2π; otherwise each relation can be met alone but not all together, and the smallest eigenvalue of Lα, positive, measures the residual incompatibility, which on an isolated ℓ-cycle is largest at holonomy π

## Source

Torres-Hugas, Duch, Gómez and Arenas (2026), [LIT-tmpre2ri](../literature.d/LIT-tmpre2ri.md), §II A–B and
§II C 3, pp. 2–5 of the arXiv preprint 2604.19682v2; read in [NOTE-tmpb8jge](../notes.d/NOTE-tmpb8jge.md).

## What was actually shown

**The setting.** A connected graph, each edge oriented, with a phase αᵢⱼ on
i → j and αⱼᵢ = −αᵢⱼ (eq. 1). The twisted incidence operator is
(δα z)ᵢⱼ = zⱼ − e^{iαᵢⱼ}zᵢ (eq. 5), the energy E(z) = ½‖δα z‖² (eq. 6), and
Lα = δα*δα (eq. 8). With every αᵢⱼ = 0 these are the ordinary incidence
operator and graph Laplacian (p. 2).

**The criterion.** E(z) = 0 exactly when every edge relation zⱼ = e^{iαᵢⱼ}zᵢ
holds (eq. 7), so "ker Lα ≠ {0} if and only if the edge compatibility
conditions can be satisfied globally in the relaxed linear setting" (p. 3).
The paper then states: "When all cycle holonomies vanish, Eq. (10) admits
nontrivial solutions. If some cycle has nonzero holonomy, then ker Lα = {0}
and the smallest eigenvalue of Lα is strictly positive" (p. 3), with the
holonomy Hol_α(C) = Σ_{(i,j)∈C} αᵢⱼ mod 2π (eq. 2).

**The step the paper leaves out.** If z meets every edge relation and is not
zero, then |zⱼ| = |zᵢ| on every edge, so on a connected graph every entry has
the same nonzero modulus. Fix z at one node; the relations then fix z along
any spanning tree. Each edge outside the tree closes one fundamental cycle,
and its relation holds exactly when that cycle's holonomy is 0 mod 2π. The
fundamental cycles generate all cycles, so the relations have a nonzero
solution iff every cycle's holonomy vanishes mod 2π, and the solution is
then unique up to a common factor. On a tree there is nothing to close, so
every connection is gauge-trivial, as the paper says (p. 2). This is the
standard result for the discrete magnetic Laplacian (Shubin, the paper's
ref. [14]) and the connection Laplacian (refs. [15], [16]).

**Residual incompatibility.** λ₁(α) = min_{‖z‖=1}⟨z, Lα z⟩ (eq. 26) is zero
iff every holonomy is (eqs. 27, 28), and when positive "measures the minimum
normalized residual incompatibility after optimization over all node states"
(p. 5).

**The isolated cycle.** For an ℓ-cycle the eigenvalues are
2 − 2cos((2πm + Hol)/ℓ), m = 0, …, ℓ − 1 (eq. 29); λ₁ is zero at Hol ≡ 0
and largest at Hol ≡ π (eqs. 30–32), where "two adjacent winding sectors
become degenerate" (p. 5), giving λ₁ = 2 − 2cos(π/ℓ). A numerical check gave
λ₁ = 1 for ℓ = 3 and 0.382 for ℓ = 5 at holonomy π, and λ₁ ≈ 10⁻¹⁶ for a
4-cycle with random phases summing to 2π.

**What could have failed.** Lα could have had a zero mode for some nonzero
holonomy, or none for a flat one; the spanning-tree argument rules out both.

## What this does not say

- **Anything about the unit-modulus phase dynamics directly.** The criterion
  is for complex states zᵢ ∈ ℂ. For the gauge-coupled flow
  ϕ̇ᵢ = κ Σ sin(ϕⱼ − ϕᵢ − αᵢⱼ) (eq. 12), the paper says only that low
  eigenmodes "best accommodate the incompatibility" (p. 3) and computes
  nothing.
- **That λ₁ is a stability boundary or a relaxation rate.** In the paper's
  own motif the stability threshold is set by the Jacobian, not by Lα
  ([THEORY-tmprsknh](THEORY-tmprsknh.md)).
- **That the obstruction is a failure of the graph or of any edge.** Every
  edge relation is satisfiable on its own; the obstruction is a property of
  composition around cycles (p. 2).
- **Where the connection comes from.** The αᵢⱼ are given. Nothing in the
  result says an interaction produces them ([CLAIM-tmpdjt64](../claims.d/CLAIM-tmpdjt64.md)).
- **That this is new mathematics.** The paper's contribution lies in the
  synchronization reading, not in the criterion.
