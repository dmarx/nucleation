---
status: 'Read'
paper: 'LIT-tmpd6bma'
title: 'Git Re-Basin: Merging Models modulo Permutation Symmetries'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv PDF (v6, 29 pages) through PyMuPDF text
    extraction: §§1–7 and Appendix A, including the proofs of Lemmas 1 and 2,
    the counterexample (A.6), the comparison with greedy matching and
    OT-Fusion (A.7), and merge-many (A.10). Results are mostly in loss and
    accuracy plots, read from captions and the numbers the text gives. The
    anthology's reading of the same paper (ANTH-LIT-333, its NOTE-116) was
    read for comparison.
date: '2026-10-03'
summary: >-
  Weight matching, coordinate descent over per-layer linear assignments
  for an NP-hard objective, aligns independently trained nets in seconds.
  After alignment, MNIST MLPs and wide CIFAR-10 ResNet-20s have zero loss
  barrier; 1×-width models and ImageNet ResNet-50 do not, and LMC appears
  only during training. A two-unit counterexample shows no permutation can
  connect some perfect solutions, so LMC is a property of SGD solutions.
---

# NOTE-tmplgnlz: Git Re-Basin: Merging Models modulo Permutation Symmetries

## Contribution

Fast, practical permutation-alignment algorithms. With them comes the first
demonstration that independently trained ResNets can be linearly connected
with zero barrier, which is direct evidence for Entezari et al.'s conjecture
where that paper had only indirect evidence. The paper also maps where
alignment fails: thin networks, early training, ImageNet at standard width,
and constructed non-SGD solutions.

## Key insight

The number of functionally equivalent relabellings of a network is
astronomically large (Table 1 compares it with the atoms in the universe),
and SGD lands on one of them at random. Choose the relabelling of B that
makes its weights most similar to A's, and for wide networks the straight
line between A and the relabelled B never leaves the basin: the two were in
one basin all along, seen through different labellings.

## Assumptions

- **Models**: same architecture, different initializations and data orders,
  possibly different data (§5.4).
- **Barrier** (Definition 2.2, after Frankle et al.): max over λ of the loss
  on the line minus the mean endpoint loss, for L(Θ_A) ≈ L(Θ_B). The
  authors note it is non-negative and so misreports paths that dip below
  both endpoints (§5.2).
- **Architectures**: MLPs with 3 hidden layers of 512 units (Adam, 1e−3);
  VGG-16 and ResNet-20 with LayerNorm in place of BatchNorm on CIFAR; standard
  ResNet-50 with BatchNorm on ImageNet, with BatchNorm statistics recomputed
  after interpolation (App. A.1–A.3).
- **Normalization** (App. A.4): LayerNorm and InstanceNorm are permutation
  invariant; BatchNorm needs statistics recomputed after merging; GroupNorm
  is not invariant, and alignment should not work with it (untested).

## Key results

- **Activation matching** (§3.1): per layer, argmax over P of ⟨P,
  Z^(A)(Z^(B))ᵀ⟩_F, a linear assignment problem; layers are independent.
- **Weight matching** (§3.2): argmax over π of Σ_ℓ ⟨W_ℓ^A, P_ℓ W_ℓ^B
  P_{ℓ−1}ᵀ⟩_F. Lemma 1: this sum of bilinear assignments is NP-hard, with no
  polynomial-time constant-factor approximation for L > 2 (by reduction from
  the quadratic assignment problem). Algorithm 1: coordinate descent over
  layers in random order; Lemma 2: it terminates. It recovers a known random
  permutation exactly in 3–4 passes (App. A.5).
- **Straight-through estimator** (§3.3, Algorithm 2): learn Θ̃_B, project to
  the nearest permutation of Θ_B in the forward pass, minimize the midpoint
  loss. Best barriers, steepest cost.
- **Barriers after matching** (Fig. 2): zero on MNIST with all three methods;
  zero on CIFAR-10 for ResNet-20 at 32× width; on ImageNet ResNet-50, 67% lower
  than naive interpolation but not zero. The test loss on MNIST becomes convex
  along the line, so the midpoint beats both endpoints.
- **Width** (Fig. 4): barrier after weight matching falls with width for
  VGG-16 and ResNet-20 on CIFAR-10, to zero at large width; 1× models do not
  show LMC.
- **Training time** (Fig. 3): for MLPs on MNIST and CIFAR-10 the barrier after
  matching is high at initialization and falls over training.
- **Counterexample** (App. A.6): data x ∼ U([−1, 1]²), y = 1[x₁ < 0 and
  x₂ > 0]; two hidden layers of two ReLU units; two perfect-fit weight
  settings, each testing the two conditions in opposite layers. All four
  permutations leave a barrier (Fig. 6).
- **Against OT-Fusion** (App. A.7): ImageNet ResNet-50 merged at 51.01% top-1
  against 1.38% for Singh & Jaggi's OT-Fusion; on VGG-11/CIFAR-10, using their
  released weights, 4.5× faster and better. Restricted to one pass over the
  layers, weight matching drops to OT-Fusion's level.
