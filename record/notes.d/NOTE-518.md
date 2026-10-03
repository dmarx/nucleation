---
number: 518
status: Read
formerly:
- NOTE-tmp55ipv
paper: 'LIT-683'
title: 'Exact expressions for double descent and implicit regularization via surrogate random design'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v3 (27 pages, text layer). Sections 1–6 read in full and
    the theorem statements checked against the extracted text. Appendices A
    (Lemma 1, expected sample size), B (Lemmas 4–6 and Lemmas 8–9 cited from
    Dereziński et al. 2019 and Kulesza and Taskar), C (Theorem 1 through
    Lemmas 10–11), D (Lemma 2 and Theorem 2) and E (Theorem 3) followed in
    outline, not checked line by line. Appendix F (experiment details)
    skimmed.
date: '2026-10-03'
summary: >-
  Surrogate design S^n_μ = Det(μ, K), density ∝ pdet(XXᵀ), K Poisson(γn)
  truncated at d. E[#rows] = n (Lemma 1); E[I − X̄⁺X̄] = (γnΣ + I)⁻¹ (Lemma
  2); E[tr((X̄ᵀX̄)⁺)] = γn(1 − det((I/γn + Σ)⁻¹Σ)) (Lemma 3); λn = 1/γn. These
  give exact MSE in all regimes (Theorem 1) and E[X̄⁺ȳ] = (Σ + λnI)⁻¹v for
  n < d, with n = tr(Σ(Σ + λnI)⁻¹) (Theorem 2). For sub-Gaussian rows the
  i.i.d.-design MSE converges to the surrogate formula (Theorem 3), at an
  observed O(1/d) rate.
---

<!-- inactive-ok-file: THEORY-080 — Proposed; named for its use of the effective number of parameters, with no relation claimed -->

# NOTE-518: Exact expressions for double descent and implicit regularization via surrogate random design

## Contribution

The first exact, non-asymptotic formulas for the mean squared error of the
minimum-norm least-squares estimator across the interpolation threshold,
for general covariance. They are obtained by changing the random design
from i.i.d. rows to a determinantal point process that is analytically
tractable and asymptotically indistinguishable from i.i.d. for well-behaved
data. The second result is a clean statement of implicit regularization:
in expectation, the unregularized interpolant is the ridge solution on the
population, at a ridge fixed by the sample size.

## Key insight

When there are fewer samples than dimensions, choosing the minimum-norm
solution is not neutral. Averaged over a suitable random design, it shrinks
exactly as ridge regression does. The amount of shrinkage is the one at
which ridge regression would use n effective degrees of freedom. Double
descent is then two different estimators meeting at n = d: on one side
least squares with variance σ² tr(Σ⁻¹)(1 − βn)/(n − d), on the other an
implicit ridge with a bias term that depends on how fast Σ's spectrum
decays.

## Assumptions

- **Homoscedastic noise** (Assumption 1): ξ = y(x) − xᵀw* has mean 0 and
  variance σ². Needed for Theorem 1, not for Theorem 2.
- **General position** (Assumption 2): for n ≤ d, n i.i.d. rows have rank n
  almost surely; Σμ = E[xxᵀ] exists and is positive definite.
- **Surrogate design** (Definition 3): Det(μ, K) rescales the density of μ^K
  by pdet(XXᵀ). For n < d, K ~ Poisson(γn) restricted to ≤ d, with γn
  solving n = tr(Σμ(Σμ + I/γn)⁻¹); K = d when n = d; K ~ Poisson(γn)
  restricted to ≥ d, γn = n − d, for n > d.
- **Theorem 3** needs rows zᵀΣ^{1/2} with independent sub-Gaussian, zero
  mean, unit variance entries, CI ≽ Σ ≽ cI, ‖w*‖ ≤ C*, and n/d → c̄ ≠ 1.
- **Well-specified model.** Unlike the misspecified settings of Belkin et
  al., Hastie et al. and Mei and Montanari, the learner observes all the
  features in which the response is linear.

## Key results

- **Theorem 1 (exact MSE).** For X̄ ~ S^n_μ, MSE[X̄⁺ȳ] equals:
  σ² tr((Σ + λnI)⁻¹)·(1 − αn)/(d − n) + w*ᵀ(Σ + λnI)⁻¹w*·(d − n)/tr((Σ +
  λnI)⁻¹) for n < d; σ² tr(Σ⁻¹) for n = d; σ² tr(Σ⁻¹)·(1 − βn)/(n − d) for
  n > d. Here αn = det(Σ(Σ + λnI)⁻¹) and βn = e^{d−n}.
- **MSE decomposition (Eq. 2).** MSE = σ² E[tr((X̄ᵀX̄)⁺)] +
  w*ᵀE[I − X̄⁺X̄]w*, the variance and the projection bias. Lemma 2 gives the
  bias matrix (γnΣ + I)⁻¹, which is not known for i.i.d. designs except
  isotropic Gaussians. Lemma 3 gives the variance term.
- **Theorem 2 (implicit regularization).** E[X̄⁺ȳ] = (Σ + λnI)⁻¹vμ,y for
  n < d and Σ⁻¹vμ,y for n ≥ d, with vμ,y = E[y(x)x]. Shrinkage is linear in
  n for isotropic features and nonlinear otherwise (Figure 1b).
- **Theorem 3 (consistency).** MSE[X⁺y] − M(Σ, w*, σ², n) → 0 almost
  surely for i.i.d. sub-Gaussian designs.
