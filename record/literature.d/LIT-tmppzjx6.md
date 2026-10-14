---
status: Deferred
status_note: 'unread, registered 2026-10-14 for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md) from Crossref metadata and the standard statement of its result. No attempt to read it is recorded.'
title: 'Database-friendly random projections: Johnson-Lindenstrauss with binary coins'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Filed, not read, at the owner's request after a survey found the record
    meets random projections from three directions without holding the
    result they share. Citation checked against Crossref on 2026-10-14. Not held in the Anthology of the SOTA: a grep of its record/ (clone at commit d1573d2) for the title, the identifier and the result's name found nothing. Crossref gives June 2003 and no day, so `published:` is the first of the month; an earlier version appeared at PODS 2001.
tags:
- mathematics
date: '2026-10-14'
published: '2003-06-01'
doi: '10.1016/S0022-0000(03)00025-4'
first_author: 'Achlioptas'
keywords:
- 'random projection'
- 'Johnson-Lindenstrauss'
- 'sparse projection'
- 'binary coins'
- 'databases'
extends:
- LIT-tmp7skui
implementations: []
summary: >-
  Achlioptas (2003), *Journal of Computer and System Sciences* 66(4): 671–687. The Johnson–Lindenstrauss guarantee holds, with no loss in dimension, when the projection's entries are ±1 at random, or are 0 with probability 2/3 and ±√3 otherwise. Unread.
---

# LIT-tmppzjx6: Database-friendly random projections: Johnson-Lindenstrauss with binary coins

Dimitris Achlioptas (2003), "Database-friendly random projections: Johnson-Lindenstrauss with binary coins", *Journal of Computer and System Sciences* 66(4): 671–687 — [doi:10.1016/S0022-0000(03)00025-4](https://doi.org/10.1016/S0022-0000(03)00025-4)

## Key takeaways

*Unread. From the result as it is standardly stated, to be checked against the text.*

- **No Gaussians needed.** Entries drawn uniformly from {−1, +1}, or
  from {−√3, 0, +√3} with probabilities 1/6, 2/3, 1/6, give the same
  guarantee as a Gaussian matrix, with k₀ = (4 + 2β)/(ε²/2 − ε³/3) · log n
  for success with probability 1 − n^−β.
- **Sparse is enough.** The second distribution zeroes two thirds of the
  matrix, so the projection costs a third of the additions.

## Standing in the record

Filed on 2026-10-14 with [LIT-tmp7skui](LIT-tmp7skui.md) for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md). It is the
step from a rotation to a sparse random matrix of small integers, which is
the form random projections take in the fly olfactory circuit ([LIT-tmpokc0j](LIT-tmpokc0j.md))
and in sparse distributed memory ([NOTE-242](../notes.d/NOTE-242.md)), so it bears on whether
those are the same object as the lemma.
