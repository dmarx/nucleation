---
number: 313
status: Proposed
formerly:
- THEORY-tmpiu6h1
promote_when: >-
  A line-by-line check of the proof of Proposition 5 (appendix B), which
  this reading followed only in outline, and a second source: either an
  independent derivation of D(p̃‖q̃) ≤ D(Σ_p‖Σ_q) ≤ D(p‖q), or a later
  paper that uses it and confirms the O(σ²) gap beyond the torus. The
  inequalities themselves follow from joint convexity and monotonicity
  of quantum relative entropy and are not in doubt. It is refuted by a
  unit-diagonal kernel and a pair p, q with D(Σ_p‖Σ_q) > D(p‖q), or with
  equality at a non-orthonormal embedding. What cannot settle it:
  numerical agreement of kernel and Shannon estimates on examples, which
  the inequalities permit at any bandwidth.
title: "With a kernel normalised to k(x,x) = 1, the covariance operator of a distribution is a density operator, and its quantum relative entropy is a lower bound on the Kullback–Leibler divergence that is tight only for an orthonormal, hence discrete, embedding, lies above the KL of the kernel-smoothed distributions, and on the torus is within O(σ²) of KL as the bandwidth σ shrinks"
version: 1
tags:
- information-theory
- mathematics
- probabilistic-modeling
date: '2026-10-14'
source:
- LIT-255
summary: >-
  Bach (2022), [LIT-255](../literature.d/LIT-255.md), read in [NOTE-837](../notes.d/NOTE-837.md). Σ_p = ∫ϕϕ* dp is uncentred
  and unit-trace, so p ↦ Σ_p maps distributions to quantum states, and
  D(p̃‖q̃) ≤ D(Σ_p‖Σ_q) ≤ D(p‖q) (Proposition 4(d), Eq. 8). The upper
  bound is joint convexity, with equality only if k(x,y) = 0 for x ≠ y.
  The lower bound is monotonicity under a measurement whose outcome law
  is p smoothed by h(x,y) = ⟨ϕ(x), Σ^{−1/2}ϕ(y)⟩². The O(σ²) gap is shown
  only for translation-invariant kernels on the torus with Lipschitz
  densities. It does not cover centred kernels, or similarity measures
  that compare Gram matrices of representations.
---
<!-- inactive-ok-file: THEORY-233 THEORY-001 THEORY-005 — Proposed; accounts this one is set beside and does not rest on -->

# THEORY-313: With a kernel normalised to k(x,x) = 1, the covariance operator of a distribution is a density operator, and its quantum relative entropy is a lower bound on the Kullback–Leibler divergence that is tight only for an orthonormal, hence discrete, embedding, lies above the KL of the kernel-smoothed distributions, and on the torus is within O(σ²) of KL as the bandwidth σ shrinks

## Source

Bach (2022), "Information Theory with Kernel Methods", [LIT-255](../literature.d/LIT-255.md), read in
[NOTE-837](../notes.d/NOTE-837.md): §2.2 (Proposition 1), §4 (Propositions 3–4), §4.1
(Eq. 8), §4.2 (Proposition 5 and the torus computation), §5.1
(Proposition 6) and appendix A.

## What was actually shown

**The state.** Assume (A1): X compact, k continuous and positive
definite, k(x,x) = 1. Then Σ_p = ∫ϕ(x)ϕ(x)* dp(x) is self-adjoint, PSD
and of unit trace, a mixture of the pure states ϕ(x)ϕ(x)*. p ↦ Σ_p is
injective when k² is universal (Proposition 1). The empirical Σ̂_p from
n samples has the non-zero spectrum of the Gram matrix K/n
(Proposition 6).

**The upper bound.** D(Σ_p‖Σ_q) = tr[Σ_p(log Σ_p − log Σ_q)] ≤ D(p‖q)
(Proposition 4(d)). Write Σ_q = ∫(dq/dp)(x)ϕ(x)ϕ(x)* dp(x) and apply
joint convexity of quantum relative entropy pointwise. Each term
contributes ‖ϕ(x)‖² log(dp/dq)(x). Equality requires k(x,y) = 0 for
x ≠ y, an orthonormal embedding, possible only for discrete X.

**The lower bound.** With h(x,y) = ⟨ϕ(x), Σ^{−1/2}ϕ(y)⟩², where Σ is
the covariance of a base measure τ, the operators
D(y) = Σ^{−1/2}ϕ(y)ϕ(y)*Σ^{−1/2} integrate to the identity under τ. So
they are a measurement, and the law of its outcome under Σ_p is
p̃(y) = ∫h(x,y)dp(x). Monotonicity gives D(p̃‖q̃) ≤ D(Σ_p‖Σ_q) (Eq. 8).

**The gap.** For strictly positive Lipschitz densities,
0 ≤ D(p‖q) − D(p̃‖q̃) ≤ E(p,q)·sup_x ∫h(x,y)d(x,y)²dy (Proposition 5).
On [0,1]^d with k̂(ω) ∝ e^{−σ‖ω‖₁}, the integral is at most dσ²/16. So
the kernel KL is within O(dσ²) of the Shannon KL.

What could have come out otherwise: the quantum relative entropy of the
embedded states could have exceeded the classical one, or had no lower
bound expressible through p and q. Both bounds are proved, not
observed.

## What this does not say

- **Not that kernel KL estimates KL.** It is a lower bound at every
  bandwidth. It converges only as σ → 0, and the estimation rate then
  degrades: the Shannon entropy rate is n^{−2/(d+4)} against an optimal
  n^{−4/(d+4)} (§5.3).
- **Not for centred covariances.** Bach's Σ_p is uncentred (footnote 1).
  A centred covariance is not of unit trace and not a mixture of pure
  states.
- **Not for arbitrary kernels.** The upper bound survives k(x,x) ≤ 1
  (§7). It does not survive kernels with unbounded diagonal, and
  unit-diagonal normalization is what makes Σ_p a state.
- **Not about comparing representations.** The Gram matrices in
  [THEORY-233](THEORY-233.md) are kernels of representations over a fixed stimulus set,
  usually centred and linear. K/tr K there coincides with Bach's K/n only
  when the kernel has unit diagonal and is uncentred. Bach never mentions
  fidelity, Bures distance or representation similarity.
- **The O(σ²) rate is shown only on the torus.** Translation-invariant
  kernels on compact groups are asserted to behave alike, and a
  leverage-score argument is sketched, not completed.
- **Nothing about conditional quantities.** Kernel mutual information
  characterizes independence (Proposition 9). Kernel conditional
  entropies do not decompose, and the submodularity equality case
  characterizes conditional independence only one way (Proposition 11).
  Not filed here.

## Connections

- **[THEORY-233](THEORY-233.md)** (CKA vs normalized Bures). Both treat trace-normalized
  PSD Gram matrices as density matrices. This account says what such a
  matrix is a state *of* when the kernel is unit-diagonal and uncentred:
  the empirical distribution. It also gives the relative entropy of two
  such states a meaning, as a lower bound on KL. [THEORY-233](THEORY-233.md) compares
  fidelity and Euclidean geometries on similar objects, for a different
  purpose. Neither depends on the other.
- **[THEORY-001](THEORY-001.md), [THEORY-005](THEORY-005.md).** Those accounts put the density ratio
  dp/dq at the centre of contrastive representation learning. Here the
  same ratio appears inside the proof of the upper bound, writing Σ_q as
  a reweighting of Σ_p. This is a parallel, not a dependence.
