---
status: Active
status_note: 'skimmed 2026-10-09 ([NOTE-tmpht8fg](../notes.d/NOTE-tmpht8fg.md)); worth reading as the geometric half of the trilogy and the successor of the withdrawn [LIT-tmpg68lt](LIT-tmpg68lt.md)''s polytope and causal-fraction results: the empirical models on any cover of a space of input histories are exactly the points of a "causaltope", the product of simplices sliced by linear causality equations derived from the space''s topology, so supported fractions and causally separable fractions are linear programs. Causal separability is defined relative to an ambient space rather than to the indiscrete one, which lets quantum switches with entangled or contextual control witness indefinite causal order once known no-signalling constraints are imposed (and not otherwise); the causally separable fraction is bounded below by the separable local fraction, and in the switch examples it tracks, and sometimes equals, the local fraction ("contextual causality"). The BFW model is 0% supported by every causally complete 3-event space and 100% by each of three indefinite orders. Read in part: introduction, causaltopes, standard causal separability and the examples.'
title: 'The Geometry of Causality'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Skimmed on 2026-10-09 (NOTE-tmpht8fg) from the arXiv v2 PDF (27
    July 2023, 86 pages), extracted with pdftotext: Section 1, Sections
    2.3–2.4 and the BFW and quantum-switch examples (2.6.6, 2.7) read;
    2.1–2.2, 2.5, 2.6.1–2.6.5, 2.8 and 2.9 skimmed for their statements;
    proofs (2.10) not read. Details checked against the arXiv abstract
    page: v1 submitted 16 March 2023, v2 27 July 2023, "Originally Part 3
    of arXiv:2206.08911v2, now extended and published as a stand-alone
    paper"; no journal reference. `published:` is the v1 date. Not held
    in the Anthology of the SOTA: a grep of its record/ (clone of
    2026-10-09, commit d8b5ba5) for the authors, the identifiers and the
    titles found nothing. Filed as a successor of LIT-tmpg68lt; the
    vocabulary has no word for causal structure.
tags:
- contextuality
- quantum-foundations
- mathematics
date: '2026-10-09'
published: '2023-03-16'
arxiv: '2303.09017'
first_author: 'Gogioso'
keywords:
- 'causal polytopes'
- 'causaltopes'
- 'causal separability'
- 'indefinite causal order'
- 'quantum switch'
- 'contextual fraction'
implementations: []
summary: >-
  Gogioso & Pinzani (2023), arXiv 2303.09017, Part 3 of the trilogy.
  Empirical models on any cover of a space of input histories are the
  points of a causaltope, a product of simplices cut by linear causality
  equations, so causal fractions are linear programs. Causal
  separability relative to a given ambient space lets entangled or
  contextually controlled quantum switches witness indefinite order once
  known no-signalling constraints are imposed, with the causally
  separable fraction bounded below by the separable local fraction.
---

<!-- inactive-ok-file: LIT-tmpg68lt — Superseded; the withdrawn paper whose polytope and causal-fraction results this one carries -->

# LIT-tmp0y2pj: The Geometry of Causality

Stefano Gogioso and Nicola Pinzani (2023), arXiv 2303.09017, Part 3 of the
trilogy after [LIT-tmp8bt8h](LIT-tmp8bt8h.md) and [LIT-tmpc7lcl](LIT-tmpc7lcl.md)

## Key takeaways

- **Causaltopes.** For a space of input histories Θ and a cover, take the
  product over contexts of simplices of distributions on output histories
  ("pseudo-empirical models", Definition 2.10). Then impose causality
  equations: for any two contexts containing a lowerset μ, their marginals
  on μ agree (Definition 2.12, with reductions in Propositions 2.21–2.22).
  The result is the causaltope (Definition 2.13). It is in convex-linear
  bijection with the empirical models of [LIT-tmpc7lcl](LIT-tmpc7lcl.md) (Theorem 2.25).
- **Hierarchy.** For spaces on the same events and inputs with the same
  maximal histories, Θ ≤ Θ′ gives Caus_std(Θ) ⊆ Caus_std(Θ′)
  (Proposition 2.26). The no-signalling polytope is the bottom and the
  indiscrete space's polytope is the whole product of simplices.
- **Causal fractions as linear programs.** The fraction of a model
  supported by a sub-space, or jointly by a family of sub-spaces, is the
  largest weight of a component in their causaltopes (Definitions
  2.14–2.15). The causally separable fraction is the fraction over the
  causal completions (Definition 2.16).
- **Relative separability.** Separability is relative to an ambient space,
  not fixed to the indiscrete space as in the causal-inequality
  literature. This is strictly finer, and it cuts the search: for a 6-party
  example, 16 known completions instead of 16,511,297,126,400 for the
  indiscrete space.
- **Contextual causality.** The causally separable fraction is at least the
  separable local fraction (Proposition 2.29). The converse is a
  conjecture (2.30). For a switch with Bell-entangled control the
  separable fraction is about 63.2% at the plotted angles, and the bound is
  not tight everywhere. For two contextually controlled classical switches
  the separable fraction is 75% and equals the local fraction of the Bell
  model controlling them. Every such example becomes causally separable if
  the no-signalling constraints to the measuring parties are dropped.
- **BFW.** The Baumeler–Feix–Wolf model is 0% supported by every causally
  complete 3-event space. It is 100% supported by each of the three
  indefinite orders in which one party acts first, and the intersection of
  those three causaltopes (38-dimensional) supports all of it.

## Standing in the record

Filed on 2026-10-09 from the manuscript bibliography of 2026-10-09 (work
`what-survives-translation`) at the owner's request, as a successor of
Gogioso and Pinzani 2021 ([LIT-tmpg68lt](LIT-tmpg68lt.md)). The withdrawn paper's
Proposition 16 (empirical models form a polytope cut by linear causality
equations) and its Section 9 (causal fractions for pre-orders, the BFW
example, with proofs deferred to a later paper) are carried and proved here.
[LIT-tmpg68lt](LIT-tmpg68lt.md) is now Superseded by the trilogy. See the curation entry of
that day.

Skimmed on 2026-10-09 ([NOTE-tmpht8fg](../notes.d/NOTE-tmpht8fg.md)). The reading covers the definitions,
the main theorem and the examples, but not the generalisation to
non-standard covers in full, nor any proofs. Its BFW result sharpens the
withdrawn paper's: there, the Ω-causal fraction was 0 for every partial
order; here, it is 0 for every causally complete space, which includes the
dynamical ones.

The vocabulary has no topic for causal structure. The paper is tagged
`contextuality` first because its examples and its central bound tie causal
separability to the contextual fraction.
