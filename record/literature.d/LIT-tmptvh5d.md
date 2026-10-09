---
status: Deferred
status_note: 'registered 2026-10-09 from arXiv, not read: only the abstract was seen. Filed from the reference list of the owner''s working manuscript. It stays Deferred until somebody reads it, not on merit.'
title: 'GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Registered, not read. Details checked against arXiv (v1 submitted 17
    October 2023; code at github.com/djghosh13/geneval). The venue is
    the manuscript's citation as arXiv only; NeurIPS 2023 Datasets and
    Benchmarks is where it appeared, not checked against a proceedings
    DOI. `published:` is the arXiv v1 date. Not held in the Anthology of
    the SOTA as a LIT: a grep of its record/ (clone of 2026-10-09,
    commit 1cffe8f) for the identifier, the title and the authors found
    the work named only in prose inside other entries, or not at all.
tags:
- representation-learning
- anthology-candidate
date: '2026-10-09'
published: '2023-10-17'
arxiv: '2310.11513'
first_author: 'Ghosh'
keywords:
- 'text-to-image'
- 'evaluation'
- 'compositionality'
- 'object detection'
- 'attribute binding'
implementations: []
summary: >-
  Ghosh, Hajishirzi & Schmidt (2023). An automated benchmark that uses
  object detectors to score text-to-image outputs on object co-
  occurrence, position, count and colour, agreeing well with human
  judgement; models of 2023 still fail at spatial relations and
  attribute binding. Unread.
---

# LIT-tmptvh5d: GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment

Dhruba Ghosh, Hannaneh Hajishirzi and Ludwig Schmidt (2023), *NeurIPS 2023
Datasets and Benchmarks* —
[ARXIV-2310.11513](https://arxiv.org/abs/2310.11513)

## Key takeaways

*Registered, not read.* From the abstract only: holistic metrics such as FID
and CLIPScore are unsuited to instance-level analysis, so GenEval uses object
detection models, linked to other discriminative vision models, to evaluate
compositional properties such as object co-occurrence, position, count and
colour, with strong agreement with humans. Recent open models improve markedly
but still fail at spatial relations and attribute binding. The record's
reading of compositional generalization in vision models is
[LIT-667](LIT-667.md).

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the works in the
reference list of the owner's working manuscript (October 2026) that the
record did not yet hold. See the curation entry of that day. It is a
machine-learning paper an anthology topic could hold (generative-modeling,
analysis-and-evaluation), so it carries the `anthology-candidate` flag
([ADR-005](../decisions.d/ADR-005.md)); it is here because the owner asked for
the manuscript's references to be filed in this record.