- **Determinant-preserving matrices (Section 4).** Definition 4, closure
  (Lemma 4), Poisson sums (Lemma 5), and
  E[det(ABᵀ)] = e^{−E[K]} det(I + E[BᵀA]) (Lemma 6).
- **Convergence rate (Section 5).** Variance discrepancy
  |E[tr((XᵀX)⁺)]/V(Σ, n) − 1| and bias discrepancy both decay as O(1/d)
  across four eigenvalue profiles for d from 10 to 1,000 (bias to about
  100). When both are below ε, (1 − 2ε)M ≤ MSE ≤ (1 + 2ε)M.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under the surrogate design the Moore–Penrose MSE has the exact closed form of Theorem 1 | strong (theorem) | Theorem 1, Appendix C |
| C2 | For n < d the expected minimum-norm solution is the population ridge solution with n = tr(Σ(Σ + λnI)⁻¹) | strong (theorem), for the surrogate design | Theorem 2, Appendix D |
| C3 | The surrogate formulas are the i.i.d.-design MSE in the proportional limit | strong (theorem) for sub-Gaussian rows with bounded condition number | Theorem 3, Appendix E |
| C4 | The discrepancy decays as O(1/d) | weak to moderate: Monte Carlo on four spectra, stated as a conjecture | Section 5, Conjecture 1 |
| C5 | Spectral decay of Σ allows generalization below the threshold even at SNR 1 | moderate: read from the exact formula, plotted | Figures 1a, 2 |

## Method

Write the quantity of interest as an expectation under the i.i.d. design
with a Poisson number of rows, reweighted by det(XXᵀ) (or det(XᵀX) above
the threshold) and normalized (Eq. 1). Compute the normalizer and the
weighted expectations with determinant-preserving identities, which hold
because a Poisson sum of i.i.d. rank-one matrices is determinant
preserving. Choose the Poisson mean so that the expected sample size is n.

## Concepts

- **surrogate random design**: a determinantal design used in place of
  the i.i.d. one to make expectations tractable, not to promote diversity.
- **determinant preserving (d.p.)**: E[det A_{I,J}] = det E[A_{I,J}] for all
  equal-size index sets.
- **effective dimension / effective degrees of freedom**: tr(Σ(Σ + λI)⁻¹),
  as in Alaoui and Mahoney (2015).
- **implicit regularization**: here, regularization produced by selecting
  the minimum-norm solution among exact solutions, not by an inexact
  algorithm such as SGD.

## Connections

- **Belkin et al. (2019a, c)**: the double-descent observation and its
  linear model.
- **Hastie et al. (2019)**: the isotropic asymptotic comparison point.
- **Liao (acknowledged)**: the random-matrix resolvent connection, which
  Liao, Couillet and Mahoney ([LIT-679](../literature.d/LIT-679.md)) work out for random features.
- **Martin and Mahoney (2018, 2019)** are cited for empirical studies of
  implicit regularization; that is their heavy-tailed self-regularization
  work, not [LIT-672](../literature.d/LIT-672.md).
- **Kobak et al. (2018), LeJeune et al. (2019)**: the asymptotic results on
  implicit ridge closest to Theorem 2.

## Bearing on the record

- **MacKay's γ ([LIT-623](../literature.d/LIT-623.md)).** The defining equation n = Σ σi/(σi + λn) is
  MacKay's γ = Σ λa/(λa + α) with the population covariance in place of the
  data Hessian βB and λn in place of α. Theorem 2 then says that the
  minimum-norm interpolant behaves, in expectation, like the posterior mean
  under a Gaussian prior whose precision makes the number of well-determined
  parameters equal to n. MacKay's evidence maximum sets α by 2αE_W = γ, a
  different condition, so the two regularizers differ in general. The
  identification is mine, not the paper's.
- **[THEORY-080](../theory.d/THEORY-080.md)** expresses a linearized network's Occam factor through the
  NTK eigenvalues and an effective number of parameters. This paper gives
  the over-parameterized linear case an exact implicit-ridge counterpart.
- **THEORY candidate (not filed):** "For minimum-norm least squares below
  the interpolation threshold, over-parameterization acts as ridge
  regularization whose strength λn makes the ridge effective dimension
  tr(Σ(Σ + λnI)⁻¹) equal the sample size, which is the condition that
  MacKay's number of well-determined parameters, computed on the population
  covariance, equals n." Source this paper and [LIT-623](../literature.d/LIT-623.md); promote when a
  reading checks the i.i.d. case beyond Theorem 3's asymptotics, or when a
  second paper (Kobak et al., LeJeune et al.) is read.
- **Anthology.** Double descent itself is [ANTH-LIT-297](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-297.md).

## Limitations

- **The exact results are for the surrogate, not the i.i.d. design.**
  Equivalence is asymptotic (Theorem 3), with the finite-d rate only
  conjectured.
- **Linear, well-specified regression.** The paper says the implicit
  regularization result "is limited to the Moore-Penrose estimator".
- **The sample size is random** under the surrogate (Poisson with mean n),
  which a fixed-n experiment does not have.
- **Theorem 3 excludes n/d → 1**, the peak itself.

## Open questions

- Is the O(1/d) rate of Conjecture 1 provable?
- Does an analogous surrogate design give exact expressions for kernel or
  random-feature regression, connecting to Liao et al.'s deterministic
  equivalents?
- How does the implicit ridge relate to the ridge chosen by evidence
  maximization on the same data?

## Corrections

- none (there was no seed)
