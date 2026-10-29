---
status: Proposed
promote_when: >-
  A held-out evaluation in several languages, with gold labels from judges
  who were not screened against the classifier, items not selected on a
  score the held-out judge contributed to, and human accuracy computed by a
  stated rule, that again finds an English-trained multilingual classifier
  well above chance and well below the human figure. A comparison that
  reuses TyDiP's model-screened judges or its extreme-quartile selection
  does not settle it.
title: 'A multilingual classifier trained only on English politeness ratings separates the most from the least polite requests in nine other languages at about 81% accuracy, without translation, yet stays about 10 points below one native judge''s agreement with two others in most of them'
version: 1
tags:
- pragmatics
- linguistics
date: '2026-10-29'
source:
- LIT-tmp2g5v4
summary: >-
  Srinivasan and Choi (2022), LIT-tmp2g5v4, read in NOTE-tmpmy2mv. XLM-R
  fine-tuned on 1,926 English requests reaches 0.808 mean accuracy on the
  balanced top/bottom-quartile sets (250 per language), 0.801 on Google
  Translate input; GPT-3 zero-shot 0.706 (Table 3). Leave-one-out human
  accuracy is around 90% (Fig. 3). The judges were screened for agreeing
  with this classifier, and the extreme items were chosen on a mean that
  includes the held-out judge, so the gap and the transfer are both
  measured on favourable ground.
---

# THEORY-tmpotaav: A multilingual classifier trained only on English politeness ratings separates the most from the least polite requests in nine other languages at about 81% accuracy, without translation, yet stays about 10 points below one native judge's agreement with two others in most of them

## Source

Srinivasan and Choi (2022), LIT-tmp2g5v4, §3, Table 3 and Fig. 3,
pp. 5726–5728 of the Findings of EMNLP 2022; read in NOTE-tmpmy2mv.

## What was actually shown

XLM-R large was fine-tuned for five epochs on 1,926 English Wikipedia
requests labelled by Danescu-Niculescu-Mizil et al. (p. 5727) and tested on
each language's 250 most and least polite TyDiP requests, a balanced binary
task with majority baseline 0.5. Accuracy on target-language input: Hindi
0.868, Korean 0.784, Spanish 0.84, Tamil 0.78, French 0.82, Vietnamese 0.844,
Russian 0.668, Afrikaans 0.856, Hungarian 0.812; mean 0.808 (Table 3;
recomputed). Translating to English first gave 0.801. Human accuracy, one
judge against the mean of the other two, resampled, hovers "around 90%"
(p. 5727), and "Six out of the nine languages have a gap of at least 10%"
(p. 5727).

What could have failed: an English-trained model could have been near
chance in typologically distant languages. It was not, in any of the nine.

## What this does not say

- **That politeness is universal.** The paper says the transfer weighs "in
  the universality of politeness phenomena" (p. 5723). A classifier that
  separates extremes across languages shows shared cues at the extremes, not
  that the middle of the scale, or the same strategy, means the same.
- **That the gap to people is 10 points.** The human figure is plotted, not
  tabulated, its binarization is unstated, and the held-out judge helped
  choose the extreme items.
- **That the judges are independent of the model.** They were kept for
  agreeing with this classifier's confident predictions (p. 5725).
- **That machine translation destroys politeness.** The XLM-R difference is
  0.7 points on average and goes the other way in four languages.
