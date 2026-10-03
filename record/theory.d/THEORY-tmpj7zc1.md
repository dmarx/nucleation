---
status: Proposed
promote_when: >-
  Two kinds of result, one for each half. For the layerwise claim, the
  same measurement outside image classification: transformers and
  language models, linearly connected by spawning, by fine-tuning from a
  shared pretrained model or by alignment. It is refuted by a pair that
  is linearly connected at the output while some intermediate layer's
  interpolated features point away from the interpolated features. For
  the averaging claim, the measurement on the averages practice actually
  uses: soups of many fine-tuned models and SWA iterates, with the
  features of the averaged network compared with the average of the
  members' features. It is refuted if the claim holds for pairs but
  fails for many-model averages. An approximate version of Zhou et al.'s
  Theorem 1, bounding the feature error by the size of the
  weak-additivity and commutativity residuals, would also move it. More
  pairwise image-classifier measurements would not.
title: "Along a low-loss linear path between two networks, every layer's features are the interpolation of the endpoints' features, so averaging weights within a basin averages features"
version: 1
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-10-03'
source:
- LIT-tmpqazdt
- LIT-tmpl64hd
extends:
- THEORY-tmptd1hh
summary: >-
  Zhou et al. (2023), [LIT-tmpqazdt](../literature.d/LIT-tmpqazdt.md): whenever two image classifiers are
  linearly mode connected, by spawning or by permutation, the features of
  nearly every layer of the interpolated network are proportional to the
  interpolation of the endpoints' features. This is layerwise linear
  feature connectivity, and two conditions, weak additivity of ReLU and a
  commutativity of weights with features, imply it exactly. Lubana et
  al.'s Lemma 2, [LIT-tmpl64hd](../literature.d/LIT-tmpl64hd.md), gives the exact one-hidden-layer case:
  linear connectivity between interpolating minima forces shared
  activation patterns, and with shared patterns the hidden features are
  linear along the path. Measured on pairs at three interpolation points,
  image classification only. The step to many-model averages such as
  soups and SWA is not measured.
---
<!-- inactive-ok-file: THEORY-tmptd1hh THEORY-tmp5fzhc — Proposed; the account this one extends, and a sibling named in Connections, nothing here rests on their open parts -->

# THEORY-tmpj7zc1: Along a low-loss linear path between two networks, every layer's features are the interpolation of the endpoints' features, so averaging weights within a basin averages features

## Source

- Zhou, Yang, Yang, Yan & Hu (2023), [LIT-tmpqazdt](../literature.d/LIT-tmpqazdt.md), read in [NOTE-tmp1in7o](../notes.d/NOTE-tmp1in7o.md):
  Definitions 2–3, Lemma 1, Theorem 1, §5.2, Figs. 2–7 and Appendix B.4.
- Lubana, Bigelow, Dick, Krueger & Tanaka (2022), [LIT-tmpl64hd](../literature.d/LIT-tmpl64hd.md), read in
  [NOTE-tmprwelh](../notes.d/NOTE-tmprwelh.md): Lemma 2 and Definition 6 of Appendix F.3.

## What was actually shown

**The regularity.** Zhou et al. ([LIT-tmpqazdt](../literature.d/LIT-tmpqazdt.md)) took pairs of networks
that are linearly mode connected. Some were spawned from a shared checkpoint after 5 epochs
(VGG-16, ResNet-20 on CIFAR-10) or 14 (ResNet-50 on Tiny-ImageNet). Others
were aligned by Git Re-Basin's weight matching, activation matching or STE
(MLPs, a 32×-wide ResNet-20). At α = 0.25, 0.5 and 0.75, they compared the
features f⁽ℓ⁾(αθ_A + (1 − α)θ_B) of each layer ℓ with αf⁽ℓ⁾(θ_A) + (1 −
α)f⁽ℓ⁾(θ_B). The mean of 1 − cosine was near zero in nearly every layer,
and far below the dissimilarity between the endpoints' own features (Figs.
2–3). For independently trained pairs that are not linearly connected, it
was much larger (Fig. 4). This could have come out otherwise: a ReLU
network is not linear in its weights, and output-level connectivity alone
does not require the inside to be linear.

