---
status: Read
paper: LIT-tmp4meti
title: 'Black Forest Labs — FLUX.1 Kontext'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read from arXiv v2 (2506.15742, 24 June 2025; v1 of 17 June 2025), text extracted with pdftotext. Read in full: abstract, §§1–5; appendix A skimmed; references skimmed. Fig. 8's bar values are not in the text extraction, so the evaluation is as the authors' prose states it. Quotes rechecked against the extracted text by script.
date: '2026-11-12'
summary: >-
  A flow-matching transformer fine-tuned from FLUX.1 to condition on a context image by sequence concatenation renders a character or object from that image in new scenes and across successive edits without per-subject fine-tuning or LoRA training, at 3–5 s per 1024² image, and on its authors' benchmark preserves characters better than the competing systems they evaluated. One in-context image model for generation and editing, in which character consistency comes from the context image at inference, fast enough for iterative work, with a crowd-sourced benchmark.
---
<!-- inactive-ok-file: THEORY-tmpdzbq1 CASE-tmp40vka CASE-tmp3isyl CLAIM-tmpnwq8a ARG-tmpu8x8a ARG-tmp4icc1 — Proposed; filed on the same branch -->

# NOTE-tmpc56d2: Black Forest Labs — FLUX.1 Kontext

## Contribution

One in-context image model for generation and editing, in which character consistency comes from the context image at inference, fast enough for iterative work, with a crowd-sourced benchmark.

## Key results

- **Personalization without training.** §1: "This property enables personalization of generative image and video models without the need for finetuning [43] or LoRA training [19, 27, 20]. Early works on such training-free subject-driven image synthesis include IP-Adapter [58]".
- **Per-use cost.** §1: image synthesis "at 1024 × 1024 of 3–5 seconds".
- **A successor base.** §3: "Training starts from a FLUX.1 text-to-image checkpoint".
- **Character results.** The abstract reports "improved preservation of objects and characters"; §4.2's character-reference comparison, by the authors' own benchmark and face-embedding measure, ranks it first among the systems evaluated.

## Assumptions

The benchmark and evaluation are the authors'; competitors are reached through APIs. Single context image.

## Concepts

- **in-context image generation** — conditioning on a context image by appending its tokens to the target's sequence.
- **character reference** — rendering a character from the context image in a new scene.

## Bearing on the record

- **CASE-tmp40vka: supports the 2025 row and A's genealogy.** The paper itself draws the line from IP-Adapter to training-free character reference, in place of fine-tuning or LoRA training. It does not measure the trade.
- **CASE-tmp3isyl:** KontextBench's character-reference cases and its multi-turn drift measure are candidate fidelity targets.
- **CLAIM-tmpnwq8a: leaves open.** Kontext is a new base derived from its predecessor; whether add-ons trained on FLUX.1 carry over is not discussed. A base derived from its predecessor is where transfer might hold, which is the claim's defeater.
- **QUESTION-095:** computing on demand, priced at 3–5 s per image.

## Limitations

Company report; own benchmark; black-box competitors; no comparison with trained personalization.
