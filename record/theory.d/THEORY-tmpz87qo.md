---
status: Active
title: 'In counterexample-guided abstraction refinement the property and the concrete system are fixed inputs: the property''s atomic formulas help build the first abstraction and no abstraction may merge states that disagree on them, every refinement only splits classes toward the concrete state space, and a real counterexample ends the procedure; so the loop revises which of the concrete system''s distinctions the model draws, never the property or the space of possible answers'
version: 1
tags:
- logic
- mathematics
date: '2026-10-27'
source:
- LIT-tmpikbhf
summary: >-
  Clarke, Grumberg, Jha, Lu and Veith (2000), [LIT-tmpikbhf](../literature.d/LIT-tmpikbhf.md), read in
  [NOTE-tmpxgbdz](../notes.d/NOTE-tmpxgbdz.md). A textual fact about the algorithm as specified in §§3–4,
  and the exact form of the limit the exchange of 2026-10-27 (A16 §6) gave
  for CEGAR as the formal neighbour of inquiry as specification
  ([CLAIM-tmpalzo4](../claims.d/CLAIM-tmpalzo4.md)). It does not say that a property cannot be revised by
  anyone, only that no step of this procedure does it.
---
<!-- inactive-ok-file: CLAIM-tmpalzo4 CLAIM-419 — Proposed; the claims it bears on, cited as open -->

# THEORY-tmpz87qo: In counterexample-guided abstraction refinement the property and the concrete system are fixed inputs: the property's atomic formulas help build the first abstraction and no abstraction may merge states that disagree on them, every refinement only splits classes toward the concrete state space, and a real counterexample ends the procedure; so the loop revises which of the concrete system's distinctions the model draws, never the property or the space of possible answers

## Source

Clarke, Grumberg, Jha, Lu and Veith (2000), [LIT-tmpikbhf](../literature.d/LIT-tmpikbhf.md), §§2–4 (pp. 4–13 of
the authors' manuscript in CMU's repository); read in [NOTE-tmpxgbdz](../notes.d/NOTE-tmpxgbdz.md).

## What was actually shown

**The property shapes the abstraction before any check.** Atoms(P) is "the
set of atomic formulas that appear in the specification or in the
conditions of the transition blocks" (p. 5), and the initial abstraction
merges two value tuples of a variable cluster only if no atomic formula of
its cluster tells them apart: "two values are in the same equivalence class
if they cannot be "distinguished" by atomic formulas appearing in the
formula cluster" (p. 8). Soundness needs every atom of the property to
respect h, that is, never to differ within a class (Theorem 1, p. 5), and
§4.2 assumes it: "assume that φ respects h" (p. 8). The property thus fixes
a set of differences that no abstraction in the loop may erase.

**The concrete system is the reference.** Whether a counterexample is real
is decided by forward images under the concrete transition relation
(Lemma 1, p. 9), and the split is computed from concrete state sets
(§4.3, p. 11).

**Every revision is a split.** Step 3 refines h "by partitioning a single
equivalence class of ≡" (p. 7); §4.3 obtains the new relation ≡′ by
partitioning component classes (p. 11). Nothing in the procedure merges
classes, adds variables or atoms, or changes φ or M. Termination depends on
this: classes of a finite domain can be split only finitely often (p. 12).
So every abstraction the loop visits lies between the first one and the
concrete state space, and each refinement chooses among distinctions the
concrete system already has.

**A real counterexample ends it.** "If the counterexample is not spurious,
we report it to the user and stop" (p. 2); step 2, "we report it to the
user" (p. 7). What follows (a corrected design, or a corrected property) is
outside the procedure.

## What this does not say

- **That properties are never revised in verification practice.** The paper
  reports its Fujitsu bug as found (p. 15) and says nothing of what was
  done with it. The finding is about the algorithm, which has no step that
  revises a property.
- **That the abstraction is chosen independently of the question.** The
  reverse: the property's atoms are among what builds it (p. 5, pp. 7–8).
- **That CEGAR cannot be extended to revise its property.** Nothing in the
  paper bears on such an extension; the paper does not raise it.
- **That the analogy with inquiry or with a record's grammar holds.** That is
  [CLAIM-tmpalzo4](../claims.d/CLAIM-tmpalzo4.md)'s and [CLAIM-419](../claims.d/CLAIM-419.md)'s business. This document fixes only what
  the formal neighbour does: it refines within an answer space bounded by
  the concrete system and the fixed property, which is the kind of change
  [CLAIM-tmpalzo4](../claims.d/CLAIM-tmpalzo4.md)'s defeater (a) describes, and not the revision its last
  clause asserts.
