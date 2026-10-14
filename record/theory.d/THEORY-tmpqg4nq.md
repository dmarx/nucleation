---
status: Proposed
promote_when: >-
  A measurement in trained networks that the model's dynamics are the
  ones training follows. Track the singular values ω_j of
  Σ_W^(−1/2)M̃ through the terminal phase of MSE training, without
  imposed re-whitening, on more than one architecture and with several
  seeds. Check that they grow at a common rate, that their ratio tends to
  1, and that the limiting direction is set by the singular vectors early
  in training, as Corollary 2 predicts. A derivation that drops the
  continual renormalization, or that allows weight decay, would also
  promote it. It is refuted if, near the central path, the ω_j spread
  apart or stall while L⊥_LS stays negligible. It is also refuted if the
  deviation from the least-squares classifier stops being negligible in
  settings LIT-974 did not test (augmentation, many classes, imbalance).
  Further closed-form results in the same renormalized model cannot settle
  it, nor can NC1–NC4 curves alone, which any account of collapse
  predicts.
title: 'Under MSE loss a trained classifier stays near the least-squares classifier for its own features, and on that central path, for unconstrained features continually renormalized to identity within-class covariance, gradient flow drives the class-separation singular values to infinity at equal rates, which is neural collapse'
version: 1
tags:
- learning-theory
- representation-learning
- loss-landscapes
date: '2026-10-14'
source:
- LIT-974
answers:
- QUESTION-051
summary: >-
  Han, Papyan & Donoho (2021), [LIT-974](../literature.d/LIT-974.md), read in [NOTE-tmpenm87](../notes.d/NOTE-tmpenm87.md). MSE loss
  splits exactly into a least-squares term and a non-negative deviation
  term, and the deviation becomes negligible early in training in 15
  dataset–network cells. On that central path, with λ = 0, the loss is
  ½ Σ 1/(ω_j² + C) in the singular values of Σ_W^(−1/2)M̃. Under a flow
  that re-whitens the features after every step, each ω_j grows as
  (4t/N)^(1/4), and their ratios tend to 1. That is NC1 and NC2, and NC3–NC4
  follow. Not shown: that ordinary training is this flow, or anything for
  cross-entropy or with weight decay.
---
<!-- inactive-ok-file: THEORY-083 THEORY-209 THEORY-039 THEORY-tmptj5wo — Proposed; the record's statement of collapse, its account of limiting dynamics, its comparison of late phases, and the imbalance account filed beside this one -->

# THEORY-tmpqg4nq: Under MSE loss a trained classifier stays near the least-squares classifier for its own features, and on that central path, for unconstrained features continually renormalized to identity within-class covariance, gradient flow drives the class-separation singular values to infinity at equal rates, which is neural collapse

## Source

Han, Papyan & Donoho (2021, ICLR 2022), [LIT-974](../literature.d/LIT-974.md), read in [NOTE-tmpenm87](../notes.d/NOTE-tmpenm87.md):
Proposition 1, Theorems 1–3, Figure 2, Eq. 7, Lemma 1, Proposition 2,
Corollaries 1–2, and Appendices A–D.

## What was actually shown

**The measured half.** Fix the features H̃ (with a 1 appended for the bias)
and solve for the MSE-optimal classifier,
W̃_LS = (1/C) M̃ᵀ (Σ̃_T + μ̃_G μ̃_Gᵀ + λI)^(−1). The loss then splits exactly:
L = L_LS(H̃) + L⊥_LS(W̃, H̃). Here L⊥_LS is a non-negative quadratic in
W̃ − W̃_LS (Theorem 1), and L_LS = L_NC1 + L_NC2/3 (Theorem 2). In VGG,
ResNet and DenseNet on MNIST, FashionMNIST, SVHN, CIFAR10 and STL10,
trained under [LIT-618](../literature.d/LIT-618.md)'s protocol, L⊥_LS is negligible against L_LS "starting
from an early epoch". It stays so through the terminal phase (Figure 2).
This could have come out the other way: the trained classifier could have
lagged its features' least-squares solution. The same runs show NC1–NC4
under MSE (Figures 3–8).

