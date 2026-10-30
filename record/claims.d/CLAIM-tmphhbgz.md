---
status: Active
title: 'Over finitely many states and finite outcome sets, one experiment is ε-deficient relative to another in every decision problem with losses in [0, 1] exactly when a single Markov kernel brings it within ε in total variation at every state, so the deficiency computed as a linear programme is the least such ε'
version: 1
history:
- version: 1
  date: '2026-10-30'
  note: >-
    Filed Active at the twenty-first status review, at the status
    review's ruling (the owner delegated these rulings). CLAIM-488's note
    of 2026-10-30 asked for Le Cam's randomization criterion for finite
    experiments, read or re-derived. Han's lecture (LIT-tmp44f5w, read
    in NOTE-tmp30fln) states it and sketches the converse; van Rooyen's
    Theorem 26 (LIT-tmphckuv, NOTE-tmp9x3x4) proves it for one fixed
    prior. The uniform converse is re-derived step by step below, as
    ADR-047's ruling on re-derivations allows, and checked numerically
    with controls (p21/claim488_lecam_converse.py), re-run by the
    coordinator before the ruling.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in (i) or (ii): finite experiments and a kernel within ε of N
  at every state together with a [0, 1]-loss problem whose least uniform
  gap exceeds ε, or finite experiments where every [0, 1]-loss problem
  has a rule for M within ε at every state while no kernel brings M
  within ε of N at every state.
tags:
- mathematical-statistics
- probabilistic-modeling
date: '2026-10-30'
line:
- formal-apparatus
- pragmatic-transport
rests_on:
- CLAIM-381
grounds:
- LIT-tmp44f5w
summary: >-
  Le Cam's randomization criterion for finite experiments, uniform in the
  state, with losses in [0, 1]. The least ε for which some kernel brings M
  within ε of N in total variation at every state, which [CLAIM-381](CLAIM-381.md)
  computes as a linear programme, equals the least ε for which M is
  ε-deficient relative to N in every finite decision problem. One
  direction composes N's rule with the kernel; the other is one minimax
  step over a bilinear objective. At ε = 0 it is the finite Blackwell
  order ([THEORY-717](../theory.d/THEORY-717.md)).
---
<!-- inactive-ok-file: CLAIM-228 — Proposed; the empirical question this result leaves open, cited as open -->

# CLAIM-tmphhbgz: Over finitely many states and finite outcome sets, one experiment is ε-deficient relative to another in every decision problem with losses in [0, 1] exactly when a single Markov kernel brings it within ε in total variation at every state, so the deficiency computed as a linear programme is the least such ε

## The claim

**Setting.** Θ, X and Y are finite. The experiment M is (P_θ) with
P_θ ∈ Δ(X), and N is (Q_θ) with Q_θ ∈ Δ(Y). A kernel K sends X to Δ(Y),
and (KP_θ)(y) = Σ_x K(y | x) P_θ(x). TV(p, q) = ½ Σ |p − q| =
max over 0 ≤ h ≤ 1 of ⟨p − q, h⟩.

- δ := min_K max_θ TV(KP_θ, Q_θ). This is [CLAIM-381](CLAIM-381.md)'s linear programme,
  and the minimum is attained, the kernels forming a compact set.
- D := the supremum, over finite action sets A, losses
  L : Θ × A → [0, 1] and rules δ_N : Y → Δ(A) for N, of
  min over rules δ_M for M of max_θ [R_θ(δ_M) − R_θ(δ_N)], where
  R_θ(δ_M) = Σ_x P_θ(x) Σ_a δ_M(a | x) L(θ, a).

M is ε-deficient relative to N, in the decision sense of Han's slide 11
([LIT-tmp44f5w](../literature.d/LIT-tmp44f5w.md)), exactly when D ≤ ε. The claim is D = δ.

**(i) D ≤ δ.** Take K\* attaining δ, and for any A, L and δ_N put
δ_M = δ_N ∘ K\*, that is δ_M(a | x) = Σ_y δ_N(a | y) K\*(y | x). Then
R_θ(δ_M) − R_θ(δ_N) = ⟨K\*P_θ − Q_θ, h_θ⟩ with
h_θ(y) = Σ_a δ_N(a | y) L(θ, a) ∈ [0, 1], so the gap is at most
TV(K\*P_θ, Q_θ) ≤ δ, at every θ. This is Han's slide 14.

