---
status: Proposed
title: 'Whether a criterion on a coarse-graining picks out the variables renormalization keeps is open in three settings: on a lattice slab the information bottleneck''s first transition is the bifurcation, and its first feature the leading transfer-matrix mode, only under some further condition; inside Kadanoff''s kernel families it is unsettled whether the exact trace condition keeps the relevant operators; and the coarse-graining that maximizes mutual information beyond a buffer has so far found only variables already known'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  this part of the formal-apparatus line left out without a reason given;
  or a link this account states that no component states. Its standing is
  its components': a question answered or retired takes its clause with
  it, and nothing here holds the clause up.
tags:
- natural-sciences
- information-theory
- representation-learning
date: '2026-11-11'
line:
- formal-apparatus
integrates:
- QUESTION-185
- QUESTION-205
- QUESTION-232
---
<!-- inactive-ok-file: ADR-047 — Superseded; cited with its standing -->
<!-- inactive-ok-file: ADR-075 SYNTHESIS-tmpa7ef9 — Proposed; cited with its standing -->

# SYNTHESIS-tmppu0yx: Whether a criterion on a coarse-graining picks out the variables renormalization keeps is open in three settings: on a lattice slab the information bottleneck's first transition is the bifurcation, and its first feature the leading transfer-matrix mode, only under some further condition; inside Kadanoff's kernel families it is unsettled whether the exact trace condition keeps the relevant operators; and the coarse-graining that maximizes mutual information beyond a buffer has so far found only variables already known

*A part account of the formal-apparatus line: three open questions that the
mechanical map of the line found linked to no other entry of it, and that
read as one inquiry. All three are promotion conditions moved off THEORY
entries when the promotion audit of 2026-10-19 and 2026-10-20 (ADR-047)
narrowed and promoted them. The line's account is built over this account
and its sibling parts. None of the three is integrated by any other
account; each carries formal-apparatus as its only line.*

## The account

- **The slab and the bottleneck.** QUESTION-185 (Open; the promotion
  condition formerly on THEORY-205, widened) starts from what THEORY-205
  holds exactly: "in the slab geometry on a cylinder the uninformative
  information-bottleneck encoder loses local stability at β =
  (λ0/λ1)^(2L_B)", in the direction of the leading excited transfer-matrix
  eigenvector. The encoder stops being globally optimal earlier, at
  β = 1/s*. In the circumference-3 critical Ising check the two thresholds
  agree; on a chain of 3-state units "they differ 27-fold at a buffer of
  two transfer steps". So "the IB's first transition in a lattice model is
  the bifurcation only under some further condition, perhaps a symmetry",
  and whether the first feature the global optimum keeps is the leading
  excited mode is open.
- **The trace condition inside Kadanoff's families.** QUESTION-205 (Open;
  the promotion condition formerly on THEORY-202) starts from THEORY-202's
  general case: over general Boltzmann machines a joint Hamiltonian "can
  match the partition function with the wrong marginal", and a
  non-interacting hidden system meets the trace condition exactly with a
  freely chosen coarse Hamiltonian. That construction needs visible-visible
  couplings, which Kadanoff's kernel families exclude. Whether exactness
  inside those families keeps the relevant operators, "or still leaves the
  coarse variables free, is not settled by either source".
- **The mutual-information maximizer beyond a buffer.** QUESTION-232
  (Open; the promotion condition formerly on THEORY-194) starts from what
  the coarse-graining trained to maximize mutual information with the
  environment beyond a buffer found on the 2D Ising and dimer models: "the
  variables renormalization already knew". Its sequels prove that full
  capture of a block's information about its environment keeps the
  Hamiltonian short-ranged, "while the optimised coarse-grainings fall
  short of that condition" (LIT-881, THEORY-198). Open: whether the
  objective and renormalization agree where renormalization's variables
  are unknown, and whether the maximizer gives short-ranged couplings in
  two or more dimensions.

## The components

- QUESTION-185, Open, the promotion condition formerly on THEORY-205
  (2026-10-19, ADR-047 v2), widened; line formal-apparatus only.
- QUESTION-205, Open, the promotion condition formerly on THEORY-202
  (2026-10-20, ADR-047 v2); line formal-apparatus only.
- QUESTION-232, Open, the promotion condition formerly on THEORY-194
  (2026-10-20, ADR-047 v3); line formal-apparatus only.

## Links the components state, and where

- **The slab and the buffer shell are different geometries.** QUESTION-232's
  body: "Near the first information-bottleneck transition the optimal
  encoder of a slab follows the leading transfer-matrix mode (LIT-885,
  THEORY-205), which is a different geometry from a block in a buffer
  shell." QUESTION-185, from the other side, under "What would answer it":
  "What would not answer it: results for planar blocks inside a buffer
  shell, or for RSMI at a fixed alphabet. They bear on the wider claim
  THEORY-205 does not make." These are the only links the three state
  among themselves, and both are between QUESTION-185 and QUESTION-232.
- **Through the parent readings, outside the line.** THEORY-205's body
  calls it "the formal counterpart of THEORY-194". THEORY-202's body cites
  THEORY-194: "THEORY-194 and LIT-873 show a target can come from the
  data's spatial structure (the environment beyond a buffer) without
  labels." THEORY-198's body: "It underpins THEORY-194, which records that
  the information-maximizing coarse-graining matched the known RG
  variables of the Ising and dimer models". These
  readings carry no `line`, so the map did not count them; they are where
  QUESTION-205 meets the other two.

## Links to other parts, stated

- **To the effective-descriptions part (SYNTHESIS-tmpa7ef9).** CLAIM-152 (Active; also
  distributed-agency) grounds on THEORY-194 and THEORY-202, the readings
  QUESTION-232 and QUESTION-205 were moved off, and its note of
  2026-10-12 reads them: THEORY-194, "which variables a compression keeps
  is set by what it must stay informative about"; THEORY-202, "the
  variables a renormalization keeps must be fixed by a stated target".
  No component names CLAIM-152, and CLAIM-152 names none of them. This is
  the only link to another part, and it runs through the parents.

## Not stated on the record

- **That the three are one finding.** That each question asks whether a
  criterion on the coarse-graining (an information-bottleneck optimum, an
  exact trace condition, maximal mutual information beyond a buffer) fixes
  the variables renormalization keeps, and that in each the record holds
  only that it does not without something further, is this account's
  grouping. Tested by ADR-075 step 5: as a sentence about the three it is
  a conjunction of held statements (each question's own "Why it is a
  question"), and in its general form it is CLAIM-152's thesis, "Any
  individuation built on sufficiency is relative to the target it is
  sufficient for". "Something further" is a free parameter: QUESTION-185's
  "perhaps a symmetry" and QUESTION-205's "a fixed kernel form, a
  short-range condition on the coarse Hamiltonian, or the preservation of
  named observables" are different conditions. Not filed.
- **QUESTION-203 and QUESTION-346.** QUESTION-203 asks how the S¹ model's
  average degree flows under geometric coarse-graining when the closure
  fails, and QUESTION-346 whether gradient search for the causal
  information bottleneck finds the partition by p(y | do(x)) at scale.
  Both are about what a coarse-graining keeps, and both were found
  unlinked with these three, but neither they nor their parent readings
  (THEORY-190; THEORY-1146 and THEORY-1125) name any of the three or their
  parents. They are left to the direct list.

## What it does not say

- That any information-theoretic coarse-graining finds renormalization
  variables where they were unknown, or fails to; all three are open.
- Anything with standing of its own.
