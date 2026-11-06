---
number: 1414
status: Proposed
formerly:
- THEORY-tmpo2kzn
promote_when: >-
  An independent derivation or computation, on a network other than the
  paper's two examples, confirms that the generalized index theorem holds
  with prestress and heterogeneous stiffness; that the zero-displacement
  tensions coincide with the states of self-stress; that the forces
  exciting each linear zero mode follow the symmetry of geometry and
  energy together; and that prestress breaking a geometric symmetry
  redirects and localizes those forces while leaving the linear zero modes
  unchanged.
title: 'Rocks and Mehta show that stating Maxwell–Calladine counting in terms of elastic susceptibilities gives an index theorem that holds with prestress and heterogeneous stiffness, in which the zero-displacement tensions are the states of self-stress while the forces that excite each linear zero mode follow the joint symmetry of geometry and energy, so that prestress breaking a geometric symmetry redirects and localizes those forces without changing the mechanisms'
version: 1
tags:
- natural-sciences
- mathematics
date: '2026-11-05'
source:
- LIT-2112
summary: >-
  Rocks and Mehta (2024; arXiv 2022), [LIT-2112](../literature.d/LIT-2112.md), read in [NOTE-1557](../notes.d/NOTE-1557.md)
  (the main text; the appendices with the proofs skipped). Proposed: the
  theorems' proofs were not read, and the symmetry-breaking result is shown
  on two small symmetric examples. It is a linear theory: it does not say
  when prestress makes a structure rigid, which the authors leave to a
  nonlinear analysis, nor whether zero modes extend to finite motions.
---

# THEORY-1414: Rocks and Mehta show that stating Maxwell–Calladine counting in terms of elastic susceptibilities gives an index theorem that holds with prestress and heterogeneous stiffness, in which the zero-displacement tensions are the states of self-stress while the forces that excite each linear zero mode follow the joint symmetry of geometry and energy, so that prestress breaking a geometric symmetry redirects and localizes those forces without changing the mechanisms

## Source

Rocks and Mehta (2024; arXiv v1 2022-08-15), [LIT-2112](../literature.d/LIT-2112.md); read in [NOTE-1557](../notes.d/NOTE-1557.md).

## What was actually shown

- **The theorem** (Sec. IV): rank–nullity on the susceptibilities ∂ℓ/∂f
  and ∂u/∂t gives N_dof − N_c = #LZEFs − #ZDTs, which "holds even in the
  presence of nonzero prestress or heterogeneous bond stiffnesses".
- **Theorem 1** (Sec. V B): "The ZDTs and SSSs are equivalent"; the LZEFs
  biject with the LZMs through ∂u/∂f, yet "in general, the LZEFs and LZMs
  span different subspaces".
- **Theorem 2** (Sec. VI A): LZMs carry the geometric symmetry group G,
  LZEFs the response symmetry G ∩ H.
- **The examples** (Sec. VI C): a diamond network and a 4×4 periodic square
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

## Note of 2026-11-06: what holds it back

The title says the authors show the generalized index theorem and Theorems 1 and 2, whose proofs are in Appendices B to D, which [NOTE-1557](../notes.d/NOTE-1557.md) did not read; a reading of those appendices, or a re-derivation checked by a second reader, would meet it. The localization clause rests on the paper's two worked examples and the title does not say so, so a promotion needs that hedge in the title. The promote_when's demand for an independent derivation on another network asks more than a reported title asserts ([ADR-065](../decisions.d/ADR-065.md)) and moves to a QUESTION when the condition is rewritten.
