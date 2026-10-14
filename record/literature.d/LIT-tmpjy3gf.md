---
status: Deferred
status_note: 'unread, registered 2026-10-14 for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md) from Crossref metadata and the standard statement of its result. No attempt to read it is recorded.'
title: 'An elementary proof of a theorem of Johnson and Lindenstrauss'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Filed, not read, at the owner's request after a survey found the record
    meets random projections from three directions without holding the
    result they share. Citation checked against Crossref on 2026-10-14. Not held in the Anthology of the SOTA: a grep of its record/ (clone at commit d1573d2) for the title, the identifier and the result's name found nothing.
tags:
- mathematics
date: '2026-10-14'
published: '2002-11-25'
doi: '10.1002/rsa.10073'
first_author: 'Dasgupta'
keywords:
- 'Johnson-Lindenstrauss lemma'
- 'random projection'
- 'Gaussian random matrix'
- 'concentration'
extends:
- LIT-tmp7skui
implementations: []
summary: >-
  Dasgupta & Gupta (2003), *Random Structures & Algorithms* 22(1): 60–65. A short proof of the Johnson–Lindenstrauss lemma from moment-generating-function bounds on a χ² variable, giving k ≥ 4(ε²/2 − ε³/3)⁻¹ ln n. Unread.
---

# LIT-tmpjy3gf: An elementary proof of a theorem of Johnson and Lindenstrauss

Sanjoy Dasgupta and Anupam Gupta (2003), "An elementary proof of a theorem of Johnson and Lindenstrauss", *Random Structures & Algorithms* 22(1): 60–65 — [doi:10.1002/rsa.10073](https://doi.org/10.1002/rsa.10073)

## Key takeaways

*Unread. From the result as it is standardly stated, to be checked against the text.*

- **Elementary.** The proof needs only the length of a random unit vector's
  projection onto k coordinates, bounded by Chernoff-style estimates on a
  χ²-type variable; no measure concentration on the sphere is cited.
- **Explicit constant.** k ≥ 4(ε²/2 − ε³/3)⁻¹ ln n suffices, and the map
  succeeds with probability at least 1/n, so repeating finds one quickly.

## Standing in the record

Filed on 2026-10-14 with [LIT-tmp7skui](LIT-tmp7skui.md) for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md). It is the
version of the proof most later work quotes, and its concentration step is
the one Baraniuk et al. ([LIT-tmpcfdvm](LIT-tmpcfdvm.md)) turn into the restricted isometry
property.
