---
number: 392
status: Open
formerly:
- QUESTION-tmpt9dhv
title: 'When does an intervention on a constraint architecture create a capability the system lacked, rather than make one it already had cheaper, faster or more reliable to reach, and how can the two be told apart?'
version: 1
tags:
- operations-research
- society-and-governance
- control-theory
date: '2026-11-05'
line:
- realizability
- readiness
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4. A's table of
  what each intervention changes: a budget changes the resource-feasible
  part of the same configuration space, crease or linkage constraints the
  space itself, prestress the energy landscape, actuator placement the
  controlled reachable set, the folding schedule peak need and completion
  time, a maintained reserve reliability under uncertain demand. A asks
  "whether a proposed change genuinely creates new capabilities or merely
  makes already available ones less expensive", and proposes an
  experiment over states A, B and a staging C. No held question asks it;
  [CLAIM-357](../claims.d/CLAIM-357.md)'s split of structural frustration from governance regret is
  its nearest relative. The wording is A's; adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-568 CLAIM-586 CLAIM-571 CASE-198 TERM-115 — Proposed; A's proposals of 2026-11-04 and the entries filed beside them, cited as filed -->
<!-- inactive-ok-file: CLAIM-566 CASE-210 — Proposed or new; entries of 2026-11-05 from the pasted synthesis on constraint architectures, cited as open -->
<!-- inactive-ok-file: CLAIM-556 — Proposed or new; the resource-bounded realizability readings of 2026-11-05, cited as open -->

# QUESTION-392: When does an intervention on a constraint architecture create a capability the system lacked, rather than make one it already had cheaper, faster or more reliable to reach, and how can the two be told apart?

## Why it is a question

A's table pairs each kind of intervention with what it changes:

| intervention | what it changes |
|---|---|
| increase a budget | the resource-feasible subset of the same configuration space |
| change crease or linkage constraints | the configuration space itself |
| change prestress | the energy landscape and the dynamically accessible paths |
| change actuator placement | the controlled reachable set |
| change the folding schedule | peak resource needs and completion time |
| add a maintained reserve | reliability under uncertain future demands |

The table's wording is the filer's summary of A's. A: "We could then ask
whether a proposed change genuinely creates new capabilities or merely
makes already available ones less expensive. That distinction is very
close to Nucleation's distinction between structural frustration and
governance regret." [CLAIM-357](../claims.d/CLAIM-357.md) separates the two: a positive frustration
residual says no admissible update meets the requirements, a positive
regret only that the actual update does worse than the best. On the
table's reading, only the second row changes what is possible at all;
the others change what is affordable, reachable by the inputs, reliable
or timely within a fixed space.

The record has pieces of an answer. [CLAIM-586](../claims.d/CLAIM-586.md) shows that a budget
enlarges the compatibility complex only up to the unbudgeted one, so a
budget never creates a jointly feasible set the architecture excludes.
[CLAIM-568](../claims.d/CLAIM-568.md) pairs four obstructions to a transition with the
intervention that acts on each. What is open is the general case: an
intervention that changes several things at once (prestress that also
changes which configurations are stable, a reserve that also changes the
architecture), and whether a new capability can be defined without a
declared space against which it is new.

## What would answer it

A criterion, relative to a declared model, that classifies an
intervention as enlarging the set of feasible or reachable states, or as
lowering the cost, time or failure probability of reaching states already
reachable; and a test that applies it to systems whose configuration
space is not given in advance. A's proposed experiment is one route:
states A and B and a staging state C, measuring the bottleneck budget
B*(A,B) of [CLAIM-571](../claims.d/CLAIM-571.md), the least time T*(A,B;b) at budget b, and the
readiness R^π(A→B;b,z) in [TERM-115](../terms.d/TERM-115.md)'s sense, and producing cases
"where B is statically feasible but unreachable, reachable but too
expensive, reachable only through an architectural change, or reachable
only when temporary reserve capacity is available." [CASE-198](../cases.d/CASE-198.md) is one
of the third kind.

## What would not answer it

A single intervention shown to raise performance, which does not say
whether it widened what was possible or cheapened what already was; or a
classification that holds only because the declared space was drawn to
make it hold.

## Note of 2026-11-05: A's resource models and further distinctions

A's research programme in Part 3 compares architectures on seven dimensions: static compatibility, infinitesimal freedom, the global topology of the configuration space, dynamic reachability, robustness, the cost of reconfiguration, and maintenance under turnover. A's crucial experiment: "construct two organizational architectures with the same component resources and similar ordinary outputs but different feasible response geometries", then ask "Does the new organization merely lower costs? Does it change the attainable set? Does it add a branch of behavior? Does it create a new viable regime? And does that regime persist when the intervention ends?" The last is the persistence half of [CLAIM-566](../claims.d/CLAIM-566.md), and [CASE-210](../cases.d/CASE-210.md) is the readiness version of the paired architectures. No status changes.

## Note of 2026-11-05: the resource-bounded realizability readings

The pasted synthesis on resource-bounded realizability states this question's distinction as "a central theorem schema": "Increasing available resources while holding the architecture fixed may make previously inaccessible configurations affordable. Changing the architecture can alter the set of admissible configurations or processes itself." Among its open questions: "Could architectural transformations be classified by the kinds of computational obstructions they remove?" [CLAIM-556](../claims.d/CLAIM-556.md) gives one form of such a classification: six levels from compatibility to regeneration, each paired with what repairs it, so that an intervention can be typed by the level it acts on. The fixed-architecture half of the schema is shown for joint demands by [CLAIM-586](../claims.d/CLAIM-586.md) and for transitions by [CLAIM-571](../claims.d/CLAIM-571.md). The other half, what a change of architecture creates, is what stays open here. A offers it as a schema, not a theorem. No status changes.
