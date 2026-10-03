---
number: 81
status: Active
formerly:
- THEORY-tmp9y0ia
title: 'The evidence of any model formed from a full model by changing only its prior is the full evidence times the full posterior expectation of the prior ratio, so the Savage–Dickey ratio is its point-mass case and choosing which parameters to keep is evidence maximisation over the prior'
version: 1
tags:
- model-comparison
- probabilistic-modeling
date: '2026-10-03'
source:
- LIT-620
- LIT-609
- LIT-614
summary: >-
  Friston & Penny (2011), [LIT-620](../literature.d/LIT-620.md), Eq. 3: if models share a
  likelihood and differ only in priors nested inside a full prior, then
  p(y|m_i) = p(y|m_F)·E_{p(θ|y,m_F)}[p_i(θ)/p_F(θ)]. Their Eq. 6 is the
  point-mass case, the Savage–Dickey ratio that Wagenmakers et al.
  (2010), [LIT-609](../literature.d/LIT-609.md), derive from the other end. Friston, Parr &
  Zeidman, [LIT-614](../literature.d/LIT-614.md), restate it for any new prior and give conjugate
  closed forms. Active because the identity is three lines of Bayes' rule
  that anyone can check. The two Savage–Dickey conditions turn out to be
  the same condition. The identity is exact. Its Laplace and variational
  forms are only as good as the full posterior, and with no constraint on
  the prior family the optimum is maximum likelihood.
---
<!-- inactive-ok-file: LIT-610 — Deferred: Dickey 1971 is unread; named as the source the ratio is named for, nothing rests on it -->
<!-- inactive-ok-file: THEORY-073 THEORY-079 — Proposed; named in Connections, no relation leans on them -->

# THEORY-081: The evidence of any model formed from a full model by changing only its prior is the full evidence times the full posterior expectation of the prior ratio, so the Savage–Dickey ratio is its point-mass case and choosing which parameters to keep is evidence maximisation over the prior

## Source

- Friston & Penny (2011), [LIT-620](../literature.d/LIT-620.md), read in [NOTE-487](../notes.d/NOTE-487.md): Eqs. 2–6
  (the identity and its point-mass case), Eq. 9 (the Laplace form), Fig. 3
  and the discussion of ARD, Table 1 and the Conclusion.
- Wagenmakers, Lodewyckx, Kuriyal & Grasman (2010), [LIT-609](../literature.d/LIT-609.md), read in
  [NOTE-484](../notes.d/NOTE-484.md): Eq. 12 and Appendix A (the ratio and its condition).
- Friston, Parr & Zeidman (2018; v2 2019), [LIT-614](../literature.d/LIT-614.md), read in
  [NOTE-477](../notes.d/NOTE-477.md): Eqs. 8–10 (the identity for any new prior), Eqs. 11–12
  and Table 1 (closed forms).

## The claim, derived

Let every model share the likelihood p(y|θ). Let m_F carry a full prior
p_F(θ), and let each reduced model m_i carry a prior p_i(θ) whose support
lies inside that of p_F ([LIT-620](../literature.d/LIT-620.md), Eq. 2). Then

p(y|m_i) = ∫ p(y|θ) p_i(θ) dθ = ∫ p(y|θ) p_F(θ) · p_i(θ)/p_F(θ) dθ
         = p(y|m_F) ∫ p(θ|y, m_F) · p_i(θ)/p_F(θ) dθ,

since p(y|θ)p_F(θ) = p(y|m_F)p(θ|y, m_F). This is Eq. 3 of Friston &
Penny. Friston, Parr & Zeidman write it as F[P̃ : P] ≈ ln E_Q[P̃/P] + F[P]
([LIT-614](../literature.d/LIT-614.md), Eq. 9), with the reduced posterior the full one reweighted
by the same ratio (Eq. 10). The reduced models never have to be fitted.
Nothing here depends on the form of the prior, the likelihood or the
posterior.

**Savage–Dickey is the point-mass case, and its two conditions are one.**
Split θ = (φ, ψ) and write the full prior as p_F(φ) p_F(ψ|φ). Take the
reduced prior that fixes φ = φ0 and keeps the full prior's conditional for
the rest: δ(φ − φ0) p_F(ψ|φ0). The conditional cancels in the ratio, so
p_i/p_F = δ(φ − φ0)/p_F(φ), and the identity gives

p(y|m_i)/p(y|m_F) = p(φ = φ0 | y, m_F) / p_F(φ = φ0).

