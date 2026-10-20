---
number: 195
status: Open
formerly:
- QUESTION-tmpcd93h
title: "Does prior-scored translation without parallel data keep an error bound that falls in the common ground and the size of the source language when the languages are not uniform or the translators are lossy?"
version: 1
tags:
- translation
- learning-theory
- information-theory
date: '2026-10-19'
line: 'pragmatic-transport'
summary: >-
  Filed when the promotion audit (batch 044, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted THEORY-270 to Goldwasser and co-authors' common-nonsense theorem,
  re-derived from its appendix. The former promote_when, a bound outside the
  uniform, lossless models, is held here.
---

# QUESTION-195: Does prior-scored translation without parallel data keep an error bound that falls in the common ground and the size of the source language when the languages are not uniform or the translators are lossy?

## Why it is a question

[THEORY-270](../theory.d/THEORY-270.md) now states the upper bound of [LIT-941](../literature.d/LIT-941.md)'s common-nonsense model:
maximum likelihood with a plausibility prior and no parallel data has
error O(log|Θ| / (α·min(m, |T|))) when source and prior are uniform over
sets from which shared random nonsense is removed and the translators are
one-to-one. The bound is proved, and was re-derived. The models are
uniform and random by design and, in the paper's words, "not intended to
accurately capture natural language". Whether the exchange between common
ground, source size and samples survives outside them is open.

## What would answer it

A proof of the same kind of bound for non-uniform (for instance Zipfian)
source languages, or for lossy translators, with an error that still falls
in the common ground and the size of the source language and a lower bound
to match, would answer it yes. So would an experiment on real corpora in
which the error of prior-scored translation without parallel data falls
with measured common ground at the predicted rate. A non-uniform model in
which richer source languages do not reduce the common ground needed would
answer it no. Further synthetic runs in the paper's two models cannot
settle it: they only confirm the proofs.
