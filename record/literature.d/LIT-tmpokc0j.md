---
status: Deferred
status_note: 'unread, registered 2026-10-14 for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md) from Crossref metadata and the standard statement of its result. No attempt to read it is recorded.'
title: 'A neural algorithm for a fundamental computing problem'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Filed, not read, at the owner's request after a survey found the record
    meets random projections from three directions without holding the
    result they share. Citation checked against Crossref on 2026-10-14. Not held in the Anthology of the SOTA: a grep of its record/ (clone at commit d1573d2) for the title, the identifier and the result's name found nothing.
tags:
- neuroscience
- information-retrieval
date: '2026-10-14'
published: '2017-11-10'
doi: '10.1126/science.aam9868'
first_author: 'Dasgupta'
keywords:
- 'fruit fly olfaction'
- 'mushroom body'
- 'Kenyon cells'
- 'locality-sensitive hashing'
- 'similarity search'
- 'random projection'
- 'winner-take-all'
implementations: []
summary: >-
  Dasgupta, Stevens & Navlakha (2017), *Science* 358(6364): 793–796. The fly olfactory circuit assigns an odour a tag by a sparse binary random projection from about 50 glomeruli to about 2,000 Kenyon cells, then keeps the top 5% by winner-take-all. Read as locality-sensitive hashing, this beats standard LSH on nearest-neighbour search benchmarks. Unread.
---

# LIT-tmpokc0j: A neural algorithm for a fundamental computing problem

Sanjoy Dasgupta, Charles F. Stevens and Saket Navlakha (2017), "A neural algorithm for a fundamental computing problem", *Science* 358(6364): 793–796 — [doi:10.1126/science.aam9868](https://doi.org/10.1126/science.aam9868)

## Key takeaways

*Unread. From the result as it is standardly stated, to be checked against the text.*

- **Three steps.** Projection neuron responses are mean-centred, then sent
  by a sparse binary random matrix (each Kenyon cell samples about six
  glomeruli) into a space about 40 times larger, then sparsified by
  winner-take-all inhibition to the top 5% of Kenyon cells.
- **It expands rather than reduces.** Unlike the Johnson–Lindenstrauss
  setting, the random projection goes up in dimension, and sparsification
  does the work that dimension reduction does in standard LSH.
- **A similarity-preserving hash.** Similar odours get overlapping tags. On
  SIFT, GIST and MNIST nearest-neighbour search the fly's scheme beats
  random-projection LSH at the same tag length.

## Standing in the record

Filed on 2026-10-14 for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md). The record mentions random
projections into the mushroom body twice in passing ([NOTE-670](../notes.d/NOTE-670.md), [NOTE-165](../notes.d/NOTE-165.md)),
and neither note cites this paper. This is the paper that makes the circuit
an algorithm. Its circuit is also very close to the neuron view of sparse
distributed memory ([NOTE-242](../notes.d/NOTE-242.md), [NOTE-779](../notes.d/NOTE-779.md)). `neuroscience` comes first
because the subject is a circuit; `information-retrieval` is for the
nearest-neighbour search it is evaluated on.
