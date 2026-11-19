---
number: 9
status: Done
formerly:
- LEAD-tmpn5ruw
title: 'Read the pretraining works that measure what the owner said the literature ought to show: Brown and colleagues on few-shot in-context learning (GPT-3) and Howard and Ruder on sample-efficient fine-tuning (ULMFiT)'
version: 2
history:
- version: 2
  date: '2026-11-19'
  note: >-
    Done: both works read the same day (LIT-2859, NOTE-2160,
    THEORY-2062; LIT-2852, NOTE-2141, THEORY-2084). The
    plan overstated what Brown and colleagues measure: accuracy against
    the number of examples by model size, not examples to a level, and
    across sizes at fixed pretraining, not with and without it.
stage: underway
method:
- reading
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
line:
- learned-structure
advances:
- CLAIM-756
- QUESTION-493
summary: >-
  The owner's suggestion of 2026-11-19, after the readings of McDermott
  and colleagues and Anguita and colleagues did not show acquired
  organization making later learning cheaper in cost terms: invoke the GPT
  paper showing pretraining enables few-shot in-context learning. Howard
  and Ruder added as the work that measures labelled-sample cost directly.
  Neither is held.
---
<!-- inactive-ok-file: THEORY-2062 THEORY-2084 CLAIM-756 TERM-131 — Proposed or newly filed; cited in this filing of 2026-11-19 -->

# LEAD-009: Read the pretraining works that measure what the owner said the literature ought to show: Brown and colleagues on few-shot in-context learning (GPT-3) and Howard and Ruder on sample-efficient fine-tuning (ULMFiT)

## What would be done

Register and read Brown and colleagues, "Language Models are Few-Shot
Learners" (2020), and Howard and Ruder, "Universal Language Model
Fine-tuning for Text Classification" (2018).

## What would count

For [CLAIM-756](../claims.d/CLAIM-756.md)'s premise in cost terms: a measured fall, due to
pretraining, in the examples or gradient steps needed to reach a level
on a new task. Brown and colleagues measure how few examples in context
reach a level, and how that changes with scale; Howard and Ruder compare
labelled examples needed with and without pretraining.

A question the reading must settle: few-shot prompting changes no
weights, so whether it is learning in [TERM-131](../terms.d/TERM-131.md)'s sense, an
experience-dependent change in retained organization, is open. It may be
the operational frontier reaching further, not acquisition. That bears on
[QUESTION-493](../questions.d/QUESTION-493.md) as well.

## Cost

Two readings.

## What came of it

Howard and Ruder measure what the owner's point at U37 needed: with 100
labelled examples a pretrained and fine-tuned model matches training from
scratch on ten to twenty times more labels, a hundred times with
unlabelled text. The saving is joint with their fine-tuning method, and
pretraining is not counted as cost. Brown and colleagues show larger
pretrained models using in-context examples more efficiently, across
sizes rather than against no pretraining, and the plan's claim that they
measure examples to a level was too strong. In-context learning changes
no weights; whether it is learning in [TERM-131](../terms.d/TERM-131.md)'s sense is now argued in
the note on that term. Notes on [CLAIM-756](../claims.d/CLAIM-756.md), [TERM-131](../terms.d/TERM-131.md) and the entries the
readings bear on carry the rest (curation entry of 2026-11-19, 202220).
