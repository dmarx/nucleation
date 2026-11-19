---
status: Active
title: 'What drives the emergence of symbolic mechanisms in large language models?'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Filed and read the same day. Registered from U9 of the exchange
    "Topological protection explained" (2026-11-18,
    https://chatgpt.com/share/6afe6dd0-9d78-83ea-9782-f55680665dcf), where
    the owner had "a hunch this fibration approach relates nicely to" it.
    Identifier checked on the arXiv API on 2026-11-19, no email address
    sent: v1 submitted 2026-11-09, cs.CL; the PDF footer names NeurIPS
    2026. Not held before: no hit for the id, the title, Li or Webb as
    first author in record/literature.d. Read from the arXiv PDF v1 in
    NOTE-tmp70cux.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-19'
published: '2026-11-09'
arxiv: '2611.13270'
first_author: 'Li'
keywords:
- symbolic mechanisms
- data diversity
- role-token bias
- binding IDs
- causal intervention
implementations: []
summary: >-
  Melody Zixuan Li and Taylor Webb (2026), arXiv 2611.13270. Small
  transformers and attention-free MLPs trained from scratch on in-context
  ABA/ABB rule completion with arbitrary tokens. Whether a mean-difference
  rule vector flips the output to the other rule's answer (the flip rate)
  depends on the diversity of the training data: vocabulary size, number
  of rules, number of examples, and role-token bias. Every architecture
  tested reaches it at high diversity. Read in [NOTE-tmp70cux](../notes.d/NOTE-tmp70cux.md); its account
  is [THEORY-tmpmtmq7](../theory.d/THEORY-tmpmtmq7.md). The owner's hunch that it relates to graph
  fibrations is filed as [QUESTION-tmpex36a](../questions.d/QUESTION-tmpex36a.md); the paper itself says nothing
  at the level of units or partitions.
---
<!-- inactive-ok-file: THEORY-tmpmtmq7 — Proposed; cited in this filing of 2026-11-19 -->

# LIT-tmpqgxkn: What drives the emergence of symbolic mechanisms in large language models?

Li and Webb (2026). arXiv 2611.13270.

## Key takeaways

- Data diversity, on four axes, decides whether a token-invariant,
  causally swappable rule representation develops; the architectural
  features tested are not necessary for it at high diversity.
- At small vocabularies the 12-layer model first solves the task without
  it, and acquires it only well after accuracy has converged.
- No random-initialization baseline; the MLP's mechanism is left open by
  the authors.

## Standing in the record

Registered from the owner's U9. Read in [NOTE-tmp70cux](../notes.d/NOTE-tmp70cux.md).
