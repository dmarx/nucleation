---
number: 278
status: Active
formerly:
- THEORY-tmpqg4nq
title: 'Under MSE loss, in Han, Papyan and Donoho''s VGG, ResNet and DenseNet runs on five balanced ten-class datasets, the trained classifier stays near the least-squares classifier for its own features from an early epoch; and on that central path, for unconstrained features continually renormalized to identity within-class covariance and without weight decay, gradient flow drives the class-separation singular values to infinity at equal rates, which in that model is neural collapse'
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision
    for THEORY-278 (batch 038, ADR-047 v2 and v3). The measured half is
    narrowed to what LIT-974 measured: fifteen cells, balanced ten-class
    datasets, one run each, with the authors' "negligible" kept as
    theirs. The derived half (Lemma 1, Proposition 2, Corollaries 1 and
    2) was re-derived step by step, in the dated note below, and it now
    says "without weight decay", as the theory assumes. The promote_when
    asked whether ordinary training follows the renormalized flow, and
    whether the central path holds in untested settings. This account
    claims neither, and the request moves unchanged to
    QUESTION-181.
- version: 3
  date: '2026-10-20'
  note: >-
    Dated note added under ADR-047 v4 (the narrowing-loss sweep, batch
    067). The wider claim this entry's narrowing dropped, the proposal
    that trained networks themselves follow the renormalized central-path
    dynamics to neural collapse, which rests on the unmeasured assumption
    A3, is now carried by THEORY-797, which extends this entry.
    Status and title are unchanged.
tags:
- learning-theory
- representation-learning
- loss-landscapes
date: '2026-10-14'
source:
- LIT-974
summary: >-
  Han, Papyan & Donoho (2021), [LIT-974](../literature.d/LIT-974.md), read in [NOTE-783](../notes.d/NOTE-783.md). MSE loss
  splits exactly into a least-squares term and a non-negative deviation
  term, and the deviation becomes negligible early in training in 15
  dataset–network cells. On that central path, with λ = 0, the loss is
  ½ Σ 1/(ω_j² + C) in the singular values of Σ_W^(−1/2)M̃. Under a flow
  that re-whitens the features after every step, each ω_j grows as
  (4t/N)^(1/4), and their ratios tend to 1. That is NC1 and NC2, and NC3–NC4
  follow. Not shown: that ordinary training is this flow, or anything for
  cross-entropy or with weight decay.
extended_by:
- THEORY-797
bears_on:
- QUESTION-051
---
<!-- inactive-ok-file: THEORY-083 THEORY-209 THEORY-039 THEORY-286 — Proposed; the record's statement of collapse, its account of limiting dynamics, its comparison of late phases, and the imbalance account filed beside this one -->
<!-- inactive-ok-file: THEORY-797 — Proposed; the wider proposal this entry's narrowing dropped, filed apart under ADR-047 v4 and extending this one -->

# THEORY-278: Under MSE loss, in Han, Papyan and Donoho's VGG, ResNet and DenseNet runs on five balanced ten-class datasets, the trained classifier stays near the least-squares classifier for its own features from an early epoch; and on that central path, for unconstrained features continually renormalized to identity within-class covariance and without weight decay, gradient flow drives the class-separation singular values to infinity at equal rates, which in that model is neural collapse

## Source

Han, Papyan & Donoho (2021, ICLR 2022), [LIT-974](../literature.d/LIT-974.md), read in [NOTE-783](../notes.d/NOTE-783.md):
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
  [THEORY-286](THEORY-286.md).
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
- **[THEORY-286](THEORY-286.md)** is the imbalance geometry for cross-entropy. Both
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

## Note of 2026-10-19: the renormalized dynamics, re-derived

From [LIT-974](../literature.d/LIT-974.md) App. D (arXiv v4, pp. 25–31). The features X are kept on the
manifold X C Xᵀ = I_C, where C = (1/CN)(I − YᵀY/N) centres within classes.
They follow the gradient flow projected onto that manifold's tangent space.

- **The loss.** In aligned SNR coordinates, Ω = (1/N) X Yᵀ is diagonal,
  and ω_j = (1/N) x_jᵀ y_j for the j-th rows x_j and y_j of X and of the
  label-indicator matrix Y. Each direction contributes
  (1/C)(ω²/(ω²+C) − 1)² + ω²/(C+ω²)² = 1/(ω²+C), so L = ½ Σ 1/(ω_j² + C).
- **The flow.** The projected differential of ω_j involves only x_j, and
  dx_j/dt = (ω_j/(C+ω_j²)²)((1/N) y_j − ω_j C x_j). Since Y y_j = N e_j,
  C y_j = 0. Hence dω_j/dt = (1/N) y_jᵀ dx_j/dt = (1/N) ω_j/(C+ω_j²)².
  The same computation gives (dΩ/dt)_jk ∝ δ_jk. So Ω stays diagonal in
  the basis it entered the path with, and the singular vectors do not
  move.
- **Integration.** Separating variables, (C+ω²)²/ω dω = dt/N, gives
  C²N log ω_j + CN ω_j² + (N/4) ω_j⁴ = a_j + t.
- **Limits.** ω_j increases. It cannot stay bounded while the right side
  grows, so ω_j → ∞. The quartic term then dominates, giving
  ω_j/(4t/N)^(1/4) → 1 for every j, and max ω_j / min ω_j → 1.
- **Collapse.** With Σ_W held at I, Σ_B grows like ω², so Σ_B†Σ_W → 0
  (NC1). The whitened class means tend to a multiple of U₀V₀ᵀ. Their Gram
  matrix tends to a multiple of I − 11ᵀ/C, a simplex ETF (NC2). NC3 and
  NC4 follow on the central path by [LIT-618](../literature.d/LIT-618.md)'s Theorem 1, which is cited,
  not re-derived.

The measured half was not re-derived. It rests on Figure 2, which the
record holds through its caption and the text's statement that L⊥_LS
"becomes negligible compared to" L_LS "starting from an early epoch in
training and persists into TPT".

## Note of 2026-10-20: the wider claim, filed apart

Under [ADR-047](../decisions.d/ADR-047.md) v4, what this entry's narrowing dropped is filed as its own
Proposed entry, so that evidence can later confirm or reject it as a
thesis. [THEORY-797](THEORY-797.md) carries the proposal that trained networks themselves follow the renormalized central-path dynamics to neural collapse, which rests on the unmeasured assumption A3. It extends this entry, whose
measured or derived content is its evidence. Nothing here changes.
