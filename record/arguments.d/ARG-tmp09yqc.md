---
status: Rejected
title: "Simon's near-decomposability carries a finite correlation length to approximately autonomous levels of description, so a system off criticality divides into levels as a nearly decomposable system does"
version: 1
form: source
grounds:
- THEORY-661
concludes:
- CLAIM-478
tags:
- complex-systems
- natural-sciences
date: '2026-11-21'
line:
- formal-apparatus
- distributed-agency
summary: >-
  A13 §9 of the exchange "Rich Get Richer Power Laws" asserts that
  "Different levels become approximately autonomous when the details of
  smaller scales become irrelevant to the behavior of larger ones", and
  that critical systems are exceptional because "that separation becomes
  less complete". The note of 2026-11-21 on CLAIM-478 puts this as a
  bridge from a finite correlation length to near-decomposability in
  Simon's sense (THEORY-661), and finds it unshown. This is that
  inference, and it fails: Simon's condition is weak interaction between
  blocks, which any short-range system satisfies for large blocks,
  critical or not, while a correlation length measures statistical
  dependence. The bridge goes through dynamic scaling, which the reading
  does not hold. Rejected. The bridge is A's (the other assistant in the
  exchange "Rich Get Richer Power Laws", A13); the verdict is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-478 CLAIM-626 CLAIM-tmpjbee7 — Proposed, held or filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->

# ARG-tmp09yqc: Simon's near-decomposability carries a finite correlation length to approximately autonomous levels of description, so a system off criticality divides into levels as a nearly decomposable system does

## The inference

A13 §9: "Renormalization suggests an answer. Different levels become
approximately autonomous when the details of smaller scales become
irrelevant to the behavior of larger ones. Critical systems are
exceptional because that separation becomes less complete: correlations
persist across scales, and the normal boundaries between descriptions
become harder to draw." So characteristic scales would explain "*when*
relatively independent levels of description can emerge and *when* they
cannot".

Put in the record's terms (the note of 2026-11-21 on CLAIM-478): with a
finite correlation length ξ, a system is nearly decomposable into blocks
larger than ξ, and THEORY-661 then gives Simon's result, fast dynamics
within blocks and slow aggregate dynamics between them, which is a
separation of levels; at a critical point ξ is unbounded and the
separation fails.

## Critical questions

- **Does the work say this, read in context?** No. THEORY-661's condition
  is on interaction: "the matrix of interaction coefficients is
  block-diagonal with off-diagonal entries below a small ε", for a
  partition the theorem takes as given. Its conclusion is about time
  scales. It says nothing about correlation length, and the reading notes
  that the theorem "takes the partition as given" and that the open
  statement the record holds gives "no rate in ε".
- **Is it said within the scope the claim needs?** No. The step needs
  ξ to decide whether the interaction condition holds, and it does not.
  For a lattice system with short-range coupling, two adjacent blocks of
  side L in d dimensions share about L^(d−1) bonds against about dL^d
  inside each, so the relative coupling between blocks falls as 1/L for
  any coupling strength and any temperature, at T_c as elsewhere. By
  Simon's criterion such a system is nearly decomposable into large
  blocks whether or not it is critical. What a correlation length
  measures is different: the statistical dependence between blocks, which
  decays beyond ξ and does not at T_c. Weak interaction and weak
  dependence are different conditions, and the reading holds only the
  first.
- **Does the claim lean on the reading for more than the reading holds?**
  Yes, at one step. The separation the note wants does exist off
  criticality, but it comes from dynamics: a block of side L ≫ ξ relaxes
  internally in a time of order ξ^z, its aggregate on a longer time set by
  L, and at T_c the internal time grows as L^z with the block, so no block
  size gives a window. That is dynamic scaling, τ ∝ ξ^z, which A17 §5
  states and the record holds only as a standard result; and the slowing
  is of the collective mode, the case CLAIM-626 separates from the others.
  THEORY-661 contributes the shape of the conclusion, fast within and
  slow between, and not the premise that puts a finite-ξ system in its
  scope.

## Verdict

Rejected as an inference from THEORY-661: Simon's near-decomposability
does not carry a finite correlation length to autonomous levels, since its
interaction condition is met by short-range systems at criticality too.
The spatial counterpart of CLAIM-478 that A13 §9 suggests may still hold,
through dynamic scaling; that route needs its own grounds. CLAIM-478 itself,
about rate differences, is untouched, and CLAIM-tmpjbee7 states what
criticality does remove.
