---
number: 486
status: Proposed
formerly:
- THEORY-tmpathbk
promote_when: >-
  A refereed version of the paper, or an independent check by a Floer
  theorist, of the two analytic steps it rests on: convergence of
  pseudo-holomorphic strips to D₄⁻-trees in the adiabatic limit (§4,
  Propositions 4.3 and 4.13, with the cited parts of Ekholm 2007 and the
  second author's 2024 preprint) and Gromov compactness and transversality
  for the deformed continuation strips (§5). Theorem statements narrowed
  to the hypotheses the proofs use (exact, finite, creative networks) would
  be part of it. A gap found in either step would refute the account as
  stated. More worked examples, and figures matching flowlines to
  augmentation terms, cannot settle it.
title: "For exact Betti Lagrangians in the cotangent bundle of a punctured surface, a finite creative spectral network exists, a point lies on its active walls exactly when a pseudo-holomorphic strip survives the adiabatic limit, and the Family Floer functor equals Gaiotto–Moore–Neitzke non-abelianization there"
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-017
summary: >-
  Casals & Nho (2025), [LIT-017](../literature.d/LIT-017.md), an unrefereed v1 preprint read in full in
  [NOTE-022](../notes.d/NOTE-022.md) by a reader who is not a Floer theorist. Theorems 1–3 are
  stated for any rank and for positive-braid asymptotics. The proofs cover
  exact Betti Lagrangians with finite creative networks; the meromorphic
  case adds hypotheses in prose, and the Family Floer functor is not built
  there. The analytic core is taken by citation from Ekholm 2007, which
  the authors patch, and from the second author's own preprint. Theorem 5,
  on networks from Demazure weaves, has no written proof and is not part
  of this account.
---

<!-- inactive-ok-file: LIT-017 — Proposed; the account is filed Proposed for the same reason the reading placed the paper there -->

# THEORY-486: For exact Betti Lagrangians in the cotangent bundle of a punctured surface, a finite creative spectral network exists, a point lies on its active walls exactly when a pseudo-holomorphic strip survives the adiabatic limit, and the Family Floer functor equals Gaiotto–Moore–Neitzke non-abelianization there

## Source

Casals & Nho (2025), "Spectral Networks and Betti Lagrangians",
arXiv:2504.08144v1, [LIT-017](../literature.d/LIT-017.md), read in full in [NOTE-022](../notes.d/NOTE-022.md). The reader is not a
Floer-theory specialist, and [NOTE-022](../notes.d/NOTE-022.md)'s Limitations mark what could and
could not be checked.

## What was actually shown

**The setting.** A Betti surface S is a punctured closed surface with a
Legendrian positive-braid link at each puncture. A Betti Lagrangian is a
Lagrangian n-fold branched cover of S inside T*S with those asymptotics,
locally the D₄⁻ germ at each branch point (Definitions 2.3, 2.6–2.7). The
account concerns class (i), the exact ones with conical ends.

**Existence (Theorem 1(i)).** Every exact Betti Lagrangian with an adapted
metric admits a finite Morse spectral network, and the proof produces one
with creation vertices only. Gappedness comes from an energy bound on
chain-interaction trees (Propositions 3.17–3.18); finiteness comes from
exactness. [NOTE-022](../notes.d/NOTE-022.md) rates this moderate to strong (C1).

**Floer characterisation (Theorem 2).** p lies on an active wall iff a
broken pseudo-holomorphic strip between T*_pS and the Lagrangian exists in
the adiabatic limit; for exact Lagrangians the strip is unbroken. The "⇐"
direction rests on Proposition 4.3, which gives convergence only to
*trimmed* D₄⁻-trees (footnote 13). The "⇒" direction in the exact case uses
creativity of the network (§5.4.1).

**Family Floer equals non-abelianization (Theorem 3 = Theorem 5.24).** For
exact L, the Family Floer functor is well defined, invariant under compactly
supported Hamiltonian isotopy, and in the adiabatic limit equal to GMN's
non-abelianization Φ_W. Its proof assumes a finite creative network, which
Theorem 1(i) supplies (C5, moderate). Theorem 4 realises Φ_W in the
A∞-operations of wrapped and partially wrapped Fukaya categories of T*S.

**What could have come out otherwise.** A strip could have survived the
limit off the network, or the continuation-strip count could have differed
from GMN's detour rule. The paper's arguments say neither happens; the
non-specialist reader could check the combinatorics and elementary
flowline analysis, not the analytic convergence.

## What this does not say

- **That the theorems hold as broadly as they are stated.** Theorem 3 says
  "a spectral network compatible with Σ" but is proved for finite creative
  networks. The meromorphic (WKB) case of Theorem 2 adds a hypothesis in
  prose, and Remark 5.10 says the functor is not constructed there.
- **That the analysis has been checked.** §§4–5 take their technical steps
  from Ekholm 2007, which has a gap the authors patch in Appendix A
  (Theorem A.3), and from the second author's 2024 preprint, cited for
  about ten lemmas. The paper was unrefereed when read.
- **That spectral networks come from Demazure weaves.** Theorem 5 is
  "implied" by Proposition 7.5, which has a one-sentence justification. The
  Berk–Nevins–Roberts match is a comparison of figures (C9–C10).
- **That non-abelianization is injective on objects.** That GMN conjecture
  is argued in two sentences inside a section whose main diagram is itself
  conjectural (C11).
- **Anything about physics beyond the dictionary.** BPS states and WKB enter
  as names for D₄⁻-trees and the meromorphic case. No physical prediction is
  derived.

## Connections

- The record has no technical neighbour. [LIT-011](../literature.d/LIT-011.md) shares the word
  "spectral" and no mathematics.
