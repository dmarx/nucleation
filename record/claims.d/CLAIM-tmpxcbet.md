---
status: Proposed
title: 'Which category is chosen changes which configurations count as the same: in the fundamental groupoid of a degree-4 vertex''s configuration space every two configurations are uniquely isomorphic, while in the category enriched in peak footprint under maximum its two folded states are 1.866 apart in each direction and each is 0 from itself, a distance the enriched Yoneda embedding keeps, so equivalence of possibilities is not equivalence of resource-bounded capabilities'
version: 1
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
- formal-apparatus
rests_on:
- CLAIM-tmpbi4ca
- CLAIM-tmp7bxc0
grounds:
- CASE-tmpe48yq
- THEORY-032
- THEORY-tmp5ebls
complements:
- CLAIM-tmpg7w69
- CLAIM-tmpsbz28
uses:
- TERM-tmpr3hl8
bears_on:
- QUESTION-031
- QUESTION-tmpkcffa
- QUESTION-tmptcuch
summary: >-
  A's proposal, from the owner's paste of 2026-11-05 (latest), A's "Yoneda,
  individuation, and resource-bounded objects" §§3 and 7, with §1 of the
  paste before it: "Yoneda does not tell us which category to use", the
  path groupoid of a configuration space identifies the configurations of a
  component and so "does not, by itself, preserve the resource barrier",
  and a declared enrichment, as in Lawvere metric spaces, keeps it. Shown
  here on the degree-4 vertex of CASE-tmpe48yq. The groupoid of its
  contractible configuration space makes every two configurations uniquely
  isomorphic; the category enriched in ([0, ∞], ≥, max, 0), with the
  bottleneck footprint as hom, puts the two folded states 1 + √3/2 ≈ 1.866
  apart, and its Yoneda embedding is an isometry. The mirror of the fold is
  a symmetry of the category, not an automorphism of any configuration.
  Checked by the filer with python3 -I. The construction is the filer's,
  from A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpb5t9j CASE-tmpe48yq CLAIM-tmp7bxc0 CLAIM-tmpbi4ca NOTE-tmpegumv — Proposed or Skimmed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# CLAIM-tmpxcbet: Which category is chosen changes which configurations count as the same: in the fundamental groupoid of a degree-4 vertex's configuration space every two configurations are uniquely isomorphic, while in the category enriched in peak footprint under maximum its two folded states are 1.866 apart in each direction and each is 0 from itself, a distance the enriched Yoneda embedding keeps, so equivalence of possibilities is not equivalence of resource-bounded capabilities

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

**The space.** CASE-tmpe48yq's vertex, sector angles 60°, 90°, 120° and
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
Yoneda (THEORY-032) Y(A) ≅ Y(B) for all A and B. The groupoid cannot tell
A from B, nor either from the flat state.

**Category 2: enriched in peak footprint.** Take the base
([0, ∞], ≥, max, 0), which the readings of Lawvere and of Marsden and
Zwart check is a commutative quantale (NOTE-tmpegumv; CLAIM-tmp7bxc0).
Let the hom from q to q′ ≠ q be CLAIM-tmpbi4ca's bottleneck,
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
relational profiles. QUESTION-031 records the additive case: "For Lawvere
metric spaces the Yoneda embedding is an isometry (Lawvere 1973)". The
max case is the filer's, by the argument above.

**Between the two, a filtration.** For each budget b, the groupoid of the
sublevel set {q : r(q) ≤ b} has A ≅ B exactly when b ≥ 1.866; at 1.5 it
has four components, as in CASE-tmpe48yq. The enriched hom is the least b
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

**Checked** by the filer with python3 -I (numpy), on CASE-tmpe48yq's
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
  footprint's. Under CASE-tmpe48yq's alternative crease energy, least at
  flat, the bottleneck is max(E(A), E(B)) and the barrier is gone. The
  paths are the same.
- **That every resource enriches.** A cumulative expenditure composes by
  sum, and its affordable processes are not closed at a finite budget
  (CLAIM-tmp7bxc0); several resources need up-sets of budgets as homs. The
  max base is the case where the enrichment is straightforward.
- **That differing in the enriched category is being distinct
  individuals.** The configurations are states of one mechanism; the
  enrichment separates states by what it costs to pass between them, which
  is A's "resource-bounded capabilities", not a claim about what the
  mechanism is (THEORY-032's presupposition of the objects).
- **That disconnected states are covered.** A vertex whose states lie in
  different components (CASE-tmpb5t9j) is told apart by the groupoid as
  well; the case here is the one where only the enrichment tells.
