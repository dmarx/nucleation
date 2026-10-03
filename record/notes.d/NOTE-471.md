---
number: 471
status: Read
formerly:
- NOTE-tmp1b4wr
paper: 'LIT-623'
title: 'Bayesian Interpolation'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from MacKay's posted PostScript of the Neural Computation
    paper (27 pages, manuscript pagination): §§1–7, Figures 1–8 with
    their captions, Table 1, the footnotes and the references. Text came
    from Ghostscript's text device, which loses Greek letters, so
    Equations 22–24 and the text around them were read from page images.
    Where this note cites an equation, the number is the paper's own.
    Results the paper attributes to Gull (1988, 1989a) and Skilling
    (1991) are taken as it reports them.
date: '2026-10-03'
summary: >-
  Evidence ≈ best-fit likelihood × Occam factor, the ratio of posterior to
  prior accessible parameter volume. At the evidence maximum the
  regulariser's χ² equals γ = Σ λ_a/(λ_a + α), the number of
  well-determined parameters, and the data χ² equals N − γ. Polynomials
  show an "Occam hill" in k, and the true Hermite model wins on data drawn
  from it.
---


# NOTE-471: Bayesian Interpolation

## Contribution

A review and demonstration, for the neural-network community, of the
Gull–Skilling Bayesian framework for regularisation and model comparison.
It derives the Occam factor and the number of good parameter measurements
γ. It shows that the evidence sets the regularising constant and the noise
level without test data, and ranks disparate interpolation models,
including a neural network, on the same scale. It proves that the true
model cannot be systematically beaten in expected log evidence.

## Key insight

A model that can explain more data sets must spread its predictions more
thinly. So when the data fall where a simpler model put its predictions,
the simpler model is more probable, with no penalty term added by hand. In
parameter terms, the penalty is how much of the prior's room the data
ruled out: the posterior volume over the prior volume.

## Assumptions

- **Two levels of inference**, with Bayes used at both; model invention is
  outside Bayes (Fig. 1).
- **Linear-in-parameters interpolants** y(x) = Σ w_h φ_h(x) with Gaussian
  noise of precision β and a quadratic regulariser of strength α
  (Eqs. 7–11). Then the posterior is exactly Gaussian, and the evidence for
  α, β is exact (Eqs. 16, 19–20). For nonlinear models the Gaussian
  approximation is appealed to via the central limit theorem (footnote 2).
- **A single dominant peak** of P(α, β | D), so that using the most
  probable α, β in place of integrating them out is valid (Eq. 18,
  footnote 12: valid when O(1) eigenvalues of B lie within e-fold of α̂).
- **Flat priors over log α and log β**, common to all models compared, so
  they cancel (§5).
- **No prior bias against complex models**: the paper uses the evidence's
  Occam's razor only, not a description-length prior over models.

## Key results

- **Evidence and Occam factor (Eqs. 4–6).** P(D|H) = ∫ P(D|w, H) P(w|H) dw ≈
  P(D|w_MP, H) · P(w_MP|H)(2π)^{k/2} det^{-1/2}A, with A = −∇∇ log P(w|D, H).
  For a flat prior of width σ_w and posterior width σ_{w|D}, the Occam
  factor is σ_{w|D}/σ_w.
- **Log evidence for α, β (Eq. 20).** −αE_W^MP − βE_D^MP − ½ log det A −
  log Z_W(α) − log Z_D(β) + (k/2) log 2π. The first, third and fourth
  terms make up the log Occam factor.
- **Optimum α (Eqs. 22–23).** 2αE_W = γ, with γ = k − α Trace A⁻¹ =
  Σ_a λ_a/(λ_a + α) ∈ [0, k]. Read as estimating the prior variance from γ
  effective samples: σ²_W = Σ w_i²/γ.
- **Optimum β (Eq. 24).** 2βE_D = N − γ, so χ²_D = N − γ, neither the
  discrepancy principle's N nor least squares' N − k. At the optimum,
  2M = N.
- **Error bars on α (§5).** σ²(log α) ≈ 2/γ and σ²(log β) ≈ 2/(N − γ). For
  data set X the evidence gives α a 1σ interval of [1.3, 5.0] (Fig. 5).
- **Demonstrations (Table 1, Fig. 7; data set X has N = 37).**
  - Legendre polynomials show an evidence maximum at k = 38 on X, an "Occam
    hill": steep on the left, where misfit costs ∝ N; gentle on the right,
    where Occam factors grow ∝ k log N. On the smoother set Y the maximum
    is at k = 11.
  - Radial basis functions show no Occam penalty for more basis functions,
    because a fixed kernel band-limits the interpolant. Cauchy beat
    Gaussian kernels on X (log evidence −18.9 vs −28.8).
  - Splines: the regulariser order p = 3 is most probable on X (log
    evidence −5.6), and p = 4–5 on Y.
  - Hermite functions are poor on X (−66) and best on Y (42.2), "over a
    million times more probable" than the alternatives, because Y was
    generated from a quadratic Hermite function.
  - Neural networks (preliminary, from the companion paper): 8 hidden units
    and log evidence −12.6 on X; 6 hidden units and 25.7 on Y.
