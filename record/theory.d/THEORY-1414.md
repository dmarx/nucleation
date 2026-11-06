---
number: 1414
status: Active
formerly:
- THEORY-tmpo2kzn
title: 'Rocks and Mehta show that stating Maxwell–Calladine counting in terms of elastic susceptibilities gives an index theorem that holds with prestress and heterogeneous stiffness, in which the zero-displacement tensions are the states of self-stress while the forces that excite each linear zero mode follow the joint symmetry of geometry and energy, and on two worked networks prestress breaking a geometric symmetry redirects those forces and localizes them to the prestressed bonds without changing the mechanisms'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted at the status review's ruling (the owner
    delegated these rulings), under ADR-065. NOTE-1557 version 2 reads the
    paper in full, the proofs in Appendices B to D included, and nothing
    in the record contradicts the report. The localization clause is
    hedged to the paper's two worked networks, which is all the paper
    shows; the general clause was the title's overstatement and gets a
    dated note (ADR-047 kind 3). The old title: Rocks and Mehta show that
    stating Maxwell–Calladine counting in terms of elastic
    susceptibilities gives an index theorem that holds with prestress and
    heterogeneous stiffness, in which the zero-displacement tensions are
    the states of self-stress while the forces that excite each linear
    zero mode follow the joint symmetry of geometry and energy, so that
    prestress breaking a geometric symmetry redirects and localizes those
    forces without changing the mechanisms. The promote_when asked for an
    independent derivation, which the title does not assert, and moves
    unchanged to QUESTION-423. The old condition: An independent
    derivation or computation, on a network other than the paper's two
    examples, confirms that the generalized index theorem holds with
    prestress and heterogeneous stiffness; that the zero-displacement
    tensions coincide with the states of self-stress; that the forces
    exciting each linear zero mode follow the symmetry of geometry and
    energy together; and that prestress breaking a geometric symmetry
    redirects and localizes those forces while leaving the linear zero
    modes unchanged. It now corroborates CLAIM-588, from whose grounds it
    moved under ADR-058, and the status review's own sharpening,
    CLAIM-609.
tags:
- natural-sciences
- mathematics
date: '2026-11-05'
source:
- LIT-2112
bears_on:
- QUESTION-423
corroborates:
- CLAIM-588
- CLAIM-609
summary: >-
  Rocks and Mehta (2024; arXiv 2022), [LIT-2112](../literature.d/LIT-2112.md), read in full in [NOTE-1557](../notes.d/NOTE-1557.md),
  the proof appendices included. Held as what the authors show: an index
  theorem in elastic susceptibilities that holds with prestress and
  heterogeneous stiffness, whose counts by Theorem 1 always equal the
  classical ones; zero-displacement tensions that are the states of
  self-stress; forces exciting the zero modes that follow the symmetry of
  geometry and energy together; and, on two worked networks with uniform
  stiffness, prestress that redirects and localizes those forces with the
  mechanisms unchanged. It is a linear theory: it does not say when
  prestress makes a structure rigid, nor whether zero modes extend to
  finite motions. Whether an independent derivation confirms it is
  [QUESTION-423](../questions.d/QUESTION-423.md).
---
<!-- inactive-ok-file: CLAIM-609 — Proposed and new; the status review's own sharpening of this reading, left for the next pass to rule on -->

# THEORY-1414: Rocks and Mehta show that stating Maxwell–Calladine counting in terms of elastic susceptibilities gives an index theorem that holds with prestress and heterogeneous stiffness, in which the zero-displacement tensions are the states of self-stress while the forces that excite each linear zero mode follow the joint symmetry of geometry and energy, and on two worked networks prestress breaking a geometric symmetry redirects those forces and localizes them to the prestressed bonds without changing the mechanisms

## Source

Rocks and Mehta (2024; arXiv v1 2022-08-15), [LIT-2112](../literature.d/LIT-2112.md); read in [NOTE-1557](../notes.d/NOTE-1557.md).

## What was actually shown

- **The theorem** (Sec. IV, proved there): rank–nullity on the susceptibilities ∂ℓ/∂f
  and ∂u/∂t gives N_dof − N_c = #LZEFs − #ZDTs, which "holds even in the
  presence of nonzero prestress or heterogeneous bond stiffnesses".
- **Theorem 1** (Sec. V B; proof App. B1): "The ZDTs and SSSs are equivalent"; the LZEFs
  biject with the LZMs through ∂u/∂f, yet "in general, the LZEFs and LZMs
  span different subspaces".
- **Theorem 2** (Sec. VI A; proof App. B3, from the invariance
  relations of App. B2): LZMs carry the geometric symmetry group G,
  LZEFs the response symmetry G ∩ H.
- **The examples** (Sec. VI C–D, both with uniform stiffness): a diamond network and a 4×4 periodic square
  lattice, where symmetry-breaking prestress leaves the LZMs unchanged and
  the coupled LZEF "localizes to the line of prestressed bonds". This could
  have come out otherwise: restoring the symmetry restores the match.

## What this does not say

- That prestress can make a floppy network rigid, or how: the counts "still
  do not fully capture the effects of prestress-induced rigidity".
- That linear zero modes extend to finite mechanisms.
- That redundant constraints create states of self-stress. The pasted
  synthesis on constraint architectures attributes that to this paper; it
  is A's paraphrase, and the paper does not discuss adding constraints.
- That the results hold for hard constraints, which are excluded.
- That the generalized count differs from the classical one. By Theorem 1 the
  number of LZEFs equals the number of LZMs and the number of ZDTs the number
  of SSSs; what changes is which forces and tensions they are.
- That stiffness alone redirects the forces. The examples use uniform
  stiffness throughout; the status review's own result ([CLAIM-609](../claims.d/CLAIM-609.md))
  shows that, for a linear zero mode, it cannot.

## Note of 2026-11-06: what holds it back

The title says the authors show the generalized index theorem and Theorems 1 and 2, whose proofs are in Appendices B to D, which [NOTE-1557](../notes.d/NOTE-1557.md) did not read; a reading of those appendices, or a re-derivation checked by a second reader, would meet it. The localization clause rests on the paper's two worked examples and the title does not say so, so a promotion needs that hedge in the title. The promote_when's demand for an independent derivation on another network asks more than a reported title asserts ([ADR-065](../decisions.d/ADR-065.md)) and moves to a QUESTION when the condition is rewritten.

## Note of 2026-11-06: read in full, narrowed and promoted

[NOTE-1557](../notes.d/NOTE-1557.md) version 2 reads Appendices A to D. The index theorem is proved in Sec. IV by rank–nullity. Theorems 1 and 2 and their corollaries are proved in Appendix B, and each step checks. The title's localization clause stated generally what the paper shows on two networks, a diamond network and a 4×4 periodic square lattice, so it is now hedged to those two. The demand for an independent derivation is [QUESTION-423](../questions.d/QUESTION-423.md). The status review's [CLAIM-609](../claims.d/CLAIM-609.md) derives the localization in general, in the limit of a vanishing regularizer. That result is the record's own and is not the paper's.
