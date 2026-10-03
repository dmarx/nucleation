---
number: 83
status: Proposed
formerly:
- THEORY-tmpi6wt0
promote_when: >-
  Replication outside the protocol of LIT-618, read in the record.
  That protocol had balanced classes, no augmentation, dropout removed,
  one run per learning rate and the best run shown. Measurements of NC1
  and NC2 through the terminal phase under augmentation, label noise,
  class imbalance and several seeds per cell would promote this. So would
  a held paper that derives collapse as the limit of gradient descent on
  cross-entropy, which would turn the measured regularity into an
  account. The claim is refuted if standard training run well past zero
  error leaves within-class variability of last-layer features flat, or
  leaves the centred class means far from equiangular. Further runs under
  the original protocol cannot settle it. Nor can the theorems, which
  assume the collapsed end state.
title: 'Training a classifier past zero training error collapses its last-layer features onto their class means and drives the centred means toward a simplex equiangular tight frame, with the classifier aligned to them and the decision becoming nearest class mean'
version: 1
tags:
- representation-learning
- learning-theory
- information-theory
- anthology-candidate
date: '2026-10-03'
source:
- LIT-618
- LIT-613
summary: >-
  Papyan, Han & Donoho (2020), [LIT-618](../literature.d/LIT-618.md), measured 480 trained
  classifiers on seven datasets with VGG, ResNet and DenseNet. Through
  the terminal phase, within-class variability of last-layer features
  falls (NC1), and the centred class means become equinorm and
  equiangular with cosine −1/(C − 1) (NC2). The classifier aligns with them
  (NC3), and the decision becomes nearest class mean (NC4). They prove that
  NC1 and NC2 imply NC3 and NC4 for the MSE-optimal and max-margin
  classifiers, and that the simplex ETF is the unique error-exponent-optimal
  codebook. Papyan (2020), [LIT-613](../literature.d/LIT-613.md), sees class means separate and grow
  more orthogonal with depth. The measurements cover one protocol, and the
  dynamics are unexplained. The paper's further claim, that the Hessian's
  class outliers are a symptom of collapse, is argued and not measured,
  and is left to [THEORY-078](THEORY-078.md).
---
<!-- inactive-ok-file: THEORY-078 THEORY-039 — Proposed; named in Connections, nothing here rests on them -->

# THEORY-083: Training a classifier past zero training error collapses its last-layer features onto their class means and drives the centred means toward a simplex equiangular tight frame, with the classifier aligned to them and the decision becoming nearest class mean

## Source

- Papyan, Han & Donoho (2020), [LIT-618](../literature.d/LIT-618.md), read in [NOTE-476](../notes.d/NOTE-476.md):
  §2J (the four collapses), Figures 2–8, Table 1, Theorems 2, 4 and 5,
  §7B.
- Papyan (2020, JMLR), [LIT-613](../literature.d/LIT-613.md), read in [NOTE-474](../notes.d/NOTE-474.md): Figures 7–10
  (class means of features and errors across layers).

## What was actually shown

**The measurements.** The terminal phase of training (TPT) begins at the
first epoch with 99.9% training accuracy (99.6% on ImageNet), and training
continues while the loss is pushed toward zero. The networks were VGG,
ResNet and DenseNet, on MNIST, Fashion-MNIST, SVHN, CIFAR-10, CIFAR-100,
STL10 and ImageNet. Four quantities fall through TPT ([LIT-618](../literature.d/LIT-618.md),
Figures 2–7):

- NC1: within-class variability relative to between-class, Tr(Σ_W Σ_B†)/C,
  on a log scale, continuing well into TPT;
- NC2: the spread of class-mean norms and of pairwise cosines, and the
  average distance of the cosines from −1/(C − 1), so that the centred
  means approach a simplex ETF;
- NC3: the distance between the normalised classifier and the normalised
  centred means;
- NC4: the disagreement between the network's decision and nearest class
  mean on test data.

The trends are monotone across all 21 cells. Each cell is one trained
model per learning rate, with the best final test error selected
([NOTE-476](../notes.d/NOTE-476.md), Limitations).

**The theorems, which assume the end state.** If features have collapsed
(NC1) onto a simplex ETF (NC2), the MSE-optimal Webb–Lowe classifier and
the max-margin limit of gradient descent on cross-entropy are both
proportional to the centred means. The decision is then nearest class
mean, which gives NC3 and NC4 (Theorems 2 and 4). For a Gaussian channel
h = μ_γ + z with ‖μ_c‖ ≤ 1 and a linear decoder, the simplex ETF with the
classifier equal to the means is the unique configuration that maximises
the error exponent as noise vanishes (Theorem 5).

**Before the last layer.** Papyan (2020) did not cite this paper. He finds
that feature class means separate from the bulk and become closer to
orthogonal with depth, and that error class means do the same toward the
output ([LIT-613](../literature.d/LIT-613.md), Figures 7–10). That is the layer-by-layer approach
to what neural collapse describes at the last layer. It is consistent
with this account and does not test it.

## What this does not say

- **It does not say why.** The theorems take the collapsed state as given.
  Why gradient descent on cross-entropy reaches it is the question the
  authors leave next.
- **It does not say the terminal phase improves generalisation.** The
  median test-accuracy gain from first zero error to the last epoch is 0.35
  points, three of 21 cells lose accuracy, and there are no seeds or
  intervals (Table 1). The robustness gain (Figure 8) is consistent in
  direction, measured with one attack on 100 images.
- **It does not say the Hessian's class outliers are a symptom of
  collapse.** The paper argues it in §7B. Under NC1 the last-layer feature
  matrix tends to rank C − 1, so the class means dominate and the
  outliers leave the bulk. It measures nothing to support the argument.
  The record keeps the measured part, that the outliers sit in the
  class-mean span and separate as between-class variation outgrows
  within-class variation, in [THEORY-078](THEORY-078.md).
- **It covers balanced classes, no augmentation and the last layer.**
  Whether collapse holds with augmentation, label noise, imbalance, or C
  larger than the feature dimension is an open question the paper names.

## Connections

- **[THEORY-078](THEORY-078.md).** The class-mean outliers of the Fisher are the
  spectral face of the class means this account describes. Collapse would
  be the limit in which within-class terms vanish, but the record does not
  hold a measurement joining the two.
- **[THEORY-039](THEORY-039.md)** compares later phases of training reported elsewhere. The
  terminal phase is one more, defined by a different quantity, and is not
  part of that comparison.
- **Information theory.** Theorem 5 is a codebook result for a Gaussian
  channel in the large-deviations regime, which is why this account
  carries `information-theory`.
