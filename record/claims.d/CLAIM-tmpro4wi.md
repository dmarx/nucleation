---
status: Active
title: 'A matrix factorization is identified only up to an invertible change of latent coordinates, which weight decay narrows to rotations and nonnegativity to rescalings and permutations plus a data-dependent remainder; such a gauge is not a symmetry of the relational system, and automorphisms of the data act on the factors only when the factorization is identifiable'
version: 1
role: granted
tags:
- mathematics
- representation-learning
date: '2026-10-10'
line: 'pragmatic-transport'
grounds:
- THEORY-004
- THEORY-017
- THEORY-180
- LIT-304
complements:
- CLAIM-tmp3sn40
- CLAIM-113
summary: >-
  Drawn by the assistant at A207 §3, made explicit at A214 §6 and kept in
  A218 (§4.2, Ch5.4–5.9). Granted, because it is elementary, and the
  record already held its mathematics. The record adds the full list of
  invariants, the data-dependent freedom of nonnegative factorization,
  and why identifiability must come before automorphisms and characters.
  It does not say latent axes are meaningless, or that observed data have
  non-trivial automorphisms.
illustrated_by:
- CASE-tmptm6yt
---
<!-- inactive-ok-file: THEORY-004 THEORY-017 THEORY-180 — Proposed; cited as readings the claim stands on, not as settled -->
<!-- inactive-ok-file: CLAIM-113 — Proposed; open, and cited as the claim whose automorphism direction this one supplies -->

# CLAIM-tmpro4wi: A matrix factorization is identified only up to an invertible change of latent coordinates, which weight decay narrows to rotations and nonnegativity to rescalings and permutations plus a data-dependent remainder; such a gauge is not a symmetry of the relational system, and automorphisms of the data act on the factors only when the factorization is identifiable

## The claim

For a factorization R ≈ PQᵀ, the change P ↦ PA, Q ↦ QA⁻ᵀ leaves PQᵀ
unchanged for every invertible A. A207 §1: "Thus an entire family of
distinct latent-coordinate systems predicts exactly the same relationship
matrix." This freedom is the factorization's gauge. The record already
held it in two forms. Park, Choe and Veitch's Theorem 3.4 ([LIT-304](../literature.d/LIT-304.md)) is the
same transformation for a softmax model, γ ↦ Aγ, λ ↦ A⁻ᵀλ, and so leaves
no inner product identified. A kernel fixes a representation only up to an
orthogonal map ([THEORY-004](../theory.d/THEORY-004.md)).

What the gauge leaves invariant is the predicted matrix and everything
computed from it:

