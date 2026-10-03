---
number: 78
status: Proposed
formerly:
- THEORY-tmp034yd
promote_when: >-
  A quantitative measurement of alignment, not another spectral density
  read by eye. Take the principal angles between the top-C eigenvectors
  of a trained classifier's Fisher G and the span of its C class-mean
  logit derivatives, which LIT-619 computes from a C × C Gram matrix.
  Measure them with a tolerance fixed in advance, under training as it is
  practised: data augmentation, dropout, unbalanced classes, and C
  comparable to the width of the last layers. Small angles across such
  settings would promote this. The account is refuted if the angles are
  large under standard training. It is also refuted if knocking out the
  class-mean component leaves the outliers standing. Hessian spectra
  cannot settle it, since their outliers carry the residual term as well.
  Neither can further measurements under the deterministic protocol of
  LIT-617, which the existing evidence already covers.
title: "The top C eigenvalues of a trained C-class classifier's Fisher are carried by the second moment of its class-mean logit derivatives, so a cut at the bulk edge keeps the span of the class means, and they stand clear of the bulk to the extent between-class separation exceeds within-class variation"
version: 1
tags:
- information-geometry
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-03'
source:
- LIT-619
- LIT-613
- LIT-617
summary: >-
  Papyan (2019), [LIT-619](../literature.d/LIT-619.md): for softmax cross-entropy the Gauss–Newton
  matrix G, which is the model's Fisher averaged over inputs, is an
  uncentred second moment of logit derivatives indexed by class and
  logit. It decomposes exactly into four terms (Eq. 28), and its top C
  eigenvalues match those of the class-mean term G₁. Papyan (2020),
  [LIT-613](../literature.d/LIT-613.md), splits those C into one global-mean outlier and C − 1
  between-class ones, finds a C(C − 1) cross-class mini-bulk beneath them,
  and proves the whole pattern for a Gaussian toy model. Papyan (2018),
  [LIT-617](../literature.d/LIT-617.md), supplies the measurements and the attribution of the
  Hessian's outliers to G. The decomposition is algebra. That G₁ carries
  the outliers is measured, by eye, under a training protocol narrower
  than practice. So this is Proposed.
extended_by:
- THEORY-085
---

<!-- inactive-ok-file: THEORY-085 THEORY-083 THEORY-084 — Proposed; named in Connections, nothing here rests on them -->

# THEORY-078: The top C eigenvalues of a trained C-class classifier's Fisher are carried by the second moment of its class-mean logit derivatives, so a cut at the bulk edge keeps the span of the class means, and they stand clear of the bulk to the extent between-class separation exceeds within-class variation

## Source

- Papyan (2019, ICML), [LIT-619](../literature.d/LIT-619.md), read in [NOTE-479](../notes.d/NOTE-479.md): Lemma 2.1,
  Eqs. 13–28, Figures 3–7.
- Papyan (2020, JMLR), [LIT-613](../literature.d/LIT-613.md), read in [NOTE-474](../notes.d/NOTE-474.md): Eq. 6.2 and
  Eq. 6.4, Figures 5–6 (knockouts and dynamics), Lemma 8.1 and Theorem 8.1.
- Papyan (2018, arXiv v2), [LIT-617](../literature.d/LIT-617.md), read in [NOTE-478](../notes.d/NOTE-478.md): Eq. 2,
  Figures 1, 3 and 7.

## What was actually shown

**The object.** The Hessian of a classifier's loss splits into a
Gauss–Newton term G and a residual H ([LIT-617](../literature.d/LIT-617.md), Eq. 2). For softmax
cross-entropy, G is the Fisher information of the network's predictive
distribution averaged over the training inputs. The 2020 paper writes it
as a probability-weighted second moment of "extended gradients" g_{i,c,c′},
the gradient of example i of class c as if its label were c′ ([LIT-613](../literature.d/LIT-613.md),
Eq. 6.2). It is the model's Fisher, with labels drawn from the model, and
not the empirical Fisher at the training labels. The 2018 paper finds
that the Hessian's outliers come from G and its bulk mostly from H, and
that H is never negligible (Figure 3).

