---
number: 1406
status: Active
formerly:
- THEORY-tmpmbmox
title: 'Hopkins (2007) holds that for a rigid stage held in parallel by ideal wire-like flexures under small motions, the motions the stage permits and the lines along which a constraint can be added without changing them determine each other uniquely as reciprocal screw spaces, and that for pure-force constraints these pairs fall into 26 types indexed by the number of non-redundant constraints'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    At the twenty-ninth status review, at the status review's ruling (the
    owner delegated these rulings; ADR-065), on NOTE-1592 v2: promoted
    Proposed → Active, and promote_when deleted. The title reports what
    Hopkins (2007) holds, and the thesis holds each clause. The old
    promote_when asked for an independent derivation or classification,
    which the attribution does not need; it moves word for word to the new
    THEORY that extends this one and states the thesis without attribution
    (ADR-047 kind 1). It read: "An independent derivation or classification of reciprocal screw systems for ideal pure-force wrenches confirms that a rigid stage's freedom space and its constraint space determine each other one to one, and that the pairs fall into 26 types across one to six non-redundant constraints." Corrected in the body: the
    one-to-one link is asserted in §5.3, by example, and follows from the
    reciprocity of §5.2.5.
tags:
- natural-sciences
- mathematics
date: '2026-11-05'
source:
- LIT-2031
summary: >-
  Hopkins (2007), [LIT-2031](../literature.d/LIT-2031.md), read in [NOTE-1592](../notes.d/NOTE-1592.md) (every argument chapter and
  every passage stating the title's clauses; the case-by-case derivations
  of chs. 7–8 not read). Active as a report of what the thesis holds.
  Whether the 26 types are complete stays with the extending THEORY. The
  count holds only for ideal pure-force constraints; the thesis itself
  finds more types once wrenches of any pitch are allowed. It says nothing
  about stiffness, dynamics or actuation. Not peer reviewed.
---
# THEORY-1406: Hopkins (2007) holds that for a rigid stage held in parallel by ideal wire-like flexures under small motions, the motions the stage permits and the lines along which a constraint can be added without changing them determine each other uniquely as reciprocal screw spaces, and that for pure-force constraints these pairs fall into 26 types indexed by the number of non-redundant constraints

## Source

Hopkins, *Design of Parallel Flexure Systems via Freedom and Constraint
Topologies (FACT)*, MIT S.M. thesis (2007), [LIT-2031](../literature.d/LIT-2031.md); read in
[NOTE-1592](../notes.d/NOTE-1592.md) (abstract, chs. 1–3 in part, 5, 9, §10.1, 11).

## What was actually shown

- **Reciprocity.** A twist is permitted when it does no work against every
  constraint wrench, so the freedom space is the null space of the wrench
  matrix (§§3.4, 5.2.5), with Blanding's rule, "Every freedom line
  intersects every constraint line." (§2.2, p. 35), as a special case.
- **Unique linkage (§5.3, p. 90).** "This principle that complementary
  spaces are uniquely linked with each other is called the Principle of
  Complementary Topologies." It is asserted there as evident and shown on
  two examples; it follows from the reciprocity above.
- **The count (abstract, p. 3).** "twenty six unique matching pairs of
  freedom and constraint spaces were identified", in Cases 1–6 with 1, 3,
  9, 9, 3 and 1 types, Case N having N non-redundant constraints.
- **Redundancy (§5.2.1, p. 75).** "A constraint is non-redundant if when it
  is added to or removed from a system, the kinematics or the freedom space
  of that system changes."

## What this does not say

- That 26 types exhaust all flexure systems. They are for ideal pure-force
  constraints; with wrenches of any pitch "Case 3, therefore, has at least
  11 types." (§9.4, p. 299). The PhD thesis, [LIT-2042](../literature.d/LIT-2042.md), counts 50.
- Anything about serial or hybrid systems, which can have freedoms no
  parallel system has.
- Anything about stiffness, dynamics or actuation: "The elasto-mechanics
  of systems has, however, not been addressed in this thesis." (§11.3,
  p. 328).
- That constraints create freedom. In this account they only remove
  freedoms or leave the freedom space unchanged.
- That the enumeration is complete: chs. 7–8 were not read, and
  finiteness is "suggested" (§5.3). See the THEORY that extends this one.
