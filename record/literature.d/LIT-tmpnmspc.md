---
status: Active
status_note: 'read 2026-10-03 ([NOTE-tmpf9552](../notes.d/NOTE-tmpf9552.md)); worth reading as the measurement that the bulk-and-C-outliers spectrum of the Hessian persists at full scale (VGG11, 28M parameters), that the outliers belong to the Gauss–Newton/Fisher term G and the bulk mostly to the residual H, and, in its second version, that G splits into class means (outliers) and two bulks (cross-class and within-class variation). Its tools are stochastic Lanczos spectral density estimation without reorthogonalization, plus subspace-iteration deflation.'
title: 'The Full Spectrum of Deepnet Hessians at Scale: Dynamics with SGD Training and Sample Size'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v2 (3 June 2019, 16 pages, "Preprint. Under review");
    v1 is 16 November 2018 and was cited by Papyan's ICML 2019 paper under
    the shorter title "Dynamics with sample size". Only v2 was read. No
    journal or proceedings version found; its content reappears in the 2020
    JMLR paper. Not held in the Anthology of the SOTA: a grep for
    "1811.07062" and "Papyan" found nothing.
tags:
- information-geometry
- learning-theory
- anthology-candidate
date: '2026-10-03'
published: '2018-11-16'
arxiv: '1811.07062'
first_author: 'Papyan'
keywords:
- 'Hessian spectrum'
- 'Gauss-Newton decomposition'
- 'bulk and outliers'
- 'Lanczos'
- 'spectral density estimation'
- 'low-rank deflation'
- 'power law'
- 'sample size'
implementations:
- 'https://github.com/AnonymousNIPS2019/DeepnetHessian'
summary: >-
  Papyan (2018), arXiv. Stochastic Lanczos without reorthogonalization
  (O(Mnp) time, O(p) memory) plus subspace-iteration deflation measures the
  full Hessian spectrum of VGG11 and ResNet18 on MNIST, Fashion-MNIST and
  CIFAR-10/100, over 16,000 trained models. It confirms a bulk with about C
  outliers, attributes the outliers to the Gauss–Newton term G and most of
  the bulk to the residual H, finds H's spectrum symmetric with a power-law
  tail rather than Marchenko–Pastur, and finds H never negligible. Version 2
  decomposes G into class means (outliers), cross-class variation and
  within-class variation (two bulks) and tracks them across epochs and
  sample sizes.
extended_by:
- LIT-tmpbfzro
- LIT-tmptvdrl
---

# LIT-tmpnmspc: The Full Spectrum of Deepnet Hessians at Scale: Dynamics with SGD Training and Sample Size

Vardan Papyan (2018), arXiv preprint — [ARXIV-1811.07062](https://arxiv.org/abs/1811.07062)

## Key takeaways

- **Bulk and outliers at full scale.** Earlier reports (Sagun et al.) used
  networks with thousands of parameters. On VGG11 with 28M parameters, train
  and test Hessians show a bulk and, "arguably", C outliers, plus negative
  eigenvalues in the train Hessian after hundreds of epochs (Figure 2).
- **Outliers come from G, the bulk mostly from H.** With the Gauss–Newton
  split Hess = H + G, where G = Ave ∂fᵀ ∇²ℓ ∂f is the generalized
  Gauss–Newton (for cross-entropy, the Fisher) and H the residual, H has no
  outliers and its spectrum tracks the Hessian's bulk (Figure 3). H is
  "never negligible compared to G", contrary to Sagun et al.'s suggestion
  that Hess ≈ G.
- **H is heavy-tailed.** Its spectrum is nearly symmetric about zero and
  fits φ = 1.2×10⁻⁴|λ|⁻²·⁷ with R² 0.99 (Figure 4), which "can not
  originate from Wigner's semicircle law".
- **G has three levels (v2, Eq. 5).** With gᵢ,c,c′ the gradient of example i
  of class c as if its label were c′, G = A₁ + A₂ + B₁ + B₂: A₁ from the C
  class means (the outliers), B₁ from the spread of cross-class means about
  them (a left bulk), B₂ from within-pair variation (the main bulk), A₂
  negligible (Figure 1). Training longer separates the two bulks; more data
  draws them together (Figure 7).

## Standing in the record

Filed on 2026-10-03 at the owner's request with Papyan's ICML 2019 paper
([LIT-tmptvdrl](LIT-tmptvdrl.md)) and 2020 JMLR paper ([LIT-tmpbfzro](LIT-tmpbfzro.md)). The owner's citation
"Papyan (2019; 2020 JMLR)" names the 2019 and 2020 papers; this preprint is
filed as well because its second version carries the same class/cross-class
decomposition of G, measures the two bulks the ICML paper could not see,
and supplies the spectral-density machinery both later papers use. The two
2019-era papers cite each other: the ICML paper uses this one's FastLanczos
and its attribution of outliers to G, and this one's v2 adopts, "slightly
modified", the ICML paper's decomposition, citing it as "Anonymous [2019]".

It is filed under `information-geometry` because G here is the
Gauss–Newton matrix, equal for softmax cross-entropy to the Fisher, and the
paper is about its spectrum; and under `learning-theory` because the
author's stated motivation is the sharpness–generalization question. A
deep-learning measurement an anthology topic could hold, so
`anthology-candidate`.
