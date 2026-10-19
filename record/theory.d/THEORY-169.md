---
number: 169
status: Active
formerly:
- THEORY-tmpllqzv
title: 'For unnormalized causal linear attention and for softmax attention, conditioning on a context is exactly training a learner on it and predicting: the first is one batch gradient step of a linear inner model from zero, the second kernel regression that stores the context, and one linear self-attention layer with constructed weights carries one gradient step of in-context linear regression; for these layers conditioning and per-sequence weight updates differ in what state is kept, not in kind'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision for THEORY-169 (batch 024,
    ADR-047). The title said "linear attention" without qualification; Sun
    et al.'s identity holds for the unnormalized causal form, and the title
    now says so and names von Oswald et al.'s construction. The promote_when
    asked for a check against an independent derivation of the
    linear-attention/fast-weight correspondence, which the record does not
    hold; under ADR-047 v2 the three identities are re-derived in the note
    of 2026-10-19 below. Its scope test, whether the pattern extends to
    further layer classes, moves unchanged to QUESTION-tmpw593l.
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
supports:
- CLAIM-118
---

# THEORY-169: For unnormalized causal linear attention and for softmax attention, conditioning on a context is exactly training a learner on it and predicting: the first is one batch gradient step of a linear inner model from zero, the second kernel regression that stores the context, and one linear self-attention layer with constructed weights carries one gradient step of in-context linear regression; for these layers conditioning and per-sequence weight updates differ in what state is kept, not in kind

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

## Note of 2026-10-19: the three identities, re-derived

Written out for the promotion audit (batch 024, [ADR-047](../decisions.d/ADR-047.md) v2).

- **Linear attention as one gradient step.** For ℓ(W; x_s) =
  ‖Wk_s − v_s‖² with k_s = θ_K x_s and v_s = θ_V x_s, the gradient is
  ∇_W ℓ = 2(Wk_s − v_s)k_sᵀ. At W₀ = 0 the batch gradient over s ≤ t is
  −2 Σ_{s≤t} v_s k_sᵀ, so one step with η = ½ gives
  W_t = Σ_{s≤t} v_s k_sᵀ. Its prediction on q_t = θ_Q x_t is
  W_t q_t = Σ_{s≤t} v_s (k_sᵀ q_t), the output of unnormalized causal
  linear attention. Normalized linear attention divides by Σ_s k_sᵀ q_t,
  which no gradient step supplies, so the identity is for the unnormalized
  form only.
- **Softmax attention as kernel regression.** The Nadaraya–Watson
  estimator Σ_s κ(k_s, q) v_s / Σ_s κ(k_s, q) with κ(k, q) = exp(kᵀq) is
  softmax attention term for term; its training step stores (k_s, v_s).
- **A gradient step carried by the tokens.** With tokens e_j = (x_j, y_j),
  key and query maps that read x, and a value map that reads −η·y, one
  linear self-attention layer adds −(η/N) Σ_i y_i (x_iᵀ x_j) to the y-part
  of token j. The gradient step on L(W) = (1/2N) Σ_i ‖W x_i − y_i‖² at
  W₀ = 0 is ΔW = (η/N) Σ_i y_i x_iᵀ, so the layer sends y_j to
  y_j − ΔW x_j. On a query token (x_q, 0) the read-out, sign flipped, is
  ΔW x_q, the updated model's prediction.
