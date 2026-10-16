---
status: Active
title: "In a bundled network, one fiber graph attached at a single node to every node of a base graph, the low Laplacian spectrum is the base spectrum divided by the fiber size to first order, so the gap exponent (Fiedler dimension) is set by the base while the density-of-states exponent (spectral dimension) is the fiber's; the two come apart generically and coincide only in special cases, and relaxation then decays with the spectral dimension at intermediate times but equilibrates on a time set by the Fiedler dimension"
version: 1
tags:
- network-science
- mathematics
date: '2026-10-16'
source:
- LIT-028
summary: >-
  Grimaldi, Villegas, Vezzani, Burioni, Cassi & Gabrielli (2025; PRE Letter
  2026), [LIT-028](../literature.d/LIT-028.md), read in full with its SM in [NOTE-005](../notes.d/NOTE-005.md), which re-derived the
  key steps and checked them numerically on the comb. λ_{n1} = ℓ^b_{n1}/N_f
  gives d_g = 2(d_f,f + d_f,b)/(d_f,f + 2d_f,b/d_g,b) in the base-controlled
  regime; d_s = d_s,f is earlier work by the same group. The comb has
  d_s = 1 and d_g = 4/3. Proved for one graph class only; the paper's
  composite finite-size scaling prefactors (SM Eqs. 25, 29) are wrong, and
  its "generic property of composite architectures" outruns the proof.
---

# THEORY-tmplo7ui: In a bundled network, one fiber graph attached at a single node to every node of a base graph, the low Laplacian spectrum is the base spectrum divided by the fiber size to first order, so the gap exponent (Fiedler dimension) is set by the base while the density-of-states exponent (spectral dimension) is the fiber's; the two come apart generically and coincide only in special cases, and relaxation then decays with the spectral dimension at intermediate times but equilibrates on a time set by the Fiedler dimension

## Source

Lorenzo Grimaldi, Pablo Villegas, Alessandro Vezzani, Raffaella Burioni,
Davide Cassi and Andrea Gabrielli (v1 2025, v2 2026), "Asymptotic versus
mesoscopic spectral dimensions in networks and inhomogeneous structures",
*Physical Review E* 114, L022301, [LIT-028](../literature.d/LIT-028.md), read in full with the
Supplemental Material in [NOTE-005](../notes.d/NOTE-005.md), v1 compared.

## What was actually shown

**Two exponents.** The spectral dimension d_s is defined by the density of
states, ρ(λ) ∼ λ^(d_s/2 − 1) as λ → 0. The Fiedler dimension d_g is defined
by finite-size gap scaling, λ₁ ∼ N^(−2/d_g).

**The reduction (SM Eqs. 6–10).** For a bundled graph the Laplacian is
L = L_f ⊗ I + L_b ⊗ P₀. In the base eigenbasis it splits exactly into N_b
fiber problems, each with a single-site impurity of strength ℓ^b, one base
eigenvalue (Eq. 7). First-order perturbation about the fiber's constant
mode gives λ_{n1} = ℓ^b_{n1}/N_f (Eq. 10). [NOTE-005](../notes.d/NOTE-005.md) confirms the
derivation, observes that the Rayleigh quotient makes it an upper bound on
each sector's lowest eigenvalue, and finds the ratio to the exact gap
0.92, 0.96, 0.98, 0.99 on the comb for L = 40 to 320.

**The rule (Eqs. 5–6).** With N_b ∼ L^(d_f,b), N_f ∼ L^(d_f,f) and the base
gap ∼ N_b^(−2/d_g,b): d_g = 2(d_f,f + d_f,b)/(d_f,f + 2d_f,b/d_g,b). It
holds when the base sector sets the gap, i.e. unless
2d_f,f/d_g,f > d_f,f + 2d_f,b/d_g,b (SM Eq. 14), a condition the main text
omits. d_g = d_g,b only when d_g,b = 2 or the fiber is finite. Meanwhile
d_s = d_s,f (Cassi–Regina; Burioni–Cassi). So the comb, a ring of rings,
has d_s = 1 and d_g = 4/3 ([NOTE-005](../notes.d/NOTE-005.md)'s numerics give a local exponent of
1.349); a d-dimensional lattice base with ring fibers has d_s = 1 and
d_g = 2(1 + d)/3, which the gap scaling of Fig. 2 follows for d = 1–4.

**Homogeneous cases agree.** On the Sierpinski gasket the C(τ) plateau
gives d_s/2 = 0.684(2) and the gap gives d_g/2 = 0.683(1), against the exact
0.683; the carpet gives 0.915(4) and 0.906(4) (v1 error bars).

**Dynamics (SM S6–S7).** The return probability decays as t^(−d_s/2) at
intermediate times and is cut off at τ_eq ∼ N^(2/d_g). So two networks with
the same d_s, comb and brush (d_g = 4/3 against 2), equilibrate on
parametrically different times.

**What could have come out otherwise.** The gap could have followed the
fiber's exponent, or the two exponents could have stayed equal as in the
homogeneous fractals. Exact numerics on lattice-based bundles fall on the
predicted curve, with deviations still about 10⁻² at 10⁶–10⁷ nodes for
d = 3 and 4.

## What this does not say

- **That composite networks in general decouple the two dimensions.** The
  proof covers one fiber type per base node, one attachment point, no
  disorder and a common scaling length. "A generic geometric property of
  composite architectures" (p. 3) is an assertion; the outlook itself
  calls the construction "a minimal controlled setting".
- **That the paper's composite finite-size scaling forms are right.** SM
  Eqs. 25 and 29 carry the homogeneous prefactors; [NOTE-005](../notes.d/NOTE-005.md) derives N^(−1)
  for G and N⁰ for C_V, and the comb confirms it. The brush, which the
  figure plots, has d_s,b = d_g and cannot show the error.
- **That homogeneous parts can never be fiber-controlled.** v2 asserts it;
  v1's one-line reason (2d_f/(d_f + 1) ≤ d_s ≤ d_f) was dropped.
- **Anything reproducible about the tree and Barabási–Albert bases.** Their
  construction and parameters are not given, and BA's "effective
  d_g,b = 2" is asserted.
- **That the mechanism explains polymer rheology.** The link is an analogy;
  no data are analysed.

## Connections

- **Higher-order networks** ([THEORY-tmpodgn4](THEORY-tmpodgn4.md), from [LIT-091](../literature.d/LIT-091.md)). Battiston et
  al. report that the spectral dimension of higher Hodge Laplacians grows
  with order in network-geometry complexes, and that synchrony is stable
  only for d_S > 4. They use "spectral dimension" in the density-of-states
  sense. An argument that joins a d_S threshold to a gap-controlled
  relaxation time should check which exponent it means; that is [NOTE-057](../notes.d/NOTE-057.md)'s
  inference from reading the two together.
- **Ollivier–Ricci flow** ([THEORY-tmp6xq6t](THEORY-tmp6xq6t.md), from [LIT-004](../literature.d/LIT-004.md)) is the record's
  other account of how a network's geometry is read off its edges; it does
  not use the spectrum.
