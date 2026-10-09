---
status: Active
status_note: 'read in full 2026-10-09 ([NOTE-tmp6dxz0](../notes.d/NOTE-tmp6dxz0.md)); worth reading as the paper that makes simulation between empirical models adaptive and shows it is the same thing as convertibility by free operations. Measurement protocols (decision trees of compatible measurements) form a comonad MP on scenarios and on empirical models; a simulation of e by d is a deterministic map MP(d ⊗ c) → e with c non-contextual. Such a simulation exists exactly when e is obtained from d by a term in the free operations (relabelling and translation of measurements, coarse-graining, mixing, choice, tensor, and the new conditional measurement), with an equational theory and normal forms. Along any simulation the non-contextual fraction cannot fall, and no contextual model can be cloned.'
title: 'A comonadic view of simulation and quantum resources'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's direct request on 2026-10-09 and read in full the
    same day (NOTE-tmp6dxz0) from the arXiv PDF (1904.10035v1, the only
    version, 12 pages, text layer extracted). Bibliography checked
    against the arXiv abstract page (v1 submitted 22 April 2019; journal
    reference LiCS 2019) and Crossref (DOI 10.1109/LICS.2019.8785677,
    2019 34th Annual ACM/IEEE Symposium on Logic in Computer Science,
    pp. 1–12, published June 2019; authors Samson Abramsky, Rui Soares
    Barbosa, Martti Karvonen, Shane Mansfield). The IEEE version was not
    consulted. `published:` is the arXiv v1 date by ADR-002. Not held in
    the Anthology of the SOTA: a grep of its record/ (clone pulled
    2026-10-09, commit d8b5ba5) for the arXiv id, the DOI, the title and
    Karvonen found nothing.
tags:
- contextuality
- mathematics
- quantum-foundations
date: '2026-10-09'
published: '2019-04-22'
arxiv: '1904.10035'
first_author: 'Abramsky'
keywords:
- 'simulation'
- 'resource theory of contextuality'
- 'free operations'
- 'measurement protocols'
- 'comonad'
- 'co-Kleisli category'
- 'contextual fraction'
- 'no-cloning'
implementations: []
summary: >-
  Abramsky, Barbosa, Karvonen & Mansfield (2019), [ARXIV-1904.10035](https://arxiv.org/abs/1904.10035), LICS
  2019. Measurement protocols form a comonad on empirical models; a
  simulation of e by d is a co-Kleisli map from d ⊗ c (c non-contextual)
  to e. Simulability coincides with convertibility by a term in the free
  operations of the resource theory of contextuality, including a new
  conditional measurement; the non-contextual fraction is monotone, and
  contextual models cannot be cloned.
extends:
- LIT-tmpes6yu
- LIT-265
- LIT-016
extended_by:
- LIT-tmp5at9s
---

<!-- inactive-ok-file: THEORY-tmprxblg — Proposed; the theory this reading is a source of, cited as such -->

# LIT-tmpjk0t0: A comonadic view of simulation and quantum resources

Samson Abramsky, Rui Soares Barbosa, Martti Karvonen and Shane Mansfield
(2019), in *2019 34th Annual ACM/IEEE Symposium on Logic in Computer
Science (LICS)*, pp. 1–12, DOI 10.1109/LICS.2019.8785677 —
[ARXIV-1904.10035](https://arxiv.org/abs/1904.10035)

## Key takeaways

- **Free operations, with one new.** The operations that build one
  empirical model from others without contextual resources (§III-A):
  the zero and singleton models, translation of measurements along a
  simplicial map (which may change the cover), coarse-graining of
  outcomes, probabilistic mixing, controlled choice (&), tensor product
  (⊗), and the new conditional measurement x?y (measure x, then choose
  the next measurement from the outcome). CF is monotone for each
  (Proposition 7); closed terms are exactly the non-contextual models
  (Proposition 8).
- **An equational theory with normal forms.** Equations (1)–(28) are
  sound up to isomorphism of models (Proposition 10); every term
  rewrites to a mixture of terms of the form (f* (base ⊗ … )[x?y]…)/h
  (Proposition 11). Completeness is open.
- **Measurement protocols as a comonad.** Protocols are prefix-closed
  sets of runs (Definition 14); MP(X) is the scenario of all protocols
  over X, MP(e) the induced model, and MP is a comonoidal comonad on
  scenarios and on empirical models (Theorem 17). A simulation of e by d
  is a deterministic morphism MP(d ⊗ c) → e for some non-contextual c
  (Definition 18): adaptive, with shared classical randomness.
- **Simulation equals free convertibility** (Theorem 20): d simulates e
  iff e ≅ t[d/v] for a typed term t in the free operations. Hence
  NCF(d) ≤ NCF(e) (Theorem 21) and no-cloning: e simulates e ⊗ e iff e is
  non-contextual (Theorem 22).
- **Examples drawn from the literature.** Barrett and Pironio's
  simulation of any two-output bipartite box by PR boxes, and their
  five-partite quantum box that no number of PR boxes simulates, are
  instances (Example 19).

## Standing in the record

Filed on 2026-10-09 at the owner's direct request, as the second of the
works on simulations between empirical models, following Karvonen's
Categories of Empirical Models ([LIT-tmpes6yu](LIT-tmpes6yu.md)). It is not from the
manuscript bibliography: the owner asked for it directly on 2026-10-09.
It is a source of [THEORY-tmprxblg](../theory.d/THEORY-tmprxblg.md). [NOTE-tmp6dxz0](../notes.d/NOTE-tmp6dxz0.md) says how it bears on
the manuscript's transport problem on line `pragmatic-transport`.
