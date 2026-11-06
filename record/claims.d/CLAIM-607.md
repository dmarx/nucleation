---
number: 607
status: Active
formerly:
- CLAIM-tmpp0p4d
title: 'Of two constraint languages both NP-complete to satisfy, navigation can be polynomial for one and PSPACE-complete for the other: deciding whether two solutions are joined by single flips through solutions is polynomial for positive 1-in-3 SAT and PSPACE-complete for positive NAE-3SAT'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the twenty-seventh status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings). Its note of
    2026-11-06 waited on a reading of the PSPACE-completeness proof for
    positive NAE-3SAT and of the tractable side for positive 1-in-3 SAT
    under the safely tight boundary. Gopalan et al. and Schwerdtfeger are
    now read in full (NOTE-1584, NOTE-1613), and THEORY-1407 and THEORY-1413
    are Active at the same review; the safe tightness of positive 1-in-3 SAT
    and the non-tightness of positive NAE-3SAT were checked by script
    (scratch/formal/gopalan_schwerdtfeger_checks.py). No objection is filed,
    and nothing in the record meets its defeated_if.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the cited classifications, so that deciding whether two
  solutions of a positive 1-in-3 SAT formula are joined by single flips is
  not polynomial, or that of a positive NAE-3SAT formula not
  PSPACE-complete.
tags:
- mathematics
- complex-systems
- operations-research
date: '2026-11-06'
line:
- realizability
- formal-apparatus
grounds:
- THEORY-1407
- THEORY-1413
complements:
- CLAIM-583
summary: >-
  Split off from [CLAIM-583](CLAIM-583.md) at the status review of 2026-11-06, keeping the
  clause that review dropped from its title. A's Response 3 §1,
  "compatibility equivalence doesn't imply computational equivalence", at
  the level of constraint languages: Gopalan et al. ([THEORY-1407](../theory.d/THEORY-1407.md)), with
  Schwerdtfeger's correction ([THEORY-1413](../theory.d/THEORY-1413.md)), give two languages equal in
  the complexity of finding a solution and opposite in the complexity of
  navigating between solutions. The record's own conditional
  demonstration from the cited classifications; Proposed while both
  readings are.
---

# CLAIM-607: Of two constraint languages both NP-complete to satisfy, navigation can be polynomial for one and PSPACE-complete for the other: deciding whether two solutions are joined by single flips through solutions is polynomial for positive 1-in-3 SAT and PSPACE-complete for positive NAE-3SAT

## The claim

A (Response 3 §1): "compatibility equivalence doesn't imply computational
equivalence." [CLAIM-583](CLAIM-583.md) shows it for two systems with one complex, move
rule and costs. This claim shows it one level up, for constraint languages.

**The version across languages** (Gopalan, Kolaitis, Maneva and
Papadimitriou; [NOTE-1584](../notes.d/NOTE-1584.md); [THEORY-1407](../theory.d/THEORY-1407.md)). For S = {R1/3}, positive
1-in-3 SAT, "This set is tight (actually, it is componentwise bijunctive),
but not Schaefer": satisfiability is NP-complete and deciding whether two
solutions are joined by single flips through solutions is polynomial. For
S = {RNAE}, positive NAE-3SAT, satisfiability is NP-complete and both
connectivity problems are PSPACE-complete. For languages that are not
tight the solution graph can have components of exponential diameter
(Theorem 2.10), A's "exponentially many operations"; Schwerdtfeger
([NOTE-1613](../notes.d/NOTE-1613.md); [THEORY-1413](../theory.d/THEORY-1413.md)) corrects the boundary to safely tight and
gives diameter 2^Ω(√n) beyond it. Equal in the complexity of finding a
solution, opposite in the complexity of navigating between solutions.

## What it does not say

- Anything beyond Boolean domains with constants and single-flip moves.
- That the two layers are unrelated: every Schaefer language is also easy
  to navigate ([THEORY-1407](../theory.d/THEORY-1407.md)).

## Note of 2026-11-06: what holds it back

[THEORY-1407](../theory.d/THEORY-1407.md) and [THEORY-1413](../theory.d/THEORY-1413.md) are Proposed: Gopalan et al. and Schwerdtfeger were skimmed ([NOTE-1584](../notes.d/NOTE-1584.md), [NOTE-1613](../notes.d/NOTE-1613.md)), and the hard side's proofs were read only in outline. A reading of the PSPACE-completeness proof for positive NAE-3SAT and of the tractable side for positive 1-in-3 SAT, under the safely tight boundary, would meet it.

## Note of 2026-11-06: Claude, read

Gopalan et al. and Schwerdtfeger are now read in full ([NOTE-1584](../notes.d/NOTE-1584.md), [NOTE-1613](../notes.d/NOTE-1613.md)). Positive 1-in-3 SAT is tight by the text (§2) and polynomial by Corollary 4.4's greedy flip, read with its proof; it is also safely tight in Schwerdtfeger's sense (Definition 4), checked by script (scratch/formal/gopalan_schwerdtfeger_checks.py), so the correction leaves it in P. Positive NAE-3SAT is not tight (checked by the same script), so not safely tight, and PSPACE-complete by Lemma 3.4, read in all four steps, with Lemma 3.6, read in full. The hold-back of the note above is met.
