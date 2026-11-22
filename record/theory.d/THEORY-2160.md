---
number: 2160
status: Proposed
formerly:
- THEORY-tmpr9w2r
title: 'Hoogland and colleagues find that in a two-layer attention-only language transformer of about 3.4 million parameters and a two-layer in-context linear-regression transformer of about 52 thousand, plateaus in SGLD estimates of the local learning coefficient over log training time divide training into five stages, four or five of which recur in each of five seeds, and most stages coincide with independently measured changes in behaviour or structure; the estimate rises in most stages and falls in three'
promote_when: >-
  An independent run of either setting, with the authors' code or a
  reimplementation, recovers the coefficient-plateau boundaries of LM1–LM4
  or LR1–LR4 and the same behavioural or structural markers inside each
  stage, including at least one stage in which the estimate falls.
version: 1
tags:
- learning-theory
- loss-landscapes
date: '2026-11-21'
source:
- LIT-2966
bears_on:
- QUESTION-518
- QUESTION-511
- QUESTION-217
- QUESTION-039
summary: >-
  Hoogland, Wang, Farrugia-Roberts, Carroll, Wei and Murfet, [LIT-2966](../literature.d/LIT-2966.md),
  read in [NOTE-2248](../notes.d/NOTE-2248.md). Stages of transformer training read off pauses in
  the local learning coefficient, matched to behavioural and structural
  changes. Motivated by Bayesian singular learning, not derived from it;
  the coefficient's decreases are unexplained; the estimator is run at one
  fixed nβ and γ per setting.
---
<!-- inactive-ok-file: THEORY-2191 LIT-3049 — Proposed or Deferred; the reading of Lee et al. filed 2026-11-22, and Carroll et al., registered from it and unread -->

# THEORY-2160: Hoogland and colleagues find that in a two-layer attention-only language transformer of about 3.4 million parameters and a two-layer in-context linear-regression transformer of about 52 thousand, plateaus in SGLD estimates of the local learning coefficient over log training time divide training into five stages, four or five of which recur in each of five seeds, and most stages coincide with independently measured changes in behaviour or structure; the estimate rises in most stages and falls in three

## Source

Hoogland, Wang, Farrugia-Roberts, Carroll, Wei and Murfet, "Loss Landscape
Degeneracy and Stagewise Development in Transformers", [LIT-2966](../literature.d/LIT-2966.md), read from
arXiv 2402.02364v3 (to appear in TMLR) in [NOTE-2248](../notes.d/NOTE-2248.md).

## What was actually shown

- Stage boundaries at plateaus of λ̂ over log t (§5); five stages per
  setting.
- In each of five seeds, LM1–LM4 and LR1–LR5 recur (B.4).
- Most stages coincide with independently measured changes: bigrams,
  n-grams, previous-token heads, induction heads; context-free prediction,
  in-context learning, loss of out-of-distribution robustness with
  layer-norm collapse (§§6–7); LM5 and LR5 uninterpreted.
- Δλ̂ negative in LM3 (−1.57), LR3 (−12.3) and LR4 (−44.1) (Fig. 1).
- The Hessian's trace and top eigenvalue miss three of four LR boundaries
  (B.5).

What could have failed: the plateaus could have fallen nowhere near the
behavioural changes, or moved between seeds; they did not, in these two
settings.

## What this does not say

- Not that stages are changes of the dominant singular region: the
  Bayesian singular learning process is an analogy whose link to training
  "remains to be understood" (§5).
- Not why the coefficient falls: "an open problem" (§8).
- Not causal, and not universal (§8).
- Not robust to the estimator's settings: nβ (21.7 or 66.7, not
  n/log n) and γ are fixed per setting, and no division under other values
  is reported.

## Note of 2026-11-22: Lee, Smith, Adam and Hoogland, read

A parallel that extends the method. Lee et al. ([THEORY-2191](THEORY-2191.md)), from
the same group, use the same localized SGLD at checkpoints, swapping the
LLC for a per-sample covariance, and match their language-model stages
to the same structures, induction heads among them. They cite this
work's TMLR version, with Carroll et al. 2025 ([LIT-3049](../literature.d/LIT-3049.md)), for
Type-A and Type-B Bayesian transitions, the second an equal-loss
transition with a falling LLC, which is a name for the decreases this
reading reports ([QUESTION-518](../questions.d/QUESTION-518.md)). Neither supports nor contradicts the
reading's sentence.
