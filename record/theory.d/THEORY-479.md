---
number: 479
status: Active
formerly:
- THEORY-tmpa30ou
title: "Shannon's chain rule is the 1-cocycle equation of a cohomology of finite probability spaces whose action is averaged conditioning, and on connected, sufficiently rich structures of partitions every measurable 1-cocycle is a constant multiple of Shannon entropy, with no symmetry or continuity axiom assumed; in the unitary-invariant quantum version the first cohomology vanishes and von Neumann entropy is the 0-cochain whose coboundary is minus Shannon entropy"
version: 1
tags:
- information-theory
- mathematics
- quantum-foundations
date: '2026-10-16'
source:
- LIT-053
summary: >-
  Baudot & Bennequin (2015), [LIT-053](../literature.d/LIT-053.md), read in [NOTE-088](../notes.d/NOTE-088.md). Theorems 1 and 3
  are proved for finite spaces, through the Tverberg–Kendall–Lee result on
  measurable solutions of the fundamental equation of information. The
  hypotheses are stated three different ways in the paper; Theorem 1's
  is operative. The higher mutual informations appear as coboundaries,
  and Theorems B, D and F and the synergy reading are sketched or
  deferred to companion papers, so they are not part of this account.
---

# THEORY-479: Shannon's chain rule is the 1-cocycle equation of a cohomology of finite probability spaces whose action is averaged conditioning, and on connected, sufficiently rich structures of partitions every measurable 1-cocycle is a constant multiple of Shannon entropy, with no symmetry or continuity axiom assumed; in the unitary-invariant quantum version the first cohomology vanishes and von Neumann entropy is the 0-cochain whose coboundary is minus Shannon entropy

## Source

Baudot & Bennequin (2015), "The Homological Nature of Entropy",
*Entropy* 17, [LIT-053](../literature.d/LIT-053.md), read in [NOTE-088](../notes.d/NOTE-088.md).

## What was actually shown

**The complex.** On a finite Ω, an information structure S is a set of
partitions containing the trivial one and closed under joins of
partitions with a common refinement in S. A partition Y acts on
functions of P by averaged conditioning, Y.F(P) = Σ_j P(Y=y_j)
F(P|Y=y_j). The bar complex of this action has the 1-cocycle equation
f((Y,Y′);P) = f(Y;P) + Y.f(Y′;P), which is the chain rule.

**Theorem 1.** If S is connected and every element lies on a rich edge
(X, Y with at least two values each, XY cutting them into at least four
pieces), Q is complete, and cochains are measurable, then H¹(S;Q) is one
dimensional and spanned by Shannon entropy. Because H⁰ consists of
constants, there are no non-trivial 1-coboundaries, so H¹ = Z¹: every
measurable 1-cocycle equals C·H, one constant per connected component.
The proof reduces to Tverberg's functional equation on Ω = {00, 01, 10,
11} (Lemma 2).

**Theorem 3 (quantum).** For unitary-invariant, connected, sufficiently
rich S with the canonical density functor, H¹_U = 0. Shannon entropy of a
decomposition is still a cocycle, but δ̂(S_X)(Y;ρ) = −H_X(Y;ρ): it is the
coboundary of minus the von Neumann entropy, which is the unique
invariant 0-cochain with that property up to an additive constant. The
proof's step IV rests on a two-sentence lemma (Lemma 7).

**Also proved.** KL divergence of image laws is a 1-cocycle for pairs of
laws (Prop. 4), and entropy satisfies the finer, operadic chain rule of
Faddeev and Baez–Fritz–Leinster (Prop. 8).

What could have come out otherwise: other measurable functions could have
satisfied the cocycle equation. On rich structures none does.

## What this does not say

- **That the quantum case is "the same".** In degree one it is the
  opposite: classical entropy is a non-trivial class, and in the
  invariant quantum theory it becomes trivial ([NOTE-088](../notes.d/NOTE-088.md), Corrections).
- **That higher mutual informations are cohomology classes.** The paper's
  formulas present them as images of δ or δ_t, coboundaries, and §3 is
  titled "A Sketch". Higher-degree cohomology is not computed.
- **That I₃ < 0 is synergy, or a Borromean linking invariant.** Asserted
  with citations (C6, weak).
- **That KL divergence is unique.** It is shown to be a cocycle, nothing
  more.
- **Anything infinite.** Ω is finite; the infinite case is deferred.
- **That cohomology has been applied to data.** The §1.7 applications are
  others' uses of three-way mutual information, not of the cohomology.

## Connections

- Shannon ([LIT-764](../literature.d/LIT-764.md), [THEORY-602](THEORY-602.md)) says his axiomatic uniqueness
  theorem is "in no way necessary" and that the coding theorems justify
  entropy. This is a second, axiom-light uniqueness result. It does not
  replace the operational justification.
- The interaction information it reads as synergy is, for two sources,
  exactly redundancy minus synergy under any PID ([THEORY-568](THEORY-568.md)).
- Like Abramsky & Brandenburger's sheaf formulation ([LIT-016](../literature.d/LIT-016.md),
  [THEORY-012](THEORY-012.md)), it attaches probability data to a site of commuting
  observables; there the question is gluing, here it is the derived
  cohomology of the conditioning module.
- The anthology's [ANTH-LIT-698](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-698.md) uses this reading by analogy.
