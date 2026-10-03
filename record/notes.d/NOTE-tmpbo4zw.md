---
status: Read
paper: 'LIT-tmpp726c'
title: 'Prevalence of Neural Collapse during the terminal phase of deep learning training'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from arXiv v2 (17 pages): main text, Theorems 2 and 4 with
    their proofs, and the supplementary proof of Theorem 5 through its
    large-deviations lemmas, followed in outline. Figures 2–8 are read from
    their captions and the text; Table 1 is read from the text.
date: '2026-10-03'
summary: >-
  NC1 Σ_W → 0 (Tr(Σ_WΣ_B†)/C falls), NC2 centred means → simplex ETF
  (cosines → −1/(C−1)), NC3 W ∝ Ṁᵀ, NC4 nearest class mean; 7 datasets × 3
  nets, 480 models. Median TPT gains: +0.35 points test accuracy, +0.0252
  DeepFool robustness. NC1–2 ⇒ NC3–4 for Webb–Lowe and max-margin (Theorems
  2, 4). Optimal small-noise error exponent C/(C−1)·1/4, only at simplex ETFs
  (Theorem 5).
---

# NOTE-tmpbo4zw: Prevalence of Neural Collapse during the terminal phase of deep learning training

## Contribution

A named, measured and widely replicated empirical regularity about trained
classifiers: their last-layer features and classifier converge to a single
rigid, symmetric configuration when training continues past zero error,
together with theorems showing that two of the four properties imply the
other two and that the configuration is the optimal one for a stylised
feature-design problem.

## Key insight

Training past zero error is not idle. It keeps shrinking within-class
variation of the last-layer features until each class is a point, and it
arranges those points as far apart as possible on a sphere: a simplex. Once
that has happened, the linear classifier has nothing left to do but point at
the class means, and classification is nearest mean.

## Assumptions

- **Balanced datasets**: MNIST subsampled to 5000 per class, SVHN to 4600,
  ImageNet to 600; no data augmentation; pixel-wise standardization.
- **Standard training**: SGD, momentum 0.9, weight decay 5×10⁻⁴ (1×10⁻⁴ on
  ImageNet), 350 epochs (300 on ImageNet), two learning-rate drops, the
  learning rate chosen by best final test error from a sweep. Dropout
  replaced by batch norm in VGG and set to zero in DenseNet.
- **TPT onset** = training accuracy 99.9% (99.6% ImageNet), because some
  datasets contain mislabels.
- **Theorem 2**: fixed features, MSE loss, Webb–Lowe optimal classifier,
  plus the NC1–NC2 end state. **Theorem 4**: fixed features, linearly
  separable, gradient descent on cross-entropy converging to max margin
  (Soudry et al. Theorem 7), plus NC1–NC2.
- **Theorem 5**: h = μγ + z ∈ ℝᶜ, z ~ N(0, σ²I), γ uniform, ‖μc‖ ≤ 1,
  linear decoder, error exponent β = −lim σ² log P(error) as σ → 0. The
  ambient dimension is reduced to C by a sufficiency argument.

## Key results

- **Figures 2–4.** Coefficients of variation of class-mean and classifier
  norms fall; the standard deviation of pairwise cosines falls; the average
  |cos + 1/(C−1)| falls: equinorm, equiangular, maximally separated.
- **Figure 5.** ‖W̃ᵀ − M̃‖²_F falls: self-duality.
- **Figure 6.** Tr(Σ_WΣ_B†)/C falls on a log scale and continues falling
  well into TPT.
- **Figure 7.** Disagreement between the network and nearest class mean on
  test data falls toward zero.
- **Table 1.** Test accuracy at first zero error versus last epoch, all 21
  cells; median gain 0.3495 points, mean 0.4984. Three cells decline:
  DenseNet CIFAR-100 (77.19 → 76.56), ResNet ImageNet (65.41 → 64.45),
  DenseNet ImageNet (65.04 → 62.38).
- **Figure 8.** DeepFool robustness Aveᵢ‖r(xᵢ)‖/‖xᵢ‖ on 100 test images
  rises; median improvement 0.0252, mean 0.2452; most of the gain during
  TPT.
- **Theorem 2.** Webb–Lowe W = (1/C)ṀᵀΣ_T†; with Σ_W = 0 and an ETF,
  W = αṀᵀ and the decision is argmin ‖h − μc‖.
