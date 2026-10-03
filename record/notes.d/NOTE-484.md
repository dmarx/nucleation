---
number: 484
status: Read
formerly:
- NOTE-tmpvg9nc
paper: 'LIT-609'
title: 'Bayesian hypothesis testing for psychologists: A tutorial on the Savage–Dickey method'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the publisher-typeset PDF in KU Leuven's Lirias
    repository (32 pages, printed pp. 158–189): §§1–9, Appendix A (the
    derivation) and Appendix B (WinBUGS code). Figures were read from
    their captions and the text. The online R code was not fetched or
    run. Results the paper takes from Dickey & Lientz (1970), Dickey
    (1971), O'Hagan & Forster (2004) and Consonni & Veronese (2008) are
    taken as it reports them.
date: '2026-10-03'
summary: >-
  For nested models the Bayes factor for a point null is the ratio of
  posterior to prior density of the tested parameter at the null value,
  under the larger model (Eq. 12, derived in Appendix A). It needs the
  nuisance parameters' prior to be continuous at the null. Worked
  examples give BF10 ≈ 2.2 where p ≈ .006, and BF01 ≈ 4 in favour of a
  null of no group difference.
---

# NOTE-484: Bayesian hypothesis testing for psychologists: A tutorial on the Savage–Dickey method

## Contribution

The paper brings the Savage–Dickey density ratio to experimental
psychologists as a practical way to compute Bayes factors for nested models.
It turns it into an MCMC procedure: sample the larger model's prior and
posterior, estimate both densities at the null value with a logspline
estimator, and divide. It shows the procedure on three real data sets,
including hierarchical one- and two-sample t-tests with order restrictions.

## Key insight

Testing whether a parameter equals a particular value does not require
fitting the model in which it does. Fit only the model in which it is free,
and ask how much the data changed the plausibility of that one value. If the
posterior density there is lower than the prior density, the data have
counted against the null by exactly that factor. The prior on the tested
parameter is therefore not a harmless choice: its height at the null value
is half of the answer.

## Assumptions

- **Nesting.** H0: φ = φ0 is H1 with φ fixed; θ = (φ, ψ), ψ the nuisance
  parameters (p. 169–170).
- **Continuity of the nuisance prior** (Appendix A):
  lim_{φ→φ0} p1(ψ | φ) = p0(ψ), so p1(ψ | φ = φ0) = p0(ψ). The authors note
  that some regard even this as too strict (Consonni & Veronese 2008).
