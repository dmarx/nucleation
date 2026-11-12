---
status: Active
status_note: >-
  read 2026-11-12 ([NOTE-tmpz29f3](../notes.d/NOTE-tmpz29f3.md)) from arXiv v2. Worth reading for the structure of a low-rank module: an additive update to one specific set of frozen weights, recovered by subtracting it, which amplifies directions already in those weights; and for its per-use claim of no added latency once merged. Language models only.
title: 'LoRA: Low-Rank Adaptation of Large Language Models'
version: 2
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read, from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). The record held no LIT with arXiv
    2106.09685, this title or this first author with this subject,
    checked on 2026-11-12. Checked against the arXiv API the same day:
    Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang and Weizhu Chen, arXiv 2106.09685, v1 submitted 2021-06-17,
    which is `published:`. The summary follows the arXiv abstract and what
    A says of the work; a reading should check both.
- version: 2
  date: '2026-11-12'
  note: >-
    Read (NOTE-tmpz29f3) from arXiv v2 (2106.09685, 16 October 2021; v1 of 17 June 2021). Read: abstract, §§1–4, §7 and §8 in full; §5 (experiments) and §6 (related work) skimmed; appendices skipped. Status Deferred to Active. THEORY-tmp6v6q8 filed. Venue or type: arXiv preprint; no venue on the arXiv record (cited elsewhere as ICLR, not checked). Corrections: None. The summary is rewritten from the reading.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-12'
published: '2021-06-17'
arxiv: '2106.09685'
first_author: 'Hu'
keywords:
- 'LoRA'
- 'low-rank adaptation'
- 'parameter-efficient fine-tuning'
implementations: []
summary: >-
  Hu et al. (2021), arXiv 2106.09685, read in [NOTE-tmpz29f3](../notes.d/NOTE-tmpz29f3.md). Adapting a large pretrained Transformer by freezing its weights W0 and training only a low-rank additive update BA to selected matrices matches full fine-tuning on the language benchmarks reported, stores about 10,000× less per task on GPT-3, and adds no inference latency once merged; the update "amplifies some features that are already in W". It is the method behind the character LoRAs of [CASE-tmp40vka](../cases.d/CASE-tmp40vka.md), though the paper is about language models. Registered from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). It grounds [CLAIM-tmpnwq8a](../claims.d/CLAIM-tmpnwq8a.md)'s premise and bears on [QUESTION-095](../questions.d/QUESTION-095.md).
---
<!-- inactive-ok-file: THEORY-tmp6v6q8 CASE-tmp40vka CLAIM-tmpnwq8a — Proposed; the reading's account and the entries it bears on, filed on the same branch -->

# LIT-tmp5b18b: LoRA: Low-Rank Adaptation of Large Language Models

Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang and Weizhu Chen (2021). "LoRA: Low-Rank Adaptation of Large Language Models." arXiv 2106.09685; arXiv preprint; no venue on the arXiv record (cited elsewhere as ICLR, not checked).

## Key takeaways

Read in [NOTE-tmpz29f3](../notes.d/NOTE-tmpz29f3.md); the account is [THEORY-tmp6v6q8](../theory.d/THEORY-tmp6v6q8.md). Parameter-efficient adaptation that adds no inference latency once merged and stores only a small per-task module beside a shared frozen model.

## Standing in the record

Registered on 2026-11-12 from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), for the history of how image
generators keep a character's identity ([CASE-tmp40vka](../cases.d/CASE-tmp40vka.md)), and read the same
day at the owner's request. It is machine-learning method, read here for
the economics of amortization ([QUESTION-095](../questions.d/QUESTION-095.md)), not for practice.
