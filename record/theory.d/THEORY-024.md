---
number: 24
status: Rejected
formerly:
- THEORY-tmp4dpbp
title: 'Classical Boolean logic is restored when a presheaf of contextual data acquires a global section or is sheafified'
version: 1
tags:
- logic
- quantum-foundations
- contextuality
- philosophy-of-science
date: '2026-09-30'
source:
- LIT-276
- LIT-325
- LIT-343
summary: >-
  Ghose (2025), [LIT-276](../literature.d/LIT-276.md) — asserts that the Heyting algebra of truth values
  "becomes Boolean" when the presheaf data collapse to a global section,
  and that sheaves encode Boolean reasoning. Both claims are asserted, not
  proved. The record's readings refute them. The internal logic of a topos
  is fixed by the base category and its topology, not by whether one
  presheaf has a section (Isham–Butterfield, [LIT-325](../literature.d/LIT-325.md), §6). Sheaf toposes
  such as Sh(ℝ) are not Boolean ([NOTE-249](../notes.d/NOTE-249.md)). The contextuality criterion
  itself is untouched.
---

# THEORY-024: Classical Boolean logic is restored when a presheaf of contextual data acquires a global section or is sheafified

## Source

Ghose (2025), [LIT-276](../literature.d/LIT-276.md), §§5–6, 10, Appendix A ([NOTE-249](../notes.d/NOTE-249.md)). Refuting readings: Isham & Butterfield (1998), [LIT-325](../literature.d/LIT-325.md), §6 ([NOTE-271](../notes.d/NOTE-271.md)); Döring & Isham (2007), [LIT-343](../literature.d/LIT-343.md), §3.2 and Appendix ([NOTE-277](../notes.d/NOTE-277.md)).

## What was actually shown

[LIT-276](../literature.d/LIT-276.md) says, correctly, that the internal logic of a presheaf topos is intuitionistic (§5). It then says that Boolean logic is "recovered precisely when the presheaf data collapse to a single global section. In that regime the Heyting algebra of truth values becomes Boolean". It adds that "sheaves thus encode the logical structure presupposed by classical physics: context-independent truth and Boolean reasoning" (§6), and that measurement is the sheafification that brings this about. No theorem, site, topology or computed example backs any of these claims.

The account fails on the record's readings.

- **The truth values belong to the base category.** In a presheaf topos the truth values at a stage are the sieves on it. Isham and Butterfield state that this Heyting algebra "is precisely fixed by the structure of the base category" ([LIT-325](../literature.d/LIT-325.md) §6). Döring and Isham's appendix builds Ω as the presheaf of sieves, independently of any state or data presheaf ([LIT-343](../literature.d/LIT-343.md)). A presheaf with a global section lives in the same topos as one without, with the same Ω. Its sub-object lattices are Heyting in general.
- **The Boolean case is narrow.** A presheaf topos is Boolean iff its base is a groupoid ([NOTE-249](../notes.d/NOTE-249.md), a standard fact the reader supplies). A context category with non-invertible refinements is not a groupoid.
- **Sheaves are not Boolean either.** The truth values of Sh(ℝ) are the open sets of ℝ, a non-Boolean Heyting algebra ([NOTE-249](../notes.d/NOTE-249.md)). A Boolean sheaf topos needs a special topology, such as the double-negation topology, and [LIT-276](../literature.d/LIT-276.md) names none.
- **Sheafification decides nothing.** It is a functor fixed by the topology and applied to every presheaf alike. On Abramsky–Brandenburger's site it either changes nothing or adjoins the empirical model itself as a formal section, and whether that model is contextual is unchanged ([NOTE-249](../notes.d/NOTE-249.md), the reader's sketch).

## What this does not say

- That contextuality is not the absence of a global section. That criterion stands ([THEORY-012](THEORY-012.md), [LIT-016](../literature.d/LIT-016.md), [LIT-325](../literature.d/LIT-325.md) §2).
- That a single Boolean context lacks classical valuations. It has them, by Stone (see the Stone claim in this group). The error is to move from "this presheaf has a section" to "the logic is Boolean".
- That no reading of "classical = Boolean" could be made precise. A different topos, over a discrete base or with the double-negation topology, would be Boolean. [LIT-276](../literature.d/LIT-276.md) specifies no such construction.

## Connections

- [THEORY-012](THEORY-012.md) (the contextuality criterion, which stands) and the topos-logic claim in this group (the Heyting logic, which does not depend on sections).
- [LIT-277](../literature.d/LIT-277.md) ([NOTE-250](../notes.d/NOTE-250.md)): [LIT-276](../literature.d/LIT-276.md)'s displayed Čech class is a coboundary and so is zero. The real obstruction is Abramsky–Mansfield–Barbosa's relative class.
