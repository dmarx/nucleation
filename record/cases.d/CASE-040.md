---
number: 40
status: Active
formerly:
- CASE-tmpmv9pi
title: 'Topic and act crossed: a factorial design that decorrelates what a text is about from what it does'
version: 1
standing: stipulated
tags:
- pragmatics
- psychometrics
date: '2026-10-10'
line: 'pragmatic-transport'
illustrates:
- CLAIM-129
- CLAIM-135
variant_of:
- CASE-021
- CASE-004
summary: >-
  A214 §8's design, which A218 names as the first experiment to run:
  topic (spending, relationships) crossed with act (teasing, reprimand),
  with lexical, judgement, uptake and intervention data, several
  factorizations, and four outcomes reported separately. A210 §5 gives a
  cross-corpus version. Proposed by the assistant; not run.
supports:
- CLAIM-129
---
<!-- inactive-ok-file: CLAIM-129 CLAIM-135 CLAIM-127 CLAIM-130 CLAIM-077 THEORY-175 — Proposed; open, and cited as claims and a reading the case bears on, not as settled -->

# CASE-040: Topic and act crossed: a factorial design that decorrelates what a text is about from what it does

## The case

A214 §8 crosses two factors: topic T ∈ {spending, relationships} and
pragmatic act P ∈ {teasing, reprimand}. "The important point is to avoid
perfectly correlating topic and pragmatic function. Otherwise, a topic
model may appear to recover pragmatic identity merely because the dataset
makes the two inseparable."

The four cells, as A214 labels them:

| | Teasing | Reprimand |
|---|---|---|
| Spending | Friends joking about an empty wallet | An authority figure criticizing overspending |
| Relationships | Friends affectionately teasing about romance | An authority figure condemning a relationship decision |

The data have four sources: lexical co-occurrence, interpretive judgements
("tone, stance, solidarity, and authority"), expected uptake (choices among
continuations) and intervention responses ("changes under experimentally
manipulated speaker roles, histories, or framing information"). Five models
are fitted: topic-only NMF, a factorization of the pragmatic responses, a
joint lexical and pragmatic factorization, a shared-and-private
factorization, and a richer context-sensitive model. The critical items are
held out and break the familiar correlation: "test whether the model
correctly distinguishes a joking use of admonitory vocabulary from a
serious reprimand."

There are four outcomes: reconstruction error, latent recovery,
cross-realization transfer and held-out decision performance. "These
outcomes should be reported separately."

A218 Part III makes it the first experiment: "hold topic and pragmatic act
independently variable, collect both lexical observations and human
response judgments, and compare models on cases where thematic similarity
and communicative identity disagree." A218's Study 2 adds "perturbations
that break correlations between topic and pragmatic act".

**The cross-corpus version.** A210 §5, after the owner's U58, runs the same
contrast through translation. Topic models are fitted to a source corpus
and to its translation, paraphrase or adaptation, and the two structures
are compared after each is independently anchored. There are three
possible outcomes. Topics change coordinates or labels but keep their
anchored associations. Topics "merge, split, or become less
distinguishable". Or "Topic associations appear stable while pragmatic or
causal relationships change substantially." The third would show "that
recovering thematic structure is not the same as recovering
communicative-act structure." Raw factors of the two corpora are not
comparable as they stand (A210 §4: "Their raw NMF factors are not directly
comparable"). Comparing them needs paired anchors ([THEORY-175](../theory.d/THEORY-175.md)), and without
those a flexible alignment can make any factors match ([CLAIM-077](../claims.d/CLAIM-077.md)).

## How it differs from [CASE-021](CASE-021.md)

[CASE-021](CASE-021.md) crossed wording, attributed speaker and the order of judgement
questions, with Henley's renderings as stimuli. This design drops the order
factor. It makes the act a manipulated factor rather than an outcome, where
[CASE-021](CASE-021.md) manipulated the attributed speaker and measured the judged act. It
adds collaborative-filtering baselines over interpreters. Its spending row
is [CASE-004](CASE-004.md)'s conditions A and B (shared complicity, normative authority)
in text rather than image, again without condition C.

## What it can show

If run, whether a structure identified from lexical co-occurrence carries
the act ([CLAIM-129](../claims.d/CLAIM-129.md)), and how far identification falls short of a kind
([CLAIM-135](../claims.d/CLAIM-135.md)). A synthetic form, with planted latent factors that are
recoverable, ambiguous or nonidentifiable (A214 §12, Experiment A), gives a
ground truth for [QUESTION-027](../questions.d/QUESTION-027.md).

## What it cannot show

It has not been run, and every cell is an example label, not a stimulus.
Its "intervention responses" manipulate a described speaker or history. In
a judgement study that is a framing intervention on the interpreter
([CLAIM-127](../claims.d/CLAIM-127.md), [CLAIM-130](../claims.d/CLAIM-130.md)), not a change to the performed act. So the
design can show how interpretation responds to information about the
situation, and not whether the act itself changed. Nor does a clean result
bear on the ontology. A218: "That doesn't prove OSR, but it establishes the
kind of empirical result an OSR-inspired theory should explain."
