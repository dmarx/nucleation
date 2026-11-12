---
status: Proposed
promote_when: >-
  A second reading confirms, from §§1–4 and Figs. 5–6, the architecture, the single-image tuning-free use, the figure-only comparison with character LoRAs, and the same-base compatibility claim.
title: 'A plug-in for a frozen SDXL, trained once by its makers, that injects a face-recognition embedding by decoupled cross-attention and adds a keypoint-conditioned ControlNet keeps a face''s identity from one reference photo without test-time tuning, is shown by figures alone to be competitive with community character LoRAs, and is claimed compatible with models fine-tuned from the same base'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed Proposed from NOTE-tmpt8cah, a reading of LIT-tmpp8vh8.
tags:
- representation-learning
date: '2026-11-12'
source:
- LIT-tmpp8vh8
corroborates:
- CLAIM-tmpnwq8a
bears_on:
- QUESTION-095
summary: >-
  Qixun Wang, Xu Bai, Haofan Wang, Zekui Qin, Anthony Chen, Huaxia Li, Xu Tang and Yao Hu (2024), [LIT-tmpp8vh8](../literature.d/LIT-tmpp8vh8.md), read in [NOTE-tmpt8cah](../notes.d/NOTE-tmpt8cah.md). technical report (arXiv comment: "Technical Report").
---

# THEORY-tmpgxdpz: A plug-in for a frozen SDXL, trained once by its makers, that injects a face-recognition embedding by decoupled cross-attention and adds a keypoint-conditioned ControlNet keeps a face's identity from one reference photo without test-time tuning, is shown by figures alone to be competitive with community character LoRAs, and is claimed compatible with models fine-tuned from the same base

## Source

Qixun Wang, Xu Bai, Haofan Wang, Zekui Qin, Anthony Chen, Huaxia Li, Xu Tang and Yao Hu (2024), "InstantID: Zero-shot Identity-Preserving Generation in Seconds", [LIT-tmpp8vh8](../literature.d/LIT-tmpp8vh8.md), read in [NOTE-tmpt8cah](../notes.d/NOTE-tmpt8cah.md)
from arXiv v2 (2401.07519, 2 February 2024; v1 of 15 January 2024).

## What was shown

- **The trade, in the authors' words.** Abstract: Textual Inversion, DreamBooth and LoRA are "hindered by high storage demands, lengthy fine-tuning processes, and the need for multiple reference images"; prior ID-embedding methods require "only a single forward inference". That phrase describes the earlier embedding methods, which InstantID joins.
- **Per-character cost of a LoRA.** §2: "LoRA necessitates individual training for each new character, limiting its flexibility."
- **Against character LoRAs.** Fig. 6 caption: "We can achieve competitive results as LoRAs without any training." The comparison is with two community character LoRAs from Civitai, by figure only; the paper has no quantitative table.
- **Compatibility within a base family.** §1: "InstantID is pluggable and compatible with other custom models fine-tuned from the same base diffusion model, enabling ID preservation in pre-trained models at no additional cost."
- **The maker's cost.** §4: "Our experiments are based on the SDXL-1.0 model and are conducted on 48 NVIDIA H800 GPUs (80GB)". Training time is not given.

## What it does not show

A technical report with no quantitative evaluation; every comparison is a figure. One base, faces only. Training time not reported.
