---
status: Read
paper: 'LIT-tmprfb8b'
title: 'Erkut, Ingolfsson and Erdoğan — Ambulance location for maximum survival'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Read on 2026-11-04 from the accepted preprint of November 2007 on
    Armann Ingolfsson's University of Alberta page,
    https://sites.ualberta.ca/~aingolfs/documents/survival15november07.pdf,
    32 pages, extracted with pdftotext. Registered and read at the owner's
    request as a stand-in for McLay and Mayorga (2010), LIT-tmprh2zk, of
    which no lawful copy was found. Read: the abstract and §§1–7 in full,
    with Tables 1–6. Not read: Appendix A (the formulations of MCLP,
    MEXCLP, MCLP+PR, MEXCLP+PR and Jarvis's heuristic) and the reference
    list, beyond spot checks. Page numbers below are the preprint's, which
    is not the typeset version of record.
date: '2026-11-04'
summary: >-
  Puts a cardiac-arrest survival function into four standard EMS covering
  models and compares locations by expected survivors on Edmonton data.
  In the deterministic models the survival objective gives up to 7.7% more
  survivors than maximal covering and up to 23.5% more than the q-median;
  once random response times or busy probabilities enter, coverage comes
  close to or reaches the survival optimum, and changing the objective
  alone captures all of the gain. Survival functions for cardiac arrest
  only; static location models; one city.
---
<!-- inactive-ok-file: LIT-tmprh2zk THEORY-tmpagbfa — Unavailable or Proposed; the unread paper this stands in for, and the account filed from this reading -->

# NOTE-tmp241k1: Erkut, Ingolfsson and Erdoğan — Ambulance location for maximum survival

## Contribution

An argument, with a pathological example, that 0–1 coverage is a poor
proxy for survival; a Monte Carlo method for averaging a medical survival
function over covariates other than response time; survival-maximizing
counterparts of four covering models (MCLP to MSLP, MEXCLP to MEXSLP,
MCLP+PR to MSLP+PR, MEXCLP+PR to MEXSLP+PR); and evidence of how much the
switch matters as the models gain realism.

## Key insight

A covering model scores a response as success or failure at a threshold,
so it cannot tell a response one second inside the standard from one far
inside it, nor one just outside from one far outside. A survival function
grades every response time. In the authors' words, "the black-and-white
nature of the coverage concept is an important limitation" (p. 2). How
much the grading buys depends on how crude the proxy model is: much for
deterministic coverage, little once coverage itself becomes a probability.

## Assumptions

- **Cardiac arrest only.** The survival functions are for out-of-hospital
  cardiac arrest; in §6 all urgent calls (about 29%) are assumed to share
  them and non-urgent calls to carry negligible risk of death.
- **Closest-station service** in MSLP.
- **Independent busy fractions** in the MEXCLP family.
- **A heuristic.** The iterative algorithm for MEXCLP+PR and MEXSLP+PR is
  not guaranteed optimal.
- **Rough inputs.** The Monte Carlo inputs (access times, bystander CPR
  rates) are estimates.
- **Evaluation** of every solution by the approximate hypercube model on
  Edmonton data, 180 demand points and 16 candidate sites (p. 12).

## Key results

- **Premise (§1, p. 1).** "We will take as given that the real objective
  for an EMS system is to maximize the number of patients that survive
  and that coverage is used as a proxy for the real objective."
- **Coverage can fail arbitrarily (§1, p. 2).** By the A–X–B example,
  "covering models can result in arbitrarily poor location decisions for
  emergency facilities".
- **Deterministic models (§4.2, pp. 12–13).** With MCLP solutions "the
  expected number of survivors is up to 7.7% lower than it could be", and
  with q-median solutions "the expected number of survivors is up to 23.5%
  lower than it could be".
- **More stations, fewer survivors (§4.2, p. 13).** Under the proxies,
  adding a station can mean "the expected number of survivors may
  decrease".
- **An interpretable objective (§4.2, p. 14).** "the 10th station will
  save an average of 15 more lives per year in cardiac arrest cases".
- **Robustness (§4.3, p. 14).** "The solutions to MSLP were identical for
  the three survival functions, for all values of q".
- **Random response times (§6.1, p. 18).** "The percent improvement due to
  the incorporation of the survival function can be as high as 5.3%, and
  it averages 0.9% over the 16 problems"; in 8 of the 16 the two models
  give the same expected survivors.
- **Busy probabilities (§6.2, p. 20).** "MEXCLP+PR is a sophisticated model
  and the inclusion of the survival function does not add much to the
  performance of its solutions"; and "With higher congestion, the
  locations of the vehicles become less important".
- **Against average response time (§6.3, p. 21).** Against Jarvis's
  heuristic, "MEXSLP+PR improves these solutions by 6.5% on average (and by
  as much as 21.6%)".
