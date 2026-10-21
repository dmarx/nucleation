---
status: Active
title: 'effective-description regime: the system, query family, intervention family, resource bounds, tolerance and horizon under which a candidate description''s adequacy is assessed, ℛ = (X, 𝒬, ℐ, ℬ, ε, τ), kept apart from the description T it evaluates, so that rival descriptions are compared under one regime and whether each is adequate, Adequate(T; ℛ), is settled once the regime is stated'
version: 3
history:
- version: 2
  date: '2026-10-21'
  note: >-
    From the readings of 2026-10-21 of the causal-abstraction papers: the
    relativity to ℐ is proved there for exact transformation, and how the
    interventions are fixed is a further choice the regime must state. The
    definition is unchanged.
- version: 3
  date: '2026-10-21'
  note: >-
    Revised at the owner's second review of 2026-10-21: the regime no longer
    includes the description T, ℛ = (X, 𝒬, ℐ, ℬ, ε, τ), with Adequate(T; ℛ)
    and (T, ℛ) an evaluation instance. Adopted: status Proposed → Active.
tags:
- complex-systems
- information-theory
- philosophy-of-science
date: '2026-10-21'
line: formal-apparatus
summary: >-
  The exchange of 2026-10-20 returned to this signature five times. A3
  proposed the six-tuple 𝔈 = (X, T, 𝒬, ℐ, ℬ, τ) so that an ablation could
  not "succeed simply by moving the goalposts". A5 added the tolerance ε
  in the predicate Adequate(T; 𝒬, ℐ, ℬ, ε, τ): "Adequacy is relational, but
  whether the relation holds can be objective." A11 named it, and A12, A13
  and A14 kept the seven-tuple; A13: "our own organizing convention rather
  than an established term of art". The owner's second review took T out
  of the tuple, ℛ = (X, 𝒬, ℐ, ℬ, ε, τ), so that descriptions are compared
  under one regime. Adopted by the owner on 2026-10-21. It
  would add a name for what [CLAIM-152](../claims.d/CLAIM-152.md), [CLAIM-302](../claims.d/CLAIM-302.md), [CLAIM-387](../claims.d/CLAIM-387.md) and [THEORY-424](../theory.d/THEORY-424.md)
  each relativize to; it replaces nothing.
used_by:
- CLAIM-tmpcrdhj
---
<!-- inactive-ok-file: CLAIM-tmpcrdhj QUESTION-tmp1nqby — Proposed; the claim and question filed from the same exchange, cited as where the regime is used -->
<!-- inactive-ok-file: CLAIM-363 CLAIM-348 — Proposed; the owner's point about relata and the target-relativity of adequacy, cited as the shape this term borrows, nothing rests on them -->

# TERM-tmpdxajb: effective-description regime: the system, query family, intervention family, resource bounds, tolerance and horizon under which a candidate description's adequacy is assessed, ℛ = (X, 𝒬, ℐ, ℬ, ε, τ), kept apart from the description T it evaluates, so that rival descriptions are compared under one regime and whether each is adequate, Adequate(T; ℛ), is settled once the regime is stated

## Definition

An **effective-description regime** is ℛ = (X, 𝒬, ℐ, ℬ, ε, τ):

- X, the underlying system;
- 𝒬, the prediction or decision queries T is to answer;
- ℐ, the interventions under which it must answer them;
- ℬ, the resources, the budget and class of operations, available to
  whoever uses T;
- ε, the tolerated error;
- τ, the horizon.

The description under evaluation, T, a map from X's states or histories,
is not part of the regime. A description is adequate relative to a regime,
Adequate(T; ℛ), A5's Adequate(T; 𝒬, ℐ, ℬ, ε, τ). The pair (T, ℛ) is an
**evaluation instance**. Keeping T out is what lets two descriptions be
compared under one regime: if T were a component, changing the
description would change the regime by definition, and every comparison
would move the goalposts A3 warned against. The regime can be extended
with what a given inquiry needs, a probability law on X, a causal model or
a measurement specification. Its point is A5's: "**Adequacy is relational,
but whether the relation holds can be objective.**" Once the regime is
stated, a verdict of adequacy can be false.

