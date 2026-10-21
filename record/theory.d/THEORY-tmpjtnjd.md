---
status: Active
title: 'For deterministic causal models with a countable set of allowed interventions, a high-level model reproduces the coarse-grained interventional law of a low-level one for every distribution on contexts exactly when some map τ_U on contexts commutes with every allowed intervention, τ(M_L(u, i)) = M_H(τ_U(u), ω(i)); exactness for one distribution is strictly weaker, since a well-chosen distribution lets unrelated models match, and τ-abstraction and strong abstraction are strictly stronger; the context map is only required to exist, so high-level exogenous variables may carry what the coarse state drops'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-tmp1bdcu. The equivalence is Beckers and
    Halpern's Theorem 3.8 with Proposition 3.6, whose countability
    hypothesis the theorem's statement omits; the strictness of the steps
    is their Examples 3.4, 3.10, 3.11 and 3.16–3.18. The equivalence is
    re-derived below step by step, which meets the condition for Active
    under ADR-047 v2. The last clause is the record's reading, with the
    hidden bit as its example.
tags:
- causality
date: '2026-10-21'
source:
- LIT-tmp6hpx6
- LIT-tmptzsyg
summary: >-
  Beckers and Halpern (2019), [LIT-tmp6hpx6](../literature.d/LIT-tmp6hpx6.md), read in [NOTE-tmp1bdcu](../notes.d/NOTE-tmp1bdcu.md), on
  Rubenstein et al.'s exact transformation ([LIT-tmptzsyg](../literature.d/LIT-tmptzsyg.md)). Uniformity over
  distributions turns a distributional match into a context-by-context
  commuting condition. It does not make the coarse endogenous state carry
  the high-level context, which is what governance-response sufficiency
  would need.
---
<!-- inactive-ok-file: TERM-tmpf5k7x — Proposed; the governance-response profile, filed from the same exchange, named for the contrast, nothing here rests on it -->

# THEORY-tmpjtnjd: For deterministic causal models with a countable set of allowed interventions, a high-level model reproduces the coarse-grained interventional law of a low-level one for every distribution on contexts exactly when some map τ_U on contexts commutes with every allowed intervention, τ(M_L(u, i)) = M_H(τ_U(u), ω(i)); exactness for one distribution is strictly weaker, since a well-chosen distribution lets unrelated models match, and τ-abstraction and strong abstraction are strictly stronger; the context map is only required to exist, so high-level exogenous variables may carry what the coarse state drops

## Source

Beckers and Halpern (2019), [LIT-tmp6hpx6](../literature.d/LIT-tmp6hpx6.md), read in full in [NOTE-tmp1bdcu](../notes.d/NOTE-tmp1bdcu.md):
Definitions 3.1, 3.5, 3.13 and 3.15, Proposition 3.6, Theorem 3.8 and the
examples named below. Exact transformation is Rubenstein et al.'s
([LIT-tmptzsyg](../literature.d/LIT-tmptzsyg.md), [NOTE-tmp6b7dr](../notes.d/NOTE-tmp6b7dr.md)).

## What was actually shown

Fix deterministic models M_L, M_H, a map τ from low- to high-level
endogenous states, and a surjective, order-preserving ω from allowed
low-level interventions I_L to high-level ones. (M_H, Pr_H) is an exact
transformation of (M_L, Pr_L) when Pr_H^{ω(i)} = τ(Pr_L^i) for every i ∈ I_L.
M_H is a uniform transformation of M_L when for every Pr_L some Pr_H makes
the pair exact.

**(b) ⇒ (a).** Suppose τ_U satisfies τ(M_L(u, i)) = M_H(τ_U(u), ω(i)) for all
contexts u and all i ∈ I_L. Given Pr_L, put Pr_H = τ_U(Pr_L). For a
high-level state v_H,
Pr_H^{ω(i)}(v_H) = Pr_H{u_H : M_H(u_H, ω(i)) = v_H}
= Pr_L{u : M_H(τ_U(u), ω(i)) = v_H} = Pr_L{u : τ(M_L(u, i)) = v_H}
= τ(Pr_L^i)(v_H).

**(a) ⇒ (b), with I_L countable.** Fix a context u and let Pr_L be the point
mass at u. Then τ(Pr_L^i) is the point mass at τ(M_L(u, i)), so the Pr_H that
uniformity supplies gives probability one to
A_i = {u_H : M_H(u_H, ω(i)) = τ(M_L(u, i))} for each i. A countable
intersection of probability-one sets has probability one, so ⋂ᵢ A_i is
nonempty; let τ_U(u) be any of its points. Then τ_U commutes with every
allowed intervention at u, and u was arbitrary. The paper's Theorem 3.8 is
stated without the countability that this step, its Proposition 3.6, uses.

**Strictness of the steps.**

- *Exact but not uniform* (Example 3.4). Two unrelated models, each with
  only the empty intervention and a point-mass distribution, with τ sending
  every state of each to the other's one realized state, are exact
  transformations of each other. With another distribution they are not.
- *Uniform but not a τ-abstraction* (Examples 3.10–3.11). Choosing ω freely
  lets M₁ and M₂ be uniform transformations of each other; and a high-level
  variable X* that changes every equation only when U* = 0, a context never
  given positive probability, is uniform with τ not surjective.
  τ-abstraction requires τ surjective, a surjective τ_U, and ω = ω_τ, the map
  τ itself induces.
- *A τ-abstraction but not strong* (Example 3.16). With energy computed from
  velocity, height and mass, M ← m leaves every energy pair reachable, so
  ω_τ sends it to the empty intervention while it changes the outcome; strong
  abstraction, which allows every intervention ω_τ is defined on, fails, and
  removing M ← m from I_L gives a τ-abstraction.

What could have failed: uniformity could have required more than a single
context map, for example one map per intervention. Countability lets one
point serve every intervention at once.

## What this does not say

- **Not that the high-level context is the coarse state.** τ_U is any map
  that works. In the hidden bit ([CASE-tmpdc0tl](../cases.d/CASE-tmpdc0tl.md)), dropping K is a
  τ-abstraction for interventions on H alone, with
  τ_U(u) = (u_t, u_H, (u_K, u_{t+1})): the high-level noise carries K. So the
  ladder up to τ-abstraction accepts a coarse-graining whose coarse state
  keeps nothing of the response to h. Governance-response sufficiency
  ([TERM-tmpf5k7x](../terms.d/TERM-tmpf5k7x.md)) is the compatibility condition with τ_U required to be the
  coarse state itself, compared on the outcome only ([NOTE-tmp1bdcu](../notes.d/NOTE-tmp1bdcu.md), Bearing
  on the record, item 1).
- **Not anything approximate;** that is [LIT-tmp0p7xl](../literature.d/LIT-tmp0p7xl.md) ([THEORY-tmpe391l](THEORY-tmpe391l.md)).
- **Not for uncountable intervention sets** without a further argument.
- **Not that every strong abstraction is constructive;** the paper
  conjectures it.

## Connections

- **[THEORY-tmpjfhcb](THEORY-tmpjfhcb.md).** Exact transformation's acceptance of marginalising a
  never-intervened variable, here seen to survive uniformity.
- **[CLAIM-350](../claims.d/CLAIM-350.md).** Its fibre-wise factorization of a judgment is the shape of
  the compatibility condition with the context map fixed to the coarse
  map.
- **[THEORY-243](THEORY-243.md).** Interchange interventions test a commuting condition of
  this kind on chosen inputs.
