---
number: 590
status: Active
formerly:
- CLAIM-tmpxcbet
title: 'Which category is chosen changes which configurations count as the same: in the fundamental groupoid of a degree-4 vertex''s configuration space every two configurations are uniquely isomorphic, while in the category enriched in peak footprint under maximum its two folded states are 1.866 apart in each direction and each is 0 from itself, a distance the enriched Yoneda embedding keeps, so equivalence of possibilities is not equivalence of resource-bounded capabilities'
version: 4
history:
- version: 2
  date: '2026-11-06'
  note: >-
    At the twenty-sixth status review (ADR-057), at the status review's ruling (the owner delegated these rulings): THEORY-1376
    leaves grounds (ADR-058), since the body cites Lawvere for A's naming
    and for the additive case, an attribution, and the max case and its
    quantale check are the filer's and CLAIM-563's, as CLAIM-563 ruled on
    2026-11-06. No status change.
- version: 3
  date: '2026-11-06'
  note: >-
    Promoted at the twenty-seventh status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings). Its note of
    2026-11-06 waited on "CASE-206 held, or the two-mode structure
    re-derived here"; CASE-206 now derives that the two folding modes are
    the whole configuration space and is Active at the same review, so the
    space is two arcs crossing at the flat state, contractible, as the
    claim takes it. Its premises, CLAIM-571, CLAIM-563, CASE-206,
    THEORY-032 and TERM-114, are Active, no objection is filed, and the
    bound on the distance between enriched profiles was re-checked.
    Nothing in the record meets its defeated_if.
- version: 4
  date: '2026-11-06'
  note: >-
    Corrected at the twenty-seventh status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings), on the full reading
    of Lawvere (NOTE-1585): the body credited the max base to the readings'
    quantale check and said "The max case is the filer's"; Lawvere gives
    R_cart (p. 152) and states the Yoneda Lemma for any closed V (p. 154),
    so the filer's argument re-derives a case of his theorem. THEORY-1376,
    Active at the same review, is added to corroborated_by (ADR-058). No
    status change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a loop in the vertex's configuration space
  that is not contractible, so that the groupoid has two path classes
  between some pair of configurations; a path from one folded state to the
  other whose largest footprint is below 1 + √3/2; a failure of
  d(q, q″) ≤ max(d(q, q′), d(q′, q″)) for the minimax distance; or a pair
  of configurations whose representable profiles in the max-enriched
  category are at a distance other than theirs. Also an error in the
  coordinates or footprints of the folded states taken from the case. Not
  defeated by another choice of resource, under which the distances
  differ and the point, that the enrichment decides them, stands; nor by
  the toy's smallness, since it is an instance, not a classification.
tags:
- mathematics
- individuation
- complex-systems
date: '2026-11-05'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-571
- CLAIM-563
grounds:
- CASE-206
- THEORY-032
complements:
- CLAIM-574
- CLAIM-583
uses:
- TERM-114
bears_on:
- QUESTION-031
- QUESTION-385
- QUESTION-393
summary: >-
  A's proposal, from the owner's paste of 2026-11-05 (latest), A's "Yoneda,
  individuation, and resource-bounded objects" §§3 and 7, with §1 of the
  paste before it: "Yoneda does not tell us which category to use", the
  path groupoid of a configuration space identifies the configurations of a
  component and so "does not, by itself, preserve the resource barrier",
  and a declared enrichment, as in Lawvere metric spaces, keeps it. Shown
  here on the degree-4 vertex of [CASE-206](../cases.d/CASE-206.md). The groupoid of its
  contractible configuration space makes every two configurations uniquely
  isomorphic; the category enriched in ([0, ∞], ≥, max, 0), with the
  bottleneck footprint as hom, puts the two folded states 1 + √3/2 ≈ 1.866
  apart, and its Yoneda embedding is an isometry. The mirror of the fold is
  a symmetry of the category, not an automorphism of any configuration.
  Checked by the filer with python3 -I. The construction is the filer's,
  from A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-204 — Proposed or Skimmed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# CLAIM-590: Which category is chosen changes which configurations count as the same: in the fundamental groupoid of a degree-4 vertex's configuration space every two configurations are uniquely isomorphic, while in the category enriched in peak footprint under maximum its two folded states are 1.866 apart in each direction and each is 0 from itself, a distance the enriched Yoneda embedding keeps, so equivalence of possibilities is not equivalence of resource-bounded capabilities

