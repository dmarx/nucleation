---
number: 1911
status: Proposed
formerly:
- THEORY-tmpz2eq3
promote_when: >-
  An independent reproduction, or a run of the released checkpoints or
  code, showing a trigger bound before erasure still eliciting the erased
  concept after at least one of the robust methods (RECE, RECELER or
  ADVUNLEARN), and the paper's tables read to confirm the stated rates
  across the six methods.
title: 'Pre-bound triggers survive concept erasure'
statement: >-
  On Braun and colleagues, a trigger bound to a concept before the model is
  sanitized survives six text-to-image concept-erasure methods, three of
  them built to search for residual representations, on Stable Diffusion
  v1.4 and v2.1 and FLUX, their deepest attack evading erasure in 71.6% of
  cases on average and up to 94.4%, and data poisoning alone, without model
  access, reaching up to 80.2% against celebrity erasure and 92.7% against
  object erasure
version: 1
tags:
- representation-learning
date: '2026-11-15'
source:
- LIT-2637
summary: >-
  Braun, Grebe, Mohr, Rohrbach & Rohrbach (2026), [LIT-2637](../literature.d/LIT-2637.md), skimmed in
  [NOTE-1980](../notes.d/NOTE-1980.md): the summary numbers are the paper's own, from its
  abstract and introduction, and the per-method tables were not read. The
  wording is the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: NOTE-1980 — Skimmed; the reading this account comes from -->

# THEORY-1911: Pre-bound triggers survive concept erasure

## Source

Braun et al. (2026), [LIT-2637](../literature.d/LIT-2637.md); skimmed in [NOTE-1980](../notes.d/NOTE-1980.md).

## The result

- §1: EEBdeep "circumvents erasure in 71.6% of the cases on average, and
  in up to 94.4%", "even against erasure methods that claim adversarial
  robustness and explicitly search for residual trigger-to-target
  representations".
- §1: without model access, "up to 80.2% success in the celebrity
  erasure, up to 92.7% success in the object erasure, and a 6× increase in
  explicit content".
- §5: "modifications that are spread across a larger set of parameters
  make backdoors harder to erase".

## What it does not show

- The per-method rates, which were not read.
- Anything outside text-to-image diffusion.
- That erasure cannot be made to remove such links: §4.6 sketches
  remedies, including activation monitoring, without testing them in
  full.
