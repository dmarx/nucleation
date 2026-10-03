---
number: 478
status: Read
formerly:
- NOTE-tmpf9552
paper: 'LIT-617'
title: 'The Full Spectrum of Deepnet Hessians at Scale'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v2 (16 pages, text layer): main text, Appendix A
    (derivation of the four-term decomposition), Appendix B (Algorithms
    1–5) and Appendix C (experimental details). v1 was not read, so what
    v1 alone contained is not established here. Figures are read from
    their captions; the extracted text does not carry plotted values.
date: '2026-10-03'
summary: >-
  Hess = H + G (Gauss–Newton). At 28M parameters the Hessian has a bulk and
  about C outliers; outliers are in G, the bulk mostly in H; H is symmetric
  and power-law, φ ∝ |λ|⁻²·⁷ (R² 0.99), not Marchenko–Pastur or semicircle.
  G = A₁ + A₂ + B₁ + B₂ (Eq. 5): C class means give the outliers, cross-class
  spread and within-pair spread give two bulks. FastLanczos costs O(Mnp)
  time and O(p) memory.
---

# NOTE-478: The Full Spectrum of Deepnet Hessians at Scale

## Contribution

Software and measurements that take the Hessian-spectrum observations of
Sagun et al. from networks with thousands of parameters to VGG11 and
ResNet18 with tens of millions, with attribution of each spectral feature to
a component of the Gauss–Newton decomposition, and their dynamics across
training epochs and training-set size.

## Key insight

The Hessian of a trained classifier is two different matrices added
together. The Gauss–Newton part G carries a small number of large,
class-driven directions; the residual H carries a broad, heavy-tailed,
roughly symmetric bulk. Neither is negligible, and they behave differently
as training proceeds and as data grows.

## Assumptions

- **Balanced C-class classification with cross-entropy**, Ave over
  examples i and classes c.
- **Deterministic operators**: no random crops or flips; dropout in VGG
  replaced by batch norm, so Lanczos and subspace iteration apply
  (Appendix C).
- **Stochastic Lanczos quadrature** with M = 128 iterations, a Gaussian
  bump per Ritz value and spectrum normalized to [−1, 1] (Algorithms 2–4);
  M = 2048 for log spectra.
- **"Arguably" C outliers**: the count is read off the plots.

## Key results

- **Eq. 2.** Hess = H + G, H = Ave Σ_c′ (∂ℓ/∂z_c′)∂²f_c′/∂θ²,
  G = Ave (∂f/∂θ)ᵀ(∂²ℓ/∂z²)(∂f/∂θ).
- **Costs.** SlowLanczos O(np² + p³) time, O(p²) memory; FastLanczos
  O(Mnp), O(p); subspace iteration O(TC²np). Ghorbani et al. (2019), with
  reorthogonalization, need M times more of both.
- **Figure 2.** VGG11 train and test Hessians on MNIST, Fashion-MNIST and
  CIFAR-10: bulk, about C outliers, a large mass at zero, negative
  eigenvalues in train; the train and test Hessians differ clearly in
  magnitude.
- **Figure 3.** Outliers present in G, absent in H; bulk of the Hessian
  tracks H; the test Hessian's upper tail and G obey interlacing.
- **Figure 4.** Test H for VGG11 on MNIST (1351 per class): fit
  φ = 1.2×10⁻⁴|λ|⁻²·⁷ (R² 0.99); log spectrum fit φ = 2.6×10⁻⁴|λ|⁻²·².
- **Figure 6.** With fixed sample size, G rises to a peak and then falls
  until negligible against H; the peak coincides with the end of the fast
  drop in training error (Figure 10).
- **Eq. 5 / Appendix A.** G = Σ_c (p_c/nC)g_cg_cᵀ (A₁) + Σ_c (p_c,c/nC)g_c,cg_c,cᵀ
  (A₂) + Σ_c (p_c/nC)Σ_c (B₁) + Σ_c,c′ (p_c,c′/nC)Σ_c,c′ (B₂), with
  probability-weighted means and covariances of gᵢ,c,c′.
- **Figures 1 and 7.** Knocking out A₁ removes the outliers, B₂ the right
  (main) bulk, B₁ the left bulk; A₂ has no visible effect. More epochs
  separate the B₁ and B₂ bulks; more data brings them closer. The authors
  read this as against Chaudhari & Soatto's claim that the gradient
  covariance stays roughly constant.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Bulk-and-outliers structure of the Hessian persists at modern scale | moderate to strong: many datasets and two architectures, 16,000 runs, but outlier count read by eye | Figures 2, 9 |
| C2 | Hessian outliers come from G; the bulk mostly from H | moderate: visual attribution on spectral densities | Figure 3 |
| C3 | H's spectrum is power-law, not a classical RMT law | moderate: one fit on one setting, R² 0.99 | Figure 4 |
| C4 | G's spectrum separates into outliers (class means) and two bulks (cross-class and within-class) | moderate: knockout on one setting (VGG11, CIFAR-10, 136 per class), dynamics on more | Figures 1, 7 |
| C5 | H is never negligible compared to G | moderate | Figure 6 |

## Concepts

- **G (here)**: the generalized Gauss–Newton part of the Hessian; for
  softmax cross-entropy it is the Fisher information averaged over inputs,
  as the 2020 paper states.
- **gᵢ,c,c′**: the gradient of example i of class c as if it belonged to
  class c′; gᵢ,c,c is the ordinary gradient.
- **LowRankDeflation**: estimate the top-C eigenpairs by subspace
  iteration, remove them, and estimate the remaining density by Lanczos.

## Connections

- **Sagun et al. (2016, 2017)** first saw bulk and C outliers on small
  networks; this paper confirms them at scale and disputes their H ≈ 0.
- **Papyan (2019, [LIT-619](../literature.d/LIT-619.md))**, under review concurrently, proposed the
  hierarchical decomposition this v2 adopts with probability weights.
- **Pennington & Bahri (2017), Pennington & Worah (2018)** assume
  Wishart/Marchenko–Pastur forms; the measured H contradicts the classical
  forms.
- **Martin & Mahoney (2018)** on heavy-tailed weight spectra, and
  **Simsekli et al. (2019)** on heavy-tailed gradient noise, are named as
  possibly related to H's power law.

## Bearing on the record

- It is the measurement under the owner's "object being thresholded": the
  spectrum of G, with its outliers attributed to class means.
- It bears on singular learning theory only indirectly: the mass of
  eigenvalues at zero, from p = 28M parameters against 50,000 examples, is
  the empirical face of a degenerate Fisher, but the paper treats it as a
  consequence of p ≫ n, not as a statement about the model's geometry.
- `anthology-candidate`.

## Limitations

- Visual attribution: "knockout" is subtraction followed by looking at a
  spectral density.
- The power-law fit is on one network, dataset and sample size.
- Randomness removed from training (no augmentation, no dropout), so the
  networks studied are not those trained in practice.
- v1 was not read.

## Open questions

- Why does G peak and then shrink relative to H during training?
- What generates H's heavy tail?

## Corrections

- none (there was no seed)
