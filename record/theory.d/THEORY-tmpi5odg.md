---
status: Active
title: "Aerts and Gabora's founding quantum model of concepts is a classical probability model written in a Hilbert space: every context it uses is a projector diagonal in one basis, so the contexts commute and generate a Boolean algebra, its entangled 'pet fish' state gives the same statistics as a classically correlated mixture for every context in the model, and its guppy weights are copied from single-concept ratings rather than predicted for the conjunction"
version: 1
tags:
- cognition
- quantum-foundations
- probabilistic-modeling
date: '2026-10-16'
source:
- LIT-312
- LIT-340
summary: >-
  Aerts & Gabora (2005), Parts II and I, [LIT-312](../literature.d/LIT-312.md) and [LIT-340](../literature.d/LIT-340.md), read in
  [NOTE-299](../notes.d/NOTE-299.md) and [NOTE-294](../notes.d/NOTE-294.md). The structural facts are checks of the published
  model, not of the authors' prose: contexts are sums of basis projectors,
  counts are chosen to match rounded frequencies, and the authors call the
  result a "quantization" of a set-theoretical model. Part I's mark of
  non-classicality (eq. 19) is met by Boolean projection lattices too, and
  its lattice structure is supposed, not derived. The model as printed is
  also infeasible in two cells. It does not say that no quantum model of
  concepts does better.
supports:
- CLAIM-041
---
<!-- inactive-ok-file: LIT-270 — Rejected; named as the later programme whose error this account traces, not as support -->
<!-- inactive-ok-file: THEORY-013 THEORY-017 THEORY-255 — Proposed; named as related or rival accounts in Connections and prose, not leaned on as settled -->

# THEORY-tmpi5odg: Aerts and Gabora's founding quantum model of concepts is a classical probability model written in a Hilbert space: every context it uses is a projector diagonal in one basis, so the contexts commute and generate a Boolean algebra, its entangled 'pet fish' state gives the same statistics as a classically correlated mixture for every context in the model, and its guppy weights are copied from single-concept ratings rather than predicted for the conjunction

## Source

- Aerts & Gabora (2005), *A theory of concepts and their combinations II:
  A Hilbert space representation*, [LIT-312](../literature.d/LIT-312.md), read in full in [NOTE-299](../notes.d/NOTE-299.md).
- Aerts & Gabora (2005), *A theory of concepts and their combinations I:
  The structure of the sets of contexts and properties*, [LIT-340](../literature.d/LIT-340.md), read in
  full in [NOTE-294](../notes.d/NOTE-294.md). Both appeared on arXiv on 26 February 2004.

## What was actually shown

**Part I's data and structure.** Eighty-one convenience subjects rated 14
exemplars and 14 properties of "pet" under seven contexts. The shifts are
large: dog goes from 0.12 under the unit context to 0.50 under "chewing a
bone"; goldfish from 0.10 to 0.48 under "is a fish" (Tables 1–5). Part I
then proposes that contexts and properties each form a complete
orthocomplemented lattice. Completeness is supposed ("We suppose", §3.2),
and the orthocomplement is stated by axioms and illustrated by negated
sentences. Its one mark of non-classicality is eq. 19: the eigenstates of a
join can exceed the union of the joined contexts' eigenstates.

**Part II's model.** Each of 1,400 "basic contexts" for "pet" (408 for
"fish") is an orthonormal basis vector, the ground state is their uniform
superposition, and each context is the projector onto a set of basis
vectors (eqs. 25, 30, 36, 43, 60). The counts n(E_i) and n(X_ij) are chosen
so that their ratios match the rounded frequencies (§3.1). Every Born
probability is then a ratio of counts, for example µ(goldfish | e6) =
48/100. The authors say the count table "corresponds more or less to a set
theoretical model of the experimental data, such that the Hilbert space
model can considered to be a quantization … of this set theoretical
model".

**The checks the readings made.** [NOTE-299](../notes.d/NOTE-299.md) and [NOTE-294](../notes.d/NOTE-294.md) establish four
facts about the model as published.

