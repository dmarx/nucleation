---
status: Deferred
status_note: 'unread, registered 2026-10-14 for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md) from arXiv metadata and the standard statement of its result. No attempt to read it is recorded.'
title: 'Optimality of the Johnson-Lindenstrauss Lemma'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Filed, not read, at the owner's request after a survey found the record
    meets random projections from three directions without holding the
    result they share. Citation checked against arXiv on 2026-10-14. Not held in the Anthology of the SOTA: a grep of its record/ (clone at commit d1573d2) for the title, the identifier and the result's name found nothing. Published at FOCS 2017.
tags:
- mathematics
date: '2026-10-14'
published: '2016-09-07'
arxiv: '1609.02094'
first_author: 'Larsen'
keywords:
- 'Johnson-Lindenstrauss lemma'
- 'dimensionality reduction'
- 'lower bound'
- 'optimality'
extends:
- LIT-tmp7skui
implementations: []
summary: >-
  Larsen & Nelson (2017), FOCS 2017, [ARXIV-1609.02094](https://arxiv.org/abs/1609.02094). For every d, n and ε within the lemma's range, some n points in ℓ₂ need Ω(ε⁻² log n) dimensions under any embedding, linear or not, with distortion 1 + ε, so the lemma's bound is tight. Unread.
---

# LIT-tmp8s1wj: Optimality of the Johnson-Lindenstrauss Lemma

Kasper Green Larsen and Jelani Nelson (2017), "Optimality of the Johnson-Lindenstrauss Lemma", FOCS 2017 — [ARXIV-1609.02094](https://arxiv.org/abs/1609.02094)

## Key takeaways

*Unread. From the result as it is standardly stated, to be checked against the text.*

- **Tight.** There are point sets of size n in ℓ₂ for which any map into
  ℓ₂ᵐ keeping distances within 1 ± ε needs m = Ω(ε⁻² log n), whenever
  ε is not too small relative to n and d.
- **Not only linear maps.** The bound covers arbitrary embeddings, so no
  cleverer nonlinear map beats a random projection on worst-case inputs.

## Standing in the record

Filed on 2026-10-14 with [LIT-tmp7skui](LIT-tmp7skui.md) for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md). It is what
makes ε⁻² log n a threshold rather than an upper bound. That is the
quantity the question compares with the thresholds of compressed sensing
and random features.
