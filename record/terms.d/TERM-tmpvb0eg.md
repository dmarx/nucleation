---
status: Proposed
title: 'relational profiles of a configuration, and which: incoming, the cost of producing it from each other configuration; outgoing, the cost of turning it into each; observational, what the tests affordable at a budget can tell it from, with the minimum distinguishing budget at a threshold; and maintenance, what preserves or regenerates its enabling constraints, which Yoneda does not supply'
version: 1
tags:
- mathematics
- individuation
- epistemology
date: '2026-11-05'
line:
- realizability
complements:
- TERM-tmpr3hl8
summary: >-
  A's proposal, from the owner's paste of 2026-11-05 (fourth), A's "Toward a
  resource-sensitive Yoneda theory of individuation" §§4 and 5: the incoming
  and outgoing capability profiles Y^−(x): p ↦ d(p,x) and Y^+(x): p ↦ d(x,p),
  A's four profiles, incoming, outgoing, observational and maintenance, and
  for the observational one the operational distinguishability
  D_b(A,B) = sup over tests affordable at b of total variation, with the
  minimum distinguishing budget B*_ε(A,B) = inf{b: D_b(A,B) > ε}. Filed as a
  term with senses, so a claim about "the profile" of a configuration says
  which. D_b is [CLAIM-302](../claims.d/CLAIM-302.md)'s d_r; the incoming, outgoing and maintenance
  profiles are the price lists of [CLAIM-tmpancvu](../claims.d/CLAIM-tmpancvu.md)'s three requirements. The
  filer adds, checked with python3 -I, that exact indistinguishability at a
  budget sorts systems into classes that only split as the budget grows,
  while at a positive threshold the relation is intransitive, as A says.
  The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmp0d5si CLAIM-tmp42yq0 CLAIM-tmpancvu CLAIM-tmpg7w69 CLAIM-tmpq06t8 CLAIM-tmpxcbet TERM-088 TERM-tmpr3hl8 — Proposed; A's proposals of 2026-11-04 and 2026-11-05, the assistant's own and the entries filed beside them, and the record's open term for the senses of individuation, cited as filed, nothing here resting on their being settled -->

# TERM-tmpvb0eg: relational profiles of a configuration, and which: incoming, the cost of producing it from each other configuration; outgoing, the cost of turning it into each; observational, what the tests affordable at a budget can tell it from, with the minimum distinguishing budget at a threshold; and maintenance, what preserves or regenerates its enabling constraints, which Yoneda does not supply

## Definition

For a configuration x of a resource-bounded constraint system
([TERM-tmpr3hl8](TERM-tmpr3hl8.md)), with d(x, y) the least cost of a process from x to y
(A §2: "d(x,y)=inf_{p:x→y} κ(p)"), A (§4) separates four profiles:

| Profile | A's "Fundamental question" | definition |
|---|---|---|
| **Incoming** | "What can produce this configuration, and at what cost?" | Y^−(x): p ↦ d(p,x) |
| **Outgoing** | "What can this configuration produce or transform into?" | Y^+(x): p ↦ d(x,p) |
| **Observational** | "What interactions distinguish it from alternatives?" | D_b(x, −), below |
| **Maintenance** | "What processes preserve or regenerate its enabling constraints?" | not defined by A |

A on their status: "The first two fit naturally into ordinary
enriched-categorical machinery. The third requires an explicit account of
measurements or tests, not merely treating all morphisms as observations.
The fourth requires additional process dynamics and dependence
structures. It is not supplied by Yoneda itself." And: "That last
qualification is crucial. Otherwise we would be redescribing Nucleation's
individuation concepts in categorical terminology without gaining
explanatory power."

**Incoming and outgoing.** Y^− "records the cost of producing x from other
configurations" and Y^+ "the cost of transforming x into other
configurations"; they are "related to the contravariant and covariant
representable constructions in enriched category theory". Why both: "a
system may be easy to assemble but hard to change once assembled, or
difficult to construct but easy to modify after construction." Under
additive costs either profile recovers d: A's d(x,y)=sup_p [d(p,y)−d(p,x)]
for the incoming one, checked on A's toy in [CASE-tmp0d5si](../cases.d/CASE-tmp0d5si.md), where the
incoming profiles are the columns of the cost table and the outgoing ones
its rows.

**Observational.** A (§5): with 𝒯_b "the tests executable within budget b,
including their preparation and evaluation costs", and P_t^A the outcome
law of test t on A,

D_b(A,B)= sup_{t∈𝒯_b} TV(P_t^A,P_t^B).

"For a fixed shared test family, D_b is a pseudometric. If test
repertoires expand with budget, then b_1 ≤ b_2 ⟹ D_{b_1}(A,B) ≤
D_{b_2}(A,B)." The **minimum distinguishing budget** at threshold ε is

