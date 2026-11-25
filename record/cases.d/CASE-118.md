---
number: 118
status: Active
formerly:
- CASE-tmptwfjg
title: 'Two competing components with overlap ρ'
statement: >-
  Two competing components with interaction matrix A = [[1, ρ], [ρ, 1]]:
  with equal growth rates their invasion growth is 1 − ρ, the smallest
  eigenvalue of the Gram matrix, and with growth rates 1 ± δ the same matrix
  supports coexistence only when |δ| < (1 − ρ)/(1 + ρ), so feature geometry
  alone does not fix coexistence
version: 5
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added: in Chesson's terms, by Letten et al.'s
    translation (NOTE-1377), ρ is the niche overlap, 1 − ρ the niche
    difference, and the coexistence bound is ρ < f₂/f₁ < 1/ρ;
    Chesson 1990 registered, Unfetched. The construction is
    unchanged.
- version: 3
  date: '2026-11-12'
  note: >-
    Draws on THEORY-004 ("measured from feature geometry (ρ, the Gram
    spectrum; THEORY-004, CLAIM-193)"). First application of draws_on
    (ADR-095). No other change.
- version: 4
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: LEAD-049's Theorem B (CLAIM-885)
    gives the case's invasion growth 1 - ρ as the two-component instance
    of n*_i d_i². The construction is unchanged.
- version: 5
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: Chesson (2011), the stand-in for Chesson
    1990, read (NOTE-2380). His overlap for MacArthur's model is the
    cosine of the niche vectors (CLAIM-1181); two readings of how
    far that settles the note of 2026-10-29 are filed. Draws on
    THEORY-2287. The construction is unchanged.
standing: fictional
kind: construction
tags:
- ecology
- mathematics
- learning-theory
date: '2026-10-18'
line: distributed-agency
summary: >-
  From the synthesis the owner relayed on 2026-10-18, checked. The
  two-component Lotka–Volterra system with symmetric overlap ρ: invasion
  growth 1 − ρ equals λ_min(A), and κ(A) = (1 + ρ)/(1 − ρ), so overlap
  weakens recovery and ill-conditions the features together. Holding A
  fixed and setting r = (1 + δ, 1 − δ) gives the coexistence equilibrium
  n* = (1/(1 + ρ) ± δ/(1 − ρ)), feasible only when |δ| < (1 − ρ)/(1 + ρ).
  The same representation geometry supports coexistence under one supply
  and exclusion under another.
draws_on:
- THEORY-004
- THEORY-2287
---
<!-- inactive-ok-file: ARG-236 — Proposed, filed by the lead run of 2026-11-22 and cited in the note of that date -->
<!-- inactive-ok-file: CLAIM-885 — Proposed, filed 2026-11-22 by LEAD-049 and cited in the note of that date -->
<!-- inactive-ok-file: CLAIM-193 — Proposed or Deferred; open claims, readings and works cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-1826 — Unfetched since 2026-10-29; Chesson 1990, cited in the note of that date as not read, nothing here rests on it -->

# CASE-118: Two competing components with overlap ρ

## The construction

Two components with abundances n₁, n₂ ≥ 0 and

  ṅ_i = n_i (r_i − (An)_i),  A = [[1, ρ], [ρ, 1]],  0 ≤ ρ < 1.

A is the Gram matrix of two unit feature vectors at inner product ρ.

**Equal growth rates, r₁ = r₂ = 1.** Component 1 alone settles at
n₁ = 1. A rare component 2 then grows at r₂ − ρn₁ = 1 − ρ, and by symmetry
the same holds the other way. The eigenvalues of A are 1 ± ρ, so
λ_min(A) = 1 − ρ, and κ(A) = (1 + ρ)/(1 − ρ). As overlap ρ → 1, the
invasion advantage vanishes and the feature system becomes
ill-conditioned together.

**Unequal growth rates, r = (1 + δ, 1 − δ), same A.** Solving An = r:

  n₁* = 1/(1 + ρ) + δ/(1 − ρ),  n₂* = 1/(1 + ρ) − δ/(1 − ρ).

The equilibrium is feasible, both positive, only when
|δ| < (1 − ρ)/(1 + ρ). Outside that range one component excludes the
other with the Gram matrix unchanged. Checked at ρ = 0.5, δ = 0.1:
n* = (0.867, 0.467), bound 0.333; eigenvalues 0.5 and 1.5; κ = 3.

## What it shows

The kernel is not enough to determine coexistence. One must also know
what resources, tasks or evaluative opportunities the system supplies.
That is [CLAIM-152](../claims.d/CLAIM-152.md)'s target-relativity applied to persistence: what a
representation supports depends on what it is asked for.

It separates three things an experiment on [QUESTION-083](../questions.d/QUESTION-083.md) could conflate:

- **structural differentiation**, measured from feature geometry (ρ, the
  Gram spectrum; [THEORY-004](../theory.d/THEORY-004.md), [CLAIM-193](../claims.d/CLAIM-193.md));
- **functional differentiation**, measured by conditional performance
  across contexts;
