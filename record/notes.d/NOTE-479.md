---
number: 479
status: Read
formerly:
- NOTE-tmplvzvr
paper: 'LIT-619'
title: 'Measurements of Three-Level Hierarchical Structure in the Outliers in the Spectrum of Deepnet Hessians'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from arXiv v1 (10 pages, text layer), including the proof
    of Lemma 2.1 and the derivation of Eqs. 12–28. Figures 3–7 are read
    from their captions and the text; the t-SNE plots and spectral
    densities themselves are not recoverable from the extracted text.
date: '2026-10-03'
summary: >-
  G = (1/n)ΔΔᵀ with δᵢ,c,c′ = column c′ of diag(√p)(I − 1pᵀ)∂f/∂θ. C² group
  means δc,c′, C cluster centres δc; G = G₀ + G₁ + G₂ + G₃ (Eq. 28). Top-C
  eigenvalues of G ≈ those of G₁ = (C−1)Ave_c δcδcᵀ, from a C×C Gram matrix,
  with λc(G) ≥ λc(G₁₊₂) ≥ λc(G₁). 18,000 CIFAR/MNIST models plus ImageNet
  VGG16/ResNet50. Group means switch from clustering by logit c′ to by class
  c during training.
---

# NOTE-479: Measurements of Three-Level Hierarchical Structure in the Outliers in the Spectrum of Deepnet Hessians

## Contribution

An explanation, by exact algebra plus measurement, of why the Hessian of a
C-class network has about C outliers: they are the eigenvalues of the second
moment of C class-cluster centres of logit derivatives. Before it the
outliers were attributed to a "covariance of gradients"; after it they are
known to come from means, and can be approximated without eigenanalysis of a
p×p matrix.

## Key insight

A second moment matrix is a covariance plus the outer product of its mean.
The Gauss–Newton term is a second moment of vectors that carry two labels,
the true class and the logit coordinate, and their means are large, far
apart by class and tight within class. So G looks like a C-rank matrix of
class centres sitting on top of a bulk of within-group noise, and its
spectrum shows exactly that.

## Assumptions

- **Balanced classes** (footnote 1); otherwise G₁₊₂ is a weighted sum.
- **Softmax cross-entropy**, so ∂²ℓ/∂z² = diag(p) − ppᵀ (Böhning 1992) and
  ∂ℓ/∂z = y − p as the paper writes it (Eq. 18).
- **Deterministic training** for the linear algebra: no input
  preprocessing, dropout replaced by batch norm (Section 5.1).
- **Within-cluster variation small against between-cluster variation**:
  this is what makes G₁ carry the outliers, and it is measured, not
  assumed.

## Key results

- **Lemma 2.1.** ∂²ℓ/∂z² = (I − 1pᵀ)ᵀdiag(p)(I − 1pᵀ).
- **Eqs. 13–16.** Δᵢ,cᵀ = diag(√p)(I − 1pᵀ)∂f/∂θ; G = (1/n)ΔΔᵀ =
  Aveᵢ,c Σ_c′ δᵢ,c,c′δᵢ,c,c′ᵀ.
- **Eq. 20.** δᵢ,c,c equals √p_c times the loss gradient; G also contains
  the c′ ≠ c columns, so G is not the second moment of loss gradients.
- **Eq. 23.** G = G₁₊₂ + G₃, means plus within-group covariances; G₁₊₂ has
  rank up to C², but C of its eigenvalues dominate.
- **Eq. 28.** G = G₀ + G₁ + G₂ + G₃ with G₀ = Ave_c δc,cδc,cᵀ,
  G₁ = (C−1)Ave_c δcδcᵀ, G₂ = (C−1)Ave_c Σc, G₃ = (1/C)Σ_c,c′ Σc,c′.
- **Figures 3–4.** t-SNE of δc,c′ shows clusters around each δc for
  DenseNet40 on MNIST, Fashion-MNIST and CIFAR-10 at 13, 702 and 5000
  examples per class, and for VGG16 and ResNet50 on ImageNet; δc,c cluster
  near zero (norms near zero at convergence), except on ImageNet where SGD
  had not converged.
- **Figure 5.** ImageNet, by epoch: clustering by c′ at epoch 1, by c from
  about epoch 18 (ResNet50) and 10 (VGG16).
