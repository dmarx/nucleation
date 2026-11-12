---
status: Deferred
status_note: >-
  filed 2026-11-12, not read. Registered from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), where A cites it at
  A18's table and the owner's case, as the method behind the character LoRAs the thread weighs against reference conditioning; the paper is about language models, and its use for image-generation characters came later. No reading was attempted; arXiv carries the paper.
title: 'LoRA: Low-Rank Adaptation of Large Language Models'
version: 1
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
  Hu et al., arXiv 2106.09685. Here because A cited it in
  the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), for the history of how image generators keep a character's
  identity, which the owner asked to compare across model generations
  (U7). It bears on the owner's case CASE-tmp40vka and on the proposed study
  CASE-tmp3isyl, both for QUESTION-095: whether the identity is learned once
  into weights or read from references at every use. What A says of it is
  unverified until read.
---

# LIT-tmp5b18b: LoRA: Low-Rank Adaptation of Large Language Models

Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang and Weizhu Chen (2021). "LoRA: Low-Rank Adaptation of Large Language Models." arXiv 2106.09685.

## Key takeaways

*Registered from the exchange, not read.* The arXiv abstract gives the per-use side of the trade: LoRA "freezes the pre-trained model weights and injects trainable rank decomposition matrices", and, "unlike adapters", adds "no additional inference latency".

## Standing in the record

Registered on 2026-11-12 from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), where A cites it at A18's table and the owner's case, as the method behind the character LoRAs the thread weighs against reference conditioning; the paper is about language models, and its use for image-generation characters came later. It
is provenance for the history of generations in CASE-tmp40vka, the owner's case
of how changing costs move the choice between learning a character into
weights and conditioning on references at each use, and a component of
the comparison CASE-tmp3isyl proposes. It is machine-learning method, registered here
for the economics of amortization (QUESTION-095), not for practice.
