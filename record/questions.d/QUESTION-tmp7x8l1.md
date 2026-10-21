---
status: Answered
title: 'In the linearized operator model, is scoring operators against predictions committed before the evidence equivalent to Regime B''s independent scoring?'
version: 1
tags:
- cognition
- complex-systems
date: '2026-10-21'
line: distributed-agency
refines:
- QUESTION-121
summary: >-
  The formal sub-question [QUESTION-121](QUESTION-121.md) asked of its third candidate,
  commitment before evidence. Split off under [ADR-049](../decisions.d/ADR-049.md) and answered No by
  [CLAIM-340](../claims.d/CLAIM-340.md). The coupling of interpretation to endorsement is
  γ = 4ηs(κ′ − κ̄), so commitment removes capture only when the
  interpretation bends the reading of the evidence no more than it bends
  the predictions. Which source in one mind does the scoring stays with
  [QUESTION-121](QUESTION-121.md).
answered_by:
- CLAIM-340
---

# QUESTION-tmp7x8l1: In the linearized operator model, is scoring operators against predictions committed before the evidence equivalent to Regime B's independent scoring?

## Answer

No. [CLAIM-340](../claims.d/CLAIM-340.md) (Active, demonstrated) derives it in [CASE-106](../cases.d/CASE-106.md), within
[CASE-099](../cases.d/CASE-099.md)'s linearization at the symmetric state, for squared-error
scoring. The coupling of interpretation to endorsement is

  γ = 4ηs(κ′ − κ̄),

where κ̄ is how far the shared meaning bends the committed predictions and
κ′ how far it bends the reading of the evidence.

- **Commitment is not enough.** For κ′ > κ̄, γ > 0 and capture returns
  under [CLAIM-330](../claims.d/CLAIM-330.md)'s condition βγ > (1 − α)(1 − δ).
- **When it works, it corrects.** For κ′ < κ̄, γ < 0 and a lean is pulled
  back. The only failure left is oscillation, once |βγ| ≥ 1 − αδ.
- **Revising after the evidence** sets γ = 0, but it also sets the
  evidence gain to 0, so authority stops tracking who predicts well.

## What it leaves to [QUESTION-121](QUESTION-121.md)

The answer is about the model, linear, at symmetry, and for squared
error. Whether a mind's commitments meet κ′ ≤ κ̄, and which of
[QUESTION-121](QUESTION-121.md)'s candidates in fact keeps a loop from locking in, are
empirical, and stay with the parent.