- **Figure 6.** ResNet18: outliers of G match eigenvalues of G₁₊₂, whose
  top C match G₁; G₀ is negligible.
- **Figure 7.** VGG11 scree plots: λc(G) ≥ λc(G₁₊₂) ≥ λc(G₁), with
  λc(G₁₊₂) and λc(G₁) "usually very close".
- **Scale of the sweep (Eq. 29).** 3 datasets × 3 networks × 20 sample
  sizes × 100 learning rates = 18,000 trained models.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | G is a second moment of logit derivatives, not a covariance and not a second moment of loss gradients | strong (algebra) | Lemma 2.1, Eqs. 13–20 |
| C2 | G decomposes exactly into the four terms of Eq. 28 | strong (algebra) | Eqs. 21–28 |
| C3 | The top-C outliers of G are approximately the eigenvalues of G₁ | moderate to strong: many datasets, networks and sample sizes, but by plot comparison; G's outliers exceed the approximation by a small margin | Figures 6–7 |
| C4 | Cluster members are tight around far-apart centres | moderate: t-SNE, which does not preserve distances | Figures 3–4 |
| C5 | The class organisation of the means emerges during training, after an initial organisation by logit | moderate: two ImageNet networks, ten random classes | Figure 5 |
| C6 | The excess of the outliers over their approximation is the kind of deviation random matrix theory predicts | weak: asserted, not computed | Section 1.1 item 7, Conclusion |

## Concepts

- **logit derivative δᵢ,c,c′**: the c′-th column of
  diag(√p)(I − 1pᵀ)∂f(xᵢ,c)/∂θ, a centred and probability-weighted
  derivative of logit c′ for example i of class c.
- **group / cluster**: the C² sets {δᵢ,c,c′}ᵢ with means δc,c′; the C sets
  {δc,c′}c′≠c with centres δc.
- **three-level hierarchy**: centres δc, then group means δc,c′, then
  individual δᵢ,c,c′.

## Connections

- **Papyan (2018, [LIT-617](../literature.d/LIT-617.md))** supplies FastLanczos and the attribution
  of the Hessian's outliers to G.
- **Sagun et al. (2016, 2017)** called the outlier-carrying term a
  covariance of gradients; this paper corrects that description.
- **Gur-Ari et al. (2018)** found SGD gradients in the span of the top-C
  Hessian eigenvectors; this paper's G₁ gives that span from class means.

## Bearing on the record

- **The owner's "class/cross-class block structure".** In this paper the
  structure is a two-way layout of logit-derivative vectors (class c ×
  logit c′), whose class-level means make a rank-C, Gram-computable
  approximation to G's top eigenspace. What is "thresholded" in a spectrum
  is, on this account, the gap between the C eigenvalues of G₁ and the bulk
  from G₂ and G₃.
- **THEORY candidate (not filed):** "The C top eigendirections of a trained
  classifier's Fisher are spanned by class-mean logit derivatives, so a
  spectral threshold at the bulk edge selects class-discriminative
  directions." Sources: this paper and [LIT-613](../literature.d/LIT-613.md).
- `anthology-candidate`.

## Limitations

- The decomposition is exact; the claim that G₁ carries the outliers is
  empirical and approximate.
- Training without augmentation or dropout.
- The C² − C mini-bulk from G₂ is predicted by the algebra but not shown;
  the 2020 paper notes it needed log-spectra to see it.
- "We plan to publish our code" — no code at the time of v1.

## Open questions

- Can the deviation of the outliers from their G₁ approximation be computed
  by random matrix theory, as the paper suggests?
- Why do group means organise first by logit and then by class?

## Corrections

- none (there was no seed)
- **Citation detail.** The arXiv PDF's footer reads "Proceedings of the 35th
  International Conference on Machine Learning, Stockholm, Sweden, PMLR 80,
  2018", a template left over from ICML 2018; the paper appeared at ICML
  2019, PMLR 97:5012–5021.
- **Sign.** Eq. 18 gives ∂ℓ/∂z = y − p; for cross-entropy on softmax logits
  it is p − y, as the 2020 paper writes it. The sign does not affect G,
  which is quadratic in these vectors.
