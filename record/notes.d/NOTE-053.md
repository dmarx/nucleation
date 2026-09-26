---
number: 53
status: Read
formerly:
- NOTE-tmpf6wkf
paper: LIT-048
title: 'Transfer entropy as a log-likelihood ratio'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv 1205.6339v3 (27 Jul 2012), 10 pp. Main
    text pp. 1–8, Fig. 1 on p. 7, acknowledgements, references [1]–[31] on
    pp. 8–10. Nothing skipped. PDF from arxiv.org/pdf/1205.6339, extracted
    with PyMuPDF to raw4/1205.6339.txt (no pdftotext on this host). Fig. 1
    came through only as axis labels; I read its caption and the prose
    around it, not the plotted curves. I checked Eq. 25 at θ = 0.4 (0.0823
    nats, matching the caption) and the degrees-of-freedom count for the
    binary example ((a−1)a^k(b^k−1) = 2 at a = b = 2, k = 1). I did not
    compare the PRL version (Phys. Rev. Lett. 109, 138105).). Upgraded from
    `Skimmed` to `Read`: the claims table, assumptions and results are new,
    and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  For a parametric Markov model f(x_t | x^k_t, y^k_t; θ) of X, the
  likelihood-ratio estimator T̂ = −(1/(n−k)) log Λ for the null "no
  dependence on Y's past" converges almost surely to the transfer entropy
  T_{Y→X} (Theorem 1a). Under the null, 2(n−k)T̂ is asymptotically χ²(d),
  with d the difference in parameter counts (Theorem 1b). For finite-state
  chains the ordinary plug-in estimator is exactly this estimator, with d
  = (a−1)a^k(b^k−1). For a linear Gaussian VAR, T̂ is half the
  Granger-causality statistic.
---

# NOTE-053: Transfer entropy as a log-likelihood ratio

## Contribution

The Letter extends Barnett, Barrett & Seth (2009), who showed transfer entropy equals half the Granger causality for Gaussian VAR processes. The extension covers any identifiable, well-specified parametric Markov predictive model for X given the joint k-lag history. In that setting, the normalised log-likelihood ratio for the nested null "f does not depend on y^k_t" is a consistent estimator of the transfer entropy. Standard likelihood-ratio asymptotics then give it a χ² null distribution. For finite-state processes, the conventional plug-in transfer-entropy estimator is already this likelihood-ratio estimator, so it inherits a χ²((a−1)a^k(b^k−1)) null distribution with no model beyond the saturated Markov chain.

## Key insight

The average log-likelihood of a correctly specified Markov predictive model converges to minus the conditional entropy H(X_t | history) (Prop. 1). Transfer entropy is a difference of two such conditional entropies (Eq. 2). So it is the limit of a difference of two maximised average log-likelihoods, which is exactly −(1/(n−k)) log Λ. "Information transfer" in Schreiber's sense and "Granger-style predictive improvement" in the likelihood sense are one quantity. Once that is seen, the whole likelihood-ratio toolkit (χ² tests, confidence intervals, model-order selection by AIC/BIC) applies to transfer entropy.

## Assumptions

- **Joint stationarity** of (X_t, Y_t) (p. 2). The joint process is *not* required to be Markov.
- **Partial model** p(x_t | x^{t−1}, y^{t−1}; θ) = f(x_t | x^k_t, y^k_t; θ) (Eq. 3). It must be *identifiable* (θ₁ ≠ θ₂ ⇒ f(·;θ₁) ≠ f(·;θ₂)) and *well-specified*: a unique θ* with f(·;θ*) = p(x_t | x^k_t, y^k_t) (Eq. 4). So X given the joint past must be k-Markov.
- **Extended model** p(x_t, y_t | past; θ) = f(x_t | x^k_t, y^k_t; θ)·q(y_t) (Eq. 5). This is deliberately misspecified. It is harmless because q carries no θ; footnote 3 says any a.e.-positive q̃ would do. Needs q(y) ≠ 0 a.e.
- **Initial distribution** p(x^k, y^k) independent of θ (p. 3).
- **Ergodicity** of U_t = (X_{t−k}, …, X_t, Y_{t−k}, …, Y_{t−1}) (Eq. 10), so that the Birkhoff–Khinchin theorem gives Eq. 11. Finite expectations are assumed throughout.
- **Nonempty null set** Θ₀ = {θ : f does not depend on y^k_t} (Eq. 14).
- **Unstated:** the regularity conditions of Wald (1943) needed for Theorem 1b (interior true parameter, smoothness, nonsingular information). Also the uniform-convergence conditions needed to pass from Eq. 11 to Prop. 2.

