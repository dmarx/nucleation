---
status: Read
paper: LIT-tmpporrt
title: 'Williamson, Orbanz and Ghahramani — Dependent Indian buffet processes'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full from PMLR's own PDF
    (https://proceedings.mlr.press/v9/williamson10a/williamson10a.pdf, the
    typeset AISTATS 2010 paper, eight pages), text extracted with
    pdftotext. Read: §§1–6, Appendix A, Table 1 and the figure captions;
    the figures themselves only through their captions and the text. The
    marginal of the whole matrix at one covariate value, and the
    persistence numbers, are the record's derivations and simulations, not
    the paper's.
date: '2026-10-26'
summary: >-
  Couples IBPs over a covariate by thresholding Gaussian processes:
  z_nk(t) = 1 when h_nk(t) falls below the b_k quantile of its marginal,
  with stick-breaking sticks b_k that do not depend on t. Each item's
  indicator is then Bernoulli(b_k) at every t, so prevalence is fixed and
  persistence is set apart from it by the GP covariance. The paper says
  Z(t) is IBP-distributed at each t; that holds exactly in its collapsed
  model, while with a shared feature-level GP the items at one t are
  correlated and fewer features are occupied. Truncated Gibbs with HMC;
  lower held-out RMSE than the IBP on two datasets.
---
<!-- inactive-ok-file: CASE-tmplcm41 — Proposed; the construction this reading is the comparator for, filed from the same exchange, cited as open -->

# NOTE-tmpcg7gu: Williamson, Orbanz and Ghahramani — Dependent Indian buffet processes

## Contribution

It does for the IBP what MacEachern's dependent Dirichlet process did for
mixtures: one binary feature matrix Z(t) for each value t of a covariate
(time, space, GDP), with each feature's column evolving over t. Because
the IBP's entries are binary, the DDP device of replacing parameters by GP
draws does not carry over directly. The paper instead writes each
Bernoulli as a thresholded Gaussian and lets the Gaussians be GP
marginals.

## Key insight

A Bernoulli(β) variable is I{u < F⁻¹(β)} for a Gaussian u with CDF F. If u
is a Gaussian process in t, the threshold fixes the probability at every t
while the process's covariance decides how the indicator moves over t.
Prevalence and persistence become separate dials: the stick bk sets how
common feature k is, and the covariance sets how long it stays where it
is.

## Assumptions

- Sticks by stick-breaking (Teh et al. 2007): vj ~ Beta(α, 1),
  bk = ∏_{j≤k} vj (1). They do not depend on t.
- Hierarchical model (4): gk ~ GP(0, Σk), hnk ~ GP(gk, Γnk),
  znk(t) = I{hnk(t) < F⁻¹(bk | 0, Σk(t,t) + Γnk(t,t))}.
- Exchangeable "bag of items" model: Γnk = ρ²I, independent of n.
- Collapsed model (5): Σk = 0, so hnk ~ GP(0, Γnk) and the threshold is
  F⁻¹(bk | 0, Γnk(t,t)).
- Inference: features truncated at K (20 and 50 in the experiments),
  Gibbs on znk through truncated Gaussians for hnk, Metropolis–Hastings
  for bk and α, hybrid Monte Carlo for the GP length scales. Squared
  exponential Σk with one length scale per feature.
- Likelihood in all experiments: linear Gaussian, X(t) = Z(t)A + noise.

## Key results

- **Three regimes (§3).**
  - *Hierarchical*: Σk a shared per-feature profile over t, Γnk item
    variation. Item n at t1 must correspond to item n at t2.
  - *Exchangeable*: Γnk = ρ²I. The paper: "For each t, the marginal
    distribution of Z(t) is an IBP, and IBP matrices have exchangeable
    rows", and rows at different t need not correspond, so N(t) may vary
    (journal issues as bags of articles).
  - *Collapsed*: Σk = 0. Each item's feature follows its own GP; items are
    coupled only through bk. Suggested for "the tracking of patients over
    time in a longitudinal study".
- **Footnote 1.** Against Van Gael et al.'s Markov IBP: the dIBP "allows
  dependence on arbitrary, possibly vector-valued, covariates, does not
  have Markov and time-invariance restrictions, and has IBP marginals at
  any covariate value."
- **Full conditionals (6)–(7), Appendix A.** Given gk(t), znk(t) is
  Bernoulli(γk(t)), with γk(t) = F(F⁻¹(bk | 0, Σk(t,t) + ρ²) − gk(t) | 0, ρ²).
- **Synthetic (§5.1).** Hierarchical: eight 8×8 image features, GP
  (Matérn) probabilities through a sigmoid over 40 steps; the posterior
  probabilities "capture the shape, but not the scale" of the true ones.
  Collapsed: one item over 100 steps, data generated not from the dIBP
  but from a Markov chain with per-feature transition probabilities
  qk ~ Beta(1, 10) and an IBP start; recovery of Z(t) is "almost perfect"
  (Fig. 3, one sample).
- **Real data (§5.2, Table 1).** Held-out RMSE, IBP against dIBP, both
  truncated at 50, linear Gaussian:
  - piano audio, 161 spectral features, 120 consecutive frames, ten random
    folds, time as covariate: 1.08 ± 0.06 against 0.69 ± 0.04;
  - UN development indicators, 13 for 144 countries, GDP as covariate,
    130/14 split, ten folds: 0.93 ± 0.06 against 0.79 ± 0.07, lower "on
    each of the ten folds".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Each item's indicator znk(t) is marginally Bernoulli(bk) at every t, in all three regimes | strong | the threshold construction (3)–(4); re-derived in [THEORY-tmpumk4q](../theory.d/THEORY-tmpumk4q.md) |
