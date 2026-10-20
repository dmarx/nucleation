---
number: 223
status: 'Open'
formerly:
- QUESTION-tmpttlk1
title: "Is Ince's common change in surprisal a correct redundancy measure: is it continuous, does it agree with a redundancy fixed by mechanism where rivals with non-negative atoms do not, may unique information depend on the source-source marginal, and can a modified sign rule restore subset equality?"
version: 1
tags:
- information-theory
- complex-systems
date: '2026-10-20'
line: 'formal-apparatus'
summary: >-
  Filed when the promotion audit (batch 056, [ADR-047](../decisions.d/ADR-047.md) v2) corrected and
  promoted [THEORY-714](../theory.d/THEORY-714.md). What I_ccs is and which axioms it keeps is now
  settled, including that it fails subset equality. Whether it is the
  right redundancy measure is not: that was the old promote_when, and it
  moves here.
answered_by:
- THEORY-tmpomt6b
---

# QUESTION-223: Is Ince's common change in surprisal a correct redundancy measure: is it continuous, does it agree with a redundancy fixed by mechanism where rivals with non-negative atoms do not, may unique information depend on the source-source marginal, and can a modified sign rule restore subset equality?

## Why it is a question

[THEORY-714](../theory.d/THEORY-714.md) now states what Ince's I_ccs ([LIT-1201](../literature.d/LIT-1201.md)) is and what it
does. It is symmetric and self-redundant, it satisfies the independent
identity property, and it fails Harder et al.'s identity, monotonicity
and subset equality. Everything there is derived. What is not settled is
whether it measures redundancy correctly, which is what the account's
former promote_when asked:

- **Continuity.** Ince conjectures it and checks it only locally in the
  examples. A sign rule makes the measure piecewise, so continuity is not
  automatic.
- **An operational test.** A system whose redundancy is fixed by
  mechanism, accepted by both sides of the dispute (a shared bit copied
  to every source, say), on which I_ccs agrees and a rival with
  non-negative atoms does not.
- **The source-source marginal.** Ince's P̂ fixes Q(A1…An) and so lets
  unique information depend on it. Bertschinger et al. ([LIT-1162](../literature.d/LIT-1162.md)) hold
  that it may not. An argument settling which is right decides between
  I_ccs and I_broja.
- **Subset equality.** The audit found it fails for I_ccs as defined,
  because the sign rule compares a source with a source containing it.
  Ince argues that subset equality, not monotonicity, is what licenses
  the redundancy lattice, so the failure matters for the measure's own
  rationale. Would a sign rule that skips sources contained in others
  restore it, and at what cost to the other properties?

An answer is a proof, a counterexample, or an operational case of the
kind above. Further examples judged by intuition do not settle it, nor
does agreement on systems where every measure agrees.
