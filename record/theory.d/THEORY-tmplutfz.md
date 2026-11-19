---
status: Proposed
title: 'Gururangan and colleagues show that continuing to pretrain RoBERTa on unlabelled text from a task''s domain, or from the task''s own training set, before fine-tuning raises end-task performance across four domains, most where the domain is far from the original corpus, that domain then task adaptation is the best order they tried, and that adaptation to an irrelevant domain or to another task''s text generally leaves end-task performance below no adaptation'
version: 1
source:
- LIT-tmptmqyy
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent replication with seeds on a pretrained masked language
  model shows domain-adaptive continued pretraining raising fine-tuned
  end-task performance over the unadapted model, most for distant domains,
  and a size-matched continued pretraining on an irrelevant domain falling
  below it.
summary: >-
  From the reading of [LIT-tmptmqyy](../literature.d/LIT-tmptmqyy.md) in [NOTE-tmpg5d9a](../notes.d/NOTE-tmpg5d9a.md). A performance result,
  not a cost one. Proposed until its promote_when is met.
---

# THEORY-tmplutfz: Gururangan and colleagues show that continuing to pretrain RoBERTa on unlabelled text from a task's domain, or from the task's own training set, before fine-tuning raises end-task performance across four domains, most where the domain is far from the original corpus, that domain then task adaptation is the best order they tried, and that adaptation to an irrelevant domain or to another task's text generally leaves end-task performance below no adaptation

## The account

A second phase of the original objective, on text from the target's
domain or task, before fine-tuning, improves the end task; relevance
decides, since the same amount of irrelevant text makes it worse. The
phases compose, domain before task. Measured as final F1 after a fixed
fine-tuning recipe, with the earlier phases' own costs reported but not
the cost of the end task's acquisition.

## Evidence

Eight classification tasks, five seeds, one base model; no learning
curves; general pretraining not ablated.
