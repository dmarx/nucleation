---
status: Proposed
promote_when: >-
  Proposition 1 checked from its proof, and an independent replication of
  one shaping experiment showing the original probe degrading while a
  refitted probe at the same or a later layer recovers the concept.
title: 'On Fel, Kowal and colleagues, penalizing a model''s reliance on or expression of a probed concept during training can degrade the original probe, from 0.98 to 0.57 balanced accuracy when gradients pass through it in reward-hacking training, while a refitted linear probe recovers 0.97–0.98; in every experiment they ran the concept stayed readable by the original, a refitted, a nonlinear or another layer''s probe, and in their linear toy theory a fixed projection makes the concept regrow along the directions the readout uses for core features'
version: 1
tags:
- representation-learning
date: '2026-11-15'
source:
- LIT-tmp40uoi
bears_on:
- QUESTION-010
summary: >-
  Fel, Kowal et al. (2026), [LIT-tmp40uoi](../literature.d/LIT-tmp40uoi.md), skimmed in [NOTE-tmp88irq](../notes.d/NOTE-tmp88irq.md), with
  the lab's summary page read in full. The 0.57 is the worst variant; the
  others kept 0.87–0.90. "Every experiment" is the authors' own range of
  settings. The wording is the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: NOTE-tmp88irq — Skimmed; the reading this account comes from -->

# THEORY-tmp2ly83: On Fel, Kowal and colleagues, penalizing a model's reliance on or expression of a probed concept during training can degrade the original probe, from 0.98 to 0.57 balanced accuracy when gradients pass through it in reward-hacking training, while a refitted linear probe recovers 0.97–0.98; in every experiment they ran the concept stayed readable by the original, a refitted, a nonlinear or another layer's probe, and in their linear toy theory a fixed projection makes the concept regrow along the directions the readout uses for core features

## Source

Fel, Kowal et al. (2026), [LIT-tmp40uoi](../literature.d/LIT-tmp40uoi.md); skimmed in [NOTE-tmp88irq](../notes.d/NOTE-tmp88irq.md).

## The result

- §4 (p. 19): with gradients through the probe score, its balanced
  accuracy "falls from 0.98 to 0.57 by update 150, whereas the other
  variants retain 0.87–0.90. Refitting a probe recovers 0.97–0.98 in every
  checkpoint".
- Page: "In all of our experiments, the concept being trained against
  remained monitorable, either with the original probe or a retrained
  one."
- §6, Proposition 1: under a fixed projection "the ablated component
  receives no gradient", and the unwanted feature's new encoding grows
  along "the direction the head already uses to read the core features".

## What it does not show

- That concepts stay monitorable under shaping in general: the claim
  covers the authors' experiments, up to 32B parameters.
- That linear erasure always leaves a nonlinear residue: the quadratic
  reader of §2.1 was not read, and one last-layer case was partly erased
  at that layer.
- That Proposition 1 holds beyond its linear and residual toy models, or
  that its proof is right; the proofs were not checked.
