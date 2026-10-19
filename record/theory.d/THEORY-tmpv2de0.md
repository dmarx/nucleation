---
status: Active
title: "For an embedding whose Gram matrix is the absolute co-occurrence deviation matrix at full rank, words on a periodic lattice whose positive and negative co-occurrence parts each depend only on separation have Fourier modes of the lattice as principal components, in degenerate cos/sin pairs with amplitude the square root of the kernel's Fourier transform, and the exponential kernel gives a closed loop with integer frequencies on a periodic lattice and an open curve with non-integer frequencies on an interval"
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-183 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-183.yaml, batch 011, ADR-047).
    THEORY-183's promote_when concerns only the empirical carry-over, that
    trained embeddings and language models get their circles from this
    symmetry, and it is unchanged there. The theorem was read with its
    proofs followed step by step in NOTE-664. Proposition 1 and
    Corollary 2 are re-derived below and in the decision file (ADR-047
    v2). Propositions 3 and 4 are carried as read.
tags:
- mathematics
- representation-learning
date: '2026-10-19'
source:
- LIT-860
summary: >-
  Karkada, Korchinski, Nava, Wyart & Bahri (2026), [LIT-860](../literature.d/LIT-860.md), Propositions 1,
  3 and 4 and Corollary 2, with the proofs in Appendix E followed in
  [NOTE-664](../notes.d/NOTE-664.md). The result is conditional throughout. It concerns an idealised embedding
  with W Wᵀ = |M*| and d ≥ rank M*, not a trained one. It needs the
  positive and negative parts of M* to be translation invariant
  separately (Assumption B.1), not M* alone. It says nothing about whether
  any corpus or model satisfies these conditions, which is [THEORY-183](THEORY-183.md).
extended_by:
- THEORY-183
---
<!-- inactive-ok-file: THEORY-183 THEORY-182 — Proposed; the empirical account this was split from, and the premise about trained embeddings that this result does not assume -->

# THEORY-tmpv2de0: For an embedding whose Gram matrix is the absolute co-occurrence deviation matrix at full rank, words on a periodic lattice whose positive and negative co-occurrence parts each depend only on separation have Fourier modes of the lattice as principal components, in degenerate cos/sin pairs with amplitude the square root of the kernel's Fourier transform, and the exponential kernel gives a closed loop with integer frequencies on a periodic lattice and an open curve with non-integer frequencies on an interval

## Source

Karkada, Korchinski, Nava, Wyart and Bahri (2026), [LIT-860](../literature.d/LIT-860.md),
Propositions 1, 3 and 4, Corollary 2 and Appendix E, as read in
[NOTE-664](../notes.d/NOTE-664.md). Proposition 1 and Corollary 2 are re-derived here.

## What was actually shown

**Setting.** M*_ij = (P_ij − P_iP_j)/(½(P_ij + P_iP_j)), split as
M* = M⁺ − M⁻ into its positive and negative parts, so |M*| = M⁺ + M⁻.
An embedding W has W Wᵀ = |M*| with d ≥ rank M*. A set S of words sits on
a periodic lattice Λ = (ℤ/L)^D with coordinates x_i. On S, the blocks of
M⁺ and M⁻ each depend only on x_i − x_j (Assumption B.1). Then the Gram
matrix of the vectors w_i, i ∈ S, is G_ij = c(x_i − x_j) for an even c.
That is the S-block of |M*|, not |M*_SS|, which is why B.1 rather than
translation invariance of M* is needed.

**Proposition 1, re-derived.**

1. G is circulant. For each wavevector k of the dual lattice,
   e_k(i) = exp(ik·x_i) satisfies
   (G e_k)(i) = e^{ik·x_i} Σ_{y∈Λ} c(y) e^{−ik·y} = m̃(k) e_k(i).
2. c is even, so m̃(k) is real and m̃(k) = m̃(−k). G is a Gram matrix, so
   m̃(k) ≥ 0. For k ≢ −k, cos(k·x) and sin(k·x) span the eigenspace of the
   pair {k, −k}. That pair is the degeneracy. At a Nyquist wavevector only
   cos survives.
3. The unit eigenvectors are √(2/|S|) cos(k·x_i) and √(2/|S|) sin(k·x_i).
   A Nyquist mode's is |S|^(−1/2) cos(k·x_i).
4. Centring by H = I − 11ᵀ/|S| commutes with G, because the constant
   vector is the k = 0 eigenvector. It removes that mode alone.
5. From the SVD of the centred embedding matrix, the coordinate of word i
   on the principal direction for eigenvalue λ_k with unit eigenvector
   u_k is √λ_k u_k(i). So the PCA coordinates are
   √(2 m̃(k)/|S|) cos(k·x_i) and √(2 m̃(k)/|S|) sin(k·x_i), in pairs,
   plus √(m̃(k)/|S|) cos(k·x_i) for Nyquist modes. This holds up to
   rotation within each degenerate eigenspace and the order of the
   directions.

**Corollary 2, re-derived.** For D = 1, take L sites with spacing 2/L and
the kernel e^(−|Δx|/σ), periodised. With q = e^(−2/(σL)) and θ = 2k/L,
m̃ = Σ_{m∈ℤ} q^|m| e^{−iθm} = (1 − q²)/(1 − 2q cos θ + q²), so
a = √((2/L) m̃). As L → ∞, a² → 2σ/(1 + σ²k²), with k_n = πn: a closed
loop with integer frequencies.

**Proposition 3, as read.** On an interval with open boundary, in the
continuum limit, the exponential kernel is the Green's function of
(1 − σ²∂²)/(2σ) with Robin boundary conditions. Its eigenfunctions are
sin kx with tan k = −σk, and, after centring, cos kx − sin k / k with
tan k = k/(1 + σ(1 + σ)k²). The eigenvalue is 2σ/(1 + σ²k²) in both
sectors. The curve is open, with non-integer frequencies ([NOTE-664](../notes.d/NOTE-664.md), C2,
strong).

**Proposition 4, as read.** On a periodic lattice whose eigenvalues do not
increase with |k|, the best rank-r linear probe for the latent coordinate
has relative squared error O(r^(−1/D)) ([NOTE-664](../notes.d/NOTE-664.md), C3, strong for the
periodic lattice).

Each could have come out otherwise. A kernel that is not translation
invariant gives eigenvectors that are not Fourier modes. And B.1 is
needed: invariance of M* alone does not make the S-block of |M*|
invariant.

## What this does not say

- **That any corpus has this symmetry, or that a trained embedding or a
  language model reads it off.** Every hypothesis above is about the
  statistics and an idealised factorisation. Whether Wikipedia's month and
  year statistics satisfy B.1, and whether trained networks inherit the
  geometry, is [THEORY-183](THEORY-183.md), which stays Proposed.
- **That word2vec is such an embedding.** That is [THEORY-182](THEORY-182.md), shown only
  for a tied quartic proxy.
- **Anything at moderate dimension.** d ≥ rank M* is assumed. Compression
  is treated in the source only empirically (§4).
- **Absolute amplitudes on real data.** M* is indefinite, so the kernel
  fitted to M* is not the one factorised. Only relative amplitudes and
  frequencies are predicted.
