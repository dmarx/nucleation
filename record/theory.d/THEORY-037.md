---
number: 37
status: Active
formerly:
- THEORY-tmpfaknx
title: 'In the topos programme quantum propositions form a distributive Heyting algebra, not an orthocomplemented lattice, and its negation is a pseudo-complement under which excluded middle can fail'
version: 3
history:
- version: 2
  date: '2026-10-16'
  note: >-
    Presupposes THEORY-619, Butterfield and Isham's proof that
    coarse-graining is the direct image of clopen spectral regions, which
    is what makes each daseinised projector a clopen sub-object. Two later
    readings, LIT-378 and LIT-382, are named in Connections: neither writes
    out the implication or checks the Heyting laws, so the promotion
    condition is still unmet.
- version: 3
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, carrying out
    the promotion audit's decision (record/promotion-audit/decisions/THEORY-037.yaml,
    batch 009, ADR-047). The promote_when asked for a held source proving
    that Sub_cl(Σ) is Heyting, with the laws checked, and ruled out the
    general fact that Sub(X) is Heyting in a topos. Under ADR-047 v2 (the
    owner's rule of 2026-10-19), a checked step-by-step re-derivation meets
    a request for a proof the record does not hold. The re-derivation, now
    in the note of 2026-10-19 below, is internal to Sub_cl(Σ) and uses the
    extremal disconnectedness of each Σ_V, so it meets the promote_when's
    objection. Sub_cl(Σ) is a frame, hence a complete Heyting algebra. Its
    pseudo-complement is (2.39). In the ℂ² case excluded middle fails. The
    restriction-stability of the interior in part 2 rests on NOTE-292's
    check. The promote_when is removed. The claim is unchanged.
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
  (Thm 2.5) is sketched in the source, and the record re-derives it: each
  Σ_V is extremally disconnected, so Sub_cl(Σ) is a frame. Paper I ([LIT-343](../literature.d/LIT-343.md)) chooses intuitionistic deduction.
  Isham–Butterfield ([LIT-325](../literature.d/LIT-325.md)) state that the Heyting algebra is fixed by
  the base category.
answers:
- QUESTION-247
presupposes:
- THEORY-619
---
<!-- inactive-ok-file: LIT-276 — Rejected; named in Connections as the claim this group rejects, not leaned on -->

# THEORY-037: In the topos programme quantum propositions form a distributive Heyting algebra, not an orthocomplemented lattice, and its negation is a pseudo-complement under which excluded middle can fail

## Source

Döring & Isham (2007), [LIT-335](../literature.d/LIT-335.md), Thms 2.1, 2.4, 2.5, eqs. 2.39, 2.44–2.45, 2.55–2.62 ([NOTE-292](../notes.d/NOTE-292.md)). Döring & Isham (2007), [LIT-343](../literature.d/LIT-343.md), §3.2 ([NOTE-277](../notes.d/NOTE-277.md)). Isham & Butterfield (1998), [LIT-325](../literature.d/LIT-325.md), §§3–6 ([NOTE-271](../notes.d/NOTE-271.md)).

## What was actually shown

Paper I gives the propositional language PL(S) the axioms of intuitionistic logic, chosen "since it allows a larger class of representations". Propositions are represented in a Heyting algebra. The classical representation is Boolean, and it validates the axiom ¬(A ε Δ) ⇔ A ε ℝ∖Δ. The authors advise against that axiom for non-Boolean targets, because it forces double-negation stability. Paper I also shows that P(H) with the orthocomplement cannot represent PL(S), because PL(S) proves distributivity and P(H) is not distributive (§3.2.4).

Paper II supplies the quantum representation. The contexts are the unital abelian von Neumann subalgebras V. The state object is the presheaf of their Gelfand spectra, which has no global elements, by Kochen–Specker. Daseinisation sends P to the least projector in each V above P, and so to a clopen sub-object of Σ (Thm 2.4). The map is injective (Thm 2.1). It preserves order and ∨, but for ∧ only δ(P∧Q) ⪯ δ(P)∧δ(Q), and strictly when Q = 1 − P (2.44–2.45). So the language may keep "A ε Δ₁ ∨ A ε Δ₂ ⇔ A ε Δ₁∪Δ₂", but not the conjunctive version (2.57–2.58). Negation is (¬S)_V = int ⋂_{V′⊆V}{λ : λ|_{V′} ∉ S_{V′}} (2.39), a pseudo-complement. The orthocomplement goes elsewhere: δ^o(1 − P) = 1 − δ^i(P), where δ^i is inner daseinisation into a different presheaf (2.62). So the negation of δ(P) is not δ(1 − P). Truth values are sieves.

Isham and Butterfield already have sieve-valued truth, and failures of strong conjunction and disjunction, in 1998. They state that the Heyting algebra of sieves "is precisely fixed by the structure of the base category" (§6).

## What this does not say

- That the Heyting structure on Sub_cl(Σ) is proved in the source. Thm 2.5 gives ∧, ∨ and ¬, leaves ⇒ to "straightforward extension", and does not check the Heyting laws ([NOTE-292](../notes.d/NOTE-292.md)). The proof is the record's own, in the note of 2026-10-19.
- That Sub_cl(Σ) is a Heyting subalgebra of Sub(Σ). Its joins and negation are regularized by closure and interior, as [LIT-378](../literature.d/LIT-378.md) also remarks.
- That the topos restores global points or a hidden-variable state space. Σ still has no global elements. What changes is the logic, and states become truth objects.
- That quantum probabilities are recovered. Sieve-valued truth from a state discards them ([LIT-325](../literature.d/LIT-325.md), spin-½ example).
- That a document using orthocomplement negation for concepts or propositions can cite this programme for its logic. The two are different logics.

## Connections

- [LIT-306](../literature.d/LIT-306.md) (Birkhoff–von Neumann) and the modular-law claim in this group: the orthocomplemented, non-distributive alternative that this programme replaces.
- [LIT-357](../literature.d/LIT-357.md) (Husimi) also keeps logic two-valued over states and rejects many-valued logics. It is a different answer to the same question ([NOTE-312](../notes.d/NOTE-312.md)).
- [LIT-276](../literature.d/LIT-276.md): a claim that the logic turns Boolean when a presheaf has a global section. It is rejected in this group.
- Two later readings leave the promotion condition unmet. Döring and Isham's merged text, [LIT-378](../literature.d/LIT-378.md) ([NOTE-326](../notes.d/NOTE-326.md)), restates Sub_cl(Σ) as Heyting (its Thm 16.1) with ⇒ again left to "a straightforward extension" (p. 188), and with negation redefined by an interior, so Sub_cl(Σ) is not a Heyting subalgebra of Sub(Σ). Butterfield and Isham's part IV, [LIT-382](../literature.d/LIT-382.md) ([NOTE-328](../notes.d/NOTE-328.md)), proves that coarse-graining is the direct image of clopen regions ([THEORY-619](THEORY-619.md)), which this account presupposes, and builds no Heyting operations.

## Note of 2026-10-19: the Heyting structure, re-derived

The source sketches Thm 2.5. This is the record's re-derivation, which meets
the promotion condition under [ADR-047](../decisions.d/ADR-047.md) v2. Order on Sub_cl(Σ) is stagewise
inclusion, and for V′ ⊆ V the restriction ρ : Σ_V → Σ_V′ is continuous and
open. Each Σ_V is compact Hausdorff and, since V is a von Neumann algebra,
extremally disconnected: the closure of an open set is open ([NOTE-292](../notes.d/NOTE-292.md),
"Topology").

**1. Sub_cl(Σ) is a frame.**

- *Finite meets* are stagewise intersections. An intersection of clopens is
  clopen, and ρ(S_V ∩ T_V) ⊆ ρ(S_V) ∩ ρ(T_V) ⊆ S_V′ ∩ T_V′.
- *Arbitrary joins.* For a family (T_i), put (⋁T_i)_V = cl(⋃_i T_i,V). This
  is the closure of an open set, so it is clopen. It is a sub-object, because
  ρ is continuous: ρ(cl ⋃ T_i,V) ⊆ cl ρ(⋃ T_i,V) ⊆ cl ⋃ T_i,V′. It is the
  least upper bound, because any upper bound U has U_V closed and containing
  each T_i,V.
- *Distributivity.* For S_V clopen and any U, S_V ∩ cl U = cl(S_V ∩ U). The
  inclusion ⊇ holds because S_V ∩ cl U is closed and contains S_V ∩ U. For
  ⊆, take x in S_V ∩ cl U. Every neighbourhood N of x gives an open
  neighbourhood N ∩ S_V, which meets U, so N meets S_V ∩ U. Taking
  U = ⋃ T_i,V, S ∧ ⋁T_i = ⋁(S ∧ T_i).

A complete lattice whose finite meets distribute over arbitrary joins is a
frame, hence a complete Heyting algebra, with S ⇒ T = ⋁{R : R ∧ S ≤ T}.
The law R ≤ (S ⇒ T) iff R ∧ S ≤ T holds by construction, and the lattice is
distributive.

**2. The pseudo-complement is (2.39).** ¬S = S ⇒ 0 is the largest R with
R ∧ S = 0. If R ∧ S = 0 and λ ∈ R_V, then for each V′ ⊆ V, λ|V′ ∈ R_V′,
which is disjoint from S_V′. So R_V lies in the closed set
⋂_(V′⊆V){λ : λ|V′ ∉ S_V′}, and, being open, in its interior. That interior
is clopen, since it is the interior of a closed set in an extremally
disconnected space. It is restriction-stable by [NOTE-292](../notes.d/NOTE-292.md)'s check, which
uses the openness of ρ. So the interiors form the largest such R, which is
(2.39).

**3. Excluded middle fails.** Take H = ℂ². The contexts are ℂ·1, whose
spectrum is one point, and the maximal abelian subalgebras V_b, one for each
orthonormal basis b. Each V_b has a two-point spectrum, and both points
restrict to the point of ℂ·1. Fix a basis b₀ and let S consist of the point
at ℂ·1, one point of Σ_(V_b₀) at V_b₀, and the full spectrum at every other
V_b. Every component is clopen, since the spaces are discrete, and every
restriction lands in the point at ℂ·1, so S is a clopen sub-object. Any R
with R ∧ S = 0 has R_(ℂ·1) = ∅. Then R_V = ∅ at every V, because ρ(R_V)
lies in R_(ℂ·1). So ¬S = 0, and S ∨ ¬S = S, which is not Σ because S omits a
point at V_b₀. The algebra is not Boolean.
