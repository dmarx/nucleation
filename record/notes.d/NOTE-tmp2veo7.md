---
status: Read
paper: 'LIT-tmpmi22s'
title: 'Barnett, Barrett and Seth — Granger causality and transfer entropy are equivalent for Gaussian variables'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from arXiv 0910.4514v2 (10 Nov 2009), 10 pp.: abstract,
    the Letter's text pp. 2–8, footnotes [28]–[34] and references
    [1]–[27]. Nothing skipped. PDF from arxiv.org/pdf/0910.4514,
    extracted with pdftotext. I checked Eq. 13 from Eqs. 9 and 12 and the
    block-determinant step behind Eq. 11. I did not compare the PRL
    version, and did not read Geweke (1982), the source of Eq. 9
    (LIT-tmpj9yuo, Unavailable).
date: '2026-10-16'
summary: >-
  For jointly Gaussian stationary processes X, Y and Z, Geweke's Granger
  causality F_{Y→X|Z} = ln(|Σ(X|X⁻⊕Z⁻)|/|Σ(X|X⁻⊕Y⁻⊕Z⁻)|) equals twice
  the transfer entropy T_{Y→X|Z}, for multivariate predictor, predictee
  and conditioning variables (Eq. 13). The proof: OLS residual covariance
  is the partial covariance Σ(X|Y), and a Gaussian's conditional entropy
  is ½ln|Σ(X|Y)| + ½n ln(2πe). The authors keep G-causality apart from
  physically instantiated causation.
---

# NOTE-tmp2veo7: Barnett, Barrett and Seth — Granger causality and transfer entropy are equivalent for Gaussian variables

## Contribution

Before this Letter, Granger causality and transfer entropy were known to be
related ("predicts" against "disambiguates") but the relation had no
statement. After it, for jointly Gaussian processes, they are one quantity
up to a factor of 2, in the conditional and fully multivariate case,
provided Granger causality is taken in Geweke's generalized-variance form.
The Letter also argues that this result is a reason to prefer that form
for a multivariate predictee.

## Key insight

Least squares on Gaussian variables computes a conditional distribution.
Its residual covariance is the partial covariance, which for Gaussians is
the conditional covariance (fn. 33). Gaussian entropy is a log-determinant
of covariance. So a log ratio of residual generalized variances is a
difference of conditional entropies.

## Assumptions

- **Joint stationarity** of X_t, Y_t, Z_t (p. 4). Footnote 30 says the
  analysis carries over to the nonstationary case; that is not shown.
- **Joint Gaussianity** of every finite set of components (p. 6). This
  is the only condition the identity needs beyond invertibility.
- **Invertible covariances** Σ(Y) wherever Σ(X|Y) is formed (Eq. 1).
- **Finite lags** p, q, r in the regressions (Eqs. 6–7). Both sides are
  defined at the same lags, so the identity is lag by lag.
- **Discrete time** (fn. 29).
- **The regressions are predictive models**, not models of the
  data-generating process. The variables may depend on latent or
  exogenous variables left out of the regressions (fn. 31).

## Key results

- **Eq. 3** — for the OLS fit of X = α + Y·A + ε, Σ(ε) = Σ(X|Y). The same
  A minimizes the total variance and the generalized variance |Σ(ε)|.
- **Eq. 9** — Geweke's measure, F_{Y→X|Z} = ln(|Σ(X|X⁻⊕Z⁻)|/|Σ(X|X⁻⊕Y⁻⊕Z⁻)|),
  is nonnegative and reduces to the univariate log variance ratio
  (Eq. 8). Its estimator is asymptotically χ² under the null, citing
  Geweke and Granger (1963) and Whittle (1953). Under the alternative it
  is non-central χ², citing Geweke and Wald (1943).
- **Eq. 11** — H(X|Y) = ½ln|Σ(X|Y)| + ½n ln(2πe) for jointly Gaussian X, Y,
  from |Σ(X⊕Y)| = |Σ(Y)|·|Σ(X|Y)|. *Checked:* the block-determinant
  identity with D = Σ(Y) gives exactly this.
- **Eq. 13** — F_{Y→X|Z} = 2T_{Y→X|Z}. *Checked:* Eq. 12 is ½ times the
  log ratio in Eq. 9, and the constants ½n ln(2πe) cancel because X is
  the predictee in both terms.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For jointly Gaussian stationary processes, F_{Y→X\|Z} = 2T_{Y→X\|Z}, multivariate and conditional | strong | Eqs. 9–13; exact algebra, checked |
