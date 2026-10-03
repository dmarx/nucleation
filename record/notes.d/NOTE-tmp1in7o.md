---
status: Read
paper: LIT-tmpqazdt
title: 'Going Beyond Linear Mode Connectivity: The Layerwise Linear Feature Connectivity'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v2 (25 pages) through the PDF text layer. Main text and
    Appendix A read in full with the proofs checked line by line; Appendix
    B read, figures from captions only. The stitching tables (Tables 2–3)
    were read from the text layer. One figure reference in Appendix B.5 is
    broken in the PDF ("see ??").
date: '2026-10-03'
summary: >-
  LLFC: c·f⁽ℓ⁾(αθ_A + (1 − α)θ_B) = αf⁽ℓ⁾(θ_A) + (1 − α)f⁽ℓ⁾(θ_B) for every
  layer ℓ and α, some c > 0. Observed whenever LMC holds (spawning or
  permutation), across MLP, VGG-16, ResNet-20/50. Lemma 1: LLFC ⇒ error ≤ 2ε
  on the path. Theorem 1: weak additivity of ReLU + commutativity
  (W_A H_A + W_B H_B = W_A H_B + W_B H_A) ⇒ LLFC with c = 1. Weight and
  activation matching minimise the two factors of
  (W_A − PW_BPᵀ)(H_A − PH_B).
---

# NOTE-tmp1in7o: Going Beyond Linear Mode Connectivity: The Layerwise Linear Feature Connectivity

## Contribution

Earlier work measured linear mode connectivity by a single number, the loss
or error along the path. This paper measures whole feature maps. It shows
that linear connectivity of the output comes with a much stronger linearity,
in which each layer's features along the path are the interpolation of the
endpoints' features. It identifies two checkable conditions that produce
that linearity, and uses them to explain why Git Re-Basin's permutation
objectives work.

## Key insight

A ReLU network is not linear in its weights, but between two networks that
are linearly connected it behaves as if it were, one layer at a time. That
happens when (a) the two networks switch on the same units for the same
inputs, so ReLU acts linearly on a blend of their pre-activations, and (b)
each layer's weights do the same thing to either network's incoming
features. Permutation matching tries to make (b) true. Matching weights
shrinks one side of the product that must vanish, and matching activations
shrinks the other.

## Assumptions

- **Architecture for the theory**: an L-layer MLP with ReLU, H⁽ℓ⁾ =
  σ(W⁽ℓ⁾H⁽ℓ⁻¹⁾ + b⁽ℓ⁾1ᵀ); convolutions reshaped to matrices. Theorem 1 is
  exact algebra under its two conditions, which are stated on a finite
  dataset.
- **Weak additivity** (Definition 3) is in effect a statement that the two
  networks' pre-activations have the same signs on the data, so ReLU is
  linear on their convex combination. Note 5 distinguishes it from
  single-network stable neurons.
- **LMC pairs** come from spawning after 5 epochs (VGG-16, ResNet-20 on
  CIFAR-10) or 14 epochs (ResNet-50 on Tiny-ImageNet), following Frankle et
  al., or from Git Re-Basin's weight matching, activation matching and STE
  on MLPs and a 32×-wide LayerNorm ResNet-20. VGG is excluded from the
  permutation experiments because it does not reach LMC that way (Appendix
  B.1.2).
- **All measurements on the test set**, after training on the training set.

## Key results

- **LLFC co-occurs with LMC** (Figs. 2–4, 8–15): E_D[1 − cosine_α] is near
  zero in nearly every layer and for every α measured, and far below
  E_D[1 − cosine_{A,B}] between the endpoints. Independently trained,
  non-LMC pairs give much larger values (Fig. 4). The scale coefficient c is
  close to 1 in most cases (Appendix B.2).
- **Lemma 1 (Appendix A.1)**: LLFC at the output and max error ≤ ε at both
  ends ⇒ Err(αθ_A + (1 − α)θ_B) ≤ 2ε. The argument is that a convex
  combination of two logit vectors can only misclassify where one of them
  does. That holds for the argmax, so the bound is sound.
- **Theorem 1 (Appendix A.2)**: weak additivity + commutativity ⇒
  f⁽ℓ⁾(αθ_A + (1 − α)θ_B) = αf⁽ℓ⁾(θ_A) + (1 − α)f⁽ℓ⁾(θ_B) for all ℓ, α.
  The proof is a layer-by-layer induction using bilinearity of (W, H) ↦ WH.
