---
status: Active
status_note: 'read in full 2026-11-27 ([NOTE-tmpanw10](../notes.d/NOTE-tmpanw10.md)); worth reading for a benchmark that changes only how a reasoning problem is presented, with its answer fixed, and finds large accuracy drops in open models, most from shuffled order and implicit reference. Read its cognitive-load framing as a label: the theory''s shared capacity limit is not tested.'
title: "Extraneous Cognitive Load in Large Language Models"
version: 2
history:
- version: 1
  date: '2026-11-27'
  note: >-
    Filed, not read. The record was searched by arXiv id and title and holds no entry. The arXiv API gives 2611.33197, posted 2026-11-16, by Arushi Gupta, Sheng Liu and James Zou, in cs.CL, cs.AI and cs.LG.
- version: 2
  date: '2026-11-27'
  note: >-
    Read in full (NOTE-tmpanw10) from the arXiv HTML v1 (CC BY 4.0; NeurIPS 2026), abstract, sections 1-6, references and appendices A-F with every table. The code the paper names, github.com/arushig100/CogLoadBench, was not fetched. The filer rechecked every quote the filing uses. Status set from the reading: Active. The summary is rewritten from the reading.
tags:
- cognition
- representation-learning
date: '2026-11-27'
published: '2026-11-16'
arxiv: '2611.33197'
first_author: 'Gupta'
implementations: []
summary: >-
  Gupta, Liu and Zou (2026). CogLoadBench holds a reasoning problem's target and answer fixed and changes only its presentation along five factors: quantity and similarity of distractors, an interfering second task, discontinuity (shuffled or interleaved steps) and underspecified reference. Across five open 4-14B models accuracy usually falls, by up to about 37 points (implicit reference) and 34 (shuffled order in Math). A per-model classifier on 30 activation statistics tells high- from low-load variants apart, but not across load factors it was not trained on, and steering along a learned direction recovers about 0.4 F1. Its account is [THEORY-tmpjgsul](../theory.d/THEORY-tmpjgsul.md).
---

# LIT-tmpukote: Extraneous Cognitive Load in Large Language Models

Gupta, Liu and Zou (2026), arXiv 2611.33197.

## Key takeaways

- Presentation alone, with the answer fixed, costs open models large amounts of accuracy; order and implicit reference cost most.
- The activation score detects which presentation the input had and does not generalize across factors; steering helps little.
- The cognitive-load reading is a label: intrinsic and extraneous load are never crossed.

## Standing in the record

Read at the owner's request of 2026-11-27. It bears on [CLAIM-1269](../claims.d/CLAIM-1269.md), [CLAIM-1086](../claims.d/CLAIM-1086.md), [CLAIM-1100](../claims.d/CLAIM-1100.md) and [CLAIM-tmpg2wk1](../claims.d/CLAIM-tmpg2wk1.md) ([NOTE-tmpanw10](../notes.d/NOTE-tmpanw10.md)).
