---
status: Deferred
status_note: >-
  filed 2026-10-26, not read. Registered from the owner's exchange
  "Experimental Infrastructure Review", shared at
  https://chatgpt.com/share/6adfa6e4-a0b0-83e9-b3a0-0b53e6000277 and read
  from the saved copy the owner uploaded, which holds turns T18–T24 only. No
  NOTE is filed.
title: 'Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T24 the reply says "recent work on fine-tuning finds
    that circuit connectivity can change substantially even when the
    components involved remain similar", with no citation. An arXiv search
    on 2026-10-26 found this paper, whose abstract states that finding.
    Checked against the arXiv record: Xu Wang, Yan Hu, Wenyu Du, Reynold
    Cheng, Benyou Wang and Difan Zou, arXiv 2502.11812, v1 submitted 17
    February 2025, which is `published:`. The ICML 2025 virtual programme
    and mlanthology list it as an ICML 2025 paper; its PMLR page was not
    seen. The identification rests on that one sentence and is the least
    certain of this exchange's.
tags:
- representation-learning
- anthology-candidate
date: '2026-10-26'
published: '2025-02-17'
arxiv: '2502.11812'
first_author: 'Wang'
keywords:
- 'fine-tuning'
- 'circuit analysis'
- 'mechanistic interpretability'
- 'LoRA'
- 'circuit-aware LoRA'
implementations: []
summary: >-
  Wang, Hu, Du, Cheng, Wang & Zou (2025), arXiv:2502.11812, ICML 2025. On
  mathematical tasks where fine-tuning brings large gains, circuits
  identified at checkpoints keep high node similarity before and after
  fine-tuning while their edges change significantly, unlike earlier reports
  that fine-tuning only adds components. A circuit-aware LoRA that assigns
  ranks by edge change improves on standard LoRA by 2.46% on average at
  similar size (abstract).
---
<!-- inactive-ok-file: CLAIM-367 — Proposed; the claim the exchange applied to training, named, nothing here rests on it -->

# LIT-tmpf4hwb: Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis

Wang, X., Hu, Y., Du, W., Cheng, R., Wang, B. & Zou, D. (2025). Towards
understanding fine-tuning mechanisms of LLMs via circuit analysis. *ICML
2025*. arXiv:2502.11812.

Not read. The summary is drawn from the abstract, and a reading should
check it first.

## Why this is here

Cited at T24 for the point that the relations among a network's components
can reorganize while the components stay the same, which the reply reads as
the network analogue of members reorganizing into new perspectives. It bears
on [QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md), and on [CLAIM-367](../claims.d/CLAIM-367.md) (which unit a training-time condition
belongs to depends on how units are individuated).