## The claim

A ("Yoneda, individuation, and resource-bounded objects", §3): "Yoneda
does not tell us which category to use. And different choices of category
give different notions of object identity." For a category whose objects
are the configurations of a rigid-origami mechanism and whose morphisms
are folding paths up to homotopy, "This is essentially the fundamental
groupoid of the configuration space. Within a connected component, any two
configurations are isomorphic." Then: "The unrestricted path groupoid
remembers that the transition exists. It does not, by itself, preserve the
resource barrier", and "Equivalence of possibilities ≠ equivalence of
resource-bounded capabilities." A's caution: "we must not simply declare
two configurations categorically different because their costs differ. We
need to specify a resource-sensitive category or enrichment in which those
differences are retained", for example Lawvere metric spaces, in which
"the enriched Yoneda embedding preserves those distances". A names the
degree-four vertex as the instance; here it is worked.

**The space.** [CASE-206](../cases.d/CASE-206.md)'s vertex, sector angles 60°, 90°, 120° and
90°, has two folding modes, each one curve through the flat state, meeting
only there. The configuration space is two arcs crossing at one point,
which is contractible. Its two folded states are A = (−90°, 150°, 90°,
150°) on mode A, footprint 0.75, and B = (150°, −90°, 150°, 90°) on mode
B, footprint 0.875. Every path between them passes the flat state, of
footprint 1 + √3/2 ≈ 1.866.

**Category 1: the fundamental groupoid.** In a contractible space any two
paths with the same ends are homotopic, so Π₁ has exactly one morphism
between any two configurations, and it is invertible. Every two
configurations are isomorphic, every automorphism group is trivial, and by
Yoneda ([THEORY-032](../theory.d/THEORY-032.md)) Y(A) ≅ Y(B) for all A and B. The groupoid cannot tell
A from B, nor either from the flat state.

**Category 2: enriched in peak footprint.** Take the base
([0, ∞], ≥, max, 0), Lawvere's R_cart (1973, p. 152), which the readings of
Lawvere and of Marsden and Zwart check is a commutative quantale ([NOTE-1585](../notes.d/NOTE-1585.md); [CLAIM-563](CLAIM-563.md)).
Let the hom from q to q′ ≠ q be [CLAIM-571](CLAIM-571.md)'s bottleneck,
d(q, q′) = inf over paths of the largest footprint along the path, and let
d(q, q) = 0, the identity process costing the unit, as in the free
category on the configuration graph. Composition is
d(q, q″) ≤ max(d(q, q′), d(q′, q″)), which holds because paths
concatenate. Then:

| | to A | to B |
|---|---|---|
| from A | 0 | 1.866 |
| from B | 1.866 | 0 |

An isomorphism in this category needs d(A, B) = d(B, A) = 0, the unit, so
A and B are not isomorphic. The mirror of A, (90°, −150°, −90°, −150°),
is also 1.866 from A, as the case finds for the snap.

**The enriched Yoneda embedding keeps the threshold.** The internal hom of
the base is [a, b] = b if b > a and 0 otherwise. The distance between the
profiles d(−, A) and d(−, B) is sup over X of [d(X, A), d(X, B)]. At X = A
it is d(A, B). For any X, d(X, B) ≤ max(d(X, A), d(A, B)), so when
d(X, B) > d(X, A) it is at most d(A, B). So the distance between profiles
is d(A, B) = 1.866: the threshold survives as the distance between
relational profiles. [QUESTION-031](../questions.d/QUESTION-031.md) records the additive case: "For Lawvere
metric spaces the Yoneda embedding is an isometry (Lawvere 1973)". The
max case is a case of Lawvere's Yoneda Lemma, stated "for any closed V and
any V-category A" (p. 154); the argument above is the filer's
re-derivation of it.

**Between the two, a filtration.** For each budget b, the groupoid of the
sublevel set {q : r(q) ≤ b} has A ≅ B exactly when b ≥ 1.866; at 1.5 it
has four components, as in [CASE-206](../cases.d/CASE-206.md). The enriched hom is the least b
at which the sublevel groupoids identify the two states. So the groupoid
is the enriched category with every cost forgotten, and the sublevel
groupoids keep the costs a budget at a time.

