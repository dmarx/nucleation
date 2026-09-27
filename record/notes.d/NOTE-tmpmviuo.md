---
status: Skimmed
paper: LIT-tmpevs68
title: 'Spekkens, generalized contextuality (2005)'
version: 1
date: '2026-09-27'
summary: >-
  Defines a noncontextual ontological model as one in which operationally equivalent procedures (preparations, measurements, transformations) get identical representations; shows the traditional Kochen–Specker notion is the special case of measurement noncontextuality for sharp measurements plus outcome determinism, proves that preparation noncontextuality implies that outcome determinism, and proves preparation contextuality already for a qubit.
---
<!-- inactive-ok-file: LIT-tmpevs68 — Deferred: filed and skimmed on 2026-09-27 while bringing the contextuality threads together; the theories citing it are Proposed until it is read closely -->

# NOTE-tmpmviuo: Spekkens, generalized contextuality (2005)

## Contribution

The paper replaces the traditional definition of noncontextuality, which is specific to quantum theory, to sharp measurements and to deterministic hidden variables, with an operational one: in a noncontextual ontological model, procedures that no experiment can tell apart are represented identically. It applies to any operational theory and to preparations, transformations and unsharp measurements. Three no-go theorems follow, one for each kind of procedure, and all three work in a two-dimensional Hilbert space, where the traditional Kochen–Specker argument cannot be run.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §II (Eqs. 1–7): operational equivalence of preparations, measurements and transformations; the "context" of a procedure is every feature not fixed by its equivalence class; preparation/measurement/transformation noncontextuality are µ_P = µ_e(P), ξ_M,k = ξ_e(M),k, Γ_T = Γ_e(T). "Universal" noncontextuality means all three. Footnote 6: by this definition any classical theory is noncontextual for all procedures.
- §III (p. 5–6): for sharp measurements represented by idempotent indicator functions (outcome determinism), independence of the representation from the fine-graining of the PVM "is just the traditional notion of noncontextuality"; traditional no-gos need dimension ≥ 3 because a 2d PVM has no non-trivial fine-grainings.
- §IV (Eqs. 13–36): six qubit pure states forming five convex decompositions of I/2; with distinguishable-preparations-don't-overlap (Feature 1) and convexity (Feature 2), preparation noncontextuality forces every µ to vanish — no preparation-noncontextual model of a qubit.
- §VIII.A (Eqs. 77–88): preparation noncontextuality implies outcome determinism for every PVM (the supports of the µ_k of an orthonormal basis must cover the ontic space, because they decompose I/d). §VIII.B (Eqs. 89–92): the Beltrametti–Bugajski model is measurement-noncontextual (ξ = Tr(Q_k|ψ⟩⟨ψ|)) but not outcome-deterministic and is preparation contextual — so measurement noncontextuality alone is consistent with quantum theory.
- §IX: "one can confine all the contextuality into the preparations and transformations … one cannot confine all the contextuality into the measurements"; KS proofs remain proofs against universal noncontextuality; a failure of local causality in a separable model implies measurement contextuality.

## Open questions

- It is the published link between Kochen–Specker/sheaf contextuality ([LIT-016](../literature.d/LIT-016.md)) and the generalized notion that [LIT-003](../literature.d/LIT-003.md), [LIT-007](../literature.d/LIT-007.md) and [LIT-019](../literature.d/LIT-019.md) rely on; none of those held works states the link. A close reading should check §VIII.A's proof, in particular that it needs the full set of quantum preparations (every state in some decomposition of I/d), which a restricted fragment may lack.
- Check §V: the paper's own unsharp-measurement proof assumes outcome determinism for sharp measurements, which §VIII then justifies from preparation noncontextuality — so its "measurement contextuality" proofs are really proofs against preparation + measurement noncontextuality.
- The "classical ⇒ noncontextual" footnote is the basis of the "contextuality = nonclassicality" stance of the Spekkens programme; it is asserted, not proved, for arbitrary classical theories.
