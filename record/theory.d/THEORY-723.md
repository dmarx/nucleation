---
number: 723
status: Active
formerly:
- THEORY-tmp3z96c
title: 'For the final embedding and unembedding of a softmax model, the output distribution fixes the representations only up to an invertible linear map, and whether closeness in distribution bounds representational dissimilarity depends on the distance: not for KL in the saturation regime, but yes for the log-likelihood variance distance'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-002 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-002.yaml, batch 009, ADR-047).
    THEORY-002's title bundles these proved results with an interpretive
    reading of the Platonic hypothesis, and its promote_when bears only on
    that reading. Every result here is proved in LIT-253 (Thm 2.2, App. B;
    Thm 3.1, App. C.1; Cor. 3.2; Thm 4.7, App. E.5–E.6), and NOTE-738 read
    those proofs in full, so ADR-047 v2 is not needed. The orthogonal case
    is THEORY-004's, which this presupposes. THEORY-002 keeps the reading
    and extends this one.
tags:
- representation-learning
- mathematics
date: '2026-10-19'
source:
- LIT-253
- LIT-250
summary: >-
  Nielsen et al. (2025), [LIT-253](../literature.d/LIT-253.md), read in full in [NOTE-738](../notes.d/NOTE-738.md), with Harvey,
  Larsen & Williams (2023), [LIT-250](../literature.d/LIT-250.md), for the kernel side. What is observed
  fixes a representation only up to that observation's symmetry group: a
  centred linear kernel up to a translation and an orthogonal map
  ([THEORY-004](THEORY-004.md)), and a softmax output distribution up to an invertible
  linear map of the embedding with the inverse transpose on the
  unembedding (Thm 2.2). KL can go to zero while the embeddings stay
  non-linearly related (Thm 3.1, Cor. 3.2), but d_LLV ≤ ε gives
  d_f,g ≤ 2Mε (Thm 4.7). Final layer only. It does not say what the
  Platonic hypothesis means; that is [THEORY-002](THEORY-002.md).
presupposes:
- THEORY-004
extended_by:
- THEORY-002
supports:
- CLAIM-379
---
<!-- inactive-ok-file: THEORY-002 — Proposed; the Platonic-hypothesis reading this core was split from and that extends it, cited as open -->

# THEORY-723: For the final embedding and unembedding of a softmax model, the output distribution fixes the representations only up to an invertible linear map, and whether closeness in distribution bounds representational dissimilarity depends on the distance: not for KL in the saturation regime, but yes for the log-likelihood variance distance

## Source

Nielsen et al. (2025), [LIT-253](../literature.d/LIT-253.md), Thm 2.2 (proof in App. B), Thm 3.1
(constructive proof in App. C.1), Cor. 3.2 and Thm 4.7 (App. E.5–E.6), read
in full in [NOTE-738](../notes.d/NOTE-738.md), whose claims table rates C1, C2, C3 and C5 "strong".
Harvey, Larsen & Williams (2023), [LIT-250](../literature.d/LIT-250.md), for the kernel-side metric, read
in [NOTE-753](../notes.d/NOTE-753.md). The orthogonal case is [THEORY-004](THEORY-004.md).

## What was actually shown

**What an observation fixes.** For a softmax model
p(y | x) ∝ exp(f(x)ᵀ g(y)), with embedding f and unembedding g, two models
with the same output distribution have embeddings related by f = A f′, and
unembeddings, taken relative to a pivot label, by g₀ = A⁻ᵀ g′₀, for an
invertible A ([LIT-253](../literature.d/LIT-253.md) Thm 2.2, a prior result restated with its proof in
App. B). The distribution fixes the representation up to the general
linear group and no further. A centred linear kernel fixes it up to a
translation and an orthogonal map ([THEORY-004](THEORY-004.md)). So what is observed sets
the symmetry group up to which the representation is fixed.

**Closeness depends on the distance.** KL divergence between the output
distributions can tend to zero while the embeddings are not related by any
invertible linear map (Thm 3.1, with a constructive proof). The
construction needs the unembedding norm to grow without bound, so that
both softmaxes saturate. Cor. 3.2 gives the same for deterministic labels.
Under the paper's log-likelihood variance distance the answer reverses:
d_LLV ≤ ε implies d_f,g ≤ 2Mε (Thm 4.7). The paper's conclusion is that
the answer "depends critically on the choice of distributional and
representational distance".

These could have gone otherwise. Some distributional distance might have
bounded representational dissimilarity uniformly, or none might have. The
paper proves one of each.

## What this does not say

- **Anything below the final layer.** Every result concerns the final
  embedding and the unembedding. The paper says earlier layers would need
  identifiability results that do not yet exist (§6).
- **How far apart the KL counterexample's embeddings are.** Thm 3.1 proves
  only that they are not linearly related. The size of the dissimilarity
  is shown numerically (Table 1).
- **What the Platonic hypothesis means, or whether it holds.** Reading
  these results as a constraint on that hypothesis, whose kernels are of
  pooled hidden states, is [THEORY-002](THEORY-002.md)'s inference, and it stays Proposed.
