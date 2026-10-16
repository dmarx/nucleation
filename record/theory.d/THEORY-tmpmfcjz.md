---
status: Active
title: "The quantum fidelity tr√(ρ1^{1/2}ρ0ρ1^{1/2}) is exactly the classical Bhattacharyya overlap of the two states' outcome distributions minimized over all measurements, and the minimum is attained by a projective measurement whose eigenvalues are square roots of likelihood ratios"
version: 1
tags:
- quantum-foundations
- information-theory
- mathematics
date: '2026-10-16'
source:
- LIT-018
summary: >-
  Fuchs (1995), [LIT-018](../literature.d/LIT-018.md), read in full in [NOTE-021](../notes.d/NOTE-021.md). min over POVMs of
  Σ_b √(tr ρ0E_b)√(tr ρ1E_b) equals tr√(ρ1^{1/2}ρ0ρ1^{1/2}) (Eq. 3.28),
  attained in the eigenbasis of M = ρ1^{-1/2}√(ρ1^{1/2}ρ0ρ1^{1/2})ρ1^{-1/2}
  (Eq. 3.67), whose eigenvalues are √(tr ρ0E_b / tr ρ1E_b) (Eq. 3.92).
  Proved for invertible ρ1 with a separate support construction, in finite
  dimension. The fidelity is the unsquared one; Jozsa's is its square. The
  thesis says nothing about trace distance, and the analogous problems for
  Rényi overlaps and the quantum Chernoff bound are left open.
---

<!-- inactive-ok-file: THEORY-tmp2ae0w — Proposed; named in Connections, not leaned on -->

# THEORY-tmpmfcjz: The quantum fidelity tr√(ρ1^{1/2}ρ0ρ1^{1/2}) is exactly the classical Bhattacharyya overlap of the two states' outcome distributions minimized over all measurements, and the minimum is attained by a projective measurement whose eigenvalues are square roots of likelihood ratios

## Source

Fuchs (1995), PhD thesis, [LIT-018](../literature.d/LIT-018.md), §3.3, read in full in [NOTE-021](../notes.d/NOTE-021.md). The
result was published separately as Fuchs & Caves (OSID), the thesis's
ref. [149].

## What was actually shown

**Definition.** A quantum distinguishability is a classical measure of
distinguishability extremized over every POVM, with the number of outcomes
free (Eqs. 3.3–3.7). For the statistical overlap F(p0,p1) = Σ_b √p0(b)√p1(b),
the Bhattacharyya coefficient (Eq. 2.40), the quantum version is its
minimum over measurements.

**Theorem (§3.3.1).** min_E Σ_b √(tr ρ0E_b)√(tr ρ1E_b) =
tr√(ρ1^{1/2}ρ0ρ1^{1/2}) (Eq. 3.28). The proof bounds each outcome's term by
a Schwarz inequality with a free unitary inserted, sums the measurement
away with Σ_b E_b = 1, and fixes the unitary by polar decomposition so the
equality condition becomes an eigen-equation (Eqs. 3.54–3.74).

**The optimal measurement.** Projectors onto the eigenbasis of
M = ρ1^{-1/2}√(ρ1^{1/2}ρ0ρ1^{1/2})ρ1^{-1/2} (Eq. 3.67). Its eigenvalues are
m_b = (tr ρ0E_b / tr ρ1E_b)^{1/2} (Eq. 3.92), so M acts as an operator
likelihood ratio. M is the Kubo–Ando geometric mean ρ1⁻¹ # ρ0 (Eq. 3.106).

**Checks.** For pure states F = |⟨ψ0|ψ1⟩| (Eq. 3.36). The naive bound
tr(ρ0^{1/2}ρ1^{1/2}) is unattainable when the states do not commute
(Eqs. 3.45–3.53). F is symmetric, unitarily invariant, between 0 and 1, and
multiplicative on products (Eq. 4.58). The Bures distance is d_B² = 2 − 2F
(Eq. 3.29).

**What could have come out otherwise.** The minimum over POVMs could have
been strictly below every projective value, or could have had no closed
form, as happens for the Rényi overlaps the thesis leaves unsolved (§3.4).

## What this does not say

- **Anything about trace distance.** [NOTE-021](../notes.d/NOTE-021.md) corrects the seeded skim: the
  thesis has no trace-distance results, and the inequalities
  1 − F ≤ D ≤ √(1 − F²) come later (Fuchs & van de Graaf, 1999).
- **That the fidelity is squared.** The convention here is unsquared.
  Jozsa's "fidelity" is its square (pp. 49, 115). Formulas that mix the two
  conventions differ by a square.
- **That every quantum distinguishability is solved.** The quantum Chernoff
  bound (Eq. 3.26) and the Rényi overlaps (§3.4) are defined and not
  solved. The quantum Kullback information has only bounds.
- **That the projective version was new.** The thesis concedes that the
  projective-measurement version could already be assembled from Wootters,
  Alberti and Uhlmann (p. 49). What it claims is the derivation over all
  POVMs, the statistical reading and the optimal measurement.
- **Infinite dimension.** The proof is written for finite dimension.

## Connections

- Its multiplicativity and monotonicity under partial trace are the
  properties on which the no-broadcasting theorem rests ([THEORY-tmpz1eac](THEORY-tmpz1eac.md),
  same thesis).
- Quantum thermodynamics' smooth entropies use this unsquared fidelity
  ([LIT-010](../literature.d/LIT-010.md), [NOTE-011](../notes.d/NOTE-011.md); [THEORY-tmp2ae0w](THEORY-tmp2ae0w.md)).