That is Friston & Penny's Eq. 6, which they reach as the limit of a
shrinking reduced prior. It is also the Bayes factor that Wagenmakers et
al. derive for a point null in their Eq. 12 ([LIT-609](../literature.d/LIT-609.md)), from Bayes'
rule and a continuity condition. Wagenmakers et
al. need the nuisance prior under the null to equal the limit of the full
model's conditional prior at the null, p1(ψ | φ → φ0) = p0(ψ) (Appendix A).
Friston & Penny need the reduced model to differ from the full one only in
its prior on φ (their Eq. 5, with the prior on the other parameters
unchanged). Written out as above, these are the same requirement: the
reduced model's prior on ψ must be the full prior's conditional at φ0.
The record's entry for Friston & Penny already calls the two the same
identity reached from opposite ends, and this is why. The step is the
filer's. Neither paper cites the other.

**Selection and optimisation are one operation.** Scoring a discrete set
of reduced priors and keeping the best one is maximising p(y|m) over a
family of priors on a fixed likelihood. Switching a parameter off is a
prior of zero variance. Automatic relevance determination maximises the
same quantity over a continuous family of prior variances. Friston &
Penny: "in both cases, one is maximizing model evidence by changing
hyperparameters that encode the prior density over the parameters of a
likelihood function" ([LIT-620](../literature.d/LIT-620.md), Introduction). Their Fig. 3 shows why
the continuous version behaves like selection. The log evidence for a
relevant parameter has an interior maximum in its prior variance. For an
irrelevant one it keeps rising as the variance goes to zero, so
optimisation switches it off.

## What this does not say

- **It does not say BMR's numbers are exact.** The identity is exact. What
  is computed is the identity with the approximate posterior Q and free
  energy F of the full model in place of the true ones ([LIT-614](../literature.d/LIT-614.md),
  Eqs. 9–10), and every reduced score inherits their error. Friston &
  Penny leave open whether, for strongly nonlinear models, "the reduced
  free-energy [is] a good proxy for the free-energy of reduced models"
  (Discussion). [THEORY-079](THEORY-079.md) takes up one case where the Laplace form
  should fail.
- **It does not license unconstrained optimisation of the prior.** With no
  restriction on the prior family, the evidence-optimal prior is a point
  mass at the maximum-likelihood value ([LIT-620](../literature.d/LIT-620.md), Eq. 7 and its
  discussion). The equivalence of selection and optimisation needs a
  constrained hyperparameterisation, which Friston & Penny assume and do
  not derive.
- **It covers reductions only.** A model that is not the full model with a
  narrower prior cannot be scored this way, and the full model must
  already contain every candidate parameter ([NOTE-477](../notes.d/NOTE-477.md), Limitations).
- **It does not say pruning finds the generating structure.** Smith et al.
  ([LIT-615](../literature.d/LIT-615.md), Table 1) apply the Dirichlet form to a learned prior over
  hidden states. The true number of concepts won in 45–80% of 100 runs
  for 4 to 7 concepts and never for 2 or 3. It won every time when the
  likelihood was given rather than learned. The identity held throughout.
  What failed was the full posterior it was applied to.
- **It does not settle Dickey's own conditions.** The ratio is named for
  Dickey (1971), [LIT-610](../literature.d/LIT-610.md), which is unread. Whether Dickey stated it
  for general nested models or only for normal linear hypotheses is open.

## Connections

- **Markov blankets.** BMR's mean-field update ([LIT-614](../literature.d/LIT-614.md), Eq. 5) sets
  each posterior factor from the expected log joint "under its Markov
  blanket". That is the graphical blanket of whichever factorisation was
  chosen. It is an instance of [THEORY-066](THEORY-066.md)'s point that a blanket is
  defined relative to a chosen set, and it claims nothing about
  individuation, which [THEORY-073](THEORY-073.md) disputes. No relation is declared
  because this account is not about blankets.
- **MacKay's Occam factor ([LIT-623](../literature.d/LIT-623.md))** is the same penalty seen from
  one parameter. When φ0 sits at the posterior peak and the prior on φ is flat,
  the Savage–Dickey ratio's prior ordinate over its posterior ordinate is
  the posterior width over the prior width, which is MacKay's Occam factor
  for φ up to a constant. Wagenmakers et al. give the same automatic
  Occam's razor in their §2.2.1, citing MacKay ([NOTE-484](../notes.d/NOTE-484.md)).
