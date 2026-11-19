---
status: Active
status_note: >-
  Read on 2026-11-19 ([NOTE-tmphfhfu](../notes.d/NOTE-tmphfhfu.md)). Worth reading as a controlled study
  of when specialized data enters pretraining, with forgetting measured;
  its plasticity window is inferred, not measured.
title: 'Midtraining Bridges Pretraining and Posttraining Distributions'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Registered and read on 2026-11-19 at the owner's request (LEAD-
    tmp5lpoy), from arXiv 2510.14865v2 (2026-02-02; v1 2025-10-16), in full.
    Listed at ICML 2026 on icml.cc; the arXiv version names no venue. Not
    held before.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-19'
published: '2025-10-16'
arxiv: '2510.14865'
first_author: 'Liu'
keywords: []
implementations: []
summary: >-
  Liu, Neubig and Xiong (2025), arXiv 2510.14865. Pythia-architecture
  models (70M to 1B) pretrained on C4 with part of the later data replaced
  by specialized data: at matched total tokens, lower loss after a fixed
  fine-tuning budget on distant domains (code, math), little on close
  ones; a heavy code mix helps most when introduced early and ends worse
  than none when introduced late, which the authors read as a plasticity
  window. Final loss, not cost; one pretraining run per condition. Read in
  [NOTE-tmphfhfu](../notes.d/NOTE-tmphfhfu.md); account [THEORY-tmpd6smn](../theory.d/THEORY-tmpd6smn.md).
---

# LIT-tmpvfc1j: Midtraining Bridges Pretraining and Posttraining Distributions

Emmy Liu, Graham Neubig and Chenyan Xiong (2025). "Midtraining Bridges Pretraining and Posttraining Distributions". arXiv 2510.14865.

## Standing in the record

Registered and read on 2026-11-19 at the owner's request, under [LEAD-tmp5lpoy](../leads.d/LEAD-tmp5lpoy.md).
