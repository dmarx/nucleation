---
number: 1374
status: Proposed
formerly:
- THEORY-tmp530tx
promote_when: >-
  An independent screw-theoretic analysis, or a worked example published
  by others, confirms for hybrid flexure systems with non-interconnected
  limbs that the system's freedom space is the intersection of its
  parallel limbs' freedom spaces and the span of its serial stages'
  freedom spaces, and that comparing the elements' orders of constraint
  with the system's constraint space classifies a design correctly as
  exactly, over- or under-constrained.
title: 'Hopkins (2013) holds that a flexure system''s freedom space is the intersection of its parallel limbs'' freedom spaces and the span of its serial stages'' freedom spaces, so the same finite library of freedom–constraint space types suffices to analyse and synthesize any combination of parallel and serial flexures, and comparing constraint orders with the system''s constraint space classifies a design as exactly, over- or under-constrained'
version: 1
tags:
- natural-sciences
- mathematics
date: '2026-11-05'
source:
- LIT-2069
summary: >-
  Hopkins (2013), [LIT-2069](../literature.d/LIT-2069.md), read in full in [NOTE-1580](../notes.d/NOTE-1580.md). Proposed:
  the rules follow from linear reciprocity of screw spaces and are stated
  with design examples, but there is no experiment and no independent
  check, and the library's completeness rests on Hopkins (2010),
  [LIT-2042](../literature.d/LIT-2042.md). It excludes interconnected limbs, is kinematic only, and
  its over-constraint test says nothing of misfit stress.
---

# THEORY-1374: Hopkins (2013) holds that a flexure system's freedom space is the intersection of its parallel limbs' freedom spaces and the span of its serial stages' freedom spaces, so the same finite library of freedom–constraint space types suffices to analyse and synthesize any combination of parallel and serial flexures, and comparing constraint orders with the system's constraint space classifies a design as exactly, over- or under-constrained

## Source

Hopkins, "Designing hybrid flexure systems and elements using Freedom and
Constraint Topologies", *Mechanical Sciences* 4 (2013), [LIT-2069](../literature.d/LIT-2069.md);
read in [NOTE-1580](../notes.d/NOTE-1580.md).

## What was actually shown

- **Duality and the library (§2.1, pp. 322–323).** "Every freedom space
  uniquely links to a complementary or reciprocal space called a
  constraint space according to the principle of duality"; "there are fifty
  types that are numbered and organized into seven columns".
- **Combination rules (§§2.2–2.4).** In parallel, constraint spaces add and
  freedom spaces intersect; in series, freedom spaces add and constraint
  spaces intersect. Applied limb by limb, they give the freedom space of a
  hybrid system.
- **The tests (§§2.3, 2.5).** "If this sum is greater than the number of
  independent wrench vectors within the system’s constraint space, the
  system is over-constrained."; freedoms left in intermediate bodies when
  the stage is fixed make it under-constrained.
- **Examples (§3).** Ten hybrid elements, one giving a three-translation
  stage.

## What this does not say

- Anything about interconnected limbs: "It does not enable designers to
  analyse and synthesize hybrid flexure systems with interconnected limbs"
  (p. 329).
- Anything quantitative about stiffness, dynamics or misfit stress; the
  costs of under-constraint are named, not modelled.
- That the library's completeness was shown here; the paper rests it on
  earlier work.
- That any design was built or measured.
