---
number: 595
status: Active
formerly:
- THEORY-tmpnz4z2
title: "A filter over a set of worlds is a finitely consistent propositional theory and an ultrafilter a negation-complete one; read so, the ultrafilter extension theorem is Lindenbaum's lemma for propositions, and Łoś's theorem builds a model that makes true exactly what an ultrafilter says, which proves first-order compactness without proof theory, given the axiom of choice"
version: 1
tags:
- logic
- mathematics
date: '2026-10-16'
source:
- LIT-145
summary: >-
  Turner (preprint 2021, published 2025), [LIT-145](../literature.d/LIT-145.md), read in [NOTE-177](../notes.d/NOTE-177.md). An
  expository paper: "None of the results are novel" (p. 2). Maximal, prime
  and ultra filters coincide (Thm 2); every filter extends to an
  ultrafilter (Thm 3); Łoś's theorem (Thm 9); compactness (Thm 12). The
  results are standard and correct, though the write-up has slips. A
  filter is only finitely consistent, and that is the point. The pairings
  with Lindenbaum and Henkin are analogies, not reductions.
---

# THEORY-595: A filter over a set of worlds is a finitely consistent propositional theory and an ultrafilter a negation-complete one; read so, the ultrafilter extension theorem is Lindenbaum's lemma for propositions, and Łoś's theorem builds a model that makes true exactly what an ultrafilter says, which proves first-order compactness without proof theory, given the axiom of choice

## Source

Turner, "Ultrafilters as Propositional Theories", [LIT-145](../literature.d/LIT-145.md), read in full in
[NOTE-177](../notes.d/NOTE-177.md) from the author's preprint of 20 November 2021, every page and
every proof. The published version (*Philosophy Compass*, 2025) was seen
only through its abstract, which omits compactness.

## What was actually shown

**The dictionary (§1.2, pp. 3–4).** Take a non-empty set W of indices
("worlds"); a W-proposition is a subset of W, with ∩ as conjunction,
complement as negation and ⊆ as implication. A filter over W, a family
closed under intersection and superset and not containing ∅, is then a
propositional theory closed under pairwise conjunction and implication
that does not contain the impossible proposition. An ultrafilter also
contains p or W − p for every p.

**Theorem 2 (p. 5).** For a filter, maximal, prime and ultra are
equivalent.

**Theorem 3 (pp. 6–8).** Every filter extends to an ultrafilter, by
transfinite recursion over a well-ordering of 𝒫(W), which needs choice.

**Theorem 9, Łoś (pp. 18–20).** Over an "intensional space" (each world
assigned a model of a fixed first-order language), the ultraproduct M_T,
whose domain is equivalence classes of world-to-object functions, satisfies
M_T, [A] ⊨ φ iff ⟦φ⟧_A ∈ T, for an ultrafilter T. Only the negation step
uses ultra-ness; for a mere filter the construction is a reduced product.

**Theorem 12, compactness (pp. 20–21).** Let W be the finite subsets of Γ,
each with a model. The sets containing some ⟦⋀Δ⟧ form a filter; extend it
to an ultrafilter and apply Łoś. So a finitely satisfiable Γ has a model.

**What could have come out otherwise.** These are standard theorems and
could not. What [NOTE-177](../notes.d/NOTE-177.md) checked is that each proof goes through. They do,
with slips it lists: a gappy maximal-to-prime step in Theorem 2, a wrong
condition cited in Theorem 9, and Δ ∩ Σ for Δ ∪ Σ in Theorem 12.

## What this does not say

- **That a filter is a consistent theory.** It is only finitely consistent.
  It can contain an "essentially infinite contradiction" (p. 3), and that is
  why compactness needs the extension to an ultrafilter.
- **That the extension theorem is Lindenbaum's lemma, or Łoś's theorem
  Henkin's proof.** Those are informal analogies (C4, C6), not formal
  reductions.
- **That the "propositions" are propositions.** They are sets of indices;
  the author calls the reading a "pretense" that helps the model theory
  (p. 15) and disclaims modal semantics (p. 11).
- **That philosophers have a use for it.** The paper says they can put
  ultrafilters "to good use" and names no application (C9).
- **That the published version says the same.** Only the preprint was read.

## Connections

- The same ultrafilter machinery builds Wenmackers's numerosity
  probabilities for a fair lottery on ℕ ([THEORY-401](THEORY-401.md)), where the
  choice of free ultrafilter is what the solution is not unique up to.
- Stone's representation of a Boolean algebra by its prime ideals
  ([THEORY-020](THEORY-020.md)) is the algebraic face of the same equivalence of prime and
  ultra filters.
