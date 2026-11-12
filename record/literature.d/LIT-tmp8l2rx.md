---
status: Active
status_note: >-
  read 2026-11-12 ([NOTE-tmpul1vj](../notes.d/NOTE-tmpul1vj.md)) from arXiv v1. Worth reading for Table 1, the batch's only side-by-side measurement of time and identity fidelity for trained and reference routes (DreamBooth 1284 s and Textual Inversion 2400 s against PhotoMaker 10 s and IP-Adapter 12 s on a V100). Cite the table, not §4.2's summary of it, which misnames a metric.
title: 'PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding'
version: 2
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
- version: 2
  date: '2026-11-12'
  note: >-
    Read (NOTE-tmpul1vj) from arXiv v1 (2312.04461, 7 December 2023, the only version). Read: abstract, §§1–5, Table 1, the ablations (Table 2, Fig. 7) and appendices F and G. Other appendix galleries skimmed; references skipped. Table 1 was read from a layout extraction of the PDF. Status Deferred to Active. THEORY-tmpvarvt filed. Venue or type: technical report (arXiv comment: "Tech report"). Corrections: Article type: a technical report, by the arXiv comment. No venue on the arXiv record. §4.2's text disagrees with its own Table 1 (below). The summary is rewritten from the reading.
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
  Li et al. (2023), arXiv 2312.04461, a technical report, read in [NOTE-tmpul1vj](../notes.d/NOTE-tmpul1vj.md). A tuning-free personalization model for SDXL, trained once on 8 A100s for two weeks, stacks embeddings of several photos of one person in place of the class word. In Table 1 it personalizes in 10 s against DreamBooth's 1284 s and Textual Inversion's 2400 s, with the highest CLIP-I and DINO of the five methods and the second-highest face similarity, behind IP-Adapter. Registered from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). It bears on [CASE-tmp40vka](../cases.d/CASE-tmp40vka.md), [CASE-tmp3isyl](../cases.d/CASE-tmp3isyl.md), [CLAIM-tmpnwq8a](../claims.d/CLAIM-tmpnwq8a.md) and [QUESTION-095](../questions.d/QUESTION-095.md).
---
<!-- inactive-ok-file: THEORY-tmpvarvt CASE-tmp40vka CASE-tmp3isyl CLAIM-tmpnwq8a — Proposed; the reading's account and the entries it bears on, filed on the same branch -->

# LIT-tmp8l2rx: PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding

Zhen Li, Mingdeng Cao, Xintao Wang, Zhongang Qi, Ming-Ming Cheng and Ying Shan (2023). "PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding." arXiv 2312.04461; technical report (arXiv comment: "Tech report").

## Key takeaways

Read in [NOTE-tmpul1vj](../notes.d/NOTE-tmpul1vj.md); the account is [THEORY-tmpvarvt](../theory.d/THEORY-tmpvarvt.md). Feed-forward, tuning-free identity personalization from any number of photos, with an ID-grouped training-data pipeline.

## Standing in the record

Registered on 2026-11-12 from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), for the history of how image
generators keep a character's identity ([CASE-tmp40vka](../cases.d/CASE-tmp40vka.md)), and read the same
day at the owner's request. It is machine-learning method, read here for
the economics of amortization ([QUESTION-095](../questions.d/QUESTION-095.md)), not for practice.
