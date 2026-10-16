---
number: 475
status: Active
formerly:
- THEORY-tmp9tc4c
title: "In simulations from the drift-diffusion model itself, with 12 subjects and 20 to 150 trials each, hierarchical Bayesian estimation recovers every DDM parameter with less error than per-subject maximum likelihood, χ²-quantile fitting or non-hierarchical Bayes, most of all at few trials; whether the gain survives misspecification, and how much of the power gain is the hierarchy's, is not shown"
version: 1
tags:
- probabilistic-modeling
- psychometrics
- cognition
date: '2026-10-16'
source:
- LIT-563
summary: >-
  Wiecki, Sofer & Frank (2013), [LIT-563](../literature.d/LIT-563.md), read in [NOTE-466](../notes.d/NOTE-466.md). Experiment 1
  gives the lowest trimmed recovery error for HB on every parameter, and
  HB beat ML on the same data sets in every condition. Experiments 2–3
  report more power to detect drift differences and trial-wise covariate
  effects, but HB was judged by a posterior-interval test and the others
  by t-tests, and the clean comparison was omitted. All data were
  generated from DDMs, with sz = st = 0. It is the standard
  partial-pooling result shown for one model family, not a test of the
  DDM.
---

<!-- inactive-ok-file: THEORY-061 — Proposed; named as the account whose parameters this method would measure, nothing here rests on it -->

# THEORY-475: In simulations from the drift-diffusion model itself, with 12 subjects and 20 to 150 trials each, hierarchical Bayesian estimation recovers every DDM parameter with less error than per-subject maximum likelihood, χ²-quantile fitting or non-hierarchical Bayes, most of all at few trials; whether the gain survives misspecification, and how much of the power gain is the hierarchy's, is not shown

## Source

Wiecki, Sofer & Frank (2013), "HDDM: Hierarchical Bayesian Estimation of
the Drift-Diffusion Model in Python", [LIT-563](../literature.d/LIT-563.md), read in [NOTE-466](../notes.d/NOTE-466.md) from the
PMC full text. Code listings and the online supplement were not seen.

## What was actually shown

**The method.** Subject parameters are draws from group distributions,
all estimated together by MCMC, with informative priors set from
published DDM estimates (e.g. μ_a ~ Gamma(1.5, 0.75), μ_v ~ N(2, 3)) and
the Navarro–Fuss likelihood. Inter-trial variabilities are estimated at
group level only.

**Experiment 1 (Fig. 6).** Group parameters drawn uniformly, v₂ = 2v₁,
sz = st = 0, 12 subjects, 20 to 150 trials. Trimmed mean absolute error
was lowest for HB for every parameter, with the largest gains for
threshold and both drifts at few trials. Paired against ML on the same
data sets, HB was significantly better in every condition.

**Experiments 2–3 (Figs. 7–8).** At 75 trials and 8 to 28 subjects, HB
detected the drift difference most often at every sample size. For a
trial-by-trial covariate on drift, HB raised detection by up to 20% for
the larger effects (0.3, 0.5) with few trials, and modestly for 0.1.

**Why it helps.** Where a parameter varies little across people, each
estimate is pulled toward the group's, which leaves more of the data to
fix the parameters that do vary. The gain is largest where trials are
few.

What could have come out otherwise: per-subject ML could have recovered
some parameter better, for instance where the informative priors were
off. It did not in these simulations.

## What this does not say

- **That HB is better when the data are not a DDM.** Every data set was
  generated from the fitted family, with sz and st set to zero.
  Robustness to a leaky or competing accumulator is untested ([NOTE-466](../notes.d/NOTE-466.md),
  Open questions).
- **That the power gain comes from the hierarchy.** HB used a
  posterior-interval test, the others t-tests. The authors attribute the
  gain to the hierarchy on the strength of a t-test on HB's estimates,
  which they then omit as invalid (C3, weak).
- **That the DDM is the right model of the choices.** The tool measures
  DDM parameters; it does not test the model.
- **Anything about theta and threshold under deep brain stimulation.**
  Fig. 5 reanalyses Cavanagh et al. (2011) as an illustration (C4).

## Connections

- The model HDDM implements is Ratcliff & McKoon's ([LIT-576](../literature.d/LIT-576.md)), and the
  account of its parameters as controlled quantities is [THEORY-061](THEORY-061.md) (Bogacz
  et al., [LIT-569](../literature.d/LIT-569.md)), which HDDM would let one test in individuals.
- [THEORY-068](THEORY-068.md) (balanced leak and inhibition) concerns accumulators HDDM
  does not implement; its race option is the linear ballistic
  accumulator.
- [QUESTION-062](../questions.d/QUESTION-062.md) asks whether a goal sets threshold, starting point or
  drift within one decision. HDDM is the measuring instrument such a
  test would use; this THEORY does not answer it.
