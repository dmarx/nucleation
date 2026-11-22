---
status: Read
paper: LIT-tmp6fb6y
title: 'Tatel and Ackerman''s posted data and analysis script for the meta-analysis of procedural skill decay'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read and analysed on 2026-11-22 for LEAD-124 from the OSF project's
    files (https://osf.io/download/8hw6u/, the independent-samples data
    sheet, version of 2025-04-09; https://osf.io/download/zq35p/, the R
    script), with the variable key in the data sheet. Read: the whole
    script (packages, data preparation, the main models, the moderator
    models including task type) and the variable key; all 1,273 rows of
    the independent-samples sheet used. The other four sheets were listed,
    not opened. The refit is CASE-tmp4f2jr, rerunnable from
    scratch/studies/lead-124/. Read beside it, for the moderator results it
    is checked against: the dissertation's §5.3.1 (pp. 79–86), §6.3
    (pp. 128–129) and Appendices C and D (pp. 148–150), LIT-2079, from
    Georgia Tech's repository PDF.
date: '2026-11-22'
summary: >-
  The coded data and metafor script behind Tatel & Ackerman (2025). Refitted
  with the authors' specification they give the abstract's slopes, and by
  task type they give the dissertation's result: laboratory tasks decline
  fastest, real-world domains slower and alike. Every type declines faster
  over short intervals than over long ones, so the linear rate depends on
  the interval mix.
---
<!-- inactive-ok-file: LIT-2088 LIT-tmp6fb6y CASE-tmp4f2jr THEORY-tmppzw1a ARG-tmpbjn5v — Unfetched or new; the unread article and the entries filed on 2026-11-22 -->

# NOTE-tmps1muw: Tatel and Ackerman's posted data and analysis script for the meta-analysis of procedural skill decay

## Contribution

The coded data and script of the only large meta-analysis of procedural
skill decay over months that the record holds. They let the article's
models be refitted and extended without its text.

## Key insight

The pooled slope of about 0.08 SD a month averages two things: laboratory
tasks that lose accuracy fast, and real-world tasks that lose it at a
quarter to a third of that rate. Within the real-world tasks only medical
and dental tasks show a measurable decline in accuracy.

## Assumptions

- **The authors' specification.** Independent-samples d with variance
  (n1+n2)/(n1·n2) + d²/(2(n1+n2)); REML random effects; intervals of 60
  months or more dropped for accuracy and speed; clusters are source ×
  study × group. The script fits with Knapp–Hartung tests and then
  clubSandwich robust errors.
- **Task domain** is the authors' code: laboratory/artificial,
  medical/dental, sports, "Military and non-military transportation",
  miscellaneous. Task realism is laboratory/artificial against real world.
- **Linear in months**, as the authors fit it. The capped refits below
  test this crudely.

## Key results

From the refit, CASE-tmp4f2jr (robust SEs, CR1):

- **Main slopes.** Accuracy −0.076 (SE 0.012, k = 824), speed −0.063
  (0.022, k = 266), mixed −0.061 (0.019, k = 178). The abstract: "grew
  stronger by 0.08/month for accuracy-based performance measures and
  0.06/month for speed-based and mixed performance measures" (LIT-2088,
  abstract).
- **Accuracy by domain.** Laboratory −0.164 (0.024, k = 274);
  medical/dental −0.043 (0.012, k = 249); military and transport −0.009
  (0.024, k = 66); miscellaneous −0.032 (0.013, k = 27); sports +0.015
  (0.021, k = 208). The interactions against laboratory, 0.12, 0.16,
  0.13 and 0.18, are the dissertation's Appendix D values to two places.
- **Speed by domain.** Laboratory −0.11 (0.065); medical/dental −0.03
  (0.025); the other domains have 9 to 46 effect sizes, none beyond six
  months, and slopes that swing in sign.
- **Mixed.** Real-world −0.045 (0.020, k = 156; mostly medical and
  dental); the 22 laboratory mixed effect sizes reach only 0.93 months.
- **Where the long intervals are.** Beyond six months: laboratory accuracy
  9 effect sizes (longest 14 months), medical/dental 27 (22), military
  and transport 3 (12), sports 2 (12), miscellaneous 3 (18).