**(ii) δ ≤ D.** Fix the problem A = Y with δ_N the identity. A rule for M
is then a kernel K, and its gap at θ is ⟨KP_θ − Q_θ, L(θ, ·)⟩.

- Let G = {g on Θ × Y : 0 ≤ g(θ, y) ≤ π(θ) for some π ∈ Δ(Θ)}, a compact
  convex polytope, and f(K, g) = Σ_θ Σ_y g(θ, y)[(KP_θ)(y) − Q_θ(y)],
  bilinear in K and g.
- (a) Each g ∈ G is πL with L ∈ [0, 1]: put L = g/π where π(θ) > 0 and 0
  elsewhere. For every K, f(K, g) = Σ_θ π(θ) gap_θ(K) ≤ max_θ gap_θ(K).
  So min_K f(K, g) ≤ min_K max_θ gap_θ(K) ≤ D, and max_g min_K f ≤ D.
- (b) The stochastic matrices and G are non-empty compact convex sets in
  finite dimensions, and f is bilinear, so by von Neumann's minimax
  theorem min_K max_g f = max_g min_K f.
- (c) For fixed K and π, the best L(θ, y) is 1[(KP_θ − Q_θ)(y) > 0], so
  max_{g ∈ G} f(K, g) = max_π Σ_θ π(θ) TV(KP_θ, Q_θ) =
  max_θ TV(KP_θ, Q_θ).

Hence δ = min_K max_g f = max_g min_K f ≤ D, and with (i), D = δ. The
supremum defining D is attained, at A = Y, δ_N the identity and the loss
L\* = g\*/π\* from a maximising g\*. For losses in [0, c] the bound scales
to cε. At ε = 0 this is the finite Blackwell–Sherman–Stein theorem
([THEORY-717](../theory.d/THEORY-717.md)), a check on the statement.

The step Han's slide 15 leaves as "swap the inf and sup" is (b), with the
conditions it needs: finite outcome sets, so that Y is an admissible
action set and the rules form a compact convex set, and the bilinear form
in the product π(θ)L(θ, a). van Rooyen's Theorem 26 ([LIT-tmphckuv](../literature.d/LIT-tmphckuv.md),
[NOTE-tmp9x3x4](../notes.d/NOTE-tmp9x3x4.md)) proves the converse for one fixed prior; the uniform form
follows from it by exchanging the garbling with the prior, which is (b)
and (c) again.

**Checked numerically.** p21/claim488_lecam_converse.py (numpy only, with
its own simplex) solves [CLAIM-381](CLAIM-381.md)'s programme and, separately, the
programme for max_g min_K f. On 60 random experiments with |Θ|, |X| and
|Y| from 2 to 4 they agree to 1.1 × 10⁻¹³, and on the single problem
built from g\* no rule for M does better than δ uniformly. Its controls:
known answers (an uninformative experiment against the identity gives
0.5; an exact garbling gives 0), the returned kernel recomputed directly,
20,000 random kernels that never beat the programme, 600 random problems
in which no optimal gap exceeds δ, and two negative controls (dropping
the ½ is detected, and van Rooyen's bound fails for a signed loss as
[NOTE-tmp9x3x4](../notes.d/NOTE-tmp9x3x4.md) says). The uniform-prior average falls strictly below δ in
50 of the 60 cases, so the check tells the fixed-prior result apart from
the uniform one.

## What it does not say

- Nothing for infinitely many states or infinite outcome sets, where the
  minimax step needs compactness arguments not given here.
- Nothing for signed losses unless they are measured by their range: with
  ‖L‖∞ the bound can be off by a factor of 2 ([NOTE-tmp9x3x4](../notes.d/NOTE-tmp9x3x4.md)).
- No kernel form for the deficiency restricted to a family Q of problems.
  That is [CLAIM-381](CLAIM-381.md)'s finite computation, and it is bounded by this one.
- Not that the deficiency tells rendering procedures apart, which is
  [CLAIM-228](CLAIM-228.md)'s empirical question.

## Connections

[CLAIM-326](CLAIM-326.md) and [CLAIM-380](CLAIM-380.md) state the Bayes-risk comparison for a stated
prior, and each says it does not state "the prior-free form or its exact
relation to Le Cam's deficiency". This claim states that form for finite
sets: the deficiency is the least ε by which every [0, 1]-loss problem
can be matched at every state. [CLAIM-488](CLAIM-488.md) rests on it.
