---
number: 466
status: Read
formerly:
- NOTE-tmpt8akb
paper: LIT-563
title: 'HDDM: Hierarchical Bayesian Estimation of the Drift-Diffusion Model in Python'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the Europe PMC full-text XML of the CC BY article
    (PMC3731670): introduction, methods, the tutorial, the three simulation
    experiments, discussion and captions. The priors were read from the
    article's image of them. Code listings and several printed outputs are
    images the XML does not carry and were not seen. The online supplement
    (within-subject models, outlier handling, the hierarchical Bayesian
    background) was not read.
date: '2026-10-03'
summary: >-
  HDDM fits the full DDM (v, a, z, t with sv, st, sz) by MCMC in PyMC, with
  group-level priors such as μ_a ~ Gamma(1.5, 0.75), μ_v ~ N(2, 3),
  z_j ~ invlogit(N(μ_z, σ_z²)), and the Navarro–Fuss likelihood. A
  patsy-style regressor lets a parameter vary with a trial covariate. In
  simulations with 12 subjects and 20–150 trials, hierarchical Bayes had the
  lowest trimmed recovery error for every parameter and the highest power
  to detect drift differences and covariate effects, by up to 20% for the
  latter with larger effects and few trials.
---
<!-- inactive-ok-file: THEORY-061 — Proposed; named as the batch theory whose parameters this tool would estimate, nothing here rests on it -->

# NOTE-466: HDDM: Hierarchical Bayesian Estimation of the Drift-Diffusion Model in Python

## Contribution

A tested, documented, BSD-licensed Python package for hierarchical Bayesian
estimation of the drift diffusion model and the linear ballistic accumulator,
with a tutorial on real data and a parameter-recovery study comparing it with
the standard alternatives. Before it, the common DDM packages (DMAT, fast-dm)
fitted participants either one by one or as an average subject.

## Key insight

Participants in a cognitive experiment are neither identical nor unrelated.
A hierarchical model estimates how alike they are, parameter by parameter, and
uses that to borrow strength: where non-decision time varies little across
people, each person's estimate is anchored to the group's, which leaves more
of the data to determine the parameters that do vary, such as threshold. That
matters most where trials are few, as with patients, intra-operative
recordings, or noisy trial-by-trial neural covariates.

## Assumptions

- **Binary choices** with RT; the DDM likelihood F(a, z, v, t, sv, st, sz)
  of Navarro and Fuss (2009), an approximation to the Wald/Feller infinite
  series.
- **Hierarchy and priors** (Fig. 2, the "informative" default): μ_a ~
  Gamma(1.5, 0.75), σ_a ~ HalfNormal(0.1), a_j ~ Gamma(μ_a, σ_a²); μ_v ~
  N(2, 3), σ_v ~ HalfNormal(2), v_j ~ N(μ_v, σ_v²); μ_z ~ N(0.5, 0.5),
  σ_z ~ HalfNormal(0.05), z_j ~ invlogit(N(μ_z, σ_z²)); μ_t ~ Gamma(0.4,
  0.2), σ_t ~ HalfNormal(1), t_j ~ N(μ_t, σ_t²); sv ~ HalfNormal(2), st ~
  HalfNormal(0.3), sz ~ Beta(1, 3). The priors are justified by past
  literature (Matzke & Wagenmakers 2009). A non-informative version exists.
- **Inter-trial variabilities are estimated at group level only**, because
  their effect on the likelihood is too small to estimate per subject.
- **Simulation design** (Exps. 1–2): group parameters drawn uniformly, v₂ =
  2v₁, sz = st = 0, subject noise SDs 0.2, 0.2, 0.1 and 0.1 on v, a, t and sv.

## Key results

- **Tutorial (Cavanagh et al. 2011 data).** A model with drift split by
  conflict condition was preferred by DIC to one with a single drift (10,775.6
  vs 10,960.6). Posteriors showed drift for the easy win–lose condition well
  above the two high-conflict conditions. A regression of threshold on theta
  power by conflict level showed a positive theta–threshold effect off deep
  brain stimulation that reversed on it (Fig. 5).
- **Convergence guidance.** 2,000–10,000 samples, 20–1,000 burn-in, Gelman–
  Rubin R̂ under 1.02, and inspection of traces and autocorrelation.
