---
status: Active
status_note: 'skimmed 2026-10-09 ([NOTE-tmp0fe8y](../notes.d/NOTE-tmp0fe8y.md)): the preface and Chapter 1 read closely, Chapter 3''s opening and its section on adjunctions and data migration read closely, the openings and summaries of Chapters 2 and 4–7 read; Chapters 2 and 4–7 otherwise not read. Worth reading as an introduction to applied category theory organised around compositionality: an observation of systems is a monotone map, a generative effect is its failure to preserve joins, and a monotone map out of a preorder with all joins has no generative effect exactly when it is a left adjoint. Later chapters treat resource theories, databases as functors, co-design, signal-flow graphs, circuits and temporal logic, each through a categorical structure.'
title: 'Seven Sketches in Compositionality: An Invitation to Applied Category Theory'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request from the manuscript bibliography of
    2026-10-09 and skimmed the same day (NOTE-tmp0fe8y) from arXiv v3 (12
    October 2018; front page "Last updated October 16, 2018"). Details
    checked against the arXiv API (1803.05316, Brendan Fong and David I.
    Spivak, v1 submitted 14 March 2018) and Crossref: the book appeared
    from Cambridge University Press as "An Invitation to Applied Category
    Theory: Seven Sketches in Compositionality", DOI
    10.1017/9781108668804, online 5 July 2019, print 18 July 2019 (ISBNs
    9781108482295, 9781108711821). The bibliography's "2019" is that
    edition; the title here is the arXiv one, and `published:` is the
    arXiv v1 date (ADR-002). Not held in the Anthology of the SOTA: a grep
    of its record/ (clone of 2026-10-09, commit d8b5ba5) for the title,
    the identifier and the authors found only a passing mention of
    "Fong-Spivak" among related work in ANTH-NOTE-355.
tags:
- mathematics
- compositionality
date: '2026-10-09'
published: '2018-03-14'
arxiv: '1803.05316'
first_author: 'Fong'
keywords:
- 'applied category theory'
- 'compositionality'
- 'Galois connections'
- 'generative effects'
- 'monoidal categories'
- 'enrichment'
- 'functorial data migration'
- 'profunctors'
- 'props'
- 'hypergraph categories'
- 'toposes'
implementations: []
summary: >-
  Fong & Spivak (2018; Cambridge University Press 2019), [ARXIV-1803.05316](https://arxiv.org/abs/1803.05316).
  A textbook invitation to applied category theory in seven chapters, each
  pairing an application with a structure: generative effects with orders
  and Galois connections, resources with monoidal preorders and
  enrichment, databases with functors and adjunctions, co-design with
  profunctors, signal-flow graphs with props, circuits with hypergraph
  categories and operads, behaviour with sheaves and toposes. Its first
  chapter defines a generative effect as an observation that preserves
  order but not joins, and shows that such maps are exactly the
  non-left-adjoints.
---

<!-- inactive-ok-file: LIT-344 — Deferred; no lawful full text, named as the related monograph, not leaned on -->

# LIT-tmp8x9r8: Seven Sketches in Compositionality: An Invitation to Applied Category Theory

Brendan Fong, David I. Spivak (arXiv 2018; Cambridge University Press 2019,
as *An Invitation to Applied Category Theory: Seven Sketches in
Compositionality*) — [ARXIV-1803.05316](https://arxiv.org/abs/1803.05316), DOI-10.1017/9781108668804

## Key takeaways

From the parts read (see [NOTE-tmp0fe8y](../notes.d/NOTE-tmp0fe8y.md) for exactly which):

- **Observation as a monotone map, and generative effects.** Following
  Adam's thesis, an observation of a system is a monotone map Φ : P → Q
  between preorders. It always satisfies Φ(a) ∨ Φ(b) ≤ Φ(a ∨ b); a
  generative effect is a case where the inequality is strict: observing the
  joined system shows something the joined observations do not. The worked
  example is connectivity of partitions of a three-point set, observed by
  "is • connected to ∗?".
- **Left adjoints are exactly the maps without generative effects.** Left
  adjoints preserve all joins and right adjoints all meets
  (Proposition 1.111); if P has all joins, a monotone map out of P preserves
  joins iff it is a left adjoint (Theorem 1.115). Adam's generative
  observations are those that preserve meets but not joins.
- **Galois connections, closure and level shifting.** f ⊣ g iff
  p ≤ g(f(p)) and f(g(q)) ≤ q; g∘f is a closure operator, and every closure
  operator comes from an adjunction with its fixed points. Each function
  g : S → T induces an adjunction between partitions, and each f : A → B
  the triple f! ⊣ f* ⊣ f∗ on subsets (image, preimage, "all in").
- **Databases as functors.** A schema is a category, an instance a functor
  to Set, and a schema map F induces the migrations Δ_F with adjoints
  Σ_F ⊣ Δ_F ⊣ Π_F (union-like and join-like); for F : C → 1, Σ gives
  connected components and Π a selection.
- **The book's stance on coherence.** The authors call the choice of
  coherence conditions "more science than mathematics": accepted when they
  yield widely applicable, strongly compositional structures.

## Standing in the record

Filed on 2026-10-09 at the owner's request, from the manuscript
bibliography of 2026-10-09 (work `what-survives-translation`): one of the
works the manuscript considered and dropped from its final reference list.

Skimmed on 2026-10-09 ([NOTE-tmp0fe8y](../notes.d/NOTE-tmp0fe8y.md)): the chapters closest to its
opening aim, orders and adjunctions as the basis of compositional
modelling, were read closely, and the rest only at their openings and
summaries. It is an introduction, not a source for results, which are
standard; a deeper reading would take Chapters 2 and 4 (resource theories
and monoidal categories) and Chapter 7 (sheaves and toposes). Its
Galois-connection material is the order theory underlying Ganter and
Wille's concept lattices ([LIT-344](LIT-344.md)), which the book does not mention.