- **dynamical stabilization**, measured by recovery when rare and by
  persistence.

A feature can be geometrically distinct without being useful. A specialist
can be useful without enough influence to survive. And differentiated
specialists can persist without any higher-level governance.

## Note of 2026-10-29: ρ in Chesson's terms

Chesson's 1990 paper on MacArthur's consumer–resource model, [LIT-1826](../literature.d/LIT-1826.md),
is registered and Unfetched, so this case's ρ cannot yet be checked
against his definition at its source. What the record can say comes from
Letten, Ke and Fukami, [LIT-1237](../literature.d/LIT-1237.md) ([NOTE-1377](../notes.d/NOTE-1377.md)), who follow that paper. In
Lotka–Volterra form, Chesson's niche overlap is √(α₁₂α₂₁/α₁₁α₂₂) and his
fitness ratio is f₂/f₁ = √(α₁₁α₁₂/α₂₂α₂₁), with mutual invasibility ρ <
f₂/f₁ < 1/ρ.

Writing this case's system as ṅ_i = r_i n_i(1 − Σ_j (A_ij/r_i) n_j) gives
α_ij = A_ij/r_i. Then the niche overlap is ρ itself, and the fitness ratio
is r₂/r₁ = (1 − δ)/(1 + δ). So the case's word "overlap" for ρ is
Chesson's, and the invasion growth 1 − ρ is his niche difference, not his
overlap. The coexistence bound |δ| < (1 − ρ)/(1 + ρ) is his ρ < f₂/f₁ <
1/ρ, rewritten (checked by hand, 2026-10-29). Whether Chesson's overlap
for MacArthur's model is the cosine of the components' feature vectors, as
the case assumes, is what a reading of [LIT-1826](../literature.d/LIT-1826.md) would settle. The
construction is unchanged.

## Note of 2026-11-22: the k-component version

[CLAIM-885](../claims.d/CLAIM-885.md) (Theorem B, [LEAD-049](../leads.d/LEAD-049.md)) proves, for any number of
components with a positive definite Gram matrix and an interior
equilibrium, that a component's invasion growth at the −i community is
at least n*_i d_i². Here d_i is the distance of its feature vector from
the span of the others'. Equality holds when no other component goes
extinct in its absence. In this case n*_i = 1/(1 + ρ) and d_i² = 1 − ρ²,
so the bound is 1 − ρ, the value above. So the 1 − ρ = λ_min(A)
coincidence is special to two components with equal growth rates. In
general what matters is d_i², which is at least λ_min(A), weighted by
the abundance n*_i. The construction is unchanged.

## Note of 2026-11-22: Chesson, read through his own restatement

The note of 2026-10-29 left one question: whether Chesson's overlap for
MacArthur's model is the cosine of the components' feature vectors, as
this case assumes. [LIT-1826](../literature.d/LIT-1826.md) is still Unfetched (its status note gives
the obstacles of this date). Chesson's 2011 chapter, [LIT-3154](../literature.d/LIT-3154.md), read
in full ([NOTE-2380](../notes.d/NOTE-2380.md)), restates that paper's reworking of MacArthur
and gives the measure in its Table 1 ([THEORY-2287](../theory.d/THEORY-2287.md)):

  ρ = Σ_l c_jl v_l K_l c_kl / r_l, divided by s_j s_k,
  s_j = √(Σ_l c_jl² v_l K_l / r_l).

With u_jl = c_jl √(v_l K_l / r_l) that is the cosine of u_j and u_k, and
s_j = ‖u_j‖. The fast-resource reduction of the model is [CLAIM-369](../claims.d/CLAIM-369.md)'s
class with these u_j as niche vectors ([CLAIM-1181](../claims.d/CLAIM-1181.md), checked by a
record script). This case's unit feature vectors are s_j = 1, so its ρ is
Chesson's overlap, its r_i is his average fitness κ_i, and its bound
|δ| < (1 − ρ)/(1 + ρ) is his ρ < κ₁/κ₂ < 1/ρ, as the note of 2026-10-29
found by Letten, Ke and Fukami's route.

Two readings of how far this settles that note's question. They would be
filed differently, and the owner chooses.

- **Reading A (the assistant's lean): settled.** The chapter is Chesson's
  own and cites the 1990 paper (its [28]) for exactly the reworking it
  tabulates, and the identity is checked against the model, not taken on
  trust. The case's word "overlap" is Chesson's for MacArthur's model.
  What is left to the 1990 paper is its derivations.
- **Reading B: settled for the 2011 measure only.** The note of
  2026-10-29 asked for the check "at its source". By its abstract the
  1990 paper develops statistical measures of association between
  utilization functions, and whether those are only Table 1's ρ cannot be
  told unread. On this reading the question stays open for the 1990
  paper, and [LIT-1826](../literature.d/LIT-1826.md) remains the reading owed.

[ARG-236](../arguments.d/ARG-236.md) argues the source step and names the same limit. Either way
the algebra stands: only the attribution would change. The construction
is unchanged.
