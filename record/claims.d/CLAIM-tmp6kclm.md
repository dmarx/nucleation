---
status: Proposed
title: 'In symmetric resource competition whose operators adapt a bounded niche trait up the selection gradient, a differentiated equilibrium is locally exponentially stable when its traits are interior and stationary or held at a bound with an outward gradient and the Hessian of the shared objective on the free coordinates is positive definite; every specialist then recovers when rare against residents whose traits are frozen, at a rate of at least its abundance times its niche vector''s squared distance from the span of the others'''
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-049 at the
    coordinator's brief. Proved here; checked numerically in
    CASE-tmp5sk3q (scripts and tests under scratch/studies/lead-049/).
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in one of the three proofs below: that within the stated class
  (A = UᵀU with u(θ) ≥ 0, r = Uᵀb − c, the trait moving up the rare-mutant
  selection gradient inside a box, at any positive rate) the flow is not
  −D∇L for the stated positive diagonal D; that an equilibrium meeting
  Theorem A's hypotheses can fail to be locally exponentially stable; or
  that, with A* positive definite and n* > 0 an equilibrium, the recovery
  growth of a specialist into the frozen −i community can fall below
  n*_i / (A*⁻¹)_ii. Not defeated by asymmetric interactions, by trait
  dynamics on an operator's own fitness gradient, or by recovery against
  residents that re-adapt, which the claim excludes (the last is
  CLAIM-tmpdsv4t's).
tags:
- ecology
- mathematics
- complex-systems
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
bears_on:
- QUESTION-132
- QUESTION-135
- QUESTION-133
rests_on:
- CLAIM-369
grounds:
- CASE-tmp5sk3q
summary: >-
  LEAD-049's restricted theorem, for the simplest class that has both of
  QUESTION-132's ingredients: CLAIM-369's symmetric resource competition, with
  each operator's niche vector u(θ_i) set by a trait confined to a box and
  moved up the rare-mutant selection gradient (adaptive dynamics' canonical
  equation). The whole system is then a gradient flow of CLAIM-369's
  objective L in a positive diagonal metric. (A) An equilibrium with every
  operator present is locally exponentially stable if each trait is
  interior and stationary or held at a bound by a strictly outward
  gradient, and the Hessian of L on the free coordinates is positive
  definite. Its abundance block is the Gram matrix, so the niche vectors
  must be linearly independent: no more specialists than niche
  dimensions, and no two the same. An undifferentiated equilibrium is
  never asymptotically stable. (B) With residents' traits frozen, a
  specialist removed and reintroduced rare grows at λ_i ≥ n*_i d_i² ≥
  n*_i λ_min(A*), where d_i is the distance of its niche vector from the
  span of the others'. Equality holds in the first when no other
  operator goes extinct in its absence. This extends CASE-118 to k
  components. (C) The same rate holds against re-adapted residents if
  the frozen −i community itself meets (A). The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmp5sk3q CLAIM-tmpdsv4t — new, filed with this claim by LEAD-049 -->

# CLAIM-tmp6kclm: In symmetric resource competition whose operators adapt a bounded niche trait up the selection gradient, a differentiated equilibrium is locally exponentially stable when its traits are interior and stationary or held at a bound with an outward gradient and the Hessian of the shared objective on the free coordinates is positive definite; every specialist then recovers when rare against residents whose traits are frozen, at a rate of at least its abundance times its niche vector's squared distance from the span of the others'

## The model class

There are k operators. Operator i has abundance, or unnormalized
participation intensity, n_i ≥ 0, and a niche trait θ_i in a box Θ (an
interval in the study; a box in ℝᵈ in the proofs). Every operator has the
same smooth niche map u: Θ → ℝᵐ with u ≥ 0, so operators differ only by
their traits. b ∈ ℝᵐ is the supply, c_i > 0 a maintenance cost, and
R = b − Σ_j n_j u(θ_j) the residual supply. Write u_i = u(θ_i), J_i for
the derivative of u at θ_i, U = [u_1 … u_k] and A = UᵀU.

  ṅ_i = n_i (u_i·R − c_i),
  θ̇_i = ε κ_i Proj_Θ [ J_iᵀ R ],  ε > 0, κ_i > 0 (for instance κ_i = n_i).

The first line is CLAIM-369's Lotka–Volterra system, with A_ij = u_i·u_j ≥ 0,
symmetric and competitive, and r = Uᵀb − c. The second moves each trait
up the selection gradient, the per-capita growth of a rare mutant with
trait θ′ against the current residents, differentiated at θ′ = θ_i. The
projection stops a trait at the edge of its box. This is adaptive
dynamics' canonical equation when κ_i = n_i (mutation supply proportional
to abundance). "Bounded niche adaptation" is read as the box.

**Why this class.** It is the smallest addition to a class the record
already holds. At fixed traits it is exactly CLAIM-369's, where the record
has the potential, the KKT reading, and acyclic invasion graphs
(THEORY-1168). One scalar trait already shows both the theorem and the
counterexample (CLAIM-tmpdsv4t). The rare-mutant gradient is chosen over
the operator's own fitness gradient because it keeps the potential. The
own-fitness gradient adds a self-crowding term −n_i J_iᵀu_i. That term is
a gradient only when |u(θ)| is constant, and the class does not cover it.

**Lemma (potential).** With L(n, θ) = ½‖b − Un‖² + c·n,
∂L/∂n_i = −(u_i·R − c_i) and ∂L/∂θ_i = −n_i J_iᵀR. So off the bounds,

  ż = −D ∇L,  D = diag(n_1, …, n_k, εκ_1/n_1, …, εκ_k/n_k),

and dL/dt = −Σ n_i (∂L/∂n_i)² − Σ (εκ_i/n_i)‖Proj ∂L/∂θ_i‖² ≤ 0.
The projection only removes outward components, so it keeps the
inequality.

