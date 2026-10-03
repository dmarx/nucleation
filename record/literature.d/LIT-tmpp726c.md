---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmpbo4zw](../notes.d/NOTE-tmpbo4zw.md)); worth reading as the source of neural collapse: in the terminal phase of training, last-layer features collapse to their class means (NC1), the centred means form a simplex equiangular tight frame (NC2), the classifier aligns with them (NC3) and the decision becomes nearest class centre (NC4). Measured on 7 datasets × 3 architectures; NC1–NC2 imply NC3–NC4 for the Webb–Lowe and max-margin classifiers, and the simplex ETF is the unique optimal codebook in a vanishing-noise Gaussian channel. It explains Papyan''s Hessian outliers as class means outgrowing collapsing within-class variation.'
title: 'Prevalence of Neural Collapse during the terminal phase of deep learning training'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from arXiv v2 (21 August 2020, 17 pages, main text and
    supplementary proof of Theorem 5); v1 is 18 August 2020. Published in
    PNAS 117(40):24652–24663, online 21 September 2020, DOI
    10.1073/pnas.2015509117, CC BY-NC-ND 4.0 (Crossref). Not held in the
    Anthology of the SOTA: a grep for "2008.08186" and the DOI found
    nothing; neural collapse is mentioned there only in passing, as a
    resemblance in ANTH-THEORY-065 and ANTH-NOTE-272.
tags:
- representation-learning
- learning-theory
- information-geometry
- information-theory
- anthology-candidate
date: '2026-10-03'
published: '2020-08-18'
arxiv: '2008.08186'
doi: '10.1073/pnas.2015509117'
first_author: 'Papyan'
keywords:
- 'neural collapse'
- 'terminal phase of training'
- 'simplex equiangular tight frame'
- 'nearest class center'
- 'self-duality'
- 'variability collapse'
- 'inductive bias'
- 'adversarial robustness'
implementations: []
summary: >-
  Papyan, Han & Donoho (2020), PNAS 117(40). Training past zero error (the
  terminal phase, TPT) drives four linked phenomena in the last layer:
  within-class variability collapses (Tr(Σ_WΣ_B†)/C → 0), centred class
  means become equinorm and equiangular with cosines −1/(C−1), a simplex
  ETF; classifier rows become proportional to the means; and the decision
  becomes nearest class mean. Measured on MNIST, Fashion-MNIST, SVHN,
  CIFAR-10/100, STL10 and ImageNet with VGG, ResNet and DenseNet, 480
  models. Test accuracy and DeepFool robustness keep improving during TPT.
  Theorems: NC1–NC2 imply NC3–NC4 for the Webb–Lowe and Soudry max-margin
  classifiers, and the simplex ETF uniquely maximizes the small-noise
  error exponent.
---

# LIT-tmpp726c: Prevalence of Neural Collapse during the terminal phase of deep learning training

Vardan Papyan, X.Y. Han and David L. Donoho (2020), *PNAS* 117(40):24652–24663 — [ARXIV-2008.08186](https://arxiv.org/abs/2008.08186)

## Key takeaways

- **Four collapses (Section 2J).** NC1, Σ_W → 0; NC2, ‖μc − μG‖ equal for
  all c and ⟨μ̃c, μ̃c′⟩ → (C/(C−1))δcc′ − 1/(C−1); NC3,
  ‖Wᵀ/‖W‖_F − Ṁ/‖Ṁ‖_F‖_F → 0; NC4, argmax ⟨wc′, h⟩ + bc′ → argmin
  ‖h − μc′‖. Figures 2–7 show each decreasing through training, with the
  terminal phase marked where training accuracy reaches 99.9% (99.6% on
  ImageNet).
- **The terminal phase pays.** Median test-accuracy gain from the first
  zero-error epoch to the last is 0.35 percentage points (mean 0.50;
  Table 1), and the median DeepFool robustness gain is 0.0252 (mean 0.2452;
  Figure 8). Not every cell improves: DenseNet on CIFAR-100 and ResNet and
  DenseNet on ImageNet lose test accuracy.
- **Collapse forces the rest (Theorems 2 and 4).** If features have
  collapsed (NC1) onto a simplex ETF (NC2), the optimal MSE classifier of
  Webb and Lowe and the max-margin limit of gradient descent on
  cross-entropy (Soudry et al.) are both self-dual and nearest-class-centre.
- **The ETF is optimal (Theorem 5).** For h = μγ + z, z ~ N(0, σ²I),
  ‖μc‖ ≤ 1 and a linear decoder, the best large-deviations error exponent
  as σ → 0 is C/(C−1)·1/4, attained only by simplex ETFs with the classifier
  equal to the means.

## Standing in the record

Filed on 2026-10-03 at the owner's request, with Papyan's spectra papers.
Its primary topic is `representation-learning`, because its object is the
geometry of learned last-layer features. It also takes `learning-theory`
(inductive bias, generalization in the interpolating regime),
`information-geometry` (it is offered, in Section 7B, as the explanation of
the class outliers in deepnet Hessian spectra, which someone browsing Fisher
and Hessian spectra should find), and `information-theory` (Theorem 5 is a
codebook-design result for a Gaussian channel, in the large-deviations
regime). It is a deep-learning finding, so `anthology-candidate`; the
anthology mentions neural collapse only as a resemblance, in its reading of
token clustering ([ANTH-THEORY-065](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-065.md)).

**Its relation to the spectra papers is explanatory, and no record relation
is declared.** It cites Papyan's preprint ([LIT-tmpnmspc](LIT-tmpnmspc.md)) and ICML paper
([LIT-tmptvdrl](LIT-tmptvdrl.md)) as references 41–42, which "explained how the spectral
outliers could be attributed to low-rank structure associated with
class-means and the bulk could be induced by within-class variations", and
it argues that NC1 and NC2 explain them: as within-class variation goes to
zero the class means dominate and the outliers emerge from the bulk. That
is not `extends` (the collapse measurements stand without the spectra),
not `compared_against` (no spectral comparison is run) and not `corrects`.
In the other direction, the 2020 JMLR paper ([LIT-tmpbfzro](LIT-tmpbfzro.md)), posted nine
days later, does not cite this one, though its finding that feature class
means separate from the bulk and become more orthogonal with depth is the
layer-by-layer approach to what this paper describes at the last layer.

For the owner's line, the point is that the structure Papyan measures in
the Fisher's spectrum has a limit: at full collapse the last-layer feature
matrix has rank C − 1, so the class component of the Fisher is as sharp as
it can be. Nothing in the paper connects that to singular learning theory,
and the record should not either without a reading that does.
