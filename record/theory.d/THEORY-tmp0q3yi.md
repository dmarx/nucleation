---
status: Active
title: 'With the couplings fixed, the square-loss Gromov–Wasserstein barycenter of several similarity matrices is their realigned average weighted by the barycenter weights, and the KL barycenter its weighted geometric average, so PSD and infinitely divisible inputs give barycenters of the same kind; but the barycenter''s size, histogram and weights are chosen beforehand, the couplings are only stationary points of a non-convex problem, and the iteration''s convergence at the step size used is not proved, so a structure carried by one input is shrunk by its weight at best and can be lost or redistributed by those choices'
version: 1
tags:
- mathematics
date: '2026-10-29'
source:
- LIT-tmp15puu
summary: >-
  Peyré, Cuturi and Solomon (2016), [LIT-tmp15puu](../literature.d/LIT-tmp15puu.md), Propositions 3–5 and
  Remark 3, read in [NOTE-tmppwiml](../notes.d/NOTE-tmppwiml.md) from the PMLR PDF. The closed forms and
  the cone preservation are proved and the PSD case was checked; the lack
  of guarantees is the authors' own statement. Active as a statement of
  what is and is not guaranteed. It does not say a barycenter erases
  minority structure; a toy run showed seed-dependent redistribution, not
  erasure.
---
<!-- inactive-ok-file: CLAIM-348 — Proposed; the claim this bears on, cited as open -->

# THEORY-tmp0q3yi: With the couplings fixed, the square-loss Gromov–Wasserstein barycenter of several similarity matrices is their realigned average weighted by the barycenter weights, and the KL barycenter its weighted geometric average, so PSD and infinitely divisible inputs give barycenters of the same kind; but the barycenter's size, histogram and weights are chosen beforehand, the couplings are only stationary points of a non-convex problem, and the iteration's convergence at the step size used is not proved, so a structure carried by one input is shrunk by its weight at best and can be lost or redistributed by those choices

## Source

Peyré, Cuturi and Solomon (2016), [LIT-tmp15puu](../literature.d/LIT-tmp15puu.md), §§2.3–3.1, pp. 2667–2669 of
the ICML 2016 proceedings; read in [NOTE-tmppwiml](../notes.d/NOTE-tmppwiml.md).

## What was actually shown

**The closed form (Prop. 3, p. 2668).** For a loss L(a, b) = f₁(a) + f₂(b)
− h₁(a)h₂(b) with f₁′/h₁′ invertible, the C step minimizing
Σ λ_s ⟨L(C, C_s) ⊗ T_s, T_s⟩ is C = (f₁′/h₁′)⁻¹(Σ λ_s (realigned h₂(C_s)) /
ppᵀ). This is a global minimizer when L is convex in its first argument
(p. 2668). The realigned matrix is T_s h₂(C_s) T_sᵀ for T_s ∈ ℝ^{N×N_s}.
The paper prints T_sᵀ … T_s, which does not fit its own convention.

**Square loss and KL (Props. 4–5, pp. 2668–2669).** For square loss the
update is the weighted arithmetic average of the realigned C_s, divided
entry-wise by ppᵀ. A positive combination of PSD matrices with a positive
diagonal rescaling is PSD, so PSD inputs give PSD iterates. For KL the
update is the exponential of the weighted average of the realigned
log C_s, and conditional positive-definiteness is preserved, so
infinitely divisible inputs give infinitely divisible iterates. Checked:
200 random trials with PSD inputs of sizes 3, 7 and 4 gave a smallest
eigenvalue of at least 0.009.

**What is not guaranteed.** The coupling step converges for step sizes
below a τ_max, but the step τ = 1/ε that makes it a Sinkhorn iteration "is
not covered by the theory" (Remark 3, p. 2667). The barycenter problem "is
convex with respect to C but not with respect to (Ts )s" (p. 2668). Its
size N and histogram p are "fixed by the user" (p. 2668).

**What could have failed.** The closed-form average could have left the
PSD or infinitely divisible cone, which would make the barycenter of
kernels not a kernel. The propositions rule that out.

## What this does not say

- **That a minority's structure is erased.** With couplings fixed it is
  shrunk by its weight λ_s. In a toy run (three two-cluster inputs, one with
  a split cluster, λ = ¼, N = 8), the optimized barycenters landed on 9
  distinct objective values over 20 seeds. The split survived at sizes
  between 2.20 and 5.24, against 0.92 for the fixed-alignment average.
  What the optimization does to a minority distinction depends on the
  initialization and on N, p, λ and ε.
- **That the barycenter is unique**, or the same across initializations.
- **That the barycenter is the structure common to the inputs.** It is a
  Fréchet mean under GW_ε for weights and a size chosen in advance.