- **Capped refits.** Fitted only up to 6 months, accuracy declines by
  0.54 SD a month on laboratory tasks (0.16) and 0.12 on medical and
  dental (0.025); up to 3 months, 0.54 and 0.14; over the full range,
  0.16 and 0.04. The laboratory–real-world gap holds at every cap, so it
  is not an artefact of laboratory studies using short intervals. But the
  slope of every type falls as longer intervals are admitted: decay is
  faster early.
- **Intercepts.** Real-world tasks start lower: at an interval of zero
  the medical and dental line sits at −0.52 against −0.13 for
  laboratory, so the two accuracy lines cross near three months (the
  reviewer's arithmetic, (0.522 − 0.125) / (0.164 − 0.043)).

From the dissertation, LIT-2079, for the same moderator:

- **Task type (p. 81).** "The moderating effects are mostly attributed to
  differences between laboratory vs. artificial tasks. Performance on
  real-world tasks was better retained over time than performance on
  laboratory/artificial tasks for accuracy-based performance measures.
  There is less evidence, however, that skill decay patterns differ
  between different types of real-world tasks (i.e., medical/dental,
  military/transportation, sports)."
- **Confounded with complexity (p. 129).** "Real-world tasks had
  significantly higher task complexity ratings across all three
  dimensions than laboratory/artificial tasks did", and "The direction of
  the relationship remains unclear."
- **Open- and closed-loop tasks (pp. 81–82).** Open-loop tasks were better
  retained for mixed measures (β = 0.11, p < 0.01), and the same trend
  held for speed, not significant; accuracy showed no difference.

## Concepts

- **Laboratory/artificial task:** a task made for the study, as against a
  real-world task (medical, dental, sports, military, transport and
  others; Appendix B of the dissertation lists them).
- **Capped refit:** the same linear model fitted only to intervals up to
  a cap. Under a correct linear model the slope would not depend on the
  cap; a slope that falls as the cap rises says the decline decelerates,
  or that studies at long intervals differ.

## Connections

**Against the article it supplies**, LIT-2088, known only from its
abstract:

- *Restates:* the slopes, which the refit reproduces to two places.
- *Does not restate:* the article's text, its moderator tables or its
  half-loss points (6.5, 13, 11 months). Whether the article reports the
  task-type moderator as the dissertation does, or with the robust errors
  the script computes, is not known. The data sheet has 1,273
  independent-samples effect sizes, against the dissertation's 1,281 and
  the abstract's 1,344, which may count paired-samples effect sizes too.
- *Against the dissertation*, LIT-2079: the same task-type result, now
  from the article's data.

## Bearing on the record

- **QUESTION-433: bears on, does not answer.** The data are the same
  authors', so not independent. They qualify the question's premise: the
  "roughly linear" decline is a fit to a decelerating one, and its slope
  is set by the mix of intervals and task types.
- **CLAIM-558: qualifies part 1, does not defeat it.** For medical and
  dental tasks, the closest to the rare clinical procedures its third part
  generalizes from, accuracy declines significantly, at about half the
  pooled rate over the full range and faster within six months. Sports and
  military or transport tasks show no measurable decline in accuracy, but
  on intervals of a year at most, so the defeater ("beyond a year") is not
  met. Filed as ARG-tmpbjn5v.
- **CLAIM-422: supports, unchanged.** A real-world procedure trained
  and not used still loses accuracy measurably.
- **THEORY-1424: narrows.** Its pooled rate is the average of
  laboratory and real-world rates that differ by a factor of about four.
  Filed: THEORY-tmppzw1a.
- No instruction for machine-learning practice.

## Limitations

- The robust errors are CR1, not the authors' CR2, and the Knapp–Hartung
  adjustment is not applied; slopes are unaffected and SEs close.
- The capped refits are a crude check for curvature. Capping selects on
  the predictor, which does not bias a correctly specified linear slope,
  so a change with the cap is evidence against linearity. But studies
  with long intervals also differ in design, so between-study confounding
  could produce the same pattern.
- Task type is confounded with complexity, interval range and measure
  type, and the domain codes are broad.
- The practice moderator was not split by task type.

## Open questions

- Does a decelerating model (log or power of the interval) fit better
  than the linear one by task type, and what half-loss times does it give
  for medical and dental tasks?
- Does the article report the task-type moderator? Reading LIT-2088
  would tell.
