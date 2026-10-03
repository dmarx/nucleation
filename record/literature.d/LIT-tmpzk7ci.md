---
status: Active
status_note: 'read 2026-10-03 ([NOTE-tmp55ipv](../notes.d/NOTE-tmp55ipv.md)); worth reading as the exact, non-asymptotic account of double descent and implicit regularization for minimum-norm least squares: replacing the i.i.d. design by a determinantal "surrogate" design gives closed-form MSE in every regime (Theorem 1) and shows that, below the interpolation threshold n < d, the expected minimum-norm solution equals the population ridge solution with the λn for which the ridge effective dimension tr(Σ(Σ + λnI)⁻¹) equals n (Theorem 2). The surrogate matches the i.i.d. design asymptotically for sub-Gaussian data (Theorem 3), at an empirically O(1/d) rate. The tool is a class of random matrices for which determinant and expectation commute.'
title: 'Exact expressions for double descent and implicit regularization via surrogate random design'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v3 (18 June 2020, 27 pages; v1 10 December 2019). The
    arXiv metadata carries no journal reference. Yang et al. (LIT-tmpf3sak)
    cite it as NeurIPS 33 (2020), which is taken as the venue. Main text
    read in full; Appendices A–E (proofs) followed in outline and Appendix
    F (experiment details) skimmed. Not held in the Anthology of the SOTA:
    a grep of its record for "1912.04533" and "surrogate random design"
    found nothing.
tags:
- learning-theory
- mathematics
- anthology-candidate
date: '2026-10-03'
published: '2019-12-10'
arxiv: '1912.04533'
first_author: 'Dereziński'
keywords:
- 'double descent'
- 'implicit regularization'
- 'minimum norm estimator'
- 'Moore-Penrose pseudoinverse'
- 'surrogate random design'
- 'determinantal point process'
- 'determinant preserving random matrices'
- 'ridge regression'
- 'effective dimension'
- 'randomized numerical linear algebra'
implementations: []
summary: >-
  Dereziński, Liang & Mahoney (2019), NeurIPS 2020. For the Moore–Penrose
  estimator X⁺y in linear regression, a determinantal surrogate design
  (density ∝ pdet(XXᵀ), Poisson sample size with mean n) gives exact MSE:
  σ² tr((Σ + λnI)⁻¹)(1 − αn)/(d − n) + w*ᵀ(Σ + λnI)⁻¹w*·(d − n)/tr((Σ +
  λnI)⁻¹) for n < d, σ² tr(Σ⁻¹) at n = d, σ² tr(Σ⁻¹)(1 − βn)/(n − d) for
  n > d, where n = tr(Σ(Σ + λnI)⁻¹). For n < d, E[X⁺y] equals the
  population ridge solution with that λn: over-parameterization is implicit
  ridge regularization whose strength makes n the effective dimension. The
  surrogate agrees with the i.i.d. design as d, n → ∞ for sub-Gaussian data.
---

# LIT-tmpzk7ci: Exact expressions for double descent and implicit regularization via surrogate random design

Michał Dereziński, Feynman Liang and Michael W. Mahoney (2019), *NeurIPS 2020* — [ARXIV-1912.04533](https://arxiv.org/abs/1912.04533)

## Key takeaways

- **Exact, finite-sample double descent** for X⁺y (Theorem 1). Under
  homoscedastic noise and general position, the surrogate-design MSE is
  given in closed form in each regime, with λn fixed by
  n = tr(Σμ(Σμ + λnI)⁻¹), αn = det(Σμ(Σμ + λnI)⁻¹) and βn = e^{d−n}. It
  peaks at n = d. With fast eigenvalue decay of Σ, the curve has a local
  optimum below the threshold, where the estimator beats the null estimator
  (Figure 1a).
- **Implicit regularization made exact** (Theorem 2). For n < d,
  E[X̄⁺ȳ] = (Σμ + λnI)⁻¹vμ,y, the global ridge solution on the population.
  The amount of implicit ℓ₂ regularization is the one for which the ridge
  effective degrees of freedom equal the sample size. This holds for any
  response, not only a linear model.
- **The surrogate is faithful** (Theorem 3). For rows zᵀΣ^{1/2} with
  sub-Gaussian z and well-conditioned Σ, the i.i.d.-design MSE minus the
  surrogate formula goes to 0 almost surely as n/d → c̄ ≠ 1. Experiments on
  four spectral decays show the discrepancy falling as O(1/d) (Figure 4,
  Conjecture 1).
- **Spectral decay changes the curve.** Varying d at fixed n (Figure 2), the
  covariance decay lets the estimator generalize below the threshold even at
  signal-to-noise 1, contrary to what the isotropic analysis of Hastie et
  al. suggests.
- **The tool.** A random matrix is determinant preserving when
  E[det A_{I,J}] = det E[A_{I,J}] for all square submatrices. The class is
  closed under independent sums and products (Lemma 4) and includes AᵀB for
  a Poisson number of i.i.d. rows (Lemma 5), which gives
  E[det(ABᵀ)] = e^{−E[K]} det(I + E[BᵀA]) (Lemma 6).

## Standing in the record

Filed on 2026-10-03 with the owner's batch ([ADR-027](../decisions.d/ADR-027.md)), as its second exact
account of double descent, beside Liao, Couillet and Mahoney
([LIT-tmpufwlh](LIT-tmpufwlh.md)). That paper is asymptotic and covers random Fourier
features; this one is non-asymptotic and covers linear regression with
arbitrary covariance. Liao is thanked here for pointing out the connection
to random-matrix resolvents. Both reduce an implicit regularization to a
self-consistent trace equation. Neither compares itself with the other, so
no relation is declared. Yang et al. ([LIT-tmpf3sak](LIT-tmpf3sak.md)) cite both for the
reading of double descent as a transition between phases. This paper
uses "phase transition" only as the name of the phenomenon, in its abstract
and introduction, and treats the threshold n = d analytically, with no
statistical-mechanics argument.

**Against the evidence framework.** λn is defined by
n = tr(Σ(Σ + λnI)⁻¹) = Σ σi/(σi + λn), over the eigenvalues σi of Σ.
That sum has the same form as MacKay's number of well-determined parameters,
γ = Σ λa/(λa + α) ([LIT-623](LIT-623.md)). So the implicit ridge of the minimum-norm
interpolant is the prior precision at which the effective number of
parameters, counted MacKay's way on the population covariance, equals the
number of samples. The paper calls the quantity the "effective dimension"
of ridge regression and does not cite MacKay. The identification is mine.
It is worth a THEORY if a reading confirms it beyond the formal match (see
the NOTE).

**Against the information-geometry line.** The quantity that sets the
implicit regularization is a regularized trace of the population
second-moment matrix, the Fisher of linear-Gaussian regression. The
spectra line (Papyan, [LIT-613](LIT-613.md), [LIT-617](LIT-617.md), [LIT-619](LIT-619.md)) measures how such spectra
look in trained classifiers; a fast decay is the regime where this paper
predicts generalization below the threshold.

**Anthology.** The double-descent curve is held there (Belkin et al.,
[ANTH-LIT-297](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-297.md)), and it is cited here as Belkin et al. (2019a, c). ML theory,
so `anthology-candidate`.
