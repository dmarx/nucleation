---
status: Rejected
status_note: 'read 2026-10-09 (NOTE-tmpjllrs), and retired: withdrawn by its authors. The arXiv record''s v3 (3 April 2024) is a withdrawal stating that the paper "has been superseded by arXiv:2206.08911v4, arXiv:2303.07148 and arXiv:2303.09017", that its Definition 3 (the locale of inputs) "is not fit for purpose", and that it is "unlikely to be the right reference". The reading confirms the defect: the meet given in Proposition 5 can leave the poset, and the poset is not distributive, so it is not a locale (NOTE-tmpjllrs gives a two-event counterexample). The idea it introduced stands: a sheaf of causal functions over lower sets of a causal order, with locality as a global section and a decomposition into deterministic causal functions. The record holds none of the successor papers. When one is filed, this entry should become Superseded by it.'
title: 'The Sheaf-Theoretic Structure of Definite Causality'
version: 1
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

# LIT-tmpg68lt: The Sheaf-Theoretic Structure of Definite Causality

Stefano Gogioso and Nicola Pinzani (2021), in M. Backens and C. Heunen (eds),
*Quantum Physics and Logic* (QPL 2021), EPTCS 343, 301–324 — ARXIV-2103.13771
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
  arXiv 2206.08911.

## Standing in the record

Filed on 2026-10-09 from the manuscript bibliography of 2026-10-09 (work
`what-survives-translation`) at the owner's request: a work the manuscript
considered and dropped from its final reference list. See the curation entry
of that day.

Read on 2026-10-09 (NOTE-tmpjllrs) and set to `Rejected`. The reason is not
the reading's judgement of its idea. The authors withdrew the paper and
named its successors, and the reading found the defect they name. A reader
who wants the sheaf-theoretic treatment of causal order should go to
Gogioso & Pinzani, *The Combinatorics of Causality* (arXiv 2206.08911), and
its sequels *The Topology of Causality* (2303.07148) and *The Geometry of
Causality* (2303.09017). The record holds none of them. Filing the first
would let this entry become `Superseded` with a named successor.

It extends LIT-016's framework: on the discrete order it reduces to it
exactly (Proposition 9). The vocabulary has no topic for causal structure
or causal order. It is tagged `contextuality` first because its
contribution is to the sheaf-theoretic contextuality framework.
