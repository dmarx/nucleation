---
number: 169
status: Proposed
formerly:
- THEORY-tmpllqzv
promote_when: >-
  Both identities are checked against an independent derivation of the
  linear-attention/fast-weight correspondence that the record reads in
  full, such as Schlag, Irie and Schmidhuber (2021), and the scope
  statement is tested by a case that would break it: an exact identity
  of this kind for a further layer class (for instance a delta-rule or
  mini-batch inner update) confirms the pattern, while a proof that some
  standard attention layer's dependence on its context admits no
  description as any learner's train-then-predict step would bound it.
  Restating the two constructions, or measuring trained models' similarity
  to gradient descent, does not count.
title: 'In attention layers, conditioning on a context is exactly training a learner on it and predicting: linear attention is one batch gradient step of a linear inner model, and softmax attention is kernel regression that stores the context, so conditioning and per-sequence weight updates differ in what state is kept, not in kind'
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-10-09'
source:
- LIT-801
- LIT-792
summary: >-
  Sun et al. (2024), [LIT-801](../literature.d/LIT-801.md), Theorems 1–2, with von Oswald et al.
  (2022), [LIT-792](../literature.d/LIT-792.md), Proposition 1. Linear attention equals a layer
  whose state is a linear model's weights, updated by batch gradient
  descent on the context from zero; softmax attention equals a
  Nadaraya–Watson learner whose "training" appends the context to a list;
  and, with constructed weights, one linear attention layer reproduces one
  gradient step of a linear regression on in-context pairs. These are
  identities of output for specific layers. They do not say that trained
  transformers do gradient descent (the anthology rejects that,
  [ANTH-THEORY-068](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-068.md)), nor anything about weight updates that persist across
  sequences.
---

# THEORY-169: In attention layers, conditioning on a context is exactly training a learner on it and predicting: linear attention is one batch gradient step of a linear inner model, and softmax attention is kernel regression that stores the context, so conditioning and per-sequence weight updates differ in what state is kept, not in kind

## Source

Sun, Li, Dalal et al. (2024), *Learning to (Learn at Test Time): RNNs with
Expressive Hidden States*, [LIT-801](../literature.d/LIT-801.md), Theorems 1 and 2, as read in
[NOTE-620](../notes.d/NOTE-620.md). von Oswald, Niklasson, Randazzo et al. (2022), *Transformers
learn in-context by gradient descent*, [LIT-792](../literature.d/LIT-792.md), Proposition 1, as
read in [NOTE-621](../notes.d/NOTE-621.md).

## What was actually shown

Three exact identities, each a short proof checked in the readings.

- **Linear attention is a parametric learner on its context** (Sun et al.,
  Theorem 1). Take an inner model f(x) = Wx with W₀ = 0 and the loss
  ℓ(W; x_t) = ‖Wθ_K x_t − θ_V x_t‖². Batch gradient descent with η = 1/2
  gives W_t = Σ_{s≤t} (θ_V x_s)(θ_K x_s)ᵀ, and the prediction W_t θ_Q x_t is
  the output of linear attention with keys θ_K x_s, values θ_V x_s and
  query θ_Q x_t.
- **Softmax attention is a nonparametric learner on its context** (Sun et
  al., Theorem 2). The Nadaraya–Watson estimator with kernel
  exp((θ_K x)ᵀθ_Q x′) and labels θ_V x_s is softmax self-attention. Its
  train step stores the token; its predict step smooths over what is
  stored.
- **A gradient step on in-context data, carried by the data** (von Oswald
  et al., Proposition 1). With tokens (x_j, y_j) and constructed weights,
  one linear self-attention layer sends every token to
  (x_j, y_j − ΔW x_j), ΔW a gradient step of a linear model on the
  context's squared loss; the query's read-out is the updated model's
  prediction. A single trained layer finds these weights up to scale.

Together they say that for these layers there is no fact of the matter,
at the level of computation, about whether the layer "reads its context"
or "learns from it": the same output has both descriptions. What
distinguishes the descriptions is the state: a list that grows with the
context (softmax attention), a fixed-size matrix that compresses it
(linear attention seen as W_t), or no stored state at all, the update
existing only in the transformed tokens (Proposition 1). In every case the
learned state is per-sequence and is discarded with the sequence. Each
identity could have failed: the algebra either closes or it does not, and
the readings followed it.

## What this does not say

- **Not that trained transformers do gradient descent.** Beyond one layer
  von Oswald et al.'s own models match a preconditioned variant (GD++),
  and later work separates trained transformers from gradient descent;
  the anthology rejects the identification for that reason
  ([ANTH-THEORY-068](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-068.md)) and keeps the weaker frame that a transformer can run
  a learning algorithm on a model held in its activations
  ([ANTH-THEORY-067](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-067.md)). This account uses only the exact constructions.
- **Not about persistent change.** The "learner" here is retrained from
  W₀ for every sequence. Nothing follows about updates to a network's own
  weights, which persist (training) or are discarded by design, as in
  Akyürek et al.'s test-time training ([LIT-796](../literature.d/LIT-796.md)); there, updating on
  the same demonstrations measurably beats conditioning on them, so at the
  level of a whole language model the two uses of a context are not
  interchangeable.
- **Not for the layers people use.** Theorem 1 needs batch gradient
  descent from zero and the simplest linear attention; TTT-Linear itself,
  with mini-batch updates, learned W₀ and LayerNorm, is not equivalent to
  any attention layer. Proposition 1 needs linear attention and a
  particular token layout.
- **Not that the two descriptions are equally useful.** That a layer can be
  described as learning does not show that the description predicts
  anything the conditioning description does not.
- **Not a claim about interpretation in general.** It is a statement
  about a class of sequence layers. Any use of it for interpreters other
  than these (people, or language models as wholes) is an analogy that
  this account does not license.
