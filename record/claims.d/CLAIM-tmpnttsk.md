---
status: Proposed
title: 'A holistic fidelity judgement is fidelity under the judges'' default task, a weighting of the profile''s components that can be estimated on some renderings and tested on others, so it is well defined and consistent with task-relativity, and a defeat condition that uses it must name the population and fix the weighting before the test'
version: 1
role: thesis
defeated_if: >-
  No weighting of the fidelity profile's components fitted on one set of
  renderings and judges predicts the holistic judgements of the same
  population on another set better than the best single component does,
  so that holistic judgements are not a weighting of the profile at all.
tags:
- psychometrics
- philosophy-of-language
date: '2026-10-10'
line: pragmatic-transport
objects_to:
- CLAIM-tmpqfgjl
complements:
- CLAIM-128
uses:
- TERM-043
summary: >-
  The record's reply, on 2026-10-10, to [CLAIM-tmpqfgjl](CLAIM-tmpqfgjl.md). Task-relativity
  ([CLAIM-128](CLAIM-128.md)) denies a ranking that holds across tasks, not that a
  population has a default task. A weighting estimated on held-in data
  and tested on held-out data is a finding, not a fit, and a weighting
  fixed before the test leaves no room to blame the task after a
  failure. A proposal: whether holistic judgements are such a weighting
  is itself empirical. The objection is right that the stated defeat
  conditions name neither task nor receivers; [CLAIM-tmpc1o4m](CLAIM-tmpc1o4m.md),
  [CLAIM-tmp3wo5j](CLAIM-tmp3wo5j.md) and [QUESTION-tmppstva](../questions.d/QUESTION-tmppstva.md) address that.
---
<!-- inactive-ok-file: CLAIM-128 CLAIM-074 CLAIM-106 CLAIM-115 CLAIM-139 — Proposed; open, and cited as the relativity thesis this reconciles and the theses whose conditions it bears on, not as settled -->
<!-- inactive-ok-file: CLAIM-tmpqfgjl — Proposed; the objection this entry answers, left open until the owner decides on the revised theses -->
<!-- inactive-ok-file: CLAIM-tmpc1o4m CLAIM-tmp3wo5j — Proposed; the record's revised theses of 2026-10-10, open -->

# CLAIM-tmpnttsk: A holistic fidelity judgement is fidelity under the judges' default task, a weighting of the profile's components that can be estimated on some renderings and tested on others, so it is well defined and consistent with task-relativity, and a defeat condition that uses it must name the population and fix the weighting before the test

## The claim

This is the record's reply of 2026-10-10 to [CLAIM-tmpqfgjl](CLAIM-tmpqfgjl.md). It reconciles
the objection's dilemma rather than refuting it, and it is a proposal: that
holistic judgements behave as the claim says is something a study can find
false.

[CLAIM-tmpqfgjl](CLAIM-tmpqfgjl.md) says the line must choose. Either the criterion in the defeat
conditions (one holistic judgement of fidelity) is well defined, and the
relativity theses ([CLAIM-128](CLAIM-128.md), [CLAIM-074](CLAIM-074.md), [CLAIM-106](CLAIM-106.md)) are in trouble; or they
are right, and the criterion is not well defined. The dilemma is not forced.

[CLAIM-128](CLAIM-128.md) says that "no single ranking of translations holds across tasks".
It does not say that a population of judges, asked "how faithful?", brings
no task to the question. A population can have a default task, the one its
members assume when none is stated, and that task fixes a weighting of the
profile's components ([TERM-043](../terms.d/TERM-043.md)). Holistic fidelity is then fidelity under that
weighting. It is one task among many, which is what [CLAIM-128](CLAIM-128.md) allows.

**The model.** For a rendering r with profile components D_1(r), …, D_k(r),
the holistic judgement J(r) of population P is modelled as

J(r) ≈ g(w_1 D_1(r) + … + w_k D_k(r)),

with g a decreasing link (more distortion, less fidelity) and the weights w
estimated on one set of renderings A, judged by one sample of judges from P,
and then tested on another set B judged by other judges from P.

**A worked case, O04's own.** Two components: D_f, the loss of footing, and
D_s, the loss of stance, each on [0, 1]; take g(x) = 1 − x. Rendering A keeps
footing and loses stance: D_f(A) = 0, D_s(A) = 1. Rendering B keeps stance and
loses footing: D_f(B) = 1, D_s(B) = 0. Suppose the held-in renderings give
w_f = 0.7, w_s = 0.3. Then

- J(A) = 1 − (0.7 · 0 + 0.3 · 1) = 1 − 0.3 = 0.7,
- J(B) = 1 − (0.7 · 1 + 0.3 · 0) = 1 − 0.7 = 0.3,

so the weighting predicts that P's judges rank A above B, before they see
either. If held-out judges from P rank B above A, the prediction fails.

**The two horns.**

- *Circular.* The objection's first horn is that the weights are fitted to
  the criterion. They are, on A. They are not on B, where they are fixed
  before the judgements are seen, so predicting B is a finding and not a fit.
- *Unfalsifiable.* The second horn is that a mismatch can be blamed on the
  judges having weighed for a different task. A defeat condition that names P
  and the preregistered w leaves no room for that: if P's judges on B depart
  from the fixed w, the thesis that used them failed, and changing w after
  the data is not allowed.

So the criterion is well defined (as fidelity under P's default task), and
the relativity theses stand (another task, another weighting).

**What would show it wrong.** If no weighting fitted on A predicts the
holistic judgements on B better than the best single component does, then
holistic judgements are not a weighting of the profile, and the reconciliation
fails. That is the defeat condition.

## What it answers

[CLAIM-tmpqfgjl](CLAIM-tmpqfgjl.md)'s dilemma, and its second suggested answer ("weights estimated
from one set of renderings and judges and tested on another"), which this
entry adopts. What the objection is right about, that the stated conditions
name no task and no receivers, is met by restatement in [CLAIM-tmpc1o4m](CLAIM-tmpc1o4m.md) and
[CLAIM-tmp3wo5j](CLAIM-tmp3wo5j.md), and held open in [QUESTION-tmppstva](../questions.d/QUESTION-tmppstva.md). [CLAIM-115](CLAIM-115.md)'s and [CLAIM-139](CLAIM-139.md)'s
own conditions are unchanged.

## What it does not say

- It does not say holistic judgements are the right criterion. The revised
  thesis [CLAIM-tmpc1o4m](CLAIM-tmpc1o4m.md) uses a task-indexed behavioural one, and keeps
  holistic ratings as a secondary outcome.
- It does not say P's default weighting is privileged. It is one task's.
- It does not say the link is linear or the components fixed. The model's
  form is part of what the preregistration fixes.
