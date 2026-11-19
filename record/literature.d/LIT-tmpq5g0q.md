---
status: Active
title: 'Overtrained Language Models Are Harder to Fine-Tune'
version: 2
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Filed, not read. Identifier checked on the arXiv API on 2026-11-19, no
    email address sent: v1 submitted 2025-03-24. Not held: no hit for the
    identifier, the title or Springer in record/literature.d.
- version: 2
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader, quotations rechecked by the
    filer; in NOTE-tmpp1jb7, account THEORY-tmp3dqbl. URL read:
    https://arxiv.org/pdf/2503.19206 (served as arXiv:2503.19206v2, 28 Mar
    2025; 72 pages).
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-19'
published: '2025-03-24'
arxiv: '2503.19206'
first_author: 'Springer'
keywords: []
implementations: []
summary: >-
  Springer, Goyal, Wen, Kumar, Yue, Malladi, Neubig and Raghunathan
  (2025), arXiv 2503.19206. They name "catastrophic overtraining": past an
  inflection point, longer pre-training leaves a worse model after
  instruction or multimodal fine-tuning even though the base model keeps
  improving (OLMo-1B at 3T against 2.3T tokens; not seen at 7B up to 3T).
  In controlled small models and a deep-linear theory, they trace it to
  "progressive sensitivity": a fine-tune of fixed size destroys more pre-
  trained capability the longer the model was pre-trained. The cost shows
  up mostly as forgetting caused by the acquisition, and the new task
  itself gets worse only in some settings. It is here as the prime
  empirical case for overconsolidation ([CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)) and the Pythia
  study ([CASE-tmphsr99](../cases.d/CASE-tmphsr99.md)), which it qualifies: the case is mainly about
  forgetting under modification, not a higher budget to acquire. Read in
  its NOTE. Read in [NOTE-tmpp1jb7](../notes.d/NOTE-tmpp1jb7.md); its account is [THEORY-tmp3dqbl](../theory.d/THEORY-tmp3dqbl.md).
---
<!-- inactive-ok-file: THEORY-tmp3dqbl — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-tmp8ljvp — Proposed; cited in this filing of 2026-11-19 -->

# LIT-tmpq5g0q: Overtrained Language Models Are Harder to Fine-Tune

Springer, Goyal, Wen, Kumar et al. (2025). arXiv 2503.19206.

## Standing in the record

Registered on 2026-11-19 from A50 of the exchange "Topological protection explained". It is the prime empirical case for overconsolidation, [CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md), and the Pythia study [CASE-tmphsr99](../cases.d/CASE-tmphsr99.md). Not read.
