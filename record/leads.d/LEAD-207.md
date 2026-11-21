---
number: 207
status: Open
formerly:
- LEAD-tmpfrw11
title: 'In a small network trained on a synthetic hierarchy whose signal strengths and dependencies are known, date for each distinction the onset of decodability, the sign change of its stability eigenvalue, its gain in held-out fit and any change in the local learning coefficient, with its variance and task sensitivity along the way; then move the onsets by changing parent strength, regularization and the timing of fine examples'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    The assistant's addition revised in place, the lead having been filed
    in this pull request, after the reading of Lau et al. (LIT-2995,
    NOTE-2239): estimating at several inverse temperatures is the
    record's proposal, not the paper's, which fixes β* = 1/log n; the
    localizer's precision γ is varied too; sampler settings are held fixed
    across compared checkpoints; and the sampler's settling is checked
    (App. H), since an unsettled sampler underestimates.
stage: idea
priority: medium
method:
- empirical
- formal
tags:
- learning-theory
- representation-learning
- loss-landscapes
date: '2026-11-21'
line:
- learned-structure
advances:
- QUESTION-511
- QUESTION-514
- CLAIM-834
- CLAIM-828
- CLAIM-807
- CLAIM-812
summary: >-
  The test the other assistant proposed four times in the exchange "Rich
  Get Richer Power Laws" (2026-11-21), merged into one: A37 §10's
  research design, A39 §8's combined measurement, A41 §7's tracking of
  variance, task sensitivity and the learning coefficient, and A43 §16's
  "decisive experiment" with interventions and a control. The assistant
  adds one measurement from [CLAIM-812](../claims.d/CLAIM-812.md): estimate the learning
  coefficient at several inverse temperatures and localizer precisions,
  with the sampler held fixed and checked for settling, so that a sloppy
  direction coming into resolution, or an unsettled sampler, is not read as
  a change of stratum. The multi-temperature protocol is the record's, not
  Lau et al.'s. The wording
  is A's (the other assistant in the exchange "Rich Get Richer Power
  Laws", A37–A43), merged by the assistant (Claude, in this session);
  adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-812 CLAIM-807 CLAIM-828 — Proposed or new, filed with this lead, or a Deferred work registered from the exchange and not yet read -->
<!-- inactive-ok-file: THEORY-2157 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->
<!-- inactive-ok-file: THEORY-tmpr9w2r — Proposed, new or Deferred; filed on 2026-11-21 from the readings of that day -->

# LEAD-207: In a small network trained on a synthetic hierarchy whose signal strengths and dependencies are known, date for each distinction the onset of decodability, the sign change of its stability eigenvalue, its gain in held-out fit and any change in the local learning coefficient, with its variance and task sensitivity along the way; then move the onsets by changing parent strength, regularization and the timing of fine examples

## Sketch

**Why.** Every connection the exchange proposed among singular strata,
small-eigenvalue directions and semantic refinement is a claim about the
order and coincidence of events in training. None has been measured in a
model where the answer is known in advance.

**Design, from A's four versions.**

- A synthetic hierarchy, supercategory → category → subcategory, with
  known signal strengths s_c and known dependencies (A37 §10; A43 §16).
- For each distinction c, four events on one clock (A43 §16): conditional
  decodability from the representation; the sign change of the relevant
  stability eigenvalue; the gain in held-out performance attributable to
  c; a change in the local learning coefficient, functional rank or
  higher-order loss structure.
- Along the way, per tracked direction, the variance V_k(t) and task
  sensitivity S_k(t) (A41 §7). A41's table reads the patterns: V rises
  before decoding (amplification), V stays small while S rises
  (specialization of a quiet direction), neither grows but decoding
  improves (better extraction), the coefficient changes (singular
  reorganization).
- Interventions (A43 §16; A42 §9): raise a parent's strength with the
  fine data fixed (the gated model predicts the child's onset at
  g_c s_c = λ_c, [CLAIM-828](../claims.d/CLAIM-828.md)); raise regularization (onset delayed or
  suppressed, [CLAIM-807](../claims.d/CLAIM-807.md)); add fine examples before, near and after
  onset (their effect should depend on which side of threshold the
  feature is). Causal ablations of quiet subspaces, "holding perturbation
  norms and relevant baseline effects comparable", repeated in other
  coordinates (A41 §7).
- The control (A43 §16): a model in which the fine feature is always
  available and only the decoder improves. If both reach the same final
  performance but respond differently to the interventions, latent
  information becoming accessible is told apart from a stability
  transition.

**The assistant's addition.** Estimate the learning coefficient with Lau
et al.'s estimator ([LIT-2995](../literature.d/LIT-2995.md), [THEORY-2157](../theory.d/THEORY-2157.md)) at two or more inverse
temperatures at each checkpoint, and at two or more localizer precisions
γ. A sloppy regular direction coming into resolution raises the estimate
at the rate of about ½ per direction resolved. A change of singular
stratum moves its level ([CLAIM-812](../claims.d/CLAIM-812.md)). One temperature cannot separate
them. The protocol is the record's: the paper fixes β* = 1/log n and sets
γ per experiment (1 or 100), and its consistency argument (App. D) is made
only at β*.

- **Vary γ as well as β.** On a quadratic loss the estimate is
  Σ ½·te_i/(te_i + γ) with t = nβ ([NOTE-2239](../notes.d/NOTE-2239.md)), so γ is a second cut-off:
  a direction with curvature below about γ/t counts as flat.
- **Hold the sampler fixed.** Step size, chain length, burn-in and batch
  size the same across compared checkpoints, as the paper does within a
  set of relative comparisons (§5.2, App. K).
- **Check settling.** "If the step size is too low, the sampler may not
  equilibriate, leading to underestimation" (App. H.1); the loss trace
  after burn-in and the MALA acceptance rate (App. H, Fig. J.3) are the
  paper's diagnostics. An underestimate from poor mixing mimics a lower
  coefficient, and would be read as a stratum change.

**Not yet said.** The architecture, the size of the hierarchy and how
"the relevant stability eigenvalue" is found in a network with more than
two parameters per feature. Hence stage `idea`.

## Note of 2026-11-21: Hoogland, Wang, Farrugia-Roberts, Carroll, Wei & Murfet, read

The paper does part of what this lead dates, without the variation the
lead asks for ([NOTE-tmp2pgi8](../notes.d/NOTE-tmp2pgi8.md), [THEORY-tmpr9w2r](../theory.d/THEORY-tmpr9w2r.md)). It dates stages by
plateaus of the estimated coefficient and checks them against
independently measured behavioural and structural markers, in two small
transformers; but it holds nβ (21.7 and 66.7, not Lau et al.'s n/log n) and
γ (100 and 13.3) fixed across checkpoints, seeds the SGLD noise identically
at every checkpoint, and reports no stage division under other values. So
the separation this lead proposes, a sloppy direction coming into
resolution against a change of stratum, is not made there ([CLAIM-812](../claims.d/CLAIM-812.md)). Two
of its findings are worth building in: stage boundaries are "sensitive to"
checkpoint spacing, smoothing, t against log t and tolerance (B.1), so the
dating protocol should fix these in advance; and three stages lower the
estimate ([QUESTION-tmphkb1w](../questions.d/QUESTION-tmphkb1w.md)), so the lead should expect decreases as well
as rises.
