---
number: 1120
status: Proposed
formerly:
- THEORY-tmp0k3ls
promote_when: >-
  A study in which at least two native raters per language independently
  score the pragmatic adequacy of the same translations, with their
  agreement reported, and in which a reference-based metric's correlation
  with the raters' mean is reported against that inter-rater ceiling, per
  phenomenon, on items chosen in advance rather than picked after the
  fact. A correlation with one rater per language does not settle it.
title: 'For LLM translations of culturally loaded Indic utterances into English, the reference-based COMET metric agrees with a native speaker''s pragmatic-adequacy rating at r ≈ 0.81 overall, better than XCOMET or MetricX, yet scores some pragmatically inverted outputs highly'
version: 1
tags:
- translation
- pragmatics
date: '2026-10-29'
source:
- LIT-1817
summary: >-
  Singh et al. (2026), [LIT-1817](../literature.d/LIT-1817.md), read in [NOTE-1345](../notes.d/NOTE-1345.md). On 416 outputs
  (104 items × 4 models), wmt22 COMET correlates with 1–5 pragmatic-adequacy
  scores at Pearson 0.813, Spearman 0.860; XCOMET ρ 0.792, MetricX ρ 0.788
  (Table 3). Four hand-picked outputs scored 0.65–0.86 by COMET and 1–2 by
  the rater. Each language had one rater, so there is no reliability
  against which to read 0.81, and the claim that metrics fail "especially
  for implicature and deixis" rests on per-phenomenon differences of 0.1
  or less.
---

# THEORY-1120: For LLM translations of culturally loaded Indic utterances into English, the reference-based COMET metric agrees with a native speaker's pragmatic-adequacy rating at r ≈ 0.81 overall, better than XCOMET or MetricX, yet scores some pragmatically inverted outputs highly

## Source

Singh et al. (2026), [LIT-1817](../literature.d/LIT-1817.md), §5.4, Table 3, Table 4 and App. A.2–A.3,
pp. 43034–43040 of the Findings of EMNLP 2026; read in [NOTE-1345](../notes.d/NOTE-1345.md).

## What was actually shown

104 of the 204 translation items (Hindi 31, Punjabi 26, Tamil 23, Malayalam
24) were translated into English by four models. One native rater per
language scored each output 1–5 on a rubric that asks whether "Pragmatic
intent" is preserved, "including tone, implicature, and cultural nuance"
(Table 4), told "not to reward fluent outputs that missed the implied
meaning" (App. A.2, p. 43039). Against these 416 scores, COMET (wmt22-da)
gave Pearson r = 0.813 and Spearman ρ = 0.860, XCOMET r 0.80, ρ 0.79,
MetricX r 0.73, ρ 0.79 (Table 3). By language, COMET's r ran from 0.68
(Malayalam) to 0.85 (Hindi); XCOMET's ρ fell to 0.54 on Hindi. By
phenomenon, COMET's ρ was lowest on Deixis (0.81) and Implicature (0.83),
its r lowest on Speech Acts (0.76).

App. A.3 shows four outputs where COMET gave 0.65–0.86 and the rater 1 or 2:
a Malayalam "don't come here" rendered "Come here", a Punjabi insult with
subject and object swapped, a misanchored "parso", a perfective rendered as
future.

What could have failed: COMET could have correlated weakly with a rater
told to ignore fluency. It did not; most of the variance it misses is
unexplained.

## What this does not say

- **How good 0.81 is.** With one rater per language there is no inter-rater
  ceiling; a second rater might agree with the first no better than COMET
  does.
- **That metrics fail "especially for implicature and deixis"** in any
  measured sense. The per-phenomenon correlations differ by 0.1 or less on
  about 80 outputs each, and the divergence cases were picked after the
  fact.
- **That a fluent translation misses meaning the same model could infer.**
  The translation items are not the MCQ or NLI items.
- **Anything about xCOMET as a fidelity criterion in general** ([LIT-1816](../literature.d/LIT-1816.md)).
  It concerns four Indic languages into English, against one reference each.
