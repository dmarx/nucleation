---
number: 58
status: Proposed
formerly:
- CLAIM-tmpgqdv7
title: 'Context-conditioned language models give a controlled computational setting in which the theory''s frame, order and transport effects can be tested before human studies'
version: 2
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Restated on 2026-10-10 after CLAIM-248: version 1 fired only on
    a reversal of direction. Version 1's condition read: "Framing and
    order effects found in models fail to replicate, even in direction,
    in matched human studies, so that the models test nothing about the
    theory's claims on pragmatic interpretation."
role: thesis
warrant: interpretive
defeated_if: >-
  Across several model families and sizes, and on stimuli written after
  the models' training cut-offs as well as the famous ones, the pattern
  of framing and order effects across conditions in models fails to
  match the pattern in matched human studies (a rank correlation of
  effect sizes below a value fixed in advance), so that the models test
  nothing about the theory's claims on pragmatic interpretation.
tags:
- philosophy-of-language
- representation-learning
date: '2026-10-08'
line: pragmatic-transport
summary: >-
  A45 §8: "Put the three LLM experiments before the human-participant
  studies, positioning the former as controlled computational tests and
  the latter as external validation." The conclusion of the U17 analogy,
  limited by the circularity objection.
argued_by:
- ARG-008
---

# CLAIM-058: Context-conditioned language models give a controlled computational setting in which the theory's frame, order and transport effects can be tested before human studies

## The claim

A45 §8: "Put the three LLM experiments before the human-participant studies,
positioning the former as controlled computational tests and the latter as
external validation." A45 §10: "The crucial first experiment would be modest:
establish whether trajectory-sensitive comparisons of LLM interpretations
predict human assessments of pragmatic fidelity better than static comparisons
do." The experiments are [CASE-005](../cases.d/CASE-005.md).

Its argument is [ARG-008](../arguments.d/ARG-008.md).

## What it does not say

That a model's judgements measure human meaning (A43: "not a direct measurement
of human communicative significance"). The manuscript's programme combines
"human judgments, language models, and visual generation" (Abstract) without
ordering them this way.

## Note of 2026-10-30: what holds it back

Its one route is [ARG-008](../arguments.d/ARG-008.md). That inference is Active, but its premise
[CLAIM-029](CLAIM-029.md) is Proposed, because [CLAIM-029](CLAIM-029.md)'s own defeat condition is met as
written by [THEORY-683](../theory.d/THEORY-683.md), so the argument is not sound. Its title is also wider
than [ARG-008](../arguments.d/ARG-008.md) version 2 carries: a test bed only with generator and evaluator
separated, stimuli held out from training and agreement across model
families, and not evidence about human pragmatics. When [CLAIM-029](CLAIM-029.md) is
promoted, this claim is narrowed to those conditions in the same
contribution.
