---
status: Read
paper: 'LIT-tmpuhjzx'
title: 'Post hoc Bayesian model selection'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the PMC author manuscript (Europe PMC full-text
    XML): abstract, introduction, theory, the three examples, the
    conclusion, Table 1 and the software appendix. Equations arrived as
    linearised MathML. Eqs. 3–6 read unambiguously; Eq. 9 was
    reconstructed from that form and checked against its restatement in
    LIT-tmpbgf7s (Eq. 11 and the Gaussian row of Table 1). Figures were
    read from their captions and the text. The SPM routines were not run.
date: '2026-10-03'
summary: >-
  Models that differ only in their priors can be scored from one fitted
  full model: reduced evidence is full evidence times the posterior
  expectation of the prior ratio. Savage–Dickey is the point-mass case,
  ARD the continuous one. Under Laplace the reduced free energy is
  closed-form. Simulations recover a sparse regression (4,096 models)
  and a three-edge brain network (64 models).
---

<!-- inactive-ok-file: LIT-tmp6vz5e — Deferred: Dickey 1971 is unread; named as the source this paper cites for the ratio its Eq. 6 recovers -->

# NOTE-tmpy47cf: Post hoc Bayesian model selection

## Contribution

The paper shows that, after fitting one full model, one can compute the
evidence and posterior of any model formed by changing its priors without
fitting that model. Under the Gaussian (variational Laplace) assumption
the computation is a few matrix operations, so thousands to millions of
models can be scored after one inversion. It also argues that model
selection, automatic relevance determination and empirical Bayes are one
procedure: maximising evidence over the hyperparameters of the prior.

## Key insight

If removing a parameter is expressed as giving it a prior of zero
variance, then every "smaller model" is the same model with a different
prior. Bayes' rule applied to two models with the same likelihood and
different priors makes the likelihoods cancel, so the full model's
posterior already says how much evidence any narrower prior would have
had. Fit once; ask afterwards.

## Assumptions

- **Shared likelihood, nested priors** (Eq. 2): p(y | θ, m_i) = p(y | θ, m_F)
  for every reduced model, and the support of each reduced prior lies inside
  the full prior's support, Ω_i ⊂ Ω_F, so that the density ratios exist.
  Every model has the same number of parameters. Models differ only in
  whether their priors let some parameters take nontrivial values.
- **Laplace (Gaussian) forms** for prior and approximate posterior, needed
  for the closed form of Eq. 9 and not for the general identity of Eq. 3.
- **The approximate posterior is good.** The scheme takes the full model's
  free energy F_F ≈ ln p(y | m_F) and q(θ | m_F) ≈ p(θ | y, m_F) as given.
  The authors flag that for strongly nonlinear models neither is
  established.

## Key results

- **Eq. 3 (reduced evidence).** p(y|m_i) = p(y|m_F) ∫ p(θ|y, m_F)
  p(θ|m_i)/p(θ|m_F) dθ. The reduced evidence is the full evidence times the
  full posterior expectation of the prior density ratio.
- **Eq. 5 (marginal form).** With θ = {θ_i, θ_\i} and the prior unchanged on
  θ_\i, the Bayes factor p(y|m_i)/p(y|m_F) needs only the marginal posterior
  over θ_i. The same point is used later to argue that a mean-field
  factorisation does not confound optimising priors on one factor.
- **Eq. 6 (Savage–Dickey).** For a point-mass reduced prior δ(θ_i),
  p(y|m_i)/p(y|m_F) = p(θ_i = θ̂_i | y, m_F)/p(θ_i = θ̂_i | m_F).
- **Eq. 7 (free energy).** F = ln p(y|m) − D(q ∥ p(θ|y, m)) = E_q[ln p(y|θ, m)]
  − D(q ∥ p(θ|m)): accuracy minus complexity.
- **Eq. 9 (Laplace).** With prior N(η, Π⁻¹) and posterior N(μ, P⁻¹) (C =
  P⁻¹): P_i = P_F + Π_i − Π_F; μ_i = C_i(P_Fμ_F + Π_iη_i − Π_Fη_F); F_i =
  ½ ln|Π_i P_F P_i⁻¹ Π_F⁻¹| − ½(μ_FᵀP_Fμ_F + η_iᵀΠ_iη_i − η_FᵀΠ_Fη_F −
  μ_iᵀP_iμ_i) + F_F. A log Bayes factor F_i − F_j above 3 (odds about 20:1)
  is the conventional threshold the paper uses.
- **Example 1 (prior optimisation, Fig. 1).** A linear model with 64
  observations, 4 regressors and two noise log-precisions (true values 2 and
  1). The evidence over the prior mean and variance of the log-precisions
  peaks at a mean just below 2 and a variance near a quarter. The optimised
  prior shrinks the posterior towards the true value. Without a constraint
  tying the two log-precisions, the optimal prior collapses to a point mass
  at the ML value (results not shown).
