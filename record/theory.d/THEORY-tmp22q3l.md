---
status: Proposed
promote_when: >-
  A direct comparison on a singular model whose RLCTs are known. Take
  the reduced-rank regression of LIT-tmpmsuf3 §6 (M = N = 6, true rank 3),
  where every lower rank is a reduction of the rank-6 model by zero-variance
  priors on columns of B and rows of A. Fit the rank-6 model once by
  variational Laplace and score ranks 1–6 by Laplace BMR (LIT-tmpuhjzx,
  Eq. 9). Compute each rank's free energy independently of the Laplace
  approximation, by thermodynamic integration over all temperatures or by
  WBIC, over a range of n spanning at least two decades. The account is
  promoted if the BMR differences between ranks depart from the
  independent ones by an amount that grows linearly in log n. It is
  refuted if the discrepancy stays bounded as n grows. A Gaussian mixture
  with redundant components would be a second case. What cannot settle it:
  BMR recovering the generating structure in simulation, since a score
  wrong by a log n term can still rank the true model first; agreement
  between Laplace BMR and Laplace re-fits of the reduced models, which
  share the approximation; and the Dirichlet reductions of LIT-tmpesz2r,
  which rest on a mean-field approximation, not on Laplace.
title: 'Bayesian model reduction under the Laplace approximation prices the reductions of a singular parent model with a Gaussian Occam factor, so its free-energy differences can be wrong by a term that grows with log n'
version: 1
tags:
- model-comparison
- probabilistic-modeling
- learning-theory
date: '2026-10-03'
source:
- LIT-tmpmsuf3
- LIT-tmpuhjzx
- LIT-tmpbgf7s
extends:
- THEORY-tmpzelk0
summary: >-
  The filer's synthesis, stated by no source. BMR's closed form (Friston &
  Penny, [LIT-tmpuhjzx](../literature.d/LIT-tmpuhjzx.md), Eq. 9; Friston, Parr & Zeidman, [LIT-tmpbgf7s](../literature.d/LIT-tmpbgf7s.md),
  Eq. 11) charges a reduction through log-determinants of Gaussian
  precisions, which is MacKay's regular Occam factor. Watanabe,
  [LIT-tmpmsuf3](../literature.d/LIT-tmpmsuf3.md), says that models with hierarchical layers or hidden
  variables are singular, that no normal distribution approximates their
  posterior, and that their free energy grows as λ log n. BMR is applied to
  exactly such models: mixtures, hierarchical empirical Bayes and latent
  states. Neither literature cites the other. The exact identity is
  untouched ([THEORY-tmp9y0ia](THEORY-tmp9y0ia.md)). The claim is about its Laplace form, and a
  test on reduced-rank regression would settle it.
---
<!-- inactive-ok-file: THEORY-tmpzelk0 — Proposed; this account extends its singular half and is no firmer than it -->

# THEORY-tmp22q3l: Bayesian model reduction under the Laplace approximation prices the reductions of a singular parent model with a Gaussian Occam factor, so its free-energy differences can be wrong by a term that grows with log n

## Source

- Watanabe (2012; JMLR 2013), [LIT-tmpmsuf3](../literature.d/LIT-tmpmsuf3.md), read in [NOTE-tmp3drtl](../notes.d/NOTE-tmp3drtl.md): the
  definition of singular models (Eq. 14 and §1), the RLCT as a minimum
  over charts (Eq. 18), Lemma 3, Theorem 2 and Table 3.
- Friston & Penny (2011), [LIT-tmpuhjzx](../literature.d/LIT-tmpuhjzx.md), read in [NOTE-tmpy47cf](../notes.d/NOTE-tmpy47cf.md): Eq. 9 and
  the Discussion's open question about the reduced free energy.
- Friston, Parr & Zeidman (2018; v2 2019), [LIT-tmpbgf7s](../literature.d/LIT-tmpbgf7s.md), read in
  [NOTE-tmpdrgaj](../notes.d/NOTE-tmpdrgaj.md): Eqs. 9–11, §6.2 (pruning a Gaussian mixture) and §7.3
  (hierarchical inversion as reductions).

## The argument

**What Laplace BMR computes.** Friston & Penny's Eq. 9 gives the reduced
free energy from the full model's Gaussian prior N(η, Π⁻¹) and Gaussian
posterior N(μ, P⁻¹). It is ½ ln|Π_i P_F P_i⁻¹ Π_F⁻¹|, plus quadratic
forms, plus the full model's free energy F_F. The log-determinant is a
ratio of Gaussian volumes, MacKay's Occam factor ([THEORY-tmpzelk0](THEORY-tmpzelk0.md), regular
half). F_F under variational Laplace is accuracy minus a Gaussian
complexity term ([LIT-tmpbgf7s](../literature.d/LIT-tmpbgf7s.md), Eq. 4). That term grows as (r/2) log n,
where r is the number of directions the data determine at the fitted
point. Friston, Parr & Zeidman restate the same Gaussian form as their
Eq. 11.

