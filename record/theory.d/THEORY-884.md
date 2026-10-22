---
number: 884
status: Proposed
formerly:
- THEORY-tmp7q3ne
promote_when: >-
  A second check that ties the result to the classical theorem rather than
  to this unreviewed web paper alone: a reading of Moore (1956) or Nerode
  (1958), or a standard automata text, that identifies Proposition 4 as the
  minimal-machine (Myhill–Nerode, Moore partition-refinement) construction
  applied to the target family {T_d ∘ J_u}, with its hypotheses (finite
  state set closed under total deterministic revisions, a state that
  includes any law needed to make revision Markovian). It is refuted by a
  finite counterexample: a representation one of whose fibres meets two
  ≈-classes and that still admits updates and decoders reproducing every
  target after every revision word, or a system that needs more than
  K* − K added revision words to separate its classes. Empirical results
  about agents cannot settle it either way; it is a statement about
  representations, not about what any reader does with them.
title: 'A retained state supports exact answers to a declared family of questions after every finite sequence of a declared family of total deterministic revisions exactly when each of its fibres lies within one class of the coarsest revision-invariant refinement of agreement on current answers; that refinement can be strictly finer than what present answers require, and at most K* − K revision sequences, beyond the current answers, are needed to tell its K* classes apart'
version: 1
tags:
- information-theory
- epistemology
date: '2026-10-22'
source:
- LIT-1376
answers:
- QUESTION-112
summary: >-
  Aevyra (2026), The Ledger of Will, [LIT-1376](../literature.d/LIT-1376.md), read in full in
  [NOTE-1091](../notes.d/NOTE-1091.md): Proposition 4, "revision closure", with its proof in §4.4
  and finite checks in Appendix A.9. The authors call it "a
  finite-machine refinement construction in the tradition of Moore and
  Nerode", not a new theorem. It answers [QUESTION-112](../questions.d/QUESTION-112.md) in one case only: a
  finite family of total deterministic revisions declared in advance. It
  does not say how to choose the family, which is that question's hard
  part, and it is not an efficient construction.
---
<!-- inactive-ok-file: CLAIM-295 CLAIM-303 — Proposed; the claims this account bears on, named, not leaned on -->

# THEORY-884: A retained state supports exact answers to a declared family of questions after every finite sequence of a declared family of total deterministic revisions exactly when each of its fibres lies within one class of the coarsest revision-invariant refinement of agreement on current answers; that refinement can be strictly finer than what present answers require, and at most K* − K revision sequences, beyond the current answers, are needed to tell its K* classes apart

## Source

Aevyra (2026), [LIT-1376](../literature.d/LIT-1376.md), read in full in [NOTE-1091](../notes.d/NOTE-1091.md) from the
version 4.0 web page of 25 September 2026: §4.4 (Proposition 4 and its
proof), with §4.1–4.3 for the definitions and §5.1 and Appendix A.9 for the
examples. The archive's checks were run and reproduce the saved results.

## What was actually shown

Setting: a finite nonempty set H of states (histories, with any current law
or status needed to make revision Markovian), closed under a finite family
of total deterministic revisions J_z, z ∈ Z; a family D of targets T_d; a
deterministic reduction ρ. For a word u = z₁…z_k, J_u applies the
revisions in order.

- **The relation.** h ≈ h′ when T_d(J_u h) = T_d(J_u h′) for every d ∈ D
  and every word u, including the empty one. It is the coarsest
  equivalence that refines agreement on current targets (∼_D) and is
  invariant under every J_z.
- **The criterion.** ρ admits updates Ĵ_z on its image and decoders g_d
  with g_d(Ĵ_u(ρ(h))) = T_d(J_u h) for all h, d, u if and only if every
  fibre of ρ lies within one ≈-class. Necessity: equal retained states
  give equal decoded outputs after any word. Sufficiency: fix a
  representative of each fibre and update through it; invariance keeps the
  representative ≈-equivalent to the true revised state.
- **The bound.** With K classes of ∼_D and K* of ≈, K* ≥ K, and the
  current targets plus at most K* − K added nonempty revision words
  distinguish all K* classes: each added word splits at least one block,
  and every split respects ≈.
- **Strictness, by example.** In the paper's four-state extension of §5.1
  (two histories × a law index that one revision sets to 1), the current
  best action gives K = 2 and the revisions give K* = 3, with the one
  revision as the added witness. A state that keeps only today's answer
  merges two histories that the next change of evaluative law separates.
- **Update is weaker than representation.** Exact outputs do not give the
  identity Ĵ_z ∘ ρ = ρ ∘ J_z; that holds only when ρ's own fibres are
  invariant. A.9 gives a three-state case where every future target is
  recoverable and that identity fails.

The proof was checked on reading, and the archive's exhaustive check of all
5,832 three-state, two-revision, binary-target systems and 3,000 seeded
systems, against an independent pair-distinguishability closure, was rerun
and agrees. A different result could have come out of these checks; none
did.

## What this does not say

- **Not new mathematics.** It is Moore–Nerode refinement applied to the
  expanded family {T_d ∘ J_u}, and the authors say so. Its interest to the
  record is that it states [QUESTION-112](../questions.d/QUESTION-112.md)'s sufficiency under changing
  families exactly, for the case where the family of changes is fixed in
  advance.
- **Not a rule for choosing the revision family.** "efficient selection
  for open-ended agents remains unresolved" (§4.4). For an inquiry whose
  questions change in response to what it finds, which is what
  [QUESTION-112](../questions.d/QUESTION-112.md) asks about, it gives the form of an answer, not the answer.
- **Not a size or cost bound.** "it is not a token, runtime, or optimal
  storage bound" (§4.4). K* − K counts test words.
- **Not about partial revisions, non-Markovian laws or infinite
  histories.** The paper sets these aside.
- **Not about what a bounded reader does.** Sufficiency is information
  available, not information used; the paper keeps "Information
  availability and computational accessibility" apart (§5.2), as
  [CLAIM-295](../claims.d/CLAIM-295.md) does.
- **Not an argument that history should be kept.** It says what must be
  kept for a declared family. Whether keeping it pays is [CLAIM-295](../claims.d/CLAIM-295.md) and
  [CLAIM-303](../claims.d/CLAIM-303.md).

## Connections

- **[QUESTION-112](../questions.d/QUESTION-112.md).** Answers it in part, as above.
- **[CLAIM-350](../claims.d/CLAIM-350.md).** The one-step case: Proposition 2, exact sufficiency iff
  the targets are constant on the fibres, is [CLAIM-350](../claims.d/CLAIM-350.md). This is that
  criterion closed under revision.
- **[CLAIM-294](../claims.d/CLAIM-294.md), [CLAIM-300](../claims.d/CLAIM-300.md).** [CLAIM-294](../claims.d/CLAIM-294.md)'s two histories with one marginal and
  different updates are a case where ∼_D is coarser than ≈. [CLAIM-300](../claims.d/CLAIM-300.md) is
  the K* = K case: a state sufficient for a fixed family needs nothing
  more for it.
- **[CLAIM-295](../claims.d/CLAIM-295.md).** The "wider family of decisions for which what is kept
  suffices" is, for a declared revision family, the move from ∼_D to ≈.
- **[TERM-067](../terms.d/TERM-067.md), [CLAIM-407](../claims.d/CLAIM-407.md).** The same factorization criterion with a
  different target family (responses to interventions on governance). An
  analogous closure for sequences of governance interventions is not
  shown here.