| C2 | OLS residual covariance equals the partial covariance, and the same coefficients minimize total and generalized variance | strong | Eqs. 2–5; standard, the second half cited to Wilks (1932) |
| C3 | Geweke's generalized-variance form is the right multivariate-predictee G-causality | weak | the equivalence offered as one further motivation (p. 5); a different form exists [16] |
| C4 | G-causality is not physically instantiated causation, which only perturbation identifies | assertion | p. 2, citing Pearl; not argued further |
| C5 | Under Gaussian assumptions there is nothing for nonlinear G-causality to add, since a stationary Gaussian AR process is linear | weak | p. 7, "preliminary work", cited to unpublished [17] |
| C6 | Outside the Gaussian case, nonzero G-causality implies nonzero transfer entropy | moderate | p. 8, cited to Marinazzo et al. (2008); not shown here |
| C7 | No general asymptotic distribution was known for transfer-entropy estimators, so significance testing is hard | weak | p. 7, "we are not aware"; Barnett and Bossomaier (2012) later give one ([NOTE-053](NOTE-053.md)) |

## Concepts

- **Partial covariance Σ(X|Y)** — Σ(X) − Σ(X,Y)Σ(Y)⁻¹Σ(X,Y)ᵀ (Eq. 1). It is
  not the conditional covariance, which is in general random, except for
  Gaussians (fn. 28, 33).
- **G-causality** — Y G-causes X given Z if adding Y's lags to a regression
  of X on its own and Z's lags reduces the prediction error (Eqs. 6–8).
- **Transfer entropy** — H(X|X⁻⊕Z⁻) − H(X|X⁻⊕Y⁻⊕Z⁻) (Eq. 10), following
  Schreiber (2000) and Kaiser and Schreiber (2002).

## Connections

- **Builds on** Wiener (1956) and Granger (1969, [LIT-tmppqyor](../literature.d/LIT-tmppqyor.md)) for the
  notion, Geweke (1982, [LIT-tmpj9yuo](../literature.d/LIT-tmpj9yuo.md)) for the multivariate measure and
  its spectral decomposition, and Schreiber (2000) for transfer entropy.
- **[LIT-048](../literature.d/LIT-048.md) (Barnett and Bossomaier 2012, [NOTE-053](NOTE-053.md)).** That Letter
  recovers this one as its linear Gaussian VAR case: T̂ is half the
  Granger statistic. [NOTE-053](NOTE-053.md)'s C7 cites this result as published; the
  reading confirms it, with the identity at the level of population
  quantities. Barnett and Bossomaier's Theorem 1b also answers this
  Letter's C7, under a well-specified parametric model.
- **[LIT-tmp7q0hf](../literature.d/LIT-tmp7q0hf.md) (Eichler and Didelez, [NOTE-tmpm48uq](NOTE-tmpm48uq.md)).** This Letter's C4
  says G-causality is not intervention causality and stops there. Eichler
  and Didelez give the conditions under which the two connect.

## Bearing on the record

- Filed as [THEORY-tmp0xaeq](../theory.d/THEORY-tmp0xaeq.md). [THEORY-641](../theory.d/THEORY-641.md) generalizes it beyond the
  Gaussian case and should name it.
- [NOTE-053](NOTE-053.md) C7 and [THEORY-641](../theory.d/THEORY-641.md)'s "recovering Barnett, Barrett and Seth"
  are correct. [NOTE-122](NOTE-122.md) relays Barrett et al.'s example that "Granger
  causality approximates transfer entropy". By this Letter it is exact
  under Gaussianity and an approximation only otherwise.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- The identity is between population quantities. In sample, agreement
  depends on the transfer-entropy estimator, which the authors say
  (p. 7). Partition estimators often fail to converge.
- Gaussianity is assumed, not tested. The authors say it is hard to check
  for highly multivariate data at limited sample sizes (p. 8).
- C5 rests on unpublished work.
- "A unified framework for data-driven causal inference" (p. 7) is the
  authors' phrase. By their own p. 2 the framework infers predictive, not
  physical, causation.

## Open questions

- How the equivalence degrades when Gaussianity fails, analytically and in
  sample (the authors' own, p. 8).
- A spectral transfer entropy built on Geweke's frequency decomposition
  (p. 7).
