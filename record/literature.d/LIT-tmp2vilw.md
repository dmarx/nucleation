---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpepej2](../notes.d/NOTE-tmpepej2.md)); worth reading here for one exact identity: with constructed key, query, value and projection matrices, one linear self-attention layer applied to tokens (x_j, y_j) changes every token exactly as one gradient-descent step on the context''s squared regression loss would change the targets (Proposition 1), so reading a context and updating an implicit model''s weights on it produce the same prediction. A trained single layer finds those weights up to scale; deeper trained models match a preconditioned variant (GD++) rather than plain gradient descent. Everything is on synthetic regression with small attention-only models.'
title: 'Transformers learn in-context by gradient descent'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed here as well as in the anthology (ANTH-LIT-533), under ADR-013,
    and read on 2026-10-09 (NOTE-tmpepej2) from the arXiv v2 PDF (31 May
    2023, 24 pp.). Bibliography checked against the arXiv API (authors
    Johannes von Oswald, Eyvind Niklasson, Ettore Randazzo, João
    Sacramento, Alexander Mordvintsev, Andrey Zhmoginov, Max Vladymyrov;
    v1 submitted 15 December 2022, which is `published:` per ADR-002) and
    the PMLR page (ICML 2023, PMLR 202:35151–35174, as the manuscript's
    bibliography gives). The anthology holds it as ANTH-LIT-533, read for
    the mechanism of in-context learning, with its rejected generalisation
    ANTH-THEORY-068 and the surviving frame ANTH-THEORY-067; a grep of its
    record/ (clone of 2026-10-09, commit d8b5ba5) confirmed this.
tags:
- representation-learning
- learning-theory
date: '2026-10-09'
published: '2022-12-15'
arxiv: '2212.07677'
first_author: 'von Oswald'
keywords:
- 'in-context learning'
- 'linear self-attention'
- 'gradient descent'
- 'mesa-optimization'
- 'meta-learning'
- 'fast weights'
implementations: []
summary: >-
  von Oswald, Niklasson, Randazzo, Sacramento, Mordvintsev, Zhmoginov and
  Vladymyrov (2022), ICML 2023. Proposition 1 constructs weights for which
  one linear self-attention layer transforms each token (x_j, y_j) to
  (x_j, y_j − ΔW x_j), with ΔW one gradient step on the context's squared
  loss, so the query token's read-out equals the prediction of the updated
  linear model. A trained single layer matches the construction up to
  scale; deeper models outperform K steps of gradient descent and match
  GD++, gradient descent on inputs transformed by I − γXXᵀ. Synthetic
  regression only.
---

<!-- inactive-ok-file: THEORY-tmpllqzv — Proposed; the account this reading is a source of -->

# LIT-tmp2vilw: Transformers learn in-context by gradient descent

Johannes von Oswald, Eyvind Niklasson, Ettore Randazzo, João Sacramento,
Alexander Mordvintsev, Andrey Zhmoginov and Max Vladymyrov (2022), *ICML
2023*, PMLR 202:35151–35174 — [ARXIV-2212.07677](https://arxiv.org/abs/2212.07677)

## Key takeaways

- **The identity (Proposition 1).** With W_K = W_Q = [[I_x, 0], [0, 0]],
  W_V = [[0, 0], [W₀, −I_y]] and P = (η/N)I, a linear self-attention step
  sends every token e_j = (x_j, y_j), the query included, to
  (x_j, y_j − ΔW x_j), where ΔW = −(η/N) Σ_i (W₀x_i − y_i)x_iᵀ is one
  gradient step on L(W) = (1/2N) Σ ‖Wx_i − y_i‖². A gradient step on the
  weights is re-expressed as a change to the data, and the attention layer
  makes exactly that change. The updated model is never stored; its effect
  appears only in the query token's output.
- **Found, not only constructible.** A single LSA layer trained on random
  linear-regression tasks reaches the loss of one tuned gradient step, its
  predictions and input sensitivities align with the construction's
  (cosine near 1), and a scale correction plus linear interpolation
  between trained and constructed weights keeps the loss unchanged, in and
  out of the training input range.
- **Deeper is not plain gradient descent.** Recurrent two-layer and
  five-layer LSA models beat K steps of gradient descent and align instead
  with GD++, a step on data transformed by H(X) = I − γXXᵀ with η and γ
  tuned per step: a curvature correction.
- **MLP then attention** (Proposition 2) gives gradient descent on a linear
  read-out of deep features, i.e. kernel regression with
  k(x, y) = m(x)ᵀm(y); trained models on sine-wave regression resemble a
  meta-learned MLP with one gradient step on its output layer.
- **Building the tokens** (Proposition 3, §4). If inputs and targets come
  in separate tokens, a first (softmax) layer can copy them together and a
  second layer then performs the step; trained two-layer models do this,
  matching one GD step, not two.

## Standing in the record

Held in both records under [ADR-013](../decisions.d/ADR-013.md). The anthology holds it as [ANTH-LIT-533](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-533.md),
read for what the forward pass of a transformer computes, and has rejected
the identification of in-context learning with gradient descent
([ANTH-THEORY-068](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-068.md)) while keeping the frame that a transformer can run a
learning algorithm on a model carried in its activations ([ANTH-THEORY-067](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-067.md)).
It is filed here at the owner's request on 2026-10-09, from the bibliography
of the owner's manuscript *What Survives Translation?* (work
`what-survives-translation`), which considered it and dropped it from the
final reference list. The second question, the one this record asks, is the
reading on this record's terms: what Proposition 1 says about the
difference between conditioning a fixed system on a context and changing
the system's parameters. That reading is [NOTE-tmpepej2](../notes.d/NOTE-tmpepej2.md), and it is a source
of [THEORY-tmpllqzv](../theory.d/THEORY-tmpllqzv.md).

The two readings do not disagree. The anthology's rejection concerns the
claim that trained transformers in general do gradient descent; this
record uses only the exact construction and the single-layer result, which
the anthology's entry keeps.
