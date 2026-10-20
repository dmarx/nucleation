---
number: 476
status: Read
formerly:
- NOTE-tmpbo4zw
paper: 'LIT-618'
title: 'Prevalence of Neural Collapse during the terminal phase of deep learning training'
version: 2
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from arXiv v2 (17 pages): main text, Theorems 2 and 4 with
    their proofs, and the supplementary proof of Theorem 5 through its
    large-deviations lemmas, followed in outline. Figures 2–8 are read from
    their captions and the text; Table 1 is read from the text.
- version: 2
  date: '2026-10-20'
  note: >-
    Figures 2–7 read from the rendered plots of arXiv v2, not only their
    captions (promotion audit, batch 052). What they show is in the dated
    note below. The plots do not bear out "monotone across all 21 cells",
    and on ImageNet the measures level off far from zero.
date: '2026-10-03'
summary: >-
  NC1 Σ_W → 0 (Tr(Σ_WΣ_B†)/C falls), NC2 centred means → simplex ETF
  (cosines → −1/(C−1)), NC3 W ∝ Ṁᵀ, NC4 nearest class mean; 7 datasets × 3
  nets, 480 models. Median TPT gains: +0.35 points test accuracy, +0.0252
  DeepFool robustness. NC1–2 ⇒ NC3–4 for Webb–Lowe and max-margin (Theorems
  2, 4). Optimal small-noise error exponent C/(C−1)·1/4, only at simplex ETFs
  (Theorem 5).
---

# NOTE-476: Prevalence of Neural Collapse during the terminal phase of deep learning training

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

- **Papyan 2018 and 2019 ([LIT-617](../literature.d/LIT-617.md), [LIT-619](../literature.d/LIT-619.md))**, cited as refs.
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

- **The limit of the spectra papers.** Papyan's spectra ([LIT-613](../literature.d/LIT-613.md))
  separate a class component from a within-class bulk; this paper says the
  within-class part of the last-layer features goes to zero and the class
  part becomes a simplex. A THEORY on the Fisher's block structure should
  cite both: one for the decomposition, one for where training drives it.
- **THEORY candidate (not filed):** "Continued training past zero error
  drives a classifier's last layer to the simplex ETF, which is the
  error-exponent-optimal codebook; the Hessian's class outliers are a
  symptom of that convergence." Sources: this paper, with [LIT-619](../literature.d/LIT-619.md) for
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

## Note of 2026-10-20: Figures 2–7 read

Read from the rendered plots of arXiv v2 (promotion audit, batch 052).
Each figure is a 3 × 7 array: VGG, ResNet and DenseNet against MNIST,
Fashion-MNIST, SVHN, CIFAR-10, CIFAR-100, STL10 and ImageNet, one plotted
run per cell, the epoch on the horizontal axis and a red line at the start
of the terminal phase (99.9% training accuracy, 99.6% on ImageNet). The
learning rate is cut tenfold at 1/3 and 2/3 of training (1/2 and 3/4 on
ImageNet), and several of the larger drops sit at those cuts.

- **Fig. 2 (NC2, equinorm).** The coefficient of variation of the centred
  class-mean norms (blue) and of the classifier norms (orange) falls in
  every cell, to near zero on the four easier datasets. It levels off
  around 0.05 for the class means on CIFAR-100, STL10 and ImageNet with
  ResNet, and the blue curves on ResNet CIFAR-100 and STL10 are jagged
  rather than monotone.
- **Fig. 3 (NC2, equiangular).** The standard deviation of the pairwise
  cosines falls from 0.1–0.3 to a plateau, near 0.02 on the easier
  datasets and about 0.05–0.1 for the class means on CIFAR-100, STL10 and
  ImageNet. It does not reach zero in any cell.
- **Fig. 4 (NC2, maximal angle).** The average distance of the cosines from
  −1/(C − 1) falls to near zero in most cells. ResNet on STL10 is the
  exception, ending near 0.1 for the class means.
- **Fig. 5 (NC3).** ‖W̃ᵀ − M̃‖²_F falls to near zero on MNIST through
  CIFAR-10 and CIFAR-100. It ends near 0.1 for ResNet and 0.3 for DenseNet
  on ImageNet, and near 0.15 for DenseNet on STL10. ResNet on CIFAR-100
  has a spike to about 0.25 late in training.
- **Fig. 6 (NC1).** Tr(Σ_W Σ_B†)/C, on a log scale, falls through the
  terminal phase in every cell, often by two or three orders of magnitude:
  to about 10⁻⁴–10⁻³ on MNIST and CIFAR-10 with VGG. On the harder datasets
  it ends higher: about 10⁻²–10⁻¹ on CIFAR-100 and STL10, and about 1
  (ResNet), 2 (VGG) and 10 (DenseNet) on ImageNet, where within-class
  variation is still comparable to or larger than between-class
  variation. Several cells are not monotone: ResNet on CIFAR-10 and
  CIFAR-100 and DenseNet on Fashion-MNIST and SVHN rise and fall after
  the terminal phase begins, and DenseNet on ImageNet rises before it
  falls.
- **Fig. 7 (NC4).** The share of test examples on which the network and
  nearest train class mean disagree falls to near zero on the four easier
  datasets, to about 0.02–0.07 on CIFAR-100 and STL10, and to about 0.1 on
  ImageNet with all three networks.

So the direction of every measure is as the paper says in all 21 cells,
and collapse is close to complete on MNIST, Fashion-MNIST, SVHN and
CIFAR-10. On ImageNet it is partial at the last epoch: NC1's ratio stays
near or above 1 and nearest class mean disagrees with the network on about
a tenth of test examples. The figures give no seeds or intervals, and the
values above are read from the plots, not stated in the text.
