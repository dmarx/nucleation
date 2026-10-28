---
number: 185
status: Active
formerly:
- THEORY-tmp5ocix
title: 'When each binary attribute of a word affects its co-occurrence independently and multiplicatively, the PMI is affine in the attributes with rank at most d + 1, so a spectral PMI embedding is a linear image of the attribute hypercube and parallelogram analogies hold exactly; over the full hypercube of words, each attribute''s two values equally frequent, the raw co-occurrence ratio mixes in products of attributes, and keeps exact analogies only when the strengths are alike enough that every attribute mode outranks every product mode'
version: 4
history:
- version: 2
  date: '2026-10-09'
  note: >-
    At the owner's prompting, a Connections section on the Lattice
    Representation Hypothesis (LIT-267) and CLAIM-119: this result derives
    the hypothesis's premise and, by the same independence, makes its
    lattice Boolean. The open question is QUESTION-025. The claim is
    unchanged.
- version: 3
  date: '2026-10-14'
  note: >-
    Connections to THEORY-271 (LIT-977), an additive-mixture rival,
    prompted by NOTE-781, and to THEORY-292 (LIT-937), a
    supervised counterpart of Appendix A5, prompted by NOTE-816.
    The claim is unchanged.
- version: 4
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision
    for THEORY-185 (batch 037, ADR-047 v2). Eq. 12, Results 1–3 and the
    Kronecker theorem were re-derived step by step, in the dated note
    below. The PMI clauses are unchanged. The raw-ratio clause is narrowed
    to the full, balanced hypercube, and "only when the signals are weak
    and alike" becomes the exact condition: every attribute mode must
    outrank every product mode. Equal strengths meet it at any strength.
    The theorem is conditional on its premise, so the promote_when's
    request to measure that premise on real text moves to
    QUESTION-178.
tags:
- representation-learning
- compositionality
date: '2026-10-09'
source:
- LIT-863
- LIT-860
corroborates:
- CLAIM-082
summary: >-
  Korchinski, Karkada, Bahri and Wyart (2025), [LIT-863](../literature.d/LIT-863.md): proved for a
  generative model of co-occurrence in which words are bundles of
  independent binary attributes, with robustness to noise, pruning and
  deleted pairs argued from eigenvalue bounds and simulated. The embeddings
  are eigendecompositions, not trained models; that real co-occurrence is
  close to this form is inferred from spectral and accuracy-curve shapes,
  not measured.
bears_on:
- QUESTION-025
---
<!-- inactive-ok-file: CLAIM-119 LIT-267 QUESTION-025 — Proposed or open; cited as what this result bears on -->
<!-- inactive-ok-file: THEORY-292 — Proposed; filed today, named in Connections as a rival and a counterpart, not leaned on -->
<!-- inactive-ok-file: THEORY-183 THEORY-182 THEORY-019 — Proposed; cited as the continuous counterpart, the premise about trained models, and the symmetry account this one bears on -->

# THEORY-185: When each binary attribute of a word affects its co-occurrence independently and multiplicatively, the PMI is affine in the attributes with rank at most d + 1, so a spectral PMI embedding is a linear image of the attribute hypercube and parallelogram analogies hold exactly; over the full hypercube of words, each attribute's two values equally frequent, the raw co-occurrence ratio mixes in products of attributes, and keeps exact analogies only when the strengths are alike enough that every attribute mode outranks every product mode

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
Over the full, balanced hypercube, an embedding of M does so only if
K ≤ d + 1 and every attribute mode outranks every product mode. The paper
reaches that with small, narrowly spread s_k, and the exact condition is in
the note of 2026-10-19 below. Otherwise the product modes interleave with
the attribute modes, and accuracy rises and then falls with K. With pairwise-correlated
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

## Connections