- **Split-data merging** (§5.4, Figs. 5, 10–11): two ResNet-20s on disjoint
  CIFAR-100 subsets (one 20% of labels 0–49 and 80% of labels 50–99, the
  other the reverse) merge into a model with lower test loss than either,
  better calibration, and not better accuracy. Ensembling and full-data
  training remain better.
- **Merge-many** (App. A.10, Table 3, Fig. 13): five MNIST MLPs merged lower
  test loss by 43%; 32 MLPs each on a random half of MNIST merge into a model
  calibrated as well as their ensemble.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Wide enough networks trained independently by SGD can be permuted into zero-barrier linear connectivity | strong for MNIST MLPs and CIFAR-10 ResNet-20/VGG-16 at large width | Figs. 2, 4 |
| C2 | Permutation alone does not linearly connect thin networks | moderate: cannot rule out a better permutation, as the authors say | Fig. 4, §5.3 |
| C3 | LMC modulo permutation emerges during training, not at initialization | moderate: MLPs only | Fig. 3 |
| C4 | Some loss landscapes contain solutions no permutation connects linearly, so LMC depends on the optimizer | strong (construction) for the toy; its embedding in larger models is asserted | App. A.6 |
| C5 | Weight matching is a fast, data-free, effective alignment method | strong | §5.1, App. A.5, A.7 |
| C6 | Merging aligned models trained on disjoint data improves loss and calibration | moderate: one split, one architecture | §5.4 |

## Method

Algorithms 1–3 as above. The paper presents them for bias-free MLPs and
says its implementation also handles biases, residual connections,
convolutions and attention (§3.2); how is not described in the text.

## Concepts

- **re-basin**: permuting a model's units so that it lies in the same basin
  as a reference model.
- **SOBLAP**: the sum of bilinear assignments problem that weight matching
  poses.
- **greedy uni-directional matching**: aligning layer 1, applying it,
  aligning layer 2, and so on in one pass; rejected here (App. A.7).

## Connections

- **Entezari et al. ([LIT-tmp2uwzo](../literature.d/LIT-tmp2uwzo.md)).** The conjecture tested. The paper
  credits it with the single-basin idea and describes its simulated
  annealing as yielding "modest reductions" over "multiple days", against
  seconds here. That paper's own appendix gives 10K seconds for 50K steps,
  so "multiple days" presumably counts its whole sweep.
- **Frankle et al. ([LIT-tmp3owu9](../literature.d/LIT-tmp3owu9.md)).** The barrier definition, and an analogue
  of the onset finding.
- **Benton et al. ([LIT-tmp6yuwj](../literature.d/LIT-tmp6yuwj.md)).** Cited for SGD solutions forming a
  connected volume of low loss.
- **Garipov et al. ([LIT-tmpotq71](../literature.d/LIT-tmpotq71.md)), Draxler et al. ([LIT-tmp3kyq9](../literature.d/LIT-tmp3kyq9.md)).** Non-linear
  mode connectivity.
- **Singh & Jaggi (2020)**, **Tatro et al. (2020)**, **Jordan et al. (REPAIR,
  2022)**, not held: OT-based fusion, alignment before curve finding, and the
  BatchNorm variance collapse that recomputing statistics addresses.
- **Model soups ([ANTH-LIT-675](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-675.md)).** Named as the setting merge-many could serve.

## Bearing on the record

- The strongest source for the THEORY candidate that barriers are mostly
  permutation artefacts, and the source of its limits: width, training time,
  and the dependence on SGD.
- Bears on the candidate that linear connectivity emerges early in training:
  here, modulo permutation, it emerges over training.
- **Disagreement with the anthology's reading ([ANTH-LIT-333](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-333.md), [NOTE-116](NOTE-116.md) there).**
  That reading describes weight matching as "Hungarian algorithm … layer by
  layer" and "greedy", says multi-model merging needs pairwise anchoring,
  reports near-zero barriers across MLPs, CNNs, VGGs and ResNets with merged
  models "within 1–2%" on CIFAR-10, and gives barrier ratios ("baseline ≈
  2–5× endpoint loss; aligned ≈ 0.01–0.1×") and an "O(H³)" cost with a
  limit at H > 10,000. This reading finds the algorithm to be coordinate
  descent over all layers, explicitly contrasted with greedy matching
  (App. A.7). It finds a merge-many algorithm (A.10), zero barriers only at
  large width, and none of the quoted figures in the text. Reported under
  [ADR-013](../decisions.d/ADR-013.md), not fixed here.

## Limitations

- **Thin models and ImageNet** are not linearly connected by these
  permutations, and the paper cannot say whether better permutations exist.
- **The width needed** is large: zero barrier for ResNet-20 at 32× width.
  8× VGG-16 did not fit in GPU memory.
- **Onset results** are for MLPs only.
- **The counterexample's reach** into realistic architectures is argued, not
  shown.
- **Merging on disjoint data** does not beat either input model in accuracy.

## Open questions

- What invariances beyond permutation matter for thin models: cross-layer
  rescaling, general linear maps between activations?
- Why are SGD solutions biased toward linearly connectable ones?
- Does the ImageNet barrier vanish with width, as the authors hypothesize?

## Corrections

- none to a seeded skim (there was no seed)
