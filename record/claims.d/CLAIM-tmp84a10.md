---
status: Proposed
title: 'For Boolean constraint languages with constants and single-variable flips, the language fixes whether deciding that one solution reaches another is polynomial or PSPACE-complete, by a boundary that cuts across the clones of polymorphisms that fix the complexity of satisfiability, so the algebra of the satisfiability dichotomy does not by itself predict the complexity of navigating a solution space'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the cited classifications: that deciding whether two
  solutions are joined by single flips is not polynomial for positive
  1-in-3 SAT, or not PSPACE-complete for positive NAE-3SAT; or an error in
  the filer's step that, with constants, both languages have only the
  projections as polymorphisms, so that they generate different clones. Not
  defeated by algebraic criteria of other kinds, such as classes of Post's
  lattice used within the Horn case for global connectivity, or a refined
  definability such as faithful expressibility, which the claim allows; it
  says the clone of polymorphisms does not suffice.
tags:
- mathematics
- logic
date: '2026-11-05'
line:
- realizability
- formal-apparatus
grounds:
- THEORY-tmpmcxbv
- THEORY-tmpo2ib0
- THEORY-tmp99dad
- THEORY-tmp8numn
complements:
- CLAIM-tmplysd0
- CLAIM-tmpsbz28
bears_on:
- QUESTION-tmp3tq0j
summary: >-
  A's proposal, from the pasted synthesis on resource-bounded realizability
  (three responses, pasted by the owner on 2026-11-05, continuing the
  exchange on constraint architectures), Response 3 §4 and the closing
  questions: the Pol–Inv Galois connection and the Bulatov–Zhuk dichotomy
  as "a strong candidate for the algebraic component of the proposed
  theory", and whether "the algebra of a constraint language" could
  "predict something about the complexity of navigating its solution
  space". Three corrections from the readings. The dichotomy classifies
  decision problems over fixed finite languages on finite domains, not
  systems. It says nothing about connectivity. Gopalan et al., a work the
  lead added, answer the navigation question for Boolean languages, but not
  through the clone: their boundaries "cut across Boolean clones". The
  filer adds a pair with the same clone and opposite navigation. The
  construction is the filer's, from A's question and the readings; adopting
  it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmplysd0 NOTE-tmp0p9z8 NOTE-tmpa8w32 NOTE-tmpec4ov NOTE-tmpwmx5d THEORY-tmp8numn THEORY-tmp99dad THEORY-tmpmcxbv THEORY-tmpo2ib0 — Proposed or Skimmed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# CLAIM-tmp84a10: For Boolean constraint languages with constants and single-variable flips, the language fixes whether deciding that one solution reaches another is polynomial or PSPACE-complete, by a boundary that cuts across the clones of polymorphisms that fix the complexity of satisfiability, so the algebra of the satisfiability dichotomy does not by itself predict the complexity of navigating a solution space

## The claim

A (Response 3 §4): "The finite-domain CSP dichotomy theorem, proved
independently by Andrei Bulatov and Dmitriy Zhuk, characterizes a division
between polynomial-time-solvable and NP-complete fixed constraint languages
using algebraic conditions." "The theory of polymorphisms provides an
existing rigorous precedent for classifying computational systems through
their constraint-preserving algebra. It would not, by itself, solve the
problem of resource-bounded reachability or architectural reconfiguration.
But it gives a strong candidate for the algebraic component of the
proposed theory." And among A's closing questions: "could the algebra of a
constraint language predict something about the complexity of navigating
its solution space?"

**Three corrections from the readings.**

