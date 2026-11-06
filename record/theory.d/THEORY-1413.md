---
number: 1413
status: Active
formerly:
- THEORY-tmpo2ib0
title: 'Schwerdtfeger shows that Gopalan, Kolaitis, Maneva and Papadimitriou''s connectivity dichotomies for Boolean constraint languages overlooked constraints in which a variable occurs twice, and that they hold once tight sets are replaced by safely tight ones, whose relations keep their component properties when variables are identified, which moves the boundary slightly toward the hard side'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the twenty-seventh status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings), on the full reading
    of Schwerdtfeger (NOTE-1613), which meets the promote_when: Example 11
    shows repeated variables breaking the easy side as stated (RPSPA is
    tight, yet st-ConnC and ConnC are PSPACE-complete), and §3.2 restates
    Theorems 2.7–2.10 with safely tight sets, Theorem 13 doing the same for
    connectivity. promote_when deleted on promotion. The trichotomy is read
    but gets no account of its own, by the same ruling.
tags:
- mathematics
- operations-research
date: '2026-11-05'
source:
- LIT-2027
summary: >-
  Schwerdtfeger (2014), LIT-2027, read in full in NOTE-1613. Active on that
  reading. The extended structural expressibility proof (Lemma 3.4) is the
  author's patch, checked at sketch level. It does not include the
  trichotomy for connectivity the paper also proves, which is read but not
  filed as an account, and it says nothing beyond Boolean domains with
  constants and single-flip moves.
---

# THEORY-1413: Schwerdtfeger shows that Gopalan, Kolaitis, Maneva and Papadimitriou's connectivity dichotomies for Boolean constraint languages overlooked constraints in which a variable occurs twice, and that they hold once tight sets are replaced by safely tight ones, whose relations keep their component properties when variables are identified, which moves the boundary slightly toward the hard side

## Source

Schwerdtfeger (2014), [LIT-2027](../literature.d/LIT-2027.md); read in NOTE-1613. The work
corrected is Gopalan et al. (2009), [LIT-2114](../literature.d/LIT-2114.md).

## What was actually shown

- **The gap**: {001, 110, 111} is OR-free, but identifying two variables
  yields OR (Example 7, checked by hand); a 4-ary relation with
  bijunctive components loses that property under identification
  (Example 8). Gopalan et al.'s Lemmas 3.2, 4.3 and 4.5 assume no
  repetition (§3.1–3.2). Example 7's relation is still safely tight, being
  safely componentwise bijunctive and safely NAND-free; the example that
  moves a set across the boundary is RPSPA (Example 11).
- **The repair**: express directly the relations that repetitions and
  constants produce (§3.1), extend Lemma 3.4 to sets that are not safely
  tight, and restate Theorems 2.7–2.10 with safely tight sets; Lemma 4.2
  is tightened so that Schaefer sets remain on the easy side (§3.2).

## What this does not say

- That Gopalan et al.'s dichotomy fails in form: it holds, with the
  boundary moved.
- The trichotomy for connectivity (P for CPSS sets, coNP-complete for the
  other safely tight sets, PSPACE-complete otherwise), which the paper
  proves in §4, read in NOTE-1613 but not filed as an account.
- Anything about formulas without constants, non-Boolean domains or other
  move sets.

## Note of 2026-11-06: Claude, read

Schwerdtfeger is now read in full (NOTE-1613), §4 and §5 included. Examples 7, 8, 10 and 11 were checked by script (scratch/formal/gopalan_schwerdtfeger_checks.py): Example 7's relation is OR-free and not safely OR-free, but stays safely tight through its other two properties; RPSPA is tight and fails all three safe properties. Promoted under ADR-065.
