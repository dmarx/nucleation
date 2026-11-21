---
status: Open
title: 'In a small network trained on a synthetic hierarchy whose signal strengths and dependencies are known, date for each distinction the onset of decodability, the sign change of its stability eigenvalue, its gain in held-out fit and any change in the local learning coefficient, with its variance and task sensitivity along the way; then move the onsets by changing parent strength, regularization and the timing of fine examples'
version: 1
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
- QUESTION-tmp82zpm
- QUESTION-tmpsy8qn
- CLAIM-tmpp83vc
- CLAIM-tmpl9zw4
- CLAIM-tmp9bp04
- CLAIM-tmpcg4uu
summary: >-
  The test the other assistant proposed four times in the exchange "Rich
  Get Richer Power Laws" (2026-11-21), merged into one: A37 §10's
  research design, A39 §8's combined measurement, A41 §7's tracking of
  variance, task sensitivity and the learning coefficient, and A43 §16's
  "decisive experiment" with interventions and a control. The assistant
  adds one measurement from CLAIM-tmpcg4uu: estimate the learning
  coefficient at several inverse temperatures, so that a sloppy direction
  coming into resolution is not read as a change of stratum. The wording
  is A's (the other assistant in the exchange "Rich Get Richer Power
  Laws", A37–A43), merged by the assistant (Claude, in this session);
  adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmpcg4uu CLAIM-tmp9bp04 CLAIM-tmpl9zw4 LIT-tmpnbl2d — Proposed or new, filed with this lead, or a Deferred work registered from the exchange and not yet read -->

# LEAD-tmpfrw11: In a small network trained on a synthetic hierarchy whose signal strengths and dependencies are known, date for each distinction the onset of decodability, the sign change of its stability eigenvalue, its gain in held-out fit and any change in the local learning coefficient, with its variance and task sensitivity along the way; then move the onsets by changing parent strength, regularization and the timing of fine examples

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
  g_c s_c = λ_c, CLAIM-tmpl9zw4); raise regularization (onset delayed or
  suppressed, CLAIM-tmp9bp04); add fine examples before, near and after
  onset (their effect should depend on which side of threshold the
  feature is). Causal ablations of quiet subspaces, "holding perturbation
  norms and relevant baseline effects comparable", repeated in other
  coordinates (A41 §7).
- The control (A43 §16): a model in which the fine feature is always
  available and only the decoder improves. If both reach the same final
  performance but respond differently to the interventions, latent
  information becoming accessible is told apart from a stability
  transition.

**The assistant's addition.** Estimate the learning coefficient (Lau
et al., LIT-tmpnbl2d) at two or more inverse temperatures at each
checkpoint. A sloppy regular direction coming into resolution raises the
estimate at the rate of about ½ per direction resolved. A change of
singular stratum moves its level (CLAIM-tmpcg4uu). One temperature cannot
separate them.

**Not yet said.** The architecture, the size of the hierarchy and how
"the relevant stability eigenvalue" is found in a network with more than
two parameters per feature. Hence stage `idea`.
