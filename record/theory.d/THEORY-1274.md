---
number: 1274
status: Active
formerly:
- THEORY-tmpxb5pl
title: 'Under a shared linear output head, the cross-entropy gradient of a multi-token-prediction head at its hidden state is exactly the gradient of a forward KL toward the model''s own position-aligned next-token prediction, held fixed, plus the next-token cross-entropy gradient at the aligned state, which alone carries the sampled target; the identity is about gradients and computations, not information, and in heads fed the intervening tokens the student and its teacher condition on the same evidence'
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-10-31'
source:
- LIT-1896
summary: >-
  Teoh (2026), [LIT-1896](../literature.d/LIT-1896.md), eqs. 1–3 and Appendix B; read in
  [NOTE-1470](../notes.d/NOTE-1470.md) and checked by finite differences. Active: elementary and
  checked. It is a gradient identity, not a decomposition of the loss's
  value, and it does not by itself make the self-distillation a
  projection onto less information: in the DeepSeek-style heads of the
  paper's main results the student sees the same tokens as its teacher.
---
<!-- inactive-ok-file: THEORY-1262 — Proposed; the empirical companion, cited as not established -->

# THEORY-1274: Under a shared linear output head, the cross-entropy gradient of a multi-token-prediction head at its hidden state is exactly the gradient of a forward KL toward the model's own position-aligned next-token prediction, held fixed, plus the next-token cross-entropy gradient at the aligned state, which alone carries the sampled target; the identity is about gradients and computations, not information, and in heads fed the intervening tokens the student and its teacher condition on the same evidence

## Source

Teoh (2026), [LIT-1896](../literature.d/LIT-1896.md), §4 eqs. (1)–(3), §5.1 eqs. (4)–(7), §5.3
eq. (8) and Appendix B, pp. 3–6 and 18–20 of arXiv 2610.38331v1; read in
[NOTE-1470](../notes.d/NOTE-1470.md).

## What was actually shown

Let p = softmax(Wh⁽ᵏ⁾_t) be MTP head k's prediction of x_{t+k+1} and
q = softmax(Wh⁽⁰⁾_{t+k}) the NTP prediction of the same token, with W
shared. Then

∇_{h⁽ᵏ⁾} CE(y, p) = W⊤(p − y) = W⊤(p − q) + W⊤(q − y),

and W⊤(p − q) = ∇_{h⁽ᵏ⁾} KL(sg(q) ‖ p). The second term is the NTP
cross-entropy gradient at h⁽⁰⁾_{t+k}, so a straight-through term
h̃⁽⁰⁾ = h⁽⁰⁾ + sg(h⁽ᵏ⁾) − h⁽ᵏ⁾, numerically zero, delivers its negative to
h⁽ᵏ⁾ and leaves exactly the KL gradient for the MTP heads and the trunk.
The output head keeps its cross-entropy gradient (App. B.4). Only the
second term depends on the sampled token; writing π for the true
next-token law, it is the teacher's error W⊤(q − π) plus zero-mean noise
W⊤(π − y) (eq. 8).

Checked numerically (V = 7, d = 5): the three gradients agree with their
closed forms, and the identity holds, to 4 × 10⁻¹⁰. The routed field
(student W⊤(p − q), teacher W⊤(q − y)) has an asymmetric Jacobian: the
student's update depends on the teacher's state and not conversely. So it
is not the gradient of any single scalar.

What could have failed: the identity needs the head to be shared and
linear. With untied heads, W⊤(p − q) would not be the KL gradient for the
student's own readout.

## What this does not say

- **That the loss splits into a distillation loss and a data loss.** In
  value, CE(y, p) = KL(q ‖ p) + (q − y)⊤Wh⁽ᵏ⁾ + H(q) (checked to
  10⁻¹⁵). The remainder is linear in the student's logits: a constant
  push with no minimum, not a second objective the student could
  satisfy. The paper states the split for gradients only.
- **That the student knows less than the teacher.** In the DeepSeek-style
  sequential heads used for every main result, head k at position t is
  fed x_{t+1}, …, x_{t+k} (Algorithm 1) and conditions on the same prefix
  as its teacher. The asymmetry is computational: one extra layer per step
  against the 36-layer trunk. Only the Meta-style parallel heads
  (App. C) predict from less context. So the conditional-projection
  account, in which the best student is E[teacher | student's
  information] with an irreducible conditional mutual information
  ([THEORY-1259](THEORY-1259.md)), is not what this identity instantiates in the main
  experiments; there the irreducible term is zero.
- **That the teacher is untouched by the student.** The stop-gradient
  cuts only the teacher's output path. The KL gradient flows into the
  trunk that also computes the teacher.
- **That removing the residual is better.** That is the paper's empirical
  claim ([THEORY-1262](THEORY-1262.md)), not a consequence of the identity.
- **Anything about who runs the distillation.** Teacher, routing and
  optimizer are the engineer's.
