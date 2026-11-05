---
number: 1413
status: Proposed
formerly:
- THEORY-tmpo2ib0
promote_when: >-
  A reading of §3 of the JSAT version, or of arXiv 1312.4524, confirms
  that constraints with repeated variables break the easy side of Gopalan
  et al.'s dichotomies as stated and that the dichotomies for
  st-connectivity, connectivity and diameter hold with safely tight sets
  in place of tight ones.
title: 'Schwerdtfeger shows that Gopalan, Kolaitis, Maneva and Papadimitriou''s connectivity dichotomies for Boolean constraint languages overlooked constraints in which a variable occurs twice, and that they hold once tight sets are replaced by safely tight ones, whose relations keep their component properties when variables are identified, which moves the boundary slightly toward the hard side'
version: 1
tags:
- mathematics
- operations-research
date: '2026-11-05'
source:
- LIT-2027
summary: >-
  Schwerdtfeger (2014), [LIT-2027](../literature.d/LIT-2027.md), skimmed in [NOTE-1613](../notes.d/NOTE-1613.md): the
  abstract, §1, the definitions and §3 through the restated theorems read,
  §4–5 not. Proposed: the extended structural expressibility proof (Lemma
  3.4) was read only as amended, not in full. It does not include the
  trichotomy for connectivity the paper also proves, whose proof was not
  read, and it says nothing beyond Boolean domains with constants and
  single-flip moves.
---
<!-- inactive-ok-file: NOTE-1613 — Skimmed; the reading this account rests on, cited from the reading of Schwerdtfeger (2014) as open -->

# THEORY-1413: Schwerdtfeger shows that Gopalan, Kolaitis, Maneva and Papadimitriou's connectivity dichotomies for Boolean constraint languages overlooked constraints in which a variable occurs twice, and that they hold once tight sets are replaced by safely tight ones, whose relations keep their component properties when variables are identified, which moves the boundary slightly toward the hard side

## Source

Schwerdtfeger (2014), [LIT-2027](../literature.d/LIT-2027.md); skimmed in [NOTE-1613](../notes.d/NOTE-1613.md). The work
corrected is Gopalan et al. (2009), [LIT-2114](../literature.d/LIT-2114.md).

## What was actually shown

- **The gap**: {001, 110, 111} is OR-free, but identifying two variables
  yields OR (Example 7, checked by hand); a 4-ary relation with
  bijunctive components loses that property under identification
  (Example 8). Gopalan et al.'s Lemmas 3.2, 4.3 and 4.5 assume no
  repetition (§3.1–3.2).
- **The repair**: express directly the relations that repetitions and
  constants produce (§3.1), extend Lemma 3.4 to sets that are not safely
  tight, and restate Theorems 2.7–2.10 with safely tight sets; Lemma 4.2
  is tightened so that Schaefer sets remain on the easy side (§3.2).

## What this does not say

- That Gopalan et al.'s dichotomy fails in form: it holds, with the
  boundary moved.
- The trichotomy for connectivity (P for CPSS sets, coNP-complete for the
  other safely tight sets, PSPACE-complete otherwise), which the paper
  proves in §4, not read here.
- Anything about formulas without constants, non-Boolean domains or other
  move sets.
