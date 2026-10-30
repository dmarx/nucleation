---
number: 728
status: Active
formerly:
- THEORY-tmpt7p6d
title: 'On a finite data set, a symmetric positive affinity normalized to a Markov operator is conjugate to a symmetric one, and its eigenvectors scaled by powers of their eigenvalues embed the data so that Euclidean distance equals the diffusion distance weighted by the inverse stationary law'
version: 2
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-565 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-565.yaml, batch 010, ADR-047).
    THEORY-565's promote_when concerns only the analytic half, the
    α-family and the Laplace–Beltrami limit of Theorem 2.1, which LIT-981
    defers to a companion paper. The finite-data construction and its
    isometry are stated in LIT-981 and called standard. NOTE-784 is a skim
    whose displayed equations were not visible, so the derivation is
    written out below and checked. Under ADR-047 v2 (the owner's rule of
    2026-10-19), a step-by-step re-derivation in the decision file meets
    the condition. THEORY-565 keeps the analytic half and extends this one.
- version: 2
  date: '2026-10-30'
  note: >-
    The twenty-first status review, at the status review's ruling (the
    owner delegated these rulings). LIT-981 is now read in full with every
    equation seen (NOTE-tmpjjdsb), which supersedes the skim of NOTE-784.
    The summary and Source said the paper was "skimmed in NOTE-784"; they
    now name the full reading, and say that the paper's own diffusion
    distance is the one its symmetric kernel ã^(m) induces, so that the
    1/π-weighted definition used here is the companion's (LIT-1246), not
    the paper's (ADR-047 kind 3). The title and the derivation are
    unchanged.
tags:
- mathematics
- representation-learning
date: '2026-10-19'
source:
- LIT-981
summary: >-
  Coifman et al. (2005), LIT-981, read in full in NOTE-tmpjjdsb, with
  the derivation written out here; the 1/π-weighted distance is the
  companion's (LIT-1246), not the paper's own. For n
  points and a symmetric affinity K with positive entries, A = D⁻¹K is a
  Markov matrix with stationary law π ∝ d. It is conjugate to the
  symmetric D^(-1/2) K D^(-1/2), so its eigenvalues are real and in
  [−1, 1], and in [0, 1] when K is positive semi-definite. The map
  x ↦ (λ_j^m ψ_j(x))_{j≥1} turns the m-step diffusion distance, weighted by
  1/π, into Euclidean distance exactly. Truncation gives a lower bound. It
  says nothing about the continuum limit, which is [THEORY-565](THEORY-565.md).
extended_by:
- THEORY-565
---
<!-- inactive-ok-file: THEORY-565 — Proposed; the analytic half this was split from and that extends it, cited as open -->
<!-- inactive-ok-file: NOTE-784 — Superseded; the skim the construction was first filed from, named as such -->

# THEORY-728: On a finite data set, a symmetric positive affinity normalized to a Markov operator is conjugate to a symmetric one, and its eigenvectors scaled by powers of their eigenvalues embed the data so that Euclidean distance equals the diffusion distance weighted by the inverse stationary law

## Source

Coifman, Lafon, Lee, Maggioni, Nadler, Warner & Zucker (2005), "Diffusion
maps", *PNAS* 102(21), [LIT-981](../literature.d/LIT-981.md), read in full in NOTE-tmpjjdsb (2026-10-30),
which replaces the skim of [NOTE-784](../notes.d/NOTE-784.md). The paper states the construction
and the embedding and calls them standard. Its own diffusion distance is
the one its symmetric kernel ã^(m) induces, with the eigenfunctions of ã as
coordinates. The definitions below are the companion's (LIT-1246), in
particular the 1/π weighting of the diffusion distance, and the derivation
is the record's.

## What was actually shown

Take n points and a symmetric matrix K = (k(x, y)) with positive entries.
Let d(x) = Σ_y k(x, y), D = diag(d), vol = Σ_x d(x) and π = d/vol.

- **A Markov operator with stationary law π.** A = D⁻¹K has rows summing to
  1. πA = 1ᵀK/vol = dᵀ/vol = π, by the symmetry of K.
- **Conjugate to a symmetric matrix.** Ã = D^(1/2) A D^(-1/2) =
  D^(-1/2) K D^(-1/2) is symmetric, so Ã = Σ_j λ_j v_j v_jᵀ with orthonormal
  v_j and real λ_j. A is stochastic, so |λ_j| ≤ 1, and λ₀ = 1 with
  v₀ = √d/√vol. If K is positive semi-definite, so is Ã, being a congruence
  of K, and every λ_j ≥ 0.
- **Spectral form of the walk.** Put ψ_j = √vol · D^(-1/2) v_j and
  φ_j = D^(1/2) v_j / √vol. Then A^m = Σ_j λ_j^m ψ_j φ_jᵀ, ψ₀ ≡ 1, and
  Σ_y φ_i(y) φ_j(y) / π(y) = v_iᵀ v_j = δ_ij.
- **The isometry.** Define the diffusion distance
  D_m(x, z)² = Σ_y (A^m(x, y) − A^m(z, y))² / π(y). Substituting the
  spectral form, A^m(x, ·) − A^m(z, ·) = Σ_j λ_j^m (ψ_j(x) − ψ_j(z)) φ_j,
  and the φ_j are orthonormal in the 1/π-weighted inner product, so
  D_m(x, z)² = Σ_j λ_j^(2m) (ψ_j(x) − ψ_j(z))². The j = 0 term vanishes
  because ψ₀ is constant. So x ↦ (λ_j^m ψ_j(x))_{j≥1} is an isometry from
  the diffusion distance to Euclidean distance, for every m.
- **Truncation.** Keeping only the first few coordinates drops nonnegative
  summands. The truncated distance is a lower bound, short by exactly the
  dropped terms, which are small once λ_j^(2m) is. That is the approximate
  isometry the paper states.

Without the symmetry of K there is no symmetric conjugate, no real
orthonormal eigenbasis, and the identity fails. The positive semi-definite
hypothesis is used only for λ_j ≥ 0. Without it the eigenvalues lie in
[−1, 1], and the coordinates λ_j^m ψ_j are signed, but the isometry still
holds.

## What this does not say

- **Anything about the continuum.** The α-family and the convergence of the
  α = 1 normalization to the Laplace–Beltrami operator are [THEORY-565](THEORY-565.md)'s,
  Proposed until the companion paper's proofs are read.
- **That the weighting is the paper's.** The 1/π weighting is the
  companion's definition (LIT-1246). The paper's own distance, seen in
  NOTE-tmpjjdsb, is induced by ã^(m) and has its own isometry in the
  unrescaled coordinates. Without the weighting this identity does not
  hold.
- **How many coordinates to keep.** That is set by a precision threshold,
  not by any task.
- **Anything for non-symmetric kernels.** A non-reversible walk has no
  symmetric conjugate.