**Why it happens, when it does.** Their Theorem 1 is exact algebra on an
L-layer ReLU MLP over a finite dataset, given two conditions. Weak
additivity: ReLU distributes over the convex combination of the two
networks' pre-activations, which in effect means the same units are on in
both. Commutativity: W_A H_A + W_B H_B = W_A H_B + W_B H_A in every layer.
Together these give the layerwise linearity exactly, with scale 1. Both
conditions are measured to hold approximately, and far better for
connected pairs than for independent ones (Figs. 5–7). Lemma 1 runs the
other way at the output: if the output layer is linear in this sense and
both endpoints err on at most ε of the data, the whole path errs on at
most 2ε. So the layerwise property is strictly stronger than linear
connectivity.

**The exact case.** Lubana et al.'s Lemma 2 ([LIT-tmpl64hd](../literature.d/LIT-tmpl64hd.md), App. F.3)
proves for a one-hidden-layer ReLU network with interpolating minima that
linear connectivity forces identical activation patterns on the data.
That is weak additivity, derived rather than assumed. The rest follows in
one line, which is the record's composition and not a statement of either
paper. With a shared pattern m(x), the hidden features are ϕ(Wᵀx) =
m(x) ⊙ Wᵀx (their Definition 6). A unit on in both endpoints is on at
every point between them, and one off in both is off. So along the path
the hidden features are exactly (1 − t)ϕ(W_αᵀx) + tϕ(W_βᵀx). In this
setting the layerwise claim is a theorem, with no approximation.

**A check from outside the measurement.** Zhou et al. stitched spawned
VGG-16 models together at any layer, with no trained adapter. Test error
was 6.88–11.84%, against 6.87% and 7.1% for the endpoints (App. B.4,
Table 2). ResNet-20 gave 8.99–13.35% against 8.69% and 8.58% (Table 3).
Each network's later layers can read the other's features, which is what
the claim implies.

## What this does not say

- **It does not reach "averaging weights averages features" for the
  averages practice uses.** Every measurement is an interpolation between
  two endpoints. Model soups ([ANTH-LIT-675](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-675.md)) average many fine-tuned models,
  and SWA ([ANTH-LIT-673](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-673.md)) averages iterates along one trajectory. Neither
  is measured. Extending the claim to them needs the conditions to hold
  jointly for every member, which nothing here tests.
- **It does not say why connected pairs satisfy the conditions.** The
  account describes pairs already found to be connected. Why spawning or
  matching produces shared activation patterns is left open.
- **The scale is not 1 in practice.** Definition 2 allows a constant
  c > 0. Theorem 1 gives c = 1. The gap is attributed to accumulated error
  in the approximate conditions, and there is no approximate theorem.
- **It is image classification only**, and the permutation results use
  wide networks, where linear connectivity after alignment is known to
  hold.

## Connections

- **[THEORY-tmptd1hh](THEORY-tmptd1hh.md)**, which this extends. That account's converse half
  says a linear low-loss path, up to symmetry, marks a shared mechanism,
  and rests on Lemma 2's shared activation patterns. This account carries
  the same mechanism from one hidden layer to every layer, and from which
  units are on to what the features are. It does not depend on that
  account's stated direction, that a barrier marks a difference in
  mechanism, and would stand if that direction failed.
- **[THEORY-tmp5fzhc](THEORY-tmp5fzhc.md)** says fine-tuned models sit at the edge of a
  low-loss region and averaging moves inward. Within such a region, this
  account says what the inward move does to the network: it blends the
  members' features. Neither paper connects the two, and the many-model
  case is the one that is missing.
