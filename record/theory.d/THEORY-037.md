---
number: 37
status: Proposed
formerly:
- THEORY-tmpfaknx
promote_when: >-
  A held source that proves Sub_cl(Σ) over the abelian von Neumann
  subalgebras is a Heyting algebra, with implication written out and the
  pseudo-complement laws checked. A later Döring–Isham paper or a topos
  textbook read for the purpose would do. A restatement of Theorem 2.5, or
  the general fact that Sub(X) is Heyting in any topos, cannot settle it,
  because clopen sub-objects are not all sub-objects. It would be refuted by
  a pair of clopen sub-objects with no relative pseudo-complement in
  Sub_cl(Σ), or by a proof that daseinisation sends the orthocomplement to
  the Heyting negation.
title: 'In the topos programme quantum propositions form a distributive Heyting algebra, not an orthocomplemented lattice, and its negation is a pseudo-complement under which excluded middle can fail'
version: 1
tags:
- logic
- quantum-foundations
- contextuality
- mathematics
date: '2026-09-30'
source:
- LIT-335
- LIT-343
- LIT-325
summary: >-
  Döring & Isham (2007, II), [LIT-335](../literature.d/LIT-335.md) — daseinisation maps each projector
  injectively to a clopen sub-object of the spectral presheaf, with
  δ(P∨Q) = δ(P)∨δ(Q) but only δ(P∧Q) ⪯ δ(P)∧δ(Q). The orthocomplement is
  carried to inner daseinisation, not to ¬δ(P). That Sub_cl(Σ) is Heyting
  (Thm 2.5) is sketched: implication is not written out and the laws are
  not checked. Paper I ([LIT-343](../literature.d/LIT-343.md)) chooses intuitionistic deduction.
  Isham–Butterfield ([LIT-325](../literature.d/LIT-325.md)) state that the Heyting algebra is fixed by
  the base category.
---

# THEORY-037: In the topos programme quantum propositions form a distributive Heyting algebra, not an orthocomplemented lattice, and its negation is a pseudo-complement under which excluded middle can fail

## Source

Döring & Isham (2007), [LIT-335](../literature.d/LIT-335.md), Thms 2.1, 2.4, 2.5, eqs. 2.39, 2.44–2.45, 2.55–2.62 ([NOTE-292](../notes.d/NOTE-292.md)). Döring & Isham (2007), [LIT-343](../literature.d/LIT-343.md), §3.2 ([NOTE-277](../notes.d/NOTE-277.md)). Isham & Butterfield (1998), [LIT-325](../literature.d/LIT-325.md), §§3–6 ([NOTE-271](../notes.d/NOTE-271.md)).

## What was actually shown

Paper I gives the propositional language PL(S) the axioms of intuitionistic logic, chosen "since it allows a larger class of representations". Propositions are represented in a Heyting algebra. The classical representation is Boolean, and it validates the axiom ¬(A ε Δ) ⇔ A ε ℝ∖Δ. The authors advise against that axiom for non-Boolean targets, because it forces double-negation stability. Paper I also shows that P(H) with the orthocomplement cannot represent PL(S), because PL(S) proves distributivity and P(H) is not distributive (§3.2.4).

Paper II supplies the quantum representation. The contexts are the unital abelian von Neumann subalgebras V. The state object is the presheaf of their Gelfand spectra, which has no global elements, by Kochen–Specker. Daseinisation sends P to the least projector in each V above P, and so to a clopen sub-object of Σ (Thm 2.4). The map is injective (Thm 2.1). It preserves order and ∨, but for ∧ only δ(P∧Q) ⪯ δ(P)∧δ(Q), and strictly when Q = 1 − P (2.44–2.45). So the language may keep "A ε Δ₁ ∨ A ε Δ₂ ⇔ A ε Δ₁∪Δ₂", but not the conjunctive version (2.57–2.58). Negation is (¬S)_V = int ⋂_{V′⊆V}{λ : λ|_{V′} ∉ S_{V′}} (2.39), a pseudo-complement. The orthocomplement goes elsewhere: δ^o(1 − P) = 1 − δ^i(P), where δ^i is inner daseinisation into a different presheaf (2.62). So the negation of δ(P) is not δ(1 − P). Truth values are sieves.

Isham and Butterfield already have sieve-valued truth, and failures of strong conjunction and disjunction, in 1998. They state that the Heyting algebra of sieves "is precisely fixed by the structure of the base category" (§6).

## What this does not say

- That the Heyting structure on Sub_cl(Σ) is proved in the source. Thm 2.5 gives ∧, ∨ and ¬, leaves ⇒ to "straightforward extension", and does not check the Heyting laws ([NOTE-292](../notes.d/NOTE-292.md)). Hence Proposed.
- That the topos restores global points or a hidden-variable state space. Σ still has no global elements. What changes is the logic, and states become truth objects.
- That quantum probabilities are recovered. Sieve-valued truth from a state discards them ([LIT-325](../literature.d/LIT-325.md), spin-½ example).
- That a document using orthocomplement negation for concepts or propositions can cite this programme for its logic. The two are different logics.

## Connections

- [LIT-306](../literature.d/LIT-306.md) (Birkhoff–von Neumann) and the modular-law claim in this group: the orthocomplemented, non-distributive alternative that this programme replaces.
- [LIT-357](../literature.d/LIT-357.md) (Husimi) also keeps logic two-valued over states and rejects many-valued logics. It is a different answer to the same question ([NOTE-312](../notes.d/NOTE-312.md)).
- [LIT-276](../literature.d/LIT-276.md): a claim that the logic turns Boolean when a presheaf has a global section. It is rejected in this group.
