---
number: 148
status: Open
formerly:
- QUESTION-tmpvxp0f
title: 'Do bilinear knowledge-graph scores (RESCAL, ComplEx, HolE, the Neural Tensor Network, QuatE) admit a representation as a coboundary of a sheaf of vector spaces, or is there a proof that they do not?'
version: 1
tags:
- mathematics
- representation-learning
date: '2026-10-19'
line: formal-apparatus
summary: >-
  The open half of [THEORY-299](../theory.d/THEORY-299.md)'s former promote_when. On 2026-10-19
  [THEORY-299](../theory.d/THEORY-299.md) was narrowed and promoted: structured and translational
  embeddings are 0-cochains of a pulled-back sheaf scored by a norm of the
  coboundary. Gebhart, Hansen and Schrater ([LIT-232](../literature.d/LIT-232.md)) state that bilinear
  models fall outside the framework as given (App. A.1) and do not prove
  it. Whether any sheaf of vector spaces takes them in is open.
---

# QUESTION-148: Do bilinear knowledge-graph scores (RESCAL, ComplEx, HolE, the Neural Tensor Network, QuatE) admit a representation as a coboundary of a sheaf of vector spaces, or is there a proof that they do not?

## Why it is a question

A structured or translational score is a norm of F_{h⊴r} x_h − F_{t⊴r} x_t,
plus a translation, which is a coboundary on the edge ([THEORY-299](../theory.d/THEORY-299.md)). A
bilinear score x_hᵀ M_r x_t is not visibly of that form. It is a pairing,
not a difference. [LIT-232](../literature.d/LIT-232.md) says such models "do not fit" (App. A.1), and
[NOTE-843](../notes.d/NOTE-843.md) rates that moderate: stated, not proved impossible. The paper
suggests sheaves valued in other categories might take them in
(App. E). Until 2026-10-19 [THEORY-299](../theory.d/THEORY-299.md)'s promote_when asked for "a proof,
or a counterexample". At the owner's direction, from the promotion
audit's batch 013 (record/promotion-audit/decisions/[THEORY-299](../theory.d/THEORY-299.md).yaml,
[ADR-047](../decisions.d/ADR-047.md)), [THEORY-299](../theory.d/THEORY-299.md) was promoted without it, because its title does not
claim it, and the request moved here.

## What would answer it

A proof that no sheaf of vector spaces on the knowledge graph, with
embeddings as 0-cochains, has a coboundary whose norm (or a fixed
monotone function of it) reproduces a bilinear score, or a construction
that does. A construction must say what it changes: the category of the
stalks, the cochain degree, or the scoring function. Benchmark results
cannot settle it, because they bear on how well the models work, not on
what they are.
