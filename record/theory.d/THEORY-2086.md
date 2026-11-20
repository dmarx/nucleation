---
number: 2086
status: Proposed
formerly:
- THEORY-tmp442o6
title: 'Furuta and colleagues find that in one-layer transformers learning modular arithmetic, a frozen embedding or body pre-grokked on an elementary operation lowers the training fraction needed to grok some related linear expressions, but for quadratic and cubic polynomials more often raises it or prevents grokking, including polynomials composed on that same operation'
version: 1
source:
- LIT-2880
tags:
- compositionality
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent replication with several seeds in small transformers on
  modular arithmetic finds against training from scratch that a frozen
  addition-pre-grokked embedding lowers the minimum grokking fraction for
  2a±b and 2a±3b, that a frozen multiplication-pre-grokked body lowers it
  for ab±b, and that frozen elementary-arithmetic modules raise it or
  prevent grokking for most quadratic and cubic polynomials tested.
summary: >-
  From the reading of [LIT-2880](../literature.d/LIT-2880.md) in [NOTE-2168](../notes.d/NOTE-2168.md). Transplanted grokked
  modules help some compositions and block others, often blocking
  compositions on their own operation. Proposed until its promote_when is
  met.
---

# THEORY-2086: Furuta and colleagues find that in one-layer transformers learning modular arithmetic, a frozen embedding or body pre-grokked on an elementary operation lowers the training fraction needed to grok some related linear expressions, but for quadratic and cubic polynomials more often raises it or prevents grokking, including polynomials composed on that same operation

## The account

At p = 97 with three seeds: frozen addition embedding takes 2a+b from 0.5 to 0.3; frozen multiplication body takes ab±b from 0.5 to 0.3; a frozen addition body prevents (a+b)^3 from grokking, which scratch groks at 0.3; every frozen module raises a^2−b^2 from 0.3 to between 0.4 and 0.7; a^3+ab, 0.9 from scratch, never groks with any frozen module.

## Evidence

Three seeds averaged; a coarse grid; transplant without ablation.
