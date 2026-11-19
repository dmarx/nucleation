---
status: Active
status_note: >-
  The closest match yet to LEAD-006: a located shared component,
  transplanted alone, carries a later sample saving against a size-matched
  random control. No matched comparison of organizations. Read on
  2026-11-19 (NOTE-tmpnu6cu).
title: 'Instilling Inductive Biases with Subnetworks'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Registered and read on 2026-11-19 at the owner's request
    (LEAD-006), from arXiv 2310.10899v2 (PDF, 1 Feb 2024). Not held
    before; the identifier checked on the arXiv API.
tags:
- compositionality
- learning-theory
- representation-learning
date: '2026-11-19'
published: '2023-10-17'
arxiv: '2310.10899'
first_author: 'Zhang'
keywords: []
implementations: []
summary: >-
  Zhang, Lepori and Pavlick, arXiv 2310.10899. Small GPT-2-style
  transformers learn a + ab mod 7; a weight mask isolates a subnetwork
  computing ab mod 7 (3 to 8 per cent of masked weights), which is copied
  frozen into a fresh model learning a² + ab mod 7 from ambiguous data
  plus disambiguating samples. The transplant reaches near-perfect
  accuracy with about 1000 disambiguating samples, at least matching
  transfer of the whole model; a same-size random subnetwork of the
  trained model needs about six times as much data; scratch reaches about
  51 per cent. First-stage cost not counted; seeds reported for one
  configuration. Read in NOTE-tmpnu6cu; account THEORY-tmp51mqd.
---

# LIT-tmpsnc7a: Instilling Inductive Biases with Subnetworks

Enyan Zhang, Michael A. Lepori and Ellie Pavlick (2023). "Instilling Inductive Biases with Subnetworks". arXiv 2310.10899.

## Standing in the record

Registered and read on 2026-11-19 at the owner's request, under LEAD-006.
