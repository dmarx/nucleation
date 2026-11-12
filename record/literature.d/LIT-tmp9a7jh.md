---
status: Active
title: 'Retrieval Collapses When AI Pollutes the Web'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12, in NOTE-tmpaeun2; account THEORY-tmp5zp11. Status
    Active. The reading found the arXiv version 2602.16136 (v1 2026-02-18,
    checked on the arXiv API), the camera-ready text of the WWW '26 short
    paper; `published:` moves to that earlier date (ADR-002), and the arXiv
    id is added.
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read, from the exchange "Medical Ethics and Media Enshitification" (2026-11-11). Checked against Crossref on 2026-11-12 (proceedings-article). The record held no LIT with this DOI, title or first author. Crossref's earliest exact date is 2026-04-12; `published:` is that date (ADR-002). The summary is how A describes the work; a reading should check it first.
tags:
- information-retrieval
date: '2026-11-12'
published: '2026-02-18'
doi: '10.1145/3774904.3792955'
arxiv: '2602.16136'
first_author: 'Yu'
keywords: []
implementations: []
summary: >-
  Yu et al. (2026), DOI-10.1145/3774904.3792955. Read on 2026-11-12 in
  [NOTE-tmpaeun2](../notes.d/NOTE-tmpaeun2.md): The authors name "Retrieval Collapse", a two-stage failure
  in which (1) AI-generated content comes to dominate search results,
  eroding source diversity, and (2) low-quality or adversarial synthetic
  content enters the retrieval pipeline. On 1,000 MS MARCO queries, each
  with ten Google-retrieved web documents (Original Pool), they add
  GPT-5-nano documents one per round for 20 rounds (pool contamination 0% →
  66.7%), in two scenarios: an "SEO" pool (LLM rewrites of original
  documents with high-IDF keywords) and an "Abuse" pool (clickbait drafts
  with named entities and numbers falsified). Its account is
  [THEORY-tmp5zp11](../theory.d/THEORY-tmp5zp11.md). Registered from the exchange "Medical Ethics and Media
  Enshitification" (2026-11-11), where A cited it at A35 §3.
---
<!-- inactive-ok-file: THEORY-tmp5zp11 — Proposed; filed from the same exchange -->

# LIT-tmp9a7jh: Retrieval Collapses When AI Pollutes the Web

Hongyeon Yu, Dongchan Kim and Young-Bum Kim (2026). "Retrieval Collapses When AI Pollutes the Web." *Proceedings of the ACM Web Conference 2026 8745-8748*. DOI-10.1145/3774904.3792955.

## Key takeaways

Read on 2026-11-12 ([NOTE-tmpaeun2](../notes.d/NOTE-tmpaeun2.md)). A named failure mode for retrieval (as
distinct from training-time model collapse), with descriptive metrics PCR /
ECR / CCR, and a small controlled simulation showing exposure amplification
of synthetic content and the decoupling of answer accuracy from source
diversity.

## Standing in the record

Registered on 2026-11-12 from the exchange "Medical Ethics and Media Enshitification" (2026-11-11), where A cited it at A35 §3. It bears on [LIT-971](LIT-971.md).

Read on 2026-11-12; the reading is [NOTE-tmpaeun2](../notes.d/NOTE-tmpaeun2.md) and its account
[THEORY-tmp5zp11](../theory.d/THEORY-tmp5zp11.md).