- **All ten models (§6.4, Table 6, p. 22).** At six vehicles and busy
  probability 0.3: average response time 697.3 survivors, 745.0 with both
  uncertainties; coverage 761.6, and 809.1 with either; survival 809.1 in
  every version. "just changing the objective function to expected number
  of survivors achieves all of the benefits, even without incorporating
  the two elements of uncertainty in the model".

## Concepts

- **Survival function** (abstract): "A survival function is a
  monotonically decreasing function of the response time of an EMS
  vehicle to a patient that returns the probability of survival for the
  patient".
- **Coverage**: a demand point is covered if it lies within a distance or
  time standard of a facility.
- **MSLP, MEXSLP, MSLP+PR, MEXSLP+PR**: the maximal covering, maximum
  expected covering and their probabilistic-response versions, with
  coverage replaced by survival probability.

## Connections

It builds on the covering-model line: Church and ReVelle's MCLP, Daskin's
MEXCLP, their probabilistic-response versions, and Larson's hypercube in
its approximate form, used for evaluation. The medical survival functions
come from the cardiac-arrest literature.

As a stand-in for McLay and Mayorga (2010), LIT-tmprh2zk:

- **It restates** the shared idea: a response-time standard is a proxy for
  survival, and locating to maximize the proxy can differ from locating to
  maximize survivors. It also says something of the same kind as McLay
  and Mayorga's two findings: realistic enough coverage models reach the
  survival optimum (§6.1, §6.4), and urban–rural standards embody a
  choice between equal access and total survivors: "The objectives of
  providing equal access to EMS versus maximizing the total number of
  survivors lead to different deployment patterns" (p. 2).
- **It does not restate** their findings: that in Hanover County,
  Virginia, locating for seven- and eight-minute thresholds also maximizes
  survival; that nine- and ten-minute thresholds are more equitable, with
  better rural survival; or their method for evaluating thresholds.
- **It partly pulls against** their headline: it says standard coverage
  models "should not be used for EMS vehicle location" (p. 2), where their
  abstract finds thresholds whose optimum coincides with survival's.

## Bearing on the record

- **The pasted bibliography on emergency readiness.** This work is not in
  A's list. It supports A's gloss on McLay and Mayorga ("the operational
  metric is not necessarily the underlying organizational objective")
  more strongly than their abstract does, and also qualifies it: by
  Table 6 a sufficiently realistic proxy model attains the best-known
  survival value, so the gap is a property of crude proxies, not of
  proxies as such.
- **CLAIM-296 (has, knows it has, can deploy within a deadline).**
  Supports. In MEXCLP a unit at a station counts only with the probability
  that it is free; a station's ambulance is not a deployable one.
- **TERM-055 (operational availability).** Qualifies. Coverage, P(response
  ≤ τ), is a fleet-level α with a fixed deadline; the survival function
  replaces the hard deadline with a graded value of time, which the
  term's "before the deadline" does not cover.
- **LIT-1330 (Espeland and Sauder, rankings and reactivity).** Qualifies.
  That work concerns measures that change the behaviour they measure;
  this one a proxy objective that selects a different optimum, with no
  reactivity.
- **CLAIM-357 (residual and regret; aggregate performance does not tell
  infeasibility from violation).** Qualifies, loosely. Both warn against
  reading the sought quantity off a convenient aggregate; there is no
  formal link.
- **CLAIM-079, CLAIM-347, CLAIM-517, QUESTION-132.** Unrelated.
- Filed: THEORY-tmpagbfa. No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- The authors (§7, p. 23): "One obvious shortcoming of our approach is that
  we only have survival functions for one type of emergency call".
- Static location models; no dispatch or relocation decisions.
- One city's data.
- The survival functions come from observational studies, with covariates
  averaged by assumption.
