---
status: Read
paper: LIT-tmpl7hwn
title: 'On Linear Mode Connectivity of Mixture-of-Experts Architectures'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v2 (86 pages). Main text in full; Appendices D, E, F
    and the G.4–G.5 tables read; the proofs of Appendices A–C (about 30
    pages) read for statements, assumptions and structure, not verified
    line by line; the G.1–G.3 interpolation galleries sampled. Numbers come
    from the text layer.
date: '2026-10-03'
summary: >-
  G(n) = ℝ^d × ℝ × S_n (common gate translation + expert permutation)
  preserves dense and top-k MoEs and, under genericity, is all of the gate's
  symmetry (Thms 4.1, 4.2, k ≥ 2). Translation leaves barriers unchanged.
  Weight matching = LAP on expert order (centred gates or Gram matrices) +
  per-expert weight matching, O(n³ + nh³). Barriers near zero (One Billion
  Word: 0.0044–0.0066 vs 0.14–0.86 without expert ordering), but only the
  inserted MoE layer is trained; the ViT/GPT-2 backbone is shared and
  frozen.
---


# NOTE-tmp1riqg: On Linear Mode Connectivity of Mixture-of-Experts Architectures

## Contribution

It establishes what symmetries a mixture-of-experts gate has. They are
permuting the experts with their gates and translating all gate rows
together, and, under genericity conditions, nothing else. The proof covers
dense softmax gating and top-k gating with k ≥ 2. It turns that into a
data-free alignment algorithm and shows that MoE layers fine-tuned from
different seeds become linearly connected once aligned.

## Key insight

An MoE's output is a softmax-weighted sum over experts. A sum does not care
about the order of its terms, and a softmax does not care if every score is
shifted by the same amount. Those are the gate's symmetries. The theorems
say that for generic parameters there are no others, so to align two MoE
layers it is enough to match which expert is which and then align each
expert's hidden units. Shifting the gate never affects the barrier, so it
can be ignored.

## Assumptions

- **Experts**: ReLU feed-forward networks, all with one architecture,
  treated as black boxes in the theorems. Symmetries inside an expert are
  outside the theorems and handled by weight matching.
- **Theorem 4.1 (dense)**: experts are pairwise distinct functions; the gate
  differences {W_i − W_j}_{i<j} are pairwise distinct vectors.
- **Theorem 4.2 (top-k, k ≥ 2)**: experts pairwise *strongly* distinct
  (differ on a dense set, which distinct ReLU networks need not); the
  consecutive differences {W_{i−1} − W_i} linearly independent, which
  requires n − 1 ≤ d. Equivalence holds on the open dense set Ω where gate
  scores are distinct.
- **Top-1** is excluded: it has an additional ℝ_{>0} scaling symmetry
  (Eq. 8).
- **Experiments**: pretrained ViT and GPT-2 backbones, frozen; one
  feed-forward layer (first, last, or all) replaced by a randomly
  initialised MoE, and only the MoE fine-tuned, from three or more seeds
  (§6.1, Appendix F). Barrier on the test set at 25 points.

## Key results

- **Propositions 3.1–3.2**: invariance of D and S under G(n); Ω is open and
  dense when the gate rows are distinct (Propositions A.1–A.2).
- **Theorems 4.1–4.2**: functional equivalence implies n = n′ and a
  G(n)-relation, with experts equal everywhere (dense) or on the inputs
  where they are selected (sparse). The proofs use linear independence of
  exponentials (Lemma B.3) and the piecewise-affine structure of ReLU
  networks.
- **Proposition D.1**: B(φ_A, φ_B) = B(φ_A, hφ_B) for any pure translation h.
- **Table 2 (12-layer ViT, 4 experts, CIFAR-10/100)**: the chosen expert
  order ranks between about 2 and 5 out of the 24 possible orders, and its
  scaled excess barrier L̂ is 0.07–3.42 (in units of 1% of the gap between
  naive and best-order barriers).
- **Table 3 / Table 11 (CIFAR-10, ViTs of 2, 4, 6 layers, MoE at each
  layer)**: loss-barrier ratio to naive interpolation 4.16–10.83%.
  Table 12 shows the raw barriers: e.g. two-layer, MoE at layer 1, 0.0314
  against 0.3422 naive.
