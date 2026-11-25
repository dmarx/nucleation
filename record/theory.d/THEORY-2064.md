---
number: 2064
status: Proposed
formerly:
- THEORY-tmpbsmcq
title: 'Code init helps reasoning until cooldown'
statement: >-
  Aryabumi and colleagues find that at a fixed total of 400B tokens, a
  470M-parameter language model initialized by pretraining on 200B tokens of
  code and continued on mostly text scores higher on natural-language
  reasoning than one trained on text alone, before a final cooldown, and
  lower after it
version: 1
source:
- LIT-2844
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent replication, with more than one run per arm, finds that a
  model initialized by code pretraining and continued on mostly text
  reaches higher natural-language reasoning scores than a text-only model
  of equal total tokens before a cooldown phase, and reports whether the
  advantage survives it.
summary: >-
  From the reading of [LIT-2844](../literature.d/LIT-2844.md) in [NOTE-2153](../notes.d/NOTE-2153.md). The positive instance
  of the owner's code-first idea, as final score at fixed total tokens;
  [THEORY-2081](THEORY-2081.md) finds no benefit at matched compute. Proposed until its
  promote_when is met.
---

# THEORY-2064: Code init helps reasoning until cooldown

## The account

Among 470M decoders trained on 400B tokens, code→text (200B code, then text with 10 per cent code) beats text-only on zero-shot natural-language reasoning by 8.8 per cent relative and ties it on knowledge, with 180B text tokens; the pattern is reported to hold at 2.8B. After a 40B-token cooldown, code→text scores 52.1 against text-only's 54.1. A 25 per cent code share is best when mixing from scratch, and the authors recommend mixing.

## Evidence

One run per arm; natural-language tokens not matched; benchmarks, not loss or cost.
