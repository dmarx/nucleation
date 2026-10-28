---
number: 292
status: Proposed
formerly:
- THEORY-tmpxmwzf
promote_when: >-
  A replication that reports, per concept and with error bars, the AUROC
  of separately fitted and of jointly orthogonalised directions against
  the strength of each pair's label correlation, in more than one layer
  and in at least one model where the number of concepts approaches the
  layer's width. It would also need a check that the orthogonal
  direction still means its concept beyond AUROC: for example, that
  ablating it removes that concept's information and not the correlated
  one's. The account is refuted if, for strongly correlated pairs, every
  direction orthogonal to its partner separates the concept markedly
  worse. That would mean the representation, not the fit, ties them.
  More steering pictures cannot settle it, since steering shows what a
  direction does, not whether a better one exists.
title: 'In CNN image classifiers, concept directions fitted one concept at a time align for attributes that co-occur in the labels, yet a joint fit finds mutually orthogonal directions that still separate each concept with little loss of AUROC, so the alignment is a property of the separate fits and not forced by the representation'
version: 1
tags:
- representation-learning
date: '2026-10-14'
source:
- LIT-937
summary: >-
  Erogullari, Lapuschkin, Samek and Pahde (2025), [LIT-937](../literature.d/LIT-937.md), read in full in
  [NOTE-816](../notes.d/NOTE-816.md). Shown at the last convolutional layer of VGG16 and
  ResNet18 on CelebA (natural correlations) and FunnyBirds (an injected
  70% beak–tail correlation). AUROC is "largely preserved" by the
  paper's account, with no values in the text and no error bars. It does
  not say the model's own axes are orthogonal, and it says nothing about
  attributes that imply one another.
bears_on:
- QUESTION-025
---

# THEORY-292: In CNN image classifiers, concept directions fitted one concept at a time align for attributes that co-occur in the labels, yet a joint fit finds mutually orthogonal directions that still separate each concept with little loss of AUROC, so the alignment is a property of the separate fits and not forced by the representation

## Source

Erogullari, Lapuschkin, Samek and Pahde (2025), "Post-Hoc Concept
Disentanglement: From Correlated to Isolated Concept Representations",
[LIT-937](../literature.d/LIT-937.md), arXiv v1. Read in full in [NOTE-816](../notes.d/NOTE-816.md): §3.2 (Eqs. 3–4, Fig. 2),
§3.3 (Eqs. 5–6), §4.2 (Figs. 3–6), Appendices A–C (Tables 1–2, Figs.
10, 12).

## What was actually shown

- **The alignment.**
  - Pattern-CAVs, argmin ‖Z − t wᵀ − b‖² fitted per concept (Eq. 2), were
    fitted for CelebA's 40 attributes at the last convolutional layer of
    VGG16.
  - Their cosine matrix shows two aligned blocks matching two blocks of
    the label correlation matrix (Fig. 2, Fig. 10). Anti-correlated
    concepts point in opposite directions.
  - The same pattern appears for the injected beak–tail correlation in
    FunnyBirds (Fig. 12).
  - That could have come out otherwise: CAVs of correlated labels might
    have been near-orthogonal if the network encoded each attribute
    apart and the fit isolated it.
- **The orthogonal alternative.**
  - The CAVs were fine-tuned for 300 epochs under
    L = L_CAV + α‖CCᵀ − I‖²_F (Eq. 6), with α = 0.01 (0.1 for
    FunnyBirds with VGG16).
  - In all four dataset–model pairs this reaches near-perfect
    orthogonality. Macro AUROC is "largely preserved", settling "at a
    slightly lower level" (Fig. 3).
  - Per concept, relative AUROC changes lie within about ±20% (Fig. 5).
    "Young" lost most and "Pale Skin" gained most (Fig. 4).
  - In an α sweep from random initialisation on VGG16 with CelebA,
    α between 10⁻⁴ and 10⁰ gave perfect orthogonality with average
    AUROC slightly *above* the unpenalised fit (Fig. 6).
  - That too could have failed: if correlated concepts were encoded along
    one shared direction, every orthogonal choice would have separated
    one of them badly.
- **Why the separate fits align.** This is the reader's derivation, not
  the paper's. Eq. 2's solution is w_c ∝ Cov(z, t_c). Suppose the
  activations were z = Σ_k t_k u_k + noise, with distinct u_k. Then
  w_c ∝ Σ_k Cov(t_k, t_c) u_k: each separately fitted direction is a
  mix of the true ones, weighted by label covariance.

## What this does not say

- **Not that the network's own axes are orthogonal.** The penalty
  chooses among separating directions. It does not discover how the
  network uses them. Both kinds of CAV are readings imposed from
  outside.
- **Not that orthogonalisation is free.** Some concepts lose AUROC, on
  an axis whose range is about −20% relative change, and the paper gives
  no values or error bars. "Little loss" is the paper's description of its figures.
- **Not general across layers or widths.** It is shown where the latent
  space is much wider than the 40 concepts (m ≫ n). Where n approaches
  m, orthogonal separating directions need not exist.
- **Not about hierarchy.** The attributes are correlated, not ordered.
  CelebA's near-implications ("Goatee" against "No Beard", "Mustache"
  and "Male") are orthogonalised like any other pair and not analysed.
  Whether implication, unlike correlation, ties directions together is
  open.
- **Not about co-occurrence embeddings.** These are supervised image
  classifiers with labelled attributes, not spectral embeddings of word
  co-occurrence.
- **Not an instruction.** That orthogonal CAVs steer and suppress
  shortcuts with less collateral damage is ML practice. It is left to
  the Anthology of the SOTA.

## Connections

- **[QUESTION-025](../questions.d/QUESTION-025.md)** (`answers`).
  - On the correlated-attribute branch, for supervised CNN features:
    correlated attributes still each have a linear separating direction.
  - Their apparent entanglement is a property of fitting each alone.
  - It does not reach the hierarchical branch or the lattice.
- **[THEORY-185](THEORY-185.md).** Its Appendix A5 case has pairwise-correlated
  attributes giving PMI eigenvectors that mix attributes. This is the
  same phenomenon in another setting: a direction read off one statistic
  at a time mixes correlated attributes, and a joint fit can separate
  them again.
- **[THEORY-117](THEORY-117.md).** There, features pass from decodable but entangled to
  linearly factored as coverage of combinations grows. Here every
  combination occurs and the correlations are partial, and each concept
  is decodable along its own direction. Whether the features are
  factored in [THEORY-117](THEORY-117.md)'s sense is not tested. The two are compatible.