**The Lattice Representation Hypothesis** ([LIT-267](../literature.d/LIT-267.md), read in [NOTE-240](../notes.d/NOTE-240.md))
assumes that binary attributes have linear directions in a model's
representations, thresholds them into an object–attribute incidence, and
reads its concept lattice as the model's. This result derives that premise
from co-occurrence: under independent attributes each one is a linear
direction of the PMI embedding, and thresholding recovers the incidence
exactly. In this model the hypothesis's first step is a theorem.

The same independence empties its second step. Every combination of
attributes is possible, so the incidence is the full hypercube and its
concept lattice is Boolean, with no implications among attributes. The
structure a concept lattice is for, attributes that imply or exclude each
other as in [LIT-267](../literature.d/LIT-267.md)'s WordNet hierarchies or [CLAIM-119](../claims.d/CLAIM-119.md)'s categories that
share attributes and differ in a few constraints, is what this model
excludes. Whether the linear directions survive it is [QUESTION-025](../questions.d/QUESTION-025.md).

**An additive rival.** [THEORY-271](THEORY-271.md) (Torii, Maeda and Hidaka, [LIT-977](../literature.d/LIT-977.md),
read in [NOTE-781](../notes.d/NOTE-781.md)) gets an exact parallelepiped in a toy
subject–verb–object corpus from a different premise. There aspects combine
as a mixture over sentences, so counts add across aspects, and the shape is
in the raw co-occurrence rows; the logarithm would break it. Here attributes
multiply, and the shape is in the PMI. The two agree that parallelograms are
in the data and disagree about which transform shows them, because they
assume different ways for attributes to combine. It is a rival account for a
different generative structure, not a second derivation of this one.

**A supervised counterpart of Appendix A5.** With pairwise-correlated
attributes, the affine eigenvectors here mix attributes (A5).
[THEORY-292](THEORY-292.md) (Erogullari et al., [LIT-937](../literature.d/LIT-937.md), read in [NOTE-816](../notes.d/NOTE-816.md)) finds the
same in CNN image classifiers for concept directions fitted one at a time,
and adds that a joint fit finds orthogonal directions that still separate
each concept. A direction found from one statistic at a time mixes
correlated attributes; a joint fit can separate them again. The setting is
labelled image attributes, not co-occurrence.

## Note of 2026-10-19: the theorem, re-derived

Any function on {±1}² is a combination of 1, a, b and ab, and a symmetric
one has equal coefficients on a and b. So
log P^(k)(a, b) = δ_k + η_k(a + b) + γ_k ab, and summing over attributes,
log M = δ11ᵀ + Aη1ᵀ + 1ηᵀAᵀ + ADAᵀ entrywise, for any set of words. Every
term's columns lie in the span of 1 and the attribute columns, so the rank
is at most d + 1. Since the PMI is symmetric, every eigenvector with a
non-zero eigenvalue lies in that span and is affine in the attributes. A
spectral embedding that keeps such modes is W_i = c + Bα_i. So
α_D = α_A − α_B + α_C gives W_A − W_B + W_C = W_D, whatever the strengths.

For the raw ratio, with all 2^d words, M = ⊗_k P^(k). In the balanced case
each factor has eigenvalues 2 and 2s_k on the constant and on α^k. The
mode that takes α^k from the attributes in a set S has eigenfunction
∏_{k∈S} α^k and eigenvalue 2^d ∏_{k∈S} s_k. With K ≤ d + 1 modes, an
embedding of M is affine, and so gives parallelograms exactly, iff no
product mode (|S| ≥ 2) is kept. That holds iff min_k s_k > s_(1)s_(2), the
product of the two largest strengths. Equal strengths satisfy it at any
strength below 1. So what matters is that the strengths be alike relative
to their size, and the source's "small and narrowly spread" is a
sufficient first-order regime. Without balance, each factor's top
eigenvector is not constant, and even the top mode of M is a product.
Whether real co-occurrence is close to the premise is [QUESTION-178](../questions.d/QUESTION-178.md).
