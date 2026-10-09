---
number: 650
status: Read
formerly:
- NOTE-tmpvhpr1
paper: 'LIT-845'
title: 'Closing Bell'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF (2104.11241v2, 24 January 2024, 38
    pages, text layer extracted): the prologue, §§1–6, every definition,
    example and theorem, the epilogue and the reference list. Followed
    step by step: Theorem 29, Lemma 36 with Theorem 37, Lemma 39,
    Theorem 40, Proposition 42, Corollary 43 and the discussion that
    proves Theorem 44; Example 27 (no simulation from the CHSH scenario
    to the triangle) was checked by hand. Theorem 46 (closed category)
    was followed at the level of the constructions; the coherence axioms
    CC1–CC5 are checked in the text only in outline and were not
    re-derived, and Corollary 47 is a sketch. §4.5 of v1 (36 pages) was
    read for comparison to see what v2 corrects. Cited works not read:
    Manzyuk 2012, Abramsky and Hardy 2012, Karvonen 2021 (no catalysis).
date: '2026-10-09'
summary: >-
  Answers which maps between the empirical models of two scenarios are
  induced by classical, non-adaptive procedures: exactly those given by a
  non-contextual model of a hom scenario [S, T] whose outcomes are
  procedures, so deciding it is a linear program. A family of compatible
  local procedures glues into one global procedure exactly when that model
  is non-contextual; the rest are "contextual simulations". The hom
  construction makes scenarios with predicates a closed category.
---

<!-- inactive-ok-file: CLAIM-100 CLAIM-001 CLAIM-105 — Proposed; open, and cited as open: the claims this reading bears on -->
<!-- inactive-ok-file: THEORY-174 — Proposed; cited for what this reading bears on, not as settled -->

# NOTE-650: Closing Bell

## Contribution

Karvonen ([LIT-846](../literature.d/LIT-846.md)) and Abramsky, Barbosa, Karvonen and Mansfield
([LIT-847](../literature.d/LIT-847.md)) defined classical simulations between empirical models.
This chapter asks the converse question: given an arbitrary map from the
models of one scenario to the models of another, is it a classical
simulation? It answers it for non-adaptive procedures, by turning the
map into an empirical model on a new scenario and asking whether that
model is non-contextual. The relative question about maps becomes the
familiar question about objects. The chapter is also a long exposition
of the sheaf framework from the resource side, and it shows that
non-local games and Bell functionals are procedures.

## Key insight

A transformation between two scenarios is itself a behaviour. For each
context of the target, a procedure says which source context to measure
and how to read the result; a family of such local instructions,
consistent on overlaps, is an empirical model on the hom scenario [S, T].
It is a classical procedure exactly when those local instructions come
from one global instruction set, which is to say when that model is
non-contextual. A transport can therefore be contextual in the same
sense that data can.

## Assumptions

- **Finite scenarios** ⟨X, Σ, O⟩ with Σ a simplicial complex, and
  **no-signalling** models (Definition 7, compatibility).
- **Single-use boxes, non-adaptive procedures.** Each target measurement
  calls a fixed set of source measurements; adaptivity is set aside
  because Lemma 39 fails for it (§6.2).
- **Shared classical randomness as convex mixtures of deterministic
  procedures** (Definition 21), which lets both π and α be random.
- **Convex maps.** Only maps preserving convex combinations are
  candidates, a necessary condition (Lemma 24).

## Key results

- **Theorem 29.** e is contextual iff there is no morphism z → e in Emp
  (z the model on the empty scenario); logically contextual iff none in
  Emp_B; strongly contextual iff none in the weak category Emp≤_B.
- **Example 27.** The procedure of Example 20 simulates the PR box from
  the triangle's strongly contextual model (Example 8). No simulation
  goes back: any simplicial relation from the triangle into the CHSH
  scenario lands in one context, whose restriction is non-contextual.
- **§3.5.** A non-local game (input distribution and winning rule) is a
  probabilistic procedure g : S → [2]; a strategy's winning probability
  is EMP(g)e. CHSH: classical value 3/4, the CHSH model 13/16, Tsirelson
  (2 + √2)/4, the PR box 1 (Example 30).
- **Proposition 34.** Every satisfiable possibilistic predicate is
  equivalent to one induced by a possibilistic model.
- **Theorem 37.** A convex map EMP(S) → EMP(T) is determined by its
  values on deterministic models, since every no-signalling model is an
  affine combination of deterministic ones (Theorem 35, from [LIT-016](../literature.d/LIT-016.md))
  and convex maps preserve existing affine combinations (Lemma 36).
- **Lemma 39.** A function of a global assignment has a least set of
  arguments through which it factors, and these least sets are additive
  over tuples.
- **Theorem 40.** A map preserving convex combinations and deterministic
  models is induced by a deterministic procedure iff, for each target
  context σ, the composite E_S(X_S) → E_T(X_T) → E_T(σ) factors through
  E_S(τ) for a single source context τ.
- **Proposition 42 and Corollary 43.** Deterministic procedures S → T are
  the deterministic models of [S, T] satisfying g_{S,T}; probabilistic
  procedures give exactly the non-contextual models of ⟨[S, T], g_{S,T}⟩.
- **Theorem 44 (v2).** A convex map F is induced by a probabilistic
  procedure iff F = F_e for some e on [S, T] that is non-contextual and
  satisfies g_{S,T}. Membership in the image of a polytope under a linear
  map: a linear program.
- **Theorem 46, Corollary 47.** [−, −] makes Scen^g_Det, Scen^g and
  Scen^g_B closed categories; Scen^g_B is isomorphic to the category of
  possibilistic models and weak simulations (Remark 48).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Contextuality at each strength is non-simulability from the empty model in the matching category | strong (proof) | Theorem 29 |
