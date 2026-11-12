---
status: Read
paper: LIT-tmpp8vh8
title: 'Wang et al. — InstantID'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read from arXiv v2 (2401.07519, 2 February 2024; v1 of 15 January 2024), text extracted with pdftotext. Read in full: abstract, §§1–5, and the appendix figures through their captions. References skimmed. Quotes rechecked against the extracted text by script.
date: '2026-11-12'
summary: >-
  A plug-in for a frozen SDXL, trained once by its makers, that injects a face-recognition embedding by decoupled cross-attention and adds a keypoint-conditioned ControlNet keeps a face's identity from one reference photo without test-time tuning, is shown by figures alone to be competitive with community character LoRAs, and is claimed compatible with models fine-tuned from the same base. Single-image, tuning-free identity preservation for a frozen SDXL: a face-recognition embedding injected by decoupled cross-attention, plus IdentityNet, a ControlNet conditioned on facial keypoints and the embedding.
---
<!-- inactive-ok-file: CASE-tmp40vka CLAIM-tmpnwq8a — Proposed; filed on the same branch -->

# NOTE-tmpt8cah: Wang et al. — InstantID

## Contribution

Single-image, tuning-free identity preservation for a frozen SDXL: a face-recognition embedding injected by decoupled cross-attention, plus IdentityNet, a ControlNet conditioned on facial keypoints and the embedding.

## Key results

- **The trade, in the authors' words.** Abstract: Textual Inversion, DreamBooth and LoRA are "hindered by high storage demands, lengthy fine-tuning processes, and the need for multiple reference images"; prior ID-embedding methods require "only a single forward inference". That phrase describes the earlier embedding methods, which InstantID joins.
- **Per-character cost of a LoRA.** §2: "LoRA necessitates individual training for each new character, limiting its flexibility."
- **Against character LoRAs.** Fig. 6 caption: "We can achieve competitive results as LoRAs without any training." The comparison is with two community character LoRAs from Civitai, by figure only; the paper has no quantitative table.
- **Compatibility within a base family.** §1: "InstantID is pluggable and compatible with other custom models fine-tuned from the same base diffusion model, enabling ID preservation in pre-trained models at no additional cost."
- **The maker's cost.** §4: "Our experiments are based on the SDXL-1.0 model and are conducted on 48 NVIDIA H800 GPUs (80GB)". Training time is not given.

## Assumptions

Faces only; one reference photo; SDXL frozen. The comparison with LoRAs rests on chosen examples.

## Concepts

- **ID embedding** — a face-recognition model's embedding, used in place of CLIP image features.
- **IdentityNet** — a ControlNet variant conditioned on five facial keypoints and on the ID embedding instead of text.
- **plug-and-play** — usable on a base and its fine-tunes without retraining.

## Bearing on the record

- **[CASE-tmp40vka](../cases.d/CASE-tmp40vka.md): supports.** The direct statement of the owner's trade with LoRA named: per-character training and many images against one image and one forward pass. Its claimed parity with character LoRAs is the authors' own judgement, without a measure, like the 2026 thread's.
- **[CLAIM-tmpnwq8a](../claims.d/CLAIM-tmpnwq8a.md): corroborates the scoping premise and the caveat.** Compatibility is claimed only within one base's family, and the module is trained by its makers once for every user, "at no additional cost" to them. It is silent on replacing the base.
- **[QUESTION-095](../questions.d/QUESTION-095.md):** names storage ("high storage demands") as a cost on the learn-and-store side, and shows amortization across users: the maker pays the training once.

## Limitations

A technical report with no quantitative evaluation; every comparison is a figure. One base, faces only. Training time not reported.
