---
number: 405
status: Active
formerly:
- THEORY-tmp0iif2
title: "Adding one classifier-free guidance term per concept to a diffusion model's unconditional noise prediction samples images that satisfy several concepts at once without retraining, and on synthetic scenes it composes object positions far better than compositional energy-based models but relations no better; the reading of the summed score as the score of a product of experts holds only for concepts conditionally independent given the image, unit weights, a conservative field and the noise-free distribution"
version: 1
tags:
- compositionality
- probabilistic-modeling
date: '2026-10-16'
source:
- LIT-770
summary: >-
  Liu, Li, Du, Torralba & Tenenbaum (2022), [LIT-770](../literature.d/LIT-770.md), read in [NOTE-597](../notes.d/NOTE-597.md).
  CLEVR object positions, 1/2/3 components: 86.42/59.20/31.36% against an
  EBM's 70.54/28.22/7.34%. Relations: 60.40/21.84/2.80% against
  78.14/24.16/4.26%. FFHQ attributes are comparable to LACE. Text-model
  composition (GLIDE, Stable Diffusion) is shown only in figures, with
  attribute confusion and hybrid objects among its listed failures. The
  product is derived at the data distribution and applied at every noise
  level, which [NOTE-597](../notes.d/NOTE-597.md) notes is in general not the score of the noised
  product.
supports:
- CLAIM-123
- CLAIM-321
---
<!-- inactive-ok-file: CLAIM-123 CLAIM-321 — Proposed; the record's own claims that cite this reading, named in Connections -->
<!-- inactive-ok-file: THEORY-117 THEORY-678 — Proposed; neighbouring accounts named in Connections, nothing here rests on them -->

# THEORY-405: Adding one classifier-free guidance term per concept to a diffusion model's unconditional noise prediction samples images that satisfy several concepts at once without retraining, and on synthetic scenes it composes object positions far better than compositional energy-based models but relations no better; the reading of the summed score as the score of a product of experts holds only for concepts conditionally independent given the image, unit weights, a conservative field and the noise-free distribution

## Source

Nan Liu, Shuang Li, Yilun Du, Antonio Torralba and Joshua B. Tenenbaum
(2022), "Compositional Visual Generation with Composable Diffusion
Models", ECCV 2022, [LIT-770](../literature.d/LIT-770.md), read in [NOTE-597](../notes.d/NOTE-597.md).

## What was actually shown

**The rule.** A diffusion model's noise prediction is, up to scale, a
score. If concepts are conditionally independent given the image,
p(x, c₁, …, cₙ) = p(x) Πᵢ p(cᵢ|x), and with p(cᵢ|x) ∝ p(x|cᵢ)/p(x) the
target's score is the unconditional score plus one likelihood-ratio
gradient per concept (Eq. 9). Conjunction (Eq. 11):
ε̂ = ε_θ(x_t, t) + Σᵢ wᵢ (ε_θ(x_t, t|cᵢ) − ε_θ(x_t, t)). With one concept and
w > 1 this is classifier-free guidance. Negation (Eq. 15) divides by the
negated concept's likelihood. All terms come from one network trained
with labels dropped 10% of the time.

**Object positions, CLEVR (Table 1, 5,000 images per setting).** Accuracy
by a classifier trained on real images, 1/2/3 components: this method
86.42/59.20/31.36%, the compositional EBM 70.54/28.22/7.34%; StyleGAN2,
LACE and GLIDE near 0 when composing. FID is best throughout.

**Relations, CLEVR (Table 2).** This method 60.40/21.84/2.80%, the EBM
78.14/24.16/4.26%. Three relations succeed under 3% of the time for every
method. FID is better (26.11 against 58.66 at three).

**Faces (Table 3).** 99.26/92.68/68.86% against LACE's
97.60/95.66/80.88%, with better FID at two and three components.

**What could have come out otherwise.** Composed sampling could have
failed beyond one concept, as single-condition generators do. For
positions it degrades but works; for relations it fails as badly as the
energy-based baseline.

## What this does not say

- **That the composed sample is the product distribution.** The
  correspondence needs conditional independence, which is stated and not
  examined; unit weights, while the method tunes them; a conservative
  score field, which is set aside by citation; and the noise-free
  distribution. The summed scores are used at every noise level, where
  the score of the noised product is not in general the sum of the noised
  conditionals ([NOTE-597](../notes.d/NOTE-597.md)'s observation; no paper the record holds states
  and tests it).
- **That it composes text prompts reliably.** On GLIDE and Stable
  Diffusion there is no metric. The authors list concepts the base model
  does not know, attribute confusion that survives composition ("a bear in
  a red forest" AND "a car" gives a red bear), and fusion into one hybrid
  object (a dog-shaped cloud).
- **That it composes relations.** Relations between objects are the
  obvious case of concepts that are not conditionally independent given
  the image, and they are where it fails.
- **That separately trained models compose.** The authors report limited
  success composing models trained on different data.

## Connections

- **Benchmarks of composition** ([THEORY-522](THEORY-522.md), from [LIT-782](../literature.d/LIT-782.md), [LIT-783](../literature.d/LIT-783.md) and
  [LIT-798](../literature.d/LIT-798.md)). Re-implemented on Stable Diffusion v2, Composable Diffusion is
  the weakest method on most T2I-CompBench categories.
- **Attend-and-Excite** ([THEORY-678](THEORY-678.md), from [LIT-806](../literature.d/LIT-806.md)) reports that its
  conjunction fuses two subjects into one object, qualitatively.
- **Compositional generalisation in recognition** ([THEORY-117](THEORY-117.md), from
  [LIT-667](../literature.d/LIT-667.md)) reaches unseen pairs through a linearly factored representation.
  This method reaches unseen combinations by an additive structure imposed
  at sampling. Both need an independence or additivity assumption to hold;
  the parallel is [NOTE-597](../notes.d/NOTE-597.md)'s, and this paper neither supports nor tests
  [THEORY-117](THEORY-117.md).
- [CLAIM-123](../claims.d/CLAIM-123.md) states the conditional-independence condition at the noisy
  state as the record's own claim, and [CLAIM-321](../claims.d/CLAIM-321.md) cites the relation
  failures.