- **Experiment 1 (12 subjects, 20–150 trials).** Trimmed mean absolute error
  was lowest for hierarchical Bayes for all parameters, with the largest gains
  for threshold and both drifts at few trials (Fig. 6). Paired with ML on the
  same data sets, HB was significantly better in every condition (inset).
- **Experiment 2 (75 trials, 8–28 subjects).** HB had the highest probability
  of detecting the drift difference at every sample size (Fig. 7).
- **Experiment 3 (trial-by-trial covariate on drift, effect sizes 0.1, 0.3,
  0.5).** HB raised detection by up to 20% for the larger effects with few
  trials, and modestly for the smallest effect (Fig. 8).
- **Source of the gain.** A t-test on HB's subject estimates also detected
  more effects, so the gain is attributed to the hierarchy. Those results were
  omitted because the t-test's independence assumption fails for
  hierarchically estimated parameters.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Hierarchical Bayesian estimation recovers DDM parameters with less error than per-subject ML, χ²-quantile and non-hierarchical Bayes, especially with few trials | moderate: simulations from the fitted model's own family, trimmed errors, one design | Exp. 1, Fig. 6 |
| C2 | It detects drift-rate differences and trial-wise covariate effects more often | moderate, with the caveat that HB used a posterior-interval test and the others t-tests | Exps. 2–3, Figs. 7–8 |
| C3 | The power gain comes from the hierarchy, not from the Bayesian test | weak: supported by a t-test result the authors omit as invalid | Results text |
| C4 | Frontal theta's effect on threshold reverses under subthalamic stimulation | not this paper's finding; a reanalysis of Cavanagh et al. (2011) shown for illustration | Fig. 5 |

## Method

Build a PyMC graphical model of the DDM with group and subject nodes,
optionally splitting parameters by condition (`depends_on`) or replacing a
parameter with a linear model of covariates (`HDDMRegressor`, patsy syntax).
Start chains at the MAP estimate, sample by MCMC, check convergence, and
compare models by DIC or by posterior differences. Run-time-critical code is
in Cython.

## Concepts

- **hierarchical Bayesian estimation**: subject parameters as draws from
  group distributions, all estimated together.
- **full DDM**: the DDM with across-trial variability in drift (sv),
  starting point (sz) and non-decision time (st).
- **informative priors**: priors set from the range of published DDM
  estimates, to reduce collinearity and implausible values.
- **DIC**: the deviance information criterion, lower is better; the authors
  note it is biased toward complex models.

## Connections

- **Ratcliff & McKoon 2008 ([LIT-576](../literature.d/LIT-576.md)).** The model statement HDDM
  implements, with the same across-trial variabilities. HDDM drops the χ²
  method on group-averaged data in favour of pooling at the level of
  parameters.
- **Bogacz et al. 2006 ([LIT-569](../literature.d/LIT-569.md)).** Interprets the parameters HDDM
  estimates as controlled quantities, which is what makes regressing
  threshold on a neural control signal meaningful.
- **Usher & McClelland 2001 ([LIT-565](../literature.d/LIT-565.md)).** Not implemented. HDDM's race
  model option is the linear ballistic accumulator, which has no leak and no
  inhibition.

## Bearing on the record

- A tool, not a theory. It is the means by which claims in the batch's
  theories (caution, bias and control of threshold, [THEORY-061](../theory.d/THEORY-061.md)) would
  be measured in individuals.
- **No ML instruction.** Bayesian inference is shared with machine learning,
  but the subject is cognitive measurement. Nothing here belongs in the
  anthology.

## Limitations

- **Self-evaluation on simulated data** generated from DDMs, with sz and st
  set to zero in the main experiments; robustness to misspecification is not
  tested here.
- **Different decision rules** for HB and the comparison methods complicate
  the power comparison; the clean comparison was omitted.
- **Binary choices only**, and the LBA is mentioned but not evaluated.
- **DIC's** known bias is acknowledged; Bayes factors are mentioned as an
  alternative but not implemented here.

## Open questions

- How robust is hierarchical estimation when the generating process is not a
  DDM, for example a leaky or competing accumulator?
- How well does trial-by-trial regression perform with fMRI, which the
  authors expect to be noisier than EEG?

## Corrections

- none to a seeded skim (there was no seed)
