---
status: Proposed
promote_when: >-
  Theorem 4.1's construction checked from its proof (appendix G.1) or
  re-implemented, the multi-hop lower bound (Theorem 4.2) checked from its
  proof, and the learned-embedding experiment replicated at the stated
  sizes: d_min growing logarithmically in N at fixed R, per-relation linear
  readouts recovering the attributes, and a frozen MLP transferring to new
  bijections when the subject embeddings are re-initialized, against a
  frozen-embedding control that needs much larger d and does not transfer.
  Refuted for the trained-model clause if training at the stated sizes
  yields MLPs that do not transfer. Probe results in released language
  models cannot settle it: the entry is about the toy.
title: 'In a one-layer transformer trained to recall R random bijections from N subjects onto a shared set of N attributes, learnable embeddings let all N·R facts be memorized with embedding dimension O(R log N) and an MLP whose width does not grow with N, by encoding each subject as a linear superposition of its R attribute codes from which a relation-conditioned ReLU MLP selects, rather than by storing subject–attribute pairs as associations in the weights, which training finds only when the embeddings are frozen; without chain-of-thought, a counting bound makes k-hop recall pay either in weights that hold the facts or in an embedding exponential in k, as Ravfogel, Yehudai, Bruna and Bietti prove and find gradient descent to recover'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Filed Proposed from NOTE-tmpov37q, the reading of Ravfogel et al.'s
    main text in full and parts of the appendix on 2026-11-15; the proofs
    were not checked.
tags:
- representation-learning
- learning-theory
date: '2026-11-15'
source:
- LIT-tmpi44jr
summary: >-
  Ravfogel, Yehudai, Bruna & Bietti (2026, preprint), [LIT-tmpi44jr](../literature.d/LIT-tmpi44jr.md), read in
  [NOTE-tmpov37q](../notes.d/NOTE-tmpov37q.md): in a one-layer toy, learned embeddings carry the facts and
  the MLP selects, at d = O(R log N); with embeddings frozen, training falls
  back to associative storage in the weights at much larger d. A regime in
  which [THEORY-1030](THEORY-1030.md)'s reading of the MLP as a memory does not hold, shown in
  a toy and not in language models. The wording is the reader's; adopting
  it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1030 THEORY-1039 — Proposed readings of FFN memory and fact recall, cited as open -->

# THEORY-tmpetsya: In a one-layer transformer trained to recall R random bijections from N subjects onto a shared set of N attributes, learnable embeddings let all N·R facts be memorized with embedding dimension O(R log N) and an MLP whose width does not grow with N, by encoding each subject as a linear superposition of its R attribute codes from which a relation-conditioned ReLU MLP selects, rather than by storing subject–attribute pairs as associations in the weights, which training finds only when the embeddings are frozen; without chain-of-thought, a counting bound makes k-hop recall pay either in weights that hold the facts or in an embedding exponential in k, as Ravfogel, Yehudai, Bruna and Bietti prove and find gradient descent to recover

## Source

Ravfogel, Yehudai, Bruna & Bietti (2026), [LIT-tmpi44jr](../literature.d/LIT-tmpi44jr.md); read in
[NOTE-tmpov37q](../notes.d/NOTE-tmpov37q.md).

## The result

- **Construction** (Theorem 4.1): a 3-layer MLP of width R and
  d = 4R log(N) + 1 suffice; each subject embedding stacks its R attribute
  codes in ±1 blocks of 4 log N.
- **Training** (§5.2): with learned embeddings d_min ≈ a + b log₂ N; with
  embeddings frozen at random, d grows "as a power law of N" (R = 16 needs
  d ≥ 512 rather than 128). Readouts and minimum-norm interventions act on
  one relation at a time. A frozen MLP transfers to new bijections once the
  subject embeddings are re-initialized; in the frozen-embedding control
  zero-shot accuracy "is near chance".
- **Multi-hop** (Theorems 4.2–4.4, C.1): a counting bound on the bits W
  in the attention and MLP weights against the bits D in the embedding.
  If D < R, "The model must store N R facts inside its weights"; if
  D > R^k the MLP can act as a selector, "but the embedding dimension is
  exponential in k"; in between the bound is loose (Remark 4.1).
  Constructions match the two ends (Theorem 4.3: "an O(N · R) wide MLP
  operates as a brute-force lookup table"). Chain-of-thought brings d down
  to Õ(R + k) (Theorem 4.4).

## What it does not show

- That released language models recall facts this way. Its LM evidence is
  a probe of linear decodability, which is consistent with weight-stored
  facts as well.
- That MLPs in LMs are not key–value memories ([THEORY-1030](THEORY-1030.md)), or where facts
  are localized ([THEORY-1011](THEORY-1011.md), [THEORY-1039](THEORY-1039.md)): it offers an alternative
  mechanism, and shows that associative storage is what training finds
  when embeddings cannot carry the facts.
- That "superposition" in the interference sense is involved: the codes sit
  in disjoint blocks.
- Anything for correlated relations, typed attributes, multi-token
  entities or long-tailed frequencies, which the authors leave open.
- The size of the zero-shot transfer, which the main text calls only
  "substantial".
