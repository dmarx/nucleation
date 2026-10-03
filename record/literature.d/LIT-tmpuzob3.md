---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmpxfj4e](../notes.d/NOTE-tmpxfj4e.md)); worth reading as the source of the Kronecker-factored Fisher: each layer''s Fisher block E[āāᵀ ⊗ ggᵀ] is approximated by E[āāᵀ] ⊗ E[ggᵀ], so it inverts as two small matrices, and the inverse is further taken as block-diagonal or block-tridiagonal across layers. The factorization is justified by small higher-order cumulants, checked on one small tanh network; the speedups are on three deep autoencoders.'
title: 'Optimizing Neural Networks with Kronecker-factored Approximate Curvature'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from arXiv (v7, 8 June 2020, 58 pages); v1 is 19 March
    2015. Published at ICML 2015, PMLR 37:2408–2417 (PMLR page checked).
    Not held in the Anthology of the SOTA: a grep of its record for
    "1503.05671" found nothing, and its K-FAC holdings are the later
    tutorial (ANTH-LIT-768) and linear-operator position paper
    (ANTH-LIT-746).
tags:
- information-geometry
- anthology-candidate
date: '2026-10-03'
published: '2015-03-19'
arxiv: '1503.05671'
first_author: 'Martens'
keywords:
- 'natural gradient'
- 'Fisher information matrix'
- 'Kronecker product'
- 'Khatri-Rao product'
- 'block-tridiagonal inverse'
- 'generalized Gauss-Newton'
- 'Tikhonov damping'
- 'second-order optimization'
extends:
- LIT-tmp26jbc
implementations: []
summary: >-
  Martens & Grosse (2015), ICML. K-FAC approximates natural gradient descent
  in neural networks. Each Fisher block between layers i and j,
  E[āᵢ₋₁āⱼ₋₁ᵀ ⊗ gᵢgⱼᵀ], is replaced by E[āᵢ₋₁āⱼ₋₁ᵀ] ⊗ E[gᵢgⱼᵀ] (activations
  times backpropagated derivatives), whose error is a sum of third- and
  fourth-order cumulants. The inverse is then taken as block-diagonal or
  block-tridiagonal across layers. With factored Tikhonov damping, re-scaling
  by the exact Fisher, an adaptive momentum and a growing mini-batch, it
  needs orders of magnitude fewer iterations than tuned SGD with Nesterov
  momentum on three deep autoencoder benchmarks, and it is invariant to
  affine reparameterizations of each layer's inputs and pre-activations.
compared_against:
- LIT-tmpbfzro
---

# LIT-tmpuzob3: Optimizing Neural Networks with Kronecker-factored Approximate Curvature

James Martens and Roger Grosse (2015), ICML 2015 — [ARXIV-1503.05671](https://arxiv.org/abs/1503.05671)

## Key takeaways

- **The Kronecker factorization.** Because vec(DWᵢ) = āᵢ₋₁ ⊗ gᵢ, the
  Fisher's (i, j) block is E[āᵢ₋₁āⱼ₋₁ᵀ ⊗ gᵢgⱼᵀ]. K-FAC approximates it by
  Āᵢ₋₁,ⱼ₋₁ ⊗ Gᵢ,ⱼ (Eq. 1), a Khatri–Rao product over layers. This assumes
  activities and backpropagated derivatives are statistically independent;
  the exact error is a fourth-order cumulant plus two third-order terms
  (Eq. 3), and the paper concedes it "likely won't become exact under any
  realistic set of assumptions".
- **The structure is in the inverse, not the Fisher.** Viewing F as a
  gradient covariance, each row of F⁻¹ holds regression coefficients, so
  F⁻¹ should be nearly block-diagonal or block-tridiagonal over layers even
  though F is not (Figure 3). The block-tridiagonal inverse is the precision
  matrix of a chain-structured Gaussian graphical model and inverts with
  Kronecker algebra (Section 4.3).
- **Damping does much of the work.** The approximate Fisher is not accurate
  to second order, so plain Tikhonov damping fails; factored Tikhonov
  damping plus re-scaling the proposal under the exact Fisher's quadratic
  model are what make the updates good (Section 6, Figure 7).
- **It is natural gradient in Amari's sense, approximated.** K-FAC takes
  the natural gradient as Amari ([LIT-tmp26jbc](LIT-tmp26jbc.md)) defines it, F⁻¹∇h with F
  the Fisher of the network's predictive distribution, and it needs that
  definition: the whole method is a way to apply F⁻¹ when F is too large to
  form. It uses the model's Fisher, sampling targets from the network, not
  the "empirical Fisher" of training labels, which it argues lacks the
  equivalence with the generalized Gauss–Newton matrix.

## Standing in the record

Filed on 2026-10-03 at the owner's request, for nucleation's line on Fisher
geometry ([ADR-026](../decisions.d/ADR-026.md)). It is the canonical example of the Fisher's Kronecker and
block structure, which the `information-geometry` blurb names. It is an ML
optimizer and so carries `anthology-candidate`; the anthology already holds
two later readings of it, Dangel et al.'s tutorial ([ANTH-LIT-768](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-768.md)) and their
case for exposing curvature as linear operators ([ANTH-LIT-746](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-746.md)).

Papyan's 2020 JMLR paper ([LIT-tmpbfzro](LIT-tmpbfzro.md)) measured K-FAC's per-layer
approximation against the true Fisher of trained classifiers and found its
outliers and mini-bulks "drastically misaligned". Its explanation is that
K-FAC's single Kronecker product multiplies each class's feature mean by
every class's error mean, whereas the Fisher's dominant directions pair a
class's features only with that class's errors. Its proposed fix, CFAC,
averages a Kronecker product per class. That is a finding this paper could
not have made: its own check of the factorization (Figures 2–3) is on one
partially trained 256-20-20-20-20-20-10 tanh network on 16×16 MNIST, and its
experiments are autoencoders, which have no classes.

For the record's question, what block structure in the Fisher is real and
what is imposed, K-FAC supplies the imposed one: block structure by layer,
factorized into input and output sides. Shampoo ([LIT-tmpujqh7](LIT-tmpujqh7.md)) imposes a
similar Kronecker shape on a different matrix, the accumulated gradient
outer product, and Papyan's papers ([LIT-tmptvdrl](LIT-tmptvdrl.md), [LIT-tmpbfzro](LIT-tmpbfzro.md)) measure the
structure that trained classifiers actually have.
