---
status: Active
title: "A two-layer ReLU student of width at least kM, fitting an orthonormal teacher of M neurons on the sphere, has for any k global minima a global minimum joined to each by a two-piece linear path of minima; and in a deep linear network of depth L and width above 1 + r(L − 1), any r global minima in general position share a global minimum linearly connected to each"
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-110 at the owner's direction, carrying out the
    promotion audit's decision for THEORY-110 (batch 044, ADR-040 and
    ADR-047 v2), on the pattern of THEORY-736's split from THEORY-109.
    THEORY-110 bundled an empirical conjecture with theorems proved in toy
    models. NOTE-535 read those proofs for statement and structure only,
    so the audit re-derived them from LIT-682's Appendices A.1, A.4–A.5 and
    B.1, as set out below. This THEORY holds the theorems; THEORY-110 keeps
    the conjecture and extends this one. Lin et al.'s probabilistic
    Theorem 10 is left out: its bound is not derived.
tags:
- loss-landscapes
- mathematics
- anthology-candidate
date: '2026-10-19'
source:
- LIT-682
summary: >-
  Lin, Li and Wu (2024), [LIT-682](../literature.d/LIT-682.md), Theorems 6, 11 and 18 with Lemmas 7 and
  25, read in [NOTE-535](../notes.d/NOTE-535.md) and re-derived by the promotion audit. Two toy
  models whose minima can be written down: a two-layer ReLU student of an
  orthonormal teacher on the sphere at population loss, and a deep linear
  network fitting y = Qx. Spare width lets every minimum be moved, along
  segments of minima, to one a common centre can reach. No permutation
  symmetry is used, and nothing is claimed about trained networks.
extended_by:
- THEORY-110
---
<!-- inactive-ok-file: THEORY-110 THEORY-109 — Proposed; the conjecture this was split from, and the precedent named in its history, neither leaned on -->

# THEORY-tmpettm0: A two-layer ReLU student of width at least kM, fitting an orthonormal teacher of M neurons on the sphere, has for any k global minima a global minimum joined to each by a two-piece linear path of minima; and in a deep linear network of depth L and width above 1 + r(L − 1), any r global minima in general position share a global minimum linearly connected to each

## Source

Lin, Li and Wu (2024), "Exploring Neural Network Landscapes: Star-Shaped
and Geodesic Connectivity", [LIT-682](../literature.d/LIT-682.md) (arXiv:2404.06391), read in [NOTE-535](../notes.d/NOTE-535.md).
The proofs, Appendices A.1, A.4–A.5 and B.1, were worked through by the
promotion audit (batch 044).

## What was actually shown

**The ReLU minima (Theorem 6).** The teacher is Σ_{j≤M} σ(x_j), M ≤ d,
with x uniform on the sphere, and the student Σ_{i≤m} σ(w_i·x). Zero
population loss means the two agree on the sphere. Setting x = ±e_j gives
w_ij ≥ 0 and Σ_i w_ij = 1 for j ≤ M, and w_ij = 0 for j > M. Setting
x = √(1−ε²)e₁ − εe₂ shows no neuron has two non-zero entries. Conversely,
any such W fits, since σ(Σ_j w_ij x_j) = Σ_j w_ij σ(x_j) when w_ij ≥ 0. So
every neuron is zero or a positive multiple of one e_j, and each column
sums to 1. The paper's statement allows any non-zero multiple; its own
proof gives positive ones, and with negative multiples the set is wrong
(rows 2e₁ and −e₁ sum to e₁ but give 2σ(x₁) + σ(−x₁) ≠ σ(x₁)).

**When two ReLU minima are linearly connected (Lemma 7).** Exactly when,
row by row, one of them is zero or both are positive multiples of the same
e_j. A segment between rows with different supports passes through rows
with two non-zero entries, and otherwise every point of the segment keeps
the form and the column sums.

**A common centre, by two-piece paths (Theorem 11).** Let m ≥ kM. Merge
each minimum θ_i to θ_i⁰: keep one row e_t for each type t, at a row where
θ_i has type t, and zero the rest. By Lemma 7, θ_i and θ_i⁰ are linearly
connected. The non-zero rows of θ_1⁰, …, θ_{k−1}⁰ number at most (k−1)M, so
at least M rows are zero in all of them. Put e_1, …, e_M on M such rows,
matching θ_k⁰'s type wherever θ_k⁰ is non-zero there, and zero elsewhere.
That is a minimum linearly connected to every θ_i⁰, and so joined to every
θ_i by two segments of minima.

**A common centre, by straight lines, for deep linear networks
(Theorem 18).** The network is A_L⋯A₁x with widths m, data y = Qx with
zero-mean, non-degenerate inputs, so the minima are the factorisations
A_L⋯A₁ = Q. The product along the segments Π_l (tA_l^{(i)} + (1−t)A_l*) is
a polynomial in t whose coefficient of t^k(1−t)^{L−k} is the sum of the
products taking k factors from θ_i. It equals Q for every t if and only if
that sum is C(L, k)Q for every k. Choosing A_L*, …, A₂* in turn by a
linear-independence lemma (Lemma 25) keeps all the partial products
independent, which needs width above (w+1)r + 1 at step w, and so above
(L−1)r + 1 at the last. The (L−1)r + 1 conditions on A₁* then have
independent coefficient rows and are solved column by column. This needs
the r minima to be in general position: for each k, the partial products
A_L^{(i)}⋯A_{L−k+1}^{(i)} are independent (the paper's Assumption 26). The
paper says this fails only on a null set of r-tuples of minima, without
arguing it. Lemma 25's hypothesis "r₁ > q" should read r₁ ≥ p; where it is
used, r₁ = m and both hold.

## What this does not say

- **Not Theorem 10.** Lin et al.'s probability that k ReLU minima share a
  *linearly* connected centre, 1 − M((M^k − 1)/M^k)^{m−kM}, is not
  derived. Its proof takes a uniform distribution on a set made of pieces
  of different dimension without defining it, treats rows as independent
  and uniform over the M + 1 neuron types, and then uses the chance 1/M²
  where that model gives 1/(M + 1)².
- **Nothing about trained networks.** The ReLU result is at population loss
  for an orthonormal teacher on the sphere; the linear one is for linear
  networks. That trained networks' solution sets are star domains modulo
  permutation is [THEORY-110](THEORY-110.md)'s conjecture, which stays Proposed.
- **Not that the centre is linearly connected for ReLU.** Theorem 11 gives
  two-piece paths.
- **Not about permutation symmetry.** The mechanism is spare width, not
  alignment.

## Connections

- [THEORY-110](THEORY-110.md) extends this account: its evidence for a star domain in
  trained networks comes from Sonthalia et al.'s measurements, and these
  theorems are the toy-model case.
- [THEORY-736](THEORY-736.md) is the same mechanism for curves: spare capacity lets working
  units be moved at no cost, so solutions connect.
