---
number: 313
status: Active
formerly:
- THEORY-tmpiu6h1
title: "With a kernel normalised to k(x,x) = 1, the covariance operator of a distribution is a density operator, and its quantum relative entropy is a lower bound on the Kullback–Leibler divergence that is tight for every pair of distributions only for an orthonormal, hence discrete, embedding, lies above the KL of the kernel-smoothed distributions, and on the torus, with Fourier coefficients proportional to e^(−σ‖ω‖₁) and strictly positive Lipschitz densities, is within O(σ²) of KL as the bandwidth σ shrinks"
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-313 (batch 043, ADR-047 v2). The sandwich, the equality case
    and the gap bound are re-derived in the dated note below, the gap
    bound independently of the source's appendix B. The title now says the
    bound is tight for every pair only for an orthonormal embedding (a
    single pair can be tight with any kernel, as at p = q), and names the
    kernel family and densities the O(σ²) is proved for. The request for a
    confirmation beyond the torus moves to QUESTION-198.
- version: 3
  date: '2026-10-20'
  note: >-
    The narrowing-loss sweep (batch 071, ADR-047 v4) filed
    THEORY-tmpbqu7h, Proposed, to carry what the narrowing dropped. This
    entry's status, title and claims are unchanged; a dated note says what
    moved.
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
  bound is joint convexity, with equality for every pair only if
  k(x,y) = 0 for x ≠ y.
  The lower bound is monotonicity under a measurement whose outcome law
  is p smoothed by h(x,y) = ⟨ϕ(x), Σ^{−1/2}ϕ(y)⟩². The O(σ²) gap is shown
  only for kernels on the torus with Fourier coefficients proportional
  to e^(−σ‖ω‖₁), with Lipschitz densities. It does not cover centred
  kernels, or similarity measures that compare Gram matrices of
  representations.
extended_by:
- THEORY-tmpbqu7h
---

<!-- inactive-ok-file: THEORY-tmpbqu7h — Proposed; the wider claim this entry's narrowing dropped, filed beside it and cited as open -->
<!-- inactive-ok-file: THEORY-001 THEORY-005 — Proposed; accounts this one is set beside and does not rest on -->

# THEORY-313: With a kernel normalised to k(x,x) = 1, the covariance operator of a distribution is a density operator, and its quantum relative entropy is a lower bound on the Kullback–Leibler divergence that is tight for every pair of distributions only for an orthonormal, hence discrete, embedding, lies above the KL of the kernel-smoothed distributions, and on the torus, with Fourier coefficients proportional to e^(−σ‖ω‖₁) and strictly positive Lipschitz densities, is within O(σ²) of KL as the bandwidth σ shrinks

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
contributes ‖ϕ(x)‖² log(dp/dq)(x). Equality for every pair of
distributions requires k(x,y) = 0 for x ≠ y, an orthonormal embedding,
possible only for discrete X (proved in the note of 2026-10-19).

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
- **The O(σ²) rate is shown only on the torus, for one kernel family.**
  Other translation-invariant kernels, and kernels on compact groups, are
  asserted to behave alike, and a leverage-score argument is sketched,
  not completed ([QUESTION-198](../questions.d/QUESTION-198.md)).
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

## Note of 2026-10-19: the sandwich, the equality case and the gap, re-derived

The promotion audit (batch 043, [ADR-047](../decisions.d/ADR-047.md) v2) re-derived each part. It did
not check appendix B line by line; it gave an independent derivation of
the gap bound instead. Setting (A1): X compact, k continuous, positive
definite, k(x, x) = 1, base measure τ with covariance Σ.

1. **State.** Σ_p = ∫ϕϕ* dp is PSD, and tr Σ_p = ∫k(x, x) dp = 1.
2. **Upper bound.** p ↦ Σ_p is a channel from classical laws to states:
   positive and trace-preserving. So D(Σ_p‖Σ_q) ≤ D(p‖q) by
   monotonicity. Joint convexity, the source's route, gives the same.
