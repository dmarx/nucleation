---
number: 286
status: Proposed
formerly:
- THEORY-tmptj5wo
promote_when: >-
  Two kinds of result, one for each link that is not yet shown. First, a
  proof that gradient descent on the unregularized unconstrained-features
  cross-entropy loss converges in direction to the UF-SVM's global
  minimizer under STEP imbalance, or a counterexample: the authors'
  conjecture C1. Second, measurements in networks trained past zero error
  under imbalance, with several seeds and with augmentation and weight
  decay varied. These should show the classifier and centred-mean Gram
  matrices approaching the SELI or λ-SELI prediction, with the norm ratios
  of Lemma 3.1 and the angles of Eq. 4, and the gap closing more slowly as
  R grows. The account is refuted if imbalanced training approaches the
  ETF more closely than SELI, or if trained logits stay far from a scaling
  of the SEL matrix once training error is zero. More UFM simulations
  cannot settle it, nor can single-seed runs at one weight decay.
title: 'Under class imbalance the last-layer geometry that unregularized cross-entropy prefers is not the simplex ETF but simplex-encoded-label interpolation: the logits equal the simplex-encoded labels, the classifier and embedding Gram matrices come from that matrix''s SVD, any finite weight decay changes the geometry, and training approaches it more slowly as imbalance grows'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    At the owner's direction, carrying out the promotion audit's decision
    for THEORY-286 (batch 024, ADR-047), the UF-SVM geometry under step
    imbalance (LIT-994 Theorem 1 and Corollary 1.3) is filed apart as
    THEORY-738, Active, re-derived by a dual certificate (ADR-047 v2).
    This THEORY extends it and keeps the gradient-descent conjecture, the
    ridge results and the measurements of trained networks. Its
    promote_when already concerned only those and is unchanged. The status
    stays Proposed.
tags:
- representation-learning
- learning-theory
- loss-landscapes
date: '2026-10-14'
source:
- LIT-994
summary: >-
  Thrampoulidis et al. (2022), [LIT-994](../literature.d/LIT-994.md), read in [NOTE-764](../notes.d/NOTE-764.md). For the
  unconstrained-features max-margin problem under STEP imbalance, every
  solution has logits ŴᵀĤ = Ẑ (one-hot minus 1/k), ĤᵀĤ = UΛUᵀ and
  ŴᵀŴ = VΛVᵀ from Ẑ's SVD (Theorem 1). This is the ETF only if the data
  are balanced or binary. No finite ridge gives it under imbalance
  (Proposition 1), though the ridge path tends to it (Proposition 2).
  ResNet-18 and VGG-13 runs sit closer to SELI than to the ETF, and
  approach it more slowly at larger R. Not shown: that gradient descent
  reaches it, and anything with more than one seed.
extends:
- THEORY-738
bears_on:
- QUESTION-051
---
<!-- inactive-ok-file: THEORY-083 THEORY-209 — Proposed; the record's statement of collapse, its account of limiting dynamics, and the MSE account filed beside this one -->

# THEORY-286: Under class imbalance the last-layer geometry that unregularized cross-entropy prefers is not the simplex ETF but simplex-encoded-label interpolation: the logits equal the simplex-encoded labels, the classifier and embedding Gram matrices come from that matrix's SVD, any finite weight decay changes the geometry, and training approaches it more slowly as imbalance grows

## Source

Thrampoulidis, Kini, Vakilian & Behnia (2022, NeurIPS), [LIT-994](../literature.d/LIT-994.md), read in
[NOTE-764](../notes.d/NOTE-764.md): Theorem 1 and Corollaries 1.1–1.3, Lemma 3.1, Eq. 4,
Theorem 2, Propositions 1–2, §4.4, Figures 2 and 4–7, Tables 2–3,
Appendices F–H.

## What was actually shown

**The preferred geometry (proved).** In the unconstrained-features model
(UFM), take k classes with (R, ρ)-STEP imbalance and d ≥ k − 1. Let
(Ŵ, Ĥ) solve the max-margin problem
min ½‖W‖²_F + ½‖H‖²_F s.t. (w_(y_i) − w_c)ᵀh_i ≥ 1. Then (Theorem 1):

