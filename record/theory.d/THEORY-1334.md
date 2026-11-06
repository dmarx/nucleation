---
number: 1334
status: Proposed
formerly:
- THEORY-tmpnmlyx
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
- LIT-1998
summary: >-
  Chen et al. (2025), [LIT-1998](../literature.d/LIT-1998.md), read in [NOTE-1524](../notes.d/NOTE-1524.md). The mediating
  reading is the authors' framing and PSM's use of the paper ([LIT-1952](../literature.d/LIT-1952.md):
  training-time shifts "can be regarded as conditioning"). What the paper
  shows is correlation of shift with expression, and steering effects in
  both directions; that the regularizer against the shift fails, with the
  trait moving to other directions, counts against a single direction being
  the carrier. Proposed for that gap.
---

# THEORY-1334: Persona shifts induced by prompting and by finetuning are mediated by the same linear trait directions, so finetuning on data that implies a trait moves the model along the trait's persona vector as a system prompt would; Chen et al. suspect personas are latent factors that persist across many tokens

## Source

Chen et al. (2025), [LIT-1998](../literature.d/LIT-1998.md); read in [NOTE-1524](../notes.d/NOTE-1524.md).

## What was actually shown

- The same vector, extracted from system-prompted contrasts, steers the trait
  (§3.2), tracks prompt-induced shifts (§3.3) and tracks finetuning-induced
  shifts (§4.2, [THEORY-1313](THEORY-1313.md)).
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

## Note of 2026-11-06: what holds it back

The paper asks whether finetuning shifts are "mediated by persona vectors"
(§4.2) and answers with correlation and steering; it has no intervention
that removes or clamps the component along the vector after finetuning and
shows that the base trait returns with no re-encoding elsewhere. Its
nearest results cut both ways: steering after finetuning keeps the domain
effect while lowering the trait on two datasets (J.1), training-time
ablation (CAFT) prevents evil and sycophancy but not hallucination (J.4),
and penalizing the shift leaves the trait expressed, suspected re-encoded
in other directions (J.5). "As a system prompt would" has only J.7.3's
comparison of preventative prompting with preventative steering, on one
task.
