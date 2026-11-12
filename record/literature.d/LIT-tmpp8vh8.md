---
status: Deferred
status_note: >-
  filed 2026-11-12, not read. Registered from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), where A cites it at
  A18, for training-free identity preservation in 2024. No reading was attempted; arXiv carries the paper.
title: 'InstantID: Zero-shot Identity-Preserving Generation in Seconds'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read, from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). The record held no LIT with arXiv
    2401.07519, this title or this first author with this subject,
    checked on 2026-11-12. Checked against the arXiv API the same day:
    Qixun Wang, Xu Bai, Haofan Wang, Zekui Qin, Anthony Chen, Huaxia Li, Xu Tang and Yao Hu, arXiv 2401.07519, v1 submitted 2024-01-15,
    which is `published:`. The summary follows the arXiv abstract and what
    A says of the work; a reading should check both.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-12'
published: '2024-01-15'
arxiv: '2401.07519'
first_author: 'Wang'
keywords:
- 'InstantID'
- 'identity preservation'
- 'zero-shot personalization'
- 'IdentityNet'
implementations: []
summary: >-
  Wang et al., arXiv 2401.07519. Here because A cited it in
  the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), for the history of how image generators keep a character's
  identity, which the owner asked to compare across model generations
  (U7). It bears on the owner's case CASE-tmp40vka and on the proposed study
  CASE-tmp3isyl, both for QUESTION-095: whether the identity is learned once
  into weights or read from references at every use. What A says of it is
  unverified until read.
---

# LIT-tmpp8vh8: InstantID: Zero-shot Identity-Preserving Generation in Seconds

Qixun Wang, Xu Bai, Haofan Wang, Zekui Qin, Anthony Chen, Huaxia Li, Xu Tang and Yao Hu (2024). "InstantID: Zero-shot Identity-Preserving Generation in Seconds." arXiv 2401.07519.

## Key takeaways

*Registered from the exchange, not read.* The arXiv abstract states the trade the case is about in its own terms: methods such as Textual Inversion, DreamBooth and LoRA are "hindered by high storage demands, lengthy fine-tuning processes, and the need for multiple reference images", while ID-embedding methods require "only a single forward inference"; InstantID is a "plug-and-play module" working from "a single facial image".

## Standing in the record

Registered on 2026-11-12 from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), where A cites it at A18, for training-free identity preservation in 2024. It
is provenance for the history of generations in CASE-tmp40vka, the owner's case
of how changing costs move the choice between learning a character into
weights and conditioning on references at each use, and a component of
the comparison CASE-tmp3isyl proposes. It is machine-learning method, registered here
for the economics of amortization (QUESTION-095), not for practice.