- **Truth is not systematically rejected (§6).** For the true H1,
  E[log P(D|H1)/P(D|H2)] = ∫ P(D|H1) log[P(D|H1)/P(D|H2)] dD ≥ 0, by Gibbs'
  inequality. Skilling's counterexample is attributed to an atypical
  parameter draw relative to the prior (footnote 14).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The evidence factorises as best-fit likelihood times an Occam factor equal to the posterior-to-prior volume ratio | strong under the Gaussian approximation (exact for the linear models used) | Eqs. 5–6 |
| C2 | At the evidence maximum 2αE_W = γ and 2βE_D = N − γ, with γ the number of well-determined parameters | strong (derivation, exact for quadratic E_W and E_D) | Eqs. 21–24 |
| C3 | The evidence ranks models sensibly, including recovering the generating model | moderate: two one-dimensional data sets, one with a known truth | Table 1, Fig. 7 |
| C4 | In expectation under the true model, no fixed alternative has higher log evidence | strong (Gibbs' inequality) | §6 |
| C5 | Evidence and test error trend together here but need not in general, for five stated reasons | moderate: Figs. 5b and 7c–d plus argument | §6 |
| C6 | Early stopping gives qualitatively the solutions of stronger regularisation, and over-learning signals a poorly matched model | weak: a geometric argument from Fig. 6, no experiment | §6 |
| C7 | MDL offers no advantage over approximating the evidence directly | weak: an opinion, given without argument | §2 |

## Concepts

- **evidence** P(D|H): the normalising constant of the first level of
  inference, used as the likelihood of the model at the second.
- **Occam factor**: P(w_MP|H) σ_{w|D}, or its k-dimensional Gaussian form;
  the volume ratio by which a model's parameter space collapses when the
  data arrive.
- **number of good parameter measurements** γ: Σ λ_a/(λ_a + α), the
  effective number of parameters determined by the data rather than the
  prior.
- **regulariser / prior** R: the two are the same object. Different
  regularisers are different hypotheses, to be compared by evidence.

## Connections

- **Gull (1988, 1989a) and Skilling (1991)** originated the framework; the
  paper is explicitly a review of it. Jeffreys (1939) is cited for Bayesian
  model comparison and the Occam effect.
- **Schwarz's BIC and Akaike** are mentioned only in passing ("Akaike's
  criterion can be viewed as an approximation to MDL"). The paper's remark
  that log Occam factors "scale as k log N" in the polynomial family is,
  up to the constant, BIC's penalty. WBIC ([LIT-616](../literature.d/LIT-616.md)) is where the
  record holds its failure for singular models.
- **The companion paper** (MacKay 1991b, *A practical Bayesian framework for
  backprop networks*) applies the framework to neural networks. The record
  does not hold it.

## Bearing on the record

- It is the record's source for the Occam factor and for γ. With WBIC
  ([LIT-616](../literature.d/LIT-616.md)) it frames one THEORY candidate: the Bayesian complexity
  penalty is a volume ratio. In regular models it is set by the curvature
  (det A ∼ n^k) and gives (k/2) log n. In singular models it is set by the
  RLCT and gives λ log n, with λ < k/2.
- **Anthology question.** Its training-practice claims (set α by evidence,
  regularise rather than stop early) are what would put it in the
  anthology. The flag is on the LIT.

## Limitations

- **Linear, one-dimensional demonstrations.** Every model is linear in its
  parameters except the preliminary neural network, and both data sets are
  one-dimensional with N = 37 (X).
- **Gaussian approximation.** For nonlinear models with multiple or
  degenerate maxima the Occam factor formula needs correction. The paper
  mentions a degeneracy multiplier and leaves the rest to other work.
- **β fixed in the demonstrations.** The Bayesian choice of β is derived
  but not demonstrated; β is set to its true value throughout §6.
- **Evidence vs generalisation.** The paper's own §6 lists five reasons they
  can disagree. The fifth, all models being poor, is said to occur in the
  companion neural-network paper.

## Open questions

- How does the evidence relate formally to cross-validation? MacKay
  calls for this "further work". Watanabe's WAIC line of work answers part
  of it for singular models.
- How should the evidence be computed when the posterior is not
  approximately Gaussian? The paper points to sampling and leaves it there.

## Corrections

- none (there was no seed)
