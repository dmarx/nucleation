---
number: 216
status: Open
formerly:
- QUESTION-tmpu5do1
title: "Does the output Fisher–Rao geometry agreement across language models replicate with released code, and does it fall when models are fitted to different laws while their activation geometry stays as it was, with only a small part of the shared eigenvector structure exceeding a fair law-matched null?"
version: 1
tags:
- information-geometry
- representation-learning
date: '2026-10-20'
line: 'pragmatic-transport'
refines:
- QUESTION-027
summary: >-
  The promotion condition formerly on [THEORY-230](../theory.d/THEORY-230.md). [THEORY-230](../theory.d/THEORY-230.md) was narrowed
  and promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v2 and v3). Its identification is
  re-derived: the Fisher–Rao geometry of next-token laws is a function of
  the laws. Its measurement is one study read in full: mean rank agreement
  0.88 against 0.62 in Picozzi's ten models, and about 9% of the top
  eigenvector overlap beyond a displacement-matched null. Replication, and
  a test that varies the law, are open.
---

# QUESTION-216: Does the output Fisher–Rao geometry agreement across language models replicate with released code, and does it fall when models are fitted to different laws while their activation geometry stays as it was, with only a small part of the shared eigenvector structure exceeding a fair law-matched null?

## Why it is a question

[THEORY-230](../theory.d/THEORY-230.md) holds what Picozzi (2026) proves and what it measured. The
output geometry is a function of the next-token laws, so models with
identical laws share it. Across ten models it agreed far more than
activation geometry did. The study is a single-author preprint with code
on request. Its models were fitted to largely shared corpora, so it does
not separate the law from the corpus on natural text. The 9% residual
is measured against one null, whose fairness is itself in question.
Until 2026-10-20 this was [THEORY-230](../theory.d/THEORY-230.md)'s promote_when.

## What would answer it

- An independent replication, with released code, of the
  cross-architecture agreement and of the law-matched null behind the 9%
  figure.
- A test that varies the law while holding training fixed: models
  trained on different corpora, languages or post-training, compared on
  one battery. The account holds if output-geometry agreement falls as
  the laws diverge while activation geometry stays as it was, and if what
  exceeds the law-matched null stays small.

Against it: models fitted to clearly different laws that agree in output
geometry as much as models fitted to the same law, or a fair law-matched
null that leaves most of the shared eigenvector structure unexplained.
What cannot settle it: further same-corpus comparisons, or the steering
and editing results, which test the metric's use, not its sharing.
