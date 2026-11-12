---
status: Active
status_note: >-
  read 2026-11-12 ([NOTE-tmp9kwwm](../notes.d/NOTE-tmp9kwwm.md)) from arXiv v2. Worth reading for what learning a subject into weights bought in 2022: full fine-tuning per subject in about five accelerator-minutes, at higher subject fidelity than Textual Inversion's frozen-model embedding, and a cost of learning, language drift, that its prior-preservation loss pays to prevent.
title: 'DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation'
version: 2
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read, from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). The record held no LIT with arXiv
    2208.12242, this title or this first author with this subject,
    checked on 2026-11-12. Checked against the arXiv API the same day:
    Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein and Kfir Aberman, arXiv 2208.12242, v1 submitted 2022-08-25,
    which is `published:`. The summary follows the arXiv abstract and what
    A says of the work; a reading should check both.
- version: 2
  date: '2026-11-12'
  note: >-
    Read (NOTE-tmp9kwwm) from arXiv v2 (2208.12242, 15 March 2023; v1 of 25 August 2022). Read: §§1–5, Tables 1–4, and the supplementary material in the arXiv PDF. References skipped; figures through captions. Status Deferred to Active. THEORY-tmplz597 filed. Venue or type: CVPR 2023 (arXiv comment: "Published at CVPR 2023"). Corrections: None; the reading was of v2. The summary is rewritten from the reading.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-12'
published: '2022-08-25'
arxiv: '2208.12242'
first_author: 'Ruiz'
keywords:
- 'DreamBooth'
- 'subject-driven generation'
- 'fine-tuning'
- 'prior preservation'
implementations: []
summary: >-
  Ruiz et al. (2022), arXiv 2208.12242, CVPR 2023, read in [NOTE-tmp9kwwm](../notes.d/NOTE-tmp9kwwm.md). Fine-tuning every weight of a text-to-image diffusion model on 3–5 images of a subject, bound to a rare-token identifier and regularized by a class-prior-preservation loss, renders the subject in new contexts with higher DINO fidelity than Textual Inversion (0.668 against 0.569 on Stable Diffusion), at about 5 minutes on one A100 per subject. Registered from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). It bears on [CASE-tmp40vka](../cases.d/CASE-tmp40vka.md), [CASE-tmp3isyl](../cases.d/CASE-tmp3isyl.md) and [QUESTION-095](../questions.d/QUESTION-095.md).
---
<!-- inactive-ok-file: THEORY-tmplz597 CASE-tmp40vka CASE-tmp3isyl — Proposed; the reading's account and the entries it bears on, filed on the same branch -->

# LIT-tmp3pjii: DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation

Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein and Kfir Aberman (2022). "DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation." arXiv 2208.12242; CVPR 2023 (arXiv comment: "Published at CVPR 2023").

## Key takeaways

Read in [NOTE-tmp9kwwm](../notes.d/NOTE-tmp9kwwm.md); the account is [THEORY-tmplz597](../theory.d/THEORY-tmplz597.md). Subject-driven generation by fine-tuning all of a diffusion model's weights on a few images, with a prior-preservation loss, a benchmark and a DINO subject-fidelity metric.

## Standing in the record

Registered on 2026-11-12 from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), for the history of how image
generators keep a character's identity ([CASE-tmp40vka](../cases.d/CASE-tmp40vka.md)), and read the same
day at the owner's request. It is machine-learning method, read here for
the economics of amortization ([QUESTION-095](../questions.d/QUESTION-095.md)), not for practice.
