---
number: 1407
status: Active
formerly:
- THEORY-tmpmcxbv
title: 'Gopalan, Kolaitis, Maneva and Papadimitriou show that, for Boolean constraint languages with constants, deciding whether two solutions are joined by single-variable flips through solutions is either in polynomial time with components of linear diameter or PSPACE-complete with components of possibly exponential diameter, according to a property of the language that properly contains Schaefer''s tractable classes and does not follow the boundaries of Boolean clones, a boundary Schwerdtfeger later corrected slightly toward the hard side'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the twenty-seventh status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings), on the full
    readings of Gopalan et al. (NOTE-1584) and Schwerdtfeger (NOTE-1613):
    the title is a report, and each clause is confirmed by the text
    (Theorems 2.9 and 2.10; Lemma 4.2, "These containments are proper"; §1,
    "cut across Boolean clones"; Schwerdtfeger §3.2, the theorems restated
    with safely tight sets). The promote_when's demand for a reading of the
    SIAM version is dropped under ADR-065: the copy read is the authors'
    version of the same work, and no discrepancy in a statement is named;
    Schwerdtfeger's quotations of the SIAM statements agree but for the term
    "structurally" for "faithfully". promote_when deleted on promotion.
tags:
- mathematics
- operations-research
date: '2026-11-05'
source:
- LIT-2114
- LIT-2027
summary: >-
  Gopalan et al. (2009), LIT-2114, read in full in NOTE-1584, with
  Schwerdtfeger's correction (2014), LIT-2027, read in full in NOTE-1613.
  Active on both readings; the SIAM version was not compared, since no
  discrepancy in a statement is named. The lead added the work, not A. It
  does not say that algebra is irrelevant to navigation (polymorphisms do
  make every Schaefer language easy to navigate), nor anything about
  non-Boolean domains, other move sets or resource budgets.
---

# THEORY-1407: Gopalan, Kolaitis, Maneva and Papadimitriou show that, for Boolean constraint languages with constants, deciding whether two solutions are joined by single-variable flips through solutions is either in polynomial time with components of linear diameter or PSPACE-complete with components of possibly exponential diameter, according to a property of the language that properly contains Schaefer's tractable classes and does not follow the boundaries of Boolean clones, a boundary Schwerdtfeger later corrected slightly toward the hard side

## Source

Gopalan et al. (2009), [LIT-2114](../literature.d/LIT-2114.md), read in NOTE-1584; Schwerdtfeger
(2014), [LIT-2027](../literature.d/LIT-2027.md), read in NOTE-1613.

## What was actually shown

- **The dichotomy** (Theorems 2.9 and 2.10): for tight S, st-connectivity
  in linear time and diameter linear, because every component of a tight
  relation has a unique minimum, a unique maximum, or distances that never
  expand (§4); for S not tight, PSPACE-complete with diameter 2^Ω(√n), by
  faithful expression of every relation from S (Theorem 2.7) and
  PSPACE-hardness for 3-CNF (§§3.2–3.3, read in full).
- **Properly containing Schaefer** (Lemmas 4.1–4.2, read with proofs):
  idempotent polymorphisms of a relation pass to its components, so every
  Schaefer set is tight; positive 1-in-3 SAT is tight and not Schaefer.
- **Not the clone boundary** (§1): the authors say the clone method "does
  not appear to apply to connectivity, as the boundaries discovered here
  cut across Boolean clones."
- **The correction** (Schwerdtfeger, §3): constraints with a repeated
  variable can give a relation that is no longer componentwise
  bijunctive, OR-free or NAND-free ({001, 110, 111} is OR-free, and
  identifying its first two variables gives OR); the dichotomy holds with
  "safely tight" sets, closed under identification of variables, in place
  of tight ones. The hard side as Gopalan et al. state it stands
  (Schwerdtfeger §3.1); the easy side moves, RPSPA being tight and yet
  PSPACE-complete (his Example 11).

## What this does not say

- That a language's polymorphisms are irrelevant: they decide one
  direction, since Schaefer languages are all easy to navigate.
- Anything about non-Boolean domains, other adjacencies than single flips,
  formulas without constants (open for connectivity; for st-connectivity the
  authors report an extension, without proof, in §5), or average-case
  instances.
- Anything about resource-bounded navigation: there is no budget, only
  existence of a path and its length.
- That navigation is always harder than finding: for positive 1-in-3 SAT
  it is easier.

## Note of 2026-11-06: what holds it back

Both sources are Skimmed ([NOTE-1584](../notes.d/NOTE-1584.md), [NOTE-1613](../notes.d/NOTE-1613.md)). The hard side of the dichotomy, the faithful-expressibility proof and the PSPACE-hardness and exponential-diameter constructions of Gopalan et al. §§3.2–3.3, was read only in outline, and the corrected boundary rests on Schwerdtfeger's §3 with the rest of his §3.2 and his §4 unread. The missing result is a full reading of those sections; the SIAM comparison is owed only if that version differs in a statement, and [NOTE-1584](../notes.d/NOTE-1584.md) names only a change of term.

## Note of 2026-11-06: Claude, read

Both sources are now read in full (NOTE-1584, NOTE-1613), so the hold-back of the note above is met. The hard side's proofs, Lemmas 3.4 to 3.7, were read; the Turing-machine reduction was checked for the functional-graph argument, and Lemma 3.7's path was rebuilt by script (scratch/formal/gopalan_schwerdtfeger_checks.py). Promoted under ADR-065. Whether a navigation dichotomy holds beyond Boolean single-flip languages stays with QUESTION-376.