- the logits are ŴᵀĤ = Ẑ, with Ẑ[c, i] = 1 − 1/k if c = y_i and −1/k
  otherwise, so every margin is equal;
- ĤᵀĤ = UΛUᵀ and ŴᵀŴ = VΛVᵀ, where Ẑᵀ = UΛVᵀ;
- the embeddings collapse to their class means at any imbalance
  (Corollary 1.1).

This is the ETF exactly when R = 1 or k = 2 (Corollary 1.3). Otherwise,
at ρ = 1/2, majority classifiers are longer than minority ones and
majority embeddings shorter (Lemma 3.1). The minority classifiers' cosine
is (R − 7)/(R − 7 + 2k(2 + √((R+1)/2))): −1/(k−1) at R = 1, rising with R,
and below 1 for every finite R (Eq. 4).

**Regularization matters (proved).** With ridge λ > 0 the landscape is
benign: every stationary point is a strict saddle or a global minimum
(Theorem 2, extended from Zhu et al.). Under imbalance with k > 2, no
finite λ makes the minimizer a scaling of SELI, because SELI would need all
singular values of Ẑ equal (Proposition 1). As λ → 0 the normalized logits
tend to Ẑ/‖Ẑ‖_* (Proposition 2). For balanced data the geometry is the ETF
at every λ. A one-layer linear classifier is proportional to Ẑ at every λ,
so the λ-dependence comes from the two-factor parametrization (§4.4).

**Measured.** In the UFM under SGD without weight decay, the distance to
SELI falls over 10⁵ epochs and stays below the distance to ETF. The fall is
slow, slower at larger R, and slower for embeddings than for classifiers
(Figure 5). ResNet-18 and VGG-13 were trained past zero error on
STEP-imbalanced MNIST, Fashion-MNIST and CIFAR10, R ∈ {1, 5, 10, 100}, with
weight decay 5 × 10⁻⁴. In these runs NC1 falls at every R (Figure 13). The
classifier, centred-mean and logit Gram matrices end closer to SELI than to
the ETF, and less close as R grows (Figures 2, 6). The majority-to-minority
classifier norm ratio matches Lemma 3.1 (Figure 7). Each of these could
have come out the other way: imbalanced training could have stayed near
the ETF, or matched neither.

## What this does not say

- **It does not say gradient descent reaches SELI.** Gradient descent on
  unregularized cross-entropy converges in direction to a KKT point of the
  non-convex max-margin problem, not provably its global minimum. The
  authors leave convergence as conjecture C1.
- **It does not say trained networks are at SELI.** Under the weight decay
  the runs used, the proved target is a λ-dependent geometry. The deep nets
  are closer to SELI than to the ETF, not at it, and each cell is one run.
- **It does not explain the slowing.** That convergence worsens with R is
  measured, not derived.
- **It does not involve the data beyond class sizes.** Features are free
  variables.
- **It does not say what the geometry costs.** Minority test error rises
  steeply with R (Table 3), but the paper does not tie that to the SELI
  norms or angles.
- **It is not a claim about how to train on imbalanced data.** Loss
  adjustments for imbalance are ML practice and belong to the anthology.

## Connections

- **[THEORY-083](THEORY-083.md)** states the ETF as the limit, measured on balanced data.
  This account is the general statement it reduces to when R = 1. NC1
  survives imbalance, but NC2 does not. [THEORY-083](THEORY-083.md)'s promote_when counts
  an imbalanced replication as evidence about equiangularity. It should
  instead count it as a test of this account.
- **[THEORY-278](THEORY-278.md)** derives collapse dynamics under MSE for balanced
  classes. Neither account holds the data. Together they cover the record's
  derivations of the collapsed geometry, one for each loss.
- **[QUESTION-080](../questions.d/QUESTION-080.md) and [THEORY-209](THEORY-209.md).** Two parts of this account bear on what
  stays fixed at the end of training. Under weight decay and imbalance the
  regularized geometry depends on λ. And approach to the preferred geometry
  is slow, slower with imbalance. So a measured last-layer geometry under
  imbalance depends on the regularizer and on when training stopped.