1. **The dichotomy classifies decision problems over fixed finite
   languages**, not systems ([NOTE-tmpa8w32](../notes.d/NOTE-tmpa8w32.md), [NOTE-tmp0p9z8](../notes.d/NOTE-tmp0p9z8.md); [THEORY-tmp99dad](../theory.d/THEORY-tmp99dad.md),
   [THEORY-tmp8numn](../theory.d/THEORY-tmp8numn.md)). Bulatov's Theorem 1: "For any finite constraint
   language Γ over a finite set the problem CSP(Γ) is either solvable in
   polynomial time or is NP-complete." Zhuk's criterion is "a WNU
   preserving Γ". A polymorphism is an operation applied coordinatewise to
   a relation's tuples, not an operation a system performs, and the domain
   must be finite; one crease pattern or one organization is one instance
   and has no complexity in this sense ([CLAIM-tmplysd0](CLAIM-tmplysd0.md)). A's continuous
   configuration spaces would need a finite-domain language first.
2. **It says nothing about connectivity.** Neither proof treats
   reconfiguration or reachability between solutions; Zhuk's "linked"
   instances are a local-consistency notion, a false friend.
3. **Gopalan et al. answer the navigation question for Boolean languages,
   but not through the clone** ([NOTE-tmpec4ov](../notes.d/NOTE-tmpec4ov.md); [THEORY-tmpmcxbv](../theory.d/THEORY-tmpmcxbv.md); corrected
   by Schwerdtfeger, [NOTE-tmpwmx5d](../notes.d/NOTE-tmpwmx5d.md), [THEORY-tmpo2ib0](../theory.d/THEORY-tmpo2ib0.md)). With constants and
   single-variable flips, deciding whether two solutions are joined is
   polynomial for (safely) tight languages and PSPACE-complete otherwise,
   aligned with linear against exponential diameter. Schaefer's theorem can
   be proved through Post's lattice of clones; "This method, however, does
   not appear to apply to connectivity, as the boundaries discovered here
   cut across Boolean clones."

**A pair with one clone and opposite navigation (the filer's step).**
Positive 1-in-3 SAT is tight and positive NAE-3SAT is not; both are
NP-complete to satisfy, and deciding whether two solutions are joined is
polynomial for the first and PSPACE-complete for the second
([NOTE-tmpec4ov](../notes.d/NOTE-tmpec4ov.md)). With constants added, a polymorphism must be idempotent,
and by Post's lattice every Boolean idempotent clone other than the
projections contains conjunction, disjunction, majority or minority.
Neither relation is closed under any of the four (checked by
enumeration). For 1-in-3: 100 ∧ 010 = 000, 100 ∨ 010 = 110, and the
majority and minority of 100, 010, 001 are 000 and 111. For
not-all-equal: 100 ∧ 010 = 000, 011 ∨ 101 = 111, and the majority and
minority of 110, 101, 011 are 111 and 000. So both
languages with constants have only the projections as polymorphisms,
unconditionally: the same clone, and navigation on opposite sides of
the dichotomy. This step is the filer's and the lead's, from Post's
lattice and the enumeration, and is not stated in the readings.

**One direction does hold.** Lemma 4.1: if a relation is closed under an
idempotent operation α, "then every connected component of G(R) is closed
under α", and every Schaefer language lies in a tight class, so a language
easy to satisfy by the algebra is easy to navigate. The converse fails, as
the pair shows.

## What it does not say

- **That algebra is irrelevant to navigation.** For global connectivity
  Gopalan et al.'s conjectured trichotomy, proved by Schwerdtfeger, uses
  classes of Post's lattice inside the Horn case; and faithful
  expressibility is a refined definability, which the authors think
  "seems unavoidable". The claim is that the clone that fixes
  satisfiability does not fix navigation.
- **Anything beyond Boolean domains, other moves, languages without
  constants, or budgets.** Those are [QUESTION-tmp3tq0j](../questions.d/QUESTION-tmp3tq0j.md); for formulas
  without constants Gopalan et al. leave the question open.
- **That A's Pol–Inv connection is wrong.** It is the standard one,
  Γ ⊆ Inv(F) ⟺ F ⊆ Pol(Γ); neither proof names it a Galois connection, a
  naming the field's and not these papers'.
