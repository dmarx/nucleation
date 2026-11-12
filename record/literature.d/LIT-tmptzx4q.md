---
status: Deferred
status_note: >-
  filed 2026-11-12, not read. Registered from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), where A cites it at
  A18, as the 2023 start of image conditioning ("IP-Adapter offered image conditioning in 2023"). No reading was attempted; arXiv carries the paper.
title: 'IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read, from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). The record held no LIT with arXiv
    2308.06721, this title or this first author with this subject,
    checked on 2026-11-12. Checked against the arXiv API the same day:
    Hu Ye, Jun Zhang, Sibo Liu, Xiao Han and Wei Yang, arXiv 2308.06721, v1 submitted 2023-08-13,
    which is `published:`. The summary follows the arXiv abstract and what
    A says of the work; a reading should check both.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-12'
published: '2023-08-13'
arxiv: '2308.06721'
first_author: 'Ye'
keywords:
- 'IP-Adapter'
- 'image prompt'
- 'decoupled cross-attention'
- 'text-to-image diffusion'
implementations: []
summary: >-
  Ye et al., arXiv 2308.06721. Here because A cited it in
  the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), for the history of how image generators keep a character's
  identity, which the owner asked to compare across model generations
  (U7). It bears on the owner's case [CASE-tmp40vka](../cases.d/CASE-tmp40vka.md) and on the proposed study
  [CASE-tmp3isyl](../cases.d/CASE-tmp3isyl.md), both for [QUESTION-095](../questions.d/QUESTION-095.md): whether the identity is learned once
  into weights or read from references at every use. What A says of it is
  unverified until read.
---

# LIT-tmptzx4q: IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models

Hu Ye, Jun Zhang, Sibo Liu, Xiao Han and Wei Yang (2023). "IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models." arXiv 2308.06721.

## Key takeaways

*Registered from the exchange, not read.* The arXiv abstract presents "an effective and lightweight adapter to achieve image prompt capability for the pretrained text-to-image diffusion models", with "only 22M parameters", and the pretrained diffusion model frozen.

## Standing in the record

Registered on 2026-11-12 from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), where A cites it at A18, as the 2023 start of image conditioning ("IP-Adapter offered image conditioning in 2023"). It
is provenance for the history of generations in [CASE-tmp40vka](../cases.d/CASE-tmp40vka.md), the owner's case
of how changing costs move the choice between learning a character into
weights and conditioning on references at each use, and a component of
the comparison [CASE-tmp3isyl](../cases.d/CASE-tmp3isyl.md) proposes. It is machine-learning method, registered here
for the economics of amortization ([QUESTION-095](../questions.d/QUESTION-095.md)), not for practice.
