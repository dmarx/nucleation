---
number: 1023
status: Active
formerly:
- THEORY-tmpeqz27
title: 'Attribution patching estimates the effect of patching an activation from a clean run into a corrupted run as the difference between the two activations dotted with the gradient of the metric on the corrupted run, so the estimates for every activation come from two forward passes and one backward pass and add over sub-components; the estimate is exact when the metric is affine in the activation, gives no effect for a nonlinearity in saturation whatever the true change, and through LayerNorm ignores the component of a patch along the vector being normalized'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-1201, the reading of Nanda (2023) in full.
    Every clause is a property of a first-order Taylor estimate and was
    re-derived; the LayerNorm Jacobian, exactness for an affine metric,
    the saturated case and the cost arithmetic were checked numerically
    (the reader's own script). The post's empirical claims about where the
    estimate is reliable in real models are THEORY-1021, Proposed.
tags:
- representation-learning
- causality
date: '2026-10-27'
source:
- LIT-1581
summary: >-
  Nanda (2023), [LIT-1581](../literature.d/LIT-1581.md), read in [NOTE-1201](../notes.d/NOTE-1201.md): the estimate and its
  mathematical properties, not its accuracy in any model. The cost is
  fixed (about four forward passes for all patches), the estimate is
  linear and so additive, and its blind spots follow from linearity:
  saturation, interaction between features, and LayerNorm's scale
  invariance.
extended_by:
- THEORY-1021
---
<!-- inactive-ok-file: THEORY-1021 — Proposed; the post's empirical account of where the estimate is reliable, cited as open -->
# THEORY-1023: Attribution patching estimates the effect of patching an activation from a clean run into a corrupted run as the difference between the two activations dotted with the gradient of the metric on the corrupted run, so the estimates for every activation come from two forward passes and one backward pass and add over sub-components; the estimate is exact when the metric is affine in the activation, gives no effect for a nonlinearity in saturation whatever the true change, and through LayerNorm ignores the component of a patch along the vector being normalized

## Source

Nanda (2023), *Attribution Patching: Activation Patching At Industrial
Scale*, [LIT-1581](../literature.d/LIT-1581.md), read in full in [NOTE-1201](../notes.d/NOTE-1201.md): What Is Attribution
Patching (with its mathematical aside), Why Care (with the runtime aside),
Intuitions, and the sections on linearity and LayerNorm.

## What is shown

**The estimate.** Let f_A(R; a) be the metric on the corrupted input R
with activation A set to a. Activation patching computes f_A(R; A(C)) −
f_A(R; A(R)). Attribution patching replaces it by
(A(C) − A(R)) · ∇_a f_A(R; a) at a = A(R).

**Cost.** One clean forward pass gives every A(C), one corrupted forward
pass every A(R), and one backward pass on the corrupted run every
gradient. Each estimate is then an elementwise product and a sum. For
GPT-2 XL, one estimate per head per position on 100 tokens replaces
120,000 forward passes by about four (a backward pass costing about two),
the post's 30,000×.

**Additivity.** The estimate is linear in the patch, so the estimate for
an activation is the sum of the estimates for any partition of its
elements, and for any decomposition of it into summands of the same shape
(a layer's output into its heads'). Path estimates over all start nodes
sum to the end node's estimate.

**Exactness and its failures.** By Taylor's theorem the estimate is exact
when f_A is affine in a. Its error is second order in the size of the
patch. For a sigmoid or softmax weight that starts saturated (near 0 or
1) the gradient is near zero, so the estimate is near zero even when the
patch moves the weight across its range. Checked: σ(−10) → σ(5) changes
the weight by 0.993, and the estimate is 6.8 × 10⁻⁴. A linear estimate
holds all but one feature fixed, so it cannot see an effect that needs two
features together (a Boolean AND).

**LayerNorm.** Normalization n(v) = √d (v − v̄)/‖v − v̄‖ has a Jacobian
that sends the centred vector to zero and scales directions orthogonal to
it by √d/‖v − v̄‖. Checked numerically to 10⁻⁹. So the estimate ignores
any part of a patch along the residual stream being normalized. That part
changes only the norm, to which normalization is invariant, so it costs
nothing for a pure rescaling. When a patch changes direction and norm
together, the error grows with its size. Through normalization alone, the
median relative error was about 6% for a twentieth of the step to an
independent vector, 22% for a fifth, and 71% for the whole step.

## What this does not say

- **Not how accurate the estimate is in any trained model.** That is an
  empirical question. The post's answer for IOI in GPT-2 Small, and its
  guesses beyond it, are [THEORY-1021](THEORY-1021.md). Kramár et al.'s measurement on
  Pythia is [THEORY-996](THEORY-996.md).
- **Not that a good estimate of a patching effect is a good account of a
  mechanism.** Patching itself tests sufficiency for one prompt pair or
  distribution, as the post insists.
- **Not which direction to patch.** The same estimate applies to noising
  the clean run (as in AtP*) with gradients taken on the clean run.

## Connections

- **[THEORY-996](THEORY-996.md).** Its misses behind saturated attention are the saturated
  case here, met in practice. AtP*'s exact recomputation of the softmax for
  queries and keys removes that case for attention by construction.
- **[THEORY-1007](THEORY-1007.md).** Node selection by linear estimates of indirect effect is
  this estimate (with integrated gradients as a refinement), and inherits
  its blind spots.
