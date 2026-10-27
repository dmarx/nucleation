---
status: Open
title: 'Can composing systems create an effective structure whose adequate specification needs a richer relational vocabulary than the parts needed separately (relations of higher arity, history, or a new kind) and, if so, under what conditions, and is the new vocabulary forced by the composite or only by the restricted class of descriptions in use?'
version: 1
tags:
- compositionality
- mathematics
- design-rationale
date: '2026-10-27'
line: distributed-agency
summary: >-
  Raised at the owner's review of the pull request, which called it the
  result most worth preserving and asked that it "become a major research
  question". Hansen and Ghrist show that eliminating an interior vertex of
  a cellular sheaf can leave a three-way boundary relation, v₁ = v₂ + v₃,
  that no sheaf on the boundary's pairwise edges expresses ([THEORY-tmpvecoh](../theory.d/THEORY-tmpvecoh.md);
  [CLAIM-tmpose3y](../claims.d/CLAIM-tmpose3y.md)). For scalar networks reduction stays pairwise. The
  question asks when composition forces a change in the type of relational
  structure an adequate description needs. It also asks whether that is a
  fact about the composite or about the class of descriptions, and whether
  the same thing is what happens when a record's relation scheme cannot
  express what a composed organization requires.
---
<!-- inactive-ok-file: CLAIM-tmpose3y CLAIM-tmpdjt64 CLAIM-419 CLAIM-tmpoe0v5 CLAIM-tmpl228b CLAIM-tmp0yhlm QUESTION-tmplxq7l — Proposed, Open or new; the claims and question this one presses on -->

# QUESTION-tmprr9yy: Can composing systems create an effective structure whose adequate specification needs a richer relational vocabulary than the parts needed separately (relations of higher arity, history, or a new kind) and, if so, under what conditions, and is the new vocabulary forced by the composite or only by the restricted class of descriptions in use?

## Why it is a question

The owner's review of the pull request, 2026-10-27, on [THEORY-tmpvecoh](../theory.d/THEORY-tmpvecoh.md): "The
cellular-sheaf example demonstrates that composition followed by reduction can
force a change in the type of relational structure needed for an adequate
description. That's a remarkably direct mathematical analogue of the sort of
event we keep encountering in Luria: the existing relation scheme cannot express
what the composed organization requires." And: "Can composition create an
effective structure whose adequate specification requires a richer relational
vocabulary than the parts required individually? I think that deserves to
become a major research question in Nucleation."

What the record holds:

- **A demonstrated case.** A star with stalk ℝ² at the centre and ℝ at three
  leaves, with maps first coordinate, second coordinate and their sum.
  Eliminating the centre leaves the boundary constraint v₁ = v₂ + v₃. No
  sheaf on the boundary vertices, all of whose conditions are pairwise,
  has exactly that space of consistent assignments (Hansen and Ghrist,
  §4.2, Fig. 4.1; [THEORY-tmpvecoh](../theory.d/THEORY-tmpvecoh.md); [CLAIM-tmpose3y](../claims.d/CLAIM-tmpose3y.md)).
- **A sufficient condition against it.** With vertex stalks of dimension at
  most one, reduction stays within pairwise sheaves (Thm 4.3). For graph
  Laplacians the Schur complement is again a graph Laplacian (Thm 4.2).
- **The history case.** Eliminating a slow interior turns an instantaneous
  coupling into a relation over histories, a memory kernel ([CLAIM-tmpose3y](../claims.d/CLAIM-tmpose3y.md)).
  That is a richer vocabulary of another kind: relations among trajectories
  where the parts needed only relations among states.
- **The record's own case.** The record's amendments have added relation
  types and fields when a composed use of the grammar needed what it could
  not say. Examples are [ADR-044](../decisions.d/ADR-044.md)'s `corroborates` beside `rests_on` and
  [ADR-043](../decisions.d/ADR-043.md)'s `warrant` ([CLAIM-419](../claims.d/CLAIM-419.md), [CLAIM-tmpoe0v5](../claims.d/CLAIM-tmpoe0v5.md)). [CASE-tmp0zvle](../cases.d/CASE-tmp0zvle.md) measured
  how often. Whether those are instances of this question's phenomenon, or
  only resemble it, is part of the question.

## What it separates

1. **Forced by the composite or by the class.** The three-way relation is
   inexpressible within sheaves on the boundary graph. It is expressible in
   a hypergraph, or by keeping the interior vertex. A change of
   vocabulary may be forced by the composite's behaviour, or only by having
   restricted the descriptions to a class that excludes the interior. The
   answer may differ between the mathematics and the record.
2. **Effective or fundamental.** The owner's review set the limit: the result
   "does not by itself establish that a new fundamental physical interaction
   has arisen." The three-way relation is the trace, through a hidden
   interior, of relations that are all pairwise.
3. **Arity, history and kind.** Higher arity (the sheaf case), history (the
   memory case) and a new kind of relation (the record's amendments) may be
   one phenomenon or three.

## What would count as an answer

- **A characterization**, for some class of compositional systems beyond
  scalar networks, of when reduction stays within the parts' relational
  vocabulary and when it must leave it. Theorem 4.3 is one sufficient
  condition. A necessary one would be the first step.
- **A physical or simulated system** in which a boundary observer, confined
  to pairwise models, measurably fails to predict a composite until it
  admits a higher-arity or history-dependent relation, with the failure
  located as in CEGAR ([NOTE-tmpxgbdz](../notes.d/NOTE-tmpxgbdz.md)).
- **For the record**, a test of whether its scheme amendments followed
  compositions that its existing relation types could not express, or arose
  otherwise.
