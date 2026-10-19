---
number: 305
status: Proposed
formerly:
- THEORY-tmp7rs2e
promote_when: >-
  Two results together. First, an independent check of the identity, for
  instance in Van Assel et al.'s Lemma on which Step 2 rests, or a
  re-derivation that writes out R(Z). Second, a settlement of the clause
  about minimizers: a derivation that the minimizer of
  tr(Zᵀ L(π) Z) + log R(Z) on the sphere does, or does not, span the
  bottom eigenvectors of L(π) under stated conditions, or a finite graph
  on which InfoNCE's exact minimizer lies outside every such span. It is
  refuted in its second clause by a proof that the minimizers are
  Laplacian eigenvectors in general. What cannot settle it: embeddings of
  trained networks, or free vectors, that look clustered, as in the
  paper's App. C, since clustering is consistent with both readings.
title: "SimCLR's InfoNCE loss, over all n objects with a Gaussian kernel on the unit sphere, equals a graph-Laplacian quadratic form on the augmentation matrix plus the log of InfoNCE's normalizers, which is spectral clustering only in a sense that admits any regularizer and does not make the minimizer the Laplacian's eigenvectors"
version: 1
tags:
- representation-learning
- probabilistic-modeling
date: '2026-10-14'
source:
- LIT-227
summary: >-
  Tan, Zhang, Yang & Yuan (2023, ICLR 2024), [LIT-227](../literature.d/LIT-227.md), read in
  [NOTE-846](../notes.d/NOTE-846.md): Theorem 3.1 and its proof (App. A), Lemma 2.5 and
  Definition 2.7. The identity between objectives is exact on a finite
  object set with symmetric π. The paper's "spectral clustering" is any
  Laplacian form plus any regularizer; it names no minimizer and no
  population optimum, so it supports neither an eigenvector reading of
  InfoNCE nor the density-ratio optimum of [THEORY-001](THEORY-001.md).
---
<!-- inactive-ok-file: THEORY-001 THEORY-228 — Proposed; accounts this one is contrasted with, not leaned on -->

# THEORY-305: SimCLR's InfoNCE loss, over all n objects with a Gaussian kernel on the unit sphere, equals a graph-Laplacian quadratic form on the augmentation matrix plus the log of InfoNCE's normalizers, which is spectral clustering only in a sense that admits any regularizer and does not make the minimizer the Laplacian's eigenvectors

## Source

Tan, Zhang, Yang & Yuan (2023; ICLR 2024), [LIT-227](../literature.d/LIT-227.md), read in
[NOTE-846](../notes.d/NOTE-846.md): Definitions 2.2 and 2.7, Lemmas 2.3–2.5 (quoted there from
Van Assel et al. 2022), Theorem 3.1 with its proof in App. A, Theorem 4.2.

## What was actually shown

**The setting.** n objects; π_ij is the probability that X_j is drawn as
the positive for X_i, with π symmetric and π_ii excluded. Embeddings
Z_i = f(X_i) lie on the unit sphere, and the kernel is Gaussian,
k(Z_i − Z_j) = exp(−‖Z_i − Z_j‖²/2τ).

**Step 1.** Sampling a directed subgraph with exactly one outgoing edge
per node from π, and scoring it under the same construction applied to
the Gram matrix of k, gives a cross-entropy that splits by rows. Each
row's term, −log k(Z_i − Z_j)/Σ_(l≠i) k(Z_i − Z_l), is exactly the InfoNCE
loss of Eq. (1), with every other object as a negative and the positive in
the denominator.

**Step 2.** By Lemma 2.5 the cross-entropy equals
−Σ π_ij log k(Z_i − Z_j) + log R(Z). With the Gaussian kernel and
symmetric π the first term is tr(Zᵀ L(π) Z), up to the factor 1/τ that
the statement drops. With the out-degree filter, R(Z) factorizes as
Π_i Σ_(l≠i) k(Z_i − Z_l), so log R(Z) is the sum of InfoNCE's log
normalizers. The factorization is the record's reconstruction; the paper
leaves the function inside R undefined.

So the "equivalence" of Theorem 3.1 is an identity between two objectives,
true at every embedding Z. It could have failed: a loss whose negatives
entered differently, or with more than one positive per query, would not
split this way, and the paper notes that the single positive is what the
out-degree filter encodes.

**What "spectral clustering" means here.** Definition 2.7 calls any
problem min_Z tr(Zᵀ L(W) Z) + E(Z) spectral clustering, "where E(Z) is a
regularization term", with no condition on E. Classical spectral
clustering takes E to be the constraint ZᵀZ = I or ZᵀDZ = I, and that
constraint is what makes the solution the bottom eigenvectors of L. The
paper does not show that log R(Z) acts as such a constraint, and states
nothing about minimizers.

## What this does not say

- **That InfoNCE's embedding is a set of Laplacian eigenvectors.** No
  minimizer is characterized. The record's population-optimum account,
  [THEORY-001](THEORY-001.md), says InfoNCE's critic fits the log of the density ratio,
  and that exp and log do not commute with rank-d truncation. That points
  away from an eigenvector reading, though neither paper proves it.
- **That this paper supports [THEORY-001](THEORY-001.md).** It never names a density ratio
  or an optimum.
- **Anything about minibatches.** The identity needs all n objects as
  negatives. The paper's remark that this "explains why SimCLR benefits
  from larger batch size" is asserted, not argued.
- **Anything off a finite object set, or for asymmetric π.** The CLIP
  extension (Theorem 4.2) applies the same identity to a directed
  bipartite graph and calls the result "generalized" spectral clustering.
  The proof is two sentences long and uses a sampling scheme CLIP does
  not use.
- **That exponential kernels are privileged.** The maximum-entropy
  argument (Thm 5.1) yields the softmax form for any similarity; the
  kernel comes from choosing the similarity.

## Connections

- **[THEORY-001](THEORY-001.md).** A different kind of statement about the same loss: an
  identity at every embedding here, a population optimum over critics
  there. The paper is cited in [THEORY-001](THEORY-001.md)'s Source, and the reading finds
  that citation unsupported.
- **[THEORY-007](THEORY-007.md) and [THEORY-228](THEORY-228.md).** These hold eigenvector characterizations
  for the spectral contrastive loss (HaoChen et al., [LIT-249](../literature.d/LIT-249.md); Johnson et
  al., [LIT-258](../literature.d/LIT-258.md)). This account says that Tan et al. do not extend them to
  InfoNCE, though the paper presents itself as doing so.
- **[THEORY-009](THEORY-009.md).** The CLIP case is a non-symmetric pair structure. It
  does not meet [THEORY-009](THEORY-009.md)'s promote_when, since no eigen- or
  singular-function analysis is given.
