---
number: 240
status: Proposed
formerly:
- CLAIM-tmpnttsk
title: 'A holistic fidelity judgement is fidelity under the judges'' default task, a weighting of the profile''s components that can be estimated on some renderings and tested on others, so it is well defined and consistent with task-relativity, and a defeat condition that uses it must name the population and fix the weighting before the test, and across populations with unequal access to the source must fit the weighting only on the components each can perceive'
version: 3
history:
- version: 2
  date: '2026-10-27'
  note: >-
    Note of 2026-10-27 added: the limit recorded in the note of
    2026-10-10, access and not weighting, is filed as the objection
    CLAIM-458. The claim is unchanged.
- version: 3
  date: '2026-10-30'
  note: >-
    Revised to concede CLAIM-458 (ADR-059), on its promotion at the
    seventeenth status review, at the status review's ruling (the owner
    delegated these rulings): the limit recorded in the note of
    2026-10-10, that across populations with unequal access to the
    source part of a split is access and not weighting, is now in the
    title. Version 2's title read: 'A holistic fidelity judgement is
    fidelity under the judges' default task, a weighting of the
    profile's components that can be estimated on some renderings and
    tested on others, so it is well defined and consistent with
    task-relativity, and a defeat condition that uses it must name the
    population and fix the weighting before the test'. Status
    unchanged.
role: thesis
warrant: interpretive
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
- CLAIM-244
complements:
- CLAIM-128
uses:
- TERM-043
summary: >-
  The record's reply, on 2026-10-10, to [CLAIM-244](CLAIM-244.md). Task-relativity
  ([CLAIM-128](CLAIM-128.md)) denies a ranking that holds across tasks, not that a
  population has a default task. A weighting estimated on held-in data
  and tested on held-out data is a finding, not a fit, and a weighting
  fixed before the test leaves no room to blame the task after a
  failure. A proposal: whether holistic judgements are such a weighting
  is itself empirical. The objection is right that the stated defeat
  conditions name neither task nor receivers; [CLAIM-220](CLAIM-220.md),
  [CLAIM-204](CLAIM-204.md) and [QUESTION-075](../questions.d/QUESTION-075.md) address that.
illustrated_by:
- CASE-067
---
<!-- inactive-ok-file: CLAIM-128 CLAIM-074 CLAIM-115 CLAIM-139 — Proposed; open, and cited as the relativity thesis this reconciles and the theses whose conditions it bears on, not as settled -->
<!-- inactive-ok-file: CLAIM-244 — Proposed; the objection this entry answers, left open until the owner decides on the revised theses -->
<!-- inactive-ok-file: CLAIM-220 CLAIM-204 — Proposed; the record's revised theses of 2026-10-10, open -->

# CLAIM-240: A holistic fidelity judgement is fidelity under the judges' default task, a weighting of the profile's components that can be estimated on some renderings and tested on others, so it is well defined and consistent with task-relativity, and a defeat condition that uses it must name the population and fix the weighting before the test, and across populations with unequal access to the source must fit the weighting only on the components each can perceive

## The claim

This is the record's reply of 2026-10-10 to [CLAIM-244](CLAIM-244.md). It reconciles
the objection's dilemma rather than refuting it, and it is a proposal: that
holistic judgements behave as the claim says is something a study can find
false.

[CLAIM-244](CLAIM-244.md) says the line must choose. Either the criterion in the defeat
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

[CLAIM-244](CLAIM-244.md)'s dilemma, and its second suggested answer ("weights estimated
from one set of renderings and judges and tested on another"), which this
entry adopts. What the objection is right about, that the stated conditions
name no task and no receivers, is met by restatement in [CLAIM-220](CLAIM-220.md) and
[CLAIM-204](CLAIM-204.md), and held open in [QUESTION-075](../questions.d/QUESTION-075.md). [CLAIM-115](CLAIM-115.md)'s and [CLAIM-139](CLAIM-139.md)'s
own conditions are unchanged.

## What it does not say

- It does not say holistic judgements are the right criterion. The revised
  thesis [CLAIM-220](CLAIM-220.md) uses a task-indexed behavioural one, and keeps
  holistic ratings as a secondary outcome.
- It does not say P's default weighting is privileged. It is one task's.
- It does not say the link is linear or the components fixed. The model's
  form is part of what the preregistration fixes.

## Note of 2026-10-10: a documented case

[CASE-067](../cases.d/CASE-067.md), found by a search the owner asked for, illustrates this
claim with a documented reception split over one translation, Deborah
Smith's *The Vegetarian*. Each side's default task is stated in print: the
Booker judges evaluate "the finished English-language work on their own
terms", and assessment in Korea "does usually involve comparison". One
critic, Charse Yun, gives two verdicts on one set of perceived features by
changing task. It does not test the defeat condition: it is qualitative,
and no weights can be fitted.

It also shows a limit of the model. Part of the split is access, not
weights. Some divergences, such as the confusion of "arm" (pal) and "foot"
(bal), are invisible to readers without Korean ("Most English readers will
simply glide over them unaware"). For those components the Anglophone
weight is zero by blindness, not by a default task. A test of this claim
across populations with unequal access to the source has to separate the
components both populations can perceive from those only one can, and fit
weights on the first kind only.

## Note of 2026-10-27: the limit filed as an objection

The limit the note of 2026-10-10 recorded, that part of a reception split
between populations with unequal access is access and not weighting, is
filed as [CLAIM-458](CLAIM-458.md), a counter, Proposed. A test of this claim across
such populations meets it by fitting weights only on the components both
can perceive. The claim is unchanged.

## Note of 2026-10-30: what holds it back

The result its own text says decides it is missing: no weighting of the
profile's components has been fitted on one set of renderings and judges
and tested on another set from the same population against the best single
component. [CASE-067](../cases.d/CASE-067.md) is qualitative.