- **Table 10 (One Billion Word, 12-layer GPT-2)**: barrier with full
  matching 0.0044–0.0066; with expert order skipped 0.14–0.86, across MoE,
  SMoE (k = 2) and DeepSeekMoE (k = 2, one shared expert), 4 or 8 experts.
- **Appendix E**: re-initialising one feed-forward layer of a pretrained ViT
  or GPT-2 hurts most in early layers. That is the stated reason for testing
  first-layer replacement.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | G(n) preserves dense and top-k MoE functions | strong (direct) | Props. 3.1–3.2 |
| C2 | Under genericity, G(n) is all the gate's symmetry (dense; top-k with k ≥ 2) | strong (proof), not verified here line by line; the top-k conditions need n − 1 ≤ d | Thms. 4.1–4.2, App. B–C |
| C3 | Gate translation does not affect barriers, so permutations are what LMC needs | strong for the gate; "permutations suffice for LMC" overall rests on prior work, not on this paper | Prop. D.1, §5.1 |
| C4 | Expert-order + per-expert weight matching yields near-zero barriers between MoE layers trained from different seeds | strong in the tested setting, which has a frozen shared backbone | Tables 3, 10–12 |
| C5 | Expert order matters: without it barriers stay high | strong in that setting | Table 10, Fig. 2 |

## Method

Algorithm 1. Step 1: expert order by LAP on either
C_ij = (‖Ŵ_i − Ŵ′_j‖² + (b̂_i − b̂′_j)²)^{1/2} with centred gate parameters
(Eq. 10), or C_ij = (‖ÃᵢᵀÃᵢ − Ã′ⱼᵀÃ′ⱼ‖²_F + ‖B̃ᵢB̃ᵢᵀ − B̃′ⱼB̃′ⱼᵀ‖²_F)^{1/2} on
permutation-invariant Gram matrices of each expert's weights (Eq. 11).
Step 2: weight matching between hidden units of each matched pair. Both
orderings are returned; they perform comparably.

## Concepts

- **dense MoE / SMoE**: softmax over all n gate scores, or over the top-k.
- **strongly distinct functions**: differ on a dense set of inputs.
- **G(n)**: the group of common gate translations and expert permutations.
- **Expert Order Matching**: Step 1 of Algorithm 1.

## Connections

- **Git Re-Basin ([LIT-tmpd6bma](../literature.d/LIT-tmpd6bma.md))**: Step 2 is its weight matching; Step 1 is
  the same LAP idea at the level of experts.
- **Entezari et al. ([LIT-tmp2uwzo](../literature.d/LIT-tmp2uwzo.md))**: the barrier definition and "winning
  permutation" are theirs, and the paper reads its results as support for
  the convexity conjecture.
- **Ferbach et al. ([LIT-tmpyiw0q](../literature.d/LIT-tmpyiw0q.md)), Sonthalia et al. ([LIT-tmpazv9l](../literature.d/LIT-tmpazv9l.md))**: cited
  for LMC guarantees under optimal transport and for star-shaped regions.
- **Theus et al. ([LIT-tmpfjk24](../literature.d/LIT-tmpfjk24.md))**: the dense-transformer counterpart. There,
  whole independently trained transformers needed orthogonal maps; here the
  transformer is shared and only the MoE layer is aligned.

## Bearing on the record

- It extends the reach of the anthology's [ANTH-SOTA-217](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-217.md) to MoE layers, with
  one more alignment step (expert order). The evidence comes from a frozen
  shared backbone, which the anthology entry would need to state.
- Not a THEORY source on its own. Its theorems are about function
  equivalence, and its empirical setting does not test whether independently
  trained MoE transformers share a basin.

## Limitations

- **Shared frozen backbone.** Only the inserted MoE layer differs between
  the endpoints. The paper does not test independently trained MoE models.
- **Experts as black boxes.** Symmetries inside experts beyond hidden-unit
  permutation, and the top-1 case, are not covered.
- **No barrier bound.** The authors note their method gives no theoretical
  bound on the barrier (§7).
- **Genericity.** The theorems exclude degenerate parameters by assumption.
  Whether trained MoEs satisfy the conditions, for example with shared or
  collapsed experts, is not checked.

## Open questions

- Do independently pre-trained MoE transformers become linearly connected
  under expert-order matching plus the residual-stream symmetries of Theus
  et al.?
- What is the full symmetry group of top-1 routing?

## Corrections

- none to a seeded skim (there was no seed)
