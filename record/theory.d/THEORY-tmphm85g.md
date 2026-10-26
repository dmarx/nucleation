---
status: Active
title: 'In an attention-only transformer without layer norm or biases, once every attention pattern is held at its value on the input, the logits are exactly a sum of end-to-end path terms, a direct path from embedding to unembedding, one term per head and one per chain of heads composed through their values, and each head''s attention scores are a bilinear form in the tokens through which earlier heads can enter on the query side, the key side or both'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpx60d8, the reading of Elhage et al. (2021) in
    full. The result is an algebraic identity. The record re-derived the
    two-layer logit and QK expansions and checked them numerically on a
    random two-layer attention-only transformer with three heads per layer
    (maximum error 1.4 × 10⁻¹² on logits of size about 2.7 × 10³; 7 ×
    10⁻¹² on the sixteen-term QK expansion of a second-layer head).
tags:
- representation-learning
- compositionality
date: '2026-10-26'
source:
- LIT-tmp9dono
summary: >-
  Elhage et al. (2021), LIT-tmp9dono, read in NOTE-tmpx60d8. For a two-layer
  model, T = Id ⊗ W_U W_E + Σ_h A^h ⊗ W_U W^h_OV W_E + Σ_{h₂,h₁}
  A^{h₂}A^{h₁} ⊗ W_U W^{h₂}_OV W^{h₁}_OV W_E, with each A^h computed from the
  model's own run and then held fixed. It is an identity, not an
  approximation, and it is exact only under its conditions: no MLPs, no
  layer norm (which enters as a per-path rescaling), no biases, and
  attention frozen. It does not say the terms are small, interpretable or
  independent in what they compute.
---
<!-- inactive-ok-file: THEORY-802 — Proposed; the basis-relative account this is set beside, cited as open -->

# THEORY-tmphm85g: In an attention-only transformer without layer norm or biases, once every attention pattern is held at its value on the input, the logits are exactly a sum of end-to-end path terms, a direct path from embedding to unembedding, one term per head and one per chain of heads composed through their values, and each head's attention scores are a bilinear form in the tokens through which earlier heads can enter on the query side, the key side or both

## Source

Elhage, Nanda, Olsson et al. (2021), *A Mathematical Framework for
Transformer Circuits*, LIT-tmp9dono, read in full in NOTE-tmpx60d8:
Transformer Overview, the one- and two-layer sections, and the notation and
layer-norm appendices.

## What was actually shown

**The steps.** Write the residual stream at layer n as X_n, an
[n_context, d_model] matrix with one row per token, and a head as
h(X) = A^h X (W^h_OV)ᵀ, where W^h_OV = W^h_O W^h_V and
A^h = softmax*(X W^h_Qᵀ W^h_K Xᵀ). Then:

1. X₀ = t W_Eᵀ for one-hot tokens t.
2. X₁ = X₀ + Σ_{h₁} A^{h₁} X₀ (W^{h₁}_OV)ᵀ; X₂ = X₁ + Σ_{h₂} A^{h₂} X₁ (W^{h₂}_OV)ᵀ.
3. The logits are X₂ W_Uᵀ. Substituting X₁ into X₂ and multiplying out
   gives three groups of terms: X₀ W_Uᵀ (direct path); A^h X₀ (W_U W^h_OV)ᵀ
   for every head h of either layer; and A^{h₂}A^{h₁} X₀
   (W_U W^{h₂}_OV W^{h₁}_OV)ᵀ for every pair (virtual heads).
4. If the A^h are treated as fixed, every term is linear in t.
5. A second-layer head's scores X₁ W_QK X₁ᵀ, with X₁ = (Id + Σ A^{h₁} ⊗
   W^{h₁}_OV) X₀ on both sides, expand into (1 + H₁)² terms, each of the form
   A_q X₀ M_qᵀ W_QK M_k X₀ᵀ A_kᵀ: query-side movement A_q, key-side
   movement A_k, and a bilinear form. Terms with a first-layer head on the
   query side are Q-composition, on the key side K-composition.

**Checked by the record.** A random two-layer attention-only transformer
(vocabulary 11, d_model 16, d_head 4, three heads per layer, seven tokens,
causal softmax) was run, its patterns recorded, and the logits recomputed
from the path terms: agreement to 1.4 × 10⁻¹². The second-layer QK
expansion (sixteen terms) agreed to 7 × 10⁻¹².

**Also exact, and used with it.** Concatenating heads and projecting by
W_O equals summing heads each with its own block of W_O. Products of
heads are heads: (A₂ ⊗ W₂)(A₁ ⊗ W₁) = A₂A₁ ⊗ W₂W₁, by the mixed-product
property.

## What this does not say

- **Not with MLPs.** A GeLU cannot be expanded through; the framework's
  appendix only shows that an MLP's pre-activations and its direct effect
  on the logits have the same form.
- **Not with layer norm, exactly.** Layer norm's centering and learned
  scale fold into adjacent weights; its division by the norm is a
  per-vector scalar, a reweighting of the paths through it, which makes
  paths through different layers not directly comparable.
- **Not that the attention patterns are linear.** The expansion is linear
  only with the patterns frozen; the patterns themselves depend on the
  input, and through Q- and K-composition on earlier heads.
- **Not that the terms are interpretable, or that few matter.** Which
  terms carry the behaviour is an empirical question. In the one
  two-layer model studied, the authors find the virtual-head terms small
  (THEORY-tmpb4xka).

## Connections

- **THEORY-tmpb4xka** is the empirical reading of one two-layer model done
  with this decomposition.
- **THEORY-802.** Every term here is built from W_QK, W_OV, W_E and W_U, so
  its value is unchanged when the residual stream is rotated and all
  matrices reading and writing it are rotated with it. The decomposition
  is basis-free, which is why it is untouched by the non-uniqueness
  THEORY-802 asserts for directions.
- **THEORY-169** describes single attention layers as learners
  conditioned on context; this identity is the bookkeeping by which such a
  layer's output is attributed to heads and paths.
