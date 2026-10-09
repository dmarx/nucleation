---
number: 183
status: Proposed
formerly:
- THEORY-tmp1cak6
promote_when: >-
  An intervention on the data: a word embedding trained by gradient descent
  at moderate dimension (not computed by diagonalising the co-occurrence
  matrix), or a language model, trained on corpora edited so that the
  co-occurrence among a concept's words stops depending only on their
  separation, or depends on it through a different kernel. The test is that
  the learned geometry changes as the Fourier account predicts: frequencies
  and relative amplitudes follow the new kernel, and the circle or curve
  degrades in step with the broken symmetry. Further PCA pictures of
  unedited models, and further fits of the kernel to unedited corpora,
  cannot settle it, because they are what the account was built to match.
title: 'When the co-occurrence of words on a latent continuum depends only on their separation, a spectral word embedding places them on the Fourier modes of that continuum, so the circles and rippled curves of months, years and places come from a symmetry of the corpus statistics'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-09'
source:
- LIT-860
- LIT-855
- LIT-322
summary: >-
  Karkada, Korchinski, Nava, Wyart and Bahri (2026), [LIT-860](../literature.d/LIT-860.md): proved
  for an embedding whose Gram matrix equals the co-occurrence matrix (or its
  absolute value) at full rank, with the exponential kernel solved for both
  boundary conditions; the symmetry measured in Wikipedia; matching PCA
  pictures in Gemma 2. That trained networks get their geometry this way is
  inferred, not tested: nothing in the paper changes the statistics and
  watches the geometry follow.
---
<!-- inactive-ok-file: THEORY-182 THEORY-022 THEORY-019 THEORY-002 — Proposed; cited as the premise and the accounts this one bears on -->

# THEORY-183: When the co-occurrence of words on a latent continuum depends only on their separation, a spectral word embedding places them on the Fourier modes of that continuum, so the circles and rippled curves of months, years and places come from a symmetry of the corpus statistics

## Source

- Karkada, Korchinski, Nava, Wyart and Bahri (2026), [LIT-860](../literature.d/LIT-860.md),
  Propositions 1, 3 and 4, Corollary 2, §4.1, Appendices B and E, and
  Figures 1–7, as read in [NOTE-664](../notes.d/NOTE-664.md).
- The premise that a word embedding factorises the co-occurrence deviation
  matrix M*: Karkada, Simon, Bahri and DeWeese (2025), [LIT-855](../literature.d/LIT-855.md), as read in
  [NOTE-660](../notes.d/NOTE-660.md) ([THEORY-182](THEORY-182.md)).
- The circles in language models: Engels et al. (2024), [LIT-322](../literature.d/LIT-322.md), as read in
  [NOTE-273](../notes.d/NOTE-273.md).

## What was actually shown

**The theorem.** Take an embedding W whose Gram matrix W Wᵀ is the matrix
absolute value of M*, with M*_ij = (P_ij − P_iP_j)/(½(P_ij + P_iP_j)) and
d ≥ rank M*. Suppose a set S of words sits on a lattice in a latent space
(the months on a circle, years on an interval, places on a plane), and
their entries of M* depend only on the distance between their coordinates.
Then their PCA coordinates are sinusoids of the latent coordinate. These
come in degenerate cos/sin pairs, and the amplitude of each is the square
root of the kernel's Fourier transform at that wavevector. That holds on a
periodic lattice of any dimension (Proposition 1). For the exponential
kernel the geometry is solved exactly. With a periodic boundary it is a
closed loop with integer frequencies (Corollary 2). With an open boundary it
is an open curve whose wavenumbers solve tan k = −σk or a centred analogue,
via a Sturm–Liouville problem (Proposition 3). The best rank-r linear probe
then recovers the coordinate with error O(r^(−1/D)) (Proposition 4).

**The measurement.** Wikipedia's month and year blocks of M* are close to
circulant and Toeplitz, with an exponential profile off the diagonal. The
predicted Lissajous curves match the spectral embeddings in frequency and
relative amplitude. This could have come out otherwise: co-occurrence of
years or months might have depended on absolute position, and in places it
does. The world wars put kinks in the year curve.

**Robustness.** With every month–month entry of M* set to zero, a
1000-dimensional embedding still orders the months on a circle. Ten
seasonal words suffice to recover the order; seventeen number words do not.
A model in which a seasonal latent variable modulates many words
reproduces this: the latent variable makes the whole PMI circulant, with
eigenvalues that grow with the number of words.

## What this does not say

- **Not that trained networks factorise the statistics this way.** Every
  theorem is about the idealised embedding. Every word-embedding figure is
  computed by diagonalising M* (Equation 2), not by training. That
  word2vec's embedding is this factorisation is [THEORY-182](THEORY-182.md), itself shown
  only for a tied quartic proxy.
- **Not that language models' geometry is caused by co-occurrence.** The
  Gemma 2 and EmbeddingGemma evidence is a visual match in PCA, one prompt
  template per concept. That LLMs build circles on top of pairwise
  statistics is the authors' inference, not their result.
- **Not exact on real data.** M* is indefinite: its positive and negative
  parts have comparable rank. So the kernel fitted to M* is not the one
  factorised, and absolute amplitudes are mispredicted.
- **Not a proof of robustness.** The step from eigenvalues of order N to
  stable eigenvectors is asserted with a reference to Weyl and Davis–Kahan.
  No gap or bound is given.
- **Not that the network finds the symmetry.** It is the reverse: the
  symmetry is in the data and the embedding reads it off. The circle is
  the ℤ/12 irreducible pair because the corpus statistics commute with
  shifts of the calendar, as [THEORY-019](THEORY-019.md) requires of any operator that
  commutes with a group. That sharpens [THEORY-022](THEORY-022.md)'s "the group comes from
  the task" for the language-model case without testing it there.
- **Not an instruction.** It says what such a model contains, not how to
  build or probe one.
