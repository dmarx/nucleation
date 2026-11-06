---
status: Proposed
promote_when: >-
  An independent derivation or classification of reciprocal screw systems
  for ideal pure-force wrenches confirms that a rigid stage's freedom space
  and its constraint space determine each other one to one, and that the
  pairs fall into 26 types across one to six non-redundant constraints.
title: 'For a rigid stage held in parallel by ideal wire-like flexures under small motions, the motions the stage permits and the lines along which a constraint can be added without changing them determine each other uniquely as reciprocal screw spaces, and for pure-force constraints these pairs fall into 26 types indexed by the number of non-redundant constraints'
version: 1
history:
- version: 1
  date: '2026-11-06'
  note: >-
    Filed at the twenty-ninth status review, at the status review's ruling
    (the owner delegated these rulings; ADR-047 kind 1, ADR-065): the wider
    thesis THEORY-1406 reported, split off when THEORY-1406 was promoted as
    a report of what Hopkins (2007) holds. It keeps THEORY-1406 v1's
    wording, without the attribution, and its promote_when word for word.
tags:
- natural-sciences
- mathematics
date: '2026-11-06'
source:
- LIT-2031
extends:
- THEORY-1406
summary: >-
  What Hopkins (2007) holds (THEORY-1406), stated as true. The thesis says
  "it was proven that these spaces embody all possible solutions"
  (abstract). Its uniqueness argument is by example, though it follows
  from screw reciprocity; finiteness is "suggested" by the six-constraint
  bound; and the 26 come from a case analysis (chs. 7–8). Proposed until an
  independent derivation or classification confirms them. The uniqueness
  half is close to standard linear algebra and might be split off as
  demonstrated, if a reviewer writes it out.
---

# THEORY-tmpdw067: For a rigid stage held in parallel by ideal wire-like flexures under small motions, the motions the stage permits and the lines along which a constraint can be added without changing them determine each other uniquely as reciprocal screw spaces, and for pure-force constraints these pairs fall into 26 types indexed by the number of non-redundant constraints

## Source

Hopkins, *Design of Parallel Flexure Systems via Freedom and Constraint
Topologies (FACT)*, MIT S.M. thesis (2007), LIT-2031; read in NOTE-1592.
The attributed report is THEORY-1406.

## What would settle it

An independent derivation or classification of reciprocal screw systems
for ideal pure-force wrenches that recovers the one-to-one link between
freedom and constraint spaces and the 26 types by number of non-redundant
constraints (1, 3, 9, 9, 3 and 1).

## Where it stands

- **Uniqueness** is asserted in §5.3 as evident and shown on two examples;
  it follows from the reciprocity of §5.2.5, the freedom space being the
  null space of the constraint wrenches.
- **Finiteness** "is suggested by the fact that no more than 6 constraints
  may be non-redundant" (§5.3).
- **The count** comes from arranging non-redundant constraint lines for
  Cases 1–3 (ch. 7) and combining twists for Cases 4–6 (ch. 8), where §8.1
  "proves that there are only 10 possible ways to combine two independent
  twists" for Case 4, nine usable with pure-force constraints. Chapters 7–8
  were not read.
- **Scope**: ideal pure-force constraints only; with wrenches of any pitch
  the thesis finds more types (§9.4), and the PhD thesis, LIT-2042, counts
  50.
