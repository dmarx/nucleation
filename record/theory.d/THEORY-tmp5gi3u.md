---
status: Active
title: 'The dynamics a coupled cell network admits, restricted to a robustly synchronous pattern, are dynamics admitted by a smaller quotient network whose cells are the synchronized classes, so behaviour of the quotient, including symmetric behaviour the original network has no symmetry to force, appears in the original as synchronous behaviour; the quotient admits more dynamics than restriction produces, and is unique only up to refinement of its arrow types'
version: 1
tags:
- network-science
- mathematics
date: '2026-10-27'
source:
- LIT-tmpwhycq
summary: >-
  Stewart, Golubitsky and Pivato (2003), [LIT-tmpwhycq](../literature.d/LIT-tmpwhycq.md), read in
  [NOTE-tmp4riih](../notes.d/NOTE-tmp4riih.md): the quotient construction (§7), Theorems 8.3, 8.4 and 9.2
  with proofs, the counterexample of Remark 7.5 and Example 7.1. Active as
  mathematics. The quotient describes the dynamics on the invariant
  subspace exactly, but only a subclass of the quotient's own admissible
  dynamics arises that way, and nothing is said about stability
  transverse to the subspace.
---

# THEORY-tmp5gi3u: The dynamics a coupled cell network admits, restricted to a robustly synchronous pattern, are dynamics admitted by a smaller quotient network whose cells are the synchronized classes, so behaviour of the quotient, including symmetric behaviour the original network has no symmetry to force, appears in the original as synchronous behaviour; the quotient admits more dynamics than restriction produces, and is unique only up to refinement of its arrow types

## Source

Stewart, Golubitsky and Pivato (2003), [LIT-tmpwhycq](../literature.d/LIT-tmpwhycq.md), §§7–9 (pp. 632–644 of
SIAM J. Appl. Dyn. Syst. 2(4), read from the accepted version); read in
[NOTE-tmp4riih](../notes.d/NOTE-tmp4riih.md). It rests on the balanced relations of [THEORY-tmpbgffi](THEORY-tmpbgffi.md).

## What was actually shown

**The quotient.** For a balanced relation ⋈, the natural quotient network
has the ⋈-classes as cells, the projections of arrows not joining two
distinct equivalent cells as arrows, and two arrows of the same type when an
input isomorphism carries the cells of one colour onto those of the other
(construction (A)–(F) and eqs. 7.3–7.4, pp. 634–636; Lemma 7.3). It is a
quotient map in the sense of Definition 8.1 (Theorem 8.3, p. 639), and any
quotient map induces a balanced relation (Lemma 8.2(c), p. 638), so
quotients and balanced relations are the same patterns seen two ways.

**The theorem.** "For any f ∈ F_{G₁}^P, the induced vector field f̄ lies in
F_{G₂}^P̄" (Theorem 9.2, p. 642): restricting an admissible field to the
polydiagonal and reading it in the quotient's coordinates (eq. 9.3) gives a
field admissible for the quotient. Hence "interesting dynamics (rotating
waves, symmetric chaos) in this subspace for the cell system G₂ corresponds
to the same dynamics in the cell system G₁, in which ⋈-equivalent cells are
synchronous" (p. 642).

**Symmetry in the quotient only.** The five-cell network of Example 7.1
restricts on {(x, y, x, y, z)} to ẋ = f(x, y, z), ẏ = f(y, z, x),
ż = f(z, x, y) (eq. 7.2), the general D₃-equivariant field: "So it is
possible for a quotient network to have symmetry even when the original
network has none" (p. 633). The three-cell master–slave network of Figure 19
has a quotient with Z₂ symmetry (p. 635), and the seven-cell chain with a
back connection has the three-cell ring as quotient, so the ring's rotating
wave is a travelling wave of the chain (eqs. 1.8–1.9, Figure 8,
pp. 614–615).

**What could have come out otherwise, and did.** The quotient's admissible
class is larger than the restrictions: in the four-cell network of Figure
20, restricted fields have linear terms αu₁ + β(u₂ + 2u₃) where a general
quotient field has αu₁ + βu₂ + γu₃, so "vector fields that are admissible
with respect to the quotient network G_⋈ do not always lift" (Remark 7.5,
pp. 637–638), "a groupoid analogue of hidden symmetry". And quotients with
the same relation need not be isomorphic (Example 8.5, Figure 21); the
natural one is universal, every other factoring through it (Theorem 8.4,
p. 639) as an edge-refinement (Corollary 8.8, p. 641).

## What this does not say

- **That a quotient solution is stable in the original network.** The
  quotient describes motion within the synchronous subspace. Stability
  transverse to it, which decides whether the synchrony is seen, is not
  treated; the paper studies "existence, not stability" (p. 626).
- **That every generic behaviour of the quotient occurs.** Restriction
  yields a subclass of the quotient's admissible fields (Remark 7.5), and
  φ̂ "is never surjective when φ is not the natural quotient map" (p. 644).
  The full criterion for lifting is deferred to Dias and Stewart (ref. [5]),
  unread.
- **That the quotient is a coarse-graining of every state.** It describes
  only states in the synchronous subspace; off it the original network's
  dynamics are not reduced.
- **That the symmetric dynamics are proved here.** Rotating waves,
  multirhythms and symmetric chaos in the examples are shown by simulation
  (Figures 8, 16–18) and by citing symmetric Hopf bifurcation and the H/K
  theorem from the authors' earlier work.