| C2 | In the exchangeable regime the whole matrix Z(t) is IBP-distributed at each t | holds only for the collapsed regime | asserted in §3 and footnote 1; the record's derivation and simulation ([THEORY-tmpumk4q](../theory.d/THEORY-tmpumk4q.md)) find it fails when Σk(t,t) > 0 |
| C3 | The choice of covariance sets the dependence and exchangeability structure | strong as a description | §3 |
| C4 | Modelling covariate dependence lowers prediction error | moderate | two datasets, ten folds each; no significance test though the text says "significantly" |
| C5 | Truncated Gibbs with HMC is a workable inference scheme | moderate | the experiments; no mixing diagnostics reported |

## Concepts

- **Dependent IBP (dIBP)**: a family {Z(t), t ∈ T} of binary matrices with
  unboundedly many columns, column k of every Z(t) coupled through a GP.
- **Stick length bk**: the prevalence of feature k, shared across t.
- **Bag of items**: rows exchangeable at each t, with no correspondence
  between rows at different t.
- **Collapsed model**: the Σk = 0 limit, in which each item's feature
  path is its own GP thresholded at bk.

## Connections

It extends the IBP ([LIT-tmpxrrf9](../literature.d/LIT-tmpxrrf9.md)) through Teh et al.'s stick-breaking
construction, MacEachern's DDP and Duan et al.'s and Sudderth and Jordan's
thresholded-Gaussian device, and positions itself against the Markov IBP
of Van Gael et al. (2009), not registered. It names "dependent beta
processes" ([LIT-tmpday8e](../literature.d/LIT-tmpday8e.md)'s measure) as an alternative left for future
work.

## Bearing on the record

- **[CASE-tmplcm41](../cases.d/CASE-tmplcm41.md), the comparator.** T23 says its model "is not
  automatically the exact dependent IBP of Williamson, Orbanz, and
  Ghahramani, whose construction uses covariate-dependent Gaussian
  processes". That is accurate. [LIT-tmpporrt](../literature.d/LIT-tmpporrt.md)'s own entry said the dIBP is
  the model "in which the feature allocation stays IBP-distributed at every
  covariate value"; the reading narrows that to the collapsed model, which
  is the one that fits members tracked over days.
- **[CASE-tmplcm41](../cases.d/CASE-tmplcm41.md), item 2.** The construction removes the second half of
  the case's finding. In T23's transition the stationary prevalence
  drifts from πk (0.36 against 0.2 at ρ = 2). In the dIBP every item's
  marginal is bk at every t by construction, whatever the persistence.
  The first half survives in another form. For a stationary GP whose
  values at t and t + 1 have correlation r, a held feature is kept with
  probability Φ₂(c, c; r)/bk, c = Φ⁻¹(bk), and for fixed r that still
  falls with prevalence: at r = 0.9 it is 0.59 for bk = 0.025 and 0.75 for
  bk = 0.2 (re-computed here, exact bivariate normal). The paper's
  per-feature length scales are what allow persistence to be set per
  feature. So the dIBP answers the case's "one ρ cannot do that" with a
  persistence parameter per feature.
- **[CASE-tmplcm41](../cases.d/CASE-tmplcm41.md), item 1.** The paper truncates by stick-breaking (at 20
  and 50), the construction [THEORY-tmppc921](../theory.d/THEORY-tmppc921.md) shows is close to the IBP at
  small K.
- **[QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md).** It is the established way to let latent features
  of members appear, fade and return over time without fixing their
  number. It does not make features depend on one another or on the
  members' interactions, which T23's social and team terms try to add.
- **[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md).** T24's port needs a prior over B_s across
  checkpoints. The collapsed dIBP is a candidate whose marginal at every
  checkpoint is an IBP; it does not condition on θ_s, which avoids the
  first gap the case records for T24, and it still treats components as
  exchangeable, which leaves the second.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **The matrix marginal.** The claim that Z(t) is an IBP at each t holds
  per item in every regime, but for the whole matrix only when Σk(t,t) =
  0. With a shared gk(t), the items at a given t are conditionally
  Bernoulli(γk(t)) with γk(t) random about bk, so they are positively
  correlated and fewer features are occupied. In the record's simulation,
  N = 12, α = 3, ρ² = 1, 40,000 draws: E[K+] = 9.34 with Σk(t,t) = 0
  (IBP: 9.31), 7.06 with Σk(t,t) = 1 and 5.35 with Σk(t,t) = 4, while
  each row still holds 3.0 features on average.
- **No dependence between features, and no dependence on other items.**
  Columns are independent given the sticks.
- **Fixed prevalence.** bk does not vary with t, so a feature's overall
  rate can change over t only through gk in the hierarchical regime.
- **Thin evidence.** Synthetic recovery is shown by one posterior sample;
  the collapsed experiment has one item. The real-data comparison is with
  the plain IBP only, not with the Markov IBP or any other dependent
  model, and "significantly" has no test behind it.
- **Approximate inference.** Truncated Gibbs; the paper names slice
  sampling as the exact alternative and does not use it.

## Open questions

- What is the law of Z(t) in the hierarchical regime? It is exchangeable
  in the rows, with column probabilities γk(t) that are not stick-breaking
  distributed; a closed form would say how far from an IBP it is.
- Can features in a dIBP be made to depend on one another or on a network
  of items while keeping IBP marginals, which is what an organizational
  model would need?
