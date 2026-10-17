---
number: 474
status: Active
formerly:
- THEORY-tmp9pyej
title: "Spekkens' toy bit theory, restricted to maximal knowledge and post-selected measurements, has a universal, sound and complete ZX-style graphical calculus whose phase-free rules and symplectic check-matrix conditions are exactly those of pure qubit stabilizer theory; the two calculi differ in the phase group, the Klein four-group against Z₄"
version: 1
tags:
- quantum-foundations
- mathematics
- contextuality
date: '2026-10-16'
source:
- LIT-054
summary: >-
  Backens & Duman (2014), [LIT-054](../literature.d/LIT-054.md), read in full in [NOTE-066](../notes.d/NOTE-066.md). A red–green
  spider calculus interpreted in the category of relations is universal and
  sound, and complete by Backens' stabilizer route. A binary matrix is a
  valid toy state iff SᵀJS = 0, the stabilizer condition (Lemma 3). The
  phase-free rules coincide with stabilizer ZX. That the phase group is the
  only categorical difference is cited, not shown, and completeness leans on
  analogy for several steps. The paper does no ψ-epistemic analysis and
  says nothing about which operational difference the phase group carries.
---

# THEORY-474: Spekkens' toy bit theory, restricted to maximal knowledge and post-selected measurements, has a universal, sound and complete ZX-style graphical calculus whose phase-free rules and symplectic check-matrix conditions are exactly those of pure qubit stabilizer theory; the two calculi differ in the phase group, the Klein four-group against Z₄

## Source

Backens & Duman (2014), [LIT-054](../literature.d/LIT-054.md), read in full in [NOTE-066](../notes.d/NOTE-066.md).

## What was actually shown

**The fragment.** Toy bits only, states of maximal knowledge (the analogue
of pure states), post-selected measurements and reversible transformations
(§1, §4). Each toy bit has four ontic states labelled by (X, Z) ∈ Z₂²; the
valid epistemic states know a commuting set of quadratures and are ignorant
otherwise (§2.1, from [LIT-007](../literature.d/LIT-007.md)). There are 24 reversible maps of one toy
bit, all of S₄ (§4.3).

**The calculus.** Green and red phased spiders and a colour-change node,
interpreted as relations; equalities are exact because the only scalars are
the empty and the full relation (§4.4). Universality follows from
Coecke–Edwards' generators (§4.3). Soundness is checked rule by rule by
computing the relations, by induction, and via Coecke–Edwards–Spekkens for
the spider rule (§4.4).

**Completeness (Thm 17).** Every state diagram rewrites to a reduced
graph-state normal form (Thms 10–11). Lemma 15 is proved in full (App. A.2).
Theorem 16, that a simplified pair represents the same state iff the
diagrams are identical, is given by analogy to Backens' stabilizer proof.
With map–state duality the calculus is complete for the fragment.

**The comparison.** A binary 2n×n matrix S is a valid toy state iff
SᵀJS = 0, and valid reversible transformations are exactly the Q with
QᵀJQ = J (Lemma 3, p. 15). These are the qubit stabilizer check-matrix
conditions. The phase-free rules (spiders, bialgebra, copy, colour change)
are identical to stabilizer ZX. The phase-bearing rules have analogues: the
11-commutation rule and ZX π-commutation are both instances of Eq. 40
(§4.5). The toy phase group is the Klein four-group {00, 01, 10, 11} under
XOR; the stabilizer one is Z₄ = {0, π/2, π, −π/2}.

**What could have come out otherwise.** Some toy-theory equation could have
needed a rule with no stabilizer counterpart, or completeness could have
failed for the relational semantics. Neither happened.

## What this does not say

- **That the phase group is proved to be the only difference.** "The only
  difference ... is the phase group" is a citation to Coecke–Edwards–Spekkens
  (§4.5; [NOTE-066](../notes.d/NOTE-066.md), C5). This paper exhibits the narrower correspondence
  above.
- **That the toy theory's locality or failure to violate Bell inequalities
  is explained by its being ψ-epistemic.** The paper asserts a relation in
  §1 with no argument (C7), and no Bell, GHZ or contextuality scenario is
  drawn. [NOTE-066](../notes.d/NOTE-066.md) answers the seeded question of which operational
  difference the phase group captures: none, in this paper.
- **That the graph-state theorems were proved for the toy theory
  independently.** They are transferred from Van den Nest–Dehaene–De Moor
  through the identical check-matrix formalism.
- **Mixed states, or qudits.** Less-than-maximal knowledge is left to a CPM
  construction not carried out; qudit completeness is open (§6).

## Connections

- [NOTE-066](../notes.d/NOTE-066.md) links the phase-group difference to [LIT-007](../literature.d/LIT-007.md) §IV.B, where the
  qubit stabilizer subtheory is contextual and its epistricted counterpart
  is not. Neither paper states the link.
- The same bit theory, with modes as systems, is the classical model of
  balanced interference in [THEORY-403](THEORY-403.md).
- The toy theory is ψ-epistemic in the overlap sense with product
  composition, so by PBR it cannot contain PBR's measurements
  ([NOTE-066](../notes.d/NOTE-066.md)'s inference; [THEORY-605](THEORY-605.md)).
