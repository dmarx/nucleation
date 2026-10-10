---
number: 177
status: Proposed
formerly:
- THEORY-tmpsywrj
promote_when: >-
  The step the proof quotes is checked at its source: a reading of Jones
  (2019), Proposition 8.4, confirming that every coupling of the observed
  system corresponds to a canonical model with the same per-content
  disagreement probabilities and conversely. An independent derivation of
  the identity from a causal-model formalism would also serve.
  Applications of Δ to data, and restatements in later papers by the same
  group, do not count.
title: 'In a binary cyclic system, the Contextuality-by-Default measure of signalling is twice the least total direct influence of context that any canonical causal model of the data must contain, and each content''s share is the total-variation distance between its marginals'
version: 1
tags:
- contextuality
- probabilistic-modeling
- causality
date: '2026-10-09'
source:
- LIT-851
summary: >-
  Wang, Sadrzadeh, Abramsky & Cervantes (2021), [LIT-851](../literature.d/LIT-851.md),
  Proposition 1. It joins CbD's maximal couplings ([LIT-777](../literature.d/LIT-777.md), Theorem 3.3)
  to Jones's 2019 correspondence between couplings and canonical models,
  which is quoted, not proved. The result measures signalling. It says
  nothing about contextuality, beyond the bound that a rank-2 system with
  Δ ≥ 2 cannot be contextual. The minimum is taken over models, so no
  particular causal model is identified.
supports:
- CLAIM-125
- CLAIM-tmprwo1c
---

<!-- inactive-ok-file: CLAIM-125 — Proposed; open, and cited as the claim this finding bears on -->

# THEORY-177: In a binary cyclic system, the Contextuality-by-Default measure of signalling is twice the least total direct influence of context that any canonical causal model of the data must contain, and each content's share is the total-variation distance between its marginals

## Source

Wang, Sadrzadeh, Abramsky & Cervantes (2021), [LIT-851](../literature.d/LIT-851.md), §3.1:
Proposition 1, Lemma 1, Proposition 2 and Corollary 1, as read in
[NOTE-654](../notes.d/NOTE-654.md).

## What was actually shown

Take a cyclic system with variables valued in {±1}. Each content q is
measured in exactly two contexts, c and c′. CbD's degree of signalling is
Δ = Σ_q |⟨R_q^c⟩ − ⟨R_q^{c′}⟩|. A canonical model in Jones's sense has a
context variable C and a latent background Λ that jointly determine each
content F_q. The direct influence of context on q is the probability over
Λ that F_q(λ, c) ≠ F_q(λ, c′). Let Δ*(F_q) be its least value over all
canonical models that reproduce the observed distributions.

The proposition is Δ = 2 Σ_q Δ*(F_q), with Δ*(F_q) = 1 − Σ_v
min(P[R_q^c = v], P[R_q^{c′} = v]). The proof has three steps:

1. The coupling that keeps a content's copies equal as often as possible
   attains the sum of the pointwise minima (Lemma 1, from [LIT-777](../literature.d/LIT-777.md)'s
   Theorem 3.3).
2. Every coupling corresponds to a canonical model whose direct
   influences are its disagreement probabilities, and conversely (quoted
   from Jones 2019, Proposition 8.4).
3. For ±1 variables, |⟨R⟩ − ⟨R′⟩| = 2(1 − m₊ − m₋).

The paper's worked example checks out: Δ = 1, and Δ* = 7/20 and 3/20. The
identity is a proof. It could fail only through an error in the quoted
step, which is why `promote_when` asks for that step to be read.

## What this does not say

- **Not a contextuality measure.** Δ and Δ* measure how far the marginals
  move, the part CbD sets aside before asking about contextuality. A
  system can have large Δ and be noncontextual. In rank 2, Δ ≥ 2 forces
  noncontextuality.
- **Not the true causal influence.** Δ* is the minimum over all canonical
  models compatible with the data. An actual mechanism may have more
  direct influence. The data identify only the lower bound.
- **Not for non-binary or non-cyclic systems** as stated. The per-content
  formula for Δ* extends to any content in two contexts, but the sum Δ and
  the factor 2 need ±1 variables.
- **Not that signalling in language is "really" causal.** The canonical
  model is a representation that always exists. It is not an empirical
  causal claim about the speaker or the reader.
- **Not about transport.** It measures signalling within one scenario.
  Whether maps between scenarios ([CLAIM-125](../claims.d/CLAIM-125.md)) preserve or bound it is not
  addressed.
