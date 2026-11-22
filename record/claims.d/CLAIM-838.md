---
number: 838
status: Proposed
formerly:
- CLAIM-tmpqqngq
title: 'On the high-dimensional unit sphere a directional bias of strength κ acts at three scales: of order one it is negligible, of order √D it shifts each cosine by order-one standard deviations and changes the occupancy of a cone holding a fixed share of random directions, and of order D it is needed for an order-one cosine or a cone of fixed angle; so discrimination can change long before visible clustering, and occupancy curves that collapse under κ/√D or κ/D are explained by geometry alone'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the scalings below for a von Mises–Fisher tilt of the uniform
  distribution on S^(D−1): a bias of order √D that leaves the occupancy of
  a fixed-share cone unchanged as D grows, or an order-one modal cosine
  reached with κ of lower order than D. Not met by a learned
  representation whose directional statistics are not von Mises–Fisher:
  the claim is about the geometric null that such data must be compared
  with.
tags:
- representation-learning
- mathematics
- probabilistic-modeling
date: '2026-11-21'
line:
- learned-structure
- formal-apparatus
bears_on:
- QUESTION-515
- QUESTION-512
uses:
- TERM-136
grounds:
- THEORY-189
summary: >-
  A30 §4, A33 §3–§4 and A35 §1 and §7 of the exchange "Rich Get Richer
  Power Laws" (2026-11-21). Against the entropy of the high-dimensional
  sphere, a directional bias κ has a detectable effect at order √D and an
  aligning one only at order D, so "a DNN may learn meaningful semantic
  discrimination long before its embeddings appear strongly clustered",
  and collapse of curves across widths under κ/√D or κ/D is a null to rule
  out before invoking criticality. The caps are measured from the origin,
  so they are not Ganea's entailment cones ([ARG-153](../arguments.d/ARG-153.md)). The wording is A's
  (the other assistant in the exchange "Rich Get Richer Power Laws", A30,
  A33 and A35); adopting it is the owner's call.
---
<!-- inactive-ok-file: ARG-153 CLAIM-827 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->
<!-- inactive-ok-file: THEORY-2188 — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# CLAIM-838: On the high-dimensional unit sphere a directional bias of strength κ acts at three scales: of order one it is negligible, of order √D it shifts each cosine by order-one standard deviations and changes the occupancy of a cone holding a fixed share of random directions, and of order D it is needed for an order-one cosine or a cone of fixed angle; so discrimination can change long before visible clustering, and occupancy curves that collapse under κ/√D or κ/D are explained by geometry alone

## The claim

**Entropy against alignment.** A30 §4: with u uniform on S^(D−1) and a
direction μ, the cosine t = μᵀu has density ∝ (1 − t²)^((D−3)/2). Under a
von Mises–Fisher tilt p(u) ∝ e^(κμᵀu) it becomes
p(t) ∝ e^(κt)(1 − t²)^((D−3)/2), with mode κ = (D − 3)t*/(1 − t*²). At fixed
κ, t* ≈ κ/D → 0; an order-one t* needs κ ∝ D. "In a high-dimensional
isotropic representation space, directional organization must overcome an
entropic opposition whose strength grows with dimension." At D = 768 a modal
cosine of ½ needs κ ≈ 510.

**Cones of fixed angle.** A33 §3: the share of random directions within a
half-angle ψ of μ, q_D(ψ) = P(uᵀμ ≥ cos ψ), falls exponentially in D, so "an
entailment constraint that seems permissive in two or three dimensions can be
exceptionally restrictive in a high-dimensional space". Its specificity
I_cone = −log₂ q_D grows linearly in D at fixed ψ, and A33 proposes
"increasing geometric selectivity, rather than simply increasing pairwise
cosine similarity" as the measure of progressive refinement. The occupancy
crossover is at κ_c/(D − 3) = cos ψ/sin² ψ (A33 §4).

