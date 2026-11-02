---
status: Active
title: 'Under weak local noise a many-body operator decays at a rate proportional to its size, so a Hamiltonian''s small-sized integrals of motion, which chaotic dynamics does not spread, decay slowly while generic operators, which it spreads, decay fast; in exact diagonalization of Ising and Heisenberg chains of up to nine sites at weak depolarizing noise, the slowest Lindbladian eigenoperators are linear combinations of the known exact and approximate small integrals of motion, and which approximate ones rank among the slowest moves with the noise strength'
version: 1
tags:
- natural-sciences
- complex-systems
date: '2026-11-02'
source:
- LIT-tmp8mp1c
summary: >-
  Yang and Abanin (2025), [LIT-tmp8mp1c](../literature.d/LIT-tmp8mp1c.md), read in [NOTE-tmpxpf7y](../notes.d/NOTE-tmpxpf7y.md). Active as a
  statement of what the paper derived exactly and what its exact
  diagonalization showed at the sizes it reached. It does not say that the
  correspondence holds at large system size ([THEORY-tmpull8q](THEORY-tmpull8q.md)), that every
  integral of motion is found (those above size 3–4 are not), or that
  slowness ranks conserved quantities independently of the environment.
---
<!-- inactive-ok-file: THEORY-tmpull8q CLAIM-478 — Proposed; neighbours cited as open -->

# THEORY-tmpggrkf: Under weak local noise a many-body operator decays at a rate proportional to its size, so a Hamiltonian's small-sized integrals of motion, which chaotic dynamics does not spread, decay slowly while generic operators, which it spreads, decay fast; in exact diagonalization of Ising and Heisenberg chains of up to nine sites at weak depolarizing noise, the slowest Lindbladian eigenoperators are linear combinations of the known exact and approximate small integrals of motion, and which approximate ones rank among the slowest moves with the noise strength

## Source

Yang and Abanin (2025), [LIT-tmp8mp1c](../literature.d/LIT-tmp8mp1c.md), arXiv:2506.02970v3, §§II–III and
Appendices A–G; read in [NOTE-tmpxpf7y](../notes.d/NOTE-tmpxpf7y.md).

## What was actually shown

**Exactly.** Under depolarizing noise a Pauli string P obeys D[P] = −γS(P)P,
so d‖O‖/dt = −γS(O)‖O‖ with S(O) the weighted number of sites O acts on
(eqs. 5, 6). For a Hermitian eigenoperator with real eigenvalue,
‖[H, V]‖² = γ²(⟨S²⟩_V − ⟨S⟩²_V) (eq. A7), so a slow eigenoperator commutes
with H up to O(γ) when its size distribution is not unusually spread.

**Numerically**, at L ≤ 9, periodic boundaries, zero momentum, γ = 10⁻³:

- mixed-field Ising (no local IOM but H): first three eigenoperators in
  span{I, H, H²} (Fig. 2a);
- transverse-field Ising: first five in the span of its Majorana-bilinear
  IOMs (Fig. 2b,c);
- XXX: first 25 accounted for by the known IOMs and their products (Fig.
  3a, Fig. 10b,c);
- XXZ and MFIM at hx = hz = 0.4: slow modes outside the listed IOMs, matched
  to approximate ones (spin current, S²ₓ + S²ᵧ, a domain-wall swap operator,
  a dressed particle number; Figs. 3b,c, 4, 10a).

These could have come out otherwise: the slowest eigenoperators could have
been dominated by non-conserved operators that happen to be small, as the
polarized-state projector is under dephasing–decay noise in Heisenberg
chains (Appendix B), or the listed IOMs could have failed to account for
them. In the depolarizing case they did account for them, up to the
approximate IOMs the authors then identified.

**The ranking moves with γ.** At γ = 0.1 in MFIM (hx = 1.5, hz = 0.1), the
approximate IOM A₁ overtakes the exact H² (Fig. 6), as expected from a
decay rate of roughly Aε² + Bγ for an approximate IOM against one linear in
γ for an exact one.

## What this does not say

- **That it holds at large L.** The diagonalization stops at nine sites;
  the large-system argument is [THEORY-tmpull8q](THEORY-tmpull8q.md)'s, and Proposed.
- **That every integral of motion appears.** IOMs larger than a threshold
  proportional to L, about 3–4 here, sink into the bulk (Appendix D); the
  quasi-local IOM of the XXX chain was not seen.
- **That the slow modes name themselves.** Each was matched by overlap to
  a candidate operator; the method gives a subspace.
- **That slowness alone picks out conserved quantities.** It does so given
  a noise model that punishes size, a split into sites that defines size,
  and dynamics that grow non-conserved operators; and the order among
  them depends on γ. Under a noise channel that spares a particular large
  operator, that operator is slow without being small.
- **Anything about noise channels in general.** Depolarizing noise is the
  main case; one other channel was checked (Fig. 7).