- its rank and singular values (A207 §3's table);
- its column and row spaces, since span(PA) = span(P);
- the item kernel of the predicted matrix, R̂ᵀR̂ = Q(PᵀP)Qᵀ.

The latent Gram matrix QQᵀ is not invariant: it becomes QA⁻ᵀA⁻¹Qᵀ. Nor are
latent cosines, or any reading of an axis. So the similarity of two items
is gauge-invariant when it is computed from their response profiles, as in
A207's hypothesis Similarity(R_·i, R_·j). It is not invariant when it is
computed from their latent vectors. A207's table does not warn of this,
and a relational signature built from latent item vectors would fail it.

Weight decay narrows the gauge without removing it. A207 §1: "orthogonal
changes still preserve both predictions and the usual squared-norm
penalty." The minimum of (‖U‖²_F + ‖V‖²_F)/2 over UVᵀ = M is the nuclear
norm ‖M‖_* ([THEORY-180](../theory.d/THEORY-180.md)). Its minimizers are the balanced factorizations
U = U_M Σ^½ R and V = V_M Σ^½ R with R orthogonal. The penalty therefore
fixes the gauge up to O(k), and it fixes latent inner products to
V_M Σ V_Mᵀ. That value is chosen by the penalty, not by the ratings.

R9's reader checked this numerically on random 6×2 and 5×2 factors. The
predicted matrix and Q(PᵀP)Qᵀ were unchanged under a random invertible A,
and QQᵀ changed. The Frobenius penalty was unchanged under a random
orthogonal A and rose from 17.0 to 73.1 under the general A.

## Nonnegative factorization

A210 §2 says NMF has "a simpler form of the gauge freedom": for any
positive diagonal D, WH = (WD)(D⁻¹H), and topics may be permuted. A214 §6
says the same: "Positive diagonal rescalings and topic permutations remain
standard ambiguities, with additional nonuniqueness possible."

Scaled permutations are the freedom every nonnegative factorization always
has. The full freedom for a given (W, H) is the set

{A invertible : WA ≥ 0 and A⁻¹H ≥ 0}.

That set depends on the data, is not a group in general, and can be much
larger than the scaled permutations, because A itself need not be
nonnegative. Nonnegativity reduces the freedom. It does not simplify it.

A worked case. Take W = [[1, .5], [.5, 1], [1, 1]] and H = [[1, .6, .3],
[.3, .6, 1]], and A = [[1.2, −.2], [−.2, 1.2]]. Then WA = [[1.1, .4], [.4,
1.1], [1, 1]] and A⁻¹H = [[.9, .6, .4], [.4, .6, .9]]. Both are
nonnegative, and they give the same X = WH. A is not a rescaling or a
permutation. In this example no word belongs to one topic alone and no
document to one topic alone, which is the condition the uniqueness
theorems exclude (separability, anchor words). This is [THEORY-017](../theory.d/THEORY-017.md)'s point in
a new place: the parts are fixed by structure supplied from outside, here
nonnegativity in the vocabulary's own basis plus a condition on the data.

## Gauge is not automorphism

A207 §3: "Ordinary matrix factorization has a *gauge symmetry*, not
necessarily a group representation whose character classifies the
objects." A214 §6: "A factorization gauge transformation can leave every
predicted observation unchanged without corresponding to any real-world
transformation of the communicative situation. A structural automorphism
must preserve the specified relational system itself." A218 Ch5.9 keeps it
as a chapter item: "Structural automorphisms versus latent-coordinate
gauge."

A gauge change alters the description and leaves the relata where they
are. An automorphism moves relata among structurally equivalent positions.
Characters are invariants of the second kind ([CLAIM-tmp3sn40](CLAIM-tmp3sn40.md)), not of the
first. The gauge group GL(k), or O(k) under weight decay, leaves every
observable fixed, so its characters carry no information about which item
is which.

## Why the arrows run in this order

A214 §6 boxes a progression, here transcribed from the display: "Observed relationships → Identifiable latent
model → Structural automorphisms → Transformation representation →
Character", and says "None of those arrows is automatic." It says only that
gauge and automorphism "can interact". The interaction is exact.

An automorphism of the data is a pair of permutations (P, Q) of documents
and words with PXQ = X. It sends a factorization (W, H) to (PW, HQ), which
is another factorization of X. If the factorization is essentially unique,
that is unique up to scaled permutations, then (PW, HQ) = (WDΠ, Π⁻¹D⁻¹H)
for a unique permutation Π of the topics. So the automorphism group acts on
the topics, and that action is a permutation representation, with
character χ(g) = the number of topics g fixes. Without identifiability the
induced action is defined only up to the gauge, and no representation on
the factor space is determined. The order of A214's arrows is a dependency,
not only a sequence. It is the Aut(F) direction of [CLAIM-113](CLAIM-113.md), which did
not reach the manuscript.

## What it does not say

- It does not say latent axes are meaningless. Constraints that break the
  gauge, such as nonnegativity under separability, can identify them.
- It does not say the invariant quantities are the communicative kind.
  They are what the data and the rank-k model determine.
- It does not say observed data have non-trivial automorphisms. Exact
  permutation symmetries PXQ = X almost never hold in a noisy real-valued
  matrix. A214 §6 lists "its automorphism group may be trivial" as one
  possible failure. For measured data it is the generic case. Literal
  characters then need designed symmetries, stipulated equivalences
  between realizations, or approximate automorphisms with a tolerance. The
  second is a new definition, not a theorem of character theory.
- It does not say gauge freedom is unimportant. It is the record's cleanest
  case of a representation without identity.
