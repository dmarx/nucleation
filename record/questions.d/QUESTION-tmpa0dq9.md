---
status: Open
title: 'When the record meets a random linear map that keeps what a later stage needs, in random features for kernels, the compressed-sensing bound on superposition, and the expand-and-threshold codes of sparse distributed memory and the fly, is it one concentration-of-measure fact applied to different families, and does each threshold count the same thing?'
version: 1
tags:
- mathematics
- learning-theory
- neuroscience
date: '2026-10-14'
line: formal-apparatus
summary: >-
  Filed when a survey of the record found random projections in three
  places and the Johnson–Lindenstrauss lemma in none. The three uses carry
  three thresholds: ε⁻² log n for distances, k log(n/k) for sparse
  recovery, and 2N = n for random-features regression. The question is
  whether these are one union bound over different families or different
  phenomena that share a tool. Seven anchor works are registered, unread.
---
<!-- inactive-ok-file: LIT-tmp7skui LIT-tmpjy3gf LIT-tmppzjx6 LIT-tmp8s1wj LIT-tmpcfdvm LIT-tmpwlsvo LIT-tmpokc0j — Deferred, unread; the anchor works this question registers -->

# QUESTION-tmpa0dq9: When the record meets a random linear map that keeps what a later stage needs, in random features for kernels, the compressed-sensing bound on superposition, and the expand-and-threshold codes of sparse distributed memory and the fly, is it one concentration-of-measure fact applied to different families, and does each threshold count the same thing?

## The question

The record uses random projections in three places and holds no reading of
the result usually given for why they work.

- **Random features.** Liao, Couillet and Mahoney ([LIT-679](../literature.d/LIT-679.md), [NOTE-519](../notes.d/NOTE-519.md))
  and [THEORY-106](../theory.d/THEORY-106.md) treat cos(WX), sin(WX) with W random. The threshold
  there is 2N = n, features against samples, and it is where the test error
  diverges.
- **Superposition.** Toy Models of Superposition proves m = Ω(k log(n/k))
  for recovering k-sparse features, assuming the restricted isometry
  property, and asks whether its phase changes are the Donoho–Tanner
  transition ([NOTE-278](../notes.d/NOTE-278.md)).
- **Expand and threshold.** Neuron-view sparse distributed memory is linear
  attention with thresholded random projections as its feature map
  ([NOTE-242](../notes.d/NOTE-242.md), [NOTE-779](../notes.d/NOTE-779.md)). The mushroom body makes the same move in tissue
  ([NOTE-670](../notes.d/NOTE-670.md), [NOTE-165](../notes.d/NOTE-165.md)).

The Johnson–Lindenstrauss lemma ([LIT-tmp7skui](../literature.d/LIT-tmp7skui.md)) gives ε⁻² log n for keeping
the distances of n points, and the bound is tight ([LIT-tmp8s1wj](../literature.d/LIT-tmp8s1wj.md)). Baraniuk
et al. ([LIT-tmpcfdvm](../literature.d/LIT-tmpcfdvm.md)) derive the restricted isometry property from the same
concentration, by a union bound over sparse supports instead of point
pairs. If that is the general shape, each threshold is the log of the size
of the family a map must hold, divided by a squared tolerance. The question
is whether that is true of all three uses, or only of the first two.

## Why it is a question

Two things suggest the three are not one phenomenon.

- **The random-features threshold counts something else.** 2N = n compares
  features with training samples. Its divergence comes from the ridgeless
  resolvent near interpolation ([THEORY-106](../theory.d/THEORY-106.md)), not from failing to keep
  distances. A random map can keep every distance and still interpolate
  badly.
- **The biological and SDM maps go up in dimension.** The fly projects
  about 50 glomeruli onto about 2,000 Kenyon cells and keeps the top 5%
  ([LIT-tmpokc0j](../literature.d/LIT-tmpokc0j.md)). Johnson–Lindenstrauss is about going down. What expansion
  followed by sparsification keeps is similarity rank under a hash, which
  is a different guarantee.

Against that, the sparse binary matrices of the fly and of SDM are the
ensembles Achlioptas ([LIT-tmppzjx6](../literature.d/LIT-tmppzjx6.md)) shows keep the JL guarantee, and
Donoho and Tanner ([LIT-tmpwlsvo](../literature.d/LIT-tmpwlsvo.md)) observe that the sparse-recovery transition
does not depend on the ensemble. So the shared tool is real. What is open
is whether it is the explanation in each case.

## What would answer it

- For superposition: the [NOTE-278](../notes.d/NOTE-278.md) bound rewritten as the Baraniuk et al.
  union bound over the toy model's sparse supports, and its phase change
  compared with the Donoho–Tanner curve at the same (δ, ρ).
- For random features: a statement of what a random-features map keeps
  that the lemma does not mention. One candidate is that a kernel's Gram
  matrix converges entrywise but not in spectral norm ([LIT-679](../literature.d/LIT-679.md)). Or a
  derivation of the 2N = n transition that goes through concentration, if
  one exists.
- For expand-and-threshold: the guarantee the fly's hash keeps, in a form
  that can be set beside ε⁻² log n, and whether SDM's critical distance is
  the same quantity.

A reading of the seven anchor works would settle the first. The other two
need the record's own derivation.
