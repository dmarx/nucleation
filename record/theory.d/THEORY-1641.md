---
number: 1641
status: Proposed
formerly:
- THEORY-tmpc6xzg
promote_when: >-
  A second reading confirms, from §§3, 4.2, 4.6 and 6, the single-embedding optimization of a frozen model, the roughly two-hour cost per concept, its reuse across generations and same-base downstream models, and the authors' limits on shape and identity.
title: 'A concept can be learned from 3–5 images as one new token embedding in the text-encoder input space of a frozen text-to-image model, at about two GPU-hours per concept, and re-used without further optimization in new prompts and in downstream models built on the same base, though it keeps a concept''s gist more than its exact shape or a person''s identity'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed Proposed from NOTE-1719, a reading of LIT-2340.
tags:
- representation-learning
date: '2026-11-12'
source:
- LIT-2340
bears_on:
- QUESTION-095
summary: >-
  Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H. Bermano, Gal Chechik and Daniel Cohen-Or (2022), [LIT-2340](../literature.d/LIT-2340.md), read in [NOTE-1719](../notes.d/NOTE-1719.md). arXiv preprint (the PDF footer reads "Preprint. Under review."); no venue on the arXiv record.
---

# THEORY-1641: A concept can be learned from 3–5 images as one new token embedding in the text-encoder input space of a frozen text-to-image model, at about two GPU-hours per concept, and re-used without further optimization in new prompts and in downstream models built on the same base, though it keeps a concept's gist more than its exact shape or a person's identity

## Source

Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H. Bermano, Gal Chechik and Daniel Cohen-Or (2022), "An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion", [LIT-2340](../literature.d/LIT-2340.md), read in [NOTE-1719](../notes.d/NOTE-1719.md)
from arXiv v1 (2208.01618, 2 August 2022, the only version).

## What was shown

- **Frozen model.** §1: "this process leaves the generative model untouched."
- **Amortization, in the authors' words.** §4.2: "we can optimize a single pseudo-word and re-use it for a multitude of new generations. The baseline models, meanwhile, use CLIP for test-time optimization and thus require expensive optimization for every new creation."
- **Up-front cost.** §6: "learning a single concept requires roughly two hours."
- **Reuse within one base.** §4.6: the pseudo-words "can be used in downstream models that build on the same initial LDM model."
- **Identity.** Societal impact: "our model does not currently preserve identity to the extent where this is a concern."

## What it does not show

One base model; CLIP metrics; weak identity preservation by the authors' account; no inference-cost figures beyond the per-concept optimization time.