**Symmetry, in the same space** (A, §7: "categorical automorphisms need not
coincide with the geometric rotations or reflections of the physical
object"). Negating every fold angle, σ(ρ) = −ρ, reflects the folded vertex
in the table's plane. It maps each mode to itself, since each mode's
relations are odd, and it leaves the plan footprint unchanged. So σ is an
automorphism of the groupoid and an isometry of the enriched category. It
is not an automorphism of any configuration: in the groupoid every
Aut(q) is trivial, and in the enriched category σ moves A to a state 1.866
away. The geometric symmetry is a symmetry of the category, acting on its
objects, and Yoneda's Aut_𝒞(A) ≅ Aut(Y(A)) does not see it.

**Checked** by the filer with python3 -I (numpy), on [CASE-206](../cases.d/CASE-206.md)'s
coordinates: closure at A and B to 5 × 10⁻¹⁶; footprints 0.75, 0.875 and
1.866025 at A, B and flat; on 400-point samples of each half-branch, the
largest footprint off flat below the flat value; minimax distances
d(A, B) = d(B, A) = 1.866025 and d(A, mirror of A) = 1.866025; no failure
of the max-triangle inequality over 62 sampled states; the distance
between enriched profiles equal to d on every sampled pair; A and B in
different sublevel components at 1.5 and joined at 1.866; and
r(−q) = r(q) on every sampled state. The configuration graph is a tree,
one hub and four paths, as contractibility requires.

## What it does not say

- **Which category is right.** Both are legitimate; they answer different
  questions. The groupoid asks what is possible, the enriched category
  what is possible at what peak. A's caution stands: the costs count only
  once an enrichment is declared, and declaring one is a choice of
  regime.
- **That the distances are the vertex's.** They are the declared
  footprint's. Under [CASE-206](../cases.d/CASE-206.md)'s alternative crease energy, least at
  flat, the bottleneck is max(E(A), E(B)) and the barrier is gone. The
  paths are the same.
- **That every resource enriches.** A cumulative expenditure composes by
  sum, and its affordable processes are not closed at a finite budget
  ([CLAIM-563](CLAIM-563.md)); several resources need up-sets of budgets as homs. The
  max base is the case where the enrichment is straightforward.
- **That differing in the enriched category is being distinct
  individuals.** The configurations are states of one mechanism; the
  enrichment separates states by what it costs to pass between them, which
  is A's "resource-bounded capabilities", not a claim about what the
  mechanism is ([THEORY-032](../theory.d/THEORY-032.md)'s presupposition of the objects).
- **That disconnected states are covered.** A vertex whose states lie in
  different components ([CASE-204](../cases.d/CASE-204.md)) is told apart by the groupoid as
  well; the case here is the one where only the enrichment tells.

## Note of 2026-11-05: A's fourth paste, and the assistant's contributions

[CLAIM-581](CLAIM-581.md) states this claim's max-enriched hom as an ultrametric when moves are reversible, so the sublevel groupoids here nest into one merge tree as the budget grows; the additive base gives no such tree, as A's U/L/R toy ([CASE-199](../cases.d/CASE-199.md)) shows. No status changes.

## Note of 2026-11-06: what holds it back

It takes the vertex's configuration space, two folding modes meeting only at the flat state, and the folded states' coordinates from [CASE-206](../cases.d/CASE-206.md), which is Proposed and rests on Foschi, Hull and Ku's equations as read in part in [NOTE-1606](../notes.d/NOTE-1606.md). The filer's check samples those branches but does not derive them; [CASE-206](../cases.d/CASE-206.md) held, or the two-mode structure re-derived here, is what is missing.

## Note of 2026-11-06: Claude, read

Lawvere states the Yoneda Lemma "for any closed V and any V-category A" (1973, p. 154; [NOTE-1585](../notes.d/NOTE-1585.md)), and says of R_cart, his max base, that "all of our general results may be reinterpreted as applying to ultrametric spaces" (p. 152). The internal hom used here, [a, b] = b if b > a and 0 otherwise, is his Hom for R_cart. So the max-enriched Yoneda step is a case of his theorem, and the filer's argument re-derives it; the body is corrected. [THEORY-1376](../theory.d/THEORY-1376.md) corroborates. No status change.

## Note of 2026-11-06: its blockers spent

The note of 2026-11-06 headed "what holds it back" names two things to wait for, and both are now met. [CASE-206](../cases.d/CASE-206.md) has been Active since the twenty-seventh status review. [NOTE-1606](../notes.d/NOTE-1606.md), Foschi, Hull and Ku's equations, is now Read: the reading is complete and its equations are checked. No status change.
