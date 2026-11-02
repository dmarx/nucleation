---
status: Proposed
promote_when: >-
  A computation of the low-lying Lindbladian spectrum, by tensor-network
  diagonalization, long-time evolution or an equivalent method, for a
  chaotic chain at system sizes well beyond exact diagonalization, at fixed
  weak γ, in a case where the integral of motion is not an exact
  eigenoperator (the energy of the mixed-field Ising model is the paper's
  example), showing that its decay rate stays near the first-order value
  and that its overlap with the slowest eigenoperator stays close to one as
  L grows; or a proof bounding ε₁∫₀^∞ e^{γ_V t}‖J₁(t)‖dt independently of L
  once hydrodynamic modes are accounted for. Agreement at L ≤ 9, or
  numerics in integrable models only, does not settle it, and neither does
  insensitivity of slow eigenvalues to L in a model whose IOMs are exact
  eigenoperators.
title: 'The first-order picture in which a small integral of motion Q of a many-body Hamiltonian is, under weak local noise, the slowest Lindbladian eigenoperator holds at large system size whenever its leak ε out of span{Q} satisfies ε ≲ γ ≪ 1, because the gap controlling the perturbation is not the exponentially small level spacing but one of order min(γL, √(v_Bγ)), set by the ballistic growth of the operators Q leaks into'
version: 1
tags:
- natural-sciences
- complex-systems
date: '2026-11-02'
source:
- LIT-tmp8mp1c
summary: >-
  Yang and Abanin (2025), [LIT-tmp8mp1c](../literature.d/LIT-tmp8mp1c.md), §IV, read in [NOTE-tmpxpf7y](../notes.d/NOTE-tmpxpf7y.md).
  Proposed because the argument assumes fully chaotic operator growth for
  the complement, is checked numerically only at nine sites, and is
  qualified by the authors themselves: hydrodynamic modes give a continuum
  of slow modes in the Mori limit, so the gap "might not exist at all"
  outside sectors orthogonal to them.
---
<!-- inactive-ok-file: CLAIM-478 — Proposed; the claim the time-scale ratio bears on -->

# THEORY-tmpull8q: The first-order picture in which a small integral of motion Q of a many-body Hamiltonian is, under weak local noise, the slowest Lindbladian eigenoperator holds at large system size whenever its leak ε out of span{Q} satisfies ε ≲ γ ≪ 1, because the gap controlling the perturbation is not the exponentially small level spacing but one of order min(γL, √(v_Bγ)), set by the ballistic growth of the operators Q leaks into

## Source

Yang and Abanin (2025), [LIT-tmp8mp1c](../literature.d/LIT-tmp8mp1c.md), §IV (eqs. 13–23, Fig. 5), pp. 6–8;
read in [NOTE-tmpxpf7y](../notes.d/NOTE-tmpxpf7y.md).

## What was actually shown

**The argument.** Write L†[Q] = −γ_Q Q + ε₁J₁ (eq. 13), with ε₁ ∼ γ for an
exact IOM and ε₁ ∼ ‖δH‖ for an approximate one. An eigenoperator
V = Q + V⊥ satisfies ‖V⊥‖ ≲ |ε₁|∫₀^∞ e^{γ_V t}‖J₁(t)‖dt (eq. 20). Without
noise ‖J₁(t)‖ is constant and the integral diverges for any ε₁. With noise,
if J₁ grows ballistically, ‖J₁(t)‖ ∼ e^{−γv_B t²/2} for v_B t < L and
e^{−γLt} after (eq. 21), so the integral converges and
‖V⊥‖ ≲ ε₁/E_g^< with E_g^< ∼ min(γL, √(v_Bγ)) (eq. 22), which does not
shrink with L and is ≫ γ at small γ and large L. Hence "we reasonably
expect the perturbation theory to hold as long as ε ≲ γ ≪ 1" (p. 8).

**The check.** Fig. 5: for MFIM with hz = 0.05 (a perturbed TFIM), L = 9,
and A₁ as the approximate IOM, γN(t) converges to an O(1) value and
(E_g^<)⁻¹ behaves as γ⁻¹ at small γ. Appendix D (Fig. 9, TFIM, γ = 0.1)
shows bulk decay rates growing with L while the slow ones do not, at small
L.

What could have come out otherwise: the integral in Fig. 5 could have
failed to converge, or (E_g^<)⁻¹ could have scaled otherwise in γ.

## What this does not say

- **That the gap exists.** The authors' first comment (p. 8): modulated
  energy densities H_k have O(k) commutators with H, giving "a continuum of
  slow modes" in the Mori limit, so the gap "must be defined in sectors
  that are orthogonal to all hydrodynamic modes … and might not exist at
  all". The argument then needs the parallel subspace widened to all
  relevant IOMs, which the authors call "challenging" in practice.
- **That it covers integrable models.** It assumes ballistic growth of the
  complement as in "fully chaotic systems"; the relaxation to "some form of
  operator growth such that J₁(t) has a larger size than Q at late times"
  is asserted, not shown.
- **That large L has been reached.** The only sizes computed are L ≤ 9.
- **The time-scale ratio as a result.** That the slow and fast rates
  separate by a factor of order √(v_B/γ) follows from eq. 22 under the
  same assumptions, and is the record's reading for [CLAIM-478](../claims.d/CLAIM-478.md), not a
  number the paper reports.
