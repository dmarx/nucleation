---
status: Deferred
status_note: >-
  filed 2026-10-15, not read. Registered at the owner's request for [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md),
  as the survey's pointer for the precomputed-answer case the four works already
  read leave out. A reading is in progress.
title: Implementing data cubes efficiently
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: 'Filed, not read. Citation checked against Crossref on 2026-10-15: SIGMOD
    ''96, pp. 205–216; Crossref gives 1996 only. The conference ran 4–6 June 1996,
    and `published:` uses its first day. Not held in the Anthology of the SOTA:
    a grep of its record/ (clone of 2026-10-15, commit d1573d2) for the title found
    nothing.'
tags:
- databases
- operations-research
date: '2026-10-15'
published: '1996-06-04'
doi: 10.1145/233269.233333
first_author: Harinarayan
keywords: []
implementations: []
summary: >-
  Harinarayan, Rajaraman and Ullman (1996), SIGMOD '96. Registered for [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md)
  as the standard source on choosing which aggregate answers to precompute and store
  under a space budget, with a greedy algorithm and a guarantee on how close it
  comes to the best choice.
---

# LIT-tmptn63k: Implementing data cubes efficiently

Harinarayan, V., Rajaraman, A. and Ullman, J. D. (1996). Implementing data cubes efficiently. In *Proceedings of the 1996 ACM SIGMOD International Conference on Management of Data*, pp. 205–216. DOI 10.1145/233269.233333

## Key takeaways

Not read yet.

## Why this is here

[QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md): the four works on physical design already read choose ways of reaching stored data. None covers a precomputed answer, which is the cockpit's case (speeds computed before landing and left as bugs). This paper chooses which answers to precompute.