## Key results

- **Prop. 1 (Eq. 12)** — ℓ̂(θ*| Xⁿ, Yⁿ) → −H(X_t | X^k_t, Y^k_t) almost surely. *Holds when:* ergodicity (10) and finite expectations.
- **Prop. 2 (Eq. 13)** — the ML estimator of the extended model satisfies θ̂ → θ* almost surely, despite the misspecification. *Argument:* Gibbs' inequality plus uniqueness of θ*.
- **Theorem 1a** — T̂_{Y→X} = −(1/(n−k)) log Λ → T_{Y→X} almost surely. The estimator is consistent but "will generally be biased".
- **Theorem 1b** — if T = 0, 2(n−k)T̂ ~ χ²(d) asymptotically, with d = (#params full) − (#params null). If T > 0, the stated distribution is non-central χ²(d; λ = 2(n−k)T). Convergence is slower than under the null.
- **Linear Gaussian VAR (p. 5)** — X_t = Σ A_i X_{t−i} + Σ B_i Y_{t−i} + ε_t with |Σ| > 0. Here the null is B₁ = … = B_k = 0, the ML is ∝ |Σ̂|^{−(n−k)/2}, and T̂ is half the Granger causality. This recovers [3].
- **Conditional TE (Eqs. 17–18)** — Theorem 1 "may be verified" to extend to T_{Y→X|Z}. This is asserted, not shown.
- **Finite state spaces (Eqs. 19–21)** — the plug-in estimator equals the model estimator, with d = (a−1)a^k(b^k−1). This scales polynomially in state-space size and exponentially in lag k.
- **Example (Eqs. 22–25, Fig. 1)** — a binary bivariate first-order chain X_t = u_t Y_{t−1} + (1−u_t)ε_t, Y_t = v_t X_{t−1} + (1−v_t)η_t with u_t ~ B(θ), v_t ~ B(φ). It has T_{Y→X} = ½(1+θ)log(1+θ) + ½(1−θ)log(1−θ), which is 0.0823 nats at θ = 0.4. Empirical CDFs come from 10⁵ realisations at n = 20, 40, 100 with φ = 0.6. They approach the χ²(2) null faster than the non-central alternative.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Average log-likelihood of the true Markov model → −(conditional entropy) | strong | Prop. 1; direct from the ergodic theorem under (10) |
| C2 | The ML estimator of the misspecified extended model is consistent for θ* | moderate | Prop. 2; informal (Gibbs + uniqueness), uniform-convergence and compactness conditions unstated |
| C3 | −(1/(n−k)) log Λ is a consistent estimator of transfer entropy | moderate | Theorem 1a; one-line derivation from C1–C2 |
| C4 | Under T = 0, 2(n−k)T̂ is asymptotically χ²(d) | moderate | Theorem 1b; cited to Wald (1943), regularity not checked; Fig. 1A toy illustration |
| C5 | Under T > 0 it is non-central χ²(d; 2(n−k)T) | weak | Theorem 1b; asserted from standard theory, and valid only as a local-alternative approximation (see corrections); Fig. 1B |
| C6 | For finite-state chains the plug-in TE estimator is exactly the LR estimator, with d = (a−1)a^k(b^k−1) | strong | Eqs. 19–21; exact algebra |
| C7 | For linear Gaussian VAR, T̂ = ½ × Granger causality | strong | p. 5; recovers the published result [3] |
| C8 | Theorem 1 extends to conditional TE | weak | assertion ("It may be verified", p. 5) |
| C9 | The result removes the need for surrogate or subsampling tests | weak | concluding assertion (p. 8); holds only asymptotically and only under the model; no finite-sample comparison is given |
| C10 | "Model transfer entropy" is the principled generalisation of Granger causality to nonlinear, GARCH or fractional-ARIMA models | weak | argument by analogy (p. 8); no such model is worked |

## Method

1. Choose a parametric predictive model f(x_t | x^k_t, y^k_t; θ) and a lag k, using the average log-likelihood (Eq. 9) with AIC/BIC (p. 3).
2. Fit by maximum likelihood over Θ (full) and over Θ₀ (no Y-dependence).
3. T̂ = [ℓ̂(θ̂) − ℓ̂(θ̂₀)], i.e. −(1/(n−k)) log Λ.
4. Test T = 0 by comparing 2(n−k)T̂ with χ²(d).

For discrete data the model is the saturated Markov chain, and steps 2–3 reduce to the plug-in estimator (Eq. 21).

## Concepts

- **Transfer entropy T_{Y→X}** — H(X_t | X^k_t) − H(X_t | X^k_t, Y^k_t) (Eq. 2), with k-lag histories. It is a conditional mutual information I(X_t ; Y^k_t | X^k_t).
- **Partial model / extended model** — the partial model specifies only X's conditional law (Eq. 3). The extended model adds an arbitrary θ-free marginal for Y_t, making the likelihood well-defined (Eq. 5).
- **Model TE estimator** — T̂ = −(1/(n−k)) log Λ (Eq. 16).
- **Plug-in estimator** — Eq. 21, empirical frequencies substituted into the conditional entropies.

## Connections

- **Builds on** Schreiber (2000) for the definition, Barnett, Barrett & Seth (2009) for the Gaussian TE–Granger equivalence, and Geweke (1982, 1984) for Granger causality and its conditional form. The χ² asymptotics come from Wald (1943). Amblard & Michel and Seghouane & Amari are cited as related work.
- **[LIT-044](../literature.d/LIT-044.md) (Stigler, read in reads/c66.md).** This letter's inferential payload is Wald (1943) [30]. Stigler describes that paper as a form of completion of Fisher's 1922 argument (asymptotic sufficiency of ML), with conditions so restrictive that they excluded even estimating a normal standard deviation (Stigler §11–12). So Theorem 1b rests on exactly the regularity conditions Stigler says have always been hard to state. Stigler's Neyman–Scott warning, that ML fails when parameters grow with n, also bears on the finite-state case. There d = (a−1)a^k(b^k−1) grows exponentially in k, and the letter's own p. 7 flags the "curse of dimensionality" if k is allowed to grow. Neither text draws this connection; it is mine.
- **[LIT-042](../literature.d/LIT-042.md) (Shannon invariants, read in reads/c35.md).** Take the sources to be the two pasts {X^k_t, Y^k_t} and the target X_t. Then T_{Y→X} = I(X_t ; Y^k_t | X^k_t) is exactly one summand, the j = Y term, of Σⱼ I(Xⱼ;Y|X₋ⱼ), the numerator of the "average degree of vulnerability" v̄ ([LIT-042](../literature.d/LIT-042.md), Prop. 2). So this letter supplies, under a parametric Markov model, a likelihood-ratio estimator with χ² asymptotics for one term of a Shannon invariant. The single-source terms I(Xᵢ;Y) of r̄ admit the same treatment. My inference is that r̄ and v̄ for time-series targets could be given model-based sampling distributions this way. Neither paper says so, and [LIT-042](../literature.d/LIT-042.md)'s networks are not Markov chains in this sense. The Shannon-invariant programme is redundancy-measure-free, and this letter is estimator-level. They meet only at the level of conditional mutual informations.
- **[LIT-025](../literature.d/LIT-025.md) (ΦID causal-emergence review, read in reads/21.md).** [LIT-025](../literature.d/LIT-025.md) says its formalism is neutral between Granger and Pearl notions of causation. This letter is the precise statement of what "Granger-sense" information flow is: transfer entropy is a predictive, log-likelihood-ratio quantity, not an interventional one. [LIT-025](../literature.d/LIT-025.md)'s decomposition of past→future information I(X_t; X_t′) would include transfer-entropy-like terms. reads/21.md does not record [LIT-025](../literature.d/LIT-025.md) stating that transfer entropy is a sum of ΦID atoms, so I leave that unverified. Seth and Barrett, Barnett's 2009 co-authors on the Gaussian equivalence [3], are among [LIT-025](../literature.d/LIT-025.md)'s authors.

## Bearing on the record

- In this record it is [LIT-048](../literature.d/LIT-048.md). Its summary is accurate. Its "What a deeper reading should check" items can be closed. The ergodicity condition is on the lagged vector U_t, not on the full process, and needs no joint Markov property. The authors flag the slow non-central convergence (p. 5), and Fig. 1B shows it only for a toy chain at n ≤ 100. The letter does not address bias beyond one sentence.
- No THEORY document in this record depends on it. If one is written on directed information in time series, this letter is the right source for "TE = LR statistic ⇒ χ² null". It should not be cited for the non-central alternative distribution or for conditional TE, which are asserted.
- **For the Anthology of the SOTA:** no instruction for ML practice. The result is classical time-series inference. It could bear on analyses of information flow between units or layers of learned systems only through a parametric model of those units, and the letter contains no such application.

## Limitations

- The model must be well-specified for X's conditional law (Eq. 4). Under misspecification of f, T̂ estimates a KL-projection quantity, not the transfer entropy. The letter does not discuss this.
- Consistency is argued informally (Prop. 2). Theorem 1b is imported, not derived, and its regularity conditions (interior θ*, smooth f, nonsingular information) are not checked for the extended model. In the finite-state case, a boundary null (e.g. a transition probability equal to 0) would break the χ² limit.
- The non-central χ² claim for T > 0 is a local-alternative approximation, not a fixed-alternative limit.
- Evidence is one toy binary chain at n ≤ 100. There is no study of continuous data, of higher lags, or of the claimed replacement of surrogate tests.
- The authors acknowledge that the curse of dimensionality in lags and states limits the discrete estimator (p. 7).

## Open questions

- Finite-sample calibration of the χ² null at realistic d, and of the non-central approximation, against surrogate-based tests. A simulation grid over (a, b, k, n) would settle it.
- Whether kernel, k-nearest-neighbour or adaptive-partition estimators can be framed parametrically so that Theorem 1 applies (raised by the authors, p. 7).
- A proof of the conditional-TE extension (Eqs. 17–18) and of the point-process extension the authors anticipate (p. 8).

## Corrections to the seeded skim

- The dossier puts the closing remarks on p. 7. The discussion of dimensionality runs over pp. 7–8, and the summary and point-process outlook are on p. 8.
- The dossier and [LIT-048](../literature.d/LIT-048.md) say the paper establishes the χ² distribution. The letter proves Theorem 1a in one line ("follows immediately from Propositions 1, 2"). Theorem 1b is not proved at all: it "follows from the standard large-sample theory [30]" (Wald 1943). Proposition 2 (consistency of θ̂ under the misspecified extended model) is argued from Gibbs' inequality plus uniqueness of θ* alone. It omits the compactness or uniform-convergence conditions that a consistency proof for a maximiser normally needs. The consistency claim should be read as an informal argument under unstated regularity.
- The dossier does not say this: the non-central χ²(d; λ = 2(n−k)T) statement for T > 0 cannot be a fixed-alternative limit, because λ grows with n. In Wald's theory a non-central χ² limit holds under local alternatives that shrink like n^{-1/2}. For fixed T > 0 the statistic is asymptotically normal. So the statement is an approximation, not a limit theorem. This is my reading of standard theory, not something the letter discusses. The authors say only that convergence to the non-central χ² "will generally be slower" (p. 5), which Fig. 1B illustrates.
- The dossier suggests checking "the later literature on transfer-entropy estimator bias". The letter contains nothing on this beyond the remark that the estimator "will generally be biased" (p. 5).
- A precision the dossier omits: for finite state spaces the result is an exact identity, not an approximation. The plug-in estimator Eq. 21 is the likelihood-ratio estimator Eq. 16, because the transition probabilities are the parameters and their ML estimates are the empirical conditionals (p. 6).
