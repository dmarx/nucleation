---
number: 1407
status: Proposed
formerly:
- THEORY-tmpmcxbv
promote_when: >-
  A reading of the SIAM version and of Schwerdtfeger's JSAT paper confirms
  the dichotomy for st-connectivity and diameter with the corrected
  boundary (safely tight), and confirms that the authors state the boundary
  cuts across Boolean clones.
title: 'Gopalan, Kolaitis, Maneva and Papadimitriou show that, for Boolean constraint languages with constants, deciding whether two solutions are joined by single-variable flips through solutions is either in polynomial time with components of linear diameter or PSPACE-complete with components of possibly exponential diameter, according to a property of the language that properly contains Schaefer''s tractable classes and does not follow the boundaries of Boolean clones, a boundary Schwerdtfeger later corrected slightly toward the hard side'
version: 1
tags:
- mathematics
- operations-research
date: '2026-11-05'
source:
- LIT-2114
- LIT-2027
summary: >-
  Gopalan et al. (2009), [LIT-2114](../literature.d/LIT-2114.md), skimmed in [NOTE-1584](../notes.d/NOTE-1584.md), with
  Schwerdtfeger's correction (2014), [LIT-2027](../literature.d/LIT-2027.md), skimmed in
  [NOTE-1613](../notes.d/NOTE-1613.md). Proposed: the hard side's proofs were read only in
  outline, the SIAM version was not compared, and Schwerdtfeger's own
  proofs were not read. The lead added the work, not A. It does not say
  that algebra is irrelevant to navigation (polymorphisms do make every
  Schaefer language easy to navigate), nor anything about non-Boolean
  domains, other move sets or resource budgets.
---
<!-- inactive-ok-file: NOTE-1584 NOTE-1613 — Skimmed; the readings this account rests on, cited from the reading of Gopalan et al. (2009) as open -->

# THEORY-1407: Gopalan, Kolaitis, Maneva and Papadimitriou show that, for Boolean constraint languages with constants, deciding whether two solutions are joined by single-variable flips through solutions is either in polynomial time with components of linear diameter or PSPACE-complete with components of possibly exponential diameter, according to a property of the language that properly contains Schaefer's tractable classes and does not follow the boundaries of Boolean clones, a boundary Schwerdtfeger later corrected slightly toward the hard side

## Source

Gopalan et al. (2009), [LIT-2114](../literature.d/LIT-2114.md), skimmed in [NOTE-1584](../notes.d/NOTE-1584.md); Schwerdtfeger
(2014), [LIT-2027](../literature.d/LIT-2027.md), skimmed in [NOTE-1613](../notes.d/NOTE-1613.md).

## What was actually shown

- **The dichotomy** (Theorems 2.9 and 2.10): for tight S, st-connectivity
  in linear time and diameter linear, because every component of a tight
  relation has a unique minimum, a unique maximum, or distances that never
  expand (§4); for S not tight, PSPACE-complete with diameter 2^Ω(√n), by
  faithful expression of every relation from S (Theorem 2.7) and
  PSPACE-hardness for 3-CNF (§3.3, skimmed).
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
  of tight ones.

## What this does not say

- That a language's polymorphisms are irrelevant: they decide one
  direction, since Schaefer languages are all easy to navigate.
- Anything about non-Boolean domains, other adjacencies than single flips,
  formulas without constants (open for connectivity), or average-case
  instances.
- Anything about resource-bounded navigation: there is no budget, only
  existence of a path and its length.
- That navigation is always harder than finding: for positive 1-in-3 SAT
  it is easier.
