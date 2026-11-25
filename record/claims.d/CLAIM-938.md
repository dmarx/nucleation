---
number: 938
status: Proposed
formerly:
- CLAIM-tmpo8cwu
title: 'Off exact symmetry, the commutator of a learning operator with a level''s projector, over the level''s slowest rate and its share of the target, bounds at every time how far the level''s residual departs from a flow without cross-level coupling; the symmetric acquisition order survives any perturbation below a threshold set by the rate gaps, and holds only down to a resolution the commutator sets'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-066: the formal
    half QUESTION-217 asks for, as a bound of A2's Conjecture A kind, with
    the study that checks it.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proofs in scratch/studies/lead-066/README.md: a symmetric
  positive semidefinite operator A, projectors P_ℓ summing to the identity,
  and a start e(0) for which ‖P_ℓ(e(t) − e^D(t))‖ exceeds
  ‖[A, P_ℓ]‖ ‖e(0)‖ (e^{−at} − e^{−λ_ℓt})/(λ_ℓ − a) at some time, e^D being
  the flow under Σ P_ℓ A P_ℓ; or an acquisition time outside the interval
  of Corollary 2 when its hypothesis holds; or, for a moving operator, a
  departure above the damped integral of Theorem 5. Not defeated by orders
  that survive beyond the threshold, which the claim says is only
  sufficient, nor by learners whose residual does not obey ė = −A_t e with
  A_t symmetric positive semidefinite, which lie outside it.
tags:
- learning-theory
- representation-learning
date: '2026-11-22'
line:
- learned-structure
bears_on:
- QUESTION-217
grounds:
- CASE-358
- THEORY-086
complements:
- CLAIM-929
summary: >-
  The bound [NOTE-985](../notes.d/NOTE-985.md) asked for, carried out under [LEAD-066](../leads.d/LEAD-066.md). A learner whose
  residual obeys ė = −Ae, with A symmetric positive semidefinite (kernel
  gradient flow, or any network under gradient flow on squared loss, with
  A its tangent kernel over n), and levels P_ℓ summing to the identity.
  The commutator ‖[A, P_ℓ]‖ is exactly the coupling between level ℓ and
  the rest. Against the flow under Σ P_ℓ A P_ℓ, in which no level talks to
  another, level ℓ's relative residual departs by at most ‖[A, P_ℓ]‖/(λ_ℓ s_ℓ)
  at any time, λ_ℓ being the level's slowest rate and s_ℓ its share of the
  initial residual; the constant cannot be improved. It follows that each
  acquisition time lies in an interval, that the symmetric order survives
  any perturbation of the operator below a threshold proportional to the
  rate gap, and that below a risk of about that ratio squared the slowest
  mode sets every level's time, so the times converge in ratio. For a
  moving operator the same holds with the commutator integrated against
  the level's own decay, a sharper form of A2's ∫‖[A_t, P_ℓ]‖dt. Checked in
  [CASE-358](../cases.d/CASE-358.md). The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-358 — new; the study of LEAD-066, filed 2026-11-22 -->

# CLAIM-938: Off exact symmetry, the commutator of a learning operator with a level's projector, over the level's slowest rate and its share of the target, bounds at every time how far the level's residual departs from a flow without cross-level coupling; the symmetric acquisition order survives any perturbation below a threshold set by the rate gaps, and holds only down to a resolution the commutator sets

## The claim

Let the residual e = F − Y of a learner on n items obey ė = −A_t e with
each A_t symmetric positive semidefinite: kernel gradient flow on the loss
(1/2n)‖F − Y‖² (A = K/n), or any network under gradient flow on that loss
(A_t its empirical tangent kernel over n). Let P_0, …, P_L be orthogonal
projectors with Σ P_ℓ = I: the levels of a hierarchy, for instance the Haar
spans of a tree's depths. Level ℓ's risk is r_ℓ = ‖P_ℓe‖²/‖P_ℓe(0)‖², and
its acquisition time T_ℓ(δ) the first time r_ℓ ≤ δ, as [QUESTION-217](../questions.d/QUESTION-217.md)
defines them with the learner's own output as decoder. Write
η_ℓ = ‖[A, P_ℓ]‖, λ_ℓ ≤ Λ_ℓ for the extreme eigenvalues of A compressed to
level ℓ, a = λ_min(A), and s_ℓ = ‖P_ℓe(0)‖/‖e(0)‖.

0. **The commutator is the coupling.** ‖[A, P_ℓ]‖ = ‖P_ℓ A (I − P_ℓ)‖. It
   vanishes for every ℓ exactly when A is block-diagonal in the levels,
   and it is at most ‖A − A₀‖ for any A₀ that commutes with the levels.
