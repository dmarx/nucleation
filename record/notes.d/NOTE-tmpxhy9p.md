---
status: Skimmed
paper: LIT-tmptcaax
title: 'The No-U-Turn Sampler (NUTS)'
version: 1
date: '2026-09-25'
summary: >-
  NUTS removes HMC's trajectory-length parameter L by building trajectories recursively (doubling) until they begin to turn back on themselves. With step size tuned automatically by Nesterov-style dual averaging, it matches or beats well-tuned HMC with no hand tuning.
---

<!-- inactive-ok-file: LIT-tmptcaax — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpxhy9p: The No-U-Turn Sampler (NUTS)

## Contribution

Hamiltonian Monte Carlo uses gradient information to avoid random-walk behaviour and handle correlated parameters, so it converges on high-dimensional targets much faster than random-walk Metropolis or Gibbs sampling. Its performance, however, depends heavily on the step size ε and the number of steps L. NUTS builds a set of candidate points spanning a wide swath of the target by a recursive algorithm, and stops automatically when the trajectory starts to double back, so L is no longer needed. Empirically NUTS is at least as efficient as well-tuned HMC. A primal-dual averaging scheme adapts ε during warm-up, so NUTS runs with no hand tuning, which makes it suitable for "turnkey" automatic inference engines such as BUGS-style systems.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Structure: §2 reviews HMC; §3.1 derives NUTS (§3.1.1 the simplified version, §3.1.2 the efficient version); §3.2 covers step-size adaptation by dual averaging; §4 is the empirical evaluation; §5 the discussion.
- Evaluation design (§4): four targets (a 250-D correlated Gaussian, Bayesian logistic regression on German credit, a hierarchical logistic regression, and stochastic volatility). There are 3,200 HMC and 600 NUTS runs. Efficiency is measured as minimum-over-dimensions ESS per gradient evaluation, counting the second moment as well as the mean to catch the anti-correlated samples HMC produces near resonances.
- Dual averaging (§4.2): it usually hits the target acceptance statistic δ and converges within a few hundred iterations, though more slowly on stochastic volatility. Parameters γ = 0.05, t₀ = 10, κ = 0.75. δ = 0.65 is used in illustrations.
- Discussion (§5): the authors compare NUTS only with basic HMC. A mass matrix approximating the posterior covariance would help both samplers. Windowed HMC suggests part of NUTS's advantage comes from having no single accept/reject step. RMHMC is noted as complementary.
- Appendix: the ESS estimator truncates autocorrelations when they first drop below 0.05, using reference moments from a separate 50,000-sample NUTS run.

## Open questions

- NUTS is the default sampler in Stan, PyMC and NumPyro, so this is the root citation for "use NUTS with adapted step size and mass matrix" in a probabilistic-modeling note. The survey is right that samplers are in the blurb.
- Current practice has moved on in details: multinomial rather than slice sampling in Stan, diagonal or dense mass-matrix adaptation, and newer ESS estimators. A note should cite Betancourt (2017) or Stan's documentation for the current form, not treat the 2011/2014 algorithm as what is run today.
