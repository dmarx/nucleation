---
status: Proposed
title: 'Park, Choe and Veitch''s unification theorem, applied in the eigenbasis Concepts Whisper measures in, predicts its sign flip between activation-side and vocabulary-side concept vectors as a rescaling by the inverse covariance, so the flip explains as well without the paper''s rotation of concept information by the forward pass'
version: 1
form: formal-application
grounds:
- LIT-304
- THEORY-018
- THEORY-tmpklef6
concludes:
- CLAIM-tmpqy8mq
tags:
- representation-learning
- information-geometry
date: '2026-11-21'
line:
- learned-structure
summary: >-
  Sets the reader's reading of Concepts Whisper's dual geometry against the
  paper's. Park et al.'s map λ̄ ∝ Cov(γ)⁻¹γ̄ lowers the Gini deviation of
  every vector in the unembedding's eigenbasis, so the paper's sign flip
  is predicted without a rotation; whether its activation vectors are such
  images is untested. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpqy8mq THEORY-tmpklef6 — Proposed or new; the claim this argues and the reading it applies the theorem to -->

# ARG-tmp801ah: Park, Choe and Veitch's unification theorem, applied in the eigenbasis Concepts Whisper measures in, predicts its sign flip between activation-side and vocabulary-side concept vectors as a rescaling by the inverse covariance, so the flip explains as well without the paper's rotation of concept information by the forward pass

## The inference

Theorem 3.2 of Park, Choe and Veitch (LIT-304) maps a concept's
unembedding representation to its embedding representation by the causal
inner product's Riesz map, λ̄_W = Cov(γ)⁻¹γ̄_W (Eq. 4.1). Acharya, Rimal and
Dhakal (THEORY-tmpklef6) measure activation-side and vocabulary-side
concept vectors in the eigenbasis of the unembedding's second moment and
find opposite signs. Applying the theorem: the inverse divides each
eigencomponent by its eigenvalue, which lowers the Gini deviation of every
vector (CLAIM-tmpqy8mq), so activation-side vectors that estimate λ̄
should sit further in the tail than the contrasts they come from.

## Critical questions

- **Does the mapping premise hold?** Partly. Σ_L is "the regularized
  uncentered second moment of the unembedding rows", over a language
  subset, with ridge τ = 0.1; Park et al.'s Cov(γ) is the centred
  covariance over the vocabulary. The activation-side result keeps its
  sign across eight constructions, centred, full-vocabulary and
  frequency-weighted among them (Table 2), and the inequality holds for
  any positive-definite Σ, ridge included, so the difference does not
  change the sign. The activation vectors are differences of means of
  pooled final-layer activations over counterfactual word pairs; Park et
  al. define embedding representations by counterfactual pairs of
  contexts, and in their experiments take λ̄_W := Cov(γ)⁻¹γ̄_W (Eq. 4.1).
  Whether the paper's vectors are close to Σ_L⁻¹γ̄ is not measured: the
  open step.
- **Are the model's assumptions met?** Theorem 3.2 assumes causally
  separable concepts forming a basis, a strong idealization; THEORY-018
  holds that the causal inner product is fixed by a stipulation, so the
  theorem predicts the sign only for the inner product it stipulates. The
  paper measures in exactly that basis, so the stipulation is the paper's
  as much as the theorem's.
- **Which rivals, and does one explain as well?** The paper's: the forward
  pass rotates concept information into the tail, supported by the depth
  profile (−0.009 at the embedding layer, deepening through the layers).
  The reading here explains the sign at the final layer as well, with no
  free parameter; it does not by itself explain the depth profile, which
  a rescaling at the output cannot. A pure anisotropy account (any vector
  scores negative in an uneven spectrum) is the paper's own foil, and both
  readings beat it, since the two sides differ in sign against matched
  nulls.
- **Would more evidence discriminate them?** Yes: the cosine between each
  activation-side concept vector and Σ_L⁻¹γ̄, against the cosine with γ̄
  and with random directions, at the final layer and through depth. A
  rotation predicts no special closeness to Σ_L⁻¹γ̄; this reading predicts
  it.

## Verdict

Holds for the sign at the final layer, Proposed until the discriminating
comparison is made. It does not show that the forward pass rotates
nothing; it shows that the paper's flip is no evidence that it does.
