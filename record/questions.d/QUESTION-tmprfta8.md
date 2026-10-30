---
status: Open
title: 'Does a learned translation metric trained on synthetic hallucinations and perturbations detect errors and hallucinations from real systems, in pairs and kinds its training did not synthesise, as well as its synthetic tests report?'
version: 1
tags:
- translation
date: '2026-10-30'
line: pragmatic-transport
summary: >-
  The promotion condition formerly on THEORY-1151, moved here when the
  twenty-second status review promoted that reading of xCOMET's §7
  (ADR-065). The paper measured detection on synthetic perturbations and
  one benchmark; whether its robustness generalises past what its training
  synthesised is this question.
---

# QUESTION-tmprfta8: Does a learned translation metric trained on synthetic hallucinations and perturbations detect errors and hallucinations from real systems, in pairs and kinds its training did not synthesise, as well as its synthetic tests report?

## Why it is a question

THEORY-1151 holds what Guerreiro et al. (2024), LIT-1816, measured: xCOMET
flags most injected localized errors and ranks fully detached
hallucinations low. But its training data included synthetic detached and
oscillatory hallucinations and DEMETR's diagnostic perturbations, the
localized errors were SMAUG perturbations of English targets only, and the
hallucinations came from one de-en benchmark. The authors give the
synthetic training data as "one plausible hypothesis" for the gains and do
not claim that detection generalises. Whether it does is open.

## What would answer it

Tests on errors and hallucinations produced by real translation systems in
language pairs and kinds the training data did not synthesise (for
instance a multilingual hallucination benchmark, or naturally occurring
number and entity errors with human labels), showing whether detection
stays at the level the synthetic tests report. Results on more synthetic
perturbations of the trained kinds do not settle it.
