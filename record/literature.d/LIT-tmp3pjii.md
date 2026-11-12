---
status: Deferred
status_note: >-
  filed 2026-11-12, not read. Registered from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), where A cites it at
  A18's table of generations, as the 2022-23 way of learning subject-specific weights. No reading was attempted; arXiv carries the paper.
title: 'DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation'
version: 1
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
  Ruiz et al., arXiv 2208.12242. Here because A cited it in
  the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), for the history of how image generators keep a character's
  identity, which the owner asked to compare across model generations
  (U7). It bears on the owner's case [CASE-tmp40vka](../cases.d/CASE-tmp40vka.md) and on the proposed study
  [CASE-tmp3isyl](../cases.d/CASE-tmp3isyl.md), both for [QUESTION-095](../questions.d/QUESTION-095.md): whether the identity is learned once
  into weights or read from references at every use. What A says of it is
  unverified until read.
---

# LIT-tmp3pjii: DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation

Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein and Kfir Aberman (2022). "DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation." arXiv 2208.12242.

## Key takeaways

*Registered from the exchange, not read.* The arXiv abstract: "Given as input just a few images of a subject, we fine-tune a pretrained text-to-image model such that it learns to bind a unique identifier with that specific subject." The arXiv comment gives CVPR 2023.

## Standing in the record

Registered on 2026-11-12 from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), where A cites it at A18's table of generations, as the 2022-23 way of learning subject-specific weights. It
is provenance for the history of generations in [CASE-tmp40vka](../cases.d/CASE-tmp40vka.md), the owner's case
of how changing costs move the choice between learning a character into
weights and conditioning on references at each use, and a component of
the comparison [CASE-tmp3isyl](../cases.d/CASE-tmp3isyl.md) proposes. It is machine-learning method, registered here
for the economics of amortization ([QUESTION-095](../questions.d/QUESTION-095.md)), not for practice.
