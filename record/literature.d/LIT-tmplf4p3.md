---
status: Active
status_note: >-
  The memorization arm's baseline: a first stage with random labels still
  changes later cost, through first-layer covariance alignment, and can
  reverse; the arm needs input-statistics controls. Read on 2026-11-19
  (NOTE-tmpmkl72).
title: 'What Do Neural Networks Learn When Trained With Random Labels?'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Registered and read on 2026-11-19 at the owner's request
    (LEAD-006), from arXiv 2006.10455v2 (PDF, 11 Nov 2020); seven
    authors, not six as the search listed. Not held before; the identifier
    checked on the arXiv API.
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
published: '2020-06-18'
arxiv: '2006.10455'
first_author: 'Maennel'
keywords: []
implementations: []
summary: >-
  Maennel, Alabdulmohsin, Tolstikhin, Baldock, Bousquet, Gelly and Keysers
  (NeurIPS 2020), arXiv 2006.10455. CNNs pretrained on random labels,
  rescaled to their initial weight norms and given a fresh head, usually
  train faster on fresh images than from scratch; sampling first-layer
  filters from the learned weight covariance, which they prove aligns with
  the data covariance, reproduces the gain. In other settings the same
  pretraining slows later training, which they attribute to later-layer
  units becoming permanently inactive; width mitigates it. First-stage
  accuracy is never reported. Read in NOTE-tmpmkl72; account
  THEORY-tmpw5877.
---

# LIT-tmplf4p3: What Do Neural Networks Learn When Trained With Random Labels?

Hartmut Maennel, Ibrahim Alabdulmohsin, Ilya Tolstikhin, Robert J. N. Baldock, Olivier Bousquet, Sylvain Gelly and Daniel Keysers (2020). "What Do Neural Networks Learn When Trained With Random Labels?". NeurIPS 2020; arXiv 2006.10455.

## Standing in the record

Registered and read on 2026-11-19 at the owner's request, under LEAD-006.
