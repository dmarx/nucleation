---
status: Proposed
title: 'The sign flip that Acharya, Rimal and Dhakal call the dual geometry of transformer representations is what Park, Choe and Veitch''s map from unembedding to embedding representations predicts: the map multiplies a concept''s unembedding contrast by the inverse of the unembedding covariance, which divides each eigencomponent by its eigenvalue and so moves the vector''s energy toward the spectral tail, a rescaling in a fixed eigenbasis rather than a rotation of concept information by the forward pass'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    The inequality split off as CLAIM-tmp6odrj (demonstrated); this claim rests
    on it and keeps the interpretive identification.
rests_on:
- CLAIM-tmp6odrj
role: thesis
warrant: interpretive
defeated_if: >-
  For the paper's concepts and models, the activation-side concept vectors
  point no closer (by cosine, or by Gini deviation in the paper's own
  spectra) to Σ⁻¹γ̄, the inverse second moment applied to the same
  concepts' unembedding contrasts, than to γ̄ itself or to norm-matched
  random directions; or the Σ⁻¹ images of the paper's unembedding
  contrasts, computed in its spectra, do not fall below random directions
  on its statistic. An error in the inequality below would defeat it too.
  That the measured activation vectors also differ from Σ⁻¹γ̄ in other
  ways does not defeat it; the claim is about the sign.
tags:
- representation-learning
- information-geometry
date: '2026-11-21'
line:
- learned-structure
grounds:
- THEORY-018
- THEORY-tmpklef6
- LIT-304
summary: >-
  Filling the gap in Acharya, Rimal and Dhakal's argument (NOTE-tmpwvltp,
  Limitations): they read their sign flip as the forward pass rotating
  concept information into the tail, without comparing it with the
  prediction of Park, Choe and Veitch's Theorem 3.2, which their own
  method builds on: λ̄_W ∝ Cov(γ)⁻¹γ̄_W. Dividing by the eigenvalues
  lowers every vector's Gini deviation; whether the measured activation
  vectors are such images is untested. The idea is the reader's, the
  check the lead's and the filer's. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp6odrj — Proposed; the inequality this rests on -->
<!-- inactive-ok-file: THEORY-tmpklef6 ARG-tmp801ah — Proposed or new; the reading this claim explains and the argument filed with it -->

# CLAIM-tmpqy8mq: The sign flip that Acharya, Rimal and Dhakal call the dual geometry of transformer representations is what Park, Choe and Veitch's map from unembedding to embedding representations predicts: the map multiplies a concept's unembedding contrast by the inverse of the unembedding covariance, which divides each eigencomponent by its eigenvalue and so moves the vector's energy toward the spectral tail, a rescaling in a fixed eigenbasis rather than a rotation of concept information by the forward pass

## The claim

Acharya, Rimal and Dhakal (THEORY-tmpklef6, NOTE-tmpwvltp) measure concept
vectors in the eigenbasis of Σ_L, the unembedding's regularized second
moment. Activation-side vectors lean to the tail; unembedding-row
contrasts lean to the head ("concept pairs concentrate (mean ≈ +0.07)"
against −0.10 for random token pairs, §7). They read this as "the forward
pass rotates concept information from the vocabulary geometry into the
low-variance activation subspace" (App. E).

Their method builds on Park, Choe and Veitch (LIT-304), whose Theorem 3.2
says the causal inner product's Riesz map "maps the unembedding
representation γ̄_W of each concept W to its embedding representation
λ̄_W", and with their choice of inner product the embedding representation
is "λ̄_W := Cov(γ)⁻¹γ̄_W" (Eq. 4.1; THEORY-018 holds that this inner
product is fixed by a stipulation). Σ_L is, up to centring and ridge, that
Cov(γ). In Σ_L's eigenbasis, Σ_L⁻¹ divides the i-th component of γ̄ by λ_i.
Nothing rotates: the basis is the same, and each coordinate is rescaled.

**The inequality** is CLAIM-tmp6odrj (demonstrated): Σ⁻¹ moves every vector's energy toward the tail, so the image of a contrast always scores lower than the contrast.

**How far.** The lead's toy (`checks/park_gini.py`, d = 256, a lognormal
spectrum, 500 draws, Gini as the signed area): random directions −0.352,
contrasts drawn with covariance Σ −0.016, their Σ⁻¹ images −0.483. The
reader's own toy (d = 512, λ_i = 1/i + 0.1): −0.084, −0.003 and −0.127. In
both the order is the paper's: images below random, contrasts above. The
paper's normalization of the area is not given, so the magnitudes are
qualitative.

**So.** To the extent Park et al.'s unification holds and the measured
activation vectors estimate embedding representations, the dual
geometry's sign is predicted, not a separate discovery, and "rotation" is
not needed to explain it. The paper does not test whether its activation
vectors match Σ_L⁻¹γ̄; the defeater names that test.

## What it does not say

- Not that the activation vectors are exactly Σ⁻¹γ̄: they are differences
  of means of pooled final-layer activations, SAE columns or probe
  weights, which Park et al.'s theory relates to λ̄ only under its
  assumptions (causal separability, a basis of such concepts).
- Not that the forward pass does no rotation: only that this sign flip
  does not show one.
- Not anything about importance: THEORY-018's point stands, that the
  inner product is stipulated, so which directions count as the tail is
  relative to it.

## Provenance

The rival reading is the reader's (the subagent that read the paper),
flagged in its report; the lead checked it, and the filer added the
inequality. The wording is the assistant's (Claude, in this session);
adopting it is the owner's call. ARG-tmp801ah sets it against the paper's
reading.
