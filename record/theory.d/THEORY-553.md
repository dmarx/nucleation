---
number: 553
status: Active
formerly:
- THEORY-tmpirvdi
title: "In the Döring–Isham topos representation of quantum theory a bounded physical quantity cannot take values in the topos's real-number object; it is represented faithfully by an arrow from the spectral presheaf to a presheaf of monotone real functions over subcontexts, so its value at a context is a spread that widens as the context shrinks, and these values form only a commutative monoid, under which sums of daseinised quantities are not daseinisations of sums"
version: 1
tags:
- quantum-foundations
- mathematics
- contextuality
date: '2026-10-16'
source:
- LIT-299
- LIT-378
summary: >-
  Döring & Isham, paper III (2007/8), [LIT-299](../literature.d/LIT-299.md) ([NOTE-290](../notes.d/NOTE-290.md)), restated with
  additions in [LIT-378](../literature.d/LIT-378.md) ([NOTE-326](../notes.d/NOTE-326.md)). The Gel'fand transforms of daseinised
  operators grow as contexts shrink, so arrows into the constant presheaf ℝ
  are impossible (3.3–3.4). Each Â gives a natural transformation
  δ̆^o(A) : Σ → ℝ^⪰ (Thm 3.1), and Â ↦ δ̆^o(A) is injective, by de Groote's
  results. ℝ^⪰ is a monoid, not a group; differences need a group
  completion, whose global elements are the functions of bounded variation
  on the context poset. No choice among the candidate value objects is
  made, and the state-dependent reading of the spread is cited, not
  proved.
presupposed_by:
- THEORY-585
---

<!-- inactive-ok-file: THEORY-017 THEORY-585 — Proposed; named in Connections, not leaned on -->

# THEORY-553: In the Döring–Isham topos representation of quantum theory a bounded physical quantity cannot take values in the topos's real-number object; it is represented faithfully by an arrow from the spectral presheaf to a presheaf of monotone real functions over subcontexts, so its value at a context is a spread that widens as the context shrinks, and these values form only a commutative monoid, under which sums of daseinised quantities are not daseinisations of sums

## Source

Döring & Isham (2007; *J. Math. Phys.* 49, 2008), "A topos foundation for
theories of physics: III", [LIT-299](../literature.d/LIT-299.md), read in full in [NOTE-290](../notes.d/NOTE-290.md). The merged
text, Döring & Isham (2008), "'What is a Thing?'", [LIT-378](../literature.d/LIT-378.md), §§7–9, read in
full in [NOTE-326](../notes.d/NOTE-326.md), restates it with corrections and adds the value in a
pseudo-state.

## What was actually shown

**Setting.** Contexts are the unital abelian von Neumann subalgebras V of
B(H), ordered by inclusion; the topos is presheaves over them; the state
object Σ assigns each V its Gel'fand spectrum. Operators are bounded.

**Daseinisation of quantities (Def 2.4).** δ^o(Â)_V is the least element of
V above Â in the spectral order, δ^i(Â)_V the greatest below (2.21, 2.18).
Both equal Â if Â ∈ V, and sp(δ^o(Â)_V) ⊆ sp(Â) (2.23). Both maps are
non-linear and are not Borel functions of Â.

**Not the real-number object (C3).** The real-number object is the constant
presheaf ℝ. The Gel'fand transforms of δ^o(Â)_V grow as V shrinks
(3.3)–(3.4), and an arrow into a constant presheaf would need equality where
there is strict growth.

**The representation (Thm 3.1).** For each Â, λ ↦ (V′ ↦ λ(δ^o(Â)_{V′})) is
a natural transformation δ̆^o(A) : Σ → ℝ^⪰, where ℝ^⪰_V is the set of
order-reversing functions on the subcontexts of V. The check is one line
(3.15). With inner daseinisation, δ̆(A) : Σ → ℝ^↔ pairs an order-preserving
and an order-reversing function. The map Â ↦ δ̆^o(A) is injective (Appendix),
resting on de Groote's bijection between operators and observable functions.

**The spread (3.47)–(3.52).** At a point λ of Σ_V the value is the interval
[λ(δ^i(Â)_{V′}), λ(δ^o(Â)_{V′})] over subcontexts V′, widening as V′
shrinks. It is state-independent, as a classical function on phase space
is. [LIT-378](../literature.d/LIT-378.md) §8.5 adds the value in a pseudo-state: if ψ is an eigenvector
of Â and Â ∈ V, both components equal the eigenvalue at V.

**Algebra (§3.5, §4; [LIT-378](../literature.d/LIT-378.md) §9).** ℝ^⪰ and ℝ^↔ are commutative monoid
objects. δ^o(Â) + δ^o(B̂) ≠ δ^o(Â + B̂) in general (fn. 19). The group
completion k(Γℝ^⪰) is the functions of bounded variation on the context
poset (one direction written; [NOTE-290](../notes.d/NOTE-290.md) checked it). Squares exist only for
classes [λ, 0] (4.19), which makes an "intrinsic dispersion" definable and
nothing more.

**What could have come out otherwise.** Daseinised operators could have
been constant along restrictions, making the reals adequate, or the
monotone-function arrows could have failed to be natural. Neither held.

## What this does not say

- **Which value object is right.** ℝ^⪰, ℝ^⪯, ℝ^↔ and their group completions
  are all offered, with no criterion; [LIT-378](../literature.d/LIT-378.md) prefers ℝ^↔ "from a physical
  perspective" and then reverts to ℝ^⪰ ([NOTE-326](../notes.d/NOTE-326.md)).
- **That the spread brackets ⟨ψ|Â|ψ⟩ as least and greatest measurement
  results.** That reading is cited from Döring's antonymous-functions
  paper, not proved, and the authors disown its instrumentalism (fn. 14;
  [NOTE-290](../notes.d/NOTE-290.md), C6).
- **That quantities can be added or squared as in quantum theory.** Values
  form a monoid; differences need completion; general squares fail
  (fn. 23).
- **Anything about unbounded operators.** Position and momentum are outside
  the construction as given.
- **That every step is proved.** Thm 3.2, Thm 5.1 and the group-object
  structure of the completion are asserted.

## Connections

- The points of Σ_V are exactly the ultrafilters of V's Boolean projection
  lattice (3.28), the operator form of the Stone fact in [THEORY-020](THEORY-020.md); Σ has
  no global points by Kochen–Specker, for dim H > 2, a condition paper III
  drops.
- Propositions in this programme, and their Heyting logic, are
  [THEORY-037](THEORY-037.md). Composing these representations across systems is
  [THEORY-585](THEORY-585.md).
- Isham & Butterfield's doubt that quantities should take real values
  ([LIT-389](../literature.d/LIT-389.md), §1.3) is the motivation this construction makes concrete.
- Unitaries act covariantly by permuting contexts (§5), which fits
  [THEORY-017](THEORY-017.md)'s claim that a context or basis is extra data.
