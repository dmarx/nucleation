---
status: Active
status_note: >-
  read in full 2026-10-27 (NOTE-tmpigjto), from arXiv v6; worth reading as
  the theorem that black-boxing passive linear circuits is functorial: the
  Lagrangian relation a circuit imposes on its terminals' potentials and
  currents composes as the circuits do. It is also a clean account of
  eliminating an interior by minimum power, and of why that elimination
  alone has no identities. Its scope is narrow: passive, linear,
  two-terminal components, time only through the Laplace transform with
  zero initial conditions.
title: 'A Compositional Framework for Passive Linear Networks'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read. Checked against the arXiv API on 2026-10-27: John
    C. Baez and Brendan Fong, arXiv 1504.05625, v1 submitted 22 April
    2015, which is `published:` per ADR-002; published in Theory and
    Applications of Categories 33(38), 2018, whose abstract page is the
    `url:` A22 gave (not fetched).
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full from arXiv 1504.05625v6 (16 November 2018), 54 pp.,
    Parts I–III, all proofs and the references; the first NOTE on the work
    (NOTE-tmpigjto). The published TAC text was not read, so its page range
    is kept from the registration unchecked. Status set from the reading:
    Active. `published:` stays at the v1 date per ADR-002; v1's date was
    not re-checked from the text, which is v6. The title agrees. The
    registration's summary was right in substance and is replaced by one
    from the text, with three additions: the functor is a hypergraph
    functor, its target is Lagrangian relations rather than Dirichlet
    forms (which form only a semicategory, Prop. 3.6), and inductors and
    capacitors enter only through the Laplace transform with zero initial
    conditions. Two THEORYs are filed from it (THEORY-tmp99qi9,
    THEORY-tmpugh7c).
tags:
- compositionality
- mathematics
date: '2026-10-27'
published: '2015-04-22'
arxiv: '1504.05625'
url: 'http://www.tac.mta.ca/tac/volumes/33/38/33-38abs.html'
first_author: 'Baez'
keywords:
- 'black boxing'
- 'decorated cospans'
- 'passive linear networks'
- 'compositionality'
- 'functorial semantics'
implementations: []
summary: >-
  Baez & Fong (2018), TAC 33. Open circuits of passive linear two-terminal
  components (resistors, and inductors and capacitors through the Laplace
  transform over ℝ(s)) are morphisms of a hypergraph category Circ built
  from decorated cospans, composed by gluing terminals. The black box
  functor Circ → LagRel, a hypergraph functor (Thm 1.1, Thm 7.7), sends a
  circuit to the Lagrangian relation between its terminals' potentials and
  currents, the graph of the differential of the power functional left
  when the interior is eliminated by the principle of minimum power. The
  external behaviour of a composite is the composite of the parts'
  behaviours. Dirichlet forms alone compose by that elimination but lack
  identities, since an ideal wire has none.
---
<!-- inactive-ok-file: CLAIM-tmpmand1 — Proposed; the claim it was filed for, cited as open -->

# LIT-tmpdkjum: A Compositional Framework for Passive Linear Networks

Baez, J. C., & Fong, B. (2018). A compositional framework for passive linear networks. *Theory and Applications of Categories*, 33(38), 1158–1222. arXiv:1504.05625.

Read in full on 2026-10-27 (NOTE-tmpigjto).

## Why this is here

A23 §IV cited it as "a rigorous theory of precisely this phenomenon":
composed interactions yield an effective boundary behavior that
constrains further interaction, the composition [CLAIM-tmpose3y](../claims.d/CLAIM-tmpose3y.md)
demonstrates in its simplest case. It bears on [CLAIM-tmpose3y](../claims.d/CLAIM-tmpose3y.md) and
[CLAIM-tmpmand1](../claims.d/CLAIM-tmpmand1.md).
