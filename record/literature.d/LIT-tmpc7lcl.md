---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmp98pr8](../notes.d/NOTE-tmp98pr8.md)); worth reading as the direct successor of the withdrawn [LIT-tmpg68lt](LIT-tmpg68lt.md)''s sheaf construction, now over spaces of input histories ([LIT-tmp8bt8h](LIT-tmp8bt8h.md)) rather than a "locale of inputs": a joint input–output function is causal when each event''s output depends only on the histories with that event as a tip, causal functions are exactly free assignments of outputs to tips (up to tip-equivalence in non-tight spaces), and an extended function is causal iff it is continuous for the lowerset topology. Causal functions form a separated presheaf that is a sheaf exactly when the space admits no "solipsistic contextuality", so tight spaces give a sheaf and some dynamical causal structures do not, letting deterministic local data fail to glue. Empirical models are compatible families of distributions over causal functions on any open cover, from the fully solipsistic to the classical; standard empirical models on causal switch spaces, total orders included, are always local. Source of [THEORY-tmpquo32](../theory.d/THEORY-tmpquo32.md).'
title: 'The Topology of Causality'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read on 2026-10-09 (NOTE-tmp98pr8) from the arXiv v2 PDF (27 July
    2023, 85 pages), extracted with pdftotext: Sections 1 and 2.1–2.5 in
    full, the Leggett–Garg and BFW examples of 2.6.4–2.6.5, and the
    reference list; the examples of 2.6.1–2.6.3 were skimmed and the
    proofs of 2.7 were not read. Details checked against the arXiv
    abstract page: v1 submitted 13 March 2023, v2 27 July 2023,
    "Originally Part 2 of arXiv:2206.08911v2, now extended and published
    as a stand-alone paper"; no journal reference. `published:` is the
    v1 date. Not held in the Anthology of the SOTA: a grep of its record/
    (clone of 2026-10-09, commit d8b5ba5) for the authors, the
    identifiers and the titles found nothing. Filed as a successor of
    LIT-tmpg68lt; the vocabulary has no word for causal structure.
tags:
- contextuality
- quantum-foundations
- mathematics
date: '2026-10-09'
published: '2023-03-13'
arxiv: '2303.07148'
first_author: 'Gogioso'
keywords:
- 'sheaf theory'
- 'contextuality'
- 'non-locality'
- 'indefinite causal order'
- 'lowerset topology'
- 'empirical models'
implementations: []
summary: >-
  Gogioso & Pinzani (2023), arXiv 2303.07148, Part 2 of the trilogy.
  Extends Abramsky–Brandenburger from no-signalling to arbitrary,
  possibly dynamical or indefinite, causal structure: causality is
  continuity in the lowerset topology, causal functions form a presheaf
  that fails to be a sheaf exactly on spaces with "solipsistic
  contextuality", empirical models live on any open cover, and standard
  empirical models on causal switch spaces (total orders included) are
  always local, so the Leggett–Garg model is local for its own total
  order.
---

<!-- inactive-ok-file: LIT-tmpg68lt — Superseded; the withdrawn paper this one replaces, named for the lineage -->
<!-- inactive-ok-file: THEORY-tmpquo32 — Proposed; the account this reading is the source of -->

# LIT-tmpc7lcl: The Topology of Causality

Stefano Gogioso and Nicola Pinzani (2023), arXiv 2303.07148, Part 2 of the
trilogy after [LIT-tmp8bt8h](LIT-tmp8bt8h.md) and before [LIT-tmp0y2pj](LIT-tmp0y2pj.md)

## Key takeaways

- **Causal functions.** A joint IO function is causal for a space Θ if,
  for every history h ∈ Θ, the outputs at h's tips are the same for all
  joint inputs extending h (Definition 2.2). For order-induced spaces this
  is the familiar F(k)_ω = G_ω(k|_{ω↓}) (Proposition 2.1). For a switch
  space it is not a fixed dependency pattern. Causal functions are
  equivalently free maps from histories to outputs at their tips, with
  outputs at an event identified across tip-equivalent histories when the
  space is not tight (Definitions 2.3, 2.7, 2.13; Theorems 2.3, 2.14;
  Propositions 2.4, 2.16).
- **Inseparable functions.** On causally incomplete spaces some causal
  functions arise from no causal completion: of 262,144 on
  total(A, {B, C}) with binary inputs, 211,968 are inseparable, such as a
  controlled swap. These are characterised by an inseparability witness
  (Theorem 2.9).
- **Factorisation.** Causal functions on parallel, sequential and
  conditional sequential compositions factor as products (Theorems
  2.17–2.19).
- **Topology.** With the lowerset topology on Ext(Θ) and on partial output
  functions, an extended function is causal iff it is continuous
  (Theorem 2.26). The opens of a space are themselves spaces, and causal
  functions restrict to them (Propositions 2.27–2.28, Corollary 2.29).
- **Sheaf or not.** Causal functions form a separated presheaf
  (Theorem 2.30). It is a sheaf iff Θ admits no solipsistic contextuality,
  so in particular when Θ is tight (Theorem 2.34). On the non-tight space
  Θ₃ there are two contexts with incompatible causal structure (A before
  B, and C before B), whose deterministic causal sections cannot be glued.
  The introduction says 1767 of the 2644 complete 3-event spaces exhibit
  this.
- **Empirical models and covers.** Distributions over extended causal
  functions form a presheaf (Definition 2.27). An empirical model is a
  compatible family on an open cover (Definition 2.31). Covers form a
  lattice from the fully solipsistic cover through the standard cover to
  the classical one (Proposition 2.42). Contextual means not the
  restriction of a classical model. Contextual and local fractions are
  defined as in Abramsky–Brandenburger (Definitions 2.32–2.34).
- **No non-locality on switch spaces.** Every standard empirical model on
  a causal switch space is local (Theorem 2.51). This includes every total
  order, and spaces built by conditional sequential composition of
  indiscrete spaces (Corollary 2.52). Other covers can still be contextual.
- **Examples.** The Leggett–Garg model is local for total(A, B, C), a
  mixture of 12 causal functions. The paper reads Leggett and Garg's
  macro-realist conditions as causal constraints that the model violates,
  so it ascribes the violation to signalling, not to contextuality. The
  BFW model is a 50–50 mixture of two inseparable functions on the
  indiscrete space.

## Standing in the record

Filed on 2026-10-09 from the manuscript bibliography of 2026-10-09 (work
`what-survives-translation`) at the owner's request, as a successor of
Gogioso and Pinzani 2021 ([LIT-tmpg68lt](LIT-tmpg68lt.md)). The authors withdrew that paper and
named this one among those superseding it. Of the three successors, this one
carries the withdrawn paper's subject: its title, its sheaf of causal
functions, locality as a global section, and empirical models as compatible
families. [LIT-tmpg68lt](LIT-tmpg68lt.md) is now Superseded by the trilogy. See the curation
entry of that day.

Read on 2026-10-09 ([NOTE-tmp98pr8](../notes.d/NOTE-tmp98pr8.md)). The reading is the source of
[THEORY-tmpquo32](../theory.d/THEORY-tmpquo32.md): when causal constraints depend on context, deterministic
locally causal data need not glue. It extends [LIT-016](LIT-016.md)'s framework, to which
it reduces on the discrete space, and [THEORY-012](../theory.d/THEORY-012.md)'s equation of
noncontextuality with gluing applies within it unchanged.

The vocabulary has no topic for causal structure. The paper is tagged
`contextuality` first because its results are about the sheaf-theoretic
contextuality framework.