**Its history in the exchange of 2026-10-20.** A3 §5 proposed six
components, 𝔈 = (X, T, 𝒬, ℐ, ℬ, τ), "where \(X\) is the underlying system,
\(T\) the representation, \(\mathcal Q\) the prediction or decision
queries, \(\mathcal I\) the intervention class, \(\mathcal B\) the
computational budget, and \(\tau\) the relevant time horizon", because
"Without a fixed target, we could make an ablation succeed simply by moving
the goalposts." A5 §1 added ε, as "an allowed error", in the predicate. A11
gave it its name in a table of proposed TERMs ("A representation evaluated
relative to specified queries, interventions, resources, error tolerance
and time horizon"). A12 wrote the seven-tuple. Those tuples included T; the owner's second
review of 2026-10-21 took it out, since "much of our analysis concerns
comparing two different representations under the same evaluation
conditions". A13: "We've returned to this
repeatedly", and "I'd file this as proposed initially, since it's our own
organizing convention rather than an established term of art." A14: "this
is a convenient specification, not a claim that every inquiry must have
exactly seven components", and its merge condition: "Future work must be
able to cite the effective-description regime without simultaneously
asserting that its particular target, intervention family, or
computational budget is privileged."

**Where the record already locates each relativity.** The target:
[CLAIM-152](../claims.d/CLAIM-152.md) (sufficiency is relative to its target) and [CLAIM-348](../claims.d/CLAIM-348.md). The
resources: [CLAIM-302](../claims.d/CLAIM-302.md) and [CLAIM-304](../claims.d/CLAIM-304.md) (feasible tests, feasible recovery).
The interventions: [THEORY-424](../theory.d/THEORY-424.md) (Â depends on an intervention distribution)
and [CLAIM-350](../claims.d/CLAIM-350.md)'s causal version; for exact transformation it is proved in
Rubenstein et al., where enlarging the declared interventions breaks
exactness ([THEORY-tmpj5zq1](../theory.d/THEORY-tmpj5zq1.md)), and Beckers and Halpern's ladder shows that how
the interventions are fixed (chosen freely, fixed by the state map, or all
that map can translate) is a further choice the regime must state
([NOTE-tmp1bdcu](../notes.d/NOTE-tmp1bdcu.md)). The budget of a compression: [CLAIM-387](../claims.d/CLAIM-387.md).
The decision family: [TERM-028](TERM-028.md) and [THEORY-717](../theory.d/THEORY-717.md) (Blackwell's order).
[CLAIM-tmpcrdhj](../claims.d/CLAIM-tmpcrdhj.md) says which of the conditions on an effective description
are parameters of the regime, and [QUESTION-tmp1nqby](../questions.d/QUESTION-tmp1nqby.md) fixes the regime
before it ablates.

**What would settle it.** Whether the conditions of [QUESTION-tmp1nqby](../questions.d/QUESTION-tmp1nqby.md) can
each be stated as adequacy relative to one regime, and whether claims that
now state their relativities one at a time are clearer stated in it.

## What it is not

- **Not a claim that adequacy is only relative.** The owner's point about
  normative relata in [CLAIM-363](../claims.d/CLAIM-363.md) ("once they are fixed, the judgment can be
  false") carries over, and is stated here in prose, not as a relation.
- **Not a fixed list.** A14's own caveat: seven is a convenient
  specification. A regime may need a projection (for memory, [QUESTION-222](../questions.d/QUESTION-222.md))
  or a background distribution ([THEORY-424](../theory.d/THEORY-424.md), where Â depends on the law of
  the environment variable).
- **Not a fidelity sense.** [TERM-034](TERM-034.md) relativizes fidelity to an interpreter
  and a communication constraint in the same spirit, and [TERM-043](TERM-043.md) compares
  a transport's distortions component by component. This is about one
  system's coarse description, not a rendering between two.
- **Not a privilege for its components.** Naming a target or a budget in a
  regime does not say it is the right one (A14's merge condition).
