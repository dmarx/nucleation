---
number: 523
status: Read
formerly:
- NOTE-tmp9flp3
paper: 'LIT-665'
title: 'ZipIt! Merging Models from Different Tasks without Training'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv HTML of v3: main text, Appendices A–F, and
    Appendix G's theorem, background and proof up to the Hoeffding step,
    after which it states that it follows Entezari et al.'s Appendix D. The
    proof's remaining steps and G.4 (relaxing uniformity) were followed for
    their statements, not checked line by line. Figures were read from
    captions and text.
date: '2026-10-03'
summary: >-
  Merging two differently initialised models trained on disjoint tasks:
  permute-then-average puts the result outside both task basins. Matching
  correlated features within and across models (Eq. 8) and merging only
  the early layers lifts CIFAR-10 (5+5) joint accuracy from 46.2 (Git
  Re-Basin) to 79.1 fully merged and 83.8 at 13/20 layers (ensemble 87.4).
  Fully merged ImageNet-1k (200+200) stays at 8.6; 10/50 layers reaches
  60.9 (ensemble 63.3). Theorem 1 tightens Entezari et al.'s barrier bound
  by (1 − 2Γ)^{1/(2d+4)} for redundancy fraction Γ.
---


# NOTE-523: ZipIt! Merging Models from Different Tasks without Training

## Contribution

It poses merging differently initialised models trained on disjoint tasks
without retraining, and shows permutation-based merging does poorly there. It
generalises the merge from a one-to-one permutation to a pairing of
correlated features anywhere in the concatenated feature space of both models.
It adds partial merging, and a bound showing that within-model merges can
only lower the barrier relative to permutation.

## Key insight

When two models learned different things, a feature in one may have no
partner in the other, but it may have a near-duplicate in its own model.
Collapsing those duplicates frees width that can then hold the other model's
features. And since features diverge with depth, the sensible merge is a
shared early trunk with separate late layers.

## Assumptions

- **Same architecture, different initialisation, disjoint tasks.** No shared
  pretrained checkpoint, except that the DeepLabV3 backbone in App. F was
  itself ImageNet-pretrained before fine-tuning.
- **CIFAR models trained with a CLIP-style loss** onto CLIP text embeddings
  of class names, so both models share an output space (§5.1). App. D shows
  that with ordinary cross-entropy, full merging fails for every method.
- **Correlations from unlabeled data**: activations after each ReLU on part
  of the training set, with training augmentations (App. B). A few hundred
  images suffice.
- **BatchNorm statistics are reset** after merging for all methods,
  following Jordan et al. (REPAIR).
- **Linear merges through ReLU** are an approximation that App. C admits.
- **Theorem 1** (App. G): two-layer ReLU networks f(x) = vᵀσ(Wx) of width h,
  W uniform on [−1/√d, 1/√d], v uniform on [−1/√h, 1/√h], inputs with
  ‖x‖₂ = √d, the setting of Entezari et al.'s Theorem 3.1; redundancy is
  modelled through the zero-type neurons of Simsek et al.

## Key results

- **Main-text bound (Eq. 4):** loss increase of the merged model ≤
  Õ((h/(1 − 2Γ))^{−1/(2d+4)}) for Γ < 0.5, and 0 for Γ ≥ 0.5, against
  Õ(h^{−1/(2d+4)}) for permutation alone. In App. G the same theorem is
  stated as Õ((h²/((r + r′) − h))^{−1/(2d+4)}) when (r + r′) − h > 0, and 0
  otherwise, with r, r′ the widths each network reduces to.
- **CIFAR-10 (5+5), ResNet-20×4** (Table 1a), joint / per-task average:
  Model A 48.2 / 71.0; W. Avg 43.0 / 60.8; Git Re-Basin 46.2 / 79.8;
  Permute 58.4 / 87.4; ZipIt! 20/20 79.1 / 92.1; ZipIt! 13/20 83.8 / 94.6;
  Ensemble 87.4 / 96.6.
- **CIFAR-100 (50+50), ResNet-20×8** (Table 1b), joint: Git Re-Basin 40.9,
  Permute 42.8, ZipIt! 20/20 54.9, 13/20 70.2, Ensemble 73.5.
- **ImageNet-1k (200+200), ResNet-50** (Table 2), joint: Git Re-Basin 3.1,
  Permute 8.6, ZipIt! 50/50 8.6, 22/50 55.8, 10/50 60.9, Ensemble 63.3. The
  same-model budget β "does not matter" here: little redundancy at this
  width.
- **Four datasets** (Stanford Dogs, Oxford Pets, CUB, NABirds; Table 3),
  average per-task: pairs, Permute 35.7, ZipIt! 49/50 37.1, 10/50 68.7,
  Ensemble 75.5; all four at once, 15.3, 16.8, 65.3, 75.5.
- **Matching algorithm** (Table 4, CIFAR-10 joint): identity 43.0, permute
  58.4, K-means 29.1, optimal matching 79.6 (11 minutes), greedy 79.0 (1.1
  s), greedy with α = 0.1 79.1.
