---
status: Superseded
superseded_by:
- LIT-tmp8bt8h
- LIT-tmpc7lcl
- LIT-tmp0y2pj
status_note: 'read 2026-10-09 ([NOTE-tmpjllrs](../notes.d/NOTE-tmpjllrs.md)), and superseded by its authors'' trilogy: [LIT-tmp8bt8h](LIT-tmp8bt8h.md) (The Combinatorics of Causality, arXiv 2206.08911), [LIT-tmpc7lcl](LIT-tmpc7lcl.md) (The Topology of Causality, 2303.07148) and [LIT-tmp0y2pj](LIT-tmp0y2pj.md) (The Geometry of Causality, 2303.09017). The authors withdrew it: the arXiv record''s v3 (3 April 2024) states that the paper "has been superseded by arXiv:2206.08911v4, arXiv:2303.07148 and arXiv:2303.09017", that its Definition 3 (the locale of inputs) "is not fit for purpose", and that it is "unlikely to be the right reference". The reading confirms the defect: the meet given in Proposition 5 can leave the poset, and the poset is not distributive, so it is not a locale ([NOTE-tmpjllrs](../notes.d/NOTE-tmpjllrs.md) gives a two-event counterexample). The successors replace the locale of inputs with spaces of input histories under the lowerset topology, a genuine topology; the sheaf of causal functions and locality as a global section are redone in [LIT-tmpc7lcl](LIT-tmpc7lcl.md), and the polytope and the BFW causal fractions are proved in [LIT-tmp0y2pj](LIT-tmp0y2pj.md).'
title: 'The Sheaf-Theoretic Structure of Definite Causality'
version: 2
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmpjllrs) from the EPTCS 343 PDF
    (QPL 2021, pp. 301–324, CC BY), fetched from the EPTCS server, with
    its proofs appendix; the arXiv v2 PDF (13 Sep 2021) is the same
    proceedings text and was fetched but not compared line by line.
    arXiv's PDF link for 2103.13771 returned an HTML page, not a PDF, and
    the abstract page shows why: v3 (3 Apr 2024, 1 KB) is a withdrawal
    notice (quoted in the status note). Details checked against arXiv (v1
    submitted 25 March 2021) and Crossref (DOI 10.4204/EPTCS.343.13,
    Electronic Proceedings in Theoretical Computer Science 343, 301–324,
    published 18 September 2021). `published:` is the arXiv v1 date. Not
    held in the Anthology of the SOTA: a grep of its record/ (clone of
    2026-10-09, commit d8b5ba5) for the authors, the identifiers and the
    title found nothing. Status Rejected because the authors withdrew it;
    the vocabulary lacks a word for causal structure, so it is tagged by
    its sheaf and contextuality content.
- version: 2
  date: '2026-10-09'
  note: >-
    Rejected → Superseded, by LIT-tmp8bt8h, LIT-tmpc7lcl and LIT-tmp0y2pj,
    the three papers the withdrawal names, filed and read the same day
    (NOTE-tmpp785f and NOTE-tmp98pr8 Read, NOTE-tmpht8fg Skimmed). The
    reason is unchanged: the authors withdrew the paper, and its
    Definition 3 is defective. Of the three, LIT-tmpc7lcl carries this
    paper's subject (the sheaf of causal functions, locality as a global
    section), LIT-tmp8bt8h replaces Definition 3 with spaces of input
    histories, and LIT-tmp0y2pj proves the polytope (Proposition 16) and
    the deferred Section 9 causal-fraction results. None of the three
    cites this paper. 2206.08911 was first posted on 17 June 2022 as
    "The Topology and Geometry of Causality" and split into the three
    papers in March 2023.
tags:
- contextuality
- quantum-foundations
- mathematics
date: '2026-10-09'
published: '2021-03-25'
arxiv: '2103.13771'
doi: '10.4204/EPTCS.343.13'
first_author: 'Gogioso'
keywords:
- 'sheaf theory'
- 'definite causal order'
- 'indefinite causal order'
- 'empirical models'
- 'causal functions'
- 'non-locality'
implementations: []
summary: >-
  Gogioso & Pinzani (2021), QPL 2021, EPTCS 343:301–324; withdrawn by the
  authors in 2024. Extends Abramsky–Brandenburger to a finite causal order.
  Inputs live on lower sets, sections are causal functions (an output
  depends only on inputs in its past), and an empirical model is a causal
  conditional distribution. Locality is a global section, equivalently a
  mixture of deterministic causal functions (Proposition 21). The models
  form a polytope cut out by linear causality equations, and pre-orders
  sketch indefinite causality. The construction's "locale of inputs" is
  not a locale, as the authors' withdrawal says.
