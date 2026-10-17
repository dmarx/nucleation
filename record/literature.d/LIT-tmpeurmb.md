---
status: Active
status_note: 'read in full 2026-10-17 (NOTE-tmpRAUH); worth reading as the short proof that the identity axiom and a non-negative decomposition on the Williams–Beer lattice cannot both hold once there are three sources: with Y1, Y2 independent bits, Y3 = Y1 ⊕ Y2 and the target their joint copy, identity, the Williams–Beer axioms and invariance under relabelling the target force the atom {12}{13}{23} to be at most −1 bit. So a multivariate extension of Bertschinger et al.''s unique information cannot be a partial information decomposition. Read it knowing that the theorem rests on the identity axiom applied to sources that are sets of variables and on an unstated invariance under relabelling the target, that its other results (monotonicity of unique information, failure of left monotonicity) are about the bivariate measures, and that the multivariate structure it calls for is left open. Filed as THEORY-tmpRAUHT.'
title: 'Reconsidering unique information: Towards a multivariate information decomposition'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Filed at the owner's request for the gap the PID filing left open: no
    held work gave ΦID a redundancy function with the identity property for
    more than two sources. Citation checked against Crossref on 2026-10-17
    (2014 IEEE International Symposium on Information Theory, pp.
    2232–2236, doi 10.1109/ISIT.2014.6875230, June 2014); `published:` is
    the arXiv v1 date, 11 April 2014. Not held in the Anthology of the
    SOTA: a grep of its record/ (clone of 2026-10-12, d1573d2) for "Rauh",
    the identifiers and "partial information decomposition" found nothing.
    Read in full the same day from arXiv 1404.3146v1, 5 pp., §§I–V, all
    proofs, Fig. 1. The ISIT version was not compared.
tags:
- information-theory
- mathematics
date: '2026-10-17'
published: '2014-04-11'
arxiv: '1404.3146'
doi: '10.1109/ISIT.2014.6875230'
first_author: 'Rauh'
keywords:
- 'unique information'
- 'shared information'
- 'synergy'
- 'partial information lattice'
- 'identity axiom'
- 'local positivity'
- 'left monotonicity'
extends:
- LIT-1162
implementations: []
summary: >-
  Rauh, Bertschinger, Olbrich & Jost (2014), ISIT 2014: 2232–2236, [ARXIV-1404.3146](https://arxiv.org/abs/1404.3146). Theorem 2: no redundancy function satisfies the Williams–Beer axioms (symmetry, self-redundancy, monotonicity), local positivity (non-negative partial-information atoms) and the identity axiom. The counterexample is three sources, two independent bits and their XOR, with the target their joint copy: identity forces each atom {i}{jk} to 1 bit and the total is 2 bits, so the atom {12}{13}{23} ≤ −1. Lemmas 3–4: Bertschinger et al.'s unique information decreases as the other source is enlarged and increases as its own source or the target is; their shared information increases with a source but violates left monotonicity, as does their synergy.
---

# LIT-tmpeurmb: Reconsidering unique information: Towards a multivariate information decomposition

Johannes Rauh, Nils Bertschinger, Eckehard Olbrich and Jürgen Jost (2014), "Reconsidering unique information: Towards a multivariate information decomposition", *2014 IEEE International Symposium on Information Theory*: 2232–2236 — [ARXIV-1404.3146](https://arxiv.org/abs/1404.3146)

## Key takeaways

*From the reading, [NOTE-tmpRAUH](../notes.d/NOTE-tmpRAUH.md).*

- **The impossibility (Theorem 2).** No I∩ satisfies symmetry,
  self-redundancy, monotonicity (with subset equality), local positivity
  and the identity axiom. In XORCOPY, Y1 and Y2 are independent uniform
  bits, Y3 = Y1 ⊕ Y2 and X = (Y1, Y2, Y3). Identity gives I∩(X: Yi; Yj) = 0
  and I∩(X: Yi; YjYk) = MI(Yi; YjYk) = 1. Monotonicity then makes the bottom
  of the lattice zero and each {i}{jk} atom 1 bit. But I∩ at {12}{13}{23}
  is at most MI(X; Y1Y2Y3) = 2, so its atom is at most 2 − 3 = −1.
- **Two silent premises.** Identity is applied with a set of variables as
  one source, and I∩(X: …) is taken to equal I∩((Yi, Yj): …) because X is
  a relabelling of any pair. The paper does not list the second as an
  axiom.
- **Consequence.** A multivariate decomposition that extends Bertschinger
  et al.'s bivariate one consistently "cannot be a partial information
  decomposition". Which terms it should have is left open.
- **Bivariate monotonicity (Lemmas 3–4, §IV-C).** ŨI(X: Y \ (Z, Z′)) ≤
  ŨI(X: Y \ Z); enlarging Y or X increases ŨI; S̃I increases when a source
  is enlarged. S̃I and C̃I violate left monotonicity, which the paper
  traces to the identity axiom: AND gives S̃I = 0.311 bit about Z but 0
  about the copy (X, Y).
- **Conjecture (§V).** MI(X; Y1…Yk) − Σ ŨI(X: Yi \ rest) ≥ 0, which would
  follow from ŨI(X: Y \ Z, W) + ŨI(X: Z \ Y, W) ≤ ŨI(X: (Y, Z) \ W).
  Unproved here.

## Standing in the record

Filed on 2026-10-17 for the gap left open by the PID filing, and read the
same day. It changes the gap's shape. The record asked for a multivariate
redundancy function with the identity property for ΦID. This paper proves
that, on the lattice ΦID inherits, no such function also gives
non-negative atoms. So the gap cannot be closed as stated. One of identity,
non-negativity or the lattice has to go, and the record's position is
[CLAIM-tmpGAP](../claims.d/CLAIM-tmpGAP.md). Ince's I_ccs ([LIT-tmpeucmj](LIT-tmpeucmj.md)) is one way of letting
non-negativity go. Filed as [THEORY-tmpRAUHT](../theory.d/THEORY-tmpRAUHT.md). `mathematics` is for the
result's form, an impossibility theorem on a lattice. It carries no
instruction for machine-learning practice.
