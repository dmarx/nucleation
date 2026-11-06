---
status: Proposed
title: 'In a central-force network at a stable ground state, the external force that couples to a linear zero mode u is (T + λI)u, with T the prestress matrix and λ the regularizer, so bond stiffness never redirects it, and as λ goes to zero it is supported only on the nodes of prestressed bonds; prestress carried by a cluster that every zero mode moves rigidly redirects nothing'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A central-force network at a stable ground state, with prestress a state
  of self-stress, in which the force mapped by the susceptibility onto a
  linear zero mode u differs from (T + λI)u; or in which, with zero
  prestress, some choice of stiffnesses makes that force not parallel to
  u; or in which, as λ goes to zero, it has a component on a node incident
  to no prestressed bond. Also defeated if it only restates a result the
  record already holds; THEORY-1414's Theorem 1 gives the bijection but
  never writes the force in terms of T.
tags:
- natural-sciences
- mathematics
date: '2026-11-06'
line:
- realizability
corroborated_by:
- THEORY-1414
summary: >-
  The status review's own result, from reading Rocks and Mehta in full
  (NOTE-1557). It sharpens THEORY-1414: there, prestress redirects and
  localizes the exciting force on two worked networks. Here, for any
  central-force network, the force is (T + λI)u. Stiffness drops out, and
  the localization is general in the limit. It is proved in one line and
  checked numerically in scratch/formal/rocks_mehta_check.py. The
  coordinator re-ran the script and checked the identity by hand. Kept
  Proposed for the next pass to rule on. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---

# CLAIM-tmp5iqbr: In a central-force network at a stable ground state, the external force that couples to a linear zero mode u is (T + λI)u, with T the prestress matrix and λ the regularizer, so bond stiffness never redirects it, and as λ goes to zero it is supported only on the nodes of prestressed bonds; prestress carried by a cluster that every zero mode moves rigidly redirects nothing

## The claim

Take Rocks and Mehta's setting (NOTE-1557). The compatibility matrix is C, with C_αi = ∂ℓ_α/∂u_i. The stiffness is K. The prestress t^ps is a state of self-stress, and its prestress matrix is T_ij = Σ_α t^ps_α ∂²ℓ_α/∂u_i∂u_j. The Hessian is H = CᵀKC + T, positive semidefinite at a stable ground state. The node susceptibility is ∂u/∂f = [H + λI]⁻¹. By their Theorem 1, the force f that produces a linear zero mode u (Cu = 0) is f = [∂u/∂f]⁻¹u.

**Derivation.** f = (H + λI)u = CᵀK(Cu) + Tu + λu = (T + λI)u.

- **Stiffness drops out.** K enters only through Cu, which is zero. With zero prestress, f = λu for every K, so the force is parallel to its mode whatever the stiffnesses.
- **Localization.** ∂²ℓ_α/∂u_i∂u_j vanishes unless i and j are endpoints of bond α. So T, and with it Tu, is supported on the nodes of bonds with t^ps_α ≠ 0. As λ goes to zero, f/|f| tends to Tu/|Tu| whenever Tu ≠ 0. For a central-force bond, ∂²ℓ/∂u² acts on the relative displacement as (I − b̂b̂ᵀ)/ℓ, so the force is the prestress times the transverse relative motion of the prestressed bonds.
- **Rigid clusters.** If every zero mode moves a self-stressed cluster rigidly, each bond's relative displacement in it is a translation or a rotation. A translation gives zero transverse motion. A rotation gives a transverse term t ω b̂⊥ per bond, and these sum to zero at each node because the tensions balance there. So Tu = 0 on that cluster, and f = λu.

**Check.** scratch/formal/rocks_mehta_check.py (python3 -I) runs two networks that are not the paper's, with heterogeneous stiffness, at λ = 1e-3 and 1e-6, with zero-prestress controls. f = (T + λI)u holds in all twelve runs. With stiffness varied and no prestress, |cos(u, f)| = 1. Prestress on a rigid braced cell leaves |cos| = 1. On a pinned grid whose straight row carries tension, |cos| = 0.53, and the share of f off the row's nodes falls from 0.0012 at λ = 1e-3 to 0 at λ = 1e-6. The coordinator of the twenty-eighth status review re-ran it and checked the identity by hand.

## What it does not say

- That stiffness does not matter to the response. It shapes everything outside the zero modes, the zero-energy modes and the energetic stiffness. Only the force that excites a linear zero mode is blind to it.
- That the limit is the physics at every λ. At finite λ the force carries the λu part as well.
- Anything beyond linear order: whether prestress stabilizes, or whether zero modes extend to finite motions.

## Bearing

It sharpens the reading of Rocks and Mehta (THEORY-1414). Their two worked networks show the localization, and this result says why it must happen whenever prestress acts transversely on a zero mode. It also qualifies the record's mechanical analogy for CLAIM-345: which force excites a mode depends on prestress, not on stiffness.
