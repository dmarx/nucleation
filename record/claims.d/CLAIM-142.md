---
number: 142
status: Proposed
formerly:
- CLAIM-tmpd1aee
title: 'Two communicative realizations can agree on every probe in a restricted family without being structurally identical, so observational equivalence is relative to the probes, and only independently justified probes evaluated on held-out cases are evidence that structure was preserved'
version: 1
role: thesis
defeated_if: >-
  For the communicative kinds studied, a finite probe family fixed in
  advance separates every pair of realizations that judges distinguish,
  on held-out realizations, so that observational and structural
  identity coincide in practice.
tags:
- epistemology
- individuation
- mathematics
date: '2026-10-10'
line: pragmatic-transport
rests_on:
- CLAIM-046
- CLAIM-011
grounds:
- THEORY-032
- LIT-221
uses:
- TERM-014
complements:
- CLAIM-050
- CLAIM-149
summary: >-
  It began at the owner's U45 pointer to Yoneda, and A158 §5 gave it
  its first form. A173, A178 §3.2, A184 §2, A203 §§8 and 14, A214 §3
  and A218 Ch7 restate it; A203 calls it "our central epistemic
  distinction". The mathematical half is elementary and exact. The
  substantive half is the realist commitment that communicative
  identity is not exhausted by any probe profile. It makes [TERM-014](../terms.d/TERM-014.md)'s
  equivalence class probe-relative, and puts a realist reading over
  [CLAIM-046](CLAIM-046.md)'s methodological ordering.
illustrated_by:
- CASE-041
supports:
- CLAIM-129
- CLAIM-133
- CLAIM-139
---
<!-- inactive-ok-file: CLAIM-046 CLAIM-050 CLAIM-038 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: TERM-002 — Superseded; cited as the definition the Yoneda reading restates, not as current -->

# CLAIM-142: Two communicative realizations can agree on every probe in a restricted family without being structurally identical, so observational equivalence is relative to the probes, and only independently justified probes evaluated on held-out cases are evidence that structure was preserved

## The claim

A158 §5, after the owner's U45 ("There's definitely a connection here to
Yoneda's Lemma"), restricted an object's profile to a selected family of
probes: "This restricted profile may no longer distinguish all objects. And
that is precisely our fidelity problem."

A203 §8 made it a premise: "Two objects may be indistinguishable by all
probes in 𝒬 without being isomorphic in the full category. This is our
central epistemic distinction: **Full structural identity and
observationally recoverable identity are not the same thing.**" A203 §14
drew the evidential rule: "Two realizations may have the same response
distributions under every probe in 𝒬. That provides observational
equivalence relative to the chosen probes. It does not guarantee complete
structural identity ... A probe family selected solely to make two
representations appear equivalent provides weak evidence of structural
preservation. A probe family justified independently and evaluated on
held-out cases provides much stronger evidence." A218 Ch7's core claim: "A
structural kind may be real while remaining indistinguishable under an
insufficient family of empirical probes."

The claim has two halves. The first is that observational equivalence
([TERM-014](../terms.d/TERM-014.md)) is relative to the probe family, and may be coarser than
structural identity. The second is the rule of evidence, which is
[CLAIM-011](CLAIM-011.md)'s remedy applied to probes: only probes justified independently
of the comparison, and evaluated on held-out cases, are evidence that
structure was preserved.

## The exact half

**When a restricted family identifies.** The restricted Yoneda functor
A ↦ Hom(−,A)|_𝒬 is fully faithful exactly when 𝒬 is dense. Examples: the
one-point set in Set; the vertex and the edge in graphs. When 𝒬 is only a
strong generator (in a category with finite limits), the functor reflects
isomorphisms without capturing all morphisms. Example: ℤ in groups, where
Hom(ℤ,−) is the underlying set. Any other family identifies objects only up
to an equivalence coarser than isomorphism, and that coarser equivalence is
what [TERM-014](../terms.d/TERM-014.md) calls an "equivalence class ... relative to a chosen family
of measurements". A158 did not name the condition.

**What the record's reading of the lemma adds.** [THEORY-032](../theory.d/THEORY-032.md), from the nLab
page ([LIT-221](../literature.d/LIT-221.md), read in [NOTE-195](../notes.d/NOTE-195.md)), sets three conditions on it:

- The profile that identifies an object is the hom-functor *with its action
  by composition*, not a list of hom-sets. Two non-isomorphic objects can
  have hom-sets in bijection for every probe (the ℤ≥0 / ℤ≥1 example). An
  empirical probing profile, a table of outcomes, is of the bare kind. So
  the categorical ideal it is said to approximate is a stronger structure
  than probing records.
- The lemma needs identities. It fails for semicategories.
- The lemma presupposes the objects it identifies. y(c) is indexed by every
  object of the category, and the conclusion is an isomorphism between two
  of them.

**What probe distributions can and cannot certify.** A184 §2: (φ_i)#P = (φ_i)#Q for every i "does not generally
imply" P = Q, and matching each probe's
marginal leaves the joint across probes unconstrained. FID keeps only two
moments of one probe. A181 §5: "a standard Gaussian and a symmetric
distribution supported on {−1,+1} have equal mean and variance", so the
population FID between them is zero. But a rich enough family does separate:
all one-dimensional linear projections determine a distribution
(Cramér–Wold).

## What it does not say

- It does not say a full Yoneda profile exists for communicative acts, or
  that one is observable. Writing 𝒬 ⊆ 𝒞 presupposes a category 𝒞 of
  communicative realizations that nobody has specified. A158's notation
  Hom_C(Q,A) also puts contexts and communicative objects in one category. A
  communicative object is a presheaf on contexts, not an object among them,
  so its restricted profile is its value at each probe.
- It does not say probabilistic fidelity follows from Yoneda. A173: "Avoid
  claiming that probabilistic fidelity follows directly from Yoneda's
  lemma."
- It does not withdraw [CLAIM-046](CLAIM-046.md)'s methodological rule. Evidence still comes
  from observable responses. What changes is what that evidence is *of*.
- A data matrix of probe outcomes is a table of hom-set-like entries without
  composition. Even a complete one is not a Yoneda profile. The exact theorem
  for counts from probes is Lovász's (1967), noted in [THEORY-032](../theory.d/THEORY-032.md) and
  [NOTE-195](../notes.d/NOTE-195.md): finite relational structures are isomorphic exactly when they
  have the same homomorphism counts from every finite structure.
- It says nothing about contextuality. A158 §4: "Yoneda does **not** say that
  every empirical presheaf is representable. Indeed, a contextual empirical
  model may be precisely the sort of structured collection for which no
  globally admissible realization exists." Being representable and having a
  global section are independent. On the poset of subsets of a set X, the
  representable y(U) for U ≠ X has no global section. The event presheaf
  U ↦ O^U is not representable in general, yet it always has global
  sections. Contextuality is a failure of the empirically constrained local
  data, supports or distributions, to extend from the cover to a global
  realization ([CLAIM-038](CLAIM-038.md)), not a failure of representability. Applied
  to the event presheaf, the lemma restates the definition of a
  communicative object ([TERM-002](../terms.d/TERM-002.md), now superseded by
  [TERM-042](../terms.d/TERM-042.md)) and adds no constraint of its own.
- It says nothing about which probes to select. That is [CLAIM-050](CLAIM-050.md)'s
  question, and [QUESTION-031](../questions.d/QUESTION-031.md) asks when a family is rich enough.
