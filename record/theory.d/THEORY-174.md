---
number: 174
status: Active
formerly:
- THEORY-tmprxblg
title: 'Classical simulations between no-signalling empirical models on different scenarios never create contextuality, and a convex map between two scenarios'' model sets is induced by a classical non-adaptive procedure exactly when some non-contextual model of the hom scenario that satisfies its predicate induces it'
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    At the owner's direction, carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-174.yaml, batch 005, ADR-047),
    the monotonicity half is filed apart as THEORY-720, Active: (a)
    non-contextual models are those the empty model simulates, (b) NCF
    cannot fall along a simulation, (c) strong contextuality is reflected
    backwards, and (d) no cloning. This THEORY extends it and keeps the
    characterisation half (LIT-845 Theorem 44, as corrected in v2). Its
    promote_when already concerned only that half; its last sentence now
    names the split. The claim and the status are unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    Promoted by the fifteenth status review on a checked re-derivation of
    the corrected Theorem 44 (ADR-047's evidence ruling: a checked
    step-by-step re-derivation meets a request for a proof), at the status
    review's ruling (the owner delegated these rulings). The proof is in
    the note of 2026-10-29, and a script run at the review checked it on
    the binary triangle scenario. The old title: Classical simulations
    between empirical models on different scenarios never create
    contextuality, and a map between model sets is such a simulation
    exactly when a non-contextual model of the hom scenario induces it.
    The title now names no-signalling models and hom models that satisfy
    the predicate; that corrects an imprecise statement of what the
    sources prove (ADR-047, kind 3), and nothing is dropped by it. It also
    narrows the characterisation to non-adaptive procedures. The adaptive
    analogue, which LIT-845 section 6.2 asserts without proof, is a clause
    the source asserts (ADR-047, kind 1), so it is filed as
    THEORY-1170, Proposed, which extends this entry.
tags:
- contextuality
- mathematics
- quantum-foundations
date: '2026-10-09'
source:
- LIT-846
- LIT-847
- LIT-845
extends:
- THEORY-720
summary: >-
  Karvonen (2018), [LIT-846](../literature.d/LIT-846.md); Abramsky, Barbosa, Karvonen & Mansfield
  (2019), [LIT-847](../literature.d/LIT-847.md); Barbosa, Karvonen & Mansfield (2021, v2 2024),
  [LIT-845](../literature.d/LIT-845.md). A simulation answers each measurement of the target by a
  jointly measurable set of the source's, with shared classical
  randomness, so the cover may change. Along any simulation the
  non-contextual fraction cannot fall; contextual models cannot be
  cloned; and which maps between model sets are classical non-adaptive
  procedures is a non-contextuality question on a hom scenario,
  re-derived here. No-signalling models
  only, and nothing about information preserved.
supports:
- CLAIM-100
---

<!-- inactive-ok-file: CLAIM-100 — Superseded; open, and cited as open: the claim this theory bears on -->
<!-- inactive-ok-file: THEORY-156 — Proposed; cited for what this theory does not say, not as settled -->

# THEORY-174: Classical simulations between no-signalling empirical models on different scenarios never create contextuality, and a convex map between two scenarios' model sets is induced by a classical non-adaptive procedure exactly when some non-contextual model of the hom scenario that satisfies its predicate induces it

## Source

Karvonen, *Categories of Empirical Models* ([LIT-846](../literature.d/LIT-846.md)), Definition
3.9 and Theorems 4.1, 4.3, 4.5 and 4.8, as read in [NOTE-651](../notes.d/NOTE-651.md).
Abramsky, Barbosa, Karvonen and Mansfield, *A comonadic view of
simulation and quantum resources* ([LIT-847](../literature.d/LIT-847.md)), Proposition 7 and
Theorems 17, 20–22, as read in [NOTE-647](../notes.d/NOTE-647.md). Barbosa, Karvonen and
Mansfield, *Closing Bell* ([LIT-845](../literature.d/LIT-845.md), arXiv v2), Theorems 29, 37, 40
and 44 and §4.5, as read in [NOTE-650](../notes.d/NOTE-650.md).

## What was actually shown

Take two finite measurement scenarios S and T, with possibly unrelated
covers. A classical procedure from S to T answers each measurement x of T
by measuring a set π(x) of S's measurements and post-processing the
outcomes. π must send every context of T into a context of S, so the
agent never attempts an incompatible set. Shared classical randomness is
allowed, as a stochastic outcome map (Karvonen), as an auxiliary
non-contextual model (the comonadic paper, which also allows adaptive
choices), or as a mixture of deterministic procedures (Closing Bell).
Every no-signalling empirical model on S is then pushed forward to one on
T.

Three results hold across all three formulations. First, a model is
non-contextual exactly when it can be simulated from the model on the
empty scenario ([LIT-846](../literature.d/LIT-846.md) Theorem 4.1; [LIT-845](../literature.d/LIT-845.md) Theorem 29, which
extends this to logical and strong contextuality). Second, if d simulates
e then NCF(d) ≤ NCF(e): the contextual fraction cannot increase (Theorem
4.5; Theorem 21), and strong contextuality is reflected backwards (Theorem
4.3). Third, a model can be used to simulate two independent copies of
itself only if it is non-contextual (Theorem 4.8; Theorem 22). The
comonadic paper adds that adaptive simulation is the same preorder as
convertibility by the free operations, which include translation of
measurements along any simplicial map and conditional measurement
(Theorem 20).

