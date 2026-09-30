---
status: Proposed
promote_when: >-
  An analysis of the mainline network's neuron-logit map W_L, or of a faithful
  replication, reporting for each key frequency that the cos and sin
  components are a rotation pair. That means they have equal norms and are
  orthogonal, so W_L's singular values come in degenerate pairs and the
  readout is a character sum, equivariant under shifts of c. Nanda et al.
  plot component norms and give Table 1 coefficients (44.6 against 43.6 for
  k = 14). That is suggestive but does not settle it. A fit with high variance
  explained by trigonometric regressors cannot settle it either, because it
  tests the basis the analyst chose, not the pairing. Clearly unequal or
  non-orthogonal cos and sin components would refute the character-product
  reading while leaving the Fourier-sparsity finding intact.
title: 'The reverse-engineered grokking network computes modular addition by multiplying characters of ℤ/p at a few frequencies, the same real two-dimensional irreducibles later found as circles in language models; in both the group comes from the task, not the network'
version: 1
tags:
- representation-learning
- learning-theory
- mathematics
date: '2026-09-30'
source:
- LIT-345
- LIT-322
- LIT-341
- LIT-305
- LIT-346
summary: >-
  Nanda et al. (2023), [LIT-345](../literature.d/LIT-345.md), show that a one-layer transformer trained on
  addition mod 113 embeds its inputs at five key frequencies. It forms
  cos/sin(w_k(a+b)) and reads out Σ_k α_k cos(w_k(a+b−c)). The reading in
  terms of characters and irreducibles is [NOTE-283](../notes.d/NOTE-283.md)'s, joined here to Engels
  et al.'s circles ([LIT-322](../literature.d/LIT-322.md)). It holds for one weight-decay model and its
  variants: dropout-trained generalisers are not Fourier-sparse. It is not
  evidence that a network discovered the group, which was given, or that the
  frequencies could be read off a spectrum.
---

# THEORY-tmp3pibh: The reverse-engineered grokking network computes modular addition by multiplying characters of ℤ/p at a few frequencies, the same real two-dimensional irreducibles later found as circles in language models; in both the group comes from the task, not the network

## Source

- Nanda, Chan, Lieberum, Smith & Steinhardt (2023), [LIT-345](../literature.d/LIT-345.md), §§4–5 and Apps B–D, as read in [NOTE-283](../notes.d/NOTE-283.md).
- Engels et al. (2024), [LIT-322](../literature.d/LIT-322.md), §5 and App. K, as read in [NOTE-273](../notes.d/NOTE-273.md).
- Power et al. (2022), [LIT-341](../literature.d/LIT-341.md), §3.1 and §3.4, as read in [NOTE-287](../notes.d/NOTE-287.md).
- The machinery: the convolution theorem (Kondor & Trivedi, [LIT-305](../literature.d/LIT-305.md), Prop. 2) and characters of finite abelian groups (O'Donnell, [LIT-346](../literature.d/LIT-346.md), §8.5).

## What was actually shown

**The circuit.** The network is a one-layer ReLU transformer: P = 113, 30%
of pairs, full-batch AdamW with λ = 1. Its embedding is sparse in the Fourier
basis, with key frequencies k ∈ {14, 35, 41, 42, 52}. Attention and the MLP
form cos/sin(w_k(a+b)), with FVE of 93–98%. W_L is about rank 10: one cos and
sin direction per key frequency. The logits are fitted by Σ_k α_k
cos(w_k(a+b−c)). Ablating the other logit Fourier components improves the
loss by 70%, and projecting onto the null space of W_L destroys it. Using
several frequencies makes the sum interfere constructively only at a + b ≡ c
(App. B). Other seeds use three or four different key frequencies. Every
generalising weight-decay model in Table 5 uses a variant of the circuit
([NOTE-283](../notes.d/NOTE-283.md)).

**The representation-theoretic reading ([NOTE-283](../notes.d/NOTE-283.md); not the paper's words).**
For each k, the functions cos(w_k x) and sin(w_k x) span a real
two-dimensional irreducible of ℤ/113, the conjugate character pair χ_k, χ̄_k.
The angle-addition step computes χ_k(a)χ_k(b) = χ_k(a+b). The readout is
Re Σ_k α_k χ_k(a+b) χ̄_k(c). This is the convolution theorem for δ_a ∗ δ_b,
evaluated at a few frequencies only. The near-equal cos and sin coefficients
in Table 1 are what a rotation pair requires. The paired singular values of
W_L are plotted as norms but not reported ([NOTE-283](../notes.d/NOTE-283.md)).

**The same object elsewhere.** Engels et al.'s weekday feature
(cos 2πα/7, sin 2πα/7) is the frequency-1 real irreducible of ℤ/7. Their
regression on Llama months adds frequency-2 and sign characters of ℤ/12
([NOTE-273](../notes.d/NOTE-273.md)). Patching the circle causally changes the answer in Mistral 7B and
Llama 3 8B. Power et al. saw only a qualitative t-SNE "number line" in the
output layer ([NOTE-287](../notes.d/NOTE-287.md)).

## What this does not say

- **That networks find the group.** Nanda et al. chose the DFT because they
  knew the group. Engels et al. took ℤ/7 and ℤ/12 from the task ([NOTE-283](../notes.d/NOTE-283.md),
  [NOTE-273](../notes.d/NOTE-273.md)). A spectral test could see these irreducibles only as pairs, and
  could not tell their frequencies apart ([NOTE-307](../notes.d/NOTE-307.md)).
- **That generalisation requires this circuit.** The dropout models grok but
  are not Fourier-sparse ([NOTE-283](../notes.d/NOTE-283.md)). The founding grokking run used no weight
  decay ([NOTE-287](../notes.d/NOTE-287.md)).
- **Anything about non-abelian tasks.** Whether S₅ generalisers use
  higher-dimensional irreducibles is untested ([NOTE-283](../notes.d/NOTE-283.md)).
- **That language models do modular arithmetic this way.** Both models get
  trivial accuracy on plain modular prompts. The downstream algorithm is only
  suggested ([NOTE-273](../notes.d/NOTE-273.md)).

## Connections

[THEORY-tmp1jea9](THEORY-tmp1jea9.md), on symmetry and degeneracy, covers
why a degeneracy test would see these pairs but not their frequencies.
[THEORY-017](THEORY-017.md): the Fourier basis is supplied, and only the isotypic planes are
fixed by the group.
