---
number: 1029
status: Active
formerly:
- THEORY-tmpnu6ih
title: 'On a three-layer parenthesis-balance classifier, causal-scrubbing hypotheses that resample the terms of one head''s input separately scored 81% and 84% of the loss recovered against 77% for the less specific hypothesis they refine, and the authors attribute the rise to resampling washing out a signal, not to a better explanation'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-1195, the reading of the paren-balance post
    in full. One study, and the title claims only what it measured: three
    scores with their standard errors and the authors' stated
    explanation (ADR-047 v3). Its mechanism is the one the main post's §7
    and the appendix post's §6.1 argue in general (NOTE-1168, C6), which
    this is the measured case of.
tags:
- causality
- representation-learning
date: '2026-10-27'
source:
- LIT-1580
- LIT-1583
summary: >-
  Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt, Lin et al. (2022),
  [LIT-1580](../literature.d/LIT-1580.md), read in [NOTE-1195](../notes.d/NOTE-1195.md). Hypothesis 3a resamples head 2.1's
  input separately at each of up to 40 positions and recovers 77% (loss
  0.97 ± 0.06). Hypotheses 3c and 3d also split each position's input into
  terms drawn from different inputs, and recover 84% (0.69 ± 0.05) and 81%
  (0.81 ± 0.05). The authors call the two results not legitimate. It does
  not say how often this happens in other models, nor that the adversary
  they propose would remove it.
---
<!-- inactive-ok-file: CLAIM-454 — Proposed; the claim this bears on, cited as open -->

# THEORY-1029: On a three-layer parenthesis-balance classifier, causal-scrubbing hypotheses that resample the terms of one head's input separately scored 81% and 84% of the loss recovered against 77% for the less specific hypothesis they refine, and the authors attribute the rise to resampling washing out a signal, not to a better explanation

## Source

Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt, Lin, Nitishinskaya,
Radhakrishnan, Shlegeris and Thomas (2022), *Causal scrubbing: results on
a paren balance checker*, [LIT-1580](../literature.d/LIT-1580.md), read in full in [NOTE-1195](../notes.d/NOTE-1195.md):
Experiment 3 and the appendix sections "Sampling unimportant inputs" and
"Breaking up Experiment 3 by term". The general argument is in the
appendix post, [LIT-1583](../literature.d/LIT-1583.md) (§§4.1, 6.1 and 8).

## What was actually shown

**The setting.** Head 2.1 of a small bidirectional transformer is
hypothesized to check, at every position i, that the suffix from i
holds no more open than close parentheses. The model needs only one
failing position to call a string unbalanced.

**The three hypotheses.**

- **3a** claims that 2.1's input at position i matters only through the
  horizon test at i. Each position's input is resampled from a string
  that agrees on that test, independently across positions: 77%
  recovered, loss 0.97 ± 0.06. The authors know the horizon test is not
  quite what the model computes there. Sampling up to 40 independent
  inputs therefore usually draws at least one that carries some
  unbalanced signal anyway.
- **3c** claims further that the input at i matters only through three of
  its terms (attention layer 0, MLP 0 and MLP 1). Each term is drawn from
  a different string agreeing on the test, and the rest from a random
  string: 84%, 0.69 ± 0.05.
- **3d**, intermediate, keeps the sum of the three terms together and
  resamples the remaining terms at random: 81%, 0.81 ± 0.05.

The more specific hypotheses permit strictly more swaps. On the method's
own logic they should score no better, and they score 4 to 7 points
higher. Treating the stated standard errors as independent, the loss
differences are 3.6 (3c) and 2.1 (3d) standard errors (record
arithmetic; the post does not say whether the runs share samples).

**The authors' explanation.** "Sampling the terms of x2[i] is enough to
'wash out' this unbalanced signal in some cases." A hypothesis that
permits sampling the terms separately also permits sampling them
together, and an adversary entitled to request the latter would recover
3a. "Are the results of experiment 3c and 3d legitimate then? We think
not." Running 3d with layer 1's terms sampled together across positions
"hurt our scrubbed model's loss".

## What this does not say

- **Not that specificity always raises the score.** In the same post, the
  other refinements lower it (1b to 2a, 1b to 3a), as the method expects.
- **Not a frequency.** One model, one task, one run of 2,000 scrubbed
  samples per hypothesis.
- **Not that the adversary fixes it.** The adversary is proposed, not run.
  The appendix post's §8 says the authors do not know how to handle an
  adversary whose rewrite is incompatible with the hypothesis.
- **Not that 3c and 3d are false.** They may be true of the model. What
  is shown is that their higher score is not evidence that they are.

## Connections

- **[NOTE-1168](../notes.d/NOTE-1168.md) and [THEORY-978](THEORY-978.md).** The main post's §7 says breaking a
  correlation can make a hypothesis score higher. This is that case,
  measured. [THEORY-978](THEORY-978.md) is about ties between hypotheses that induce the
  same partition. This is a different failure: a hypothesis that permits
  more swaps scoring above one that permits fewer.
- **[CLAIM-454](../claims.d/CLAIM-454.md).** A score that rises with an illegitimate refinement is
  one more way a passing explanation can certify less than the variable
  that does the work.
