---
status: Proposed
promote_when: >-
  An independent proof, read and checked, of the corrected Theorem 44 of
  LIT-tmp5at9s (a convex map between the model sets of two scenarios is
  induced by a classical non-adaptive procedure iff some non-contextual
  model of the hom scenario induces it), or a refereed publication of the
  corrected statement; the published chapter carries the uncorrected one.
  Further examples of contextuality-monotone operations cannot settle it,
  since the monotonicity half is already proved in refereed venues.
title: 'Classical simulations between empirical models on different scenarios never create contextuality, and a map between model sets is such a simulation exactly when a non-contextual model of the hom scenario induces it'
version: 1
tags:
- contextuality
- mathematics
- quantum-foundations
date: '2026-10-09'
source:
- LIT-tmpes6yu
- LIT-tmpjk0t0
- LIT-tmp5at9s
summary: >-
  Karvonen (2018), [LIT-tmpes6yu](../literature.d/LIT-tmpes6yu.md); Abramsky, Barbosa, Karvonen & Mansfield
  (2019), [LIT-tmpjk0t0](../literature.d/LIT-tmpjk0t0.md); Barbosa, Karvonen & Mansfield (2021, v2 2024),
  [LIT-tmp5at9s](../literature.d/LIT-tmp5at9s.md). A simulation answers each measurement of the target by a
  jointly measurable set of the source's, with shared classical
  randomness, so the cover may change. Along any simulation the
  non-contextual fraction cannot fall; contextual models cannot be
  cloned; and which maps between model sets are simulations is a
  non-contextuality question on a hom scenario. No-signalling models
  only, and nothing about information preserved.
supports:
- CLAIM-100
---

<!-- inactive-ok-file: CLAIM-100 — Proposed; open, and cited as open: the claim this theory bears on -->
<!-- inactive-ok-file: THEORY-156 — Proposed; cited for what this theory does not say, not as settled -->

# THEORY-tmprxblg: Classical simulations between empirical models on different scenarios never create contextuality, and a map between model sets is such a simulation exactly when a non-contextual model of the hom scenario induces it

## Source

Karvonen, *Categories of Empirical Models* ([LIT-tmpes6yu](../literature.d/LIT-tmpes6yu.md)), Definition
3.9 and Theorems 4.1, 4.3, 4.5 and 4.8, as read in [NOTE-tmpvuygo](../notes.d/NOTE-tmpvuygo.md).
Abramsky, Barbosa, Karvonen and Mansfield, *A comonadic view of
simulation and quantum resources* ([LIT-tmpjk0t0](../literature.d/LIT-tmpjk0t0.md)), Proposition 7 and
Theorems 17, 20–22, as read in [NOTE-tmp6dxz0](../notes.d/NOTE-tmp6dxz0.md). Barbosa, Karvonen and
Mansfield, *Closing Bell* ([LIT-tmp5at9s](../literature.d/LIT-tmp5at9s.md), arXiv v2), Theorems 29, 37, 40
and 44 and §4.5, as read in [NOTE-tmpvhpr1](../notes.d/NOTE-tmpvhpr1.md).

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
empty scenario ([LIT-tmpes6yu](../literature.d/LIT-tmpes6yu.md) Theorem 4.1; [LIT-tmp5at9s](../literature.d/LIT-tmp5at9s.md) Theorem 29, which
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
  data ([LIT-842](../literature.d/LIT-842.md), [LIT-tmp2g08h](../literature.d/LIT-tmp2g08h.md)) are outside its reach.
- **Nothing about information preserved.** The simulation preorder
  orders resources by contextuality. It is not shown to relate to
  Blackwell's informativeness order ([THEORY-156](THEORY-156.md)), and no result says when
  a transport preserves what a decision-maker could learn from the
  source.
- **Not that contextual transports are understood.** "Contextual
  simulations", models of [S, T] that do not glue, are named in
  [LIT-tmp5at9s](../literature.d/LIT-tmp5at9s.md) (§6.7) and not studied; this theory says only that they
  are not classical procedures.
- **Not the adaptive characterisation.** Theorem 40 fails to transfer to
  adaptive procedures because its key lemma fails (§6.2); the adaptive
  form of Theorem 44 is asserted without proof.
- **Not a statement about language or translation.** The use made of it
  for the manuscript's transport problem ([CLAIM-100](../claims.d/CLAIM-100.md)) is the readers', in
  the NOTEs, and not the authors'.
