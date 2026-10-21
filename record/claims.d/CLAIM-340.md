---
number: 340
status: Active
formerly:
- CLAIM-tmpkss5r
title: 'Scoring operators on predictions committed before the evidence is not by itself Regime B: in the linearized operator model the coupling of interpretation to endorsement has the sign of κ′ − κ̄, so commitment removes capture only when the interpretation bends the reading of the evidence no more than it bends the predictions, and it keeps the learning that revising after the evidence would lose'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation of γ = 4ηs(κ′ − κ̄) or of the stability
  conditions in CASE-106. A showing that a different proper scoring
  rule reverses the sign relation would narrow it to squared error, not
  defeat it.
tags:
- cognition
- complex-systems
date: '2026-10-16'
line:
- distributed-agency
- formal-apparatus
rests_on:
- CLAIM-330
grounds:
- CASE-106
answers:
- QUESTION-121
summary: >-
  The formal question [QUESTION-121](../questions.d/QUESTION-121.md) asked, answered in [CASE-099](../cases.d/CASE-099.md)'s
  linearization ([CASE-106](../cases.d/CASE-106.md)): is committing predictions before the
  evidence equivalent to Regime B? No. The coupling γ is 4ηs(κ′ − κ̄),
  where κ̄ is how far the shared meaning bends the committed predictions
  and κ′ how far it bends the reading of the evidence. It is corrective,
  null or capturing as κ′ is below, at or above κ̄. Strong correction can
  fail by oscillation when |βγ| ≥ 1 − αδ. Revising predictions after the
  evidence sets γ = 0 but also stops authority from tracking who predicts
  well. Linear, at the symmetric state, for squared-error scoring.
illustrated_by:
- CASE-tmp3uarw
supports:
- CLAIM-tmpjo2zr
---

# CLAIM-340: Scoring operators on predictions committed before the evidence is not by itself Regime B: in the linearized operator model the coupling of interpretation to endorsement has the sign of κ′ − κ̄, so commitment removes capture only when the interpretation bends the reading of the evidence no more than it bends the predictions, and it keeps the learning that revising after the evidence would lose

## The claim

[QUESTION-121](../questions.d/QUESTION-121.md)'s third candidate was commitment before evidence: a
prediction made and held before the evidence it is scored against arrives,
so that the order in time does what the auditor does in Regime B. It asked
whether that is equivalent to Regime B (γ ≈ 0) in the sense of [CLAIM-330](CLAIM-330.md).

In [CASE-099](../cases.d/CASE-099.md)'s linearization, with each specialist scored by squared error
between its committed prediction and the evidence as read ([CASE-106](../cases.d/CASE-106.md)):

  γ = 4ηs(κ′ − κ̄).

Here s is how far each specialist leans to its hypothesis, η the rate at
which score moves authority, κ̄ the mean weight with which the shared
meaning bends the committed predictions, and κ′ the weight with which it
bends the reading of the evidence. Three consequences:

- **Commitment is not enough.** What decides is not when the prediction is
  made but whether the evidence is read through the interpretation more
  than the predictions are. If it is (κ′ > κ̄), capture returns, under
  [CASE-099](../cases.d/CASE-099.md)'s condition βγ > (1 − α)(1 − δ).
- **When it works, it does better than Regime B.** For κ′ < κ̄, γ < 0. A
  lean toward A makes the A-specialist's predictions overshoot and costs
  it authority, which pulls the system back. The only failure left is
  over-correction: oscillation once |βγ| ≥ 1 − αδ.
- **Commitment is what keeps learning.** Predictions revised after the
  evidence give no score difference at all. That sets γ = 0, but it also
  sets the evidence gain to 0, so authority no longer tracks who predicts
  well. Regime B scores independently and keeps learning. Revising after
  the fact gives the first without the second.

So [CLAIM-342](CLAIM-342.md)'s anchor, evidence whose arrival or scoring does not
pass through the interpretation it tests, is in this model the condition
κ′ ≤ κ̄ together with commitment. The order in time is necessary for
learning. It does not make the scoring independent.

## What it does not say

- That a mind meets κ′ ≤ κ̄. On constructed-perception accounts the reading
  of evidence is bent by the interpretation ([THEORY-593](../theory.d/THEORY-593.md); [NOTE-434](../notes.d/NOTE-434.md)),
  which pushes κ′ up. Whether it is bent more than the predictions are is
  empirical.
- Anything beyond the linearization at symmetry, or for scores other than
  squared error.

## Note of 2026-10-18: cryptographic commitments fix timing and integrity only

A36 §4 of the exchange of 2026-10-17, on the owner's "Maybe also
cryptography?", proposed commitment protocols as "independent endorsement
audits": each operator fixes a prediction before the outcome and reveals
it after. A36 bounded them by this claim: "it only solves one problem: the
timing and integrity of the prediction. It does not establish that the
outcome is interpreted correctly, that the scoring rule is appropriate, or
that the operator was exposed to representative evidence." That is this
claim's result, a second appearance: a commitment secures the order in
time, which keeps learning, and removes capture only when κ′ ≤ κ̄, which
no protocol guarantees. [CLAIM-346](CLAIM-346.md) holds the three obstructions A36
set this in.