1. *Commutative.* Every projector used is diagonal in the basis B, so all
   contexts commute and generate a Boolean algebra. No incompatible context,
   order effect or interference term occurs.
2. *Entanglement idle.* The "pet fish" state Σ_u |u⟩⊗|u⟩/√100 (eq. 78) is
   used only with projectors diagonal in B⊗B. For all of them it gives the
   same statistics as the separable mixture Σ_u |u⟩⟨u|⊗|u⟩⟨u|/100.
3. *Part I's criterion is not a test.* In any Hilbert space a family of
   commuting projectors generates a Boolean lattice, yet the eigenstates of
   P ∨ Q strictly exceed those of P and Q together. So eq. 19 cannot certify
   a non-Boolean logic of concepts.
4. *Guppy imported.* The guppy and goldfish weights in the compound, 0.46
   and 0.48, are Part I's ratings of "pet" under "The pet is a fish". No
   typicality for the conjunction "pet fish" was measured, and the authors
   write of the single-concept version "Of course this is not the real
   guppy effect" (§5).

**Two cells of the model are infeasible.** n(X_ij) must not exceed n(E_i).
Table 2 has 126 for parrot under e5 where n(E₁₇) = 98, and Table 5 has 39
for guppy where m(E₄₂) = 32. As printed neither model exists. [NOTE-299](../notes.d/NOTE-299.md)
judges this a bookkeeping error, since the parrot row can be repaired.

**What could have come out otherwise.** The model could have used
incompatible contexts, so that entangled and classically correlated states
gave different predictions, or it could have predicted conjunction
typicality out of sample. It does neither, so its fit could not have
failed.

## What this does not say

- **That quantum models of concepts are classical.** This is about the
  2005 model. Aerts (2009) puts non-commuting subspaces to work on
  Hampton's membership data, for the k-type items ([THEORY-255](THEORY-255.md)).
- **That the data show nothing.** Context shifts the ratings of single
  exemplars and properties, and that is the experiment's finding. Part I's
  Table 5 has three p-values above 1 and four duplicated columns, and the
  full analysis is unpublished, so the significance claims cannot be
  checked from the paper.
- **That the proposal is empty.** Concepts as states changed by contexts,
  contexts as projectors, and the tensor product for combination are owned
  here, and Part II proposes tensor-product sentence meaning in 2004,
  before DisCoCat. They are proposals; the paper does not demonstrate them.
- **That the Hilbert model reproduces property weights.** Part II's §5 says
  it does; no property projector is ever built.
- **Anything about contextuality.** "Contextual" in these papers means that
  the state changes with context, which shows up as shifting marginals. It
  is not Kochen–Specker contextuality, and the papers do not claim it.

## Connections

- **Contextuality-by-Default.** Every effect in Part I's data is a
  context-dependent marginal, which [THEORY-013](THEORY-013.md) separates from
  contextuality. The programme's later CHSH claims ([LIT-270](../literature.d/LIT-270.md), Rejected) rest
  on the same confusion.
- **[CLAIM-041](../claims.d/CLAIM-041.md)** grounds its claim that a Hilbert-space representation alone
  does not establish non-classicality partly on [LIT-312](../literature.d/LIT-312.md)'s diagonal
  projectors; this account states that ground.
- **The later model.** [THEORY-255](THEORY-255.md) shows that in Aerts's 2009 subspace model
  meet and join cannot produce the guppy-type deviations, and that the
  non-commuting structure is confined to the k-type items.
- **Lattices.** [THEORY-041](THEORY-041.md) records what Birkhoff and von Neumann's modular
  law was; Part I never reaches modularity or orthomodularity.
- **DisCoCat.** The maximally correlated sentence state Σ|u⟩⊗|u⟩⊗|u⟩ is the
  image of the copy map of the basis, the Frobenius structure behind
  [THEORY-017](THEORY-017.md) and [LIT-272](../literature.d/LIT-272.md). The connection is [NOTE-299](../notes.d/NOTE-299.md)'s, not the paper's.
