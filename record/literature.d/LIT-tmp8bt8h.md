---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpp785f](../notes.d/NOTE-tmpp785f.md)); worth reading as the paper that replaces causal orders by "spaces of input histories": finite, join-prime sets of partial functions from events to inputs, each history being data on which the output at its tip event may depend. Order-induced spaces are a special case, and input-dependent (dynamical) causal constraints, such as a switch where one party''s input fixes the order of the other two, are first-class. Spaces form a lattice under inclusion of their extended histories; causal completeness (one tip event per history) recovers definite order; causal switch spaces are exactly the maximal complete spaces. On 3 events with binary inputs there are 2644 causally complete spaces in 102 symmetry classes, of which order-induced spaces account for 19; most are non-tight. It is the first of the three papers that supersede [LIT-tmpg68lt](LIT-tmpg68lt.md), and its spaces replace that paper''s defective "locale of inputs".'
title: 'The Combinatorics of Causality'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read on 2026-10-09 (NOTE-tmpp785f) from the arXiv v4 PDF (27 July
    2023, 65 pages), extracted with pdftotext: Sections 1–3.7 in full,
    with the proofs of Propositions 2.2, 2.4, 3.21, 3.23 and 3.24 and
    Theorems 3.34 and 3.37 followed; the other proofs in 3.8 were not
    read. The Hasse diagrams are images and were followed from the prose
    and captions. Details checked against the arXiv abstract pages: v1
    submitted 17 June 2022 as "The Topology and Geometry of Causality"
    (394 pages), split at v3 (17 March 2023); the current title is from
    v3. No journal reference is given on arXiv. `published:` is the v1
    date, the first appearance of the work under this identifier. Not
    held in the Anthology of the SOTA: a grep of its record/ (clone of
    2026-10-09, commit d8b5ba5) for the authors, the three arXiv
    identifiers and the titles found nothing. Filed as the successor of
    LIT-tmpg68lt, which its authors withdrew in favour of this
    identifier. The vocabulary has no word for causal structure; see
    "Standing in the record".