---

<!-- inactive-ok-file: THEORY-tmpquo32 — Proposed; named as the successor's account of where this paper's sheaf claim holds -->

# LIT-tmpg68lt: The Sheaf-Theoretic Structure of Definite Causality

Stefano Gogioso and Nicola Pinzani (2021), in M. Backens and C. Heunen (eds),
*Quantum Physics and Logic* (QPL 2021), EPTCS 343, 301–324 — [ARXIV-2103.13771](https://arxiv.org/abs/2103.13771)
(withdrawn, v3)

## Key takeaways

- **Scenarios.** A definite causal scenario is a finite poset Ω of events,
  with finite input and output sets at each event (Definition 1). The
  discrete order is exactly the Abramsky–Brandenburger non-locality
  scenario (Definition 2, Proposition 9).
- **Causal sections.** Sections over a family of input sets indexed by a
  lower set are *causal* functions: the output at ω depends only on
  inputs at events ≤ ω (Definitions 6–7). Explicitly, a product over ω of
  functions from the inputs in ω's down-set to O_ω (Eq. 21; worked for a
  four-event diamond in Section 5).
- **Empirical models are causal conditional distributions**
  (Proposition 15). For every lower set λ, the marginal on λ does not
  depend on inputs outside λ. The probabilistic ones form a polytope: a
  product of simplices cut by the linear causality equations
  (Proposition 16).
- **Locality** (Definition 18, Proposition 21). A model is local if and
  only if it is a mixture, with weights in the semiring R, of deterministic
  causal functions: a classical hidden-variable model in which outputs
  depend only on past inputs. The quantum diamond example (Section 8) is
  presented as a model, not analysed for locality.
- **Indefinite causality, sketched** (Section 9). Pre-orders replace
  partial orders. For the Baumeler–Feix–Wolf model, an "Ω-causal fraction"
  is 0 for every partial order and 1 for four pre-orders. Results are
  stated, with proofs deferred to a later paper.
- **Withdrawn.** The authors withdrew it on arXiv in April 2024. Its
  Definition 3 should be replaced by the "spaces of input histories" of
  arXiv 2206.08911 ([LIT-tmp8bt8h](LIT-tmp8bt8h.md)).

## Standing in the record

Filed on 2026-10-09 from the manuscript bibliography of 2026-10-09 (work
`what-survives-translation`) at the owner's request: a work the manuscript
considered and dropped from its final reference list. See the curation entry
of that day.

Read on 2026-10-09 ([NOTE-tmpjllrs](../notes.d/NOTE-tmpjllrs.md)) and set to `Rejected`. The reason was not
the reading's judgement of its idea. The authors withdrew the paper and
named its successors, and the reading found the defect they name.

Later the same day the three successors were filed and read, and this entry
became `Superseded` by them:

- *The Combinatorics of Causality* ([LIT-tmp8bt8h](LIT-tmp8bt8h.md), arXiv 2206.08911)
  replaces the locale of inputs with spaces of input histories.
- *The Topology of Causality* ([LIT-tmpc7lcl](LIT-tmpc7lcl.md), 2303.07148) redoes this
  paper's sheaf of causal functions over the lowerset topology of those
  spaces. That topology is a genuine locale. It shows that the sheaf
  property holds for every space induced by a causal order, so the
  definite case of this paper survives, but fails for some dynamical
  structures ([THEORY-tmpquo32](../theory.d/THEORY-tmpquo32.md)).
- *The Geometry of Causality* ([LIT-tmp0y2pj](LIT-tmp0y2pj.md), 2303.09017) proves the
  polytope of Proposition 16 in general and computes the BFW causal
  fractions this paper's Section 9 deferred.

A reader who wants the sheaf-theoretic treatment of causal order should go
to [LIT-tmpc7lcl](LIT-tmpc7lcl.md) first. None of the three cites this paper.

It extends [LIT-016](LIT-016.md)'s framework: on the discrete order it reduces to it
exactly (Proposition 9). The vocabulary has no topic for causal structure
or causal order. It is tagged `contextuality` first because its
contribution is to the sheaf-theoretic contextuality framework.
