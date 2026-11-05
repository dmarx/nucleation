---
number: 119
status: Active
formerly:
- CASE-tmpuuf3p
title: 'Three demands each requiring one coordinate of an outcome to equal 1, with attainable outcomes (1,1,0), (1,0,1) and (0,1,1): every pair is jointly satisfiable and the triple is not, and a new composite policy that can also produce (1,1,1) relieves the frustration by enlarging the attainable set, with the acceptance sets unchanged and no demand suppressed'
version: 1
standing: fictional
kind: construction
tags:
- mathematics
- self-governance
- ecology
date: '2026-10-18'
line: distributed-agency
summary: >-
  From the synthesis the owner relayed on 2026-10-18. A compatibility
  complex with all three edges and no filled triangle, the minimal
  structurally frustrated collection of [CLAIM-347](../claims.d/CLAIM-347.md) with three members.
  When the organization acquires a composite operation that can produce
  (1,1,1), ℛ(𝒪) ⊊ ℛ(𝒪′) and the complex gains the triangle: relief in
  [CLAIM-347](../claims.d/CLAIM-347.md)'s sense, by changing what is attainable, not by weakening a
  demand. The construction says such relief is possible; whether
  specialization produces it is [QUESTION-133](../questions.d/QUESTION-133.md).
supports:
- CLAIM-449
---
<!-- inactive-ok-file: CLAIM-534 CLAIM-553 — Proposed, Deferred, Unavailable or new; cited from the exchange "Organizational Nucleation and SLT" of 2026-11-04 as open -->

# CASE-119: Three demands each requiring one coordinate of an outcome to equal 1, with attainable outcomes (1,1,0), (1,0,1) and (0,1,1): every pair is jointly satisfiable and the triple is not, and a new composite policy that can also produce (1,1,1) relieves the frustration by enlarging the attainable set, with the acceptance sets unchanged and no demand suppressed

## The construction

Outcomes are y ∈ {0, 1}³. Demand i requires y_i = 1, so
A_i = {y : y_i = 1}. The organization 𝒪 can attain

  ℛ(𝒪) = {(1,1,0), (1,0,1), (0,1,1)}.

- For each pair i ≠ j, ℛ(𝒪) ∩ A_i ∩ A_j ≠ ∅: (1,1,0) meets demands 1 and 2,
  (1,0,1) meets 1 and 3, (0,1,1) meets 2 and 3.
- ℛ(𝒪) ∩ A₁ ∩ A₂ ∩ A₃ = ∅: no attainable outcome has all three
  coordinates 1.

So 𝒦(𝒪) has every vertex and edge and no triangle. {1, 2, 3} is a
minimal structurally frustrated collection ([CLAIM-347](../claims.d/CLAIM-347.md)).

**The reorganization.** Through differentiation and coordination the
organization acquires a new composite policy that can also produce
(1,1,1). Then ℛ(𝒪) ⊊ ℛ(𝒪′) = ℛ(𝒪) ∪ {(1,1,1)}. The acceptance sets are
unchanged, no demand is removed or weakened, and 𝒦(𝒪′) gains the
triangle, losing nothing. By [CLAIM-347](../claims.d/CLAIM-347.md) this is relief of structural
frustration.

## What it shows

Some organizational conflicts are not problems of choosing among
competing demands. They are problems of functional organization: the
existing repertoire cannot realize a jointly demanded outcome, and a
differentiated or recomposed repertoire can. This is [CASE-115](CASE-115.md)'s
point (a split of a shared parameter removes a frustration) in
combinatorial form, and it is the first of [CLAIM-360](../claims.d/CLAIM-360.md)'s three effects, a
larger realizable set, rather than a better choice within the old one.

It also shows pairwise compatibility failing to fix collective
compatibility. Every pair is compatible and the triple is not, as in
ecological communities where pairwise coexistence does not determine
multispecies coexistence (Hofbauer and Schreiber 2022 on invasion
graphs). [THEORY-598](../theory.d/THEORY-598.md) is the caution in the other direction: some apparent
higher-order dynamics reduce to pairwise interactions. Here the
higher-order fact is real: the complex is not determined by its
1-skeleton.

## What it does not show

That specialization tends to produce such relief. Differentiation can
also add costs or dependencies and shrink what is attainable. Whether and
when it enlarges ℛ is [QUESTION-133](../questions.d/QUESTION-133.md).

## Note of 2026-11-04: a budget form with intervention probabilities, from "Organizational Nucleation and SLT"

A16 §5, answering the owner's U15, gives this case in continuous form.
Three perspectives share two units of governing opportunity:
x_i ≥ 0, x_i ≤ 1, Σx_i ≤ 2. Each wants one unit, with discrepancy
d_i = 1 − x_i and tolerance 0.2, so each accepts x_i ≥ 0.8.

- Any pair needs 1.6 units, so every pair is jointly satisfiable.
- The triple needs 2.4, so it is not. The complex is ∂Δ², and the minimal
  conflict has three members, as here.
- With intervention probability σ(16(d − τ)), the owner's corrected form
  of U15's complaint probability (U17), every feasible allocation leaves
  some perspective at least at σ(16(1/3 − 0.2)) ≈ 0.894. The best is
  x_i = 2/3. "It cannot eliminate the underlying conflict; it can only
  distribute the departures from each perspective's ideal."

The reader rechecked this: a grid search gives min-max discrepancy 1/3, and
σ(2.133) = 0.8941. A16 calls the result "the distinction between
**resolving a conflict** and **governing an unavoidable conflict**". In this
case's terms, the second is [CLAIM-534](../claims.d/CLAIM-534.md)'s allocation, and relief would need a
larger budget or a composite policy, as here.

It is a variant, not a new construction. Its use is [CLAIM-553](../claims.d/CLAIM-553.md).
No status changes.

## Note of 2026-11-05: the constraint-architecture readings

Stern et al. ([NOTE-1571](../notes.d/NOTE-1571.md)), from the pasted synthesis on constraint architectures, support the case's use as the combinatorial twin of a frustrated loop of origami vertices: every open chain of 4-vertices has a zero-energy branch assignment and closing the loop removes it, as here every pair of demands is satisfiable and the triple is not. The minimal mechanical loop has four vertices, not three, and the designed branch is jointly realizable, so the parallel is with the distractor branches, not the target. The paper has nothing answering to the case's relief by a new composite policy. No status changes.
