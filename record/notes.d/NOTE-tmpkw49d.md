---
status: Read
paper: LIT-tmptzx4q
title: 'Ye et al. — IP-Adapter'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read from arXiv v1 (2308.06721, 13 August 2023, the only version), text extracted with pdftotext. Read in full: abstract, §§1–5 and Table 1. The reference list was skimmed; figures were read through their captions, since the extraction holds no images. Quotes rechecked against the extracted text by script.
date: '2026-11-12'
summary: >-
  An image-prompt adapter of about 22M parameters, trained once against a frozen Stable Diffusion v1.5, matches fully fine-tuned image-prompt models on COCO alignment metrics and can be reused without retraining on models fine-tuned from the same base, but by its authors' account does not keep a given subject's identity as Textual Inversion and DreamBooth do. A lightweight adapter, trained once per base model, that adds image prompts to a frozen text-to-image diffusion model by decoupled cross-attention, and matches fully fine-tuned image-prompt models while staying compatible with text prompts, with community models fine-tuned from the same base, and with structural controls.
---
<!-- inactive-ok-file: THEORY-tmp3jjfo CASE-tmp40vka CASE-tmp3isyl CLAIM-tmpnwq8a ARG-tmpu8x8a ARG-tmp4icc1 — Proposed; filed on the same branch -->

# NOTE-tmpkw49d: Ye et al. — IP-Adapter

## Contribution

A lightweight adapter, trained once per base model, that adds image prompts to a frozen text-to-image diffusion model by decoupled cross-attention, and matches fully fine-tuned image-prompt models while staying compatible with text prompts, with community models fine-tuned from the same base, and with structural controls.

## Key results

- **The fine-tuned alternative.** Abstract: direct fine-tuning methods "require large computing resources and are not compatible with other base models, text prompt, and structural controls." §1 says what that means: "the image prompt ability cannot be directly transferred to the other custom models derived from the same text-to-image base models." It is about sibling fine-tunes of one base, not about a successor base.
- **Reuse within one base's family.** §4.3.1: "once IP-Adapter is trained, it can be directly reusable on custom models fine-tuned from the same base model". The three community models tested are fine-tunes of SD v1.5; SD v1.4, which v1.5 continues, is the one other base used.
- **Quality at small size.** Table 1 (COCO 2017 val): IP-Adapter, 22M trainable parameters, CLIP-T 0.588 and CLIP-I 0.828; the fine-tuned SD unCLIP (870M) 0.584 and 0.810.
- **Its own limit.** §5: "it cannot synthesize images that are highly consistent with the subject of a given image like some existing methods, e.g., Textual Inversion [51] and DreamBooth [52]."

## Assumptions

One base model, SD v1.5. CLIP-I and CLIP-T measure alignment with the image prompt, not identity. Qualitative comparisons are best of four samples.

## Concepts

- **image prompt** — an image given as a prompt, read by a CLIP image encoder.
- **decoupled cross-attention** — a separate cross-attention layer for image tokens beside each text cross-attention layer, the outputs summed.
- **custom model** — a community fine-tune of a released base checkpoint.

## Bearing on the record

- **CLAIM-tmpnwq8a: carries less than the claim cited it for.** The claim grounded itself on the abstract's "not compatible with other base models". Read in context, that sentence is about transfer between fine-tunes of the same base, not about a successor base. The paper supports only the claim's scoping premise, that a trained add-on is good for its base model's family, and its caveat, that a reference adapter is trained once by its maker. The ground is moved to `corroborates`, with ARG-tmpu8x8a.
- **CASE-tmp40vka: qualifies A's 2023 row.** For character identity, IP-Adapter in 2023 did not do what A's row implies; its §5 says so. Identity-level reference conditioning came with the face-ID methods of late 2023 and 2024 (PhotoMaker, InstantID).
- **QUESTION-095:** the adapter is a computation done once, by its maker, and reused by every user of every derived model: amortization across users.

## Limitations

One base (SD v1.5). No identity measure. No cost per generation; the added cross-attention at inference is not measured.