- **Example 2 (model selection, Figs. 2–3).** 16 observations, 4 true and 8
  irrelevant regressors, prior variances switched between 0 and 8: 2¹² =
  4,096 models scored "in under a second". The true model was selected with
  posterior probability above 50%. As prior variance goes to zero the
  evidence has an interior maximum for relevant parameters and keeps rising
  for irrelevant ones, which is why optimisation behaves like thresholding
  (ARD).
- **Example 3 (network discovery, Figs. 4–6).** A nonlinear hemodynamic
  state-space model of four regions, three true bidirectional connections,
  256 time bins, inverted once by Generalized Filtering. Of 64 models (with
  connections forced to be reciprocal) the true one was selected with
  nearly 100% posterior probability. Optimising each connection's prior
  variance separately, with no reciprocity constraint, drove absent
  connections' variances to zero and recovered the reciprocal structure.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The evidence and posterior of any model that differs from a full model only in its prior follow from the full model's evidence and posterior | strong (derivation from Bayes' rule) | Eqs. 3–5 |
| C2 | The Savage–Dickey density ratio is the point-mass special case | strong (derivation) | Eq. 6 |
| C3 | Under Gaussian prior and posterior the reduced free energy and posterior are closed-form | strong (derivation); the PMC rendering of Eq. 9 was reconstructed | Eq. 9 |
| C4 | Model selection, ARD, empirical Bayes, ReML, MAP and ML are all evidence maximisation over prior hyperparameters | moderate: a formal recasting, Table 1; "in principle", not implemented for each | Eqs. 13–15, Table 1 |
| C5 | Post hoc selection recovers true sparse structure in linear and nonlinear dynamic models | weak to moderate: one simulation each, generated from the model class itself | Figs. 2, 5, 6 |
| C6 | The reduced free energy is a reasonable proxy for the free energy of the reduced model in weakly nonlinear models | weak: the authors' "early impressions", sampling checks in progress | Conclusion |

## Concepts

- **full / reduced model**: models sharing a likelihood, the reduced ones
  with priors whose support lies inside the full prior's.
- **reduced free energy**: the free energy of a reduced model computed from
  the full model's posterior and priors (Eq. 9), not by inverting the
  reduced model.
- **automatic model selection (AMS)**: hyperparameters λ ∈ {0, 1} switching
  prior variances on or off (Table 1).
- **automatic relevance determination (ARD)**: continuous optimisation of
  per-parameter shrinkage-prior variances (Table 1).
- **greedy search**: for large model spaces, search over the 8 parameters
  whose removal costs least evidence, remove, and repeat (Conclusion; the
  spm_dcm_post_hoc appendix).

## Connections

- **Dickey (1971) ([LIT-tmp6vz5e](../literature.d/LIT-tmp6vz5e.md))** and Verdinelli & Wasserman (1995) are the
  cited sources of the ratio that Eq. 6 recovers. The record's reading of
  that ratio is Wagenmakers et al. ([LIT-tmp2suxj](../literature.d/LIT-tmp2suxj.md)). This paper does not cite
  Wagenmakers et al.
- **Bayesian model reduction ([LIT-tmpbgf7s](../literature.d/LIT-tmpbgf7s.md))** restates Eqs. 3, 4 and 9 and
  adds the Dirichlet, beta, gamma and multinomial forms.
- **MacKay ([LIT-tmpx82v3](../literature.d/LIT-tmpx82v3.md)).** The paper cites MacKay & Takeuchi (1996) for
  ARD, not the 1992 evidence paper. The record's MacKay reading supplies
  the Occam factor, the complexity term that Eq. 7's KL divergence
  generalises.

## Bearing on the record

- It is the formal source for any THEORY the record files on structure
  learning by evidence: one fit, then pruning by reduced evidence.
- Its free energy is variational, which agrees with what the record's
  reading of [LIT-526](../literature.d/LIT-526.md) ([NOTE-421](NOTE-421.md)) says about Friston's use of the term.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **Laplace.** For strongly nonlinear models the posterior is not Gaussian,
  the free energy only bounds the log evidence, and the authors do not
  know whether the reduced free energy approximates the free energy of the
  reduced model. They conjecture it may be the better proxy, and leave the
  sampling checks to future work.
- **Model space.** The method scores a space; it does not define one.
  Models that are not reduced forms of the full model cannot be compared,
  and large spaces still need a greedy search (an eight-node DCM has
  2^(8×8) ≈ 1.84 × 10¹⁹ configurations, by the paper's count).
- **Evidence for the examples** is simulation from the same model class, so
  recovery of the generating structure is close to a consistency check.

## Open questions

- When does the reduced free energy disagree with the free energy of the
  reduced model, and which is closer to the true log evidence? The paper
  names the question and proposes Gibbs sampling to answer it.
- What hyperparameterisation of the prior is the right constraint? Without
  one, the optimum is maximum likelihood, so everything depends on a
  hierarchical choice the paper does not derive.

## Corrections

- none (there was no seed)
