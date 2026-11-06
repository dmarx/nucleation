---
number: 1424
status: Active
formerly:
- THEORY-tmpsm9h9
title: 'Tatel finds that procedural skills with motor components decline roughly linearly with months of infrequent use, by about 0.06 to 0.08 standard deviations a month on average, losing about half of training gains within six to fifteen months, and that accuracy declines more slowly when a performance opportunity, most often an earlier retention test, falls in the interval'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    The twenty-ninth status review, at the status review's ruling (the
    owner delegated these rulings). NOTE-1560 is now Read: the
    effect-size chapter, all moderators, the formula comparison and the
    publication-bias sections are added. Narrowed under ADR-047, kind 3:
    the old title's practice clause stated for all measures what Tatel
    finds for accuracy only, and the code behind it is mostly an earlier
    retention test. The old title was "Tatel finds that procedural skills
    with motor components decline roughly linearly with months of
    non-use, by about 0.06 to 0.08 standard deviations a month, losing
    about half of training gains within six to fifteen months, and more
    slowly when occasional practice occurs during the interval".
    "non-use" becomes Tatel's "infrequent use", and "on average" marks
    the pooled slopes. Status Proposed → Active under ADR-065: the title
    reports one meta-analysis, read in full on every part it uses, with
    its hedges kept. The promote_when, "An independent meta-analysis, or
    a large longitudinal study, of motor or procedural skill retention
    over intervals of months finds a monotonic decline of comparable size
    (on the order of 0.05 to 0.1 standard deviations a month, or about
    half of training gains lost within six to fifteen months), together
    with slower decline when intermittent practice occurs during the
    interval.", moves to a new QUESTION. The body adds the
    laboratory–real-world difference and the level of the practice
    moderator.
tags:
- learning-and-conditioning
- psychometrics
date: '2026-11-04'
source:
- LIT-2079
bears_on:
- QUESTION-tmpec8ky
summary: >-
  Tatel (2023), [LIT-2079](../literature.d/LIT-2079.md), the PhD dissertation behind Tatel & Ackerman
  (2025), [LIT-2088](../literature.d/LIT-2088.md); read in NOTE-1560. A random-effects
  meta-regression over 457 sources. The slopes are the article abstract's
  too; the half-loss ranges are the dissertation's (the article gives
  6.5, 13 and 11 months). The practice moderator holds for accuracy only,
  and the author calls the moderators far from definitive. It does not
  say that decay is linear beyond a year, where data are few, or anything
  about organizations. Active as a report of one meta-analysis; whether an
  independent synthesis agrees is open.
---
<!-- inactive-ok-file: LIT-2088 — Unfetched; the article the dissertation stands in for -->

# THEORY-1424: Tatel finds that procedural skills with motor components decline roughly linearly with months of infrequent use, by about 0.06 to 0.08 standard deviations a month on average, losing about half of training gains within six to fifteen months, and that accuracy declines more slowly when a performance opportunity, most often an earlier retention test, falls in the interval

## Source

Tatel (2023), [LIT-2079](../literature.d/LIT-2079.md); read in [NOTE-1560](../notes.d/NOTE-1560.md). It stands in for
Tatel & Ackerman (2025), [LIT-2088](../literature.d/LIT-2088.md), unread.

## What was actually shown

- **The rate** (p. 70): random-effects meta-regressions of the
  acquisition-to-retention standardized mean difference on retention
  interval in months give −0.08 for accuracy (829 effect sizes) and −0.06
  for speed (267) and mixed (180). The slope could have been flat or
  non-linear; non-linear fits did not improve fit or were non-monotone
  (p. 69, fn. 10).
- **The share of gains** (p. 106): set against a separate meta-analysis
  of acquisition gains, about half is lost after 6–9 months (accuracy),
  12–15 (speed) and 9–12 (mixed), all after about 15, 27 and 30.
- **Practice in the interval** (pp. 86–87; Appendix L, p. 165): a binary
  code for performance opportunities, set mostly for a second retention
  test on the same people (p. 40), moderated the slope for accuracy
  (β = 0.06, p < 0.01), not significantly for mixed (0.06) or speed
  (0.02). The author reads it as "less rapid skill decline was observed
  on second retention tests" (p. 130). With an opportunity the accuracy
  intercept is 0.59 SD lower (Appendix L). By the reviewer's arithmetic
  from Appendix L, not Tatel's (0.59 / 0.06), the two lines cross near ten
  months, so the advantage shows only beyond that.
- **Laboratory against real-world tasks** (pp. 79–80; Appendix C, p. 148):
  "performance on laboratory tasks declined faster over time than
  performance on real-world tasks did". For accuracy the laboratory slope
  is −0.16 a month and the interaction +0.11, about −0.05 for real-world
  tasks. Real-world tasks are also more complex (p. 129).
- **Robustness** (§§5.5–5.6): paired-sample effect sizes give slopes "not
  substantially different" for accuracy and mixed measures (p. 110), and
  the author judges that publication bias "is unlikely to have
  substantially influenced the results" (p. 118).

## What this does not say

- That decay is linear at long intervals: only 14 intervals exceed a year
  (p. 64).
- That the rates hold for skills without a motor component, or for teams
  and organizations rather than individuals under test.
- That practice slows decay in general: the moderator is a coarse code,
  significant for accuracy only, and the moderators are "far from
  definitive" (p. 128).
- That real-world skills decline at the pooled rate: laboratory tasks
  decline faster than real-world ones (Appendix C).
- That an occasional test keeps a skill better at every interval: the
  opportunity changes the slope, and the level starts lower.
- That the estimates are unbiased: the author argues relearning during
  retention tests makes them too low.
- Anything about measuring a capability by how often it is used.

## Note of 2026-11-06: read in full

[NOTE-1560](../notes.d/NOTE-1560.md) now reads the effect-size chapter, all of §5.3 and §§5.5–5.6.
The slopes survive a change of effect-size formula (§5.5), and the author
judges publication bias not substantial (§5.6). The practice clause is
narrowed to accuracy, as the earlier note asked. Whether an independent
synthesis agrees is [QUESTION-tmpec8ky](../questions.d/QUESTION-tmpec8ky.md).