| C2 | Bell functionals and non-local games are procedures into a one-bit scenario | strong (definitional, with worked CHSH) | §3.5, Example 30 |
| C3 | A convex map between model sets is a classical non-adaptive procedure iff some non-contextual model of the hom scenario induces it | strong (proof, as corrected in v2) | Theorem 44 with Corollary 43, Theorem 37 |
| C4 | Compatible local procedures glue into a global one exactly when their hom-scenario model is non-contextual | moderate (argued in prose, not stated as a theorem) | §4.5 |
| C5 | Scenarios with predicates form a closed category | moderate (proof in outline) | Theorem 46, Corollary 47 |
| C6 | The characterisation extends to adaptive procedures | not supported | §6.2: Lemma 39 fails; only the analogue of Theorem 44 is claimed |

## Method

The relative point of view: properties of objects are recast as
properties of morphisms, and then the morphisms are internalised as
objects. The technical core is linear: Theorem 37 uses signed global
sections to determine convex maps from deterministic models; Lemma 39
supplies canonical least supports for deterministic experiments.

## Concepts

- **deterministic procedure** S → T: a simplicial relation π from X_T
  to subsets of X_S and outcome maps α_x : E_S(π(x)) → O_T,x.
- **probabilistic procedure**: a convex mixture of deterministic ones.
- **experiment, predicate**: a procedure into [n], and into [2].
- **simulation e → d**: a procedure f with EMP(f)e = d; possibilistic
  and weak simulations relax "equal" to equal supports and to inclusion.
- **hom scenario** [S, T]: T's measurements and contexts, with outcomes
  ⟨U, α : E_S(U) → O_T,x⟩; the predicate g_{S,T} requires each context's
  outcomes to use a context of S jointly.
- **contextual simulation**: a contextual model of [S, T] (§6.7).

## Connections

Revises the morphisms of [LIT-846](../literature.d/LIT-846.md) (stochastic outcome maps only)
and of [LIT-847](../literature.d/LIT-847.md) (simplicial maps with adaptive protocols) into
mixtures of deterministic procedures over simplicial relations (Remark
28). Uses Abramsky and Brandenburger ([LIT-016](../literature.d/LIT-016.md)) for signed global
sections (Theorem 35). The CHSH game, Specker's triangle, and Boole's
conditions of possible experience frame the exposition. The prologue
cites Wang, Sadrzadeh, Abramsky and Cervantes ([LIT-842](../literature.d/LIT-842.md)) as natural
language among the domains where the same structure occurs.

## Bearing on the record

- **[CLAIM-100](../claims.d/CLAIM-100.md)** (directed transport between scenarios with changing
  covers is the open problem). This is the closest existing answer. A94
  asks "under what conditions can a directed stochastic transport preserve
  … global compatibility while changing its observational cover"; this
  chapter characterises, for no-signalling models and non-adaptive
  procedures, exactly which maps between the models of two arbitrary
  scenarios are classical transports, and every classical transport
  preserves non-contextuality (Theorem 29 composed with any procedure).
  [CLAIM-100](../claims.d/CLAIM-100.md)'s `defeated_if` asks for a framework that "characterizes
  stochastic maps between empirical models with different covers,
  including when they preserve decision-relevant information and global
  compatibility". The global-compatibility part is met here; the
  decision-relevant-information part is not, and signalling data are
  excluded. My reading: [CLAIM-100](../claims.d/CLAIM-100.md) should stay Proposed but narrow its
  open problem to those two parts, and its "Partial prior art" should
  name this chapter and its two predecessors before Gogioso and Pinzani.
- **The manuscript's §6 gap** ("cover-changing or incompatible maps
  demand separate analysis"). §4.5 gives the analysis for the case the
  manuscript calls incompatible: a family of local transport kernels
  compatible on overlaps that does not come from one global kernel is a
  contextual model of [S, T]. That is [CLAIM-070](../claims.d/CLAIM-070.md)'s limit ("false if one
  assumes only local kernels with no globally compatible realization")
  with a name and a test.
- **[CLAIM-105](../claims.d/CLAIM-105.md)** (chains may become more or less contextual). A
  contextual simulation is the only kind of transport that could add
  contextuality; the chapter names the notion and develops none of it.
- **[CLAIM-001](../claims.d/CLAIM-001.md)** (the owner's answer: conditional diffusion already
  covers directed transport). This chapter is prior art from the sheaf
  side, closer to A94's question than the diffusion literature, because
  it decides gluing exactly rather than combining conditional scores.
- Produces [THEORY-174](../theory.d/THEORY-174.md), with [LIT-846](../literature.d/LIT-846.md) and [LIT-847](../literature.d/LIT-847.md).
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- No-signalling models only; nothing on signalling or
  Contextuality-by-Default data.
- Non-adaptive procedures only for the sharp result (Theorem 40); the
  adaptive analogue of Theorem 44 is asserted in §6.2 without proof.
- The published chapter states the uncorrected Theorem 44; v2 is the
  version of reference by the authors' own note.
- The gluing statement of §4.5 is argued in prose.
- Contextual simulations are named, not studied.

## Open questions

- Adaptive versions of Theorem 40 and of the closed structure; a
  monoidal closed structure, which seems to need directed adaptive
  tensors (§6.3).
- What contextual simulations can do, and whether they match maps
  d ⊗ c → e with c contextual (§6.7).
- A Stone-type duality with generalised partial Boolean algebras, with
  [2] as dualising object (§6.4).
