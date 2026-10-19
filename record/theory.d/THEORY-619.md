---
number: 619
status: Active
formerly:
- THEORY-tmpqv891
title: "Over the poset of commutative von Neumann subalgebras, coarse-graining a projector to a smaller subalgebra is exactly the direct image of its clopen region of the Gelfand spectrum under restriction, so the coarse-graining presheaf is the presheaf of clopen spectral regions; and a quantum state's sieve-valued truth values are fixed by one coherent family of regions, its supports: a proposition is true at a subcontext exactly when the support there lies under the coarse-grained proposition"
version: 1
tags:
- quantum-foundations
- mathematics
- logic
- contextuality
date: '2026-10-16'
source:
- LIT-382
summary: >-
  Butterfield & Isham (2001), "Topos Perspective on the Kochen-Specker
  Theorem: IV", [LIT-382](../literature.d/LIT-382.md), read in full in [NOTE-328](../notes.d/NOTE-328.md). §2.4 proves G ≅ CloΣ:
  restricting the characters of V₁ that make P̂ true gives exactly the
  characters of V₂ that make its coarse-graining true, via a cited
  state-extension theorem. Theorem 3.1 shows that any assignment defined
  by "support ≤ coarse-grained proposition", with supports forming a global
  element of G, is a sieve-valued valuation obeying FUNC; a state's supports
  qualify. Both theorems are close to definitional. Nothing here builds
  Heyting operations on clopen sub-objects.
presupposed_by:
- THEORY-037
---

<!-- inactive-ok-file: LIT-380 — Superseded by LIT-382; named as the paper that introduced the base category and asserted the isomorphism this account states as proved -->

# THEORY-619: Over the poset of commutative von Neumann subalgebras, coarse-graining a projector to a smaller subalgebra is exactly the direct image of its clopen region of the Gelfand spectrum under restriction, so the coarse-graining presheaf is the presheaf of clopen spectral regions; and a quantum state's sieve-valued truth values are fixed by one coherent family of regions, its supports: a proposition is true at a subcontext exactly when the support there lies under the coarse-grained proposition

## Source

Butterfield & Isham (2001; *IJTP* 41, 2002), [LIT-382](../literature.d/LIT-382.md), read in full in
[NOTE-328](../notes.d/NOTE-328.md).

## What was actually shown

**Setting.** The base category V is the poset of commutative von Neumann
subalgebras of B(H). The coarse-graining presheaf G assigns V its projection
lattice L(V), and sends P̂ to the least projector of a smaller V₂ above it.
For a projector, V(P̂) := {κ ∈ σ(V) | κ(P̂) = 1} is a clopen subset of the
Gelfand spectrum.

**G ≅ CloΣ (§2.4, eqs. 2.7–2.11).** For V₂ ⊆ V₁ and P̂ ∈ L(V₁),
{κ|_{V₂} | κ ∈ σ(V₁), κ(P̂) = 1} = {λ ∈ σ(V₂) | λ(G(P̂)) = 1}. One inclusion
is easy. For the other, a character λ of V₂ with λ(G(P̂)) = 1 extends to a
character κ of V₁ with κ(P̂) = 1, by Kadison–Ringrose Thm 4.3.13 (credited
to Halvorson). The step from a state extension to a character extension is
left implicit; [NOTE-328](../notes.d/NOTE-328.md) calls it standard and repairable. So P̂ ↦ V(P̂) is a
natural isomorphism between G and the presheaf of clopen subsets with
direct image as its arrow map.

**Supports determine the semantics (Thm 3.1).** Let supports
s(α, V) = inf T^α(V) form a global element of G, and let
i_{V₂V₁} ∈ α_{V₁}(P̂) iff s(α, V₂) ≤ G(P̂). Then α is sieve-valued, obeys
FUNC, and α_{V₁}(P̂) = {V₂ | G(s(α, V₁)) ≤ G(P̂)} (3.3). The proof uses only
monotonicity and functoriality of G. A state's valuation ν^ρ meets the
conditions: its support at V is the least projector of V that ρ makes
certain. Theorem 3.2 gives the same with intervals of the spectrum in place
of supports, when they form a "tight" subobject of Σ.

**Choice of relation (§4).** Defining a valuation by "a(V₂) R G(P̂)" for a
global element a of G, FUNC holds for every R, and R = ≤ gives sievehood,
null, monotonicity and exclusivity, provided a never assigns 0̂. [NOTE-328](../notes.d/NOTE-328.md)
checked each item.

**What could have come out otherwise.** Restriction of a clopen region
could have landed strictly inside the region of the coarse-grained
projector, which would have made coarse-graining lossy on the spectral
side. The extension theorem rules it out.

## What this does not say

- **That the theorems are deep.** Condition (i) of Theorem 3.1 is
  essentially its conclusion once (ii) holds, and the paper calls the
  converses "trivially" true. The substance is G ≅ CloΣ, which sits in the
  "review" section and is not mentioned in the abstract.
- **Anything about the Heyting operations on clopen sub-objects.** No
  implication or negation is built, so this does not meet [THEORY-037](THEORY-037.md)'s
  promotion condition. It does sharpen [THEORY-037](THEORY-037.md)'s caveat: daseinised
  projectors are tight subobjects, global elements of CloΣ, and not every
  subobject of Σ is one.
- **That probability-r valuations fail to form global elements.** That is
  asserted without counterexample.
- **Anything on the operator category beyond discrete spectra.** The
  claim f(s(·, Â)) ⊆ s(·, f(Â)) "even if Â has in part a continuous
  spectrum" (3.26) is undefined as written for continuous spectra, and
  [NOTE-328](../notes.d/NOTE-328.md) gives a counterexample under the closed-support reading.
- **Anything about probabilities, dynamics or composites.**

## Connections

- Part III (Hamilton, Isham & Butterfield, [LIT-380](../literature.d/LIT-380.md), Superseded) introduced
  the base category V and asserted G ≅ CloΣ; this paper proves it.
- [THEORY-037](THEORY-037.md) rests on daseinisation sending each projector to a clopen
  sub-object of Σ; Döring–Isham's daseinisation is G here, and the
  isomorphism proved here is what makes the sub-object clopen.
- The support of a pure state ψ at V is the least projector of V above
  |ψ⟩⟨ψ|, the later "pseudo-state" of [LIT-378](../literature.d/LIT-378.md) ([NOTE-328](../notes.d/NOTE-328.md)'s gloss).
- Pairwise, between nested contexts, local two-valued valuations always
  extend; the Kochen–Specker obstruction appears only over the whole poset,
  which fits [THEORY-020](THEORY-020.md).
- The sieve semantics in general, and why it does not depend on global
  sections, is [THEORY-516](THEORY-516.md).
