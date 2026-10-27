---
number: 83
status: Active
formerly:
- THEORY-tmpi6wt0
title: 'In Papyan, Han and Donoho''s runs of VGG, ResNet and DenseNet trained with cross-entropy on seven balanced datasets without augmentation, training past zero error shrinks last-layer within-class variability against between-class variability, and moves the centred class means and the classifier toward a common simplex equiangular tight frame and the decision toward nearest class mean, nearly to completion on the four easier datasets and only partly on ImageNet'
version: 3
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision file
    for THEORY-083 (batches 044 and 052, ADR-047 v3). The figures were read
    from the plots, not only their captions (NOTE-476, dated note). The
    title now claims what the plotted runs show: the direction of every
    measure in all 21 cells, collapse close to complete on MNIST,
    Fashion-MNIST, SVHN and CIFAR-10, and partial on ImageNet. The body's
    "monotone across all 21 cells" is corrected. The promote_when,
    replication outside this protocol and a gradient-descent derivation,
    moves unchanged in substance to QUESTION-202.
- version: 3
  date: '2026-10-20'
  note: >-
    Note of 2026-10-20 added: the wider claim this entry's narrowing
    dropped is now filed as THEORY-788, Proposed, which extends
    this one (ADR-047 v4). The title and status are unchanged.
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
  codebook. Read from the plots, collapse is close to complete on the
  four easier datasets and partial on ImageNet at the last epoch. Papyan (2020), [LIT-613](../literature.d/LIT-613.md), sees class means separate and grow
  more orthogonal with depth. The measurements cover one protocol, and the
  dynamics are unexplained outside free-features models. Within them,
  THEORY-278 (LIT-974) derives collapse for MSE under a re-whitened
  flow, and THEORY-286 (LIT-994) gives the cross-entropy endpoint
  under class imbalance. The paper's further claim, that the Hessian's
  class outliers are a symptom of collapse, is argued and not measured,
  and is left to [THEORY-078](THEORY-078.md).
extended_by:
- THEORY-788
bears_on:
- QUESTION-051
---

<!-- inactive-ok-file: THEORY-788 — Proposed; the wider claim this entry's narrowing dropped, cited as open -->
<!-- inactive-ok-file: QUESTION-080 — Proposed or Open; a symmetry account of collapse and the question it bears on, open -->
<!-- inactive-ok-file: THEORY-078 THEORY-039 — Proposed; named in Connections, nothing here rests on them -->
<!-- inactive-ok-file: THEORY-286 — Proposed; derivations in free-features models, cited for the limits they set on this account, not leaned on -->

# THEORY-083: In Papyan, Han and Donoho's runs of VGG, ResNet and DenseNet trained with cross-entropy on seven balanced datasets without augmentation, training past zero error shrinks last-layer within-class variability against between-class variability, and moves the centred class means and the classifier toward a common simplex equiangular tight frame and the decision toward nearest class mean, nearly to completion on the four easier datasets and only partly on ImageNet

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

Every measure moves in the stated direction in all 21 cells, but not
monotonically in all of them, and not to zero everywhere (see the note of
2026-10-20). Each cell is one trained model per learning rate, with the
best final test error selected ([NOTE-476](../notes.d/NOTE-476.md), Limitations).

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
  For imbalance the record now holds an answer in free-features models
  ([THEORY-286](THEORY-286.md), from [LIT-994](../literature.d/LIT-994.md)): NC1 survives, but the equiangular NC2
  holds for balanced or binary classes only. An imbalanced test of NC2
  should be read against that geometry.

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

## Note of 2026-10-13: a symmetry account of collapse

Ziyin (2024), [LIT-1014](../literature.d/LIT-1014.md), read in [NOTE-716](../notes.d/NOTE-716.md), attributes neural
collapse to symmetries of the loss ([THEORY-213](THEORY-213.md)). Symmetric subspaces
are absorbing for gradient training, and favoured when weight decay is
strong. This account's protocol uses weight decay. The paper offers a
mapping, not a derivation: it describes neural collapse only as the
penultimate representation becoming low-rank, and does not address NC1–NC4
as this account defines them. Whether the symmetry account predicts the
simplex equiangular geometry, or only low rank, is open. It bears on
[QUESTION-080](../questions.d/QUESTION-080.md) too: an absorbing collapsed state would stay fixed while
other parameters keep moving.

## Note of 2026-10-20: what the plots show

Promotion audit, batch 052. [NOTE-476](../notes.d/NOTE-476.md) had read Figures 2–7 from their
captions; they are now read from the plots ([NOTE-476](../notes.d/NOTE-476.md), dated note). Collapse
is close to complete on MNIST, Fashion-MNIST, SVHN and CIFAR-10: NC1's
ratio Tr(Σ_W Σ_B†)/C falls to about 10⁻⁴–10⁻² and nearest class mean
agrees with the network on almost every test example. It is partial on
CIFAR-100 and STL10 and clearly incomplete on ImageNet, where the ratio
ends near or above 1 for all three networks and nearest class mean
disagrees on about a tenth of test examples. Several cells rise and fall
after the terminal phase begins, and some of the largest drops coincide
with the learning-rate cuts. The title is narrowed to these runs and to
what they show. Whether collapse holds outside this protocol, and why
training reaches it, is [QUESTION-202](../questions.d/QUESTION-202.md).

## Note of 2026-10-20: the wider claim filed

The promotion audit narrowed this entry to what was shown. Under
[ADR-047](../decisions.d/ADR-047.md) v4 the claim the narrowing dropped, neural collapse as a general law of training past zero error, beyond Papyan, Han and Donoho's protocol, is now filed as
[THEORY-788](THEORY-788.md), Proposed, which extends this entry and takes it as
evidence. This entry's title and status are unchanged.
