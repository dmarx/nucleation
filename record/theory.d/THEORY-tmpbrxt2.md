---
status: Active
title: "From core mereology, classical extensional mereology (GEM) is reached by exactly three pairings of a decomposition principle with an unrestricted-sum principle: Supplementation with Sum2, Strong Supplementation with Sum3, and Complementation with Sum1; Supplementation with Sum3, the pairing given by Simons (1987), does not yield it, because which definition of 'sum' is used decides which decomposition axiom is needed"
version: 1
tags:
- mereology
- mathematics
- logic
date: '2026-10-16'
source:
- LIT-124
summary: >-
  Varzi, SEP "Mereology" (2003, revised June 2026), [LIT-124](../literature.d/LIT-124.md), read in full in
  [NOTE-163](../notes.d/NOTE-163.md). A result the entry reports with citations (Hovda 2009; Cotnoir
  and Varzi 2019) and a countermodel (its Fig. 4; Pietruszczak 2000a,
  Pontow 2004), and which corrects Simons (1987), Casati and Varzi (1999)
  and the entry's own 2003 edition. The record has not checked the proofs.
  It is stated for first-order theories with a single primitive P and
  infinitary principles as axiom schemas, and it is a fact about axiom
  systems: it does not say classical mereology is true of anything.
---
<!-- inactive-ok-file: THEORY-017 THEORY-tmpnan16 THEORY-tmpr3k41 — Proposed; neighbouring accounts named for comparison; this result does not rest on them -->

# THEORY-tmpbrxt2: From core mereology, classical extensional mereology (GEM) is reached by exactly three pairings of a decomposition principle with an unrestricted-sum principle: Supplementation with Sum2, Strong Supplementation with Sum3, and Complementation with Sum1; Supplementation with Sum3, the pairing given by Simons (1987), does not yield it, because which definition of 'sum' is used decides which decomposition axiom is needed

## Source

Achille Varzi, "Mereology", *Stanford Encyclopedia of Philosophy*, [LIT-124](../literature.d/LIT-124.md),
first published 2003, substantive revision of 27 June 2026, read in full in
[NOTE-163](../notes.d/NOTE-163.md) (all sections and all 48 notes; the figures through their captions).

## What was actually shown

**The ladder.** Core Mereology M is (P.1) Reflexivity, (P.2) Transitivity and
(P.3) Antisymmetry over a primitive P. MM adds (P.4) Supplementation,
PPxy → ∃z(Pzy ∧ ¬Ozx). EM adds (P.5) Strong Supplementation,
¬Pyx → ∃z(Pzy ∧ ¬Ozx). GEM is EM with every instance of Unrestricted Sum3,
the systems of Leśniewski and Leonard–Goodman, "also known as Classical
Mereology". The same theory is MM with Unrestricted Sum2, since (P.5) is then
derivable. EM or MM with Sum1 is strictly weaker (Fig. 8).

**Three sums (§4.2).** S1 is a minimal upper bound. S2, after Leśniewski,
Tarski and Lewis, requires every part of z to overlap x or y. S3, after
Leonard–Goodman, Simons and Casati–Varzi, requires z to overlap exactly what
overlaps x or y. Given Transitivity, S2 implies S3; S3 implies S2 only with
(P.5).

**Three routes and one failure (§4.4).** From M the only adequate pairings are
Supplementation with Sum2, Strong Supplementation with Sum3, and
Complementation with Sum1 (Hovda 2009; Cotnoir and Varzi 2019). The Fig. 4
model satisfies Supplementation and Unrestricted Sum3 and is not a model of
GEM (Pietruszczak 2000a; Pontow 2004). That contradicts Simons (1987: 37),
Casati and Varzi (1999) and the entry's 2003 edition, corrected in Spring 2009
(note 29).

**Related results the entry reports.**

- Given (P.1) and (P.2), Supplementation entails Antisymmetry. MM with products
  for overlappers already contains EM (Simons 1987: 30f).
- GEM is finitely axiomatizable in first-order logic (Tsai 2018) and decidable
  (Tsai 2013a), whereas M, MM and EM are undecidable.
- GEM's parthood is "virtually isomorphic" to inclusion on the non-empty subsets
  of a set. Precisely, every model is isomorphic to a Boolean subalgebra, not
  necessarily complete, of a complete Boolean algebra with zero removed (note
  34; Pontow and Schubert 2006, Thm 34).
- Atomistic GEM with κ atoms has 2^κ − 1 elements, so it has models of sizes 1,
  3, 7, 15 and 2^ℵ₀ and none of size 2, 4, 6 or ℵ₀.
- Every GEM model has a top element, so GEM is incompatible with junk.

**What could have come out otherwise.** Simons's pairing could have sufficed. A
single countermodel shows it does not.

## What this does not say

- **That GEM is the right mereology.** The result is about which axiom sets
  coincide. The entry treats every principle beyond the core, and the core
  itself, as contested ([THEORY-tmpnan16](THEORY-tmpnan16.md)).
- **That the result holds outside its setting.** It is stated in first-order
  logic with identity and a single primitive P, with infinitary principles as
  schemas over open formulas, which cover only denumerably many specifiable
  sets. Note 9 concedes that free logic or plural quantification might suit
  sums better.
- **That "sum" and "fusion" are interchangeable.** Some authors reserve "sum"
  for S2 and "fusion" for S3 (note 23). A claim that something is the "sum" of
  some parts is not determinate until the definition is fixed.
- **That the record has checked it.** The entry gives citations and at most
  one-line derivations, and [NOTE-163](../notes.d/NOTE-163.md) did not check the sources.
- **Anything about quantum or systems "mereology".** Note 18 excludes quantum
  part–whole formalisms, and note 1 the systems-theory and ecological senses.

## Connections

- Whether mereology's axioms are meaning postulates is [THEORY-tmpnan16](THEORY-tmpnan16.md), from
  the same entry.
- Fiat and bona fide boundaries ([LIT-1024](../literature.d/LIT-1024.md), [THEORY-tmpr3k41](THEORY-tmpr3k41.md)) add topology to a
  mereology of this kind, with extensional mereology and unrestricted fusion
  taken for simplicity.
- Hilbert-space factorization ([THEORY-017](THEORY-017.md)) is the quantum part–whole question
  the entry leaves out.
