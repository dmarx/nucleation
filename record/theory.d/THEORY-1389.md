---
number: 1389
status: Active
formerly:
- THEORY-tmpelyg5
title: "Connelly and Whiteley prove that for tensegrity frameworks first-order rigidity implies prestress stability, which implies second-order rigidity, which implies rigidity, give bar-framework examples that none of these implications reverses, and prove that whether a first-order flex extends to second order is decided by a Farkas-type test on the framework's proper self-stresses"
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    At the twenty-ninth status review, at the status review's ruling (the
    owner delegated these rulings; ADR-065), on NOTE-1588 v2, which reads
    the proofs of the hierarchy and of the stress test: promoted Proposed
    → Active, and promote_when deleted. Its second alternative ("or the
    proofs of §§4–5 skipped in this reading are read and found to
    establish them") is met. Narrowed (kind 3): the paper proves the three
    implications and the test, but shows that the converses fail by
    examples, one of them (Figure 16d) a drawing. The old title was
    "Connelly and Whiteley prove that for tensegrity frameworks first-order
    rigidity implies prestress stability, which implies second-order
    rigidity, which implies rigidity, that none of these implications
    reverses even for bar frameworks, and that whether a first-order flex
    extends to second order is decided by a Farkas-type test on the
    framework's proper self-stresses". Corrected in the body: the test is
    Corollary 5.2.1, not Theorem 4.3.1, and Figure 9b is a tensegrity
    example.
- version: 3
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-383 and QUESTION-389, at the reading review of
    2026-11-11 (by question, ADR-091). QUESTION-383 names it where stress
    decides, the order of first-order rigidity, prestress stability,
    second-order rigidity and rigidity; QUESTION-389 as "Loads that decide
    motions": a first-order flex extends to second order "exactly when no
    proper self-stress gives it positive energy". No other change.
tags:
- mathematics
- natural-sciences
date: '2026-11-05'
source:
- LIT-2080
summary: >-
  Connelly and Whiteley (1996), [LIT-2080](../literature.d/LIT-2080.md), read in [NOTE-1588](../notes.d/NOTE-1588.md) (all of
  §§1–4, §§5.1–5.3 and §6; §§5.4–5.6 and Appendix A.2–A.3 skipped). Active:
  the three implications and the stress test are proved in the text read,
  and the converses are shown by examples, two with calculations and one, a
  rigid bar framework that is not second-order rigid (Figure 16d), as a
  drawing. It is about local rigidity, not global rigidity, and it does not
  say that every first-order flex of a non-rigid framework extends to a
  finite motion.
bears_on:
- QUESTION-383
- QUESTION-389
---

# THEORY-1389: Connelly and Whiteley prove that for tensegrity frameworks first-order rigidity implies prestress stability, which implies second-order rigidity, which implies rigidity, give bar-framework examples that none of these implications reverses, and prove that whether a first-order flex extends to second order is decided by a Farkas-type test on the framework's proper self-stresses

## Source

Connelly and Whiteley (1996), [LIT-2080](../literature.d/LIT-2080.md); read in [NOTE-1588](../notes.d/NOTE-1588.md).

## What was actually shown

- **The hierarchy** (abstract; Proposition 3.3.3, Theorems 4.4.1 and
  4.3.1, proofs read): "We demonstrate a hierarchy of
  rigidity--first-order rigidity implies prestress stability implies
  second-order rigidity implies" rigidity, for any tensegrity framework.
- **Irreversibility** (abstract): "Examples show that none of these
  implications are reversible, even for bar frameworks." Bar witnesses:
  Figure 7 (prestress stable, not first-order rigid), Example 5.3.1 and
  Figure 18b (second-order rigid, not prestress stable; the first
  calculated, and recomputed in scratch/formal/connelly_whiteley_531_check.py),
  Figure 16d (rigid with a nontrivial second-order flex, drawn only).
  Figure 9b is the tensegrity case: rigid and second-order rigid, not
  prestress stable (§3.5, Remark 4.4.1).
- **The stress test** (§1.4; Corollary 5.2.1, proof read): a first-order
  flex p′ extends to second order if and only if p′ᵀΩp′ ≤ 0 for every
  proper self-stress, by "a special case of the "Farkas alternative""
  (Proposition 5.1.3).
- **Its reach** (§6.2): used to prove Roth's conjecture, and to show that
  bars that add proper self-stresses can make a framework with a
  first-order flex "even prestress stable".

## What this does not say

- Anything about global rigidity: "Neither infinitesimal rigidity nor
  global rigidity implies the other" (§1.5).
- That a first-order flex that does extend to second order extends to a
  continuous motion, beyond independent bar frameworks (Proposition 6.1.1).
- That second-order rigidity and prestress stability coincide in general;
  they do only with a one-dimensional cone of flexes or of proper
  self-stresses (Proposition 5.3.1).
