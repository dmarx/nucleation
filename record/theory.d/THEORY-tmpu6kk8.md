---
status: Active
title: 'In Transformer attention the weights each query puts on the positions depend only on query–key compatibility, softmax(QKᵀ/√d_k), and the output is those weights applied to the values, so for a fixed input what a head selects and what it transports are separate factors; because queries, keys and values are all projections of the same input, the separation holds only with the input, and so the pattern, held fixed'
version: 1
tags:
- representation-learning
date: '2026-11-03'
source:
- LIT-tmp91wxa
- LIT-1534
summary: >-
  Vaswani et al. (2017), LIT-tmp91wxa, read in full in NOTE-tmp2mbd7, eq. 1
  and §3.2.2; the circuit vocabulary is Elhage et al.'s (LIT-1534,
  THEORY-988). Active: it is the definition of the mechanism, checked
  against the equations. It does not say that heads are interpretable
  observers, which the paper supports only with visualizations, or that
  the separation survives composition across layers.
---

# THEORY-tmpu6kk8: In Transformer attention the weights each query puts on the positions depend only on query–key compatibility, softmax(QKᵀ/√d_k), and the output is those weights applied to the values, so for a fixed input what a head selects and what it transports are separate factors; because queries, keys and values are all projections of the same input, the separation holds only with the input, and so the pattern, held fixed

## Source

Vaswani et al. (2017), LIT-tmp91wxa, §3.2; read in NOTE-tmp2mbd7. The QK/OV
naming is Elhage et al.'s, LIT-1534.

## What was actually shown

Eq. (1): Attention(Q, K, V) = softmax(QKᵀ/√d_k)V. "The output is computed as
a weighted sum of the values, where the weight assigned to each value is
computed by a compatibility function of the query with the corresponding
key" (pp. 3–4). In a head, Q = XW^Q, K = XW^K, V = XW^V (p. 5), so for input X
the output is A(X)·X W^V W^O with A(X) = softmax(XW^Q(XW^K)ᵀ/√d_k): linear in
the transported content once A is fixed, and nonlinear in X through A.

The paper's reason for several heads (p. 5): with one head, "averaging
inhibits" attending to different subspaces at different positions, since
each row of A is a convex combination.

## What this does not say

- That a head is an observer in any sense beyond this factorization.
- That selection and transport stay separable across layers: later queries
  and keys are computed from earlier heads' outputs.
- That heads learn distinct, interpretable tasks: asserted from a few
  visualizations (p. 7).