- **Width** (Fig. 7b, CIFAR-100): below 4× width ZipIt! equals Permute;
  above it ZipIt! rises towards the ensemble (about 75%) while Permute and Git
  Re-Basin plateau near 45%. At 1.5× width on ImageNet, 37/50 layers rise
  from 33.1 to 49.0 joint (Table 8).
- **Depth** (Table 5): mean cross-model correlation at 7/20, 13/20, 19/20
  layers is 0.50, 0.37, 0.27.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Permute-then-average merges of disjoint-task models land outside both task basins | moderate: shown as a schematic (Fig. 2) and by the accuracy drop, not by measured landscapes | §3, Tables 1–2 |
| C2 | Allowing within-model merges improves merging of disjoint-task models | strong for CIFAR at sufficient width; absent on ImageNet at 1× width | Tables 1, 4; Fig. 7 |
| C3 | Partial merging recovers most of the ensemble's accuracy at lower cost | strong across all settings | Tables 1–3, 9; App. A |
| C4 | Within-model merging gives a strictly tighter barrier bound than permutation when units are redundant | strong in the two-layer random-weight setting; transfer to trained deep nets is argued from Fig. 7b only | Theorem 1, App. G |
| C5 | Feature correlation between two models falls with depth, which is why late layers should stay separate | moderate: one setting | Table 5 |

## Method

1. Concatenate the two models' features at a layer, f^A ‖ f^B, and compute
   pairwise activation correlations over a few hundred images.
2. Greedily pair the most correlated features, without replacement, across
   or within models; a budget β caps the share of within-model pairs, and α
   damps repeated matching when merging more than two models.
3. Build a merge matrix M (rows average each pair) and its pseudoinverse
   unmerge matrix U = 2Mᵀ.
4. Fuse into each weighted layer: W* = M^A W^A U^A_{i−1} + M^B W^B U^B_{i−1}
   (Eq. 8). Propagate M and U through BatchNorm, ReLU, pooling and skip
   connections (App. C).
5. For a partial zip, stop at a stage boundary and feed U to each model's
   remaining layers, which become heads.

## Concepts

- **zip**: the merge-and-unmerge operation of Eq. 8.
- **partial zip / ZipIt!_{n/m}**: n of m layers merged.
- **same-model budget β**: the share of merged features allowed to come from
  one model merging with itself.
- **Γ**: the fraction of features that are redundant within a model.

## Connections

- **Entezari et al. ([LIT-652](../literature.d/LIT-652.md)).** The conjecture that same-task networks
  are linearly mode connected modulo permutation is the premise the paper
  argues does not carry to different tasks. Its Theorem 3.1 and proof are
  the base of this paper's Theorem 1.
- **Git Re-Basin ([LIT-661](../literature.d/LIT-661.md)).** The main baseline, run in its
  weight-matching form; Eq. 8 reduces to its permute-then-interpolate.
- **REPAIR (Jordan et al.)**, not in the record, supplies the activation-
  correlation matching and the BatchNorm reset. The Permute baseline is
  REPAIR without its extra parameters.
- **Garipov et al. ([LIT-673](../literature.d/LIT-673.md)), Draxler et al. ([LIT-653](../literature.d/LIT-653.md)), Frankle et
  al. ([LIT-654](../literature.d/LIT-654.md))** are cited as the mode-connectivity line that merging
  of differently initialised models relies on.
- **Shared-initialisation merging**, including model soups ([ANTH-LIT-675](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-675.md)),
  task arithmetic, TIES-Merging ([LIT-675](../literature.d/LIT-675.md)) and Gueta et al.
  ([LIT-658](../literature.d/LIT-658.md)), is the setting this paper says it does not assume.

## Bearing on the record

- A THEORY candidate with TIES-Merging: merging fails where the two models'
  units do not correspond, whether because features diverge (here, with
  depth and task) or because the updates conflict in sign (TIES). Not filed.
- The anthology's practice [ANTH-SOTA-217](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-217.md) (align permutations before
  averaging) is narrowed by this paper to same-task models. That is a
  report for the anthology's process, not an edit ([ADR-013](../decisions.d/ADR-013.md)).

## Limitations

- Models are small to mid-sized ResNets and VGG11; no transformers.
- The CLIP-style output space makes full-model merging possible on CIFAR;
  with cross-entropy the full merge falls below each original model (App.
  D), so the headline CIFAR numbers depend on that choice.
- Partial zipping trades away the single-model property; at 10/50 layers on
  ImageNet the merged model costs 7.43 GFLOPs against 8.22 for the ensemble
  (Table 2).
- The theorem holds for random two-layer networks; the authors offer Fig. 7b
  as support for its intuition in trained deep networks.

## Open questions

- Does within-model merging help when the models share a pretrained start,
  as in task arithmetic and TIES?
- Can the linear merge through ReLU be corrected (App. C names this as open)?
