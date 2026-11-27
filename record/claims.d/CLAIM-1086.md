---
number: 1086
status: Proposed
formerly:
- CLAIM-tmpeonjp
title: 'Grounding as reliability under interventions'
statement: >-
  Grounding in a learning system is reliability over a family of cases
  closed under interventions that separate what makes an answer true from
  what accompanies it, so the cue-reading and stale-source cases fail
  reliability rather than a separate condition, and the work of the account
  lies in declaring the family
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A case in which a learning system's answers stay true under every
  intervention on what makes them true (its effects following, its mere
  correlates held at their own values), over the family the question
  ranges over, and the system nonetheless does not know, for a reason
  that cannot be restated as a failure under some further intervention of
  that kind: a deviant route by which the answer depends on the
  truthmaker, shown to defeat knowledge. Not defeated by a case in which
  the family was declared too narrowly, which the claim says is where the
  work lies.
tags:
- epistemology
- learning-theory
- causality
date: '2026-11-23'
line:
- learned-structure
bears_on:
- QUESTION-493
grounds:
- CASE-416
- CASE-399
summary: >-
  One of two readings of the grounding criterion in [QUESTION-493](../questions.d/QUESTION-493.md)'s
  candidate answer, filed as alternatives; this is the assistant's lean.
  The watermark classifier and the stale-source model are reliable over
  their families as declared, and fail once the family includes
  interventions on what makes the answer true. On this reading that
  failure is all grounding adds: an interventionist reading of A73's
  "connected appropriately to what makes it correct". The alternative,
  [CLAIM-1028](CLAIM-1028.md), holds grounding a further condition. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-416 CASE-399 CLAIM-1028 — Proposed; filed by the lead run of 2026-11-23 -->

# CLAIM-1086: Grounding as reliability under interventions

## The claim

[QUESTION-493](../questions.d/QUESTION-493.md)'s candidate (A73) lists three criteria for knowledge in a
learning system: truth, counterfactual reliability over a declared
family, and grounding, "knowledge must be connected appropriately to what
makes it correct". The cases of [LEAD-001](../leads.d/LEAD-001.md)'s set that separate reliable
performance from competence are [CASE-416](../cases.d/CASE-416.md) (a classifier that reads a
watermark accompanying the class) and [CASE-399](../cases.d/CASE-399.md) (a model whose true
answer comes from a training period that has ended). Both are reliable
over the family as declared, and neither knows.

On this reading what they lack is reliability over the right family. Let
the family range over interventions on what makes the answer true, with
the truthmaker's effects following and its mere correlates held at the
values they would otherwise have:

- a horse photographed outside the archive (the watermark does not
  follow, since it is not an effect of being a horse): the classifier
  fails;
- a different present executive (the training data do not follow, since
  they were fixed before): the model fails.

A system that reads an effect of the truth passes such a family, as
reading smoke for fire does, while one that reads a correlate fails it.
A73's second and third tests, intervention on spurious cues and a changed
fact with valid corrective evidence, are then the means of declaring the
family, not tests of a separate condition. Intervening on a cue alone
diagnoses whether it is an effect of the truth or a correlate; failing
that intervention is not by itself disqualifying, since forged smoke
deceives anyone who knows fire by its smoke.

So grounding is not a further property beside reliability. What the
account needs is a rule for declaring the family, and that rule is where
a theory of knowledge for learning systems does its work.

## Why the lean

It keeps the account to tests that can be run on a model, as
[QUESTION-493](../questions.d/QUESTION-493.md) asks ("whose tests could be run on a model"), and it says
what A73's tests 2 and 3 are for. The alternative must say what
"appropriately connected" adds that no intervention can show.

## What it does not say

- Not that any declared family will do: a family declared over the
  training distribution alone gives the wrong verdicts on both cases.
- Not that the truthmaker can always be identified independently of the
  question; where it cannot, this reading inherits the difficulty, and
  [CLAIM-1028](CLAIM-1028.md) presses exactly there.
- Not a verdict on environmental luck, where the actual family is full of
  forgeries: the reading gives knowledge where reliability over the
  actual family holds and denies it where it does not.

## Note of 2026-11-27: Gupta, Liu and Zou, read

<!-- inactive-ok-block: THEORY-tmpjgsul — new; the reading of Gupta, Liu and Zou and its account -->

[THEORY-tmpjgsul](../theory.d/THEORY-tmpjgsul.md) corroborates this claim with interventions of the kind it names. Each of CogLoadBench's factors keeps what makes the answer true and changes what accompanies it ([NOTE-tmpanw10](../notes.d/NOTE-tmpanw10.md)). Reliability over the family that includes those changes fails, most of all for analogies under similar distractors, where accuracy falls from 52.3 to 21.0.
