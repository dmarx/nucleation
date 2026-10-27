---
status: Active
title: 'One arrangement of harmonic particles on a finite graph, with the same wiring, potential and inverse-mass response, gives the discrete wave equation when the integrator stores position and momentum and the discrete heat equation when it stores position alone; both are governed by the symmetrized graph Laplacian, and the coupling data do not decide between them'
version: 1
tags:
- compositionality
- mathematics
- complex-systems
date: '2026-10-27'
source:
- LIT-tmpfywhk
summary: >-
  Spivak (2026), LIT-tmpfywhk, read in NOTE-tmplvblh from arXiv v2. In
  the operad ArrSm, harmonic particles wired along a finite directed
  graph form one closed arrangement with potential Σ(κ_e/2)(q_tgt −
  q_src)². The phase semantics gives m_v q̈_v = −(L_G q)_v (Proposition
  7.4.1) and a symplectic step; the configuration semantics gives
  m_v(q_v(t+1) − q_v(t)) = −(L_G q(t))_v (Remark 7.4.2). Active: both
  are short exact computations. It says nothing about time scales, and
  what differs between the two is a modelling choice, not the coupling.
---
# THEORY-tmp09707: One arrangement of harmonic particles on a finite graph, with the same wiring, potential and inverse-mass response, gives the discrete wave equation when the integrator stores position and momentum and the discrete heat equation when it stores position alone; both are governed by the symmetrized graph Laplacian, and the coupling data do not decide between them

## Source

Spivak (2026), LIT-tmpfywhk, §§6.3, 6.6 and 7.3–7.4 (pp. 54–61, 67–71,
76–87 of arXiv 2606.28984v2); read in NOTE-tmplvblh.

## What was actually shown

**The arrangement.** For a finite directed graph G = (V, E, src, tgt), each
vertex v is a particle with parameter ℝ, constant sharp ξ ↦ ξ/m_v, output
the diagonal broadcasting its position to its out-edges, and potential
Σ_{e∈v⁻} (κ_e/2)(q − q′_e)² over its in-edges. Wiring them by the graph's
prism lens gives one closed arrangement wire_G with parameter ℝ^V and
composite potential U(q) = Σ_{e∈E} (κ_e/2)(q_tgt(e) − q_src(e))², (89),
p. 85. Its differential is dU = L_G q, the weighted graph Laplacian, and the
orientation drops out because each edge term is symmetric in its endpoints
(p. 85).

**Two integrators.** The configuration integrator stores q and updates
q ↦ q − ♯_q(ξ) (41), p. 56. The phase integrator stores (q, ξ), presents
q̃ = q + ♯_q(ξ), and updates ((q, ξ), ξ′) ↦ (q + ♯_q(ξ), ξ − ξ′) with ξ′ the
gradient at q̃ (50), p. 61. Both share the factor Φ′sm, the polynomial
interpretation of the arrangement, and differ only in the stored state and
the update (p. 68).

**The wave equation.** Proposition 7.4.1 (p. 86): "every trajectory of
Φphase(wire_G) … satisfies m_v q̈_v(t) = −(L_G q(t))_v (v ∈ V, t ≥ 1)",
with q̈_v(t) = q_v(t+1) − 2q_v(t) + q_v(t−1). The arrangement is harmonic,
so by Proposition 6.6.1 the step is a linear isomorphism preserving the
canonical symplectic pairing (p. 86). §7.3 does the chain with pinned ends
twice, composing in the syntax and composing the parts' semantics, and the
two agree (pp. 79–83).

**The heat equation.** Remark 7.4.2 (pp. 86–87): "applying Φconf to the
very same smooth adaptive arrangement wire_G of (88)—same graph wiring, same
potential, and the same positive inverse-mass response—recovers the
discrete heat equation on G", M q̇ = −L_G q with q̇_v(t) = q_v(t+1) − q_v(t)
and M = diag(m_v). The author's summary: "the second-order, symplectic
regime and the first-order, descent regime are two semantics of one
syntactic object" (p. 87).

Both computations were checked numerically on a four-vertex path graph
(NOTE-tmplvblh): the wave residual was at machine precision, and U fell
monotonically under the heat step.

## What this does not say

- **Anything about time scales.** The paper does not speak of relaxation
  rates, separation or hierarchy. That the heat step damps each eigenmode of
  M⁻¹L_G at a rate set by its eigenvalue while the symplectic step damps
  none is a reading through CLAIM-tmpywecm, not in the text.
- **That the coupling is dissipative or conservative.** The regime is fixed
  by the integrator, which the paper calls the semantics; physically it is
  the choice of whether the particles carry momentum. So the result shows
  that wiring, potential and response underdetermine the dynamics, not that
  one physical system shows both.
- **That either step is stable for every step size.** Neither the heat step
  nor the phase step comes with a stability bound in the paper; both are
  explicit, one tick per step.
- **That the discrete step conserves energy.** It preserves the symplectic
  pairing for harmonic systems; "The discrete step (65) need not conserve H
  exactly" (p. 70).
- **Continuum equations.** These are difference equations on a graph; the
  continuum limit of the chain is pointed to a reference, not derived
  (footnote 31, p. 76).
- **That the regime is in the semantics for every arrangement.** The author
  expects that for each quadratic arrangement f there is g on T*Q with
  Φphase(f) = Φconf(g) (p. 88). If so, the same split can also be expressed
  in the syntax.
