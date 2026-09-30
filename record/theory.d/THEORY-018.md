---
number: 18
status: Active
formerly:
- THEORY-tmp053xo
title: 'Softmax training identifies a language model''s final-layer representation only up to an invertible linear map, so no inner product on it is intrinsic, and Park, Choe and Veitch''s causal inner product is fixed by a stipulation'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-09-30'
source:
- LIT-304
- LIT-323
extends:
- THEORY-017
summary: >-
  Park, Choe & Veitch (2023), [LIT-304](../literature.d/LIT-304.md), prove the invariance γ ↦ Aγ + β,
  λ ↦ A⁻ᵀλ (eq. 3.1). They choose M = Cov(γ)⁻¹ by setting a free diagonal
  D = I, and admit they have no principle for choosing D. [NOTE-302](../notes.d/NOTE-302.md) derives,
  and the filer re-checked, that Cov(γ) alone is compatible with every
  positive-definite M. So the paper's remark that most inner products are
  ruled out holds only once the true concept directions are known. Under
  superposition ([LIT-323](../literature.d/LIT-323.md)) no inner product can make all features orthogonal.
---

# THEORY-018: Softmax training identifies a language model's final-layer representation only up to an invertible linear map, so no inner product on it is intrinsic, and Park, Choe and Veitch's causal inner product is fixed by a stipulation

## Source

- Park, Choe & Veitch (2023), [LIT-304](../literature.d/LIT-304.md): §3 (eq. 3.1), Def. 3.1, Thms 3.2 and 3.4, §3.2 and App. D.2, as read in [NOTE-302](../notes.d/NOTE-302.md).
- Supporting: Elhage et al. (2022), [LIT-323](../literature.d/LIT-323.md), as read in [NOTE-278](../notes.d/NOTE-278.md), for the superposition limit.

## What was actually shown

**The invariance, proved in the source.** P(y | x) ∝ exp(λ(x)ᵀγ(y)) is
unchanged by γ ↦ Aγ + β and λ ↦ A⁻ᵀλ, for any invertible A. So the
final-layer context vectors and the unembeddings are identified at best up to
GL(d). Inner products between concept directions are not preserved,
⟨γ̄_W, γ̄_Z⟩ ≠ ⟨Aγ̄_W, Aγ̄_Z⟩, and Euclidean cosine has no meaning until an
inner product is chosen ([NOTE-302](../notes.d/NOTE-302.md), C3).

**The choice, conceded in the source.** A causal inner product is one that
makes causally separable concepts orthogonal (Def. 3.1). Which concepts are
separable is the authors' judgement. Under such an inner product, the Riesz
map sends each concept's unembedding direction to its steering direction
(Thm 3.2). Thm 3.4 assumes d mutually separable concepts whose directions G
form a basis, and uncorrelatedness over the vocabulary. It then gives
M⁻¹ = GGᵀ and GᵀCov(γ)⁻¹G = D for a positive diagonal D. Setting D = I gives
M = Cov(γ)⁻¹. The paper says "We do not have a principle for picking out a
unique choice of D" ([NOTE-302](../notes.d/NOTE-302.md)).

**What the data constrain, derived by the reader.** Take any symmetric
positive-definite M. Let LLᵀ = M⁻¹, let O diagonalise LᵀCov(γ)⁻¹L, and set
G = LO. Then both equations hold. So the covariance by itself excludes no
inner product, the Euclidean one included, since M = I is met by taking G to
be the eigenvectors of Cov(γ). An inner product is ruled out only by
knowledge of the true concept directions G, and given G, M = (GGᵀ)⁻¹ has no
freedom left ([NOTE-302](../notes.d/NOTE-302.md)). [NOTE-302](../notes.d/NOTE-302.md) checked this for d = 6, and I re-checked it
when filing. Both equations hold to about 4·10⁻¹⁶.

**A limit from superposition ([NOTE-278](../notes.d/NOTE-278.md)'s inference).** No inner product
makes more than d nonzero directions pairwise orthogonal. Def. 3.1 asks for
all separable concepts to be orthogonal, and Thm 3.4 wants d of them to form
a basis. Applied to more than d superposed features, the framework must
either declare most of them non-separable or fail. The 27 concepts tested in
d = 4,096 never reach that limit.

This is [THEORY-017](THEORY-017.md)'s thesis for an ML model with a larger group. For a
softmax output the intrinsic symmetry is GL(d), not O(d). So not even an
inner product is intrinsic, and the analyst supplies one from separability
judgements and a stipulation.

## What this does not say

- **That Cov(γ)⁻¹ is a bad choice.** On Gemma-2B the Euclidean product fails
  and the whitened one recovers the expected structure. On LLaMA-2 the
  Euclidean product "somewhat works" (App. D.2). The claim is about what is
  identified, not what is useful. The evidence for either is read from
  heatmaps, with no statistic ([NOTE-302](../notes.d/NOTE-302.md)).
- **Anything about intermediate layers.** The argument uses the softmax
  symmetry, which acts only on the final context vector and the
  unembedding. Interpretability at hidden layers faces a different, unstated
  group ([NOTE-302](../notes.d/NOTE-302.md)).
- **That kernel comparisons across models are meaningless.** The context
  kernel λ(x)ᵀλ(x′) is not identified at the output, so [THEORY-004](THEORY-004.md)'s premise
  of a given kernel is an extra choice there. The Platonic hypothesis's
  kernels ([LIT-302](../literature.d/LIT-302.md)) are average-pooled hidden states, where this argument
  does not directly apply ([NOTE-286](../notes.d/NOTE-286.md)).
- **That a Riesz argument forces a unique factorisation.** Riesz carries over
  whatever inner product it is given and supplies none ([NOTE-302](../notes.d/NOTE-302.md);
  record/curation.d/2026/09/29/230637.md).

## Connections

[LIT-253](../literature.d/LIT-253.md) (Nielsen et al.) starts from the same symmetry. Engels et al.'s
separability index and cosine clustering are Euclidean too, and so are
relative to a choice this theory says is not given ([NOTE-273](../notes.d/NOTE-273.md)).