Closing Bell answers the converse question for non-adaptive procedures.
A map F from S's models to T's models preserves convex combinations if it
is a simulation (Lemma 24), and is then fixed by its values on
deterministic models (Theorem 37). It is induced by a procedure exactly
when F = F_e for some non-contextual model e of the hom scenario [S, T]
(T's contexts, with procedures into S as outcomes), satisfying the
predicate that each context uses a context of S (Theorem 44, as
corrected in v2). Deciding this is a linear program. A family of local
procedures that agree on overlaps but do not glue into one global
procedure is a contextual model of [S, T].

What could have come out otherwise: a cover-changing map built from
locally classical pieces could have produced a global inconsistency the
source lacked. It cannot when the pieces form one procedure, and Closing
Bell shows that whether they do is itself a contextuality question.

## What this does not say

- **Nothing about signalling data.** Every result assumes
  no-signalling; Karvonen's pushforward is undefined without it (Remark
  3.2). Contextuality-by-Default systems and corpus or language-model
  data ([LIT-842](../literature.d/LIT-842.md), [LIT-844](../literature.d/LIT-844.md)) are outside its reach.
- **Nothing about information preserved.** The simulation preorder
  orders resources by contextuality. It is not shown to relate to
  Blackwell's informativeness order ([THEORY-156](THEORY-156.md)), and no result says when
  a transport preserves what a decision-maker could learn from the
  source.
- **Not that contextual transports are understood.** "Contextual
  simulations", models of [S, T] that do not glue, are named in
  [LIT-845](../literature.d/LIT-845.md) (§6.7) and not studied; this theory says only that such a
  family is not a classical procedure; the map it induces may still be
  one (note of 2026-10-29).
- **Not the adaptive characterisation.** Theorem 40 fails to transfer to
  adaptive procedures because its key lemma fails (§6.2); the adaptive
  form of Theorem 44 is asserted without proof. It is [THEORY-1170](THEORY-1170.md),
  Proposed.
- **Not a statement about language or translation.** The use made of it
  for the manuscript's transport problem ([CLAIM-100](../claims.d/CLAIM-100.md)) is the readers', in
  the NOTEs, and not the authors'.

## Note of 2026-10-19: the monotonicity half filed apart

The three results that "hold across all three formulations" above are now
[THEORY-720](THEORY-720.md), Active, sourced to [LIT-846](../literature.d/LIT-846.md) and [LIT-847](../literature.d/LIT-847.md), whose proofs [NOTE-651](../notes.d/NOTE-651.md)
and [NOTE-647](../notes.d/NOTE-647.md) followed. Its no-cloning result cites [LIT-847](../literature.d/LIT-847.md) Theorem 22 rather
than [LIT-846](../literature.d/LIT-846.md) Theorem 4.8, which rests on a monoidal structure the paper
asserts without checking. What keeps this THEORY Proposed is the
characterisation: which maps between model sets are classical procedures.

## Note of 2026-10-29: Theorem 44 re-derived

The corrected statement follows from the definitions with Corollary 43,
in two short steps. Write a deterministic procedure f = (π, α) as a global
assignment x ↦ ⟨π(x), α_x⟩ of the hom scenario [S, T]. It satisfies
g_{S,T} on every context, because π sends each context of T into a
context of S. For a model e on [S, T] that satisfies g, set
F_e(d)_σ(t) = Σ_a e_σ(a) · d|_τ{s : α_x(s|U_x) = t_x for x ∈ σ}, with τ
any context of S containing the U_x. No-signalling makes this independent
of τ.

- **If F = Σ_k p_k EMP(f_k),** let e be the marginals of p on the contexts
  of T. It is non-contextual by construction, and its supports satisfy
  g. The summand for a context depends only on f_k's restriction to it,
  so F_e = F.
- **If e is non-contextual,** some distribution q on global assignments of
  [S, T] has e's marginals. Each global assignment in q's support
  restricts on each context into e's support, which satisfies g, so each
  is a deterministic procedure, and F_e = Σ_f q(f) EMP(f).

Neither step uses convexity or Theorem 37. They enter only in deciding
the condition for a map given as a black box: Theorem 37 fixes a convex
map by its values on deterministic models, and the condition becomes a
linear program over deterministic procedures.

The map e ↦ F_e is not injective, so the theorem's "some" matters. A
contextual model of [S, T] can induce a classical map, for instance one
that writes the constant 0 as two different local procedures in a
strongly contextual pattern. So a contextual simulation in §6.7's sense
is a family of local procedures that does not glue, not necessarily a map
that no classical procedure induces.

A script run at the review checked this on the binary triangle as both S
and T: 52,472 deterministic procedures, 12,152 distinct maps. F_p and
F_{e_p} agreed exactly on 20 random procedures and ten no-signalling
models, the strongly contextual one included. The linear program
recognised random classical maps (residual below 10⁻¹³), and the
procedure it recovered reproduced the map on contextual models, which is
Theorem 37 at work. Two contextual hom models whose maps send every model
to the contextual triangle model were rejected (residual 1.6), and the
non-injective case was accepted. As a control on the well-definedness
check, a signalling source made the result depend on the choice of τ.
