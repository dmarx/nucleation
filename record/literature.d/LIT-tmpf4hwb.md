---
status: Active
status_note: >-
  read 2026-10-26 (NOTE-tmplotfq) in full, from the arXiv copy (v2, the
  ICML 2025 version); worth reading for its tracking of EAP-IG circuits
  across fine-tuning checkpoints on tasks the pretrained model fails, with
  node change rates of 15–24% against edge change rates of 66–80%, and for
  using the layers whose edges change most to allocate LoRA rank. Read it
  knowing that the node–edge contrast has no null comparison at the same
  edge budget and that a fixed edge budget produces it by itself
  (THEORY-tmpoirdq), that it concerns fine-tuning a pretrained model on
  arithmetic rather than development from initialization, and that the
  abstract's 2.46% gain is not recoverable from its tables.
title: 'Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis'
version: 2
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
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmplotfq), from the arXiv copy, v2 of 13 June 2025,
    fetched 2026-10-26; its footer confirms ICML 2025, PMLR 267. Status
    Deferred → Active. One THEORY filed, THEORY-tmpoirdq, Proposed. The
    identification is checked against the reading and holds: T24's
    "circuit connectivity can change substantially even when the
    components involved remain similar" matches the abstract clause by
    clause (nodes keep high similarity, edges change significantly), and
    the works the paper contrasts itself with found the opposite. It still
    rests on one uncited sentence. The summary is checked and the reported
    gain marked as not reproduced.
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
  five arithmetic tasks where LoRA fine-tuning of Pythia-1.4B brings large
  gains, EAP-IG circuits found at successive checkpoints keep most of
  their nodes while most of their edges change, unlike earlier reports
  that fine-tuning only adds components. A circuit-aware LoRA that assigns
  higher rank to the layers whose edges change most beats uniform and
  random rank allocation at similar size (the abstract's 2.46% average
  gain over LoRA is not recoverable from the tables, which give about
  1.8–2.4 points), and the union of two subtasks' circuits approximates a
  two-step task's circuit.
---
<!-- inactive-ok-file: THEORY-tmpoirdq — Proposed; the account drawn from this reading, cited as open -->
<!-- inactive-ok-file: CLAIM-367 — Proposed; the claim the exchange applied to training, named, nothing here rests on it -->

# LIT-tmpf4hwb: Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis

Wang, X., Hu, Y., Du, W., Cheng, R., Wang, B. & Zou, D. (2025). Towards
understanding fine-tuning mechanisms of LLMs via circuit analysis. *ICML
2025*. arXiv:2502.11812.

Read in full on 2026-10-26 (NOTE-tmplotfq). One account was drawn from
it: THEORY-tmpoirdq. The identification from T24 was checked against the
reading and holds (see the history).

## Why this is here

Cited at T24 for the point that the relations among a network's components
can reorganize while the components stay the same, which the reply reads as
the network analogue of members reorganizing into new perspectives. It bears
on [QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md), and on [CLAIM-367](../claims.d/CLAIM-367.md) (which unit a training-time condition
belongs to depends on how units are individuated).
