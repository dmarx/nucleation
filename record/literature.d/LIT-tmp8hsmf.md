---
status: Active
status_note: 'read 2026-10-09 (NOTE-tmpchl3b); worth reading for its reframing of a sequence layer as a learner trained on its own context: the hidden state is the weights of an inner model, the update rule a gradient step on a self-supervised loss, the output rule the inner model''s prediction. Two exact identities follow: a linear inner model with batch gradient descent is linear attention (Theorem 1), and the Nadaraya–Watson estimator as inner learner is softmax self-attention (Theorem 2). The empirical part, TTT-Linear and TTT-MLP against Mamba and a Transformer at 125M–1.3B, is an architecture result that belongs to the anthology''s question.'
title: 'Learning to (Learn at Test Time): RNNs with Expressive Hidden States'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed and read on 2026-10-09 (NOTE-tmpchl3b) from the arXiv v4 PDF
    (31 Aug 2025, 33 pp.; the authors state that all experiments were
    completed in v1). The manuscript's bibliography cites "Sun et al.
    (2025), Learning to (learn at test time): RNNs with expressive hidden
    states, PMLR 267:57503–57522"; this is that paper, not the 2023
    preprint "Learning to (Learn at Test Time)" (arXiv 2310.13807) by
    overlapping authors. Checked against the arXiv API (twelve authors,
    Yu Sun first; v1 submitted 5 July 2024, which is `published:` per
    ADR-002) and the PMLR volume 267 index (ICML 2025, pp. 57503–57522).
    Not held in the Anthology of the SOTA as a LIT: a grep of its record/
    (clone of 2026-10-09, commit d8b5ba5) finds the identifier only in
    prose (ANTH-LIT-379, its NOTE-167 and SOTA-235, each warning of the
    TTT name collision). Hence `anthology-candidate`.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-09'
published: '2024-07-05'
arxiv: '2407.04620'
first_author: 'Sun'
keywords:
- 'test-time training'
- 'TTT layers'
- 'RNN'
- 'hidden state'
- 'linear attention'
- 'fast weights'
- 'long context'
implementations: []
summary: >-
  Sun, Li, Dalal, Xu, Vikram, Zhang, Dubois, Chen, Wang, Koyejo, Hashimoto
  and Guestrin (2024), ICML 2025. Makes a sequence layer's hidden state
  the weights W of an inner model f, updated per token by a gradient step
  on a learned self-supervised reconstruction loss, with output
  f(θ_Q x_t; W_t). With a linear f and batch gradient descent this is
  exactly linear attention (Theorem 1); with the Nadaraya–Watson estimator
  as inner learner it is exactly softmax self-attention (Theorem 2).
  TTT-Linear and TTT-MLP match or beat Mamba at 125M–1.3B and keep
  lowering perplexity to 32k tokens of context, where Mamba plateaus
  after 16k.
---

<!-- inactive-ok-file: THEORY-tmpllqzv — Proposed; the account this reading is a source of -->

# LIT-tmp8hsmf: Learning to (Learn at Test Time): RNNs with Expressive Hidden States

Yu Sun, Xinhao Li, Karan Dalal, Jiarui Xu, Arjun Vikram, Genghan Zhang,
Yann Dubois, Xinlei Chen, Xiaolong Wang, Sanmi Koyejo, Tatsunori Hashimoto
and Carlos Guestrin (2024), *ICML 2025*, PMLR 267:57503–57522 —
ARXIV-2407.04620

## Key takeaways

- **Every sequence layer is a state, an update rule and an output rule.**
  An RNN compresses context into a fixed-size state; self-attention keeps
  the whole context (the KV cache) and scans it. A TTT layer makes the
  state the weights W of a model f, the update W_t = W_{t−1} − η∇ℓ(W_{t−1};
  x_t), and the output z_t = f(θ_Q x_t; W_t). Even at test time the layer
  trains a fresh sequence of weights for every input sequence.
- **Two loops.** The inner loop trains W on reconstruction,
  ℓ(W; x_t) = ‖f(θ_K x_t; W) − θ_V x_t‖²; the outer loop trains θ_K, θ_V,
  θ_Q (and the rest of the network, the initial weights and a
  token-dependent learning rate) on next-token prediction. Outer-loop
  parameters are hyper-parameters of the inner learning problem; W is
  state, not a parameter.
- **Theorem 1.** Linear f, batch gradient descent with η = 1/2 and W₀ = 0
  gives z_t = Σ_{s≤t} (θ_V x_s)(θ_K x_s)ᵀ(θ_Q x_t), which is linear
  attention.
- **Theorem 2.** The Nadaraya–Watson estimator with kernel
  exp((θ_K x)ᵀθ_Q x′) and labels θ_V x_s, as a nonparametric inner
  learner, gives softmax self-attention. Training is storing the context;
  prediction is kernel smoothing over it.
- **What changes the results.** Mini-batch inner updates (b = 16) instead
  of batch gradient descent give the largest gain (perplexity 14.05 →
  12.35 in the 125M ablation); LayerNorm and a residual in f the second.
- **Long context.** TTT-Linear and TTT-MLP keep reducing perplexity with
  token index out to 32k, like the Transformer and unlike Mamba. TTT-MLP
  is costly in wall-clock time, which the authors leave open.

## Standing in the record

Filed on 2026-10-09 at the owner's request, from the bibliography of the
owner's manuscript *What Survives Translation?* (work
`what-survives-translation`), which considered it and dropped it from the
final reference list. Read on its own terms (NOTE-tmpchl3b).

It carries `anthology-candidate`: as an architecture paper its subject is
one anthology topics hold, and the anthology names it without filing it.
What this record takes from it is the two theorems, which state attention
as learning on the context. They are a source of THEORY-tmpllqzv.

The name "test-time training" covers two things: here, an inner model
whose weights are a layer's state; in Akyürek et al. (LIT-tmp686hl), a
temporary update to the network's own weights. Akyürek et al. say so in a
footnote.
