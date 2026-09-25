---
status: Skimmed
paper: LIT-tmp1t8m4
title: 'Riehl & Shulman, type theory for synthetic ∞-categories'
version: 1
date: '2026-09-25'
summary: >-
  Adding a directed interval 2 and a separate "shape" layer (the coherent theory of a strict interval) to homotopy type theory yields a synthetic theory of (∞,1)-categories. Segal types, where binary composites are unique up to homotopy, automatically get coherent associativity and unitality, and a dependent Yoneda lemma holds for covariant families. The model is bisimplicial sets, where Segal and Rezk types are (complete) Segal spaces.
---

<!-- inactive-ok-file: LIT-tmp1t8m4 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpoux3y: Riehl & Shulman, type theory for synthetic ∞-categories

## Contribution

The authors propose foundations for synthetic (∞,1)-category theory inside homotopy type theory. They axiomatize a directed interval type, build higher simplices from it, and use these to probe the categorical structure of any type. Segal types have homotopically unique binary composites, which is enough for coherent associativity and unitality in all dimensions. Rezk types additionally identify categorical isomorphisms with type-theoretic identities, a local univalence. Covariant fibrations vary functorially over Segal types and satisfy a dependent Yoneda lemma, a directed analogue of identity elimination. Having an adjoint is shown to be a mere proposition for functors between Rezk types. To manage the bookkeeping, the paper uses a three-layer type theory with shapes (polytopes in directed cubes) and extension types generalising cubical path types. An appendix gives semantics in the Reedy model structure on bisimplicial sets.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1: HoTT is a synthetic theory of ∞-groupoids because identity elimination generates all the higher structure. A directed analogue has been elusive: not all functors are exponentiable, and there are too many kinds of fibration. The authors' indirect route, also suggested by Joyal, is to interpret HoTT in Reedy bisimplicial sets and identify internally the types that behave like complete Segal spaces.
- §1: 2 is a strict interval (totally ordered, with distinct 0 and 1), and simplicial sets classify such objects. Simplices are carved out, e.g. Δ² = {(s,t) | t ≤ s}. Maps Δ²→A are commutative triangles, and A is Segal if composites form a contractible type.
- §1 on design: a "brute force" two-level type theory (Voevodsky's HTS, Annenkov–Capriotti–Kraus) with a non-fibrant strict equality is considered and rejected. Instead, all types are kept fibrant and cofibrations are specified in a separate shape syntax, with extension types ⟨Π_{y:B} C(y) | d⟩ (an idea credited to Lumsdaine and Shulman). The authors say swapping in Joyal's disks might give (∞,n)-categories.
- Remark 1.1: formally close to cubical type theory, but the interval 2 is orthogonal to the native homotopy direction and not another presentation of it.
- Roadmap (§1, ToC): §2–4 cover shapes and extension types, §5–6 Segal types and their 2-category, §7 discrete types (the groupoids), §8–9 covariant families and Yoneda, §10 Rezk types, §11 adjunctions, and Appendix A the semantics.

## Open questions

- It is directly paired with c26 (nLab, two-level type theory). This paper names 2LTT as the alternative it rejects, and the nLab page lists "type theory with shapes" under See also. A reading should file them together.
- Later developments to check include the Rzk proof assistant, which implements this simplicial type theory, and the follow-up synthetic ∞-category work. The v5 correction to the proof of 8.13 is noted on the arXiv page.
