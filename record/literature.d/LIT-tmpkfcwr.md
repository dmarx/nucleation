---
status: Active
title: 'Weight Decay Improves Language Model Plasticity'
version: 2
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Filed, not read. Identifier checked on the arXiv API on 2026-11-19, no
    email address sent: v1 submitted 2026-02-11. Not held: no hit for the
    identifier, the title or Han in record/literature.d.
- version: 2
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader, quotations rechecked by the
    filer; in NOTE-tmps6j9j, account THEORY-tmp8wxgt. URL read:
    https://arxiv.org/pdf/2602.11137 (served as arXiv:2602.11137v2, 28 May
    2026; 32 pages). The PDF states it appears in the Proceedings of the
    43rd International Conference on Machine Learning (ICML 2026), PMLR 306.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-19'
published: '2026-02-11'
arxiv: '2602.11137'
first_author: 'Han'
keywords: []
implementations: []
summary: >-
  Han, Bordt, Zhang and Kakade (2026), arXiv 2602.11137, ICML 2026. They
  pre-train Llama-2 and OLMo-2 models (0.5B-4B, at 20 and 140 tokens per
  parameter) across AdamW weight decay values, then fine-tune on twelve
  tasks. Weight decay above the default 0.1 gives better fine-tuned
  performance even where it worsens pre-training loss (OLMo-2-1B at 140
  tokens per parameter), so pre-training loss does not rank models by what
  they become. Plasticity is measured only as the fine-tuned score on the
  target task, and forgetting is not measured. It is here as a preventive
  training regime for overconsolidation (CLAIM-tmp8ljvp) and an arm of
  CASE-tmphsr99, and it is the clearest case for CLAIM-675's point that
  present capability does not rank later capability. Read in its NOTE.
  Read in NOTE-tmps6j9j; its account is THEORY-tmp8wxgt.
---
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-tmp8ljvp — Proposed; cited in this filing of 2026-11-19 -->

# LIT-tmpkfcwr: Weight Decay Improves Language Model Plasticity

Han, Bordt, Zhang, Kakade (2026). arXiv 2602.11137.

## Standing in the record

Registered on 2026-11-19 from A54 of the exchange "Topological protection explained". It would be a training regime that prevents overconsolidation ([CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)) and an arm of [CASE-tmphsr99](../cases.d/CASE-tmphsr99.md). Not read.
