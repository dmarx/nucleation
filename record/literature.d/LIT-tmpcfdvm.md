---
status: Deferred
status_note: 'unread, registered 2026-10-14 for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md) from Crossref metadata and the standard statement of its result. No attempt to read it is recorded.'
title: 'A Simple Proof of the Restricted Isometry Property for Random Matrices'
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
published: '2008-01-15'
doi: '10.1007/s00365-007-9003-x'
first_author: 'Baraniuk'
keywords:
- 'restricted isometry property'
- 'compressed sensing'
- 'Johnson-Lindenstrauss lemma'
- 'random matrices'
- 'concentration of measure'
extends:
- LIT-tmp7skui
implementations: []
summary: >-
  Baraniuk, Davenport, DeVore & Wakin (2008), *Constructive Approximation* 28(3): 253–263. Any random matrix family whose norms concentrate as in the Johnson–Lindenstrauss lemma has the restricted isometry property of order k with high probability once m = O(k log(n/k)), via a covering of the k-sparse vectors. Unread.
---

# LIT-tmpcfdvm: A Simple Proof of the Restricted Isometry Property for Random Matrices

Richard Baraniuk, Mark Davenport, Ronald DeVore and Michael Wakin (2008), "A Simple Proof of the Restricted Isometry Property for Random Matrices", *Constructive Approximation* 28(3): 253–263 — [doi:10.1007/s00365-007-9003-x](https://doi.org/10.1007/s00365-007-9003-x)

## Key takeaways

*Unread. From the result as it is standardly stated, to be checked against the text.*

- **JL implies RIP.** If ‖Φx‖² concentrates around ‖x‖² for each fixed x
  with the tail used in JL proofs, then a union bound over a net of each
  k-dimensional coordinate subspace, and over all such subspaces, gives
  the restricted isometry property of order k.
- **The cost is k log(n/k).** The count of k-sparse supports replaces the
  count of point pairs, so the number of measurements is O(k log(n/k)).
- **The same matrices.** Gaussian, ±1 and Achlioptas's sparse ensembles all
  qualify, and the RIP comes with a JL embedding for free.

## Standing in the record

Filed on 2026-10-14 for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md) as the bridge between two of
its threads. The compressed-sensing bound that Toy Models of Superposition
proves in its appendix ([NOTE-278](../notes.d/NOTE-278.md)) assumes the restricted isometry property.
This paper derives that property from the same concentration as the
Johnson–Lindenstrauss lemma ([LIT-tmp7skui](LIT-tmp7skui.md), [LIT-tmpjy3gf](LIT-tmpjy3gf.md)). So if this proof is
right, the superposition bound and the lemma share their mechanism.
