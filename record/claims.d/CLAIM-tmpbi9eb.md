---
status: Active
title: 'The task-paired risk difference the record uses in place of Blackwell''s order, D_Q = sup_q |R_q(U) − R_τ(q)(V)|, is a different quantity: it reduces each risk set to one number, needs the losses of paired tasks on one scale, and its absolute value counts improvement as distortion'
version: 1
role: granted
tags:
- mathematical-statistics
- information-theory
date: '2026-10-10'
line: pragmatic-transport
grounds:
- THEORY-156
objects_to:
- CLAIM-050
- CLAIM-106
uses:
- TERM-028
- TERM-043
summary: >-
  Found in the record's audit of the line on 2026-10-10 (formal lens); no
  turn of the exchange raises it. [CLAIM-050](CLAIM-050.md) is stated in Blackwell's
  order, and the record's decision term is A86's D_Q. A risk per task
  needs a prior or a minimax summary, where Blackwell's order compares
  whole risk sets. Subtracting the risks of two tasks needs their losses
  on one scale, which nothing supplies. The absolute value makes D_Q
  symmetric, against [CLAIM-106](CLAIM-106.md). Granted, because each point is
  elementary. It objects to [CLAIM-106](CLAIM-106.md) by undermining the measure meant to
  realize it, not [CLAIM-106](CLAIM-106.md)'s truth, and it does not say a decision term
  is unworkable.
---
<!-- inactive-ok-file: CLAIM-050 CLAIM-106 — Proposed; open, and cited as the claims this objection is to -->
<!-- inactive-ok-file: CLAIM-087 CLAIM-128 — Proposed; the improvement claim D_Q misreads and the claim that notes D_causal's correspondence, cited as open -->
<!-- inactive-ok-file: THEORY-156 — Proposed; cited as the reading of Blackwell's order D_Q is compared with, not as settled -->

# CLAIM-tmpbi9eb: The task-paired risk difference the record uses in place of Blackwell's order, D_Q = sup_q |R_q(U) − R_τ(q)(V)|, is a different quantity: it reduces each risk set to one number, needs the losses of paired tasks on one scale, and its absolute value counts improvement as distortion

## The objection

[CLAIM-050](CLAIM-050.md) says Blackwell's order "makes that comparison precise". The
quantity the record writes down for the comparison is another one.
[TERM-028](../terms.d/TERM-028.md) gives A86 §7's decision distance, "D_Q(U, V) = sup_q |R_q(U) −
R_τ(q)(V)|", and the crystallized argument's "D_dec = sup_(q∈Q) |R_q^o −
R_τ(q)^t|". [TERM-043](../terms.d/TERM-043.md) makes D_dec the decision component of the fidelity
profile, "Loss of ability to perform relevant communicative inference
tasks". The manuscript's L_dec "compares achievable decision risks for
paired communicative tasks" and drops the supremum ([TERM-028](../terms.d/TERM-028.md)). The
quantity and the order differ in four ways.

1. **One number per task.** R_q(U) is a single number. So it is either a
   Bayes risk, which needs a prior on the situation, or a minimax risk,
   which is one summary of the set of attainable risks. Blackwell's order
   compares the whole sets and needs neither. [THEORY-156](../theory.d/THEORY-156.md): "for every
   closed bounded convex set A of loss vectors, every risk vector
   attainable with β is attainable with α". Two renderings can be ordered
   one way by R_q under one prior and the other way under another.
2. **Two tasks on one scale.** D_Q subtracts the risk of task q from the
   risk of a different task τ(q). That needs their losses on a common
   scale, and nothing in the record supplies one. A worked case: let the
   rendering be the source itself, V = U, read the same way, and let τ(q)
   be the same task as q with its loss doubled. Then R_τ(q)(V) = 2R_q(U),
   and D_Q = R_q(U). That is positive whenever the task is not solved
   perfectly, though nothing has changed.
3. **The absolute value.** A rendering that does better on τ(q) counts as
   distorted. If R_q(U) = 1/4, a rendering with R_τ(q)(V) = 0 and one with
   R_τ(q)(V) = 1/2 both give 1/4. When τ is a bijection, D_Q(U, V) under τ
   equals D_Q(V, U) under τ⁻¹: substitute q′ = τ(q) in the supremum. So the
   quantity is symmetric. [CLAIM-106](CLAIM-106.md) makes fidelity "a graded, potentially
   asymmetric property of transport". [CLAIM-087](CLAIM-087.md)'s improved access would
   register as a loss.
4. **The task correspondence.** τ on tasks is one more correspondence that
   nothing anchors ([QUESTION-005](../questions.d/QUESTION-005.md)). [CLAIM-128](CLAIM-128.md) says the same of D_causal's
   correspondence on interventions.

No theorem attaches to D_Q. Blackwell's theorem is about the order.
Its quantitative counterpart, Le Cam's deficiency, is defined for
experiments on one parameter, and it is not D_Q either.

## What it does not say

- It does not say a decision term is unworkable. A signed difference, a
  stated prior or a minimax form, and losses normalised per task would
  meet the first three points. The fourth is [QUESTION-005](../questions.d/QUESTION-005.md).
- It does not say [CLAIM-050](CLAIM-050.md) is false. It says the record's measure of
  decision-relative fidelity is not the order [CLAIM-050](CLAIM-050.md) names, and has no
  results of its own yet.
- It does not say [CLAIM-106](CLAIM-106.md) is false. It says the measure meant to realize
  [CLAIM-106](CLAIM-106.md)'s directed fidelity is symmetric.
