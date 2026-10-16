---
status: Active
title: "The nearest rank-r matrix to a real matrix in the least-squares norm keeps its r largest singular values and zeroes the rest; it is unique when the r-th and (r+1)-th singular values differ, its squared error is the sum of the dropped squares, and the singular-vector factors that build it are not unique"
version: 1
tags:
- mathematics
- representation-learning
date: '2026-10-16'
source:
- LIT-330
summary: >-
  Eckart & Young (1936), [LIT-330](../literature.d/LIT-330.md), read in full in [NOTE-301](../notes.d/NOTE-301.md), which checked
  the error bound. The argument is first-order stationarity on the
  orthogonal group plus two cited theorems (the SVD and a simultaneous-SVD
  criterion), and assumes a minimiser exists. Only the Frobenius norm and
  real matrices are covered. Uniqueness is of the approximating matrix,
  under a spectral gap, never of the factors; the paper's last section
  argues the canonic components cannot be read straightforwardly as
  psychological factors.
---

<!-- inactive-ok-file: THEORY-002 — Proposed; named in Connections, not leaned on -->

# THEORY-tmpdkgv9: The nearest rank-r matrix to a real matrix in the least-squares norm keeps its r largest singular values and zeroes the rest; it is unique when the r-th and (r+1)-th singular values differ, its squared error is the sum of the dropped squares, and the singular-vector factors that build it are not unique

## Source

Eckart & Young (1936), "The approximation of one matrix by another of lower
rank", *Psychometrika* 1(3):211–218, [LIT-330](../literature.d/LIT-330.md), read in full in [NOTE-301](../notes.d/NOTE-301.md).

## What was actually shown

**The problem.** For a real n×N matrix a of rank R, find the matrix β of rank
r < R nearest to a in the least-squares distance, the square root of
Σ_ij (a_ij − β_ij)².

**The tools, cited (Thms I–II, pp. 213–214).** Every real matrix has a
"canonic resolution" a = u′λU with u, U orthogonal and λ diagonal and
non-negative, now the SVD. Two matrices are diagonalised by one orthogonal
pair iff aβ′ and β′a are symmetric. Both are taken from the literature, not
proved.

**The argument (pp. 215–216).** The distance is invariant under orthogonal
transformations on either side (eq. 9). Writing β = u′μU and varying u and U
along skew-symmetric increments, stationarity forces aβ′ and β′a symmetric,
so a and β share singular vectors, and the squared distance becomes
Σ_i (λ_i − μ_i)² with only r of the μ_i non-zero.

**The result (eq. 17).** With λ₁ ≥ λ₂ ≥ ⋯, take μ_i = λ_i for i ≤ r and 0
otherwise. "This is also the only solution unless λ_r = λ_{r+1}." The minimum
squared error is Σ_{i=r+1}^R λ_i², so the error is at most l(1 − r/R)^{1/2},
with l the length of a. [NOTE-301](../notes.d/NOTE-301.md) checked the bound.

**A corollary, asserted (p. 216).** The best rank-r approximation of a gives
the best of aa′ (as ββ′) and of a′a (as β′β). The proof is "readily
supplied" and not written out.

**What could have come out otherwise.** The best approximation could have
needed singular vectors other than a's. Stationarity rules that out.

## What this does not say

- **That the factors are unique.** Uniqueness is of β, and only under a gap
  λ_r > λ_{r+1}. u and U are not unique: the rows of U beyond the rank are
  arbitrary, and equal singular values allow rotations. ββ′ determines β
  only up to an orthogonal transformation on the right.
- **That the canonic components are the real underlying factors.** The
  paper's own last section argues that reading them as abilities and test
  demands, with λ² as variances, is "not a tenable interpretation", because
  tests and individuals enter symmetrically (pp. 217–218).
- **The spectral norm or other unitarily invariant norms.** That is Mirsky
  (1960), not in the record.
- **A complete optimality proof.** The argument is first-order and assumes a
  minimiser exists; existence follows by compactness, which the paper does
  not say.
- **Priority.** Standard histories credit E. Schmidt (1907) with the result
  for integral operators. The reading did not check it.
- **Anything about models trained separately.** The theorem fixes the
  truncation of one given matrix; it says nothing about whether two models'
  representations agree. A "Universal Convergence" argument that leans on it
  for uniqueness of factors goes beyond it ([NOTE-301](../notes.d/NOTE-301.md)).

## Connections

- [THEORY-004](THEORY-004.md): a representation is fixed by its kernel up to an orthogonal
  transformation. The ββ′ corollary is its matrix form: the best Gram-matrix
  approximation fixes β only up to that freedom.
- [THEORY-002](THEORY-002.md): convergence of kernels fixes representations only up to a
  symmetry group. Eckart–Young gives the low-rank truncation of a kernel,
  not a unique factor.
