---
number: 177
status: Active
formerly:
- THEORY-tmpsywrj
title: "In a binary cyclic system, the Contextuality-by-Default measure of signalling is twice the sum, over contents, of the least direct influence of context that a canonical causal model of the data must place on each content, and each content's least influence is the total-variation distance between its two marginals"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-177 (batch 045, ADR-047 v2). The dated note below derives the
    correspondence between canonical models and couplings from the causal-
    model side, which the promote_when accepts in place of reading Jones's
    Proposition 8.4. "The least total direct influence" becomes the sum of
    per-content minima: one model reaches every content's minimum at once
    only when the system is noncontextual, so in a contextual system the
    least total is larger.
tags:
- contextuality
- probabilistic-modeling
- causality
date: '2026-10-09'
source:
- LIT-851
summary: >-
  Wang, Sadrzadeh, Abramsky & Cervantes (2021), [LIT-851](../literature.d/LIT-851.md), Proposition 1. It
  joins CbD's maximal couplings ([LIT-777](../literature.d/LIT-777.md), Theorem 3.3) to Jones's 2019
  correspondence between couplings and canonical models, which the paper
  quotes and the record derives independently. The result measures
  signalling. Its minima are per content, each reached in its own model;
  one model reaches them all only if the system is noncontextual. It says
  nothing about contextuality beyond the bound that a rank-2 system with Δ
  ≥ 2 cannot be contextual, and identifies no particular causal model.
supports:
- CLAIM-125
- CLAIM-245
---

<!-- inactive-ok-file: CLAIM-125 — Proposed; open, and cited as the claim this finding bears on -->

# THEORY-177: In a binary cyclic system, the Contextuality-by-Default measure of signalling is twice the sum, over contents, of the least direct influence of context that a canonical causal model of the data must place on each content, and each content's least influence is the total-variation distance between its two marginals

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

The proposition is Δ = 2 Σ_q Δ*(F_q), a sum of per-content minima, with Δ*(F_q) = 1 − Σ_v
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

## Note of 2026-10-19: the quoted step, derived

Derived for the promotion audit (batch 045, [ADR-047](../decisions.d/ADR-047.md) v2) from the
causal-model side, as the promote_when allows. A canonical model has
context C and background Λ, with Λ independent of C. The definition of
direct influence as P(Λ ∈ {λ : F_q(λ, c) ≠ F_q(λ, c′)}), unconditional on
the context, requires that. F_q(Λ, c) is distributed as the observed R_q^c.

1. **Every model gives a coupling.** Take content q, measured in
   contexts c and c′. Since Λ is independent of C, the pair
   (F_q(Λ, c), F_q(Λ, c′)) has the two observed marginals, so it is a
   coupling of them. Its disagreement probability is q's direct influence.
   So every model's direct influence on q is at least the least
   disagreement over couplings. That is 1 − Σ_v min(P[R_q^c = v],
   P[R_q^{c′} = v]), the total-variation distance, reached by the maximal
   coupling ([LIT-777](../literature.d/LIT-777.md), Theorem 3.3).
2. **The minimal coupling gives a model, for one content at a time.**
   Fix the maximal coupling of q's two copies, and leave the other
   contents' copies uncoupled. In a cyclic system the remaining
   constraints, the context bundles and q's pair, form a path with no
   cycle. So they glue into one joint distribution by conditional
   independence along it. Taking Λ to be that joint reproduces every
   context's observed distribution and gives q the least direct
   influence. So Δ*(F_q) equals the total-variation distance.
3. **The factor 2.** For ±1 variables with P(R = +1) = p,
   |⟨R⟩ − ⟨R′⟩| = 2|p − p′| = 2·TV. Summing over contents,
   Δ = 2 Σ_q Δ*(F_q).

Step 2 reaches each content's minimum in its own model. A single model
that reached every content's minimum at once would be a coupling with
every connection maximal. In Contextuality-by-Default that exists exactly
when the system is noncontextual. So the least total direct influence of
one model equals Δ/2 for a noncontextual system and exceeds it for a
contextual one, which is why the title now says "the sum, over contents,
of the least".
