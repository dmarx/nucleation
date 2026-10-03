---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmplvzvr](../notes.d/NOTE-tmplvzvr.md)); worth reading as the paper that explains the C outliers of the deepnet Hessian: the Gauss–Newton/Fisher term G is a second moment, not a covariance, of logit derivatives indexed by (example, class, logit), and the C outliers are the eigenvalues of G₁ = (C−1)·Ave_c δ_c δ_cᵀ, the C class-cluster centres, computable from a C×C Gram matrix without high-dimensional eigenanalysis. The match is empirical, over 18,000 trained models.'
title: 'Measurements of Three-Level Hierarchical Structure in the Outliers in the Spectrum of Deepnet Hessians'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from arXiv v1 (24 January 2019, 10 pages). Published at
    ICML 2019, PMLR 97:5012–5021 (PMLR page checked; the arXiv PDF's
    footer still carries the ICML 2018 template line "PMLR 80, 2018").
    The owner's "Papyan (2019)" is this paper. Not held in the Anthology of
    the SOTA: a grep for "1901.08244" and "Papyan" found nothing.
tags:
- information-geometry
- learning-theory
- anthology-candidate
date: '2026-10-03'
published: '2019-01-24'
arxiv: '1901.08244'
first_author: 'Papyan'
keywords:
- 'Hessian outliers'
- 'Gauss-Newton matrix'
- 'second moment matrix'
- 'logit derivatives'
- 'three-level hierarchy'
- 'class means'
- 'Gram matrix'
- 'random matrix theory'
extends:
- LIT-tmpnmspc
implementations: []
summary: >-
  Papyan (2019), ICML. For a C-class network the Gauss–Newton term of the
  Hessian is G = (1/n)ΔΔᵀ, a second moment (not covariance) of logit
  derivatives δᵢ,c,c′ indexed by example, true class and logit. Grouping
  them into C² group means δc,c′ and C clusters with centres δc gives
  G = G₀ + G₁ + G₂ + G₃ (Eq. 28). The top-C outliers of G are those of
  G₁ = (C−1)Ave_c δcδcᵀ, because clusters are far apart and tight. Early in
  training the group means cluster by logit c′, later by true class c.
  Holds across MNIST, Fashion-MNIST, CIFAR-10 and ImageNet with VGG, ResNet
  and DenseNet; the outliers exceed their approximations slightly, as random
  matrix theory would predict.
extended_by:
- LIT-tmpbfzro
---

# LIT-tmptvdrl: Measurements of Three-Level Hierarchical Structure in the Outliers in the Spectrum of Deepnet Hessians

Vardan Papyan (2019), ICML 2019 — [ARXIV-1901.08244](https://arxiv.org/abs/1901.08244)

## Key takeaways

- **G is a second moment, and that is why it has outliers.** Writing the
  softmax Hessian as (I − 1pᵀ)ᵀdiag(p)(I − 1pᵀ) (Lemma 2.1) gives
  G = (1/n)ΔΔᵀ with columns δᵢ,c,c′ = √pᵢ,c,c′ × (centred logit derivative)
  (Eqs. 13–16). No mean is subtracted, so large means make large
  eigenvalues. G is a second moment of logit derivatives, not of loss
  gradients: δᵢ,c,c is a scaled gradient, but δᵢ,c,c′ for c′ ≠ c are not.
- **The class/cross-class block structure is a two-way layout.** Indexing
  by class c and logit c′ gives C² groups with means δc,c′ and covariances
  Σc,c′; the off-diagonal means of each class form a cluster with centre δc
  and covariance Σc. Then G = Ave_c δc,cδc,cᵀ (G₀) + (C−1)Ave_c δcδcᵀ (G₁) +
  (C−1)Ave_c Σc (G₂) + (1/C)Σ Σc,c′ (G₃) (Eq. 28). The top-C eigenvalues of
  G match those of G₁, and λc(G) ≥ λc(G₁₊₂) ≥ λc(G₁) (Figure 7).
- **Cheap principal subspace.** The outliers can be read from the C×C Gram
  matrix of class centres, "much simpler even than the power method".
- **The structure forms during training.** In ImageNet t-SNE plots, group
  means first cluster by logit coordinate c′, then by true class c, the
  switch near epoch 18 for ResNet50 and 10 for VGG16 (Figure 5).

## Standing in the record

Filed on 2026-10-03 at the owner's request: the owner's "Papyan (2019)",
the first of the two papers he names as the "Fisher-spectrum block
structure, the object being thresholded". The block structure it finds is
in G, which for softmax cross-entropy is the Fisher of the model's
predictive distribution averaged over training inputs (the paper calls it
the Gauss–Newton component; the 2020 paper calls the same matrix the
Fisher Information Matrix).

It extends Papyan's preprint ([LIT-tmpnmspc](LIT-tmpnmspc.md)), and could not stand without
it: the spectral densities in Figure 6 are computed with that paper's
FastLanczos, and its starting point is that paper's finding that the
Hessian's outliers belong to G rather than H. The 2020 JMLR paper
([LIT-tmpbfzro](LIT-tmpbfzro.md)) extends this one in turn.

What it bears on in the record:

- **K-FAC ([LIT-tmpuzob3](LIT-tmpuzob3.md)).** This paper finds the dominant directions of G
  indexed by class, which a per-layer Kronecker factorization does not
  represent; the 2020 paper turns that into a measured failure of K-FAC.
- **Neural collapse ([LIT-tmpp726c](LIT-tmpp726c.md))** cites this paper and its preprint as
  the spectral observation that collapse explains: as within-class
  variability vanishes, class means dominate and the outliers separate.
- `learning-theory`: the paper's motivation includes sharp-minima and
  generalization arguments that use the Hessian spectrum. `anthology-candidate`
  as deep-learning measurement.
