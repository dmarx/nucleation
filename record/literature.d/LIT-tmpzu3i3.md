---
status: Active
status_note: >-
  read 2026-11-22 (NOTE-tmpmrw49) from the PsyArXiv preprint (CC BY);
  worth reading as the method by which hysteresis could be detected in
  one person's time series: two switching thresholds, one for each
  direction, against a single one. Its psychopathology case is simulated;
  it reports that the model "has not been used to investigate hysteresis
  in empirical psychological time series, so far", and its one empirical
  case is the speed–accuracy trade-off.
title: 'Detecting hysteresis in psychological processes with the hysteretic threshold autoregressive (HysTAR) model'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Found by the literature search of LEAD-032 (Europe PMC query
    H2_hysteresis, scratch/studies/lead-032/) and read the same day in
    NOTE-tmpmrw49, from the preprint at osf.io/zrcft/download (CC BY,
    20 pp. of text and references). Identifier, authors and posting date
    checked on Crossref, no email address sent; Crossref finds no
    published version under this title, only the preprint and the R
    package hystar on CRAN (10.32614/cran.package.hystar). Not held
    before: no hit for the DOI, the title or "HysTAR" in
    record/literature.d.
tags:
- complex-systems
- mathematical-statistics
- psychopathology-and-treatment
date: '2026-11-22'
published: '2023-12-18'
doi: '10.31234/osf.io/zrcft'
url: 'https://osf.io/zrcft'
first_author: 'de Jong'
keywords:
- hysteresis
- regime switching
- threshold autoregression
- threshold autoregressive model
- non-linearity
- sudden jumps
- discontinuous time series
- bimodality
- bistability
implementations:
- 'hystar (R package, CRAN)'
summary: >-
  de Jong, Ryan, van der Maas & Hamaker (2023), PsyArXiv preprint. Brings
  the hysteretic threshold autoregressive model of econometrics (Li et
  al. 2015) to psychology, with an R package: an outcome series switches
  regime when a measured control variable crosses an upper threshold, and
  switches back only when it falls below a lower one. Simulations show
  information criteria pick it over the one-threshold model when the
  regimes differ in mean and the series is long. It recovers hysteresis
  (thresholds −0.30 and 0.55) in data simulated from Cramer et al.'s
  depression symptom network, and in one empirical speed–accuracy data
  set. It reports no empirical psychopathology series. For QUESTION-045
  it is the method "individual data showing hysteresis" would need, and
  evidence that such data had not been analysed with it. Read in
  NOTE-tmpmrw49; the reading is THEORY-tmpan7c6.
---
<!-- inactive-ok-file: THEORY-tmpan7c6 — new; this work's reading -->

# LIT-tmpzu3i3: Detecting hysteresis in psychological processes with the hysteretic threshold autoregressive (HysTAR) model

de Jong, Ryan, van der Maas & Hamaker (2023), PsyArXiv,
DOI 10.31234/osf.io/zrcft. R package: hystar.

## Key takeaways

- Hysteresis, in their definition, is present "when the switches between
  two regimes are associated with two different thresholds, one for each
  direction of the state transition". The HysTAR model estimates both
  thresholds from a bivariate series, a control variable and an outcome,
  and nests the one-threshold TAR model as the case r0 = r1.
- Detection is by comparing the two models' fit; it works when regimes
  differ in mean, the series is long, and the control variable is
  observed near both thresholds.
- In data simulated from a 14-symptom depression network driven by
  stress going up and down, the model found "a substantial hysteresis
  effect, r̂1 − r̂0 = 0.55−(−0.33) = 0.88"; its own table gives the lower
  threshold as −0.30.
- No empirical psychopathology series is analysed; the authors say the
  model "has not been used to investigate hysteresis in empirical
  psychological time series, so far".

## Standing in the record

Filed by LEAD-032 for the second thing QUESTION-045 would accept,
"individual data showing hysteresis". It supplies the test, not the data.
