---
status: Deferred
status_note: >-
  filed 2026-11-12, not read. Registered from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), where A cites it at
  A18, which dates it to 2024 with InstantID; arXiv v1 is of 2023-12-07, so A's year is not the year it first appeared. No reading was attempted; arXiv carries the paper.
title: 'PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read, from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). The record held no LIT with arXiv
    2312.04461, this title or this first author with this subject,
    checked on 2026-11-12. Checked against the arXiv API the same day:
    Zhen Li, Mingdeng Cao, Xintao Wang, Zhongang Qi, Ming-Ming Cheng and Ying Shan, arXiv 2312.04461, v1 submitted 2023-12-07,
    which is `published:`. The summary follows the arXiv abstract and what
    A says of the work; a reading should check both.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-12'
published: '2023-12-07'
arxiv: '2312.04461'
first_author: 'Li'
keywords:
- 'PhotoMaker'
- 'stacked ID embedding'
- 'personalized text-to-image generation'
implementations: []
summary: >-
  Li et al., arXiv 2312.04461. Here because A cited it in
  the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), for the history of how image generators keep a character's
  identity, which the owner asked to compare across model generations
  (U7). It bears on the owner's case [CASE-tmp40vka](../cases.d/CASE-tmp40vka.md) and on the proposed study
  [CASE-tmp3isyl](../cases.d/CASE-tmp3isyl.md), both for [QUESTION-095](../questions.d/QUESTION-095.md): whether the identity is learned once
  into weights or read from references at every use. What A says of it is
  unverified until read.
---

# LIT-tmp8l2rx: PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding

Zhen Li, Mingdeng Cao, Xintao Wang, Zhongang Qi, Ming-Ming Cheng and Ying Shan (2023). "PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding." arXiv 2312.04461.

## Key takeaways

*Registered from the exchange, not read.* The arXiv abstract encodes "an arbitrary number of input ID images into a stack ID embedding" and reports "better ID preservation ability than test-time fine-tuning based methods" with "significant speed improvements".

## Standing in the record

Registered on 2026-11-12 from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), where A cites it at A18, which dates it to 2024 with InstantID; arXiv v1 is of 2023-12-07, so A's year is not the year it first appeared. It
is provenance for the history of generations in [CASE-tmp40vka](../cases.d/CASE-tmp40vka.md), the owner's case
of how changing costs move the choice between learning a character into
weights and conditioning on references at each use, and a component of
the comparison [CASE-tmp3isyl](../cases.d/CASE-tmp3isyl.md) proposes. It is machine-learning method, registered here
for the economics of amortization ([QUESTION-095](../questions.d/QUESTION-095.md)), not for practice.
