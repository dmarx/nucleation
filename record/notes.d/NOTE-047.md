---
number: 47
status: Skimmed
formerly:
- NOTE-tmpcpuvk
paper: LIT-040
title: 'nLab, two-level type theory'
version: 1
date: '2026-09-25'
summary: >-
  Two-level type theory pairs a homotopy (univalent, fibrant) type theory with an outer level having UIP "exact equality" (the internalised metatheory). This lets one reason explicitly about the presenting model category, e.g. to define semisimplicial types by induction on strict equalities. Whether this breaks the (∞,1) principle of equivalence, and how many natural-number types to have, are open design questions.
---

<!-- inactive-ok-file: LIT-040 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-047: nLab, two-level type theory

## Contribution

The page describes 2LTT as versions of Martin-Löf type theory with two layers: an inner homotopy type theory (univalent universes, higher inductive types) and an outer traditional type theory satisfying uniqueness of identity proofs, which can be read as the internalised metatheory of the first. The inner types are called fibrant and the outer ones pretypes, following fibration-category and model-category semantics. The trade-off is explicit control over the presenting model category at the apparent cost of the (∞,1)-categorical principle of equivalence. The extent of that cost is an open question.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Type theories: the first proposal was Voevodsky's Homotopy Type System, whose reflection rule made type-checking undecidable. Altenkirch–Capriotti–Kraus (ACK) simply assume UIP for exact equality. Computational cubical type theory can also carry a non-fibrant layer, with fibrancy a defined condition.
- Applications: the motivating application is semisimplicial types. In plain HoTT the simplicial identities hold only up to coherent homotopy, and encoding that coherence syntactically is "unsolved to date". Exact equality defined by induction removes the problem.
- Variations: one fibrant ℕ or two (fibrant and non-fibrant)? With two, the theory cannot define a fibrant type of untruncated semisimplicial types without extra axioms, e.g. closure of fibrant types under limits of towers indexed by the non-fibrant ℕ. With one, some models, such as local model structures on simplicial presheaves, may be excluded.
- References: Altenkirch, Capriotti & Kraus, arXiv:1604.03799, and Annenkov, Capriotti, Kraus & Sattler, *Two-Level Type Theory and Applications*, arXiv:1705.03307. See also: Homotopy Type System, type theory with shapes.

## Open questions

- The survey says "drop: a wiki page, not a work". If kept, the note should cite the canonical paper, Annenkov–Capriotti–Kraus–Sattler, arXiv:1705.03307, not the wiki. That is the preferred source under the record's arxiv > doi > url rule.
- It pairs directly with c22 (Riehl–Shulman), which names 2LTT as the "brute force" option it declines in favour of shapes and extension types.
