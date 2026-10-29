---
number: 1087
status: Active
formerly:
- THEORY-tmprsknh
title: 'In the symmetric Sakaguchi–Kuramoto model on a triangle and a pentagon sharing one vertex, the lag α gives each ℓ-cycle a phase-independent path mismatch (ℓ − 2)α, and the remote-synchronized locked branch passes through an exact two-group state at α = π/3, where the pentagon''s mismatch reaches π; but that branch has already lost transverse stability, in the pentagonal symmetry sector, at αc ≃ 1.0164, so the point of maximal cycle frustration marks the geometry of the phase relations, not the end of the synchronized pattern'
version: 1
tags:
- network-science
- complex-systems
date: '2026-10-27'
source:
- LIT-1668
summary: >-
  Torres-Hugas, Duch, Gómez and Arenas (2026), [LIT-1668](../literature.d/LIT-1668.md), read in
  [NOTE-1218](../notes.d/NOTE-1218.md) from the arXiv preprint v2. The mismatch (ℓ − 2)α is a
  three-line derivation (eqs. 15–18); the two-group state at π/3 is exact
  algebra (eqs. 38–40); the threshold αc is a numerical continuation with
  det M⊥ = 0 (Supplementary Material). All three were reproduced. Active
  for this motif and branch; the paper's wider reading, that remote
  synchronization is a manifestation of cycle-level constraints, is not
  what this says.
---

# THEORY-1087: In the symmetric Sakaguchi–Kuramoto model on a triangle and a pentagon sharing one vertex, the lag α gives each ℓ-cycle a phase-independent path mismatch (ℓ − 2)α, and the remote-synchronized locked branch passes through an exact two-group state at α = π/3, where the pentagon's mismatch reaches π; but that branch has already lost transverse stability, in the pentagonal symmetry sector, at αc ≃ 1.0164, so the point of maximal cycle frustration marks the geometry of the phase relations, not the end of the synchronized pattern

## Source

Torres-Hugas, Duch, Gómez and Arenas (2026), [LIT-1668](../literature.d/LIT-1668.md), §II C 1 and
§II C 4–6, pp. 3–7, and the Supplementary Material, pp. 9–10, of the arXiv
preprint 2604.19682v2; read in [NOTE-1218](../notes.d/NOTE-1218.md).

## What was actually shown

**The model.** ϕ̇ᵢ = ω + κ Σⱼ Aᵢⱼ sin(ϕⱼ − ϕᵢ − α) (eq. 14), "where the same
phase lag α appears in both interaction directions". It is not the paper's
gauge-coupled model, whose lag reverses with the edge and which is a gradient
flow: "The two models have different local coupling laws" (p. 3).

**The mismatch.** For an edge (u, v) of a simple ℓ-cycle, the coupling
argument on the edge is ϕᵥ − ϕᵤ − α and the sum along the other ℓ − 1 edges
is ϕᵥ − ϕᵤ − (ℓ − 1)α, so h_α(C) = (ℓ − 2)α mod 2π, "independent of the
phase configuration" and of the edge chosen (eqs. 15–18). In the motif,
h_α(C₃) = α and h_α(C₅) = 3α (eqs. 33, 34). On a cactus graph an associated
antisymmetric connection is built so that its holonomies equal these
mismatches (eqs. 21, 22); that step is a representation by construction.

**The two-group state.** Complete synchrony is not a locked state here
because the degrees differ (p. 6). The branch continued from complete
synchrony at α = 0 respects the reflection classes {1}, {2, 3}, {4, 7},
{5, 6}, with offsets x, y, z = y + x obeying eqs. (38, 39). At x = 0,
y = z = α these reduce to sin α(2cos α − 1) = 0, so α = π/3, 3α = π, and
h_α(C₅) = π (eq. 40). There ϕ₁ = ϕ₂ = ϕ₃ and ϕ₄ = ϕ₅ = ϕ₆ = ϕ₇ = ϕ₁ + π/3
(p. 7).

**The instability.** Transverse perturbations split by symmetry into a
triangular mode η on {2, 3} and a 2 × 2 block M⊥ on the pairs {4, 7} and
{5, 6} (SM p. 9). Along the branch the first zero of det M⊥ is at
αc ≃ 1.0164, with σ(M⊥) ≃ {0, −1.7038}, the η-rate ≃ −1.5247 and the other
symmetry-preserving eigenvalues negative, "Hence this transverse crossing is
also the first instability of the full linearized dynamics" (SM p. 10). So
αc ≃ 1.0164 < απ = π/3 ≃ 1.0472 (eqs. 41, 42), and "this configuration lies
on the transversely unstable continuation of the locked branch" (p. 7).

**What could have failed, and was checked.** The two-group state could have
fallen anywhere on the branch, and the instability could have coincided with
the frustration peak or come after it. A numerical continuation of eqs.
(38, 39) for this note found x = 0, y = π/3 at α = π/3 and the det M⊥
crossing at α ≈ 1.017, with branch values matching the paper's to two
decimals.

## What this does not say

- **That frustration stabilizes or creates the pattern.** The pattern is
  continued smoothly from complete synchrony (p. 6); its nonuniformity is
  forced by unequal degrees (p. 6); and it loses stability before the
  frustration peak (p. 7).
- **That remote synchronization in general is a cycle-holonomy effect.** The
  paper proposes that it "can be understood as a manifestation of effective
  higher-order constraints" (p. 1); what it shows is one motif.
- **What happens past αc.** Whether the pentagonal pairs desynchronize while
  {2, 3} stays in step, as the symmetry structure ([THEORY-276](THEORY-276.md)) would allow,
  is not followed; nor is the bifurcation's type named.
- **That the twisted spectrum sets the dynamics' rates or stability.** "The
  twisted Laplacian thus encodes the geometric reorganization of the
  cycle-compatibility structure, whereas the Jacobian determines the stability
  of the nonlinear phase-locked state" (p. 7). For the whole motif the
  associated λ₁(α) does not even peak at π/3 (by my computation, near
  α ≈ 1.09), and the paper warns that no monotone relation should be expected
  (p. 8).
- **Anything beyond cactus graphs**, where an edge in two cycles would need
  two phases (pp. 4, 8).
