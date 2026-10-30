---
status: Proposed
title: 'xCOMET''s error spans are more coherent with its own score than either is with expert judgement: the agreement between its heads is coherence through one encoder, not evidence that the spans explain human-judged quality'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A held-out evaluation that reports, for the same segments and on one
  scale, the agreement between the score and the spans and the agreement
  of each with expert MQM, and finds them comparable.
tags:
- translation
date: '2026-10-30'
line:
- pragmatic-transport
grounds:
- THEORY-1134
summary: >-
  The record's reading of Guerreiro et al.'s Table 5, split from
  THEORY-1134 when the twenty-second status review narrowed it to the
  measurements and promoted it (ADR-065; ADR-047 kind 2). An instance of
  CLAIM-496's distinction between coherence and fidelity. The statistics
  compared differ (Pearson between heads; Kendall and F1 against humans),
  and converted to one scale the gap is smaller than it looks.
---

# CLAIM-tmp2um57: xCOMET's error spans are more coherent with its own score than either is with expert judgement: the agreement between its heads is coherence through one encoder, not evidence that the spans explain human-judged quality

## The claim

xCOMET (LIT-1816, read in NOTE-1341) gives a sentence score and error spans
from one shared encoder. The MQM score computed from its own spans
correlates with its regression scores at Pearson 0.73 to 0.82 per pair,
and at 0.90 to 0.92 with its final score, which includes the span score
with weight 2/9 by construction (THEORY-1134). Against expert MQM its
segment-level Kendall τ is 0.39 to 0.47 and its span F1 0.24 to 0.32. The
paper presents the heads' agreement as support for the spans as an
explanation of the score. The record reads it as CLAIM-496 reads agreement
between routes: two outputs of one encoder agreeing is coherence, and its
size says nothing about how often either is right.

## How large the gap is

The figures are on different scales, and the gap is smaller than the raw
numbers suggest. Under bivariate normality Kendall's τ and Pearson's r are
related by r = sin(πτ/2), so τ of 0.390, 0.432 and 0.470 correspond to r of
about 0.58, 0.63 and 0.67. A simulation of bivariate normal pairs at those
r reproduced τ to within about 0.02 (the status review's check of
2026-10-30). Against the regression heads' 0.73 to 0.82 that is a gap, but
not a large one. The large gaps are against the final score, whose 0.90 to
0.92 is partly arithmetic, and against span F1 of about 0.28, which is not
a correlation. MQM scores are skewed and heavily tied, so the conversion is
rough. Hence "more coherent", not "far more".

## What would settle it

A held-out evaluation, on expert MQM from a domain and year the metric was
not trained near, that reports for the same segments both the agreement
between the metric's score and its own error spans and the agreement of
each with the human annotation, and finds the first reliably larger than
the second; or one that finds them comparable. Further correlations with
humans alone do not settle it, since the claim is about the gap.

## What it does not say

- **That the spans are wrong or useless.** They match human spans better
  than GPT-4 prompting did (THEORY-1134).
- **That the shared encoder is the mechanism.** That is the authors'
  hypothesis; no experiment isolates it.
