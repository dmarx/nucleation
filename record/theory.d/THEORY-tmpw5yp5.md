---
status: Proposed
promote_when: >-
  A rigorous proof of the small-initialisation result (bounding the
  couplings Karkada et al. discard), or an independent analysis or
  measurement on untied weights with word2vec's own asymmetric negative
  sampling showing whether the learned embedding still converges to the top
  eigenspace of the deviation-from-independence matrix in eigenvalue order.
  Further runs under the symmetric, tied setting cannot settle it.
title: 'A rank-limited contrastive word embedding trained from small initialisation learns the top eigenvectors of the co-occurrence matrix''s relative deviation from independence, one at a time in order of eigenvalue, not the best low-rank approximation of its unconstrained optimum'
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-10-09'
source:
- LIT-tmp2n2m4
summary: >-
  Karkada, Simon, Bahri and DeWeese (2025), [LIT-tmp2n2m4](../literature.d/LIT-tmp2n2m4.md): for the quartic
  approximation of word2vec with tied weights and symmetric, constant-weight
  reweighting, the minimisers are proved and the stepwise order is derived,
  and the prediction matches trained word2vec far better than truncated PMI.
  It is shown for a proxy of word2vec, not for word2vec, and the dynamics
  are an approximate derivation.
---
<!-- inactive-ok-file: THEORY-001 — Proposed; the unconstrained-optimum account this one is set beside -->

# THEORY-tmpw5yp5: A rank-limited contrastive word embedding trained from small initialisation learns the top eigenvectors of the co-occurrence matrix's relative deviation from independence, one at a time in order of eigenvalue, not the best low-rank approximation of its unconstrained optimum

## Source

Karkada, Simon, Bahri and DeWeese (2025), [LIT-tmp2n2m4](../literature.d/LIT-tmp2n2m4.md), Theorem 1,
Proposition 2, Lemma 3.1, Result 3 and Figures 2, 3, 5 and 7, as read in
[NOTE-tmpiys9p](../notes.d/NOTE-tmpiys9p.md).

## What was actually shown

Approximate the word2vec skip-gram negative-sampling loss by its quartic
expansion at the origin and tie the two embedding matrices. The objective
becomes ¼ Σ G_ij (W Wᵀ − M*)²_ij + const, where
M*_ij = (Ψ⁺P_ij − Ψ⁻P_iP_j) / (½(Ψ⁺P_ij + Ψ⁻P_iP_j)) measures how far the
reweighted co-occurrence of words i and j departs from independence. When
the reweightings are symmetric and G_ij is constant, the rank-d minimisers
are exactly the top d eigenvectors of M*, scaled by √λ, up to rotation
(proved). From aligned initialisation each eigendirection is acquired by an
independent sigmoid in time (1/λ_k) ln(λ_k/s_k²(0)) (proved); from vanishing
random initialisation the embedding first aligns with the eigenbasis and
then follows the same steps (derived with dropped couplings, not proved).

The comparison could have come out the other way. If word2vec found the
best low-rank fit of its own unconstrained optimum, truncated PMI would
predict it; instead truncated PMI scores 8.4% on Google analogies, PPMI
50.6%, the factorisation of M* 66.3% and word2vec 68.0%, and word2vec's
principal directions overlap M*'s eigenvectors more closely than PPMI's. An
ablation that could have shown otherwise shows that the stepwise order
comes from the reweighting condition, not from the quartic approximation.

## What this does not say

- **Not that word2vec factorises M\*.** The proofs are for a proxy with tied
  weights and a symmetric reweighting that word2vec's own negative sampling
  does not satisfy; that word2vec behaves like the proxy is an empirical
  match on one corpus.
- **Not that the unconstrained optimum is wrong.** [THEORY-001](THEORY-001.md)'s statement
  about the population optimum of contrastive losses stands; this is about
  what a rank limit and a training path select from it. M* agrees with PMI
  to third order but is bounded, and the difference that matters is which
  directions are kept.
- **Not a theorem for the dynamics from random initialisation.** Result 3
  is an approximate derivation the authors hope to make rigorous.
- **Not that embedding directions are unique.** The loss sees only W Wᵀ;
  the eigen-features are the principal directions, and any rotation of the
  embedding coordinates is equally optimal.
- **Not an account of analogies.** The paper's spiked-random-matrix picture
  of analogy vectors is a fitted observation, and nothing here depends on
  it.
- **Not an instruction.** It says what a trained model contains, not how to
  train one.
