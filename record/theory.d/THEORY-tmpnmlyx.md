---
status: Proposed
promote_when: >-
  An intervention study showing that the persona vector carries the
  finetuning-induced change: for example, that removing or clamping the
  component of the finetuned model's activations along the vector, at the
  layers where it acts, restores the base model's trait expression across
  traits and datasets while leaving the finetuning's domain-specific effect
  in place, and that the finetuned model does not re-encode the trait in
  other directions. A higher correlation between shift and expression does
  not settle it, and neither does post-hoc steering lowering the trait,
  since both are consistent with the vector being a correlate of a change
  carried elsewhere.
title: 'Persona shifts induced by prompting and by finetuning are mediated by the same linear trait directions, so finetuning on data that implies a trait moves the model along the trait''s persona vector as a system prompt would; Chen et al. suspect personas are latent factors that persist across many tokens'
version: 1
tags:
- representation-learning
- self
date: '2026-11-03'
source:
- LIT-tmpyjvij
summary: >-
  Chen et al. (2025), LIT-tmpyjvij, read in NOTE-tmpp25f6. The mediating
  reading is the authors' framing and PSM's use of the paper (LIT-tmp4flye:
  training-time shifts "can be regarded as conditioning"). What the paper
  shows is correlation of shift with expression, and steering effects in
  both directions; that the regularizer against the shift fails, with the
  trait moving to other directions, counts against a single direction being
  the carrier. Proposed for that gap.
---
<!-- inactive-ok-file: NOTE-tmpp25f6 — Proposed, Open, Deferred, Unfetched, Unavailable or new; cited as open -->

# THEORY-tmpnmlyx: Persona shifts induced by prompting and by finetuning are mediated by the same linear trait directions, so finetuning on data that implies a trait moves the model along the trait's persona vector as a system prompt would; Chen et al. suspect personas are latent factors that persist across many tokens

## Source

Chen et al. (2025), LIT-tmpyjvij; read in NOTE-tmpp25f6.

## What was actually shown

- The same vector, extracted from system-prompted contrasts, steers the trait
  (§3.2), tracks prompt-induced shifts (§3.3) and tracks finetuning-induced
  shifts (§4.2, THEORY-tmp6nup8).
- Subtracting it after finetuning lowers the trait (§5.1); adding it during
  finetuning prevents much of the shift (§5.2).
- A loss penalizing change along it is "ineffective", "We suspect this is
  because the optimization pressure pushes the model to represent the
  personality trait using alternative directions" (p. 9).
- The authors' explanation of the generalization: "we suspect it has to do
  with personas being latent factors that persist for many tokens" (pp. 13–14).

## What this does not say

- That the direction is necessary for the trait: the regularization result
  suggests it is not.
- That training is conditioning in PSM's strict sense: the paper does not
  compare finetuned models to conditioned ones beyond the shared direction.
