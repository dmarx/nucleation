---
status: Active
title: "For any presheaf of propositions over a small category of contexts, a sieve-valued valuation satisfies the generalized functional-composition condition exactly when it is a subobject of that presheaf, and the construction runs unchanged in classical physics, where every microstate gives a global section yet truth values are still non-Boolean sieves; so the logic of the truth values is fixed by the base category, not by whether a presheaf has global sections"
version: 1
tags:
- quantum-foundations
- logic
- contextuality
- mathematics
date: '2026-10-16'
source:
- LIT-381
- LIT-389
corrects:
- THEORY-024
answers:
- QUESTION-055
summary: >-
  Butterfield & Isham (1998), [LIT-381](../literature.d/LIT-381.md), read in full in [NOTE-329](../notes.d/NOTE-329.md): Theorem
  4.1 proves that generalized FUNC is exactly naturality of ν : G → Ω, for
  any presheaf G of posets on any small category. In classical physics the
  value presheaf has a global section per microstate (3.6–3.7), yet the
  macrostate and microstate valuations are sieve-valued, and [NOTE-329](../notes.d/NOTE-329.md)
  shows excluded middle failing at a microstate. Isham & Butterfield
  (1999), [LIT-389](../literature.d/LIT-389.md) ([NOTE-334](../notes.d/NOTE-334.md)), adds that Ω is unique for a given topos and
  that a base with one arrow between any two objects gives two-valued
  logic. The choice of base, and so
  of the logic, remains free.
---

<!-- inactive-ok-file: THEORY-024 — Rejected; the account this one corrects, cited as such -->
<!-- inactive-ok-file: THEORY-037 — Proposed; named in Connections, not leaned on -->

# THEORY-tmpevmkz: For any presheaf of propositions over a small category of contexts, a sieve-valued valuation satisfies the generalized functional-composition condition exactly when it is a subobject of that presheaf, and the construction runs unchanged in classical physics, where every microstate gives a global section yet truth values are still non-Boolean sieves; so the logic of the truth values is fixed by the base category, not by whether a presheaf has global sections

## Source

Butterfield & Isham (1998; *IJTP* 1999), "A Topos Perspective on the
Kochen-Specker Theorem: II", [LIT-381](../literature.d/LIT-381.md), read in full in [NOTE-329](../notes.d/NOTE-329.md). Isham &
Butterfield (1999; *Found. Phys.* 2000), [LIT-389](../literature.d/LIT-389.md), read in full in [NOTE-334](../notes.d/NOTE-334.md).

## What was actually shown

**The general theorem ([LIT-381](../literature.d/LIT-381.md), Thm 4.1).** Let G be a presheaf of posets
with 0 and 1 on a small category C, and ν a sieve-valued valuation
assigning to each proposition d at A a sieve ν(A, d) on A. Then ν obeys
generalized FUNC, ν(B, G(f)(d)) = f*(ν(A, d)) (4.2), iff A ↦ ν(A, ·) is a
natural transformation G → Ω, that is, a subobject of G. The proof is the
one-line naturality check (4.4), and it is correct.

**The classical analogue ([LIT-381](../literature.d/LIT-381.md) §3).** Over the category M of measurable
functions on a classical state space, with arrows B̄ = f∘Ā, the value
presheaf Υ(Ā) = Ā(S) has global sections, one per microstate s,
γ^s_Ā = Ā(s) (3.6–3.7). Macrostates R still give sieve-valued valuations,
ν^R(A ∈ Δ) = {f | B̄(R) ⊆ f(Δ)} (3.10), and so does a single microstate
(3.15). [NOTE-329](../notes.d/NOTE-329.md) checked (3.10). [NOTE-329](../notes.d/NOTE-329.md) also shows, with constants
admitted as in the main text, that every false proposition gets a
non-empty, non-principal sieve whose pseudo-complement is empty, so
excluded middle fails at a classical microstate.

**What decides the logic.** A one-object base gives two truth values
([LIT-381](../literature.d/LIT-381.md) §2.2). [LIT-389](../literature.d/LIT-389.md) §2.2 argues that because the subobject classifier is
unique up to isomorphism, the many-valued logic is not arbitrary, and §3.1
observes that a base with exactly one arrow between any two objects gives
the ordinary true/false logic. [LIT-389](../literature.d/LIT-389.md) writes out the Heyting operations on
sieves for any small category (2.10)–(2.12): only S ∨ ¬S ≤ 1 holds.

**What could have come out otherwise.** Classical physics, having global
sections, could have yielded two-valued truth values under the same
construction. It does not: truth values remain sieves on its base.

## What this does not say

- **That the many-valued logic is non-arbitrary outright.** It is fixed
  given the topos. The choice of base category remains free, and the series
  itself moved from operators (O) and Boolean subalgebras (W) to von Neumann
  subalgebras (V). The arbitrariness is relocated, not removed ([NOTE-334](../notes.d/NOTE-334.md),
  C5).
- **That sieve values are forced.** [LIT-381](../literature.d/LIT-381.md)'s headline, that these are
  among "the most natural" valuations for any presheaf of propositions,
  rests on Theorem 4.1 and a partial-truth argument the authors say is not
  a deduction (§5.2).
- **That every base has a non-trivial logic, or a trivial one.** [LIT-389](../literature.d/LIT-389.md)'s
  remark that the presheaf of Hilbert spaces over (ℝ, ≤) has "essentially
  trivial" logic is wrong: that base is a non-trivial poset, and its sieves
  form a non-Boolean Heyting algebra ([NOTE-334](../notes.d/NOTE-334.md), C8).
- **Anything about probabilities.** Both papers set statistical content
  aside; quantum probabilities enter only through probability one.

## Connections

- **Corrects** [THEORY-024](THEORY-024.md), which held that Boolean logic returns when a
  presheaf acquires a global section or is sheafified. Its rejection already
  rests on Isham–Butterfield's statement that the Heyting algebra of sieves
  is fixed by the base ([LIT-325](../literature.d/LIT-325.md) §6) and on Isham 1997 ([LIT-390](../literature.d/LIT-390.md)). The
  classical case here is the series' own counterexample: global sections
  everywhere, sieve-valued truth anyway.
- **Answers in part** [QUESTION-055](../questions.d/QUESTION-055.md): if a communicative object is a presheaf
  over contexts, its truth values are sieves on the base, and their negation
  is the Heyting pseudo-complement the base fixes, not an orthocomplement.
  Which base the communicative object has is the part left open.
- The Heyting structure of propositions in the von Neumann-algebra form of
  the programme is [THEORY-037](THEORY-037.md). One Boolean context alone always has
  two-valued valuations, and the Kochen–Specker obstruction lies in how
  contexts overlap ([THEORY-020](THEORY-020.md)).
- How a quantum state's sieve-valued valuation is fixed by its supports on
  the von Neumann-algebra base is [THEORY-tmpqv891](THEORY-tmpqv891.md).
