---
status: Active
title: 'Classical simulations between no-signalling empirical models on finite scenarios, which may change the cover, never create contextuality: a model is non-contextual exactly when the empty model simulates it, the non-contextual fraction cannot fall along a simulation, strong contextuality is reflected backwards, and only non-contextual models can be cloned'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-174 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-174.yaml, batch 005, ADR-047).
    THEORY-174's promote_when concerns only its characterisation half (the
    corrected Theorem 44 of LIT-845) and says "the monotonicity half is
    already proved in refereed venues". This THEORY holds that half.
    NOTE-651 followed the proofs of Theorems 4.1, 4.3 and 4.5 of LIT-846
    step by step, and NOTE-647 followed the no-cloning proof of LIT-847
    Theorem 22. The monotonicity step was checked again for the split.
    THEORY-174 keeps the characterisation and extends this one.
tags:
- contextuality
- mathematics
- quantum-foundations
date: '2026-10-19'
source:
- LIT-846
- LIT-847
summary: >-
  Karvonen (2018), [LIT-846](../literature.d/LIT-846.md), Theorems 4.1, 4.3 and 4.5, read in [NOTE-651](../notes.d/NOTE-651.md);
  Abramsky, Barbosa, Karvonen & Mansfield (2019), [LIT-847](../literature.d/LIT-847.md), Theorems 21 and
  22, read in [NOTE-647](../notes.d/NOTE-647.md). A classical simulation answers each measurement of
  the target by a jointly measurable set of the source's, with shared
  classical randomness, so the cover may change. Non-contextual models are
  exactly those the empty model simulates, NCF cannot fall along a
  simulation, strong contextuality is reflected backwards, and a model
  clones itself only if it is non-contextual. No-signalling models on
  finite scenarios only. Which maps are simulations is [THEORY-174](THEORY-174.md)'s open
  half.
extended_by:
- THEORY-174
---
<!-- inactive-ok-file: THEORY-174 — Proposed; the characterisation this half was split from and that extends it, cited as open -->
<!-- inactive-ok-file: THEORY-156 — Proposed; cited for what this theory does not say, not as settled -->

# THEORY-tmp4o2p3: Classical simulations between no-signalling empirical models on finite scenarios, which may change the cover, never create contextuality: a model is non-contextual exactly when the empty model simulates it, the non-contextual fraction cannot fall along a simulation, strong contextuality is reflected backwards, and only non-contextual models can be cloned

## Source

Karvonen, *Categories of Empirical Models* ([LIT-846](../literature.d/LIT-846.md)), Definition 3.9 and
Theorems 4.1, 4.3 and 4.5, as read in [NOTE-651](../notes.d/NOTE-651.md) (claims C1–C3, "strong
(proof)", proofs followed step by step). Abramsky, Barbosa, Karvonen and
Mansfield, *A comonadic view of simulation and quantum resources*
([LIT-847](../literature.d/LIT-847.md)), Theorems 21 and 22, as read in [NOTE-647](../notes.d/NOTE-647.md) (claim C4, proof
followed). Both are refereed (QPL 2018 in EPTCS, and LICS 2019).

## What was actually shown

Take two finite measurement scenarios S and T, with possibly unrelated
covers. A classical procedure from S to T answers each measurement x of T
by measuring a set π(x) of S's measurements and post-processing the
outcomes. π sends every context of T into a context of S, so no
incompatible set is attempted. Shared classical randomness is allowed: as
a stochastic outcome map ([LIT-846](../literature.d/LIT-846.md)), or as an auxiliary non-contextual
model, with adaptive choices ([LIT-847](../literature.d/LIT-847.md)). Each no-signalling empirical model
d on S is pushed forward to one on T. When some procedure takes d to e, d
simulates e.

- **(a) Non-contextuality is simulability from nothing.** A model is
  non-contextual exactly when the model on the empty scenario simulates it
  ([LIT-846](../literature.d/LIT-846.md) Theorem 4.1). A simulation from the empty scenario is a mixture
  of deterministic assignments, which is Fine's form of a non-contextual
  model.
- **(b) The non-contextual fraction cannot fall.** If d simulates e, then
  NCF(d) ≤ NCF(e) ([LIT-846](../literature.d/LIT-846.md) Theorem 4.5; [LIT-847](../literature.d/LIT-847.md) Theorem 21). The check:
  write d = λd₀ + (1 − λ)d₁ with d₀ non-contextual and λ = NCF(d). The
  pushforward F is affine, so F(d) = λF(d₀) + (1 − λ)F(d₁). F(d₀) is
  non-contextual, by (a) and composition of simulations. So NCF(e) ≥ λ.
  Equivalently, the contextual fraction cannot rise.
- **(c) Strong contextuality is reflected backwards.** If e is strongly
  contextual and d simulates e, then d is strongly contextual ([LIT-846](../literature.d/LIT-846.md)
  Theorem 4.3).
- **(d) No cloning.** e simulates e ⊗ e exactly when e is non-contextual
  ([LIT-847](../literature.d/LIT-847.md) Theorem 22). The proof first rules out NCF(e) = 0 by pigeonhole
  on the finitely many protocol components. It then rules out
  0 < NCF(e) < 1, since (b) and NCF(e ⊗ e) = NCF(e)² would give
  NCF(e) ≤ NCF(e)².

What could have come out otherwise: a map that changes the cover and is
built from locally classical pieces could have produced a global
inconsistency the source lacked. It cannot, when the pieces form one
procedure.

## What this does not say

- **Which maps between model sets are simulations.** That characterisation
  ([LIT-845](../literature.d/LIT-845.md) Theorem 44, correct only in its v2 form) is [THEORY-174](THEORY-174.md)'s, and is
  Proposed.
- **Nothing about signalling data.** Every result assumes no-signalling.
  The pushforward is undefined without it ([LIT-846](../literature.d/LIT-846.md) Remark 3.2), so
  Contextuality-by-Default systems are outside its reach.
- **Nothing about information preserved.** The simulation preorder orders
  resources by contextuality. It is not shown to relate to Blackwell's
  informativeness order ([THEORY-156](THEORY-156.md)).
- **Not for [LIT-846](../literature.d/LIT-846.md)'s monoidal form of no-cloning.** [LIT-846](../literature.d/LIT-846.md)'s Theorem 4.8
  rests on a monoidal structure that the paper asserts without checking.
  (d) is cited to [LIT-847](../literature.d/LIT-847.md) Theorem 22, whose proof was followed.
