---
number: 1096
status: Active
formerly:
- THEORY-tmp5sao6
title: 'Blackwell''s comparison of experiments, its easy direction: an experiment is a family of distributions indexed by a common parameter, and if one experiment is a garbling of another by a Markov kernel, every risk attainable with the garbling in any decision problem with bounded losses is attainable with the original, on any outcome spaces'
version: 1
tags:
- mathematical-statistics
- information-theory
- mathematics
date: '2026-10-27'
source:
- LIT-781
extends:
- THEORY-156
summary: >-
  Split from [THEORY-156](THEORY-156.md) by the status review of 2026-10-27 ([ADR-057](../decisions.d/ADR-057.md)).
  [THEORY-156](THEORY-156.md)'s equivalence needs a second proof of the general converse and
  stays Proposed. Ten of its twelve dependents used only its definitions
  (an experiment, a garbling, the informativeness order), or only the easy
  direction, that a garbling never helps a decision-maker free to choose any
  rule. The easy direction holds on any outcome spaces, and its proof is two
  lines, re-derived below under [ADR-047](../decisions.d/ADR-047.md) v2's ruling, which [ADR-057](../decisions.d/ADR-057.md) keeps. It is
  Theorem 3 of Blackwell (1953), [LIT-781](../literature.d/LIT-781.md), read in [NOTE-595](../notes.d/NOTE-595.md), and Blackwell's
  1951 result. The finite converse is [THEORY-717](THEORY-717.md), Active.
---
<!-- inactive-ok-file: THEORY-156 ADR-047 — Proposed and Superseded; the account this is split from, and the decision whose re-derivation ruling ADR-057 keeps -->

# THEORY-1096: Blackwell's comparison of experiments, its easy direction: an experiment is a family of distributions indexed by a common parameter, and if one experiment is a garbling of another by a Markov kernel, every risk attainable with the garbling in any decision problem with bounded losses is attainable with the original, on any outcome spaces

## Source

Blackwell (1953), [LIT-781](../literature.d/LIT-781.md), read in [NOTE-595](../notes.d/NOTE-595.md): the definitions in §1 and
Theorem 3, "α ≻ β implies α ⊃ β". The paper quotes the result from
Blackwell (1951), unread here. The re-derivation below does not depend on
either proof.

## Definitions

- **Experiment.** For a parameter set Θ, an experiment α is a family
  (α_θ)_{θ∈Θ} of probability measures on one measurable outcome space X.
  [THEORY-156](THEORY-156.md) quotes it: "an n-tuple of probability measures on a common
  space, one per state". Two experiments compared must share Θ, and they
  need not share an outcome space.
- **Garbling.** β on Y is a garbling of α on X when there is a Markov
  kernel K from X to Y with β_θ(B) = ∫ K(B | x) α_θ(dx) for every θ and
  every measurable B. Blackwell's "α is sufficient for β", written α ≻ β.
- **Decision problem and risk.** An action space A, a loss L(θ, a)
  bounded and measurable in a, and a decision rule for β, which is a Markov
  kernel δ from Y to A. The rule's risk at θ is
  R_β(δ, θ) = ∫∫ L(θ, a) δ(da | y) β_θ(dy). The risk vector is
  (R_β(δ, θ))_{θ∈Θ}.
- **Informativeness order.** α ⊃ β when, in every decision problem, every
  risk vector attainable with β is attainable with α. [THEORY-156](THEORY-156.md) quotes
  the finite-Θ form: "for every closed bounded convex set A of loss
  vectors, every risk vector attainable with β is attainable with α".

## The claim, and its proof

**If β is a garbling of α, then α ⊃ β.**

Take any decision problem and any rule δ for β. Define a rule for α by
first garbling and then applying δ: δ'(C | x) = ∫ δ(C | y) K(dy | x).
This is a Markov kernel from X to A, being a composition of two kernels. Its
risk at θ is

R_α(δ', θ) = ∫ [∫∫ L(θ, a) δ(da | y) K(dy | x)] α_θ(dx)
           = ∫∫ L(θ, a) δ(da | y) [∫ K(dy | x) α_θ(dx)]
           = ∫∫ L(θ, a) δ(da | y) β_θ(dy) = R_β(δ, θ).

The exchange of integrals is Fubini's theorem. It applies because L is
bounded and measurable, and every kernel is a probability measure in its
first argument. The second line is the definition of the garbling. So δ'
attains with α exactly the risk vector δ attains with β, at every θ. Since
δ and the problem were arbitrary, α ⊃ β. ∎

Nothing in the proof uses finiteness of Θ, X, Y or A. It uses only that
rules may be randomized, so that a composition of kernels is a rule, and
that losses are bounded, so the integrals exist.

## What it does not say

- **The converse.** That α ⊃ β implies a garbling exists is [THEORY-717](THEORY-717.md)
  for finitely many states and outcomes (Active), and [THEORY-156](THEORY-156.md) in
  general (Proposed).
- **Anything about a restricted receiver.** The decision-maker may use any
  rule. A receiver limited to a class of rules can do better with a
  garbling than with the original ([CLAIM-199](../claims.d/CLAIM-199.md), [CLAIM-225](../claims.d/CLAIM-225.md)).
- **How much worse an incomparable experiment is.** The order is
  qualitative. That is Le Cam's deficiency, unread here ([LIT-778](../literature.d/LIT-778.md)).