- **Commutativity measured** (Figs. 7, 16–19): Dist_com is negligible next
  to the distance between the two networks' weights (Dist_W) and between
  their features (Dist_H), for spawned and permuted pairs.
- **Permutation methods as commutativity** (§5.2): commutativity between θ_A
  and π(θ_B) is (W_A − P⁽ℓ⁾W_B P⁽ℓ⁻¹⁾ᵀ)(H_A − P⁽ℓ⁻¹⁾H_B) = 0 (Eq. 9). Minimising
  the product directly is a sum of Koopmans–Beckmann QAPs plus bilevel
  matching terms, so NP-hard (Appendix A.3).
- **Stitching without a trained adapter** (Appendix B.4): stitching
  spawned VGG-16 models at any layer gives 6.88–11.84% test error, against
  6.87% and 7.1% for the endpoints (Table 2). For ResNet-20 it gives
  8.99–13.35%, against 8.69% and 8.58% (Table 3).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | When two networks are LMC, they are LLFC in nearly all layers | moderate to strong as an empirical regularity on image classifiers; nothing outside vision tested | Figs. 2–4, 8–15 |
| C2 | LLFC at the output implies LMC (error ≤ 2ε) | strong (short proof) | Lemma 1 |
| C3 | Weak additivity and commutativity imply exact LLFC | strong (proof), but both conditions hold only approximately and the approximate version is not proved | Theorem 1 |
| C4 | Weight and activation matching work because they make commutativity hold | moderate: an algebraic decomposition plus measured small residuals, not a proof that the matchings minimise the product | §5.2, Eq. 9 |
| C5 | Low-rank weights and features are why permutation matching succeeds for wide, well-trained nets and fails for narrow or early ones | weak: an informal linear-algebra argument with singular-value plots | App. B.5, Figs. 20–22 |

## Concepts

- **LLFC**: per-layer feature proportionality along the weight
  interpolation (Definition 2).
- **spawning**: train for k steps, copy, continue with different SGD noise.
- **weak additivity for ReLU**: ReLU distributes over the convex
  combination of the two networks' pre-activations.
- **commutativity**: next-layer weights of either network act the same on
  either network's features, in sum.

## Connections

- **Frankle et al. ([LIT-tmp3owu9](../literature.d/LIT-tmp3owu9.md))**: source of the spawning method and of
  its recipes (5 epochs for CIFAR-10, 14 for Tiny-ImageNet).
- **Git Re-Basin ([LIT-tmpd6bma](../literature.d/LIT-tmpd6bma.md))**: source of the permutation method and the
  checkpoints, and the object of §5.2's reinterpretation.
- **Entezari et al. ([LIT-tmp2uwzo](../literature.d/LIT-tmp2uwzo.md))**: cited for the permutation conjecture.
  LLFC does not test the conjecture; it describes pairs already connected.
- **Lubana et al. ([LIT-tmpl64hd](../literature.d/LIT-tmpl64hd.md))**: the converse direction. Lubana et al.
  prove (one hidden layer) that LMC forces shared activation patterns,
  which is close to this paper's weak additivity condition, reached
  independently.
- **Theus et al. ([LIT-tmpfjk24](../literature.d/LIT-tmpfjk24.md))** cite this work as linking global LMC to
  layer-wise linearity.

## Bearing on the record

- A THEORY candidate: *along a flat linear path between two minima, every
  layer's features are the interpolation of the endpoints' features, so
  weight averaging inside a basin is feature averaging*. Its sources would be
  this paper and Lubana et al.'s Lemma 2.
- No instruction for practice.

## Limitations

- **Description, not cause.** LLFC is shown for pairs already found to be
  LMC; the paper does not say why spawning or matching produces weak
  additivity in the first place.
- **The scale factor c.** Theorem 1 gives c = 1, while Definition 2 needs
  c > 0 to fit the data. The authors attribute the gap to accumulated error
  in the approximate conditions and leave an approximate theorem to future
  work (§6).
- **Image classification only**, as the authors note.
- **Wide models for permutation.** Permutation results use Git Re-Basin's
  32×-wide ResNet-20, where LMC is known to hold.

## Open questions

- Is there a permutation (or a wider symmetry) that minimises the
  commutativity product directly, and does it extend LMC to narrower
  networks?
- Does LLFC hold for transformers and language models?

## Corrections

- none to a seeded skim (there was no seed)
