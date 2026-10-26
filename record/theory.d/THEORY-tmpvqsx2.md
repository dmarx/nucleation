---
status: Active
title: 'In Musat, Pimentel, Zucchet and Hofmann''s two-layer attention-only transformer on in-context bigrams, once an in-weights circuit that maps each common token to its memorized partner has saturated, the population gradient on the induction circuit is what it would be without it multiplied by fr + (1 − fr)fv, the share of the data the memorized map does not solve, up to errors that vanish at large vocabulary and large in-weights margin when no distractor block carries the query''s partner; the two circuits occupy orthogonal coordinates and still interact, because they solve overlapping parts of the data'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpcuw4h. The result is the paper's Theorem 2,
    proved in its Appendix D.4. The proof's decomposition and its bound on
    the scrambled part were checked step by step below, which meets the
    condition for Active under ADR-047 v2. The reading as a source of
    sequential onset, and its relation to THEORY-783, are the record's.
tags:
- learning-theory
date: '2026-10-26'
source:
- LIT-tmp01if4
summary: >-
  Musat et al. (2026), [LIT-tmp01if4](../literature.d/LIT-tmp01if4.md), read in [NOTE-tmpcuw4h](../notes.d/NOTE-tmpcuw4h.md). A memorized
  shortcut that solves part of the data removes the in-context circuit's
  gradient on that part and leaves the rest. It is a theorem in an
  idealized model under a disjointness assumption (A4) that the paper's
  own sampler violates, at a cost it states. It does not say the observed
  order in the paper's one run is due to it: there fr = 0.9 and the
  factor is 0.9.
---
<!-- inactive-ok-file: THEORY-783 CLAIM-367 — Proposed; the account and claim this one is set beside, cited as open -->

# THEORY-tmpvqsx2: In Musat, Pimentel, Zucchet and Hofmann's two-layer attention-only transformer on in-context bigrams, once an in-weights circuit that maps each common token to its memorized partner has saturated, the population gradient on the induction circuit is what it would be without it multiplied by fr + (1 − fr)fv, the share of the data the memorized map does not solve, up to errors that vanish at large vocabulary and large in-weights margin when no distractor block carries the query's partner; the two circuits occupy orthogonal coordinates and still interact, because they solve overlapping parts of the data

## Source

Musat, Pimentel, Zucchet and Hofmann (2026), arXiv:2607.11875,
[LIT-tmp01if4](../literature.d/LIT-tmp01if4.md), read in full in [NOTE-tmpcuw4h](../notes.d/NOTE-tmpcuw4h.md): §4.2 (equations (11)–(13))
and Appendix D.4 (Lemmas 1–4, Remark 1).

## What was actually shown

**The setting.** The simplified architecture of [THEORY-tmpdxhxm](THEORY-tmpdxhxm.md) with two
layers and one head each. The induction circuit is the direction
(α, β, γ): W^(1) = αM, W^(2) = βI^(t)V^(1)ᵀ, W̄ = γI^(t)V^(2)ᵀ. The
in-weights circuit is W̄ = δC. Queries are rare with probability fr; a
common query's in-context partner differs from its canonical one with
probability fv.

**The argument, checked.**
1. *Split the data.* Three parts: rare queries (mass fr), common queries
   whose in-context partner is the canonical one (mass (1 − fr)(1 − fv)),
   and common queries whose partner differs (mass (1 − fr)fv). The masses
   sum to 1, and the expected gradient is the mass-weighted sum of the
   three parts' gradients.
2. *The induction gradient's Jacobian does not see δ* (Lemma 1). The ICL
   coordinates enter the logits only through write subspaces orthogonal
   to the token subspace, which C annihilates. So δ enters the ICL
   gradient only through the softmax probabilities p(z), and
   ∇_ICL L = (p(z) − y)ᵀJ with J independent of δ.
3. *Canonical part* (Lemma 2). Both circuits push the correct logit, so
   ‖p(z) − y‖ = O(|V|e^{−δ}), and with ‖J‖₁ = O(1) the gradient is of that
   order. The memorized map has removed it.
4. *Rare part* (Lemma 3). C e_q = 0 for a rare query, so nothing changes.
5. *Scrambled part* (Lemma 3). Adding δ moves Θ(1) probability onto the
   wrong token x′_q and rescales every other probability down, each by at
   most O(|V|⁻¹). The change in the gradient, Δpᵀ J, is then bounded by
   |Δp_{x′_q}||J_{x′_q}| + max_{x≠x′_q}|Δp_x| ‖J‖₁. The second term is
   O(|V|⁻¹). The first is O(|V|⁻¹) only if J_{x′_q} = O(|V|⁻¹), which is
   assumption (A4): the canonical partner never appears in the context,
   so the induction circuit never reads it.
6. *Equal gradients without the in-weights circuit* (Lemma 4). With
   orthonormal common embeddings and lexinvariant rare ones, the ICL-only
   loss depends on the target only through γ and |V|, so the three parts'
   ICL-only gradients agree up to O(|V|⁻¹).
7. Summing: (fr + (1 − fr)fv) ∇_ICL L(W) + O(|V|e^{−δ}) + O(|V|⁻¹).

Step 5's split into an ℓ∞ bound on Δp and an ℓ1 bound on J is needed; the
paper notes that a per-coordinate bound summed over |V| coordinates gives
only O(1).

**What could have come out otherwise.** The in-weights circuit could have
interfered on the parts it does not solve, through the shared softmax.
Steps 4–5 show it does not, to first order, except through the
canonical-partner coordinate that (A4) removes.

## What this does not say

- **Not for the paper's sampler.** That sampler does not enforce (A4). A
  distractor carries the canonical partner with probability
  Θ(n fc/|V^c|), and then the error is O(|V|⁻¹ + n fc/|V^c|), which
  "does not vanish in the orthonormal idealization" (Remark 1). With 16
  common tokens this is not small.
- **Not that it explains the run in Fig. 3.** That run has fr = 0.9 and
  fv = 0 (D.1), where the factor is 0.9. The in-context circuit's delay
  there owes more to its being a product of three small coordinates, a
  small-initialization plateau, while δ is a single coordinate. The paper
  says the delay "grows as fr decreases or as fv → 0".
- **Not a statement about real transformers,** whose value maps are
  learned and whose embeddings are not orthonormal.
- **Not an instruction** for data curation; that would be the anthology's.

## Connections

- **[THEORY-783](THEORY-783.md) and [QUESTION-193](../questions.d/QUESTION-193.md).** Under plain gradient descent this
  gives one circuit starting after another for a reason that is neither
  competition for coordinate signs nor dependence of one skill on
  another: redundancy, two circuits solving overlapping parts of the data,
  so the first to saturate takes the shared part's gradient. It does not
  meet [THEORY-783](THEORY-783.md)'s refutation clause, which asks for orthogonal *skills*:
  here the coordinates are orthogonal but the losses are not separate
  per-skill terms, as they are in the Geometry model of [THEORY-253](THEORY-253.md). So it
  is a third source of sequential onset beside the two [THEORY-783](THEORY-783.md) names,
  in an idealized model.
- **[CLAIM-367](../claims.d/CLAIM-367.md).** The rate at which the induction circuit forms is set by
  data statistics (fr, fv, and by Theorem 3 burstiness b), a condition of
  training that belongs to the data–optimizer–network system.
- **Theorem 3 of the same paper** (burstiness multiplies the induction
  gradient by b, up to a factor 1 + O(b/n)) is the complementary result.
  It is not filed separately.