- **Theorem 4.** Max-margin with collapsed features reduces to
  min ½‖A‖²_F s.t. (ec − ec′)ᵀAVᵀec ≥ 1, solved by A = V, so W = Ṁᵀ
  (up to scale) and NC4 follows.
- **Theorem 5.** β* = (C/(C−1))·(1/4), attained by M* = √(C/(C−1))(I − 11ᵀ/C)
  with W = M*, b = 0; every optimal M is UM* for orthogonal U.
- **Section 7B.** Under NC1 the last-layer feature matrix tends to rank
  C − 1, so the within-class standard deviation becomes small against the
  class means and the Hessian outliers emerge from the bulk: NC1 with NC2
  "explains these important and highly visible observations".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | NC1–NC4 occur during the terminal phase across standard datasets and architectures | strong for the protocol used: 7 datasets × 3 architectures, monotone trends; one trained model per learning rate, best one shown | Figures 2–7 |
| C2 | TPT improves test accuracy | weak to moderate: small median gain, 3 of 21 cells decline, no seeds or intervals | Table 1 |
| C3 | TPT improves adversarial robustness | moderate: consistent direction, 100 images per cell, one attack | Figure 8 |
| C4 | NC1–NC2 imply NC3–NC4 for the Webb–Lowe and max-margin classifiers | strong (proof), for fixed features at the end state | Theorems 2, 4 |
| C5 | The simplex ETF is the unique optimal codebook for a linear decoder as noise vanishes | strong (proof), for the stated channel model | Theorem 5, SI |
| C6 | Neural collapse explains the class outliers in Hessian spectra | weak to moderate: argued, not measured in this paper | Section 7B |
| C7 | Neural collapse explains the benefits of the interpolating regime | weak: stated as a hypothesis | Conclusion |

## Concepts

- **terminal phase of training (TPT)**: training after the first epoch of
  (effectively) zero training error, while the loss is still pushed toward
  zero.
- **simplex ETF**: C points √(C/(C−1))(I − 11ᵀ/C), up to rotation and
  scale: equal norms, pairwise cosine −1/(C−1).
- **self-duality**: the classifier's rows are proportional to the centred
  class means.
- **NCC**: nearest class-centre decision rule.

## Connections

- **Papyan 2018 and 2019 ([LIT-tmpnmspc](../literature.d/LIT-tmpnmspc.md), [LIT-tmptvdrl](../literature.d/LIT-tmptvdrl.md))**, cited as refs.
  41–42, are the spectral observations Section 7B says collapse explains.
- **Webb & Lowe (1990)** and **Soudry et al. (2018)** are the classifier
  results that Theorems 2 and 4 sharpen by adding learned features at the
  collapse end state.
- **Scattering-transform theory (Bruna & Mallat and others)** aimed at
  suppressing within-class variability by design; NC1 shows SGD achieving
  it.
- **Fisher (1936) LDA**: Webb–Lowe's classifier is LDA with Σ_T in place of
  Σ_W.

## Bearing on the record

- **The limit of the spectra papers.** Papyan's spectra ([LIT-tmpbfzro](../literature.d/LIT-tmpbfzro.md))
  separate a class component from a within-class bulk; this paper says the
  within-class part of the last-layer features goes to zero and the class
  part becomes a simplex. A THEORY on the Fisher's block structure should
  cite both: one for the decomposition, one for where training drives it.
- **THEORY candidate (not filed):** "Continued training past zero error
  drives a classifier's last layer to the simplex ETF, which is the
  error-exponent-optimal codebook; the Hessian's class outliers are a
  symptom of that convergence." Sources: this paper, with [LIT-tmptvdrl](../literature.d/LIT-tmptvdrl.md) for
  the outliers. Its second clause is weakly supported here.
- `representation-learning` first; `anthology-candidate`.

## Limitations

- Last layer only; the paper does not measure earlier layers.
- No augmentation, no dropout: a training protocol narrower than practice.
- One model per (dataset, network, learning rate), with the best final test
  error selected, so the improvement figures are for selected runs.
- Theorems assume the end state; they do not show that training reaches it.
  The authors leave the dynamics to future work.
- The Hessian connection is argued in a paragraph, not measured.

## Open questions

- Why does SGD on cross-entropy reach the collapse state? The paper calls
  this the next question.
- Does collapse hold with augmentation, label noise, imbalance, or C larger
  than the feature dimension?
- Does the Fisher's mini-bulk (cross-class means) also collapse, and what
  does that do to its spectrum?

## Corrections

- none (there was no seed)