tags:
- causality
- quantum-foundations
- mathematics
date: '2026-10-09'
published: '2022-06-17'
arxiv: '2206.08911'
first_author: 'Gogioso'
keywords:
- 'causal order'
- 'indefinite causal order'
- 'dynamical causal order'
- 'spaces of input histories'
- 'causal completeness'
- 'quantum switch'
implementations: []
summary: >-
  Gogioso & Pinzani (2022–23), arXiv 2206.08911 (v1 "The Topology and
  Geometry of Causality"). Generalises causal orders to spaces of input
  histories, sets of partial input assignments on which outputs may
  depend, so that causal constraints can depend on inputs. Defines
  causal completeness, tightness and sequential, parallel and
  conditional composition; proves the maximal complete spaces are the
  causal switch spaces; and counts 2644 causally complete spaces on 3
  binary-input events (19 from definite orders), with about a billion
  estimated on 4.
---

<!-- inactive-ok-file: LIT-tmpg68lt — Superseded; the withdrawn paper this one replaces, named for the lineage -->

# LIT-tmp8bt8h: The Combinatorics of Causality

Stefano Gogioso and Nicola Pinzani (2022; current version 2023), arXiv
2206.08911, Part 1 of a trilogy whose Parts 2 and 3 are [LIT-tmpc7lcl](LIT-tmpc7lcl.md) and
[LIT-tmp0y2pj](LIT-tmp0y2pj.md)

## Key takeaways

- **Causal orders and their lowersets.** A causal order is a finite
  preorder; definite ones are partial orders. What matters operationally
  is the lattice of lowersets Λ(Ω). Ω ≤ Ω′ iff Λ(Ω) ⊇ Λ(Ω′)
  (Proposition 2.2), and Λ(Ω) ∩ Λ(Ω′) = Λ(Ω ∨ Ω′) (Proposition 2.4). But
  Λ(Ω) ∪ Λ(Ω′) need not be a lattice, so satisfying two orders' constraints
  is not satisfying their meet's.
- **Spaces of input histories.** The input histories of an order are the
  input assignments on the causal past of each event (Definition 3.5). In
  general, a space is any finite join-prime set Θ of partial functions
  (Definitions 3.7–3.8), and its extended histories Ext(Θ) are the
  compatible joins. Spaces are ordered by Θ′ ≤ Θ iff Ext(Θ′) ⊇ Ext(Θ)
  (refinement means more constraints) and form lattices (Proposition 3.10).
  Order-induced spaces are closed under join, not under meet
  (Propositions 3.11–3.12).
- **Free choice, tips and completeness.** The free-choice condition says
  every joint input arises by stitching histories together. A tip event of
  a history is an event not covered by any history below it. A space is
  causally complete if every history has exactly one tip. An order-induced
  space is complete iff the order is definite (Proposition 3.21), and
  completeness has a one-step deletion test (Theorem 3.37).
- **Composition and switches.** Parallel, sequential and conditional
  sequential composition are defined. The last lets one event's input
  choose what comes next, as in the 3-party causal switch. All three
  preserve completeness and free choice under stated conditions
  (Propositions 3.13–3.24). The spaces with Θ = Ext(Θ) and single tips are
  exactly the recursively built causal switch spaces (Theorem 3.34,
  Corollary 3.35), and these are exactly the maxima of the complete
  spaces (Theorem 3.36). Their number grows more than doubly
  exponentially.
- **Tightness.** A space is tight if under every extended history each
  event is the tip of a unique history (Definition 3.16). Order-induced
  spaces are tight (Proposition 3.32). A meet of two order-induced spaces
  is tight iff every event's two causal pasts are nested (Theorem 3.33).
  58 of the 102 symmetry classes on 3 events are non-tight.
- **The census.** On 3 events with binary inputs there are 2644 causally
  complete spaces in 102 classes under event and input permutation. 13
  classes admit no fixed definite order. After 106 days of search on 4
  events, 869,529,223 spaces in 2,312,000 classes had been found, and a
  fitted curve projects about a billion. For comparison, earlier work used
  25 of the 3-event spaces: 19 order-induced and 6 more for indefinite
  causality.

## Standing in the record

Filed on 2026-10-09 from the manuscript bibliography of 2026-10-09 (work
`what-survives-translation`) at the owner's request. The manuscript
considered Gogioso and Pinzani 2021 ([LIT-tmpg68lt](LIT-tmpg68lt.md)), which its authors
withdrew in April 2024. The withdrawal names this paper (as
arXiv:2206.08911v4), *The Topology of Causality* and *The Geometry of
Causality* as superseding it. All three are filed, and [LIT-tmpg68lt](LIT-tmpg68lt.md) is
Superseded by them, this one first. See the curation entry of that day.

Read on 2026-10-09 ([NOTE-tmpp785f](../notes.d/NOTE-tmpp785f.md)). This paper is the combinatorial
groundwork. It defines the spaces that replace [LIT-tmpg68lt](LIT-tmpg68lt.md)'s Definition 3,
the "locale of inputs", which the authors' withdrawal says "is not fit for
purpose". The sheaf of causal functions over these spaces is in
[LIT-tmpc7lcl](LIT-tmpc7lcl.md), and the polytopes of empirical models in [LIT-tmp0y2pj](LIT-tmp0y2pj.md).

**The vocabulary has no word for causal structure or causal order.** The
paper is about the combinatorics of causal constraints between events,
motivated by quantum indefinite causality. It is tagged `quantum-foundations`
first, for that motivation, and `mathematics` for its content. Neither says
what it is about. A topic for causal structure would be added by decision,
and the trilogy and [LIT-tmpg68lt](LIT-tmpg68lt.md) would take it.
