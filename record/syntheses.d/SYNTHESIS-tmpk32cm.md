---
status: Proposed
title: 'A regularized linear readout separates exactly what the kernel separates: equal centred Gram matrices mean a translation and an orthogonal map, for positive ridge the readout kernel and the Gram matrix fix each other while the unregularized member sees only the column space, a symmetry forces degeneracy in a commuting operator but the spectrum fixes neither the group nor a basis, and so no such readout supplies a distinction beyond that freedom'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  the readout part of the formal-apparatus line left out without a reason
  given; or a link this account states that no component states. Its
  standing is its components': a component retired or demoted takes its
  clause with it, and nothing here holds the clause up.
tags:
- representation-learning
- mathematics
date: '2026-11-11'
line:
- formal-apparatus
integrates:
- CLAIM-290
- CLAIM-379
- CLAIM-385
- CLAIM-269
---
<!-- inactive-ok-file: ADR-075 CLAIM-193 CLAIM-263 SYNTHESIS-030 THEORY-002 THEORY-005 THEORY-080 — Proposed; components, decisions and accounts cited with their standing -->
<!-- inactive-ok-file: SYNTHESIS-tmpa7ef9 SYNTHESIS-tmpvz4mj — Proposed; cited with its standing -->

# SYNTHESIS-tmpk32cm: A regularized linear readout separates exactly what the kernel separates: equal centred Gram matrices mean a translation and an orthogonal map, for positive ridge the readout kernel and the Gram matrix fix each other while the unregularized member sees only the column space, a symmetry forces degeneracy in a commuting operator but the spectrum fixes neither the group nor a basis, and so no such readout supplies a distinction beyond that freedom

*A part account of the formal-apparatus line: one of the line's eleven
small clusters, four of the record's own demonstrations on what kernels
and spectra fix of a learned representation. The line's account is built
over it and its sibling parts. CLAIM-290 is first in learned-structure,
where SYNTHESIS-030 lists it among the entries linked to no other
component; this account integrates it again because its `line` includes
formal-apparatus.*

## The account

- **Equal Gram matrices.** CLAIM-290 (the record's own proofs of steps
  THEORY-004 rests on; thesis, demonstrated, Active): a positive-definite
  kernel's minimal realizations are unique up to a unitary, and two finite
  representation matrices with the same centred Gram matrix differ by a
  translation and an orthogonal map. Q need not be unique when the rank is
  below d.
- **The readout's separating power.** CLAIM-379 (split from CLAIM-269 at
  the owner's direction, carrying out the promotion audit; thesis,
  demonstrated, Active): on a finite set of stimuli, for ridge b > 0 the
  readout kernel and the Gram matrix determine each other, "Equal kernels
  therefore mean equal Gram matrices, and the converse is immediate", so
  readouts cannot tell apart exactly the orthogonal transformations of a
  centred representation of the same width; the CCA member, b = 0, sees
  only the column space, an invertible-linear freedom.
- **Symmetry and spectrum.** CLAIM-385 (the record's own, filed from
  THEORY-019; thesis, demonstrated, Active): an operator commuting with
  an orthogonal representation of a compact group has invariant
  eigenspaces and multiplicities that count real-irreducible dimensions,
  so SO(2) and ℤ/n for n ≥ 3 force paired eigenvalues; conversely the
  spectrum fixes neither the group nor a basis inside an eigenspace.
  "What a spectrum carries is the isotypic dimension count of whatever
  group is present, not the group."
- **The general statement.** CLAIM-269 (the assistant's restatement of
  CLAIM-193's general content, split under ADR-040, narrowed and promoted
  at the thirteenth status review; thesis, demonstrated, Active, version
  5): a regularized linear readout tells apart only representations that
  differ in normalized kernel, kernels fix a representation only up to
  the symmetry of what is observed, and so no such readout supplies a
  distinction beyond that symmetry. Its version 4 note: the degeneracy
  bullet "is what this claim adds to CLAIM-379, and it is CLAIM-385's item
  4". Its version 5 note: "Not by the readouts" follows from CLAIM-379.

## The components

- CLAIM-290, the record's own proofs, thesis, demonstrated, Active; first
  line learned-structure; grounds on LIT-259 and LIT-250.
- CLAIM-379, the promotion audit's split, thesis, demonstrated, Active;
  formal-apparatus only; rests on CLAIM-290.
- CLAIM-385, the record's own, thesis, demonstrated, Active;
  formal-apparatus only.
- CLAIM-269, the assistant's restatement, thesis, demonstrated, Active;
  formal-apparatus only; rests on CLAIM-379 and CLAIM-385.

## Links the components state, and where

Three pairs are linked, all relations:

- **CLAIM-379 rests on CLAIM-290.** Its body: "Two finite representation
  matrices of the same width with the same Gram matrix differ by an
  orthogonal transformation (CLAIM-290)".
- **CLAIM-269 rests on CLAIM-379 and CLAIM-385.** CLAIM-269's history
  (versions 2, 4 and 5) and its note of 2026-10-19 say which half each
  holds: the readout result is CLAIM-379, and the degeneracy bullet is
  CLAIM-385's item 4.

CLAIM-290 and CLAIM-385 name neither each other nor CLAIM-269.

## Links to other parts, stated

The community map found none. Mentions in histories only:

- **To the entries the line account (SYNTHESIS-tmpvz4mj) integrates directly.** CLAIM-385's history cites the precedent
  that a result the record proves belongs in a CLAIM, "as THEORY-005's
  became CLAIM-370 and THEORY-080's became CLAIM-384"; CLAIM-391's history
  cites the same precedent, naming CLAIM-385.

Outside the line, CLAIM-193 (pragmatic-transport, Proposed) rests on both
CLAIM-269 and CLAIM-264 of the effective-description account (SYNTHESIS-tmpa7ef9). That is the
nearest the cluster comes to another part, and it is two steps, through
an entry outside the line.

## Where else these entries are integrated

SYNTHESIS-030 (learned-structure) integrates CLAIM-290, and its "Links
tested as claims" sets CLAIM-290 beside CLAIM-263. No account integrates
CLAIM-269, CLAIM-379 or CLAIM-385.

## Not stated on the record

Tested by ADR-075's step 5 at this review and not filed:

- **A readout cannot see a rotation inside a degenerate eigenspace.**
  From CLAIM-379 (readouts are blind to every orthogonal map at b > 0) and
  CLAIM-385 (the spectrum fixes no basis inside an eigenspace). A rotation
  within an eigenspace is one orthogonal map among all, so the sentence is
  a trivial instance of CLAIM-379. Fails.
- **What CLAIM-269 adds to its premises.** See the review file's Arm A:
  read as the freedom CLAIM-379 names, CLAIM-269's "symmetry of what is
  observed" adds nothing to CLAIM-379 and CLAIM-385's item 4; read as the
  symmetry of the data distribution, the clause it dropped THEORY-002 for,
  it adds content that no premise now grounds.

## What it does not say

- Anything about nonlinear probes, estimated kernels, approximate
  equality or infinitely many stimuli, which every component disclaims.
- That the spectrum detects a symmetry; CLAIM-385 says the reverse.
