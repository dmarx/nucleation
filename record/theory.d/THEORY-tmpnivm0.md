---
status: Proposed
title: 'Min and colleagues show that fine-tuning a 770M-parameter language model on many tasks presented as few-shot episodes makes it better at learning held-out classification and multiple-choice tasks in context, without parameter updates, than the same model without such training or trained on the same tasks without demonstrations, with the largest gains on targets unlike the training tasks and with diverse training tasks mattering most'
version: 1
source:
- LIT-tmp7ge7b
tags:
- representation-learning
- learning-theory
date: '2026-11-19'
corroborates:
- CLAIM-118
promote_when: >-
  An independent replication, on another base model or another collection
  of held-out tasks, finds that meta-training in the in-context format
  beats both plain in-context learning and multi-task zero-shot transfer
  from the same tasks on held-out targets.
summary: >-
  From the reading of [LIT-tmp7ge7b](../literature.d/LIT-tmp7ge7b.md) in [NOTE-tmpbyao9](../notes.d/NOTE-tmpbyao9.md). Min, Lewis,
  Zettlemoyer and Hajishirzi (2021; arXiv 2110.15943, v2 May 2022) fine-
  tune GPT-2 Large on 142 NLP datasets presented as few-shot episodes,
  training it to predict the last example's output from the k before it.
  On 52 held-out target tasks, with no parameter updates, the meta-trained
  model beats plain in-context learning and multi-task zero-shot transfer
  in most of seven splits. The gains are largest on targets unlike the
  training tasks, and it matches a model 8x larger. Fine-tuning after
  meta-training remains better, and without meaningful label words every
  model falls near chance unless meta-trained on remapped labels. Here
  because A54 named it where meta-learning and in-context learning meet.
  It is the plainest case of outer training improving the interpreter so
  that it uses the signal better ([CLAIM-118](../claims.d/CLAIM-118.md)), and of the meta-learning arm
  of [CASE-tmphsr99](../cases.d/CASE-tmphsr99.md). Read in its NOTE.
---
<!-- inactive-ok-file: CASE-tmphsr99 — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-tmpnivm0: Min and colleagues show that fine-tuning a 770M-parameter language model on many tasks presented as few-shot episodes makes it better at learning held-out classification and multiple-choice tasks in context, without parameter updates, than the same model without such training or trained on the same tasks without demonstrations, with the largest gains on targets unlike the training tasks and with diverse training tasks mattering most

## The account

MetaICL trains the weights once, across tasks, on the in-context objective: predict the (k+1)-th output from k concatenated examples of the same task. Tested on 52 target tasks disjoint from training, the meta-trained GPT-2 Large beats plain in-context learning and multi-task zero-shot transfer in most of seven splits. The channel variant is best in 6 of 7, with 6–15 point gains where targets differ most from training. It matches GPT-J used without meta-training. It approaches fine-tuning on each target, though fine-tuning after meta-training is better still. Diversity of meta-training tasks matters more than their number. Learning to learn in context is something outer training can install, and the result is a weight change that pays off through the context.

## What it does not show

- That the model learns new input–label mappings at test time. Appendix C.4: with meaningless label words every model falls to near chance unless meta-trained on remapped labels, and then reaches only 43.5%.
- Anything beyond 774M parameters, classification and multiple choice, or English.
- That meta-training beats per-task fine-tuning: fine-tuning with meta-training exceeds MetaICL.
- Which training tasks help, or why: the variance across choices is large and unexplained.