- **Converged MCMC** and a reliable one-dimensional density estimate at φ0
  (the R package polspline's logspline estimator).
- **Priors in the examples:** uniform Beta(1, 1) on rates; a standard Normal
  "unit information" prior on effect size δ; uniform (0, 10) on standard
  deviations; a truncated standard Normal on a probit group mean.

## Key results

- **Bayes factor as an evidence ratio (Eqs. 6–8).** The posterior odds are
  the prior odds times p(D | M1)/p(D | M2). The marginal likelihood averages
  the likelihood over the prior. In the binomial example BF12 ≈ 0.107, so
  the data are about 9.3 times likelier under "not guessing".
- **Savage–Dickey (Eq. 12; Appendix A, Eqs. 16–19).** Under the continuity
  condition, p0(D) = p1(D | φ = φ0). Bayes' rule then gives
  p0(D) = p1(φ = φ0 | D) p1(D) / p1(φ = φ0), and so
  BF01 = p1(φ = φ0 | D) / p1(φ = φ0).
- **Example 1, equality of proportions.** Condom use at first sex: 424 of
  777 pledgers against 5,416 of 9,072 non-pledgers. A frequentist test gives
  p ≈ .006. The analytic Bayes factor (Eq. 15) gives BF01 ≈ 0.45, so BF10 ≈
  2.22. The MCMC Savage–Dickey estimate is BF10 = 2.17. With the order
  restriction δ < 0, BF20 ≈ 3.78 by logspline and ≈ 4.34 by renormalising.
  The unrestricted result bounds the restricted one at 2.22 × 2 = 4.44.
- **Example 2, hierarchical one-sample t-test** (Zeelenberg et al.,
  74 participants; reported t(73) = 2.19, p < .05). With effect size
  δ = μα/σα, a standard Normal prior truncated to δ > 0, BF01 ≈ 0.22, about
  4.49 times more likely under the alternative.
- **Example 3, hierarchical two-sample t-test** (Geurts et al., 26 controls
  and 52 children with ADHD on the WCST; t(40.2) = 0.37, p = .72).
  BF01 = 3.96 unrestricted and BF02 = 4.94 for δ > 0, which is evidence for
  the null that a p-value cannot give.
- **Three regimes for order restrictions (§5.2).** When the posterior agrees
  with the restriction, the evidence against H0 at most doubles. When the
  posterior is symmetric about φ0, nothing changes. When the posterior
  contradicts the restriction, the evidence for H0 grows sharply (≈ 78 in
  the reversed pledger test).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For nested models with a nuisance prior continuous at φ0, BF01 equals the posterior-to-prior density ratio of φ at φ0 under H1 | strong (derivation) | Appendix A, Eqs. 16–19 |
| C2 | The Bayes factor is sensitive to the prior on the tested parameter in proportion to the prior's height at φ0, and insensitive to vague priors on shared nuisance parameters | strong for the ratio's form; the nuisance claim rests on the continuity condition | Eq. 12, §3 points 1–2 |
| C3 | The MCMC Savage–Dickey estimate agrees with the analytic Bayes factor where one exists | moderate: one example | Example 1, 2.17 vs 2.22 |
| C4 | An order restriction that the posterior already satisfies can at most double the Bayes factor against a point null | strong (follows from truncation doubling the prior ordinate) | §5.2 |
| C5 | Bayes factors are more conservative than p-values in these data and can support the null | moderate: three examples | Examples 1–3 |
| C6 | The Savage–Dickey test depends on parameterisation through the Borel–Kolmogorov paradox | stated, not shown | §8 point 5, citing Consonni & Veronese 2008 |

## Concepts

- **Bayes factor**: the ratio of marginal likelihoods p(D | H0)/p(D | H1),
  read as the weight of evidence (Jeffreys; Good).
- **Savage–Dickey density ratio**: posterior ordinate over prior ordinate of
  the tested parameter at the null value, under the encompassing model.
- **automatic Ockham's razor**: the Bayes factor's penalty on models that
  spread prior mass over values the data make unlikely (§2.2.1, citing
  MacKay 2003, ch. 28).
- **encompassing prior approach**: the Hoijtink–Klugkist framework of which,
  per Appendix A, Savage–Dickey is the "exact equality" special case.

## Connections

- **Dickey (1971) ([LIT-610](../literature.d/LIT-610.md)).** The paper names its source chain:
  Dickey & Lientz (1970) first published the result and attributed it to
  Savage, and Dickey (1971) is cited for the name. The record has since
  read Dickey 1971 ([NOTE-508](NOTE-508.md)), and this account matches it: Dickey
  calls the result "Savage's Density Ratio", credits the proof to Dickey
  and Lientz, and states it for any continuous likelihood. The continuity
  condition of Appendix A is his condition (3.8), which he too writes as a
  limit when he applies it.
- **Verdinelli & Wasserman (1995)** is cited as a generalisation for when
  the continuity condition fails. The record does not hold it. Friston &
  Penny ([LIT-620](../literature.d/LIT-620.md)) cite it too.
- **Friston & Penny ([LIT-620](../literature.d/LIT-620.md)) and Bayesian model reduction
  ([LIT-614](../literature.d/LIT-614.md)).** Their Eq. 6 is this paper's Eq. 12, derived as the
  point-mass case of a reduced-prior evidence identity. The two literatures
  do not cite each other.

## Bearing on the record

- It supplies the record's statement of the Savage–Dickey ratio and the
  condition it needs, so that the Friston line of work ([LIT-620](../literature.d/LIT-620.md),
  [LIT-614](../literature.d/LIT-614.md), [LIT-615](../literature.d/LIT-615.md)) can be read as a generalisation of something
  the record already holds and does not have to be taken on its own
  terms.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **Point nulls and nesting only.** The method needs one model to be a
  special case of the other.
- **Tail estimates.** When φ0 lies far in the posterior tail, the density
  estimate rests on few samples. The authors argue the qualitative
  conclusion is still safe there, even if the number is not.
- **Prior choice for the tested parameter** is sidestepped by working with
  rates and standardised effect sizes. The authors admit this, and their
  "unit information" prior is a default, not a derivation.
- **Borel–Kolmogorov.** The authors give no resolution, and say none of the
  alternatives they know of is free of its own drawbacks.

## Open questions

- How much does a Savage–Dickey Bayes factor change under a
  reparameterisation of the tested parameter, in the models psychologists
  actually use? The paper says the effect exists and does not measure it.
- How does it relate to the reduced-prior identity of Friston & Penny
  outside the point-mass case? That paper answers it, from the other
  direction.

## Corrections

- none (there was no seed)
