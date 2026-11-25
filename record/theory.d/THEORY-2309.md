---
number: 2309
status: Proposed
formerly:
- THEORY-tmpqj2d4
promote_when: >-
  Kleene's 1945 paper, or another primary or textbook source (Troelstra
  1973, Troelstra's handbook chapter "Realizability"), read and found to
  state the clauses as given here, in particular that a realizer of an
  existential is a pair of a witness and a realizer of its instance and a
  realizer of a true atomic sentence is 0, and the soundness theorem for
  Heyting arithmetic. A second survey repeating van Oosten does not count.
title: 'Realizers carry information, not proofs'
statement: >-
  In Kleene's 1945 realizability a realizer of an arithmetical sentence is
  information about how it holds, not a proof of it: for an existential, a
  witness paired with a realizer of its instance; for an implication or
  universal, a program; for a true atomic sentence, the number 0; the
  relation is classical and every theorem of Heyting arithmetic has a
  realizer, and the typed, proof-relevant form came later, with Kreisel
version: 1
tags:
- logic
- mathematics
- philosophy-of-mathematics
date: '2026-11-22'
source:
- 'LIT-3221'
corroborates:
- CLAIM-949
summary: >-
  Van Oosten (2002), [LIT-3221](../literature.d/LIT-3221.md), read in [NOTE-2420](../notes.d/NOTE-2420.md) as the stand-in for
  Kleene 1945 ([LIT-3213](../literature.d/LIT-3213.md), Unavailable): pp. 3–6 for the definition and
  the soundness theorem, p. 4 for information against proofs, p. 11 for
  Kreisel's typed realizability, p. 15 for the effective topos. Proposed
  because it rests on a survey of the paper, not the paper. It corroborates
  [CLAIM-949](../claims.d/CLAIM-949.md)'s reading of Kleene's realizer as a realization with its
  witness kept, and [ARG-244](../arguments.d/ARG-244.md) says how far.
---
<!-- inactive-ok-file: CLAIM-949 LIT-3213 ARG-244 — Proposed or Unavailable; the claim this bears on, the work it reports, and the argument that weighs it -->

# THEORY-2309: Realizers carry information, not proofs

## Source

Van Oosten (2002), [LIT-3221](../literature.d/LIT-3221.md), §1.1–1.6 and §2.1, pp. 3–15 of the
author's manuscript; read in [NOTE-2420](../notes.d/NOTE-2420.md). It stands in for Kleene (1945),
[LIT-3213](../literature.d/LIT-3213.md), which was not read.

## What was shown

**The clauses** (p. 5). By induction on a sentence of arithmetic: "n
realizes F, where F is an atomic sentence, if and only if n = 0 and F is
true"; a conjunction by a pair of realizers; a disjunction by a tagged
realizer of one disjunct; an implication by the index of a partial
recursive function taking realizers of the antecedent to realizers of the
consequent; "n realizes an existential statement ∃xφ(x) if and only if
n = ⟨m, k⟩ and k realizes φ(m̄)"; a universal by the index of a total
recursive function.

**Soundness** (p. 6). Every theorem of HA has a realizer; in the glued
form, a realizable sentence lies in the set P glued on. Kleene drew the
weak Church's rule from it, and the underivability of double-negation
shift.

**Information, not proofs** (p. 4). Realizability "is designed to handle
“information” about formulas rather than proofs"; Kleene found that
"Heyting's proof-interpretation failed to help me to my goal" (1973, as
quoted). The relation is stated in classical terms, "read and checked by
the classical mathematician".

**Typed, later** (p. 11). Kreisel's modified realizability (1959) types
each formula's realizers by its logical form, "predates the slogan
“formulae as types” … by 10 years", and was later used to interpret
Martin-Löf's type theory.

**A model** (p. 15). In Hyland's effective topos the truth definition for
arithmetic "is equivalent to Kleene's 1945-realizability".

## What this does not say

- **That a realizer is a proof or certificate.** At a true atomic sentence
  it is 0, and an almost negative formula's realizer can be computed from
  the formula (p. 9). What it carries beyond truth is witnesses, choices
  and programs.
- **That realizability matches intuitionistic logic.** Some realizable
  propositional formulas are not intuitionistically provable (Rose 1953,
  p. 8).
- **Anything in Kleene's own words** beyond the one passage the survey
  quotes (n. 7). The clauses are van Oosten's restatement.