**The algebra.** Papyan (2019) writes the softmax Hessian as
(I − 1pᵀ)ᵀ diag(p)(I − 1pᵀ) (Lemma 2.1), so G = (1/n)ΔΔᵀ. The columns
δ_{i,c,c′} are probability-weighted, centred derivatives of logit c′ for
example i of class c (Eqs. 13–16). No mean is subtracted, so G is a second
moment and large means make large eigenvalues. Grouping the δ's by class
and logit gives the exact decomposition G = G₀ + G₁ + G₂ + G₃ (Eq. 28),
with G₁ = (C − 1)·Ave_c δ_c δ_cᵀ the second moment of the C class centres.
G₁ has rank at most C. Its eigenvectors lie in the span of the C
class-mean vectors, and they can be read from a C × C Gram matrix.

**The measurement.** The top C eigenvalues of G match those of G₁, with
λ_c(G) ≥ λ_c(G₁₊₂) ≥ λ_c(G₁) and the last two "usually very close"
([LIT-619](../literature.d/LIT-619.md), Figures 6–7). This holds for MNIST, Fashion-MNIST, CIFAR-10
and ImageNet with VGG, ResNet and DenseNet. The 2020 paper refines it by
knockout ([LIT-613](../literature.d/LIT-613.md), Eq. 6.4 and Figure 5, VGG11 on CIFAR-10).
Removing the class component removes the C outliers. Of these, the
largest belongs to the global mean and C − 1 to the between-class second
moment. Removing the cross-class component removes a mini-bulk of about
C(C − 1) eigenvalues, and removing the within-class component removes the
main bulk.

**The separation.** For multinomial logistic regression on
x = t·e_c + z with z ~ N(0, I), Theorem 8.1 of [LIT-613](../literature.d/LIT-613.md) gives the
expected Fisher's spectrum exactly. It has C outliers, C(C − 2) mini-bulk
eigenvalues and a bulk, and raising the signal-to-noise ratio s = t²
pulls all three apart. In deep networks, longer training separates the
cross-class bulk from the within-class bulk, and more data draws them
together ([LIT-617](../literature.d/LIT-617.md), Figure 7; [LIT-613](../literature.d/LIT-613.md), Figure 6).

**So a threshold at the bulk edge** keeps the span of the class-mean
vectors, which is the global-mean direction plus C − 1 between-class
directions. Whether it also keeps the cross-class mini-bulk depends on
whether it sits above or below it ([NOTE-474](../notes.d/NOTE-474.md)).

## What this does not say

- **It does not say the cut keeps C discriminative directions.** One of
  the C is the global mean, the direction shared by all classes.
- **It does not say a Hessian threshold does the same.** The Hessian adds
  H, whose heavy-tailed, roughly symmetric spectrum shapes the bulk
  ([LIT-617](../literature.d/LIT-617.md), Figure 4).
- **The attribution is by eye, under a narrow protocol.** Knockouts are
  judged by looking at spectral densities, with no alignment metric. The
  networks were trained without augmentation and with dropout replaced by
  batch norm, so that the operators are deterministic. Classes were
  balanced, and C was smaller than the feature dimension. The 2020 paper
  says that otherwise no bulk-and-outlier shape need appear.
- **It does not explain why the means are large.** Papyan, Han & Donoho
  ([LIT-618](../literature.d/LIT-618.md), §7B) argue that neural collapse is the limit of this
  picture. As within-class variation goes to zero, the class means
  dominate and the outliers leave the bulk. That is argued in a paragraph
  and not measured. It is also why the clause about separation in the
  title is scoped to between-class against within-class variation and
  not to collapse ([THEORY-083](THEORY-083.md)).
- **It says nothing about generalisation.** Section 9.4 of [LIT-613](../literature.d/LIT-613.md)
  argues that sharpness measures should look at outlier-to-bulk separation.
  That is a recommendation, not a result.
- **It does not say that a classifier's Fisher is singular in Watanabe's
  sense.** About C² informative directions over a large null space has the
  shape of a degenerate Fisher. These papers measure eigenvalue sizes, not
  the local geometry an RLCT describes ([NOTE-474](../notes.d/NOTE-474.md)).

## Connections

- **[THEORY-085](THEORY-085.md)** extends this account layer by layer, to the
  Kronecker structure of the class directions and what K-FAC does to them.
- **[THEORY-083](THEORY-083.md)** is the last-layer end state the separation clause
  points toward.
- **[THEORY-084](THEORY-084.md)** finds a different block structure in a different
  regime: harmonic-degree blocks in a squared-loss Fisher in the kernel
  regime. The two have not been compared on one network.
