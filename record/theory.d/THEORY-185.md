---
number: 185
status: Proposed
formerly:
- THEORY-tmp5ocix
promote_when: >-
  A measurement of the premise on real text, not of its consequences:
  for the word quadruples of analogy families, how far the PMI departs
  from additivity in the attributes across all context words, with the
  finding that families whose statistics are close to additive are the
  ones a spectral embedding completes and those far from it are not. Or an
  intervention on a corpus that adds an interaction between two attributes
  (contexts that favour one combination beyond the sum of the two
  effects), with the parallelogram for that pair breaking in the PMI
  embedding as the account predicts while the others stay. More agreement
  in the shape of analogy accuracy against embedding dimension, or of the
  PMI spectrum, cannot settle it, because the model was built to match
  those shapes.
title: 'When each binary attribute of a word affects its co-occurrence independently and multiplicatively, the PMI is affine in the attributes with rank at most d + 1, so a spectral PMI embedding is a linear image of the attribute hypercube and parallelogram analogies hold exactly; the raw co-occurrence ratio mixes in products of attributes and keeps them only when the signals are weak and alike'
version: 1
tags:
- representation-learning
- compositionality
date: '2026-10-09'
source:
- LIT-863
- LIT-860
summary: >-
  Korchinski, Karkada, Bahri and Wyart (2025), [LIT-863](../literature.d/LIT-863.md): proved for a
  generative model of co-occurrence in which words are bundles of
  independent binary attributes, with robustness to noise, pruning and
  deleted pairs argued from eigenvalue bounds and simulated. The embeddings
  are eigendecompositions, not trained models; that real co-occurrence is
  close to this form is inferred from spectral and accuracy-curve shapes,
  not measured.
supports:
- CLAIM-082
---
<!-- inactive-ok-file: THEORY-183 THEORY-182 THEORY-019 — Proposed; cited as the continuous counterpart, the premise about trained models, and the symmetry account this one bears on -->

# THEORY-185: When each binary attribute of a word affects its co-occurrence independently and multiplicatively, the PMI is affine in the attributes with rank at most d + 1, so a spectral PMI embedding is a linear image of the attribute hypercube and parallelogram analogies hold exactly; the raw co-occurrence ratio mixes in products of attributes and keeps them only when the signals are weak and alike

## Source

- Korchinski, Karkada, Bahri and Wyart (2025), [LIT-863](../literature.d/LIT-863.md), the Theorem
  of §5 with Appendix A1, Eq. 12 and Results 1–4 of §6, §§7–9, Appendices
  A4–A5 and Figures 1–3, 6–10, as read in [NOTE-665](../notes.d/NOTE-665.md).
- The combination with continuous attributes: Karkada, Korchinski, Nava,
  Wyart and Bahri (2026), [LIT-860](../literature.d/LIT-860.md), Appendix D (Theorem 5), as read in
  [NOTE-664](../notes.d/NOTE-664.md).

## What was actually shown

**The theorem.** Let word i be α_i ∈ {−1, +1}^d, and let
P(i, j) = P(i)P(j) ∏_k P^(k)(α_i^k, α_j^k), with each 2 × 2 factor fixed by
normalisation up to a strength s_k. The ratio M = P(i, j)/P(i)P(j) is then
the Kronecker product of the factors. Its eigenvectors are products: the
constant, d attribute modes v_k(i) ∝ α_i^k with eigenvalue ∝ s_k, then
modes ∝ s_k s_k′ carrying products of attributes, and so on. Its logarithm,
the PMI, is exactly δ11ᵀ + ADAᵀ + Aη1ᵀ + 1ηᵀAᵀ, with A the words-by-attributes
matrix. So the PMI has rank at most d + 1, every eigenvector is affine in
the attributes, and a spectral embedding satisfies
W_A − W_B + W_C = W_D whenever α_D = α_A − α_B + α_C, for any strengths.
An embedding of M does so only if the s_k are small and narrowly spread
and K ≤ d + 1. Otherwise the product modes interleave with the attribute
modes, and accuracy rises and then falls with K. With pairwise-correlated
attributes the PMI keeps rank ≤ d + 1 and affine eigenvectors, which then
mix attributes (A5).

**Robustness.** I.i.d. noise of scale σ in the PMI has norm about
2σ2^(d/2), against attribute eigenvalues of order 2^d. Analogies survive
until about 2^(d/2)/σ noise modes are admitted, and the rescaled curves
collapse. A random 15% of the vocabulary keeps the spectrum up to scale.
Zeroing every pair that differs only in one attribute leaves that
attribute's direction in place.

**Wikipedia.** Spectral embeddings of M and log(M + 10⁻²) over 10,000
words reproduce the pattern on Mikolov et al.'s analogies: the PMI beats
M and saturates with K. Zeroing a family's own pairs costs little. The
PMI's spectrum is broad and near log-normal, as in the model with broadly
spread strengths. That comparison could have come out otherwise: the PMI
could have been near-isotropic, as Arora et al.'s model implies, or
deleting a family's own pairs could have destroyed it.

## What this does not say

- **Not that language is made of independent binary attributes.** The
  model posits them. No attribute, strength or dimension d is recovered
  from the data, and the ratio condition that earlier accounts postulated
  holds exactly in the model because independence builds it in. The
  account explains analogies by an assumption about the statistics; the
  assumption itself is untested.
- **Not that trained embeddings do this.** Every embedding is a truncated
  eigendecomposition. That word2vec learns the top eigenvectors of M*,
  which agrees with the PMI to third order, is [THEORY-182](THEORY-182.md), shown only for
  a tied quartic proxy.
- **Not proved robust.** The perturbation steps bound eigenvalues by Weyl's
  inequality and assert that eigenvectors follow; no eigenvector bound is
  given. The deletion experiments zero entries of the matrix, which is
  not deleting sentences from a corpus.
- **Not that analogies need K ≥ d.** Equation 11 can hold with K < d + 1
  for analogies within the kept attributes, but the nearest-neighbour score
  may then be degenerate, as the paper's d = 2 example with K = 2 shows.
- **Not an account of language models.** The Discussion's pointer to
  linear subspaces in LLMs is a motivation, and nothing is tested there.
- **Not a symmetry account by itself.** In the balanced case the
  eigenvectors are the Walsh characters of (ℤ/2)^d acting by flipping
  attribute values, a case of [THEORY-019](THEORY-019.md), the binary counterpart of the
  Fourier modes of [THEORY-183](THEORY-183.md). But affineness in the PMI comes from the
  logarithm turning a product into a sum, and it holds with the symmetry
  broken (q_k ≠ 1) too.
- **Not an instruction.** It says what such an embedding contains, not how
  to build one.
