---
status: Proposed
promote_when: >-
  A second reading confirms, from Table 1, §4.3.1 and §5, the CLIP-I and CLIP-T scores against the fine-tuned image-prompt models, the reuse on SD v1.5-derived models without retraining, and the authors' statement that it does not reach subject-level consistency.
title: 'An image-prompt adapter of about 22M parameters, trained once against a frozen Stable Diffusion v1.5, matches fully fine-tuned image-prompt models on COCO alignment metrics and can be reused without retraining on models fine-tuned from the same base, but by its authors'' account does not keep a given subject''s identity as Textual Inversion and DreamBooth do'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed Proposed from NOTE-tmpkw49d, a reading of LIT-tmptzx4q.
tags:
- representation-learning
date: '2026-11-12'
source:
- LIT-tmptzx4q
corroborates:
- CLAIM-tmpnwq8a
bears_on:
- QUESTION-095
summary: >-
  Hu Ye, Jun Zhang, Sibo Liu, Xiao Han and Wei Yang (2023), LIT-tmptzx4q, read in NOTE-tmpkw49d. arXiv preprint (v1, the only version; no venue on the arXiv record).
---
<!-- inactive-ok-file: CLAIM-tmpnwq8a — Proposed; filed on the same branch -->

# THEORY-tmp3jjfo: An image-prompt adapter of about 22M parameters, trained once against a frozen Stable Diffusion v1.5, matches fully fine-tuned image-prompt models on COCO alignment metrics and can be reused without retraining on models fine-tuned from the same base, but by its authors' account does not keep a given subject's identity as Textual Inversion and DreamBooth do

## Source

Hu Ye, Jun Zhang, Sibo Liu, Xiao Han and Wei Yang (2023), "IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models", LIT-tmptzx4q, read in NOTE-tmpkw49d
from arXiv v1 (2308.06721, 13 August 2023, the only version).

## What was shown

- **The fine-tuned alternative.** Abstract: direct fine-tuning methods "require large computing resources and are not compatible with other base models, text prompt, and structural controls." §1 says what that means: "the image prompt ability cannot be directly transferred to the other custom models derived from the same text-to-image base models." It is about sibling fine-tunes of one base, not about a successor base.
- **Reuse within one base's family.** §4.3.1: "once IP-Adapter is trained, it can be directly reusable on custom models fine-tuned from the same base model". The three community models tested are fine-tunes of SD v1.5; SD v1.4, which v1.5 continues, is the one other base used.
- **Quality at small size.** Table 1 (COCO 2017 val): IP-Adapter, 22M trainable parameters, CLIP-T 0.588 and CLIP-I 0.828; the fine-tuned SD unCLIP (870M) 0.584 and 0.810.
- **Its own limit.** §5: "it cannot synthesize images that are highly consistent with the subject of a given image like some existing methods, e.g., Textual Inversion [51] and DreamBooth [52]."

## What it does not show

One base (SD v1.5). No identity measure. No cost per generation; the added cross-attention at inference is not measured.
