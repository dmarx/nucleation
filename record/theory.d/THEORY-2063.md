---
number: 2063
status: Proposed
formerly:
- THEORY-tmp9adpz
title: 'Ma and colleagues report that a 2.6B language model pretrained with a large share of code scores above a released text-only model of the same size on most of six reasoning tasks, without matched data or tokenizer, and that within instruction tuning a falling share of code works best on code tasks'
version: 1
source:
- LIT-2856
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent study, or the released models rerun with several seeds,
  shows a model pretrained with code scoring above a text-only model
  trained on matched total tokens with the same tokenizer on non-code
  reasoning tasks, and the code-decreasing instruction-tuning schedule
  beating uniform and increasing schedules of equal mean code share on
  code tasks across seeds.
summary: >-
  From the reading of [LIT-2856](../literature.d/LIT-2856.md) in [NOTE-2155](../notes.d/NOTE-2155.md). A weak, uncontrolled
  instance; [THEORY-2066](THEORY-2066.md) holds the controlled version of its open
  question. Proposed until its promote_when is met.
---

# THEORY-2063: Ma and colleagues report that a 2.6B language model pretrained with a large share of code scores above a released text-only model of the same size on most of six reasoning tasks, without matched data or tokenizer, and that within instruction tuning a falling share of code works best on code tasks

## The account

CodePanGu 2.6B, about 42B tokens with 36 per cent Python, scores above the released PanGu 2.6B on five of six reasoning tasks; code instructions mainly help code tasks; a stepwise-decreasing code share (5:5 to 7:3 text to code) is best on code tasks among three instruction-tuning schedules of equal mean share.

## Evidence

Single runs; baseline a released checkpoint with another tokenizer; small test sets.