3. **When it is tight.** If k(x, y) = 0 for x ≠ y, the states commute
   and D(Σ_p‖Σ_q) = D(p‖q) for every pair. Conversely, suppose
   k(x, y) ≠ 0 for some x ≠ y, and take p ≠ q of full support on {x, y}.
   Equality in monotonicity makes the channel sufficient for {p, q}
   (Petz): its Petz map R recovers both. R ∘ Φ is linear and p, q span
   R², so R would send the pure states ϕ(x)ϕ(x)* and ϕ(y)ϕ(y)* to δ_x
   and δ_y. That raises their trace distance from below 2 to 2, which no
   channel does. So the inequality is strict there. Equality for every
   pair therefore holds exactly for orthonormal embeddings. A continuous
   unit-diagonal kernel that is orthonormal makes every point isolated, so
   X is finite. For a single pair the bound can be tight with any kernel,
   at p = q or for laws on mutually orthogonal points. That is why the
   title says "for every pair". With overlap 0.3, p = (½, ½) and
   q = (¼, ¾): KL is 0.1438 and the quantum relative entropy 0.1348.
4. **Lower bound.** The operators D(y) = Σ^(−1/2)ϕ(y)ϕ(y)*Σ^(−1/2)
   integrate under τ to Σ^(−1/2)ΣΣ^(−1/2) = I, so they form a measurement.
   tr Σ_p D(y) = ∫⟨ϕ(x), Σ^(−1/2)ϕ(y)⟩² dp(x) = p̃(y). Monotonicity under
   the measurement gives D(p̃‖q̃) ≤ D(Σ_p‖Σ_q). Since
   ∫h(x, y) dτ(y) = ‖ϕ(x)‖² = 1, h is a Markov kernel and p̃ is p smoothed
   by it.
5. **The gap.** Let P(x, y) = p(x)h(x, y) and Q(x, y) = q(x)h(x, y). The
   chain rule gives D(p‖q) − D(p̃‖q̃) = E_(p̃) D(p(·|y) ‖ q(·|y)). The
   posterior ratio is ρ(x)/ρ̄(y), with ρ = p/q and ρ̄(y) = E_(q(·|y)) ρ.
   Use KL ≤ χ², and Var ≤ E(ρ(x) − ρ(y))² ≤ C²_(p/q) d(x, y)², where
   C_(p/q) is the Lipschitz constant of p/q in d. These give
   gap ≤ (C²_(p/q) / inf ρ) · sup_x ∫h(x, y)d(x, y)² dτ(y). That is
   Proposition 5's form with a simpler constant.
6. **The torus.** Take τ uniform on [0, 1], k̂(ω) ∝ e^(−σ|ω|) and
   d(x, y) = |sin π(x − y)|, as in the source. Σ is diagonal in the
   Fourier basis, so h(x, y) = g(x − y)², where the Fourier coefficients
   of g are k̂^(1/2): a Poisson kernel. The source's exact integral equals
   ½ tanh(σ/2) tanh(σ/4); a numerical check agreed to four digits for
   σ from 0.01 to 4. Since tanh u ≤ u, it is at most σ²/16. On [0, 1]^d
   with e^(−σ‖ω‖₁) the kernel factorizes, which gives dσ²/16. Hence
   D(p‖q) − D(Σ_p‖Σ_q) ≤ D(p‖q) − D(p̃‖q̃) = O(σ²).

A numerical check on 300 random finite examples satisfied both
inequalities to 10⁻¹³. That the rate extends beyond this kernel family,
as the source asserts, is held in [QUESTION-198](../questions.d/QUESTION-198.md).

## Note of 2026-10-20: the wider claim, filed Proposed

Under [ADR-047](../decisions.d/ADR-047.md) v4 the narrowing-loss sweep (batch 071) filed [THEORY-tmpbqu7h](THEORY-tmpbqu7h.md) as Proposed, extending this entry. It carries the general reading this entry's title carried before the promotion audit narrowed it: that the O(σ²) gap holds for translation-invariant kernels generally and on compact groups, as Bach asserts. This entry is its evidence and is not changed by the filing.