## The claim

**Theorem A (local stability).** Let z* = (n*, θ*) be an equilibrium with
every n*_i > 0. Call a trait coordinate *held* if it sits at a bound of Θ
and the selection gradient there points strictly outward. Suppose every
trait coordinate is either held or interior with zero gradient. Let F be
the free coordinates, all n_i and the trait coordinates not held, and
H_F the Hessian of L on F at z*. If H_F is positive definite, z* is
locally exponentially stable.

*Proof.* By continuity there is a neighbourhood of z* in which every held
coordinate's gradient stays strictly outward. There a held coordinate at
its bound stays there, and one displaced inward returns to the bound in
a time proportional to its displacement, its speed being bounded below.
During that time the other coordinates move by at most a proportional
amount, so a small enough perturbation reaches the face still near z*.
On the face where the held coordinates are fixed, the flow is
the smooth ż_F = −D_F ∇_F L, and ∇_F L(z*) = 0. Its Jacobian at z* is
therefore −D_F H_F, since the derivative of D_F multiplies a vanishing
gradient. −D_F H_F is similar to −D_F^{1/2} H_F D_F^{1/2}, which is
symmetric and negative definite. So the eigenvalues are real and
negative. ∎

The abundance block of H_F is A* = U*ᵀU*. Positive definiteness therefore
needs the niche vectors u(θ*_i) to be linearly independent, so k ≤ m and
no two operators share a trait. An equilibrium in which two present
operators share a trait is never asymptotically stable. Moving abundance
between them, at fixed total, changes neither R nor any gradient, so it
lies on a line of equilibria. That holds for exactly identical operators
in particular. Their symmetric state is invariant, so differentiation
needs a perturbation to break it.

**Theorem B (recovery when rare, residents frozen).** Let n* > 0 be an
equilibrium at traits θ* with A* positive definite. For each i, let ñ be
the −i community at the same traits: the unique minimizer of the strictly
convex L(·, θ*) over n ≥ 0 with n_i = 0, which is the unique saturated
equilibrium of the system without i. Then i's recovery growth there
satisfies

  λ_i = r_i − (A*ñ)_i ≥ n*_i / (A*⁻¹)_ii = n*_i d_i² ≥ n*_i λ_min(A*) > 0,

where d_i is the distance of u(θ*_i) from the span of the other niche
vectors. Equality holds in the first inequality when no other operator is
absent from ñ.

*Proof.* Let d = n* − ñ. Since ∇_n L(n*) = 0 and L is quadratic in n,
L(ñ) = L(n*) + ½dᵀA*d. By convexity,
L(n*) ≥ L(ñ) + ∇L(ñ)·d + ½dᵀA*d. At ñ the KKT conditions give
∂_jL(ñ) = 0 where ñ_j > 0 and ∂_jL(ñ) ≥ 0 where ñ_j = 0 (j ≠ i). In the
second case d_j = n*_j ≥ 0. So ∇L(ñ)·d ≥ ∂_iL(ñ) n*_i = −λ_i n*_i.
Combining, λ_i n*_i ≥ dᵀA*d. Since d_i = n*_i, the minimum of dᵀA*d
over such d is n*_i²/(A*⁻¹)_ii, which gives the first inequality. When no
other operator is absent, the constrained minimizer is
ñ = n* − λ_i A*⁻¹e_i, and ñ_i = 0 gives equality. 1/(A*⁻¹)_ii is the
Schur complement A*_ii − A*_{i,−i}(A*_{−i})⁻¹A*_{−i,i}, which is d_i². It is
at least λ_min(A*). ∎

With two components, A = [[1, ρ], [ρ, 1]] and r = (1, 1), this gives
n*_i = 1/(1 + ρ) and d_i² = 1 − ρ², so λ_i = 1 − ρ, CASE-118's value.

**Theorem C (recovery against re-adapted residents).** Suppose the frozen
−i community (ñ, θ*_{−i}) itself meets Theorem A's hypotheses for the
system without i. Then it is a locally exponentially stable state of the
adaptive −i system, and a specialist reintroduced there with its old trait
recovers at Theorem B's rate. If the niche vectors are orthogonal (A*
diagonal), removing i changes no other abundance, so the state just after
removal is the frozen −i community. The hypothesis then also decides
whether any resident moves. A resident held at a bound stays exactly when
its outward margin survives the added residual n*_i u(θ*_i).

*Proof.* The first sentence is Theorem A applied to the −i system, and
the rate is Theorem B's, since the residents' traits there are θ*_{−i}.
For the second, with A* diagonal, ∂L/∂n_j = −u_j·b + A*_jj n_j + c_j does
not involve n_i. ∎

## What it does not say

- **That the hypotheses hold.** They are sufficient conditions. Whether
  they hold depends on u, b and c, and CASE-tmp5sk3q checks them in
  two instances.
- **That a specialist recovers against residents that re-adapt.** Theorem
  C needs its hypothesis. CLAIM-tmpdsv4t gives an instance in which every
  hypothesis of A and B holds and C's fails, the residents take over the
  vacated niche, and the removed specialist cannot recover.
- **That the differentiated equilibrium is the only stable state.** L is
  not convex in the traits, so the class allows alternative stable states.
  CLAIM-tmpdsv4t's instance has one.
- **That a trainable specialist's recovery is covered.** The returning
  specialist keeps its old trait. While rare, with κ_i = n_i, it barely
  adapts, but QUESTION-132's frozen-against-trainable distinction is not
  otherwise addressed.
- **Anything for asymmetric interactions or normalized shares.** Those
  are CLAIM-369's two boundaries. The question's next steps (asymmetry,
  delayed adaptation, influence-dependent training) are not attempted.