**Cones of fixed share.** A35 §1: √D·uᵀμ tends to N(0, 1), so a cone of
half-angle ψ_D = π/2 − a/√D holds a share 1 − Φ(a) of random directions at
every large D; 5% needs about 78.2° at D = 64 and 86.6° at D = 768. "The
same cone angle does not represent the same degree of semantic selectivity
across dimensions", so cones should be calibrated by their mass under a
reference distribution. Under a tilt κ = c√D, √D·uᵀμ tends to N(c, 1) and
the occupancy is Q(c) = 1 − Φ(a − c).

**Three scales.** A35 §1:

| κ | effect |
|---|---|
| O(1) | negligible directional shift at large D |
| O(√D) | detectable shift relative to random fluctuations |
| O(D) | macroscopic alignment with a nonzero limiting cosine |

"These are scaling regimes, not automatically thermodynamic phase
transitions." A35 §7 turns them into null predictions: occupancy curves from
different widths that collapse against c = κ/√D (fixed-share cones) or
c̃ = κ/D (fixed-angle cones) "can be explained by high-dimensional geometry
without any interacting phase transition", and "a sharp occupancy curve alone
would not establish criticality."

## Checked

Computed in this session (python3 -I, scipy):

- κ = 765 × 0.5/0.75 = 510 at D = 768, t* = ½.
- A33's table of cap probabilities (from the regularized incomplete beta
  function ½ I_(sin²ψ)((D − 1)/2, ½)) reproduces exactly, for example
  0.0187 at D = 64, 75° and 6.35 × 10⁻⁷ at D = 768, 80°.
- A33's asymptotic q_D ≍ (sin ψ)^(D−1)/(cos ψ √(2πD)) overstates the exact
  value by factors of 1.04, 1.16, 1.32 and 1.84 at D = 64 and 60°, 75°,
  80°, 85°, and by 1.00 to 1.14 at D = 768: good away from 90°, poor near it.
  The table does not use it. Likewise I_cone at D = 768 and 80° is 20.6 bits
  exactly against 16.9 from the leading term −(D − 1) log₂ sin ψ; the
  O(log D) remainder A33 names is not small at these sizes.
- The 5% half-angles are 78.12° and 86.60° exactly, against A35's
  normal-approximation 78.2° and 86.6°.
- Q(c) = 1 − Φ(a − c) with a = 1.645: exact occupancies at D = 768 are
  0.0501, 0.2594 and 0.637 for c = 0, 1, 2, against 0.05, 0.2595 and 0.639.
- The fixed-angle crossover sharpens with D, as A33 §4 says: for ψ = 60°
  and κ = r·κ_c, the occupancy at r = 0.9, 1.0, 1.1 is 0.33, 0.46, 0.60 at
  D = 64 and 0.002, 0.50, 0.997 at D = 4,096. It becomes a step in κ/D,
  with no interaction in the model: a concentration step, not a bifurcation.

## Gaps

- **Equilibrium.** The von Mises–Fisher law is a Gibbs measure on the
  sphere, the equilibrium assumption A29 §4 warned against for training.
- **κ and temperature.** A30 says the result "has direct implications for
  contrastive temperature"; the mapping of κ to an inverse temperature 1/τ
  is asserted, not derived.
- **Caps are not entailment cones.** The caps are measured from the origin;
  Ganea's cones are tested at their apex, cannot be defined near the
  origin, and narrow as the apex moves outward ([THEORY-189](../theory.d/THEORY-189.md)). A33 says so
  ("not the volumes of hyperbolic entailment cones"), then carries the
  thresholds to entailment anyway. What carries over is argued in [ARG-153](../arguments.d/ARG-153.md).
- How these scales relate to the BBP threshold and to an alignment
  bifurcation is the assistant's [CLAIM-827](CLAIM-827.md).

## Note of 2026-11-22: Cai and colleagues, read

Cai, Zhang, Liu and Shi ([LIT-2975](../literature.d/LIT-2975.md), [NOTE-2277](../notes.d/NOTE-2277.md), [THEORY-2188](../theory.d/THEORY-2188.md)): **background.** The
unimodal optimum is a Gibbs law of directional bias of order 1/τ, which is
this claim's κ; this claim's three scales say when such a bias matters in
high dimension, which the paper, with experiments on S¹ and S², does not
address. No relation.
