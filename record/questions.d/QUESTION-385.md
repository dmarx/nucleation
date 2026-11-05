---
number: 385
status: Open
formerly:
- QUESTION-tmpkcffa
title: 'Under what conditions do systems on different substrates implement the same algebra of constrained realizability, up to a stated resource overhead and level of observation, and which of its properties depend on a substrate''s geometry rather than on the pattern of constrained interaction?'
version: 1
tags:
- complex-systems
- mathematics
- philosophy-of-science
date: '2026-11-05'
line:
- realizability
summary: >-
  A's question, from the pasted synthesis on resource-bounded realizability
  (three responses, pasted by the owner on 2026-11-05, continuing the
  exchange on constraint architectures), Response 3 §§10 and 11, with A's
  two experimental programmes (Response 2 §5 and Response 3 §10): three
  implementations of one small constraint architecture, rigid origami, a
  finite constraint network and an organizational model, translated into
  one another, measuring compatibility, directed reachability, Pareto
  frontiers of resources, complexity under scaling, robustness and
  architectural plasticity, starting from the degree-4 vertex of
  [CASE-206](../cases.d/CASE-206.md) and extending to networks of vertices. [CLAIM-573](../claims.d/CLAIM-573.md) is
  the hypothesis it would test. The wording is A's; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-206 CLAIM-556 CLAIM-560 CLAIM-566 CLAIM-567 CLAIM-571 CLAIM-573 CLAIM-585 TERM-111 — Proposed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# QUESTION-385: Under what conditions do systems on different substrates implement the same algebra of constrained realizability, up to a stated resource overhead and level of observation, and which of its properties depend on a substrate's geometry rather than on the pattern of constrained interaction?

## Why it is a question

A (Response 3 §11): "Under what conditions do different systems implement
the same algebra of constrained realizability, up to a specified resource
overhead and level of observation?" And (§10): "Which properties depend on
the geometry of paper, and which depend only on the pattern of constrained
computational interaction?" "If the same properties survive translation
into a non-geometric constraint network, they become candidates for
universality."

The record holds the pieces a comparison would measure, each on one
substrate: the compatibility complex ([CLAIM-347](../claims.d/CLAIM-347.md)), feasible against
reachable ([CLAIM-567](../claims.d/CLAIM-567.md)), the bottleneck threshold and its frontier with
several resources ([CLAIM-571](../claims.d/CLAIM-571.md), [CLAIM-585](../claims.d/CLAIM-585.md)), the two filtrations
([CLAIM-560](../claims.d/CLAIM-560.md)), the obstruction levels ([CLAIM-556](../claims.d/CLAIM-556.md)), assembly,
persistence and regeneration ([CLAIM-566](../claims.d/CLAIM-566.md)), and the senses of
universality a result could claim ([TERM-111](../terms.d/TERM-111.md)). It holds no translation
between substrates.

## What would answer it

A's programmes give one route. Response 2 §5: three implementations of a
small constraint architecture, "one using rigid origami, one as a finite
computational transition system, and one as an abstract organizational
model", with translations of states, demands and operations, testing
whether these are preserved:

1. "The pattern of compatible and incompatible demand sets."
2. "The emergence of new reachable states as budgets increase."
3. "The Pareto structure of minimal resources needed for transitions."
4. "The distinctions between possible, controllable, reliable, and
   regenerable configurations."

For the computational sense, "bounded overhead across families of
increasingly large systems". Response 3 §10 orders six measurements:
compatibility and its minimal non-faces, directed transition graphs,
Pareto frontiers, the scaling of solution and reconfiguration complexity,
robustness to noise and imperfect actuation and observation, and
"Architectural plasticity: Which changes to the constraint architecture
create genuinely new capabilities, and which only lower the cost of
existing ones?", the last being [QUESTION-392](QUESTION-392.md). "The first experiment
could use the degree-four origami vertex already constructed in PR [#401](https://github.com/dmarx/nucleation/issues/401),
then extend to assemblies of multiple vertices", [CASE-206](../cases.d/CASE-206.md), because "A
single vertex may reveal bifurcations and resource barriers. A network of
vertices may reveal frustration, combinatorial branching, difficult
control problems, and emergent computational structure."

An answer would be a stated class of translations, with the properties
each preserves and the families over which it does, and a property found
to survive translation into a constraint network with no geometry, or one
shown to depend on the paper.

## What would not answer it

A: "Agreement in one small example would be evidence of a shared model,
not a universality theorem." Nor would agreement by translations that
declare the target's transition graph directly ([TERM-111](../terms.d/TERM-111.md)), nor
sameness of complexity class alone, which families whose reconfiguration
is PSPACE-complete already share. An organizational model with no declared
size parameter cannot enter the comparison under scaling.

## Note of 2026-11-05: A's fourth paste, and the assistant's contributions

A's fourth paste proposes extending the experiments "to families of increasing size, looking for complexity separations or scaling laws". No status changes.
