---
status: Proposed
promote_when: >-
  An independent evaluation, on FLUX.1-dev or another diffusion model,
  of the rank-concatenated LoRAs merged with the least-squares router
  against task arithmetic, TIES and DARE on the same updates, over
  several seeds or LoRA pools, shows the router's single-task fidelity
  above theirs at K = 9 by more than seed variation, and above 90% of
  the single-LoRA oracle. A result on another objective or another
  modality would not settle it.
title: 'Merging the LoRAs of a diffusion model by concatenating them along the rank dimension and inserting a fixed router, the least-squares map that reconstructs each LoRA''s output on its own task''s inputs from one calibration prompt per task, kept over 90% of single-LoRA subject fidelity with nine LoRAs on FLUX.1-dev, above task arithmetic, TIES and DARE applied to the same updates'
version: 1
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmpanxdy
summary: >-
  Wei et al. (2026), [LIT-tmpanxdy](../literature.d/LIT-tmpanxdy.md), read in [NOTE-tmpmpv2r](../notes.d/NOTE-tmpmpv2r.md). The router
  R = QG⁻¹ is the least-squares solution of the layer-local
  reconstruction objective (Theorem 3.1) and is absorbed into B, so the
  merged model is one static LoRA; task arithmetic is R = I. At K = 9 on
  FLUX.1-dev it scores DINO 0.6713 against 0.4723 for TIES and 0.6240
  for IterIS, a 90.2% recovery. One LoRA pool, no seeds. The wording is
  the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-107 — Proposed; the coordinate account this one is set beside -->

# THEORY-tmpvun8m: Merging the LoRAs of a diffusion model by concatenating them along the rank dimension and inserting a fixed router, the least-squares map that reconstructs each LoRA's output on its own task's inputs from one calibration prompt per task, kept over 90% of single-LoRA subject fidelity with nine LoRAs on FLUX.1-dev, above task arithmetic, TIES and DARE applied to the same updates

## Source

Wei et al. (2026), [LIT-tmpanxdy](../literature.d/LIT-tmpanxdy.md), read in [NOTE-tmpmpv2r](../notes.d/NOTE-tmpmpv2r.md): §§1–4.2,
Tables 1–3.

## The result

- **Construction** (§3). Stack the K LoRAs' A matrices and place their B
  matrices side by side, giving rank Kr. From one calibration prompt per
  task, form G = Σ Z_k Z_kᵀ over the projected features and Q from
  H_k Z_kᵀ, and set R = QG⁻¹. Theorem 3.1: R minimizes
  Σ‖B_comb R Z_k − Y_k‖²_F. Absorb it as B̃ = B_comb R.
- **Same budget** (§4). Task arithmetic, TIES, DARE and SSR "operate on the
  same collection of K low-rank updates"; only the router differs.
- **Fidelity** (Table 1, FLUX.1-dev, ten DreamBooth subjects). SSR stays
  above every baseline as K grows; at K = 9 it scores DINO 0.6713 and
  CLIP 0.7850, a recovery of 90.2% and 92.9% of the single-LoRA upper
  bound, against 0.4723 and 0.6839 for TIES and 0.6240 and 0.7520 for
  IterIS. This could have failed: a router fitted on one prompt and one
  timestep might have overfitted.

## What it does not show

- **That interference lives in activations rather than coordinates in
  general.** It shows that a data-conditioned, layer-local objective beats
  coordinate-wise trimming and sign election here; it does not separate
  sign from scale, so it does not test [THEORY-107](THEORY-107.md).
- **Data-free merging.** The router needs one calibration prompt per task.
- **Input-dependent routing.** R is a fixed linear map; "routing" is the
  authors' word for decorrelation, not gating.
- **Image quality in general.** The metrics are DINO and CLIP similarity to
  the subject and detection success; the theorem is optimality for the
  reconstruction objective only.
- **Robustness.** One LoRA pool, one main model, no seeds or intervals.
  RegMean, the nearest relative, was excluded, not beaten.