1. **Level-wise deviation.** Let e^D be the flow under D = Σ P_ℓ A P_ℓ from
   the same start, in which each level evolves on its own. Then at every
   time ‖P_ℓ(e − e^D)‖ ≤ η_ℓ‖e(0)‖(e^{−at} − e^{−λ_ℓt})/(λ_ℓ − a) ≤ η_ℓ‖e(0)‖/λ_ℓ,
   so √r_ℓ departs from the decoupled level's √r_ℓ^D by at most
   ε_ℓ = η_ℓ/(λ_ℓs_ℓ). The bound does not grow with time, and its constant
   is attained (a slow level leaking into a fast one).
2. **Acquisition times and their order.** If ε_ℓ < √δ, then
   ln(1/(√δ + ε_ℓ))/Λ_ℓ ≤ T_ℓ(δ) ≤ ln(1/(√δ − ε_ℓ))/λ_ℓ. Level ℓ comes before
   level m whenever the upper end for ℓ is below the lower end for m. With
   a symmetric baseline A₀ = Σ μ_ℓP_ℓ and ‖A − A₀‖ = ε_op, the extremes are
   within ε_op of μ_ℓ (Weyl), so the baseline order of any two levels
   survives every ε_op below a positive threshold, to first order
   proportional to the rate gap, and, when the target term dominates, to
   √δ ln(1/√δ) and the smaller target share.
3. **Data.** A perturbation of the data enters only through the kernel
   matrix's distance from a tree-symmetric one; for the linear kernel that
   distance is at most (2‖X₀‖‖Δ‖ + ‖Δ‖²)/(nd).
4. **Resolution.** If A's smallest eigenvalue is simple with eigenvector v
   and v has a part in level ℓ, then
   T_ℓ(δ) = ln(1/δ)/(2a) + O(1): off exact commutation, the levels' times
   converge in ratio as δ → 0, their order at fine δ set by the overlaps
   ‖P_ℓv‖/s_ℓ, not by the rates. The order the commutator certifies holds
   down to δ of order ε_ℓ².
5. **Moving operator.** For A_t moving, ‖P_ℓ(e − e^D)(t)‖ ≤
   ‖e(0)‖ ∫₀^t ‖[A_s, P_ℓ]‖ exp(−∫_s^t λ_ℓ(u)du) ds ≤ ‖e(0)‖ ∫₀^t ‖[A_s, P_ℓ]‖ds,
   e^D now the flow under D_t. The last form is A2's measure.

The proofs are variation of constants on each level, with the level's own
block as propagator (it contracts at rate λ_ℓ) and the commutator as the
only source; the derivations are in scratch/studies/lead-066/README.md.

So A2's Conjecture A, as [QUESTION-217](../questions.d/QUESTION-217.md) records it ("If the learning operator
A nearly commutes with every P_ℓ ([A, P_ℓ] ≈ 0) and its effective
eigenvalues fall as finer distinctions are added, acquisition is nearly
coarse to fine, with deviations set by the cross-level coupling and the
spectral gaps"), holds with constants for a fixed operator, and in its
comparison half for a moving one. [LEAD-052](../leads.d/LEAD-052.md) proved the exact case, every
commutator zero on tree-symmetric data; this claim is its perturbation
theory. Three consequences bear on the question. Off symmetry the target
re-enters the kernel order, through s_ℓ, which [LEAD-052](../leads.d/LEAD-052.md) found absent at
exact symmetry. The order has a resolution, so a claim of coarse-to-fine
acquisition must say at what risk. And what breaks the order is the
operator's distance from the symmetric one measured against the rate gaps,
not the data's distance as such.

## What it rests on

Proof, in scratch/studies/lead-066/README.md, with the standard
Davis–Kahan sin θ theorem used only for a side remark. [THEORY-086](../theory.d/THEORY-086.md), the
kernel regime fitted eigenspace by eigenspace, is the exact case's
dynamics, which part 1 perturbs. [CASE-358](../cases.d/CASE-358.md) checks every part
numerically; none failed.

## What it does not say

- It does not give the order of the decoupled flow under a moving
  operator. Part 5 bounds the distance to it; how each level's own block
  moves, and so which level that flow acquires first, is left open.
- The threshold in part 2 is sufficient, not necessary. In the study the
  order survived in 96–100% of pairs at perturbations six times the
  smallest rate gap, where nothing was certified.
- On random perturbations the uniform bound was three to seven times the
  largest departure observed. The constant is sharp only for aligned
  couplings.
- It says nothing about learners whose residual is not driven by a
  symmetric positive semidefinite operator: cross-entropy, momentum,
  adaptive optimizers.
- A2's integral form, though true, was vacuous in the trained networks of
  [CASE-358](../cases.d/CASE-358.md) (it allowed relative departures of 0.3 to 1.7); the damped
  form, which lets a level forget an early coupling at its own rate, is the
  one that informs.
