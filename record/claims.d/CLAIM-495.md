---
number: 495
status: Active
formerly:
- CLAIM-tmp3lml8
title: 'For an O(d)-valued connection on a connected graph, the assignments that meet every edge relation xᵢ = Tᵢⱼxⱼ form a space isomorphic to the vectors at one vertex fixed by every holonomy based there, which is the kernel of the connection Laplacian; for d = 1, and for U(1) phases, that space is all or nothing, but for d > 1 a connection whose loops are not trivial can still keep a subspace on which every loop is, so compatibility among local frames can be partial and graded by direction; and edge maps that do not commute can compose to a flat loop, so non-commutativity is not holonomy'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the spanning-tree argument or in the example. The reading,
  that partial compatibility is a distinct organizational possibility,
  is not defeated by the mathematics and is not claimed by it; it is
  defeated for a given system if no measured transports among its parts
  are O(d) with d > 1 in a sense its behaviour bears out.
tags:
- mathematics
- network-science
date: '2026-10-29'
line:
- formal-apparatus
- distributed-agency
grounds:
- THEORY-1082
- THEORY-1140
complements:
- CLAIM-471
summary: >-
  From A2 and A3 of the exchange "Paper assessment" (2026-10-29), which
  drew it out of [LIT-1820](../literature.d/LIT-1820.md)'s O(d) setting against [THEORY-1082](../theory.d/THEORY-1082.md)'s U(1)
  one. The proof and the example are the record's, checked numerically.
  It is the zeroth cohomology of the connection sheaf, so standard, and
  it says nothing about which organizations have such transports.
---

# CLAIM-495: For an O(d)-valued connection on a connected graph, the assignments that meet every edge relation xᵢ = Tᵢⱼxⱼ form a space isomorphic to the vectors at one vertex fixed by every holonomy based there, which is the kernel of the connection Laplacian; for d = 1, and for U(1) phases, that space is all or nothing, but for d > 1 a connection whose loops are not trivial can still keep a subspace on which every loop is, so compatibility among local frames can be partial and graded by direction; and edge maps that do not commute can compose to a flat loop, so non-commutativity is not holonomy

## The claim

Let a connected graph carry Tᵢⱼ ∈ O(d) on each edge, Tⱼᵢ = Tᵢⱼ⁻¹, and call
x = (xᵢ) a global section if xᵢ = Tᵢⱼxⱼ on every edge.

**Sections are fixed vectors.** Fix a base vertex b and a spanning tree.
A section is determined by x_b, since the tree relations carry it to every
vertex. Each non-tree edge closes one fundamental cycle, and its relation
holds exactly when the holonomy H_C of that cycle, based at b, fixes x_b.
The fundamental cycles generate every loop at b. So restriction to b is an
isomorphism from global sections onto ⋂_C Fix(H_C), the vectors fixed by
the whole holonomy group. With energy E(x) = ½Σ‖xᵢ − Tᵢⱼxⱼ‖² = ½⟨x, L_T x⟩
and L_T positive semidefinite, the sections are exactly ker L_T. This is
[THEORY-1082](../theory.d/THEORY-1082.md)'s spanning-tree step, which there needed |xᵢ| constant and
here needs nothing beyond the O(d) relations.

**All or nothing for d = 1.** A phase e^{iθ} acting on ℂ fixes either
everything (θ ≡ 0) or nothing. So in [THEORY-1082](../theory.d/THEORY-1082.md)'s setting a single
nontrivial loop removes every nonzero section.

**Graded for d > 1.** Let every transport on a graph with a triangle
and a square sharing an edge be a rotation of ℝ³ about one common axis, by
angles chosen at random. The holonomies are rotations about that axis by
nonzero angles, with normalized traces 0.295 and 0.815 in one draw. They
are not trivial, yet every one fixes the axis, so the sections are one-
dimensional. A numerical check gave nullity(L_T) = 1 and a common fixed
subspace of dimension 1. Generic O(3) transports on the same graph gave
0 and 0. Compatibility then holds along some directions and fails along
others. A mean of 1 − tr H/d over cycles, the scalar diagnostic, cannot
see which.

**Non-commutativity is not holonomy.** For any A, B ∈ O(d) with AB ≠ BA,
the triangle T₁₂ = A, T₂₃ = B, T₃₁ = (AB)⁻¹ has holonomy I. Order-
sensitive relations can compose flat. [CLAIM-373](CLAIM-373.md)'s bound on carrying
commutators and [LIT-1820](../literature.d/LIT-1820.md)'s holonomy measure different things.

## What it does not say

- **That an organization's parts have O(d) transports among them.** Whether
  any measured relations behave as such is the question [QUESTION-130](../questions.d/QUESTION-130.md) asks
  of evaluative contexts and [QUESTION-319](../questions.d/QUESTION-319.md) of organizations.
- **That a fixed subspace is a shared commitment.** It is a set of
  directions every loop leaves alone. Reading it as common ground or a
  shared value needs the directions to be validated as meaning that.
- **Anything new in mathematics.** It is H⁰ of the connection sheaf, which
  is the setting of [THEORY-1090](../theory.d/THEORY-1090.md)'s Hansen and Ghrist. It is filed because
  the record's own result is the U(1) case, and [CASE-179](../cases.d/CASE-179.md)'s higher-
  dimensional stalks need the general one.
