---
number: 118
status: Active
formerly:
- CASE-tmptwfjg
title: 'Two competing components with interaction matrix A = [[1, ρ], [ρ, 1]]: with equal growth rates their invasion growth is 1 − ρ, the smallest eigenvalue of the Gram matrix, and with growth rates 1 ± δ the same matrix supports coexistence only when |δ| < (1 − ρ)/(1 + ρ), so feature geometry alone does not fix coexistence'
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added: in Chesson's terms, by Letten et al.'s
    translation (NOTE-1377), ρ is the niche overlap, 1 − ρ the niche
    difference, and the coexistence bound is ρ < f₂/f₁ < 1/ρ;
    Chesson 1990 registered, Unfetched. The construction is
    unchanged.
standing: fictional
kind: construction
tags:
- ecology
- mathematics
- learning-theory
date: '2026-10-18'
line: distributed-agency
supports:
- CLAIM-369
summary: >-
  From the synthesis the owner relayed on 2026-10-18, checked. The
  two-component Lotka–Volterra system with symmetric overlap ρ: invasion
  growth 1 − ρ equals λ_min(A), and κ(A) = (1 + ρ)/(1 − ρ), so overlap
  weakens recovery and ill-conditions the features together. Holding A
  fixed and setting r = (1 + δ, 1 − δ) gives the coexistence equilibrium
  n* = (1/(1 + ρ) ± δ/(1 − ρ)), feasible only when |δ| < (1 − ρ)/(1 + ρ).
  The same representation geometry supports coexistence under one supply
  and exclusion under another.
---
<!-- inactive-ok-file: CLAIM-193 — Proposed or Deferred; open claims, readings and works cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-tmpdoqmq — Unfetched since 2026-10-29; Chesson 1990, cited in the note of that date as not read, nothing here rests on it -->

# CASE-118: Two competing components with interaction matrix A = [[1, ρ], [ρ, 1]]: with equal growth rates their invasion growth is 1 − ρ, the smallest eigenvalue of the Gram matrix, and with growth rates 1 ± δ the same matrix supports coexistence only when |δ| < (1 − ρ)/(1 + ρ), so feature geometry alone does not fix coexistence

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

Chesson's 1990 paper on MacArthur's consumer–resource model, LIT-tmpdoqmq,
is registered and Unfetched, so this case's ρ cannot yet be checked
against his definition at its source. What the record can say comes from
Letten, Ke and Fukami, LIT-1237 (NOTE-1377), who follow that paper. In
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
the case assumes, is what a reading of LIT-tmpdoqmq would settle. The
construction is unchanged.
