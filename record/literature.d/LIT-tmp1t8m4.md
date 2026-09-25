---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-25; not read in full
title: 'A type theory for synthetic ∞-categories'
version: 1
tags:
- mathematics
date: '2026-09-25'
published: '2017-05-21'
arxiv: '1705.07442'
doi: '10.21136/hs.2017.06'
first_author: 'Riehl'
keywords:
- 'homotopy type theory'
- '(∞'
- '1)-categories'
- 'Segal types'
- 'Rezk types'
- 'directed interval'
- 'extension types'
- 'type theory with shapes'
- 'dependent Yoneda lemma'
implementations: []
summary: >-
  Riehl et al. (2017), [ARXIV-1705.07442](https://arxiv.org/abs/1705.07442). Adding a directed interval 2 and a separate "shape" layer (the coherent theory of a strict interval) to homotopy type theory yields a synthetic theory of (∞,1)-categories. Segal types, where binary composites are unique up to homotopy, automatically get coherent associativity and unitality, and a dependent Yoneda lemma holds for covariant families. The model is bisimplicial sets, where Segal and Rezk types are (complete) Segal spaces.
---

# LIT-tmp1t8m4: A type theory for synthetic ∞-categories

Emily Riehl, Michael Shulman (2017), *Higher Structures 1(1):147–224 (2017); arXiv preprint first* — [ARXIV-1705.07442](https://arxiv.org/abs/1705.07442)

## Key takeaways

- Adding a directed interval 2 and a separate "shape" layer (the coherent theory of a strict interval) to homotopy type theory yields a synthetic theory of (∞,1)-categories. Segal types, where binary composites are unique up to homotopy, automatically get coherent associativity and unitality, and a dependent Yoneda lemma holds for covariant families. The model is bisimplicial sets, where Segal and Rezk types are (complete) Segal spaces.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

The authors propose foundations for synthetic (∞,1)-category theory inside homotopy type theory. They axiomatize a directed interval type, build higher simplices from it, and use these to probe the categorical structure of any type. Segal types have homotopically unique binary composites, which is enough for coherent associativity and unitality in all dimensions. Rezk types additionally identify categorical isomorphisms with type-theoretic identities, a local univalence. Covariant fibrations vary functorially over Segal types and satisfy a dependent Yoneda lemma, a directed analogue of identity elimination. Having an adjoint is shown to be a mere proposition for functors between Rezk types. To manage the bookkeeping, the paper uses a three-layer type theory with shapes (polytopes in directed cubes) and extension types generalising cubical path types. An appendix gives semantics in the Reedy model structure on bisimplicial sets.

## Standing in the record

Filed from the survey of 2026-09-25 of work the anthology set aside as out of scope (tier C): 570 seconds of active reading over 2 sessions in the papers-feed tracker. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: medium — It has the highest owner time in the maths half (t=570, n=2) and is the foundational paper for directed HoTT. The skim captures the architecture but none of the proofs.**

What a deeper reading should check:

- It is directly paired with c26 (nLab, two-level type theory). This paper names 2LTT as the alternative it rejects, and the nLab page lists "type theory with shapes" under See also. A reading should file them together.
- Later developments to check include the Rzk proof assistant, which implements this simplicial type theory, and the follow-up synthetic ∞-category work. The v5 correction to the proof of 8.13 is noted on the arXiv page.

Access when seeded: arXiv abs page (v1 21 May 2017 through v5 8 Jun 2023; v4 is the final journal version) and full PDF of v5 (78 pp.) read directly: abstract, table of contents, §1 introduction including Remark 1.1 and the section roadmap. The arXiv page lists no DOI. I found the journal record by a Crossref bibliographic search: Higher Structures 1:147–224, issued 2017-12-22, DOI 10.21136/hs.2017.06. That DOI string is taken from Crossref and I did not resolve it.
