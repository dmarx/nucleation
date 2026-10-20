---
number: 806
status: Proposed
formerly:
- THEORY-tmpliiy2
promote_when: 'A proof of the same kind of bound outside the uniform, lossless models: for non-uniform (for instance Zipfian) source languages, or for lossy translators, an error bound that still falls in the common ground and in the size of the source language, with a lower bound to match. Or an experiment on real corpora in which the error of prior-scored translation without parallel data falls with measured common ground at the predicted rate. It is refuted for natural settings by a non-uniform model in which richer source languages do not reduce the common ground needed. What cannot settle it: further synthetic runs in the same two models, which only confirm the proofs.'
title: Translation without parallel data, as of an unknown animal communication system into a human language, is learnable from a plausibility prior over the target language alone, with error falling as the common ground between the languages grows and as the source language grows richer
version: 1
tags:
- translation
- learning-theory
- information-theory
date: '2026-10-20'
source:
- LIT-941
summary: The general reading that [THEORY-270](THEORY-270.md) held before the promotion audit narrowed it to the common-nonsense model its bound is proved in (batch 044). Goldwasser, Gruber, Kalai and Paradise (NeurIPS 2023), [LIT-941](../literature.d/LIT-941.md), read in [NOTE-804](../notes.d/NOTE-804.md), motivate their framework by translating animal communication and state its lesson for translation in general, while saying their stylised models are not intended to capture natural language. Filed under [ADR-047](../decisions.d/ADR-047.md) v4 so the wide form stays a thesis evidence can confirm or reject.
extends:
- THEORY-270
answers:
- QUESTION-195
---

# THEORY-806: Translation without parallel data, as of an unknown animal communication system into a human language, is learnable from a plausibility prior over the target language alone, with error falling as the common ground between the languages grows and as the source language grows richer

## Source

Goldwasser, Gruber, Kalai and Paradise (NeurIPS 2023), [LIT-941](../literature.d/LIT-941.md), framed from
its title on by the translation of animal communication, §§1–4 read in
[NOTE-804](../notes.d/NOTE-804.md). The general Occam-type guarantee is Theorem A.2; the rates are
Theorems 3.2, 3.4 and 3.5 in two stylised models.

## What is asserted, and by whom

The thesis is that unsupervised translation is possible in general, not only
in the authors' models: a translator scored against a plausibility prior
over the target language alone is learnable, and the data it needs fall as
the languages share more common ground and as the source language is more
complex. The paper is framed by it, for animal communication in particular,
and ends with advice on what data to collect for whale communication.
[NOTE-804](../notes.d/NOTE-804.md) rates the general guarantee strong (C1, Theorem A.2), the rates
strong in the models and weak beyond them (C3), and prompting a language
model as the prior weak (C5).

## What the record holds toward it

- [THEORY-270](THEORY-270.md) (Active): in the common-nonsense model, with uniform languages and one-to-one translators, maximum likelihood with the prior alone has error O(log|Θ| / (α·min(m, |T|))), tight up to a constant.
- Theorem A.2 gives an Occam-type guarantee for any finite translator family and prior, but it bounds error by the prior's plausible ambiguities, which the paper sizes only in its models.

## What would confirm or reject it

A bound for non-uniform or lossy settings that still falls in common ground
and source size, or a real-corpus experiment at the predicted rate, confirms
it; a non-uniform model in which richer source languages do not reduce the
common ground needed rejects it for natural settings. [QUESTION-195](../questions.d/QUESTION-195.md) asks the
same thing as a question; this entry is the answer the authors propose.
