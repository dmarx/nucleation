---
number: 314
status: Proposed
formerly:
- CASE-tmp4f2jr
title: 'Refitting Tatel and Ackerman''s posted data by task type reproduces their headline slopes and finds accuracy declining by 0.16 SD a month on laboratory tasks against 0.04 on medical and dental tasks, and not measurably on sports or military and transport tasks, with every type declining faster over short intervals'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-124. The article
    (LIT-2088) could not be fetched; its OSF project (LIT-3080)
    holds the data and script, which were refitted. The scripts and
    output are committed under scratch/studies/lead-124/; the data are
    not, and are downloaded again from OSF to rerun.
standing: documented
kind: executed-study
tags:
- learning-and-conditioning
- psychometrics
date: '2026-11-22'
line:
- readiness
reported_in:
- LIT-3080
draws_on:
- THEORY-1424
bears_on:
- QUESTION-433
summary: >-
  [LEAD-124](../leads.d/LEAD-124.md) asked for decay estimates by skill type from Tatel & Ackerman
  (2025). With the authors' own specification and their posted
  independent-samples data (1,273 effect sizes), the main slopes are
  −0.076, −0.063 and −0.061 SD a month (accuracy, speed, mixed), the
  abstract's 0.08, 0.06 and 0.06. By task domain, accuracy declines by
  0.164 a month on laboratory tasks, 0.043 on medical and dental, 0.032
  on miscellaneous and 0.009 on military and transport, and sports
  improves by 0.015 (robust SEs 0.012 to 0.024). Capped at six months, laboratory 0.54 and
  medical and dental 0.12. The laboratory–real-world gap holds at every
  cap; every slope shrinks as longer intervals are admitted.
---
<!-- inactive-ok-file: LIT-2088 — Unfetched or new; the unread article and its OSF project, filed on 2026-11-22 -->

# CASE-314: Refitting Tatel and Ackerman's posted data by task type reproduces their headline slopes and finds accuracy declining by 0.16 SD a month on laboratory tasks against 0.04 on medical and dental tasks, and not measurably on sports or military and transport tasks, with every type declining faster over short intervals

## What was done

[LEAD-124](../leads.d/LEAD-124.md) asks for Tatel & Ackerman (2025), [LIT-2088](../literature.d/LIT-2088.md), to be read for
"Decay estimates by skill type". The article's APA copy answered with a
WAF challenge (2026-11-22). Its OSF project, [LIT-3080](../literature.d/LIT-3080.md), holds the
coded data and the authors' metafor script, so the article's task-type
models were refitted from those.

Specification, following the script: Cohen's d for independent samples,
variance (n1+n2)/(n1·n2) + d²/(2(n1+n2)); REML random effects; intervals
of 60 months or more dropped for accuracy and speed; robust standard
errors clustered by source × study × group (CR1 here, CR2 in the
script). Models: retention interval alone; retention interval × task
realism; retention interval × task domain, with laboratory tasks as the
reference; the same models with intervals capped at 1, 3, 6 and 14
months. Code: scratch/studies/lead-124/ (`metareg.py`, tested;
`by_task_type.py`; `results.json`).

## Checks

- Main slopes: accuracy −0.076 (k = 824), speed −0.063 (266), mixed −0.061
  (178). The abstract gives 0.08, 0.06 and 0.06.
- Accuracy domain interactions: 0.121, 0.155, 0.132, 0.178. The
  dissertation's Appendix D ([LIT-2079](../literature.d/LIT-2079.md), pp. 149–150) gives 0.12, 0.16,
  0.13, 0.18.

## Results

Slope in SD a month (robust SE), accuracy:

| Task type | k | k beyond 6 months | Full range | Up to 6 months | Up to 3 months |
|---|---:|---:|---:|---:|---:|
| Laboratory/artificial | 274 | 9 | −0.164 (0.024) | −0.540 (0.160) | −0.539 (0.160) |
| All real-world | 550 | 35 | −0.054 (0.010) | −0.134 (0.019) | −0.140 (0.039) |
| Medical/dental | 249 | 27 | −0.043 (0.012) | −0.118 (0.025) | −0.135 (0.056) |
| Military and transport | 66 | 3 | −0.009 (0.024) | −0.036 (0.042) | −0.025 (0.064) |
| Miscellaneous | 27 | 3 | −0.032 (0.013) | −0.335 (0.282) | −0.335 (0.282) |
| Sports | 208 | 2 | +0.015 (0.021) | +0.022 (0.036) | +0.038 (0.120) |

Speed: laboratory −0.110 (0.065), all real-world −0.037 (0.023),
medical/dental −0.029 (0.025); the other domains have 9 to 46 effect
sizes and none beyond six months. Mixed: real-world −0.045 (0.020); the
22 laboratory mixed effect sizes end at 0.93 months, so the domain model
is singular.

## What it shows

1. **Skill type matters, mostly as laboratory against real world.** At
   every cap, laboratory accuracy declines three to four times faster
   than real-world accuracy. The gap is not an artefact of laboratory
   studies using shorter intervals.
2. **Among real-world tasks, medical and dental decline measurably.**
   Sports and military or transport accuracy show no measurable decline,
   on intervals of a year at most and with two or three effect sizes
   beyond six months.
3. **The decline decelerates.** Every type's slope is steeper over short
   intervals. The linear slopes, pooled or by type, depend on the mix of
   intervals in the data. Between-study differences could produce the
   same pattern; a non-linear model was not fitted.
4. **Real-world tasks start lower.** The medical and dental line sits at
   −0.52 at an interval of zero, against −0.13 for laboratory tasks. The
   lines cross near three months (the assistant's arithmetic).

## Limits

The data are the same authors', so this is not the independent synthesis
[QUESTION-433](../questions.d/QUESTION-433.md) asks for. The article's own moderator analyses are unread.
Task type is confounded with complexity, interval range and measure.
Robust SEs are CR1 without Knapp–Hartung, so p-values are approximate.
The practice moderator was not split by type.

The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
