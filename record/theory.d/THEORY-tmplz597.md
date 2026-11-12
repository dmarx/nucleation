---
status: Proposed
promote_when: >-
  A second reading confirms, from Tables 1 and 2 and §3.3, the DINO and user-preference comparison with Textual Inversion and the reported training time per subject.
title: 'Fine-tuning all weights of a pretrained text-to-image diffusion model on 3–5 images of a subject, bound to a rare-token identifier and regularized by a class-prior-preservation loss, renders that subject in new contexts with higher subject fidelity than Textual Inversion''s frozen-model embedding (DINO 0.668 against 0.569 on Stable Diffusion; 68% against 22% of users), at about five accelerator-minutes per subject'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed Proposed from NOTE-tmp9kwwm, a reading of LIT-tmp3pjii.
tags:
- representation-learning
date: '2026-11-12'
source:
- LIT-tmp3pjii
bears_on:
- QUESTION-095
summary: >-
  Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein and Kfir Aberman (2022), LIT-tmp3pjii, read in NOTE-tmp9kwwm. CVPR 2023 (arXiv comment: "Published at CVPR 2023").
---

# THEORY-tmplz597: Fine-tuning all weights of a pretrained text-to-image diffusion model on 3–5 images of a subject, bound to a rare-token identifier and regularized by a class-prior-preservation loss, renders that subject in new contexts with higher subject fidelity than Textual Inversion's frozen-model embedding (DINO 0.668 against 0.569 on Stable Diffusion; 68% against 22% of users), at about five accelerator-minutes per subject

## Source

Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein and Kfir Aberman (2022), "DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation", LIT-tmp3pjii, read in NOTE-tmp9kwwm
from arXiv v2 (2208.12242, 15 March 2023; v1 of 25 August 2022).

## What was shown

- **Method.** Abstract: "we fine-tune a pretrained text-to-image model such that it learns to bind a unique identifier with that specific subject." §3.3: the best subject fidelity comes from "fine-tuning all layers of the model".
- **Up-front cost.** §3.3: training takes about "5 minutes on one TPUv4 for Imagen, and 5 minutes on a NVIDIA A100 for Stable Diffusion".
- **Fidelity.** Table 1, DINO: DreamBooth (SD) 0.668, Textual Inversion (SD) 0.569, real images 0.774. Table 2's user study prefers DreamBooth for subject fidelity, 68% to 22%.
- **A cost of learning into weights.** §3.3, language drift: the model "slowly forgets how to generate subjects of the same class as the target subject", which the prior-preservation loss counters.

## What it does not show

Partly curated results; CLIP and DINO metrics; 30 subjects, mostly objects and pets. Cost reported only as training time.
