---
status: Read
paper: LIT-tmpzu3i3
title: 'de Jong, Ryan, van der Maas and Hamaker, read for what individual data showing hysteresis would have to be, and whether any psychopathology series has shown it'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 by the LEAD-032 worker from the PsyArXiv preprint
    (osf.io/zrcft/download, CC BY), text layer extracted with pdftotext.
    Sections 1–3 (models, estimation), 4.1 and 4.3 (simulation 1 set-up
    and conclusion), 6 (the depression simulation), 7 (the empirical
    example) and 8 (discussion) read in full; the result tables of
    simulations 1 and 2 (section 5) and Appendix B skimmed. Quotations
    rechecked against the extracted text.
date: '2026-11-22'
summary: >-
  A methods paper. It defines hysteresis as two switching thresholds, one
  for each direction, gives a model and an R package to estimate them from
  one person's series of a control variable and an outcome, and shows by
  simulation when the test works. Its psychopathology case is data
  simulated from a depression symptom network; it says no empirical
  psychological series had been analysed with it. For QUESTION-045 it
  makes "individual data showing hysteresis" testable and shows the data
  were not yet in hand. The reading is THEORY-tmpan7c6.
---
<!-- inactive-ok-file: THEORY-tmpan7c6 THEORY-058 — new or Proposed; this reading, and the account whose promote_when names hysteresis -->

# NOTE-tmpmrw49: de Jong, Ryan, van der Maas and Hamaker, read for what individual data showing hysteresis would have to be, and whether any psychopathology series has shown it

## Contribution

Brings the hysteretic threshold autoregressive model of econometrics
(Zhu et al. 2014; Li et al. 2015) into psychology, with an R package
(hystar), so that hysteresis can be tested in intensive longitudinal data
from one person rather than fitted, as the cusp catastrophe model usually
is, to cross-sectional data. The reading is THEORY-tmpan7c6.

## Key results

- **The definition (§1).** "Hysteresis is present when the switches
  between two regimes are associated with two different thresholds, one
  for each direction of the state transition". A switch "cannot be
  reversed as easy as would be the case when there is a single
  threshold".
- **The model (§2.2, eq. 3).** The regime is 0 when the control variable
  z (at lag d) is at or below r0, 1 when it is above r1, and unchanged in
  between, "the hysteresis zone". With r0 = r1 it is the ordinary TAR
  model, so the TAR is nested in it.
- **A panic example in their words (§2.1).** "When perceived threat is
  elevated by some external event, an individual might experience a panic
  attack, and the feedback loops of the system will retain this state. To
  end the panic attack, perceived threat may have to decrease to a lower
  level than the level that triggered the attack in the first place."
  Stated as illustration, citing Robinaugh et al. 2019; no data.
- **Why the cusp model is not enough (§1).** It "is often fit to
  cross-sectional data ..., which heavily impedes any conclusion about
  dynamics at the individual level", so "not much is known about
  hysteresis in psychological processes, yet."
- **When detection works (§4.2–4.3).** Information criteria "can detect
  hysteresis if the regimes have different means and T is sufficiently
  large"; the Ljung–Box comparison has "a high type-II error" but high
  precision. The control variable must be observed near the thresholds:
  in one condition "the observed z-values are not close to the true
  threshold, leading to a correct model selection of 0%."
- **The depression simulation (§6).** Data generated from Cramer et al.'s
  (2016) 14-symptom network, with stress moved between −1 and 1 over
  1,000 time points. All information criteria preferred the HysTAR model;
  "The difference between the threshold estimates indicates a
  substantial hysteresis effect, r̂1 − r̂0 = 0.55−(−0.33) = 0.88"; Table 2
  gives the threshold interval as (−0.30, 0.55], which makes it 0.85. The
  depressed regime had the stronger autoregression (0.89 against 0.73).
- **No empirical psychopathology (§7).** "the HysTAR model has not been
  used to investigate hysteresis in empirical psychological time series,
  so far." The one empirical case is a reanalysis of two participants in
  a speed–accuracy experiment (Dutilh et al. 2011), where the payoff for
  accuracy, the control variable, was set by the experimenters and moved
  up and down; hysteresis was supported for both.
- **What it does not give (§8).** "although we detected this phenomenon,
  the model did not give a description of the mechanism through which
  hysteretic regime switching took place."

## Assumptions

- Two regimes, each an autoregressive process; switching is
  deterministic given the control variable.
- One measured control variable, with its delay known or estimated; no
  measurement error.
- The control variable must range across both thresholds, more than
  once, for the zone to be estimated.

## Concepts

- **Hysteresis zone**: the range (r0, r1] of the control variable in which
  either regime can hold, and the current one persists.
- **TAR / HysTAR**: threshold autoregression with one threshold, or with
  one for each direction.
- **Control variable**: the measured driver (stress, payoff, perceived
  threat) whose crossing of a threshold switches the regime.

## Bearing on the record

- **QUESTION-045 (sharpens what would answer it; no answer).** The
  question accepts "individual data showing hysteresis". This paper says
  what such data must be: one person's series in which a measured driver
  (a stressor, perceived threat) rises past a level that switches them
  into the disordered regime and then falls back below that level without
  switching them out, until it passes a lower one. A disorder that
  "outlasts its trigger" is the case where the trigger has fallen inside
  the hysteresis zone. The paper also reports that no empirical
  psychological series had been analysed this way. So the second route of
  the question is open for want of data, not of method.
- **THEORY-058 (its promote_when, route 1; not met, the test supplied).**
  The route asks for hysteresis "in which symptoms stay up after the
  measured trigger has returned to its earlier level". This is a test for
  exactly that, and its only depression case is a simulation, which the
  route says "would not settle it". It does not meet the route.
- **TERM-020 (the hysteresis form in its note of 2026-10-18; parallel).**
  The note sets out ż = μz − z³ + h, which leaves its upper state only
  when h falls below a lower value than the one that brought it in. The
  HysTAR model is the discrete, estimable counterpart: r1 and r0 are the
  two values of the driver h. It gives the record a way to test the
  form on data, not support for it.
- **LIT-tmpuur53 (read beside it, contrast).** Critical slowing down,
  which Smit et al. test, is a sign of approaching a tipping point;
  hysteresis is the persistence after it. A series can show either
  without the other.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **A preprint**, with a reported effect that does not match its own
  table (0.88 in the text, 0.85 from the table's thresholds).
- **One outcome, one control variable**; the authors list measurement
  error and multiple outcomes as gaps that other models handle.
- **The control variable must be measured and must move both ways.** In
  clinical data the trigger is rarely measured, and rarely seen to fall
  back; the paper does not discuss how to get such data.
- **Detection, not mechanism**, as the authors say: a hysteretic fit does
  not show that a maintaining link is what holds the regime.
