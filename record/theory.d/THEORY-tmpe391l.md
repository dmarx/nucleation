---
status: Active
title: 'Beckers, Eberhardt and Halpern''s approximate abstraction error, the least over surjective context maps of the worst case over allowed interventions and contexts of the high-level distance between the coarse-grained low-level outcome and the high-level outcome, is zero exactly for τ-abstraction; an abstraction followed by an α-approximation of the high-level model is within α, an α-approximation of the low-level model followed by an abstraction only within kα, k the worst-case ratio of high- to low-level distances, and an approximate abstraction need not factor into an exact abstraction and an approximation'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-tmpqfl95. The definition is the paper's
    Definition 3.2; the results are its Propositions 3.3, 5.1 and 5.2 and
    Example 5.3, re-derived below step by step, which meets the condition
    for Active under ADR-047 v2.
tags:
- causality
date: '2026-10-21'
source:
- LIT-tmp0p7xl
- LIT-tmp6hpx6
summary: >-
  Beckers, Eberhardt and Halpern (2020; arXiv 2019), [LIT-tmp0p7xl](../literature.d/LIT-tmp0p7xl.md), read in
  [NOTE-tmpqfl95](../notes.d/NOTE-tmpqfl95.md), on Beckers and Halpern's τ-abstraction ([LIT-tmp6hpx6](../literature.d/LIT-tmp6hpx6.md)).
  The error is relative to a metric the user chooses, takes the worst case
  over interventions, and minimizes over context maps, so like exact
  abstraction it is zero for a coarse-graining whose dropped detail the
  high-level noise can hold. It does not measure the governance deficiency
  Γ.
supports:
- CLAIM-tmp4r4mi
---

# THEORY-tmpe391l: Beckers, Eberhardt and Halpern's approximate abstraction error, the least over surjective context maps of the worst case over allowed interventions and contexts of the high-level distance between the coarse-grained low-level outcome and the high-level outcome, is zero exactly for τ-abstraction; an abstraction followed by an α-approximation of the high-level model is within α, an α-approximation of the low-level model followed by an abstraction only within kα, k the worst-case ratio of high- to low-level distances, and an approximate abstraction need not factor into an exact abstraction and an approximation

## Source

Beckers, Eberhardt and Halpern (2020; arXiv:1906.11583, 2019),
[LIT-tmp0p7xl](../literature.d/LIT-tmp0p7xl.md), read in full in [NOTE-tmpqfl95](../notes.d/NOTE-tmpqfl95.md): Definitions 2.4–2.5, 3.1–3.2,
Propositions 3.3, 5.1 and 5.2, Example 5.3. τ-abstraction is Beckers and
Halpern's ([LIT-tmp6hpx6](../literature.d/LIT-tmp6hpx6.md), [NOTE-tmp1bdcu](../notes.d/NOTE-tmp1bdcu.md)).

## What was actually shown

Let (M_L, I_L) and (M_H, I_H) be finite deterministic causal models,
τ-consistent: τ surjective, I_H = ω_τ(I_L), |R_L(U_L)| ≥ |R_H(U_H)|. With a
metric d_H on high-level states,

d_τ(M_L, M_H) = min over surjective τ_U of max over i ∈ I_L and u ∈ R_L(U_L)
of d_H(τ(M_L(u, i)), M_H(τ_U(u), ω_τ(i))).

**Zero is exact abstraction (Proposition 3.3).** The minimum is over a
finite set, so d_τ = 0 iff some surjective τ_U makes every term zero, iff
τ(M_L(u, i)) = M_H(τ_U(u), ω_τ(i)) for all u and i, which with τ-consistency
is Definition 2.5's τ-abstraction.

**Abstraction, then approximation (Proposition 5.1).** Let M_H be a
τ-abstraction of M_L via τ_U, and M_H′ be similar to M_H with
max_{i,u_H} d_H(M_H′(u_H, i), M_H(u_H, i)) ≤ α. Using the same τ_U, each
term d_H(τ(M_L(u, i)), M_H′(τ_U(u), ω_τ(i))) equals
d_H(M_H(τ_U(u), ω_τ(i)), M_H′(τ_U(u), ω_τ(i))) ≤ α. The minimum is no larger.

**Approximation, then abstraction (Proposition 5.2).** If instead M_L is a
d_max-α approximation of M_L′ and M_H a τ-abstraction of M_L, then
d_H(τ(M_L′(u, i)), M_H(τ_U(u), ω_τ(i))) = d_H(τ(M_L′(u, i)), τ(M_L(u, i)))
≤ k · d_L(M_L′(u, i), M_L(u, i)) ≤ kα, with k the maximum of the ratio of the
two distances. The bound is what τ does to distances, which can be anything:
"d_VL(v_L, v_L′) and d_VH(τ(v_L), τ(v_L′)) may be unrelated."

**No factoring (Example 5.3), checked.** M_L has A = B = C = U with U ≡ 0,
and allowed interventions ∅, A ← 0, A ← 1, B ← 0, B ← 1; τ(a, b, c) =
(a ⊕ b, b ⊕ c). Each single-variable intervention leaves every high-level
pair reachable, so ω_τ sends all of them to the empty intervention, and
I_H = {∅}; M_H has D = E = U ≡ 0. Under B ← 1 the low state is (0, 1, 0),
lifted to (1, 1), at Euclidean distance √2 from (0, 0); under A ← 1 it is
(1, 0, 0), lifted to (1, 0), at distance 1. So d_τ = √2. For M_H to be an
exact abstraction of a model M_L′ with the same signature, every allowed
intervention must yield a state lifted to (0, 0), so a = b = c. Then B ← 0
and B ← 1 must give A = 0 and A = 1, so A depends on B; and A ← 0 and A ← 1
must give B = 0 and B = 1, so B depends on A. No recursive M_L′ does both.
(The paper ends "Thus, M_H cannot be recursive"; the argument is about
M_L′.)

What could have failed: errors could have failed to compose at all once
the two levels have unrelated metrics; they compose in one order with no
loss and in the other only through k.

## What this does not say

- **Not a measure of whether the coarse state keeps a system's response.**
  The minimum over τ_U lets high-level noise hold what τ drops, so for
  [CASE-tmpdc0tl](../cases.d/CASE-tmpdc0tl.md) with interventions on H only, d_τ = 0 while the
  governance deficiency is ρ(h = 1) bits ([NOTE-tmpqfl95](../notes.d/NOTE-tmpqfl95.md)). The deficiency of
  [TERM-tmpf5k7x](../terms.d/TERM-tmpf5k7x.md) would need τ_U fixed to the coarse state, an average over
  interventions rather than a maximum, and an information measure rather
  than a metric.
- **Not a scale independent of the metric.** "the choice of distance
  function makes a crucial difference."
- **Not the probabilistic variants,** which replace the maximum over
  contexts by an expectation (Definition 4.4) and add an intervention
  distribution over implementations (Definition 4.8); they are recorded in
  [NOTE-tmpqfl95](../notes.d/NOTE-tmpqfl95.md) and not re-derived here.
- **Not a bound when k is undefined,** as it is wherever M_L′ and M_L agree.

## Connections

- **[THEORY-tmpjtnjd](THEORY-tmpjtnjd.md).** Its zero set.
- **[TERM-043](../terms.d/TERM-043.md).** D_causal is a different graded relation: an average over
  interventions of a distance between push-forward distributions.