B*_ε(A,B) = inf{b: D_b(A,B) > ε},

"the minimum distinguishing budget at a specified discrimination
threshold". A: "It's a proposed measure, but it captures a real
computational question: How much computation must be available before a
specified difference between two systems becomes operationally
detectable?" A's caution: "This is not, by itself, a Yoneda construction.
It is an operational measurement structure that we can place alongside
the categorical one."

**Maintenance** has no formula. A (§4): "A structure may be easy to
construct, difficult to maintain, and impossible to regenerate without
external intervention."

## What it adds to what the record holds

- **D_b is held.** [CLAIM-302](../claims.d/CLAIM-302.md) defines, from A15, d_r(x, x′) = sup over f in
  F_r of |E[f | x] − E[f | x′]|, total variation over all tests, growing
  with nested families, with its pseudorandom witness: "Equivalence under
  feasible tests can be much coarser than statistical equivalence". A's
  gloss on that witness (§5): "Resource-bounded indistinguishability is
  not an absence of difference. It is a mathematically constrained
  limitation on the ability to realize a distinction." New here is the
  threshold budget B*_ε and the profile's place beside the other three.
- **The monotonicity is held** for exact comparison over nested families
  ([CLAIM-tmpg7w69](../claims.d/CLAIM-tmpg7w69.md)), and its opposite on the side of acting
  ([CLAIM-tmp42yq0](../claims.d/CLAIM-tmp42yq0.md); [QUESTION-tmp3icc7](../questions.d/QUESTION-tmp3icc7.md)). B*_ε is the observing counterpart
  of the transition threshold: the least observing budget that splits a
  pair, against the least acting budget that joins them ([CLAIM-tmpxcbet](../claims.d/CLAIM-tmpxcbet.md)'s
  enriched hom; [CLAIM-tmpq06t8](../claims.d/CLAIM-tmpq06t8.md)).
- **Three requirements, priced per configuration.** [CLAIM-tmpancvu](../claims.d/CLAIM-tmpancvu.md): a form
  has resource requirements "to construct it, to maintain it, and to move
  into or out of it", and none fixes another. The incoming profile prices
  the first, the outgoing the third, and the maintenance profile is the
  second, which, as A says, no representable supplies.
- **The senses of individuation they serve.** The observational profile is
  [TERM-088](TERM-088.md)'s descriptive sense at a budget; the maintenance profile bears
  on its autonomy sense. Incoming and outgoing profiles are positions in a
  space of costed transformations, which A (§3) calls "effective
  individuation" and [TERM-088](TERM-088.md) does not list.

## Threshold and transitivity (the filer's)

A: "the relation D_b(A,B) ≤ ε need not be transitive for positive ε. It is
an approximate similarity relation, not automatically an equivalence
relation." Instance: one test reading a coin of bias 0, 0.1 or 0.2 gives
TV 0.1, 0.1 and 0.2, so at ε = 0.15 the first and second are within ε, the
second and third are, and the first and third are not.

What does hold is a weakened triangle. Since each D_b is a pseudometric,
for every A, B, C and ε ≥ 0,

B*_{2ε}(A,C) ≥ min(B*_ε(A,B), B*_ε(B,C)),

because below the smaller budget both pairs are within ε, so A and C are
within 2ε. At ε = 0 this is B*_0(A,C) ≥ min(B*_0(A,B), B*_0(B,C)): exact
indistinguishability at a budget is an equivalence relation, its classes
only split as the budget grows, and they form one tree, as [CLAIM-tmpq06t8](../claims.d/CLAIM-tmpq06t8.md)
finds for reachability under peak costs. At ε > 0 the inequality at a
single threshold fails. Checked with python3 -I: on 4,000 random systems
of three over six tests with costs 1 to 5, D_b was monotone in b, the
2ε-inequality held in all 16,000 cases at ε in {0, 0.05, 0.1, 0.2}, and an
example breaking it at one threshold, ε = 0.15, was found.

## What it is not

- **A claim that the four profiles exhaust a configuration.** A says "at
  least four".
- **Defined for every resource semantics.** Incoming and outgoing profiles
  as written need a scalar cost; with several resources a distance is an
  up-set of budgets ([TERM-tmpr3hl8](TERM-tmpr3hl8.md)).
- **A theory of maintenance.** The fourth profile is named, not built.
- **Individuation of individuals.** A profile of any of the four kinds
  characterizes a configuration; whether relations constitute it is
  another question ([THEORY-032](../theory.d/THEORY-032.md); [CLAIM-150](../claims.d/CLAIM-150.md)).

## What would settle it

Adoption by the owner, or a claim of the record's own that names which
profile it means.