**The derived half.** On the central path the least-squares predictions are
invariant to any invertible symmetric linear map of the centred features
(Eq. 7). So the features can be whitened to Σ_W = I at no cost, and the
whitened class means are the matrix SNR = Σ_W^(−1/2)M̃. Take the
unconstrained-features model with balanced classes and λ = 0. Let the
features follow a gradient flow projected so that they stay whitened (Eq.
5). Then:

- the loss is L = ½ Σ_(j=1)^(C−1) 1/(ω_j² + C) (Lemma 1);
- each singular value obeys dω_j/dt = (1/N) ω_j/(C + ω_j²)², so
  C²N log ω_j + CN ω_j² + (N/4) ω_j⁴ = a_j + t (Proposition 2);
- every ω_j → ∞ with ω_j/(4t/N)^(1/4) → 1, and max ω_j/min ω_j → 1
  (Corollary 1);
- SNR/ω_max → Û₀V̂₀ᵀ, the singular vectors at entry to the path. That gives
  Σ_B†Σ_W → 0 (NC1) and a simplex ETF of the whitened means (NC2), and NC3
  and NC4 follow by [LIT-618](../literature.d/LIT-618.md)'s Theorem 1 (Corollary 2).

The mechanism is that one scalar law drives every class-separation
direction. The weakest separations grow on the same schedule as the
strongest, so the means equalize as they separate.

## What this does not say

- **It does not say networks train by this flow.** Continual
  renormalization (A3) is imposed, motivated by batch normalization and by
  the invariance. It is not measured. Only proximity to the central path
  (A1) is measured.
- **It does not cover cross-entropy.** The derivation needs the classifier
  in closed form, which only MSE gives. Collapse under cross-entropy is
  still underived in the record, except in the UF-SVM limit of
  [THEORY-tmptj5wo](THEORY-tmptj5wo.md).
- **It does not cover weight decay.** The theory sets λ = 0, where the
  loss has no finite minimum. Every experiment used weight decay.
- **It does not say collapse is reached.** It is a limit at rate t^(1/4),
  with Σ_W full rank throughout.
- **It is about the data only through the labels.** Features are free
  variables, so nothing here says why NC1 stalls near 1 on ImageNet and
  near 10⁻² on CIFAR-10 ([LIT-978](../literature.d/LIT-978.md), §3.3).
- **Balanced classes and ten-class datasets only.** One run per learning
  rate, best test error kept.

## Connections

- **[THEORY-083](THEORY-083.md)** is the measured regularity this account explains, under
  a different loss. Its summary's "the dynamics are unexplained" should now
  read "explained only for MSE, in a renormalized unconstrained-features
  model".
- **[THEORY-tmptj5wo](THEORY-tmptj5wo.md)** is the imbalance geometry for cross-entropy. Both
  explain collapse from the labels alone.
- **[THEORY-209](THEORY-209.md) and [QUESTION-080](../questions.d/QUESTION-080.md).** Here the limiting state is approached
  as a power law, and its orientation is set by the start of the central
  path. In this model, what training leaves depends on when it stops and
  where it entered the path. That is one of the two branches [QUESTION-080](../questions.d/QUESTION-080.md)
  distinguishes. The model has no noise and no weight decay, so it cannot
  meet [THEORY-209](THEORY-209.md) on its own ground.
- **[THEORY-039](THEORY-039.md).** Figure 2 shows an order inside the terminal phase.
  L_NC2/3 falls first and the within-class term afterwards. That phase
  structure is not among those [THEORY-039](THEORY-039.md) compares.
- **Anthology.** MSE training of classifiers is ML practice, and the
  anthology is the place for it. This account claims nothing about which
  loss to use.
