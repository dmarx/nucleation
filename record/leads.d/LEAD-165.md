---
number: 165
status: Open
formerly:
- LEAD-tmptx3gm
title: 'Run the language-model experiments on frame commutation and on in-context learning against test-time training'
version: 1
stage: specified
priority: medium
method:
- empirical
tags:
- philosophy-of-language
- representation-learning
date: '2026-11-19'
line:
- pragmatic-transport
advances:
- CLAIM-074
- CLAIM-118
- CLAIM-085
- CLAIM-117
operationalized_in:
- CASE-005
summary: >-
  Named in [CLAIM-074](../claims.d/CLAIM-074.md). Filed by the backlog audit of 2026-11-19.
---

# LEAD-165: Run the language-model experiments on frame commutation and on in-context learning against test-time training

## What it would do

Run [CASE-005](../cases.d/CASE-005.md)'s experiments with current open models; experiment 3 compares
adaptation by context with adaptation by test-time training on measured
fidelity.

Where the record names it:

- [CLAIM-074](../claims.d/CLAIM-074.md): "Experiment 3 of [CASE-005](../cases.d/CASE-005.md) would test it."

## What would count

Fidelity that depends on the adaptation route supports [CLAIM-074](../claims.d/CLAIM-074.md); none
defeats it. Both [CLAIM-074](../claims.d/CLAIM-074.md) and [CLAIM-118](../claims.d/CLAIM-118.md) also wait on the owner's ruling
on test-time training.

## Note of 2026-11-26: von Oswald et al. (2023), read


Bears on the design of experiment 3. In [LIT-3313](../literature.d/LIT-3313.md) ([NOTE-2426](../notes.d/NOTE-2426.md)), in
synthetic sequences, in-context learning is itself an inner optimization
of fast weights, and the mesa-layer is a test-time learner inside a
layer. An ICL arm and a TTT arm may therefore differ in where the learned
state is kept, not in kind, as [THEORY-169](../theory.d/THEORY-169.md) says. The experiment's contrast
should be stated by what each arm retains across sequences ([CLAIM-118](../claims.d/CLAIM-118.md),
[CLAIM-074](../claims.d/CLAIM-074.md)), not by mechanism. No change of stage.
