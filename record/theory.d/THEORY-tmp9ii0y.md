---
status: Active
title: 'When a transformer''s MLP sublayers are replaced by transcoders and the attention patterns and LayerNorm scales on a prompt are held fixed, the contribution of an earlier transcoder feature at the same token to a later one''s pre-activation is the earlier feature''s activation times the dot product of its decoder with the later feature''s encoder, scaled by one LayerNorm constant per token, so the weight factor is fixed by the trained weights and holds on every input'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpbsp9v, the reading of Dunefsky, Chlenski and
    Nanda (2024) in full. The result is their Eq. 7 (App. D.2); the record
    re-derived it step by step below (ADR-047 v2), and the derivation makes
    explicit a scalar the paper's Eq. 7 leaves to App. D.4: the later
    layer's LayerNorm scale, which depends on the input.
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-tmptgo43
summary: >-
  Dunefsky, Chlenski and Nanda (2024), LIT-tmptgo43, read in NOTE-tmpbsp9v,
  Eq. 7 and App. D.2–D.4, re-derived here. The weight factor is a weight of
  the replacement model, not of the original, and it is exact only for the
  replacement. It says nothing about why attention attends where it does,
  and "input-invariant" holds only up to a per-token LayerNorm scalar and
  only while the later feature is active.
---
<!-- inactive-ok-file: CLAIM-tmpwr001 THEORY-802 — Proposed; the record's own claim and a neighbouring account, named, nothing here rests on them -->
# THEORY-tmp9ii0y: When a transformer's MLP sublayers are replaced by transcoders and the attention patterns and LayerNorm scales on a prompt are held fixed, the contribution of an earlier transcoder feature at the same token to a later one's pre-activation is the earlier feature's activation times the dot product of its decoder with the later feature's encoder, scaled by one LayerNorm constant per token, so the weight factor is fixed by the trained weights and holds on every input

## Source

Dunefsky, Chlenski and Nanda (2024), NeurIPS 2024, arXiv:2406.11944,
LIT-tmptgo43, read in full in NOTE-tmpbsp9v: §3.2 (Eqs. 6–8) and App.
D.2–D.4.

## What was actually shown

A derivation, checked by the record step by step.

**Setting.** A pre-norm transformer with residual stream x. At layer l and
token t, x_mid^(l,t) = x_pre^(l,t) + Σ_h attn^(l,h), and x_pre^(l+1,t) =
x_mid^(l,t) + MLP^(l)(LN(x_mid^(l,t))). A transcoder for layer l is
TC^(l)(u) = Σ_j z_j(u) f_dec^(l,j) + b_dec, with z_j(u) = ReLU(f_enc^(l,j) ·
u + b_enc,j), trained so that TC^(l) ≈ MLP^(l).

**Step 1: the residual is a sum.** By the residual connections,
x_mid^(l',t) is the token embedding plus the outputs of every earlier
attention head and every earlier MLP at token t, plus the bias terms.

**Step 2: substitute the transcoders.** Replacing each MLP^(l), l < l', by
TC^(l), the MLP-l part of x_mid^(l',t) is Σ_j z_j^(l,t) f_dec^(l,j) +
b_dec^(l).

**Step 3: the later feature's pre-activation.** Feature i' of layer l'
reads LN(x_mid^(l',t)) = γ ⊙ P x_mid^(l',t) / σ^(l',t) + β, where P
removes the mean and σ^(l',t) is the token's standard deviation. Holding
σ^(l',t) fixed at its value on the prompt (the paper's App. D.4), the
pre-activation is h = g · x_mid^(l',t) / σ^(l',t) + const, where g = P(γ ⊙
f_enc^(l',i')) depends only on weights, since P is symmetric.

**Step 4: linearity.** The MLP-l part of h is therefore Σ_j z_j^(l,t)
(f_dec^(l,j) · g) / σ^(l',t). Each earlier feature j contributes

  z_j^(l,t) × (f_dec^(l,j) · g) × 1/σ^(l',t).

The first factor is the activation on this input. The second is fixed by
the trained weights. The third is one scalar for the whole token. The
paper's Eq. 7 writes the first two, z · (f_dec · f_enc), and applies the
third in App. D.4 "by multiplying each f feature vector by the appropriate
LayerNorm 'scaling constant'".

**Step 5: through attention.** For a head at layer l < l' moving
information from token s to t, the output is Σ_s score^(l,h)(t,s) W_OV
LN(x_pre^(l,s)). With the scores held at their values on the prompt, the
contribution of x_pre^(l,s) is score × (W_OVᵀ g) · LN(x_pre^(l,s)), so
W_OVᵀ g acts as a new encoder-like vector at token s (Eqs. 8, 22–24) and
Steps 1–4 apply again, with the score as a further input-dependent factor.

**Step 6: what an attribution is to.** The ReLU of the later feature is
not linear. The decomposition is of its pre-activation; it is the
contribution to the activation only while the feature is active, which
the paper assumes ("assuming that this feature is active").

**What could have come out otherwise.** Nothing, as a derivation. What the
paper tests empirically is whether the weight factor is useful: whether
the top input-invariant connections and de-embeddings name what a feature
does, which its blind case studies do in five of nine cases and partly in
two more.

## What this does not say

- **Not a property of the original model.** The factorization holds in the
  replacement. How far the replacement's circuits are the model's is a
  separate, empirical question; in one case study (App. H.1.2) the
  replacement computes a feature differently from the model.
- **Not fully input-invariant.** The weight factor is, but the attribution
  also carries 1/σ at each layer it passes through and, through attention,
  the attention score. Which features are active is input-dependent too.
- **Nothing about QK circuits.** Freezing the scores is what makes the
  attribution linear, and it leaves unexplained why information moved.
- **Not unique.** The weights are those of one trained dictionary. Another
  transcoder of equal fidelity could carry the computation in other
  features, which is THEORY-802's point about decompositions, here for
  dictionaries.

## Connections

- **LIT-tmpsuo6l.** Ameisen et al.'s edge weights are this rule extended to
  cross-layer transcoders, with all normalization denominators frozen, and
  their "virtual weights" are this weight factor.
- **CLAIM-tmpwr001.** A transcoder feature comes with its downstream
  weights, which is more than a recovered feature has, but they are weights
  of a stand-in.