**What singular learning theory says the price is.** If a model "contains
hierarchical layers, hidden variables, or grammatical rules, then it is
singular". Its likelihood cannot be approximated by any normal
distribution, and its free energy grows as λ log n, with λ the RLCT
([LIT-tmpmsuf3](../literature.d/LIT-tmpmsuf3.md), §1 and Theorem 2). λ is a minimum over the charts of a
resolution of singularities (Eq. 18). By the computation of Lemma 3 made
locally, a smooth point of the optimal set with non-degenerate curvature
across it contributes r/2. So λ is at most the Gaussian count at any such
point, and it is strictly smaller when the optimal set has a more singular
point. That step is the filer's, made from the paper's definition.
Table 3 shows the gap is real. Rank-4, 5 and 6 models of a rank-3 truth
have λ = 15, 16 and 17, against half-dimensions of 16, 17.5 and 18.

**Where the two meet.** BMR is used on singular parents. §6.2 of
[LIT-tmpbgf7s](../literature.d/LIT-tmpbgf7s.md) prunes a Gaussian mixture, and mixtures are on Watanabe's
list. §7.3 inverts hierarchical models as cascades of reductions, and
§7.2 prunes the hidden-state priors of active-inference agents. A
reduction that switches off a column of B in reduced-rank regression is
also a reduction to a singular set: once that column is zero, the matching
row of A drops out of the likelihood. The Savage–Dickey form makes the
consequence concrete. The reduced evidence is the full posterior's density
at the reduced set, divided by the prior's density there ([THEORY-tmp9y0ia](THEORY-tmp9y0ia.md)).
In a singular model that set is where the true posterior's non-Gaussian
mass sits. A Gaussian Q fitted at the peak assigns it a density fixed by
curvature at the peak instead.

**The claim.** Under the Laplace approximation, the free energy of a
singular full model, and the reduced free energies computed from it, carry
complexity terms of the form (r/2) log n where the true free energies
carry λ log n. Their differences are then wrong by a multiple of log n
unless the gaps happen to cancel. More data does not remove the error. It
grows.

## What this does not say

- **It does not touch the identity.** [THEORY-tmp9y0ia](THEORY-tmp9y0ia.md) is exact. The claim
  is about computing it with a Gaussian posterior.
- **It does not say BMR selects the wrong model.** A log n error in every
  score can leave the ranking intact, and the simulations in [LIT-tmpuhjzx](../literature.d/LIT-tmpuhjzx.md)
  and [LIT-tmpbgf7s](../literature.d/LIT-tmpbgf7s.md) recover their generating structures. It says the free
  energies and Bayes factors reported are not the singular ones.
- **It does not say BMR's models are all singular.** Nonlinear is not
  singular. A dynamic causal model whose parameters are identified at the
  fitted point may be regular there. Friston & Penny's "early impressions"
  of agreement for weakly nonlinear models are not evidence against this
  account, and they compared Laplace with Laplace.
- **It does not cover the Dirichlet forms.** Smith et al. ([LIT-tmpesz2r](../literature.d/LIT-tmpesz2r.md))
  reduce Dirichlet counts under a mean-field posterior. Their reductions
  failed for 2–3 concepts and succeeded every time when the likelihood was
  given. That is suggestive. The approximation there is a different one,
  and whether it shares this defect is open.
- **It is not in either literature.** WBIC does not mention model
  reduction. The BMR papers do not mention singular models or the RLCT.
  Friston & Penny name the general worry themselves: "for highly nonlinear
  models the true posterior density will not be Gaussian", so whether "the
  reduced free-energy [is] a good proxy for the free-energy of reduced
  models" is open ([LIT-tmpuhjzx](../literature.d/LIT-tmpuhjzx.md), Discussion).

## Connections

- **Extends [THEORY-tmpzelk0](THEORY-tmpzelk0.md).** That account says the penalty is set by
  curvature in regular models and by λ in singular ones. This one carries
  it into Bayesian model reduction. Laplace BMR uses the regular penalty,
  and its parents are often singular.
- **[THEORY-tmp9y0ia](THEORY-tmp9y0ia.md)** is the exact identity whose Gaussian evaluation is
  in question here.
